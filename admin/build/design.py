"""The redesign, as mockups for review: /admin/design/. Called by build.py with its namespace; writes five pages,
their markdown twins and their lines in llms.txt. Deterministic, standard library only, real data throughout.

The editor's brief (23 October 2026): use the width; less geeky, more professional and visual; a menu that is not a
mess; the reader's persona, and how much of the site they want to see, should change the layout and what is shown;
what a reader has seen gets out of the way; the team gets an admin console with its own menu and layout.
The brief is admin/content/briefs/2026-10-23__brief__the-redesign.md.
"""
import json, re
from collections import Counter, OrderedDict

# --------------------------------------------------------------------------- the two dials
# Who you are (the persona) and how much of the site you want (the view). A page group is shown in Focus to the
# personas listed, from Standard to everyone listed in standard ('*' = all), and in Everything to all.
VIEWS = [('focus', 'Focus', 'Only what your role needs: today, your briefing, what to do, ask.'),
         ('standard', 'Standard', 'The story and the evidence, organised by task.'),
         ('everything', 'Everything', 'Every page, the method, the data and the team console: power users and the team.')]
GROUPS = OrderedDict([
    ('today',    ('Today', 'front page, what is new, the phone app', ['*'], ['*'])),
    ('briefing', ('Your briefing', 'the briefing written for your role', ['*'], ['*'])),
    ('ask',      ('Ask', 'questions readers ask, the Sherpa', ['*'], ['*'])),
    ('explain',  ('Explained', 'plain-English explainer, glossary', ['everyone', 'site-owner', 'board', 'pm', 'cfo', 'comms'], ['*'])),
    ('act',      ('What to do', 'playbook, patching, affected systems, check your stack', ['site-owner', 'security', 'engineer', 'developer', 'appsec', 'cto', 'ciso'], ['*'])),
    ('incident', ('The incident', 'the flaws, timeline, discovery, leak, exploitation, impact, defence', ['security', 'journalist', 'researcher', 'analyst', 'ciso'], ['*'])),
    ('analysis', ('The analysis', 'claims, fact-check, numbers, agencies, who says what', ['journalist', 'analyst', 'comms', 'dpo'], ['decide', 'act', 'communicate', 'study'])),
    ('grc',      ('Risk and compliance', 'risk register, frameworks, stakeholders', ['dpo', 'ciso'], ['decide'])),
    ('code',     ('The code', 'the fix in php-src, the review graph', ['researcher', 'engineer', 'appsec'], ['act', 'study'])),
    ('stories',  ('Stories', 'signed articles written here', ['journalist', 'analyst'], ['*'])),
    ('evidence', ('The evidence', 'every source, the vaults, the pipeline, versions', ['researcher', 'journalist'], ['communicate', 'study'])),
    ('site',     ('The site and the team', 'method, roles, board, releases, admin', [], [])),
])

def group_of(path):
    p = path
    if p in ('index.html', 'whatsnew/index.html', 'summary/index.html') or p.startswith(('now/', 'you/', 'reader/', 'feeds/', 'subscribe/')): return 'today'
    if p.startswith(('briefings/', 'start/')): return 'briefing'
    if p.startswith(('questions/', 'sherpa/', 'interview/')): return 'ask'
    if p.startswith(('explained/', 'glossary/')): return 'explain'
    if p.startswith(('playbook/', 'patching/', 'affected/', 'stack/', 'check/')): return 'act'
    if p.startswith(('flaws/', 'timeline/', 'discovery/', 'leak/', 'exploitation/', 'compromise/', 'impact/', 'defence/', 'context/', 'signals/')): return 'incident'
    if p.startswith(('claims/', 'factcheck/', 'numbers/', 'agencies/', 'actors/', 'graph/', 'readings/')): return 'analysis'
    if p.startswith('grc/'): return 'grc'
    if p.startswith(('code/', 'review/')): return 'code'
    if p.startswith(('articles/',)): return 'stories'
    if p.startswith(('sources/', 'vaults/', 'layers/', 'pipeline/', 'versions/', 'facts/', 'admin/vault/')): return 'evidence'
    return 'site'

def level(gid, persona):
    """'f' shown in Focus, 's' from Standard, 'e' only in Everything."""
    _, _, focus, std = GROUPS[gid]
    if '*' in focus or persona['id'] in focus: return 'f'
    if '*' in std or persona['group'] in std or persona['id'] in std: return 's'
    return 'e'

def visible(by_group, persona, view):
    """Pages this reader sees in this view. In Focus the briefings shrink to their own briefing and the reader map."""
    n = 0
    for g in GROUPS:
        lv = level(g, persona)
        if view == 'everything' or lv == 'f' or (view == 'standard' and lv == 's'):
            n += 2 if (g == 'briefing' and view == 'focus') else by_group[g]
    return n

# --------------------------------------------------------------------------- helpers
def svg_spark(values, w=220, h=44, cls='var(--info)'):
    if not values: return ''
    mx = max(values) or 1
    step = w / max(1, len(values) - 1)
    pts = ' '.join(f'{i * step:.1f},{h - 4 - (v / mx) * (h - 8):.1f}' for i, v in enumerate(values))
    return f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" role="img" aria-label="trend"><polyline fill="none" stroke="{cls}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" points="{pts}"/></svg>'

def svg_donut(parts, size=168):
    """parts: list of (value, colour, label). A ring with the total in the middle."""
    tot = sum(v for v, _, _ in parts) or 1
    r, c = 62, 2 * 3.14159265 * 62
    off, segs = 0.0, ''
    for v, col, lab in parts:
        L = c * v / tot
        segs += f'<circle r="{r}" cx="84" cy="84" fill="none" stroke="{col}" stroke-width="22" stroke-dasharray="{L:.2f} {c - L:.2f}" stroke-dashoffset="{-off:.2f}" transform="rotate(-90 84 84)"><title>{v} {lab}</title></circle>'
        off += L
    return (f'<svg viewBox="0 0 168 168" width="{size}" height="{size}" role="img" aria-label="facts by status">{segs}'
            f'<text x="84" y="80" text-anchor="middle" font-size="30" font-weight="700" fill="currentColor">{tot}</text>'
            f'<text x="84" y="104" text-anchor="middle" font-size="12" fill="currentColor" opacity=".65">facts</text></svg>')

STATUS_COL = OrderedDict([('confirmed', 'var(--good)'), ('reported', 'var(--info)'), ('disputed', 'var(--warn)'), ('contradicted', '#d6a556'), ('unverified', 'var(--alert)')])

def build(ns):
    D, E, VERSION, STORY, PERSONAS, AUD = ns['D'], ns['E'], ns['VERSION'], ns['STORY'], ns['PERSONAS'], ns['AUD']
    NAV, PAGES, write, human_time, BASE_URL, SITE_NAME = ns['NAV'], ns['PAGES'], ns['write'], ns['human_time'], ns['BASE_URL'], ns['SITE_NAME']
    SOURCES, short_name = ns['SOURCES'], ns['short_name']
    when = human_time(STORY['data_as_of'])
    pl, im, claims = D['plain'], D['impact'], D['claims']
    st = Counter(c['status'] for c in claims)
    nav_pages = [p for _, items in NAV for p, _ in items]
    all_pages = [p for p, _, _, _ in PAGES]
    by_group = Counter(group_of(p) for p in all_pages)
    made = []

    def shell(path, title, desc, body, mock, persona=None, view=None, nav=None, console=False):
        """The page: the mockup banner, then the proposed top bar (or none, for the console), then the body."""
        up = '../' * path.count('/')
        banner = (f'<div class="mock-banner"><div class="shell"><span><b>Mockup {mock}</b> for review: a proposed design, built from the live data of release v{E(VERSION)}. '
                  f'Not the live site.</span><a href="{up}admin/design/index.html">All mockups and the design notes &rarr;</a></div></div>')
        top = ''
        if not console:
            p = PERSONAS[persona]
            links = ''.join(f'<a href="#"{" class=here" if i == 0 else ""}>{E(t)}{f"<span class=n>{n}</span>" if n else ""}</a>' for i, (t, n) in enumerate(nav or []))
            dial = ''.join(f'<span{" class=on" if v == view else ""}>{E(lab)}</span>' for v, lab, _ in VIEWS)
            top = (f'<header class="topbar"><div class="shell"><a class="logo" href="{up}index.html"><i>PHP</i>October<span>2026</span></a>'
                   f'<nav class="mainnav" aria-label="Main">{links}</nav>'
                   f'<div class="dials"><span class="who"><span class="av {E(p["group"])}">{E(p["person"][0])}</span>{E(p["person"])}, {E(p["label"])}</span>'
                   f'<span class="dial" aria-label="How much of the site">{dial}</span><a class="iconbtn" href="#">Ask</a></div></div></header>')
        html = f'''<!doctype html>
<html lang="en" data-root="{up}" data-path="{path}" data-ver="{VERSION}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)} &middot; {SITE_NAME}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="noindex">
<link rel="canonical" href="{BASE_URL}/{path}">
<link rel="icon" href="data:,">
<link rel="alternate" type="text/markdown" href="{up}{path[:-5]}.md">
<link rel="stylesheet" href="{up}assets/design/v2.css">
</head>
<body>
{banner}
{top}
{body}
</body>
</html>
'''
        PAGES.append((path, title, desc, 'site'))
        write(path, html)
        md = re.sub(r'<(script|style|svg).*?</\1>', '', body, flags=re.S)
        md = re.sub(r'<(h1|h2|h3)[^>]*>(.*?)</\1>', lambda m: '\n' + '#' * (int(m.group(1)[1]) + 1) + ' ' + re.sub(r'<[^>]+>', '', m.group(2)) + '\n', md, flags=re.S)
        md = re.sub(r'<li[^>]*>', '\n- ', md)
        md = re.sub(r'<(p|div|section|article|tr)[^>]*>', '\n', md)
        md = re.sub(r'<[^>]+>', ' ', md)
        md = re.sub(r'[ \t]+', ' ', md)
        md = re.sub(r'\n\s*\n+', '\n\n', md)
        import html as H
        write(path[:-5] + '.md', f'# {title}\n\n{desc}\n\n> Mockup {mock} for review, built from the data of release v{VERSION}. Not the live site.\n\n' + H.unescape(md).strip() + f'\n\n---\nsite v{VERSION} · {BASE_URL}/{path}\n')
        made.append((path, title, desc))

    # ======================================================================= mockup A: the board member, Focus
    board = PERSONAS['board']
    tiles = [
        ('good', 'A fix', 'Available', f'PHP {", ".join(D["affected"]["fixed"])}, since 21 Oct', None),
        ('alert', 'Severity', 'Critical', '9.2 out of 10, both flaws', None),
        ('good', 'Confirmed break-ins', 'None', 'no named organisation, as of the latest capture', None),
        ('warn', 'Taken offline', f'{len(im["offline"])} organisations', 'as a precaution, across 6 countries', None),
        ('info', 'Agencies compared', f'{len(D["agencies"])}', 'all say update; they split on offline', None),
    ]
    tl_days = Counter(t['at'][:10] for t in D['timeline'] if t['at'][:7] == '2026-10')
    days = sorted(tl_days)
    spark = svg_spark([tl_days[d] for d in days], cls='var(--alert)')
    kpis = ''.join(f'<div class="card kpi {c}"><div class="k">{E(k)}</div><div class="v">{E(v)}</div><div class="d">{E(d)}</div>{spark if k == "Agencies compared" and False else ""}</div>' for c, k, v, d, _ in tiles)
    decisions = [
        ('Are we exposed?', 'Ask for the list, not a percentage: every system that runs PHP, including vendor products and hosting panels, and which are on the internet.'),
        ('Is everything updated and restarted?', 'Updating is not enough until PHP is restarted. Ask for the running version, checked after the restart, system by system.'),
        ('Who can pull a system offline, and how fast?', 'Every agency puts offline last, but you need to be able to do it in minutes. Name the person and rehearse it once.'),
    ]
    dec = ''.join(f'<div class="decision"><div class="num">{i + 1}</div><div><h3>{E(t)}</h3><p>{E(x)}</p></div></div>' for i, (t, x) in enumerate(decisions))
    latest = ''.join(f'<li><span class="pill new">New</span> <span class="small">{E(x["when"])}</span><div class="t">{E(x["text"])}</div></li>' for x in pl['latest'][-3:])
    moments = ''.join(f'<div class="jst {"good" if m["tone"] == "ok" else "alert" if m["tone"] == "bad" else m["tone"] if m["tone"] in ("warn", "info") else ""}"><div class="w">{E(m["when"])}</div><div class="x">{E(m["what"])}</div></div>' for m in pl['moments'])
    stance = Counter()
    for a in D['agencies']:
        o = a['offline']
        stance['Take offline' if o == 'yes' else 'Isolate' if o.startswith('isolate') or o == 'restrict from abroad' else 'Offline after other steps' if o in ('after mitigations', 'consider') else 'No offline advice' if o == 'none' else 'Not readable'] += 1
    order = [('Take offline', 'var(--alert)'), ('Isolate', 'var(--warn)'), ('Offline after other steps', '#d6a556'), ('No offline advice', 'var(--info)'), ('Not readable', 'var(--line-2)')]
    sbar = ''.join(f'<div style="flex:{stance[k]};background:{c}" title="{stance[k]} {E(k)}"></div>' for k, c in order if stance[k])
    slegend = ''.join(f'<li><i style="background:{c}"></i>{stance[k]} {E(k.lower())}</li>' for k, c in order if stance[k])
    body = f'''
<section class="band"><div class="shell hero">
  <div><p class="eyebrow"><span class="live">Developing</span> &nbsp;&middot;&nbsp; last checked {E(when)}</p>
    <h1 class="display">{E(pl["headline"])}</h1>
    <p class="lede">{E(re.sub(r"<[^>]+>", "", pl["deck"]))}</p></div>
  <aside class="ans"><div class="who-line"><span class="av decide">{E(board["person"][0])}</span><div><b>Your answer in thirty seconds</b><div class="small" style="color:var(--band-muted)">for {E(board["person"])}, {E(board["label"].lower())}</div></div></div>
    <p>{E(board["answer"])}</p></aside>
</div></section>
<main class="shell">
  <section class="block"><div class="tiles">{kpis}</div></section>
  <section class="block"><div class="grid cols-12">
    <div class="card span-8" style="align-self:start"><div class="block-head"><h2 class="h2">Three questions to put to your team this week</h2><span class="small">from your briefing</span></div>{dec}</div>
    <div class="span-4 grid" style="align-content:start">
      <div class="card"><div class="block-head"><h2 class="h2">Since you last looked</h2><span class="pill">3 new</span></div><ul class="delta">{latest}</ul><p class="small" style="margin-bottom:0">Read items disappear from this list. <a href="#">Everything new &rarr;</a></p></div>
      <div class="card flat" style="background:var(--brand-soft);border-color:transparent"><h3>Ask about it</h3><p class="small" style="color:var(--ink-2)">"What should I tell the board on Thursday?" Answers cite the evidence.</p><a class="iconbtn" href="#">Ask a question</a></div>
    </div></div></section>
  <section class="block"><div class="grid cols-12">
    <div class="card span-7"><div class="block-head"><h2 class="h2">How it unfolded</h2><a class="small" href="#">The full timeline</a></div><div class="journey">{moments}</div></div>
    <div class="card span-5"><div class="block-head"><h2 class="h2">What governments advise</h2><span class="small">{len(D["agencies"])} agencies</span></div>
      <p style="margin:.2rem 0 .8rem;color:var(--ink-2)">All say install the fix. They split on what to do if you cannot.</p>
      <div style="display:flex;height:22px;border-radius:7px;overflow:hidden;gap:2px">{sbar}</div><ul class="legend">{slegend}</ul>
      <p class="small" style="margin-bottom:0"><a href="../c/index.html">See every agency &rarr;</a></p></div>
  </div></section>
  <footer class="foot">Focus view shows {visible(by_group, board, "focus")} of {len(all_pages)} pages for this reader. Switch to Standard for the story and the evidence, or Everything for the whole site. Every number here links to its saved source on the live site.</footer>
</main>'''
    shell('admin/design/a/index.html', 'Mockup A: the front page for a board member, Focus view', 'The front page for a board member who wants only what their role needs: the situation, five numbers, three questions for the team, what is new, and one picture each of how it unfolded and what governments advise.', body, 'A', 'board', 'focus',
          [('Today', 3), ('Your briefing', 0), ('What to ask', 0), ('Explained', 0)])

    # ======================================================================= mockup B: the security lead, Standard
    sam = PERSONAS['security']
    items = list(ns['all_items']().items())  # this build's items, not the file save_items() writes at the end of it (read from disk, it lagged one build: board 175)
    feed = [(k, v) for k, v in items if v['kind'] in ('fact', 'event', 'question', 'story', 'front')]
    feed.sort(key=lambda kv: (kv[1].get('date') or '', kv[1]['changed'], kv[0]), reverse=True)
    feed = feed[:9]
    def fitem(k, v, i):
        c = next((c for c in claims if 'fact-' + c['id'] == k), None)
        status = c['status'] if c else ''
        col = {'confirmed': 'good', 'reported': 'info', 'disputed': 'warn', 'contradicted': 'warn', 'unverified': 'alert'}.get(status, '')
        text = c['claim'] if c else v['title']
        srcs = ''.join(f'<span class="chip">{E(short_name(SOURCES[s]))}</span>' for s in (c['sources'] if c else [])[:4] if s in SOURCES)
        spill = f'<span class="pill {col}">{E(status)}</span>' if status else ''
        return (f'<article class="card fitem"><div><div class="meta"><span class="pill {"new" if i < 4 else "warn"}">{"New" if i < 4 else "Changed"}</span>'
                f'<span class="pill">{E(v["kind"])}</span>{spill}<span class="small">v{E(v["changed"])}</span></div>'
                f'<h3>{E(text[:180])}</h3>{f"<div class=chips>{srcs}</div>" if srcs else ""}</div><div class="check" title="Mark read">&#10003;</div></article>')
    feedhtml = ''.join(fitem(k, v, i) for i, (k, v) in enumerate(feed))
    steps = [('Patch internet-facing first', 'mod_php, then FPM, then the rest. Restart every worker; rebuild every image.'),
             ('Bound the known paths', 'session.upload_progress off, low post_max_size, fatal_error_backtraces off on 8.5. None of these is a fix.'),
             ('Watch the process tree', 'Alert on a PHP worker spawning a shell or a downloader. A clean access log proves nothing.')]
    actions = ''.join(f'<div class="card action"><div class="n">{i + 1}</div><div><h3>{E(t)}</h3><p>{E(x)}</p></div></div>' for i, (t, x) in enumerate(steps))
    donut = svg_donut([(st[k], c, k) for k, c in STATUS_COL.items() if st[k]])
    dleg = ''.join(f'<li><i style="background:{c}"></i>{st[k]} {E(k)}</li>' for k, c in STATUS_COL.items() if st[k])
    dmax = max(tl_days.values()) if tl_days else 1
    bars = ''.join(f'<div class="{"hot" if d >= "2026-10-20" else ""}" style="height:{max(3, round(100 * tl_days[d] / dmax))}%" title="{tl_days[d]} events on {d}"></div>' for d in days)
    blabels = ''.join(f'<span>{E(d[8:])}</span>' for d in days)
    ex = ''.join(f'<li><span class="small">{E(x["when"])}</span><div class="t" style="font-size:.9rem">{E(x["who"].split("(")[0].strip())}: {E(x["what"][:90])}</div></li>' for x in D['exploitation'][:4])
    groups_nav = [('Today', '9 new'), ('What to do', ''), ('The incident', ''), ('Detection and defence', ''), ('The agencies', '16'), ('Every claim', f'{len(claims)}'), ('Ask', '')]
    rnav = ''.join(f'<a href="#"{" class=here" if i == 0 else ""}>{E(t)}<span>{E(n)}</span></a>' for i, (t, n) in enumerate(groups_nav))
    path_done = 2
    body = f'''
<main class="shell app">
  <aside class="rail">
    <div class="card"><div style="display:flex;gap:.7rem;align-items:center"><span class="av act" style="width:42px;height:42px">{E(sam["person"][0])}</span><div><b>{E(sam["person"])}</b><div class="small">{E(sam["label"])}</div></div></div>
      <p class="small" style="margin:.7rem 0 .4rem">Your reading path</p><div class="progress"><b style="width:{round(100 * path_done / len(sam["path"]))}%"></b></div><p class="small" style="margin:.4rem 0 0">{path_done} of {len(sam["path"])} read &middot; next: Exploitation signals</p></div>
    <nav class="railnav card flat" style="padding:.4rem">{rnav}</nav>
  </aside>
  <div>
    <p class="eyebrow">Since your last visit &middot; {E(when)}</p>
    <h1 class="display" style="font-size:clamp(1.7rem,2.6vw,2.6rem);margin:.3rem 0 .4rem">9 things are new, 3 changed. Two matter for your runbook.</h1>
    <p class="lede" style="margin:0 0 1.2rem">{E(sam["answer"])}</p>
    <section><div class="block-head"><h2 class="h2">Your next three actions</h2><a class="small" href="#">The whole playbook</a></div><div class="actions">{actions}</div></section>
    <section class="feed"><div class="block-head" style="margin-top:1.6rem"><h2 class="h2">What changed</h2><div class="chips"><span class="chip" style="background:var(--ink);color:var(--surface)">All</span><span class="chip">Facts</span><span class="chip">Timeline</span><span class="chip">Questions</span><span class="chip">Stories</span></div></div>{feedhtml}
      <p class="small">Marked read, an item fades and then leaves this list; it comes back only if what it says changes.</p></section>
  </div>
  <aside class="rail right">
    <div class="card"><h3>How sure are we?</h3><div style="display:flex;gap:1rem;align-items:center;flex-wrap:wrap">{donut}<ul class="legend" style="flex-direction:column">{dleg}</ul></div></div>
    <div class="card"><h3>Events per day, October</h3><div class="bars">{bars}</div><div class="bars-l">{blabels}</div><p class="small" style="margin:.5rem 0 0">Red: from the leak on 20 October.</p></div>
    <div class="card"><h3>Exploitation signals</h3><ul class="delta">{ex}</ul><p class="small" style="margin:0"><span class="pill good">0</span> confirmed compromises</p></div>
    <div class="card"><h3>Fixed in</h3><div class="chips">{"".join(f"<span class=chip style='font-family:var(--mono)'>{E(v)}</span>" for v in D["affected"]["fixed"])}</div><p class="small" style="margin:.5rem 0 0">8.1 and older: source backports only.</p></div>
  </aside>
</main>'''
    shell('admin/design/b/index.html', 'Mockup B: the front page for a security lead, Standard view', 'A three-column working view for a security lead: their reading path and the site by task on the left, what changed since the last visit and the next three actions in the middle, and the state of the evidence as charts on the right.', body, 'B', 'security', 'standard',
          [('Today', 9), ('What to do', 0), ('The incident', 0), ('The evidence', 0), ('Your briefing', 0)])

    # ======================================================================= mockup C: a content page, the agencies
    BUCKETS = [('none', 'No offline advice', 'var(--info)'), ('consider', 'Consider it, or after other steps', '#d6a556'), ('restrict', 'Restrict access', 'var(--warn)'),
               ('isolate', 'Isolate from the internet', 'var(--warn)'), ('yes', 'Take it offline', 'var(--alert)')]
    def bucket(o): return 'yes' if o == 'yes' else 'isolate' if o.startswith('isolate') else 'restrict' if o == 'restrict from abroad' else 'consider' if o in ('after mitigations', 'consider') else 'none' if o == 'none' else None
    cols = ''.join(f'<div class="bk"><div class="bk-h" style="border-top-color:{c}"><b>{sum(1 for a in D["agencies"] if bucket(a["offline"]) == k)}</b> {E(lab)}</div><div class="chips">' + ''.join(f'<span class="chip"><b style="font-family:var(--mono);font-weight:600">{E(a["country"].split()[0])}</b> {E(a["agency"].split(" (")[0])}</span>' for a in D['agencies'] if bucket(a['offline']) == k) + '</div></div>' for k, lab, c in BUCKETS)
    unread = [a for a in D['agencies'] if bucket(a['offline']) is None]
    dots = f'<div class="buckets">{cols}</div>' + (f'<p class="small" style="margin:.8rem 0 0">Not readable from this capture environment: {", ".join(E(a["agency"]) for a in unread)}.</p>' if unread else '')
    def scls(o): return 's-yes' if o == 'yes' else 's-isolate' if o.startswith('isolate') or o == 'restrict from abroad' else 's-consider' if o in ('after mitigations', 'consider') else 's-none' if o == 'none' else 's-unknown'
    def slab(o): return {'yes': 'Take offline', 'none': 'No offline advice', 'unknown': 'Could not be read'}.get(o, o[0].upper() + o[1:])
    cards = ''.join(f'''<article class="card agency {scls(a["offline"])}"><div style="display:flex;justify-content:space-between;gap:.5rem"><h3 style="margin:0">{E(a["agency"])}</h3><span class="cc">{E(a["country"])}</span></div>
<span class="pill {"alert" if a["offline"] == "yes" else "warn" if scls(a["offline"]) in ("s-isolate", "s-consider") else "info" if a["offline"] == "none" else ""}">{E(slab(a["offline"]))}</span>
{f"<q>{E(a['offline_text'][:170])}</q>" if a.get("offline_text") and a["offline"] not in ("none", "unknown") else f"<p class=small style='margin:0'>{E((a.get('note') or '')[:150])}</p>"}
<div class="chips">{"".join(f"<span class=chip>{E(short_name(SOURCES[s]))}</span>" for s in a["sources"][:2] if s in SOURCES)}</div></article>''' for a in D['agencies'])
    body = f'''
<section class="band"><div class="shell hero" style="grid-template-columns:minmax(0,1.3fr) minmax(300px,1fr)">
  <div><p class="eyebrow">The analysis &middot; government advice</p><h1 class="display">{len(D["agencies"])} agencies. All say update. They split on offline.</h1>
  <p class="lede">The question that divides them is not whether to patch but what to do with a system you cannot patch today. Read left to right: from no offline advice to take it offline.</p></div>
  <div class="ans"><p class="eyebrow" style="margin:0 0 .4rem">In one line</p><p style="font-size:1.15rem">The US says take it offline. The UK says that is the fourth step. Europe says isolate. Australia, Japan and the Netherlands say nothing about it.</p></div>
</div></section>
<main class="shell">
  <section class="block"><div class="card"><div class="block-head"><h2 class="h2">The spectrum</h2><span class="small">every agency, by what it says to do with a system you cannot patch</span></div>
    <div class="rail-g"></div>{dots}</div></section>
  <section class="block"><div class="block-head"><h2 class="h2">Agency by agency</h2><div class="chips"><span class="chip" style="background:var(--ink);color:var(--surface)">All {len(D["agencies"])}</span><span class="chip">Take offline</span><span class="chip">Isolate</span><span class="chip">No offline advice</span></div></div>
    <div class="tiles" style="grid-template-columns:repeat(auto-fill,minmax(270px,1fr))">{cards}</div></section>
  <section class="block"><details class="card flat"><summary class="h2" style="cursor:pointer">The evidence table: every agency's words, dates and sources</summary><p class="small">On the live site this is the full table, one row per agency with the verbatim sentence, the publication time and every saved source.</p></details></section>
  <footer class="foot">A wall of text becomes three layers: the one-line answer, the picture, and the cards; the evidence table is one click away, not the first thing you see.</footer>
</main>'''
    shell('admin/design/c/index.html', 'Mockup C: a content page, what sixteen agencies advise', 'The agencies page redesigned: the answer in one line, every agency placed on one spectrum from no offline advice to take it offline, a card per agency, and the evidence table one click away.', body, 'C', 'ciso', 'standard',
          [('Today', 0), ('What to do', 0), ('The incident', 0), ('The evidence', 0), ('Your briefing', 0)])

    # ======================================================================= mockup D: the admin console
    A = D['admin']
    bstat = Counter(b['status'] for b in A['board'])
    def tickets(status, n=7):
        rows = [b for b in A['board'] if b['status'] == status][-n:][::-1]
        return ''.join(f'<div class="ticket"><span class="id">#{E(b["id"])}</span><div>{E(b["title"][:120])}{"…" if len(b["title"]) > 120 else ""}</div><div class="o"><span>{E(b["owner"])}</span>{("<span>v" + E(b["version"]) + "</span>") if b.get("version") else ""}</div></div>' for b in rows)
    rel = D['versions']['versions'][:8]
    rels = ''.join(f'<tr><td style="font-family:var(--mono);white-space:nowrap">v{E(r["version"])}</td><td class="small" style="white-space:nowrap">{E(r["date"])}</td><td>{E(r["title"][:130])}{"…" if len(r["title"]) > 130 else ""}</td></tr>' for r in rel)
    roles = ''.join(f'<tr><td><b>{E(r["name"])}</b></td><td class="small">{E(r["owns"][:120])}</td><td style="text-align:right">{sum(1 for b in A["board"] if b["owner"] == r["id"] and b["status"] == "open")}</td></tr>' for r in A['roles'][:9])
    side = [('Console', [('Overview', '', True), ('Board', str(bstat['open']), False), ('Agents', str(len(A['roles'])), False), ('Releases', str(len(D['versions']['versions'])), False), ('Pipeline', '', False)]),
            ('Editorial', [('Briefs', '', False), ('Fact-check queue', '', False), ('Corrections', '', False), ('Readers and feedback', '', False)]),
            ('Systems', [('Vaults and keys', str(len(D['vaults']['vaults'])), False), ('Telemetry', '', False), ('Synthetic readers', '', False), ('Design', '5', False)])]
    sidehtml = ''.join(f'<h4>{E(g)}</h4>' + ''.join(f'<a href="#"{" class=here" if h else ""}>{E(t)}{f"<span>{E(n)}</span>" if n else ""}</a>' for t, n, h in items) for g, items in side)
    kp = [('info', 'Release', f'v{VERSION}', f'{len(D["versions"]["versions"])} releases since 22 Oct'), ('warn', 'Open on the board', str(bstat['open']), f'{bstat["done"]} done, {bstat.get("waiting", 0)} waiting'),
          ('good', 'Pages built', str(len(all_pages)), 'every one with a markdown twin'), ('info', 'Sources in the vault', str(len(D['sources'])), f'{sum(1 for s in D["sources"] if s.get("status") == "captured")} captured')]
    kpis = ''.join(f'<div class="card kpi {c}"><div class="k">{E(k)}</div><div class="v">{E(v)}</div><div class="d">{E(d)}</div></div>' for c, k, v, d in kp)
    body = f'''
<div class="console">
  <nav class="side" aria-label="Console"><a class="logo" href="../../../index.html"><i>PHP</i>Team console</a>{sidehtml}
    <h4>Reader site</h4><a href="../a/index.html">Back to the reader site</a></nav>
  <main class="cmain">
    <div class="block-head"><div><p class="eyebrow">Team console &middot; public, like everything here</p><h1 class="display" style="font-size:clamp(1.6rem,2.4vw,2.4rem)">Overview</h1></div><span class="small">built {E(when)}</span></div>
    <div class="tiles" style="margin-bottom:1.4rem">{kpis}</div>
    <div class="block-head"><h2 class="h2">The board</h2><span class="small">newest first in each lane</span></div>
    <div class="kanban">
      <div class="lane"><h3>Open <span>{bstat["open"]}</span></h3>{tickets("open")}</div>
      <div class="lane"><h3>Waiting <span>{bstat.get("waiting", 0)}</span></h3>{tickets("waiting")}</div>
      <div class="lane"><h3>Done <span>{bstat["done"]}</span></h3>{tickets("done")}</div>
    </div>
    <div class="grid cols-12" style="margin-top:1.6rem">
      <div class="card span-7"><div class="block-head"><h2 class="h2">Releases</h2><span class="small">latest 8</span></div><div class="tw"><table class="tbl">{rels}</table></div></div>
      <div class="card span-5"><div class="block-head"><h2 class="h2">Agents and what they own</h2><span class="small">open items</span></div><div class="tw"><table class="tbl">{roles}</table></div></div>
    </div>
  </main>
</div>'''
    shell('admin/design/d/index.html', 'Mockup D: the team console', 'The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.', body, 'D', console=True)

    # ======================================================================= the hub: the design notes
    pgroups = OrderedDict((g['id'], g) for g in D['personas']['groups'])
    reps = ['everyone', 'board', 'cfo', 'ciso', 'journalist', 'security', 'engineer', 'researcher']
    head = ''.join(f'<th><span class="av {E(PERSONAS[r]["group"])}" style="width:26px;height:26px;font-size:.75rem" title="{E(PERSONAS[r]["label"])}">{E(PERSONAS[r]["person"][0])}</span><div class="small">{E(PERSONAS[r]["label"].split(" or ")[0])}</div></th>' for r in reps)
    rows = ''.join(f'<tr><td><b>{E(lab)}</b><div class="small">{E(what)} &middot; {by_group[g]} pages</div></td>' + ''.join(f'<td><span class="dot-v {level(g, PERSONAS[r])}" title="{ {"f": "Focus", "s": "Standard", "e": "Everything"}[level(g, PERSONAS[r])] }"></span></td>' for r in reps) + '</tr>' for g, (lab, what, _, _) in GROUPS.items())
    counts = ''.join(f'<tr><td><b>{E(PERSONAS[r]["person"])}</b> <span class="small">{E(PERSONAS[r]["label"])}</span></td>' + ''.join(f'<td>{visible(by_group, PERSONAS[r], v)}</td>' for v, _, _ in VIEWS) + '</tr>' for r in reps)
    menus = ''.join(f'<div class="card"><p class="eyebrow">{E(lab)}</p><p style="margin:.3rem 0 .6rem">{E(txt)}</p><div class="chips">' + ''.join(f'<span class="chip">{E(x)}</span>' for x in m) + '</div></div>' for lab, txt, m in [
        ('Focus', 'Four places. For a board member, a CFO, a website owner.', ['Today', 'Your briefing', 'What to ask', 'Explained']),
        ('Standard', 'The site by task, not by where the data came from.', ['Today', 'What to do', 'The incident', 'The evidence', 'Your briefing', 'Ask']),
        ('Everything', 'All of it, for power users and the team.', ['Today', 'What to do', 'The incident', 'The evidence', 'Risk and compliance', 'Stories', 'Method and data', 'Team console'])])
    problems = [('It reads as a wall of text', 'Long paragraphs and tables first; the picture, if any, comes last. Mockup C turns the agencies page into answer, picture, cards, then the table.'),
                ('It does not use the screen', 'Pages stop at 1,080 pixels; on a laptop half the screen is empty. The proposal runs to 1,680 with two or three columns that stack on a phone.'),
                ('The menu is the site map', f'Eleven groups and {len(nav_pages)} entries, ordered by how the site was built, not by what a reader wants to do. The proposal: four to eight entries, chosen by who you are and how much you want.'),
                ('Everyone sees everything', 'A board member meets the vault, the board and the billing model on the way to their answer. The proposal: two dials, who you are and how much of the site you see.'),
                ('Read things stay in the way', 'The delta strip is right, but read items still fill the pages. The proposal: read items fade, then leave; they return only when they change.'),
                ('The team lives in the reader site', 'The board, roles, keys and telemetry sit in the reader menu. The proposal: a console with its own menu and layout, still public.')]
    prob = ''.join(f'<div class="card"><h3>{E(t)}</h3><p class="small" style="color:var(--ink-2);margin:0">{E(x)}</p></div>' for t, x in problems)
    thumbs = ''.join(f'<a class="thumb" href="{k}/index.html"><img src="../../assets/design/{k}.png" alt="Mockup {k.upper()}" loading="lazy" width="1600" height="1000"><h3>{E(t)}</h3><p class="small">{E(x)}</p></a>' for k, t, x in [
        ('a', 'A. Front page: board member, Focus', 'The situation on a dark band, five numbers, three questions for the team, what is new, two pictures.'),
        ('b', 'B. Front page: security lead, Standard', 'Three columns: reading path and tasks; what changed and the next three actions; the evidence as charts.'),
        ('c', 'C. A content page: the agencies', 'Answer in one line, every agency on one spectrum, a card each, the evidence table one click away.'),
        ('d', 'D. The team console', 'Its own menu and layout: board as lanes, releases, agents and what they own.')])
    body = f'''
<section class="band"><div class="shell hero" style="grid-template-columns:minmax(0,1.4fr) minmax(300px,1fr)">
  <div><p class="eyebrow">Admin &middot; design &middot; for review</p><h1 class="display">The redesign: who you are, and how much you want to see</h1>
  <p class="lede">The editor's review of 23 October: the site is right in substance and wrong in form. Too geeky, too much text, a menu that is a site map, and half the screen unused. Four mockups, built from the live data, and the model behind them.</p></div>
  <div class="ans"><p class="eyebrow" style="margin:0 0 .4rem">The model, in one line</p><p style="font-size:1.12rem">Two dials. <b>Who you are</b> sets the layout and the order. <b>How much you want</b> (Focus, Standard, Everything) sets which pages exist for you at all. What you have read gets out of the way.</p></div>
</div></section>
<main class="shell">
  <section class="block"><div class="block-head"><h2 class="h2">The four mockups</h2><span class="small">each is a real page, at full width; resize it to see it stack</span></div><div class="thumbs">{thumbs}</div></section>
  <section class="block"><div class="block-head"><h2 class="h2">What is wrong now</h2></div><div class="tiles" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr))">{prob}</div></section>
  <section class="block"><div class="grid cols-12">
    <div class="card span-7"><div class="block-head"><h2 class="h2">Which pages each reader sees</h2><span class="small">a dark square is in Focus; mid is from Standard; light is only in Everything</span></div><div class="tw"><table class="tbl matrix"><thead><tr><th>Part of the site</th>{head}</tr></thead><tbody>{rows}</tbody></table></div></div>
    <div class="span-5 grid" style="align-content:start">
      <div class="card"><div class="block-head"><h2 class="h2">Pages per reader, per view</h2></div><div class="tw"><table class="tbl matrix"><thead><tr><th>Reader</th>{"".join(f"<th>{E(l)}</th>" for _, l, _ in VIEWS)}</tr></thead><tbody>{counts}</tbody></table></div><p class="small" style="margin-bottom:0">Counted from the {len(all_pages)} pages this release builds.</p></div>
      <div class="card"><h3>Who sees the team console</h3><p class="small" style="color:var(--ink-2);margin:0">Everything view only. It stays public, because how the site is run is part of the story; it just stops being in a reader's way.</p></div>
    </div></div></section>
  <section class="block"><div class="block-head"><h2 class="h2">The menu, per view</h2><span class="small">today: 11 groups, {len(nav_pages)} entries, the same for everyone</span></div><div class="tiles">{menus}</div></section>
  <section class="block"><div class="grid cols-12">
    <div class="card span-6"><h2 class="h2" style="margin-bottom:.6rem">Design principles</h2><ol style="margin:0;padding-left:1.2rem;color:var(--ink-2)">
      <li><b>Use the screen.</b> Up to 1,680 pixels, two or three columns on a laptop, one on a phone; text columns stay readable at 60 to 75 characters.</li>
      <li><b>Answer, picture, detail.</b> Every page opens with its answer in one line, then a picture, then the cards; tables and evidence one click down.</li>
      <li><b>Quiet colour, loud only for status.</b> Ink and paper; red, amber, green and blue only where they mean confirmed, warning, risk or information.</li>
      <li><b>The reader chooses who and how much.</b> Two dials in the top bar, remembered in the browser and in their vault.</li>
      <li><b>Seen things get out of the way.</b> Read items fade, then leave; they return only when they change.</li>
      <li><b>The team has a console.</b> Its own menu and layout, public, out of the reader's path.</li></ol></div>
    <div class="card span-6"><h2 class="h2" style="margin-bottom:.6rem">How to roll it out</h2><ol style="margin:0;padding-left:1.2rem;color:var(--ink-2)">
      <li>The editor picks from these mockups and marks them up; this page records the decisions.</li>
      <li>The design tokens and the wide grid go into the live stylesheet; every page widens at once.</li>
      <li>The top bar with the two dials replaces the menu; the view decides which entries exist.</li>
      <li>The front page and the briefings move to layouts A and B, per persona group.</li>
      <li>Content pages follow pattern C, starting with the agencies, the numbers and the impact.</li>
      <li>The admin pages move into console D.</li></ol></div>
  </div></section>
  <footer class="foot">Mockups built by the design agent from release v{E(VERSION)}; the brief is on the briefs page. Board items record each step.</footer>
</main>'''
    shell('admin/design/index.html', 'Design: the redesign, in four mockups', 'The proposed redesign of the site for review: what is wrong now, the two dials (who you are and how much you see), which pages each reader sees, the menu per view, and four mockups built from the live data.', body, 'notes', 'board', 'everything',
          [('Today', 0), ('What to do', 0), ('The incident', 0), ('The evidence', 0), ('Team console', 0)])
    return made

def llms_lines(made, BASE_URL):
    out = ['', '## Design: the redesign, in mockups (for review)']
    out += [f'- [{t}]({BASE_URL}/{p[:-5]}.md): {d}' for p, t, d in made]
    return '\n'.join(out) + '\n'


# =========================================================================== v0.12: the redesign, live
# The editor, 24 October: "A, B and C are three different audiences ... implement all of them; D is for everybody,
# the team." Each persona belongs to a track (data/personas.json): A Briefing (the front page), B Operations (/ops/),
# C Analysis (/analysis/). The menu is by task, and the two dials (who you are, how much you see) decide what of it a
# reader sees, in their browser (assets/design/dials.js). The admin pages sit in the console (layout D).

TRACK_HOME = {'a': 'index.html', 'b': 'ops/index.html', 'c': 'analysis/index.html'}
MENU = [('Today', ['today']), ('For you', ['briefing', 'explain', 'ask']), ('What to do', ['act']), ('The incident', ['incident', 'code']),
        ('The evidence', ['analysis', 'evidence']), ('Risk and compliance', ['grc']), ('Stories', ['stories']), ('About', ['site'])]

def scope_css(css, sc='.v2'):
    """Every rule of v2.css under one class, so the redesign's names cannot reach the rest of the site."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    out, i, n = [], 0, len(css)
    def sel(s):
        s = s.strip()
        if s in (':root', 'body', 'html'): return sc
        if s == '*': return sc + ', ' + sc + ' *'
        return sc + ' ' + s
    def block(start):
        """Read rules from start until the matching close brace; return (text, end)."""
        res, j = [], start
        while j < n:
            while j < n and css[j] in ' \n\t\r': j += 1
            if j >= n or css[j] == '}': return ''.join(res), j + 1
            k = css.index('{', j); pre = css[j:k].strip()
            if pre.startswith('@media'):
                inner, j = block(k + 1); res.append(pre + '{' + inner + '}\n')
            elif pre.startswith('@keyframes'):
                depth, m = 1, k + 1
                while depth: depth += {'{': 1, '}': -1}.get(css[m], 0); m += 1
                res.append(css[j:m] + '\n'); j = m
            else:
                e = css.index('}', k); body = css[k + 1:e]; j = e + 1
                if pre == 'html' and 'text-size-adjust' in body: continue
                res.append(', '.join(sel(s) for s in pre.split(',')) + '{' + body + '}\n')
        return ''.join(res), j
    text, _ = block(0)
    return text

LIVE_CSS = """
/* the live layer: wider pages with readable text, the task menu and its dials, the full-bleed band, the console */
nav.site .row,footer.site .row{max-width:1680px}
main{max-width:1440px}
main > p,main > ul,main > ol,main section > p,main section > ul,main section > ol,main .lead,main .deck{max-width:82ch}
html[data-track-home] main{max-width:1680px}
.v2 .band{margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw)}
.v2 .band > .shell{max-width:1680px}
.v2 > .shell,.v2 .wrap{max-width:none;padding-left:0;padding-right:0}
.dials-live{display:flex;align-items:center;gap:.45rem;flex-wrap:wrap;font-size:.8rem}
.dials-live select{font:inherit;font-size:.8rem;border:1px solid var(--line2,#cfccc2);border-radius:999px;padding:.25rem .6rem;background:var(--panel,#fff);color:inherit;max-width:14rem}
.dials-live .dl-view{display:inline-flex;border:1px solid var(--line2,#cfccc2);border-radius:999px;padding:2px;background:var(--panel,#fff)}
.dials-live .dl-view button{border:0;background:none;font:inherit;font-size:.76rem;font-weight:600;padding:.2rem .6rem;border-radius:999px;cursor:pointer;color:inherit;opacity:.7}
.dials-live .dl-view button.on{background:var(--fg,#1b1b1a);color:var(--bg,#fff);opacity:1}
.dials-live .dl-home{font-weight:600;white-space:nowrap}
[data-g].dl-hide{display:none!important}
nav.site .tools{flex-wrap:wrap;max-width:100%;min-width:0}
@media (max-width:760px){.dials-live{width:100%}.dials-live select{flex:1;max-width:none;min-width:0}}
.ni.dl-hide{display:none!important}
.console-live{display:grid;grid-template-columns:250px minmax(0,1fr);gap:clamp(1rem,2vw,2rem);align-items:start}
.console-live > .side{position:sticky;top:5rem;height:auto;max-height:calc(100vh - 6rem);border-radius:14px}
.console-live > .cmain{min-width:0}
@media (max-width:900px){.console-live{grid-template-columns:1fr}.console-live > .side{position:static;max-height:none}}
"""

def write_live_css(ns):
    src = open(ns['os'].path.join(ns['ROOT'], 'assets', 'design', 'v2.css'), encoding='utf-8').read()
    ns['write']('assets/design/v2-live.css', '/* Generated by admin/build/design.py from assets/design/v2.css: every rule scoped under .v2, then the live layer. Do not edit. */\n' + scope_css(src) + LIVE_CSS)

def track_of(pid, PERSONAS):
    return (PERSONAS.get(pid) or {}).get('track', 'a')

def menu_html(ns, path, up):
    """The task menu: every NAV page, regrouped by what a reader wants to do, each entry tagged with its part of the site."""
    E, U, NAV = ns['E'], ns['U'], ns['NAV']
    seen, groups = set(), OrderedDict((label, []) for label, _ in MENU)
    where = {g: label for label, gs in MENU for g in gs}
    extra = [('ops/index.html', 'Operations view: patch and defend'), ('analysis/index.html', 'Analysis view: weigh the evidence')]
    for p, t in [(p, t) for _, items in NAV for p, t in items] + extra:
        if p in seen: continue
        seen.add(p)
        g = group_of(p)
        if p.startswith('admin/') and not p.startswith('admin/design/'): g = 'site'
        groups[where.get(g, 'About')].append((p, t, g))
    out = []
    for label, items in groups.items():
        if not items: continue
        active = any(p == path for p, _, _ in items)
        subs = ''.join(f'<a class="sl{" here" if p == path else ""}" href="{up}{U(p)}" data-g="{E(g)}">{E(t)}</a>' for p, t, g in items)
        gs = ' '.join(sorted({g for _, _, g in items}))
        out.append(f'<div class="ni" data-gs="{E(gs)}"><a class="nl{" here" if active else ""}" href="{up}{U(items[0][0])}">{E(label)}<span class="caret">&#9662;</span></a><div class="sub">{subs}</div></div>')
    return ''.join(out)

def dials_html(ns, up):
    E, J, PERSONAS = ns['E'], ns['J'], ns['PERSONAS']
    cfg = {'groups': {g: [f, s] for g, (_, _, f, s) in GROUPS.items()},
           'personas': {pid: {'group': p['group'], 'track': p.get('track', 'a'), 'depth': p['depth'], 'person': p['person'], 'label': p['label']} for pid, p in PERSONAS.items()},
           'homes': TRACK_HOME, 'tracks': {k: v['label'] for k, v in ns['D']['personas'].get('tracks', {}).items()}}
    opts = ''.join(f'<option value="{E(pid)}">{E(p["label"])}</option>' for pid, p in PERSONAS.items())
    return (f'<div class="dials-live" aria-label="Who you are, and how much of the site you see">'
            f'<select class="dl-who" aria-label="Who are you?"><option value="">Who are you?</option>{opts}</select>'
            f'<span class="dl-view" role="group" aria-label="How much of the site"><button type="button" data-v="focus">Focus</button><button type="button" data-v="standard">Standard</button><button type="button" data-v="everything">Everything</button></span>'
            f'<a class="dl-home" href="{up}index.html" hidden>Your home</a></div>'
            f'<script type="application/json" id="p2s-dials">{J(cfg)}</script>')

DIALS_JS = r"""// php.oct.2026.newsroom.sgit.ai: the two dials, who you are and how much of the site you see. Generated by
// admin/build/design.py. Kept in this browser only (p2s.persona, shared with the rest of the site, and p2s.view).
(function () {
  'use strict';
  var cfgEl = document.getElementById('p2s-dials'); if (!cfgEl) return;
  var C = JSON.parse(cfgEl.textContent), html = document.documentElement, up = html.getAttribute('data-root') || '', here = html.getAttribute('data-path') || '';
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
  function persona() { var id = get('p2s.persona'); return id && C.personas[id] ? id : null; }
  function view() { var v = get('p2s.view'); if (v === 'focus' || v === 'standard' || v === 'everything') return v; var p = persona(); if (!p) return 'everything'; var P = C.personas[p]; return (P.depth === 1 || P.group === 'understand') ? 'focus' : 'standard'; }
  function level(g, pid) {
    var r = C.groups[g]; if (!r) return 'e'; var P = C.personas[pid];
    if (r[0].indexOf('*') >= 0 || r[0].indexOf(pid) >= 0) return 'f';
    if (r[1].indexOf('*') >= 0 || r[1].indexOf(P.group) >= 0 || r[1].indexOf(pid) >= 0) return 's';
    return 'e';
  }
  function shows(g, pid, v) { if (v === 'everything' || !pid) return true; var l = level(g, pid); return l === 'f' || (v === 'standard' && l === 's'); }
  function apply() {
    var pid = persona(), v = view();
    html.setAttribute('data-view', v); if (pid) html.setAttribute('data-persona', pid); else html.removeAttribute('data-persona');
    document.querySelectorAll('[data-g]').forEach(function (a) { a.classList.toggle('dl-hide', !shows(a.getAttribute('data-g'), pid, v)); });
    document.querySelectorAll('.ni[data-gs]').forEach(function (ni) { ni.classList.toggle('dl-hide', !ni.querySelector('[data-g]:not(.dl-hide)')); });
    document.querySelectorAll('.dl-who').forEach(function (s) { s.value = pid || ''; });
    document.querySelectorAll('.dl-view button').forEach(function (b) { b.classList.toggle('on', b.getAttribute('data-v') === v); });
    var home = pid ? C.homes[C.personas[pid].track] : null;
    document.querySelectorAll('.dl-home').forEach(function (a) { if (home && home !== here) { a.hidden = false; a.href = up + home; a.textContent = (C.tracks[C.personas[pid].track] || 'Your') + ' home'; } else a.hidden = true; });
    var P = pid ? C.personas[pid] : null;
    document.querySelectorAll('[data-answer-for]').forEach(function (box) {
      var src = document.getElementById('p2s-answers'); if (!src) return; var A = JSON.parse(src.textContent), a = A[pid] || A[box.getAttribute('data-answer-for')];
      if (!a) return; var w = box.querySelector('[data-a-who]'), t = box.querySelector('[data-a-text]'), av = box.querySelector('[data-a-av]');
      if (w) w.textContent = 'for ' + a.person + ', ' + a.label.toLowerCase(); if (t) t.textContent = a.answer; if (av) { av.textContent = a.person.charAt(0); av.className = 'av ' + a.group; }
    });
  }
  // the front page sends a reader who said who they are to their track's home, once per visit; ?home stays here
  (function () {
    var pid = persona(); if (!pid || here !== 'index.html' || /[?&]home\b/.test(location.search)) return;
    var t = C.personas[pid].track, home = C.homes[t];
    var seen = null; try { seen = sessionStorage.getItem('p2s.routed'); } catch (e) {}
    if (t !== 'a' && home && !seen) { try { sessionStorage.setItem('p2s.routed', '1'); } catch (e) {} location.replace(up + home); }
  })();
  document.addEventListener('change', function (e) {
    if (e.target && e.target.classList && e.target.classList.contains('dl-who')) {
      var id = e.target.value || null; set('p2s.persona', id); set('p2s.view', null); apply();
      var home = id ? C.homes[C.personas[id].track] : null;
      if (home && (here === 'index.html' || here === 'ops/index.html' || here === 'analysis/index.html') && home !== here) location.href = up + home + (home === 'index.html' ? '?home' : '');
    }
  });
  document.addEventListener('click', function (e) {
    var b = e.target && e.target.closest ? e.target.closest('.dl-view button') : null;
    if (b) { set('p2s.view', b.getAttribute('data-v')); apply(); }
  });
  apply();
})();
"""

def answers_json(ns):
    PERSONAS, J = ns['PERSONAS'], ns['J']
    return f'<script type="application/json" id="p2s-answers">{J({pid: {"person": p["person"], "label": p["label"], "group": p["group"], "answer": p["answer"]} for pid, p in PERSONAS.items()})}</script>'

def answer_card(ns, default):
    E, PERSONAS = ns['E'], ns['PERSONAS']
    p = PERSONAS[default]
    return (f'<aside class="ans" data-answer-for="{E(default)}"><div class="who-line"><span class="av {E(p["group"])}" data-a-av>{E(p["person"][0])}</span>'
            f'<div><b>Your answer in thirty seconds</b><div class="small" style="color:var(--band-muted)" data-a-who>for {E(p["person"])}, {E(p["label"].lower())}</div></div></div>'
            f'<p data-a-text>{E(p["answer"])}</p><p class="small" style="color:var(--band-muted);margin-bottom:0">Choose who you are in the bar above and this answer, the menu and your home change to fit.</p></aside>')

def kpi(ns, cls, k, v, d, href=None, up=''):
    E, U = ns['E'], ns['U']
    inner = f'<div class="k">{E(k)}</div><div class="v">{E(v)}</div><div class="d">{E(d)}</div>'
    return f'<a class="card kpi {cls}" href="{up}{U(href)}" style="text-decoration:none;color:inherit">{inner}</a>' if href else f'<div class="card kpi {cls}">{inner}</div>'

def agency_parts(ns, up):
    """The agencies as stance columns under one colour scale, and a card each: mockup C, for the live page."""
    D, E, SOURCES, short_name, U = ns['D'], ns['E'], ns['SOURCES'], ns['short_name'], ns['U']
    BUCKETS = [('none', 'No offline advice', 'var(--info)'), ('consider', 'Consider it, or after other steps', '#d6a556'), ('restrict', 'Restrict access', 'var(--warn)'),
               ('isolate', 'Isolate from the internet', 'var(--warn)'), ('yes', 'Take it offline', 'var(--alert)')]
    def bucket(o): return 'yes' if o == 'yes' else 'isolate' if o.startswith('isolate') else 'restrict' if o == 'restrict from abroad' else 'consider' if o in ('after mitigations', 'consider') else 'none' if o == 'none' else None
    cols = ''.join(f'<div class="bk"><div class="bk-h" style="border-top-color:{c}"><b>{sum(1 for a in D["agencies"] if bucket(a["offline"]) == k)}</b> {E(lab)}</div><div class="chips">' + ''.join(f'<span class="chip"><b style="font-family:var(--mono);font-weight:600">{E(a["country"].split()[0])}</b> {E(a["agency"].split(" (")[0])}</span>' for a in D['agencies'] if bucket(a['offline']) == k) + '</div></div>' for k, lab, c in BUCKETS)
    unread = [a for a in D['agencies'] if bucket(a['offline']) is None]
    spectrum = f'<div class="card"><div class="block-head"><h2 class="h2">The spectrum</h2><span class="small">every agency, by what it says to do with a system you cannot patch</span></div><div class="rail-g"></div><div class="buckets">{cols}</div>' + (f'<p class="small" style="margin:.8rem 0 0">Not readable from this capture environment: {", ".join(E(a["agency"]) for a in unread)}.</p>' if unread else '') + '</div>'
    def scls(o): return {'yes': 's-yes', 'isolate': 's-isolate', 'restrict': 's-isolate', 'consider': 's-consider', 'none': 's-none'}.get(bucket(o), 's-unknown')
    def slab(o): return {'yes': 'Take offline', 'none': 'No offline advice', 'unknown': 'Could not be read'}.get(o, o[0].upper() + o[1:])
    cards = ''.join(f'''<article class="card agency {scls(a["offline"])}"><div style="display:flex;justify-content:space-between;gap:.5rem"><h3 style="margin:0">{E(a["agency"])}</h3><span class="cc">{E(a["country"])}</span></div>
<span class="pill {"alert" if a["offline"] == "yes" else "warn" if scls(a["offline"]) in ("s-isolate", "s-consider") else "info" if a["offline"] == "none" else ""}">{E(slab(a["offline"]))}</span>
{f"<q>{E(a['offline_text'][:200])}</q>" if a.get("offline_text") and a["offline"] not in ("none", "unknown") else f"<p class=small style='margin:0'>{E((a.get('note') or '')[:170])}</p>"}
<div class="chips">{"".join(f"<a class=chip href='{up}sources/{U(s)}/index.html'>{E(short_name(SOURCES[s]))}</a>" for s in a["sources"][:3] if s in SOURCES)}</div></article>''' for a in D['agencies'])
    return spectrum, f'<div class="tiles" style="grid-template-columns:repeat(auto-fill,minmax(270px,1fr))">{cards}</div>'

def console_side(ns, path, up):
    E, U, NAV, D = ns['E'], ns['U'], ns['NAV'], ns['D']
    seen, rows = set(), []
    for _, items in NAV:
        for p, t in items:
            if p in seen or not (p.startswith(('admin/', 'status/', 'team/')) or p in ('method/index.html', 'brief/index.html', 'corrections/index.html')): continue
            seen.add(p); rows.append((p, t))
    def area(p):
        if p.startswith(('admin/board', 'admin/agents', 'admin/roles', 'team/', 'admin/versions', 'status/', 'admin/index')): return 'Console'
        if p.startswith(('admin/briefs', 'brief/', 'corrections/', 'admin/factcheck', 'admin/sherpa', 'admin/synthetic', 'method/')): return 'Editorial'
        return 'Systems'
    out = OrderedDict((k, []) for k in ('Console', 'Editorial', 'Systems'))
    for p, t in rows: out[area(p)].append((p, t))
    html = f'<a class="logo" href="{up}admin/index.html"><i>PHP</i>Team console</a>'
    for k, items in out.items():
        if not items: continue
        html += f'<h4>{E(k)}</h4>' + ''.join(f'<a href="{up}{U(p)}"{" class=here" if p == path else ""}>{E(t.split(":")[0])}</a>' for p, t in items)
    html += f'<h4>Reader site</h4><a href="{up}index.html">Back to the reader site</a>'
    return f'<nav class="side" aria-label="Team console">{html}</nav>'

def console_overview(ns):
    D, E, VERSION = ns['D'], ns['E'], ns['VERSION']
    A = D['admin']; bstat = Counter(b['status'] for b in A['board'])
    def tickets(status, n=6):
        rows = [b for b in A['board'] if b['status'] == status][-n:][::-1]
        return ''.join(f'<div class="ticket"><span class="id">#{E(b["id"])}</span><div>{E(b["title"][:120])}{"…" if len(b["title"]) > 120 else ""}</div><div class="o"><span>{E(b["owner"])}</span>{("<span>v" + E(b["version"]) + "</span>") if b.get("version") else ""}</div></div>' for b in rows)
    rel = D['versions']['versions'][:6]
    rels = ''.join(f'<tr><td style="font-family:var(--mono);white-space:nowrap"><a href="versions.html#v{E(r["version"])}">v{E(r["version"])}</a></td><td class="small" style="white-space:nowrap">{E(r["date"])}</td><td>{E(r["title"][:140])}{"…" if len(r["title"]) > 140 else ""}</td></tr>' for r in rel)
    kp = ''.join([kpi(ns, 'info', 'Release', f'v{VERSION}', f'{len(D["versions"]["versions"])} releases since 22 October'), kpi(ns, 'warn', 'Open on the board', str(bstat['open']), f'{bstat["done"]} done, {bstat.get("waiting", 0)} waiting', 'admin/board/index.html', '../'),
                  kpi(ns, 'good', 'Agents', str(len(A['roles'])), 'each with a mandate and a key', 'admin/roles/index.html', '../'), kpi(ns, 'info', 'Sources in the vault', str(len(D['sources'])), f'{sum(1 for s in D["sources"] if s.get("status") == "captured")} captured', 'sources/index.html', '../')])
    return f'''<div class="v2 console-top">
<p class="eyebrow">Team console &middot; public, like everything here</p>
<div class="tiles" style="margin:.6rem 0 1.4rem">{kp}</div>
<div class="block-head"><h2 class="h2">The board</h2><a class="small" href="board/index.html">every row &rarr;</a></div>
<div class="kanban"><div class="lane"><h3>Open <span>{bstat["open"]}</span></h3>{tickets("open")}</div><div class="lane"><h3>Waiting <span>{bstat.get("waiting", 0)}</span></h3>{tickets("waiting")}</div><div class="lane"><h3>Done <span>{bstat["done"]}</span></h3>{tickets("done")}</div></div>
<div class="card" style="margin-top:1.4rem"><div class="block-head"><h2 class="h2">Latest releases</h2><a class="small" href="versions.html">all {len(D["versions"]["versions"])} &rarr;</a></div><div class="tw"><table class="tbl">{rels}</table></div></div>
</div>'''

def it_mark(E, iid, it):
    return f'<span class="it" data-item="{E(iid)}" data-h="{E(it["hash"])}" data-n="{E(str(it.get("v", 1)))}"></span>'

def build_tracks(ns):
    """The homes of tracks B (Operations) and C (Analysis), as live pages through the site's own page()."""
    D, E, U, PERSONAS, page = ns['D'], ns['E'], ns['U'], ns['PERSONAS'], ns['page']
    SOURCES, short_name, human_time, STORY = ns['SOURCES'], ns['short_name'], ns['human_time'], ns['STORY']
    claims = D['claims']; st = Counter(c['status'] for c in claims); when = human_time(STORY['data_as_of'])
    items = ns['all_items']()  # this build's items; data/items.json on disk is the previous build's until save_items() runs (board 175)
    cl = {('fact-' + c['id']): c for c in claims}
    tl_days = Counter(t['at'][:10] for t in D['timeline'] if t['at'][:7] == '2026-10'); days = sorted(tl_days)

    # ------------------------------------------------------------------ B: Operations
    sam = PERSONAS['security']
    feed = sorted([(k, v) for k, v in items.items() if v.get('kind') in ('fact', 'event', 'question', 'story', 'front')],
                  key=lambda kv: (kv[1].get('date') or '', kv[1].get('changed') or '', kv[0]), reverse=True)[:14]
    def fitem(k, v):
        c = cl.get(k); status = c['status'] if c else ''
        col = {'confirmed': 'good', 'reported': 'info', 'disputed': 'warn', 'contradicted': 'warn', 'unverified': 'alert'}.get(status, '')
        text = c['claim'] if c else v['title']
        srcs = ''.join(f'<a class="chip" href="../sources/{U(s)}/index.html">{E(short_name(SOURCES[s]))}</a>' for s in (c['sources'] if c else [])[:4] if s in SOURCES)
        spill = f'<span class="pill {col}">{E(status)}</span>' if status else ''
        return (f'<article class="card fitem lv"><div><div class="meta">{it_mark(E, k, v)}<span class="pill">{E(v["kind"])}</span>{spill}<span class="small">v{E(v.get("changed", ""))} &middot; {E(v.get("date") or "")}</span></div>'
                f'<h3><a href="../{U(v["path"])}" style="color:inherit;text-decoration:none">{E(text[:200])}</a></h3>{f"<div class=chips>{srcs}</div>" if srcs else ""}</div></article>')
    steps = [('Patch internet-facing first', 'mod_php, then FPM, then the rest. Restart every worker; rebuild every image; check the running version after the restart.', 'playbook/index.html'),
             ('Bound the known paths', 'session.upload_progress off, low post_max_size, fatal_error_backtraces off on 8.5, pm.max_requests on FPM. Each blocks a path; none is a fix.', 'flaws/index.html#mitigations'),
             ('Watch the process tree', 'Alert on a PHP worker spawning a shell or a downloader. A clean access log proves nothing about the host.', 'defence/index.html')]
    actions = ''.join(f'<a class="card action" href="../{U(h)}" style="text-decoration:none;color:inherit"><div class="n">{i + 1}</div><div><h3>{E(t)}</h3><p>{E(x)}</p></div></a>' for i, (t, x, h) in enumerate(steps))
    donut = svg_donut([(st[k], c, k) for k, c in STATUS_COL.items() if st[k]])
    dleg = ''.join(f'<li><i style="background:{c}"></i>{st[k]} {E(k)}</li>' for k, c in STATUS_COL.items() if st[k])
    dmax = max(tl_days.values()) if tl_days else 1
    bars = ''.join(f'<div class="{"hot" if d >= "2026-10-20" else ""}" style="height:{max(3, round(100 * tl_days[d] / dmax))}%" title="{tl_days[d]} events on {E(d)}"></div>' for d in days)
    blabels = ''.join(f'<span>{E(d[8:])}</span>' for d in days)
    ex = ''.join(f'<li><span class="small">{E(x["when"])}</span><div class="t" style="font-size:.9rem">{E(x["who"].split("(")[0].strip())}: {E(x["what"][:100])}</div></li>' for x in D['exploitation'][:4])
    rnav = ''.join(f'<a href="../{U(h)}">{E(t)}<span>{E(n)}</span></a>' for t, n, h in [('If you run PHP', 'steps', 'playbook/index.html'), ('Check your stack', '', 'stack/index.html'), ('Patching: who gets a fix', '', 'patching/index.html'),
        ('The two flaws', '', 'flaws/index.html'), ('Exploitation signals', '', 'exploitation/index.html'), ('Detection and defence', '', 'defence/index.html'), ('The agencies', str(len(D['agencies'])), 'agencies/index.html'), ('Every claim', str(len(claims)), 'claims/index.html'), ('The code', '', 'code/index.html')])
    path_html = ''.join(f'<li><a href="../{U(x)}">{E(ns["nav_title"](x))}</a></li>' for x in sam['path'])
    body = f'''<div class="v2">
<div class="app">
  <aside class="rail">
    <div class="card" data-answer-for="security"><div style="display:flex;gap:.7rem;align-items:center"><span class="av act" data-a-av style="width:42px;height:42px">{E(sam["person"][0])}</span><div><b>Operations</b><div class="small" data-a-who>for {E(sam["person"])}, {E(sam["label"].lower())}</div></div></div>
      <p class="small" style="margin:.7rem 0 .2rem">Your reading path</p><ol class="small" style="margin:0;padding-left:1.1rem">{path_html}</ol></div>
    <nav class="railnav card flat" style="padding:.4rem" aria-label="Operations">{rnav}</nav>
  </aside>
  <div>
    <p class="eyebrow">Operations &middot; data as of {E(when)}</p>
    <h1 class="display" style="font-size:clamp(1.7rem,2.6vw,2.6rem);margin:.3rem 0 .5rem">What changed, what to do next, and how sure we are</h1>
    <p class="lede" style="margin:0 0 1.2rem" data-answer-for="security"><span data-a-text>{E(sam["answer"])}</span></p>
    <section><div class="block-head"><h2 class="h2">Your next three actions</h2><a class="small" href="../playbook/index.html">The whole playbook</a></div><div class="actions">{actions}</div></section>
    <section class="feed"><div class="block-head" style="margin-top:1.6rem"><h2 class="h2">What changed, newest first</h2><a class="small" href="../whatsnew/index.html">Release by release</a></div>
      {"".join(fitem(k, v) for k, v in feed)}
      <p class="small">Mark an item read with its circle: it fades, and leaves when you choose to hide read items. It comes back only if what it says changes.</p></section>
  </div>
  <aside class="rail right">
    <div class="card"><h3>How sure are we?</h3><div style="display:flex;gap:1rem;align-items:center;flex-wrap:wrap">{donut}<ul class="legend" style="flex-direction:column">{dleg}</ul></div><p class="small" style="margin:.4rem 0 0"><a href="../factcheck/index.html">The fact-check</a></p></div>
    <div class="card"><h3>Events per day, October</h3><div class="bars">{bars}</div><div class="bars-l">{blabels}</div><p class="small" style="margin:.5rem 0 0">Red: from the leak on 20 October. <a href="../timeline/index.html">The timeline</a></p></div>
    <div class="card"><h3>Exploitation signals</h3><ul class="delta">{ex}</ul><p class="small" style="margin:0"><a href="../exploitation/index.html">Every signal</a> &middot; <a href="../compromise/index.html">No named compromise: the evidence</a></p></div>
    <div class="card"><h3>Fixed in</h3><div class="chips">{"".join(f"<span class=chip style='font-family:var(--mono)'>{E(v)}</span>" for v in D["affected"]["fixed"])}</div><p class="small" style="margin:.5rem 0 0">8.1 and older: source backports only. <a href="../affected/index.html">Affected systems</a></p></div>
  </aside>
</div></div>{answers_json(ns)}'''
    page('ops/index.html', 'Operations: what changed, what to do next, how sure we are', 'The home for people who patch and defend: the next three actions, everything that changed newest first with what you have read marked, and the state of the evidence as charts: facts by status, events per day, exploitation signals, fixed versions.', body, kind='story', topics='php2shell operations')

    # ------------------------------------------------------------------ C: Analysis
    nums = D['numbers']
    ncards = ''.join(f'<a class="card kpi {"good" if n["status"] == "confirmed" else "warn" if n["status"] in ("disputed", "contradicted") else "alert" if n["status"] == "unverified" else "info"}" href="../numbers/index.html#{U(n["id"])}" style="text-decoration:none;color:inherit"><div class="k">{E(n["status"])}</div><div class="v">{E(n["value"])}</div><div class="d">{E(n["of"])}</div></a>' for n in nums[:8])
    spectrum, _ = agency_parts(ns, '../')
    topics = Counter(c['topic'] for c in claims)
    tmax = max(topics.values()) if topics else 1
    tbars = ''.join(f'<div style="display:grid;grid-template-columns:9rem minmax(0,1fr) 2.5rem;gap:.6rem;align-items:center;margin:.35rem 0"><span class="small" style="color:var(--ink-2)">{E(t)}</span><span style="display:flex;height:14px;border-radius:5px;overflow:hidden;background:var(--surface-2)">' + ''.join(f'<i style="width:{100 * sum(1 for c in claims if c["topic"] == t and c["status"] == k) / tmax:.1f}%;background:{col}" title="{k}"></i>' for k, col in STATUS_COL.items()) + f'</span><b class="small">{n}</b></div>' for t, n in topics.most_common())
    contested = [c for c in claims if c['status'] in ('disputed', 'contradicted', 'unverified')]
    cont = ''.join(f'<li><span class="pill {"alert" if c["status"] == "unverified" else "warn"}">{E(c["status"])}</span> <a href="../facts/{U(c["id"])}/index.html" style="color:inherit">{E(c["claim"][:170])}</a><div class="small">who says it: {E(c["by"][:90])}</div></li>' for c in contested[:10])
    body = f'''<div class="v2">
<section class="band"><div class="shell hero" style="grid-template-columns:minmax(0,1.3fr) minmax(320px,1fr)">
  <div><p class="eyebrow">Analysis &middot; data as of {E(when)}</p><h1 class="display">{len(claims)} facts. {st["confirmed"]} confirmed. {st["disputed"] + st["contradicted"] + st["unverified"]} still contested.</h1>
  <p class="lede">Every fact on this site carries one of five words for how far it can be trusted, and links to the saved pages it rests on. This is the view for weighing them: the numbers and what each measures, where governments disagree, and what is contested.</p></div>
  <div class="ans" data-answer-for="journalist"><div class="who-line"><span class="av communicate" data-a-av>R</span><div><b>Your answer in thirty seconds</b><div class="small" style="color:var(--band-muted)" data-a-who>for {E(PERSONAS["journalist"]["person"])}, journalist</div></div></div><p data-a-text>{E(PERSONAS["journalist"]["answer"])}</p></div>
</div></section>
<section class="block"><div class="grid cols-12">
  <div class="card span-4"><h2 class="h2" style="margin-bottom:.6rem">How sure are we?</h2><div style="display:flex;gap:1rem;align-items:center;flex-wrap:wrap">{svg_donut([(st[k], c, k) for k, c in STATUS_COL.items() if st[k]])}<ul class="legend" style="flex-direction:column">{"".join(f"<li><i style='background:{c}'></i>{st[k]} {E(k)}</li>" for k, c in STATUS_COL.items() if st[k])}</ul></div><p class="small" style="margin-bottom:0"><a href="../factcheck/index.html">The fact-check</a> &middot; <a href="../claims/index.html">every claim</a></p></div>
  <div class="card span-8"><div class="block-head"><h2 class="h2">The facts by topic, and by status</h2><span class="small">green confirmed, blue reported, amber disputed, red unverified</span></div>{tbars}</div>
</div></section>
<section class="block"><div class="block-head"><h2 class="h2">The numbers in the news, and how far each holds</h2><a class="small" href="../numbers/index.html">What each one measures</a></div><div class="tiles">{ncards}</div></section>
<section class="block">{spectrum}<p class="small"><a href="../agencies/index.html">Agency by agency, with their own words &rarr;</a></p></section>
<section class="block"><div class="grid cols-12">
  <div class="card span-7"><div class="block-head"><h2 class="h2">Contested: disputed, contradicted, unverified</h2><span class="small">{len(contested)} facts</span></div><ul class="delta">{cont}</ul></div>
  <div class="span-5 grid" style="align-content:start">
    <a class="card" href="../graph/index.html" style="text-decoration:none;color:inherit"><h3>As a graph</h3><p class="small" style="margin:0;color:var(--ink-2)">Every claim, event and source, and the citations between them.</p></a>
    <a class="card" href="../actors/index.html" style="text-decoration:none;color:inherit"><h3>Who says what</h3><p class="small" style="margin:0;color:var(--ink-2)">Every party quoted, with the claims each one makes.</p></a>
    <a class="card" href="../sources/index.html" style="text-decoration:none;color:inherit"><h3>Every source</h3><p class="small" style="margin:0;color:var(--ink-2)">{len(D["sources"])} pages, saved and fingerprinted at the minute they were read.</p></a>
    <a class="card" href="../articles/index.html" style="text-decoration:none;color:inherit"><h3>Stories</h3><p class="small" style="margin:0;color:var(--ink-2)">Signed and dated analysis, written here and kept as written.</p></a>
  </div></div></section>
</div>{answers_json(ns)}'''
    page('analysis/index.html', 'Analysis: how sure we are, and where the sources disagree', 'The home for people who weigh the evidence: every fact by status and topic, the numbers in the news with how far each holds, where governments disagree, and what is still contested, each linked to its saved sources.', body, kind='story', topics='php2shell analysis evidence')
