#!/usr/bin/env python3
"""Build php.oct-2026.story.sgit.ai from data/ into the repository root.

Deterministic: the same data/ and VERSION produce byte-identical output. There is no clock in
this file. Every page gets a markdown twin at the same path, and llms.txt lists every page.
Run: python3 admin/build/build.py        (from the repository root or anywhere)
"""
import html, json, os, re, sys
from collections import Counter, OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA = os.path.join(ROOT, 'data')
SITE = 'php.oct.2026.newsroom.sgit.ai'
BASE_URL = 'https://' + SITE
REPO_URL = 'https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP'
NEWSROOM = 'https://newsroom.sgit.ai/php-flaws/index.html'

def load(name):
    with open(os.path.join(DATA, name + '.json'), encoding='utf-8') as f:
        return json.load(f)

VERSION = open(os.path.join(ROOT, 'VERSION'), encoding='utf-8').read().strip()
D = {k: load(k) for k in ('story', 'claims', 'timeline', 'numbers', 'agencies', 'affected', 'exploitation',
                          'actors', 'roles', 'versions', 'billing', 'sources', 'vault', 'software',
                          'vault-claims', 'vault-timeline', 'code', 'history', 'impact', 'defence', 'admin', 'telemetry', 'review', 'questions')}
TREP = load('telemetry-report') if os.path.exists(os.path.join(DATA, 'telemetry-report.json')) else None
SOURCES = OrderedDict((s['slug'], s) for s in D['sources'])
STORY = D['story']
if D['vault'].get('latest_capture'):
    STORY['data_as_of'] = D['vault']['latest_capture']  # the time of the latest capture in the vault, never a clock

E = html.escape

# ----------------------------------------------------------------------------- small helpers

STATUS_WORDS = OrderedDict([
    ('confirmed', 'two or more primary sources agree, or the fact was counted from a captured file'),
    ('reported', 'one party says so, and it has not been contradicted'),
    ('disputed', 'the sources disagree, and both readings are shown'),
    ('contradicted', 'a primary source says otherwise'),
    ('unverified', 'even the reporting outlet could not check it'),
])

def pill(status):
    s = (status or '').split(' ')[0].split(',')[0].lower()
    cls = s if s in STATUS_WORDS else 'other'
    return f'<span class="st st-{cls}">{E(status)}</span>'

def src_links(slugs, depth):
    out = []
    for s in slugs:
        if s in SOURCES:
            row = SOURCES[s]
            out.append(f'<a class="src" href="{"../" * depth}sources/{E(s)}/index.html" title="{E(row.get("title") or row.get("publisher") or s)}">{E(short_name(row))}</a>')
        else:
            out.append(f'<span class="src src-missing" title="not in the manifest">{E(s)}</span>')
    return ' '.join(out)

def short_name(row):
    pub = row.get('publisher') or row['slug']
    pub = re.sub(r'\s*\(.*?\)\s*', ' ', pub).strip()
    pub = pub.replace('US Cybersecurity and Infrastructure Security Agency', 'CISA')
    pub = pub.replace('UK National Cyber Security Centre', 'NCSC UK').replace('US National Security Agency', 'NSA')
    pub = pub.replace('NIST National Vulnerability Database', 'NVD').replace('Canadian Centre for Cyber Security', 'CCCS')
    pub = pub.replace('Swiss Federal Office for Cyber Security', 'BACS').replace('CERT-FR', 'CERT-FR')
    pub = pub.replace('The PHP Foundation', 'PHP Foundation').replace('PHP Group', 'php.net')
    pub = pub.replace('NCSC-NL', 'NCSC-NL').replace('oss-security list', 'oss-security')
    pub = pub.replace('php/php-src on GitHub', 'php-src').replace('OpenAI Developer Community', 'OpenAI forum')
    pub = pub.replace('CVE Program', 'CVE record').replace('ENISA / EU CSIRTs Network', 'ENISA CNW')
    pub = pub.replace('NSA Cybersecurity', 'NSA Cyber').replace("ASD's ACSC", 'ACSC')
    pub = pub.replace('Alexandre Daubois', 'Daubois').replace('The Hacker News', 'THN').replace('Techzine Global', 'Techzine')
    kind = row.get('kind')
    if kind == 'social' and 'x.com' in (row.get('url') or ''):
        pub += ' on X'
    return pub[:34]

def fmt_at(at):
    """A date or ISO instant as the timeline shows it."""
    if not at:
        return ''
    m = re.match(r'^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})(?::(\d{2}))?Z$', at)
    if m:
        return f'{m.group(1)} {m.group(2)}{":" + m.group(3) if m.group(3) else ""} UTC'
    return at

def md_escape_cell(s):
    return s.replace('|', '\\|').replace('\n', ' ')

# ----------------------------------------------------------------------------- html -> markdown

def to_markdown(fragment):
    """A small, deterministic HTML to Markdown conversion for the .md twins."""
    s = fragment
    s = re.sub(r'<svg.*?</svg>', '', s, flags=re.S)
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<sg-meter[^>]*></sg-meter>', '', s)
    # tables
    def table(m):
        t = m.group(0)
        rows = re.findall(r'<tr.*?</tr>', t, flags=re.S)
        out, first = [], True
        for r in rows:
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, flags=re.S)
            cells = [md_escape_cell(inline(c)).strip() for c in cells]
            out.append('| ' + ' | '.join(cells) + ' |')
            if first:
                out.append('|' + '---|' * len(cells))
                first = False
        return '\n' + '\n'.join(out) + '\n'
    def inline(x):
        x = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f'[{strip(m.group(2))}]({m.group(1)})', x, flags=re.S)
        x = re.sub(r'<(b|strong)>(.*?)</\1>', r'**\2**', x, flags=re.S)
        x = re.sub(r'<(i|em|q)>(.*?)</\1>', r'*\2*', x, flags=re.S)
        x = re.sub(r'<code>(.*?)</code>', r'`\1`', x, flags=re.S)
        x = re.sub(r'<br\s*/?>', ' ', x)
        return strip(x)
    def strip(x):
        x = re.sub(r'<[^>]+>', '', x)
        return html.unescape(re.sub(r'\s+', ' ', x))
    s = re.sub(r'<table.*?</table>', table, s, flags=re.S)
    s = re.sub(r'<h1[^>]*>(.*?)</h1>', lambda m: '\n# ' + inline(m.group(1)) + '\n', s, flags=re.S)
    s = re.sub(r'<h2[^>]*>(.*?)</h2>', lambda m: '\n## ' + inline(m.group(1)) + '\n', s, flags=re.S)
    s = re.sub(r'<h3[^>]*>(.*?)</h3>', lambda m: '\n### ' + inline(m.group(1)) + '\n', s, flags=re.S)
    s = re.sub(r'<h4[^>]*>(.*?)</h4>', lambda m: '\n#### ' + inline(m.group(1)) + '\n', s, flags=re.S)
    s = re.sub(r'<li[^>]*>(.*?)</li>', lambda m: '- ' + inline(m.group(1)) + '\n', s, flags=re.S)
    s = re.sub(r'<(p|dt|dd|figcaption)[^>]*>(.*?)</\1>', lambda m: '\n' + inline(m.group(2)) + '\n', s, flags=re.S)
    s = re.sub(r'<pre[^>]*>(.*?)</pre>', lambda m: '\n```\n' + html.unescape(re.sub(r'<[^>]+>', '', m.group(1))) + '\n```\n', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t]+\n', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip() + '\n'

# ----------------------------------------------------------------------------- layout

NAV = [
    ('Questions', [('questions/index.html', 'Questions readers ask')] + [(f'questions/{q["id"]}/index.html', q['q']) for q in D['questions']['questions']]),
    ('The story', [('index.html', 'Front page'), ('flaws/index.html', 'The two flaws'), ('code/index.html', 'The code'), ('timeline/index.html', 'Timeline'),
                   ('discovery/index.html', 'Who found it'), ('leak/index.html', 'How disclosure broke'),
                   ('exploitation/index.html', 'Exploitation signals'), ('review/index.html', 'The fix, mapped to the code'), ('review/ui/index.html', 'Walk the graph'), ('impact/index.html', 'Impact: offline vs compromised'),
                   ('defence/index.html', 'Detection and defence'), ('context/index.html', 'In context: 2008 to 2026'), ('playbook/index.html', 'If you run PHP')]),
    ('The evidence', [('claims/index.html', 'Every claim'), ('numbers/index.html', 'The numbers'), ('agencies/index.html', 'The agencies'),
                      ('affected/index.html', 'Affected systems'), ('affected/software.html', 'Software inventory'), ('sources/index.html', 'Every source'),
                      ('actors/index.html', 'Who says what'), ('graph/index.html', 'As a graph')]),
    ('Briefings', [(f'briefings/{a["id"]}/index.html', a['name']) for a in D['roles']['audiences']]),
    ('About', [('method/index.html', 'The method'), ('team/index.html', 'The team'), ('billing/index.html', 'The billing model'),
               ('account/index.html', 'Your reading account'), ('brief/index.html', 'The brief'),
               ('corrections/index.html', 'Corrections'), ('admin/versions.html', 'Release history'), ('admin/index.html', 'Admin & engineering'),
               ('admin/board/index.html', 'The board'), ('admin/roles/index.html', 'Roles'), ('admin/briefs/index.html', 'Briefs'), ('admin/vault/index.html', 'The vault, opened'), ('admin/telemetry/index.html', 'Who reads this site')]),
]

PAGES = []  # (path, title, description) in order, for llms.txt

def layout(path, title, description, body, kind='page', date=None, topics='', ld_type='Article'):
    depth = path.count('/')
    up = '../' * depth
    PAGES.append((path, title, description, kind))
    here = path
    nav_items = []
    for label, items in NAV:
        active = any(p == here for p, _ in items)
        subs = ''.join(f'<a class="sl{" here" if p == here else ""}" href="{up}{p}">{E(t)}</a>' for p, t in items)
        nav_items.append(f'<div class="ni"><a class="nl{" here" if active else ""}" href="{up}{items[0][0]}">{E(label)}<span class="caret">&#9662;</span></a><div class="sub">{subs}</div></div>')
    cfg = D['billing']['runs']
    meter_cfg = {
        'storageKey': cfg['storageKey'], 'start': cfg['start'], 'symbol': cfg['symbol'],
        'prices': {**cfg['prices'], 'article': cfg['prices']['story'], 'article_new': cfg['prices']['story']},
        'newDays': cfg['newDays'], 'minDepth': cfg['minDepth'], 'topup': cfg['topup'],
        'links': {'account': 'account/index.html', 'topup': 'account/top-up.html'},
        'links2': {'newsroom': 'account/index.html', 'personas': 'account/index.html'},
        'root': up,
    }
    meter_json = json.dumps(meter_cfg, sort_keys=True, separators=(',', ':'))
    page_meter = '' if kind == 'free' else f'<sg-meter view="page" quiet kind="{E(kind)}" date="{E(date or STORY["data_as_of"][:10])}" topics="{E(topics)}" title="{E(title)}"></sg-meter>'
    ld = {
        '@context': 'https://schema.org', '@type': ld_type, 'headline': title, 'description': description,
        'url': f'{BASE_URL}/{path}', 'isPartOf': {'@type': 'WebSite', 'name': SITE, 'url': BASE_URL},
        'license': 'https://creativecommons.org/licenses/by/4.0/', 'dateModified': STORY['data_as_of'][:10],
        'version': VERSION,
    }
    return f'''<!doctype html>
<html lang="en" data-root="{up}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)} &middot; {SITE}</title>
<meta name="description" content="{E(description)}">
<link rel="canonical" href="{BASE_URL}/{path}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE}">
<meta property="og:url" content="{BASE_URL}/{path}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta name="twitter:card" content="summary">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="icon" href="data:,">
<link rel="alternate" type="text/markdown" href="{up}{md_path(path)}">
<link rel="stylesheet" href="{up}assets/site.css">
<link rel="stylesheet" href="{up}assets/themes/themes.css">
<link rel="stylesheet" href="{up}assets/themes/site-tokens.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/json" id="sg-meter-config">{meter_json}</script>
<script type="module" src="{up}assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js"></script>
<script src="{up}assets/site.js" defer></script>
<script src="{up}assets/telemetry.js" defer></script>
</head>
<body>
<nav class="site"><div class="row">
  <script src="{up}assets/themes/themes.js"></script>
  <a class="brand" href="{up}index.html">php2shell<span>.newsroom</span></a>
  <a class="ver" href="{up}admin/versions.html#v{E(VERSION)}" title="Site release history: what v{E(VERSION)} changed">v{E(VERSION)}</a>
  <span class="status">{E(STORY["status"])} &middot; data as of {E(STORY["data_as_of"])}</span>
  <span class="crumbs"><a href="https://newsroom.sgit.ai/">newsroom</a> / <a href="https://2026.newsroom.sgit.ai/">2026</a> / <a href="https://oct.2026.newsroom.sgit.ai/">October</a> / <b>php2shell</b></span>
  <div class="tools"><div class="theme-pick"></div><sg-meter view="balance"></sg-meter></div>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-items" aria-label="Menu">Menu</button>
  <div class="nav-items" id="nav-items">{''.join(nav_items)}<a class="nl ext" href="{up}llms.txt">llms.txt</a></div>
</div></nav>
<main>
{body}
{page_meter}
</main>
<footer class="site">
  <div class="row">
    <p><b>{SITE}</b> follows one story, the two PHP flaws of October 2026, as evidence: every claim with a status and its sources, every source captured, dated and hashed into a private vault. Built and run by one editor and a team of software agents; <a href="{up}team/index.html">the roles</a> and <a href="{up}method/index.html">the method</a> are public, and the site is rebuilt from the vault, never written by hand. One of the SGit Newsroom's story sites: up from here are <a href="https://oct.2026.newsroom.sgit.ai/">October 2026</a>, <a href="https://2026.newsroom.sgit.ai/">the year</a> and <a href="https://newsroom.sgit.ai/">the newsroom</a>, whose own section on the story is <a href="{NEWSROOM}">here</a>. Part of the <a href="https://sgit.ai/network/index.html">sgit.ai network</a>.</p>
    <p class="disc">&#9888; Participant disclosure: published by the sgit project, which builds the vault and metering stack this site runs on. Content CC BY 4.0 for this site's own text, tables and data; quoted words are their authors', linked; no third-party page is reproduced. Code Apache-2.0.</p>
    <p class="small">&#9673; This page sends one anonymous usage event (page, referrer host, country and region, no IP, no cookie) to a write-only vault lane; <a href="{up}admin/telemetry/index.html">what is sent and what is counted</a>. Honoured: Do Not Track and Global Privacy Control.</p>
    <p class="small">site v{E(VERSION)} &middot; evidence vault commit {E(D["vault"]["head"]["commit"] or "unknown")} &middot; <a href="{up}admin/index.html">engineering</a> &middot; <a href="{up}{md_path(path)}">this page as markdown</a> &middot; <a href="{REPO_URL}">GitHub</a></p>
  </div>
</footer>
</body>
</html>
'''

def md_path(path):
    return re.sub(r'\.html$', '.md', path)

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

def page(path, title, description, body, **kw):
    html_out = layout(path, title, description, body, **kw)
    write(path, html_out)
    md = f'<!-- {SITE} v{VERSION} · {path} · {title} -->\n'
    write(md_path(path), f'# {title}\n\n{description}\n\n' + to_markdown(body) + f'\n\n---\nsite v{VERSION} · data as of {STORY["data_as_of"]} · vault commit {D["vault"]["head"]["commit"]} · {BASE_URL}/{path}\n')

def table(headers, rows, cls='t'):
    th = ''.join(f'<th>{h}</th>' for h in headers)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def section(id, title, inner, lead=None):
    return f'<section id="{id}"><h2>{title}</h2>{("<p class=lead>" + lead + "</p>") if lead else ""}{inner}</section>'

def stat(n, label, href=None, depth=0):
    inner = f'<b>{E(str(n))}</b><span>{label}</span>'
    return f'<a class="stat" href="{"../" * depth}{href}">{inner}</a>' if href else f'<div class="stat">{inner}</div>'

def weight(c):
    prim = sum(1 for s in c['sources'] if s in SOURCES and SOURCES[s].get('primary'))
    blocked = sum(1 for s in c['sources'] if s in SOURCES and SOURCES[s].get('status') in ('blocked', 'failed'))
    return prim, len(c['sources']), blocked

def claim_rows(claims, depth):
    rows = []
    for c in claims:
        note = f'<div class="note">{E(c["note"])}</div>' if c.get('note') else ''
        p, n, b = weight(c)
        wt = f'<span class="wt" title="primary sources among the sources cited; blocked captures">{p}/{n}' + (f' <small>({b} blocked)</small>' if b else '') + '</span>'
        rows.append([f'<span id="{E(c["id"])}">{E(c["claim"])}</span>{note}', E(c['by']), pill(c['status']), wt, src_links(c['sources'], depth)])
    return table(['Claim', 'Who says it', 'Status', 'Primary', 'Sources'], rows, 'claims')

def status_legend(depth=0):
    items = ''.join(f'<li>{pill(k)} {E(v)}</li>' for k, v in STATUS_WORDS.items())
    return f'<ul class="legend">{items}<li><span class="wt">p/n</span> primary sources among the n cited; a blocked capture is counted and marked</li></ul>'

def counts():
    c = Counter(x['status'] for x in D['claims'])
    return {'claims': len(D['claims']), 'by_status': c, 'events': len(D['timeline']), 'agencies': len(D['agencies']),
            'numbers': len(D['numbers']), 'signals': len(D['exploitation']), 'sources': D['vault']['sources'],
            'captures': D['vault']['captures'], 'hashed': D['vault']['hashed_files'], 'primary': D['vault']['primary'],
            'blocked': D['vault']['blocked'], 'software': D['software']['count'] if D.get('software') else 0}

C = counts()

# ----------------------------------------------------------------------------- pages

def build_index():
    s = STORY
    known = ''.join(f'<li>{k["html"]} <span class="refs">{src_links(k["sources"], 0)}</span></li>' for k in s['known'])
    openq = ''.join(f'<li>{o["html"]}</li>' for o in s['open'])
    stats = ''.join([
        stat(C['sources'], 'sources in the evidence vault', 'sources/index.html'),
        stat(C['captures'], 'dated captures, each file hashed', 'sources/index.html'),
        stat(C['claims'], f'claims with a status: {C["by_status"]["confirmed"]} confirmed, {C["by_status"]["disputed"] + C["by_status"]["contradicted"]} disputed or contradicted, {C["by_status"]["unverified"]} unverified', 'claims/index.html'),
        stat(C['events'], 'dated events on the timeline', 'timeline/index.html'),
        stat(C['agencies'], 'national agencies compared', 'agencies/index.html'),
        stat(len(D['impact']['offline']), 'operators reported offline, 0 confirmed compromises', 'impact/index.html'),
        stat(C['software'], 'products in the NCSC-NL inventory', 'affected/software.html'),
    ])
    latest = sorted([t for t in D['timeline'] if t['at'] >= '2026-10-20'], key=lambda t: t['at'])[-8:]
    latest_rows = [[f'<span class="when">{E(fmt_at(t["at"]))}</span>', E(t['event']), src_links(t['sources'], 0)] for t in latest]
    doors = ''.join(f'<a class="door" href="briefings/{a["id"]}/index.html"><b>{E(a["name"])}</b><span>{E(a["question"])}</span></a>' for a in D['roles']['audiences'])
    nums = D['numbers']
    numrow = ''.join(f'<a class="num" href="numbers/index.html#{E(n["id"])}"><b>{E(n["value"])}</b><span>{E(n["of"])}</span>{pill(n["status"])}</a>' for n in nums[:6])
    body = f'''
<header class="hero">
  <p class="kicker">{E(s["status"])} &middot; {E(" and ".join(s["cves"]))} &middot; updated with the vault, {E(s["data_as_of"])}</p>
  <h1>{E(s["title"])}</h1>
  <p class="lead">{s["lead_html"]}</p>
  <div class="stats">{stats}</div>
  <p class="caveat">{s["caveat_html"]}</p>
</header>
{section("numbers", "Six numbers, and what each one measures", f'<div class="nums">{numrow}</div><p>The figures in circulation range from 2.6 million hosts to 70% of the Internet. They are not contradictory so much as incommensurable: each measures a different thing. <a href="numbers/index.html">The numbers page</a> says what each one counts, who said it, and whether anyone has checked it.</p>')}
{section("known", "What is established", f'<ul class="known">{known}</ul>')}
{section("open", "What is not", f'<ul class="open">{openq}</ul>', "Open questions, stated rather than papered over. Each one names what would close it.")}
{section("latest", "The last 48 hours", table(["When (UTC)", "What", "Source"], latest_rows, "tl") + '<p><a href="timeline/index.html">The whole timeline &rarr;</a> runs from the 2024 audit to the latest capture, with every time stated as its source states it and every conversion marked.</p>')}
{section("questions", "Questions readers ask", '<ul class="asks">' + ''.join(f'<li><a href="questions/{E(q["id"])}/index.html"><b>{E(q["q"])}</b></a> {E(q["short"].split(". ")[0])}.</li>' for q in D['questions']['questions'][:5]) + '</ul><p><a href="questions/index.html">Every question, and the page that answers it &rarr;</a></p>', "Asked in group chats, newsrooms and boardrooms; each answer is short enough to paste back, and points at the pages and sources behind it.")}
{section("doors", "Read it for your job", f'<div class="doors">{doors}</div>', "Six briefings from the same claims. None adds a claim; each selects, orders and keeps every source.")}
{section("how", "How this site works", '''<div class="how">
<div><h3>Capture, don't paraphrase</h3><p>Every source is captured into a private, encrypted vault: the page as served, as rendered, its text, a screenshot and its headers, each file hashed at capture time. Captures are only ever added, so a page that changes leaves a series. The captures are third-party pages and are not republished; <a href="sources/index.html">their hashes are</a>.</p></div>
<div><h3>Claims carry a status</h3><p>Five words, each defined: confirmed, reported, disputed, contradicted, unverified. A claim is a row pointing at the sources that give it that status, and the page never upgrades a claim its sources do not support.</p></div>
<div><h3>Rebuilt, never edited</h3><p>The site is a deterministic function of the vault and a version number: the same data produces byte-identical pages, there is no clock in the build, and a gate refuses to release a broken link, an orphan page, an unsourced claim or a credential. <a href="method/index.html">The method</a>, <a href="team/index.html">the team</a> and <a href="billing/index.html">the billing model</a> are published.</p></div>
</div>''')}
'''
    page('index.html', s['title'], s['description'], body, kind='story', topics='php2shell overview', ld_type='NewsArticle')

def build_flaws():
    a = D['affected']
    cves = [
        {'id': 'CVE-2026-109618', 'ghsa': 'GHSA-w8hw-w9fx-j79w', 'title': 'RCE via OOM corruption', 'src': ['cve-cve-2026-109618', 'github-ghsa-w8hw-w9fx-j79w', 'nvd-cve-2026-109618', 'openwall-oss-security-2026-10-21-6'],
         'desc': 'PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).',
         'reserved': '2026-10-12T21:03:58Z', 'published': '2026-10-21T13:48:34Z', 'ghsa_at': '2026-10-21T13:34:25Z',
         'demo': 'Complete RCE validated over HTTP against mod_php with default input and memory limits, before any application code runs. FPM: susceptible by source analysis; the GitHub advisory says no complete FPM exploit has been demonstrated. FrankenPHP likely susceptible; LSAPI likely but unvalidated.',
         'fix': 'Removes longjmp() for OOM. A delayed, graceful soft OOM at the next VM safe point, plus a hard OOM via _exit() at a higher threshold.'},
        {'id': 'CVE-2026-109619', 'ghsa': 'GHSA-6wmf-4rv5-p3rp', 'title': 'RCE via stale global state', 'src': ['cve-cve-2026-109619', 'github-ghsa-6wmf-4rv5-p3rp', 'nvd-cve-2026-109619', 'openwall-oss-security-2026-10-21-7'],
         'desc': 'PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).',
         'reserved': '2026-10-12T21:04:00Z', 'published': '2026-10-21T13:54:43Z', 'ghsa_at': '2026-10-21T13:34:13Z',
         'demo': 'A use-after-free of worker global state across requests: a producer request and a consumer request on the same worker. Confirmed on the PHP 8.5 fatal-error-backtrace path (the basis of the mod_php exploit) and the session upload progress path, which is enabled by default and needs no session_start(); the session path was validated against mod_php and FPM.',
         'fix': 'Part of the same change, "Avoid state corruption via bailout": global state is reset so it cannot refer to freed request memory.'},
    ]
    cards = ''
    for c in cves:
        cards += f'''<article class="cve" id="{E(c["id"])}">
<h3>{E(c["id"])}: {E(c["title"])}</h3>
<p class="meta">{E(c["ghsa"])} &middot; CVSS v4.0 <b>9.2</b> &middot; CWE-416, 755, 824, 1325, 1419 &middot; reserved {E(fmt_at(c["reserved"]))} &middot; advisory {E(fmt_at(c["ghsa_at"]))} &middot; CVE record {E(fmt_at(c["published"]))}</p>
<p class="verb"><b>The record's description, verbatim.</b> <q>{E(c["desc"])}</q></p>
<p><b>What was demonstrated.</b> {E(c["demo"])}</p>
<p><b>The fix.</b> {E(c["fix"])}</p>
<p class="refs">{src_links(c["src"], 1)}</p>
</article>'''
    vector = 'CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N'
    sapis = table(['SAPI', 'Risk', 'What the primary sources say', 'Sources'], [[E(s['sapi']), E(s['risk']), E(s['text']), src_links(s['sources'], 1)] for s in a['sapis']])
    blast = '''
<p>Remote code execution <i>as the web worker</i> is the floor, not the ceiling, and not yet a breach. What an attacker gets is whatever that worker can reach: the application's source and configuration, the database credentials in it, the session store, the files the worker can read or write, the outbound network it can open, and anything that trusts requests from that host. What they do not automatically get is the database server's other schemas, the credentials that were never on that host, or a system behind an allow-list the worker is not on. The blast radius of one compromised PHP worker is therefore a property of the system around it, and that is the first thing to map. The questions, with where the answer usually lives:</p>
<ul>
<li><b>What runs there?</b> A brochure site with no login, a shop with payment data, an intranet with single sign-on, a mail client, an admin panel. The same bug has a different consequence in each. (The NCSC-NL inventory is a start; your asset register is the real answer.)</li>
<li><b>What credentials sit on the host?</b> Database passwords, API keys, cloud instance roles, SSH keys in a deploy user's home. A key that cannot be used from anywhere else is a much smaller loss than one that can.</li>
<li><b>What can the worker reach outbound?</b> Egress rules decide whether a shell becomes a download of tooling, a callback, or a pivot.</li>
<li><b>What trusts the host?</b> Internal services that accept any request from the web tier, shared file systems, backup agents.</li>
<li><b>What would you see?</b> CISA's signal is concrete: PHP worker processes launching shells or downloading tools. JPCERT warns that with several exploit paths, one detection rule can miss an attack and a clean log does not prove a clean system.</li>
<li><b>How fast can you pull the plug?</b> Taking a system offline is the last step in every agency's list, but the ability to do it in minutes, cleanly, is a property worth having before the next one of these.</li>
</ul>
<p class="refs">''' + src_links(['cisa-alert-php-20261021', 'jpcert-at260033', 'github-ghsa-6wmf-4rv5-p3rp', 'ncsc-nl-php2shell-software-list'], 1) + '</p>'
    body = f'''
<h1>The two flaws</h1>
<p class="lead">Two bugs in the PHP engine, the same severity, the same fix, the same four releases. Both are memory-safety failures in how PHP recovers from an error, and both can be reached by an unauthenticated HTTP request. This page keeps to what the primary records say and marks where they differ.</p>
<p class="kv"><b>Fixed in</b> PHP {", ".join(a["fixed"])} &middot; <b>Vector</b> <code>{vector}</code> &middot; <b>Nickname</b> php2shell (NSA: PHP2Shell) &middot; <b>CNA</b> PHP Group</p>
{cards}
{section("sapis", "Which deployments", sapis, "The flaw is in the engine, so what matters is how PHP is wired to the web server. php.net ranks mod_php highest.")}
{section("blast", "What a compromise would mean: the blast radius", blast, "This section is the site's own analysis, written from the sources it cites. It is a way of asking the question, not an assessment of any system.")}
{section("versions", "Affected and fixed versions", table(['Branch', 'Affected', 'Fixed', 'In the CVE record'], [[E(r['branch']), E(r['affected']), E(r['fixed']), 'yes' if r['in_cve'] else '<b>no</b>'] for r in a['ranges']]) + f'<p>{E(a["ranges_note"])}</p><p class="refs">{src_links(a["ranges_sources"], 1)}</p>')}
{section("mitigations", "The temporary mitigations, and what each one does not do", table(['For', 'Setting', 'Caveat, from the same source'], [[E(m['for']), E(m['what']), E(m['caveat'])] for m in a['mitigations']]) + f'<p>php.net: <q>while only an update is a complete solution, the following measures reduce exposure to specific attack paths but do not make an installation safe.</q> <span class="refs">{src_links(a["mitigations_sources"], 1)}</span></p>')}
<p>The engineering steps, in order, are on <a href="../playbook/index.html">If you run PHP</a>. The disagreement between the two primary accounts of FPM is <a href="../claims/index.html#rce-fpm">claim rce-fpm</a>.</p>
'''
    page('flaws/index.html', 'The two flaws: CVE-2026-109618 and CVE-2026-109619', 'What the CVE records, the GitHub advisories and the PHP security team say about php2shell: the bug classes, what was demonstrated, which deployments, which versions, the fix and the temporary mitigations, with the blast-radius questions.', body, kind='story', topics='php2shell technical cve')

def build_timeline():
    phases = OrderedDict([('origin', 'Origins, 2024 to mid-2026'), ('discovery', 'Discovery, August 2026'), ('coordination', 'Coordinated disclosure, August to 19 October'),
                          ('leak', 'The leak, 17 to 21 October'), ('release', 'The release, 21 October 13:30 to 14:44 UTC'), ('response', 'The response, 20 to 22 October'),
                          ('aftermath', 'Aftermath, 21 to 22 October'), ('method', 'This site')])
    evs = sorted(D['timeline'], key=lambda t: (t['at'], t['event']))
    out = ''
    for ph, title in phases.items():
        rows = [[f'<span class="when">{E(fmt_at(t["at"]))}</span>', E(t['event']) + (f'<div class="note">{E(t["note"])}</div>' if t.get('note') else ''), pill(t['confidence']), src_links(t['sources'], 1)] for t in evs if t.get('phase') == ph]
        if rows:
            out += section('ph-' + ph, title, table(['When', 'What', 'Time is', 'Sources'], rows, 'tl'))
    legend = '<ul class="legend"><li>' + pill('stated') + ' the source states this date or time</li><li>' + pill('inferred') + ' this site worked it out, and the note says how</li><li>' + pill('disputed') + ' the sources give different times</li></ul>'
    body = f'''
<h1>The timeline</h1>
<p class="lead">{C["events"]} events from the 2024 audit to the latest capture, each dated as its source states it. Times are UTC; where this site converted from a local time, or inferred a date from a phrase such as <q>two days ago</q>, the row says so. A row that lists several sources is one that at least two accounts carry; a row with one source is that party's account.</p>
{legend}
{out}
<p>The sequence as a graph of who said what first is on <a href="../discovery/index.html">Who found it</a>; the leak alone is on <a href="../leak/index.html">How disclosure broke</a>.</p>
'''
    page('timeline/index.html', 'The timeline, 2024 to the latest capture', f'{C["events"]} dated events in the php2shell story, from the 2024 audit through discovery, coordinated disclosure, the leak, the release and the response, every one tied to a captured source.', body, kind='story', topics='php2shell timeline')

def build_claims():
    topics = OrderedDict([('technical', 'The flaws themselves'), ('scale', 'How big it is'), ('discovery', 'Who found it, and how'), ('leak', 'The leak'),
                          ('timing', 'When things happened'), ('exploitation', 'Exploitation'), ('advice', 'What the agencies advise'), ('impact', 'What was taken offline')])
    out = ''
    for t, title in topics.items():
        cs = [c for c in D['claims'] if c['topic'] == t]
        if cs:
            out += section('t-' + t, title, claim_rows(cs, 1))
    counts = ', '.join(f'{C["by_status"][k]} {k}' for k in STATUS_WORDS if C['by_status'][k])
    body = f'''
<h1>Every claim, and who makes it</h1>
<p class="lead">{C["claims"]} claims: {counts}. A claim is a sentence somebody said, with the party that said it, the captured sources it comes from, and one of five words for how far it can be trusted. The words are defined here, once, and the build refuses a claim whose sources are not in the manifest.</p>
{status_legend()}
{out}
<p>The newsroom's own twelve claims, seeded from the BBC live page on the morning of 22 October, are in the vault as <code>claims/claude-newsroom-lead.json</code> and are superseded by the rows above, which trace each of them to primary sources. The raw rows are in <a href="../data/claims.json">data/claims.json</a>.</p>
'''
    page('claims/index.html', 'Every claim, with its status and sources', f'{C["claims"]} claims about php2shell, each with who makes it, a status (confirmed, reported, disputed, contradicted or unverified) and the captured sources behind it.', body, kind='analysis', topics='php2shell claims provenance')

def build_numbers():
    rows = []
    for n in D['numbers']:
        rows.append([f'<b id="{E(n["id"])}">{E(n["value"])}</b><br><span class="small">{E(n["of"])}</span>', E(n['measures']), E(n['who']), pill(n['status']), E(n['note']), src_links(n['sources'], 1)])
    body = f'''
<h1>The numbers, and what each one measures</h1>
<p class="lead">The editor's starting point for this site was a figure that did not add up: <q>70% of the internet</q>. It turns out to be a headline's restatement of a share-of-websites statistic that nobody on this beat sources, sitting next to a host count a thousand times smaller and a national count a thousand times smaller again. None of them is wrong on its own terms. The table says what each one counts.</p>
{table(['Figure', 'What it measures', 'Who said it', 'Status', 'Note', 'Sources'], rows, 'nums-t')}
{section("why", "Why they differ by four orders of magnitude", '''
<ul>
<li><b>A share of websites that use PHP</b> (about 70%) is the population a survey counts by looking at response headers and page markup across a sample of the web. It includes every site on a shared host that patched hours ago, every site behind a CDN, and every site that has not been touched since 2019. It is an upper bound on exposure.</li>
<li><b>Internet-facing hosts that expose PHP</b> (2.6 million, one scanner's count) is a count of machines, not sites. One host serves many sites; most sites sit behind hosts that do not announce PHP at all. It is a lower bound on the machines an attacker could reach directly.</li>
<li><b>Websites that could be affected</b> (30 million) has no stated basis. It may be a fraction of a websites total; it may be a guess.</li>
<li><b>Resources potentially affected in one country</b> (about 6,000 in Latvia) is the only figure from a body that could inventory what it counts. Scaled naively by population it would put the EU in the low millions, which is a different number from any of the above and is not offered here as one.</li>
<li><b>Products in an inventory</b> (674) counts software, not deployments: one row is WordPress, another is a Linux distribution's package.</li>
</ul>
<p>The number a reader actually wants, how many systems were exploitable at a given hour and how many were exploited, does not exist in any captured source. What exists is a set of signals, on <a href="../exploitation/index.html">the exploitation page</a>.</p>''')}
'''
    page('numbers/index.html', 'The numbers: 70%, 30 million, 2.6 million, 6,000, 674', 'Every scale figure in circulation about php2shell, with what it measures, who said it, whether anyone checked it, and why they differ by four orders of magnitude.', body, kind='analysis', topics='php2shell numbers scale')

def build_agencies():
    ag = D['agencies']
    offl = Counter(a['offline'] for a in ag)
    rows = [[f'<b>{E(a["agency"])}</b><br><span class="small">{E(a["country"])}</span>', E(a['published']), f'{pill(a["offline"])}<div class="note">{E(a["offline_text"])}</div>', E(a['exploitation']), E(a['note']), src_links(a['sources'], 1)] for a in ag]
    summary = ', '.join(f'{n} say <i>{E(k)}</i>' for k, n in sorted(offl.items(), key=lambda kv: -kv[1]))
    body = f'''
<h1>The agencies, side by side</h1>
<p class="lead">{len(ag)} national and supranational bodies, each read from its own page. The question that divides them is not whether to patch (all say patch) but what to do with a system that cannot be patched now. Of {len(ag)}: {summary}. Two could not be read because their sites block automated browsers; the block is recorded.</p>
<p>The BBC's morning framing, <q>the UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline</q>, holds for the NSA and CISA, is a simplification of the NCSC's fourth of six steps, and is not supported by the Australian page at all. The sentence the BBC quotes from the NCSC is not on the NCSC page as captured; its opening matches the Canadian text.</p>
{table(['Agency', 'Published', 'Offline?', 'Exploitation', 'Note', 'Sources'], rows, 'ag')}
<p>Each agency's full text is in its capture; the sentences here are the ones the collectors copied verbatim into their notes. Translations from French, Italian, Latvian and Japanese are this site's and are marked as such in the notes.</p>
'''
    page('agencies/index.html', 'What sixteen agencies actually advise', 'The NSA, CISA, the UK NCSC, CERT-EU, ENISA, CERT-FR, Canada, Australia, New Zealand, the Netherlands, Italy, Switzerland, Latvia, Japan, Spain and Portugal on php2shell: who says take it offline, who says isolate, who says patch and nothing more, and who has seen exploitation.', body, kind='analysis', topics='php2shell agencies advisories')

def build_affected():
    a, sw = D['affected'], D['software']
    st18, st19 = sw['by_status_109618'], sw['by_status_109619']
    sup = Counter((r.get('supplier') or '').strip() for r in sw['rows'])
    top = sorted(sup.items(), key=lambda kv: (-kv[1], kv[0]))[:15]
    vuln = [r for r in sw['rows'] if r.get('status_109618') == 'Vulnerable' or r.get('status_109619') == 'Vulnerable']
    fixed = [r for r in sw['rows'] if r.get('status_109618') == 'Fix' and r.get('status_109619') == 'Fix']
    body = f'''
<h1>Affected systems</h1>
<p class="lead">Three layers: the PHP versions, the ways PHP is attached to a web server, and the software that runs on top. The first two come from the PHP project. The third comes from NCSC-NL's public inventory, which this site counts rather than quotes: {sw["count"]} products at commit <code>{E(sw["commit"] or "")}</code>, of which {st18.get("Vulnerable", 0)} are marked vulnerable to CVE-2026-109618, {st18.get("Fix", 0)} fixed, {st18.get("Investigation", 0)} under investigation and {st18.get("Not vuln", 0)} not vulnerable.</p>
{section("versions", "Versions", table(['Branch', 'Affected', 'Fixed', 'In the CVE record'], [[E(r['branch']), E(r['affected']), E(r['fixed']), 'yes' if r['in_cve'] else '<b>no</b>'] for r in a['ranges']]) + f'<p>{E(a["ranges_note"])} <span class="refs">{src_links(a["ranges_sources"], 1)}</span></p>')}
{section("sapis", "Deployments", table(['SAPI', 'Risk', 'What the primary sources say', 'Sources'], [[E(s['sapi']), E(s['risk']), E(s['text']), src_links(s['sources'], 1)] for s in a['sapis']]))}
{section("apps", "Applications", f'<p>{E(a["applications_confirmed"]["text"])} <span class="refs">{src_links(a["applications_confirmed"]["sources"], 1)}</span></p>')}
{section("inventory", "The NCSC-NL inventory, counted", table(['Status', 'CVE-2026-109618', 'CVE-2026-109619'], [[E(k), E(str(st18.get(k, 0))), E(str(st19.get(k, 0)))] for k in ['Vulnerable', 'Fix', 'Investigation', 'Not vuln', 'none']]) + f'''
<p>NCSC-NL generates the list from an SPDX 3 inventory with VEX statements and says an entry is an investigation lead until a vendor or upstream backs it. {len(fixed)} products carry a fix for both CVEs; {len(vuln)} are marked vulnerable to at least one. The suppliers with the most entries:</p>''' + table(['Supplier', 'Entries'], [[E(s), E(str(n))] for s, n in top]) + f'<p><a href="software.html">The full inventory, all {sw["count"]} rows &rarr;</a> The parsed file is in the vault as <code>{E(sw["file"])}</code>; the repository bundle and tree at the same commit are there too. <span class="refs">{src_links(["ncsc-nl-php2shell-software-list", "ncsc-nl-php2shell"], 1)}</span></p>')}
'''
    page('affected/index.html', 'Affected systems: versions, deployments, applications, inventory', f'Which PHP versions and SAPIs php2shell affects, which applications had RCE demonstrated, and the NCSC-NL inventory of {sw["count"]} products counted by status.', body, kind='analysis', topics='php2shell affected inventory')
    rows = []
    for r in sw['rows']:
        links = ' '.join(f'<a href="{E(u)}" rel="noopener nofollow">{E(re.sub(r"^https?://(www\.)?", "", u).split("/")[0])}</a>' for u in (r.get('links') or [])[:3])
        rows.append([E(r.get('supplier') or ''), E(r.get('product') or ''), E(r.get('version') or ''), pill(r.get('status_109618') or 'none'), pill(r.get('status_109619') or 'none'), E((r.get('notes') or '').split('\n')[0][:220]), links])
    body = f'''
<h1>The NCSC-NL software inventory</h1>
<p class="lead">All {sw["count"]} rows of NCSC-NL's php2shell inventory at commit <code>{E(sw["commit"] or "")}</code>, as parsed into the vault. Status is NCSC-NL's per CVE; the note is the first line of theirs. Licence EUPL-1.2. This page is generated from the parsed file and changes only when the vault does. <span class="refs">{src_links(["ncsc-nl-php2shell-software-list", "ncsc-nl-php2shell"], 1)}</span></p>
{table(['Supplier', 'Product', 'Version', '109618', '109619', 'NCSC-NL note', 'Links'], rows, 'sw')}
'''
    page('affected/software.html', f'The NCSC-NL inventory: {sw["count"]} products', f'Every row of the NCSC-NL php2shell software inventory at commit {sw["commit"]}, with its status per CVE.', body, kind='evidence', topics='php2shell inventory')

def build_exploitation():
    rows = [[E(fmt_at(x['when'])), E(x['who']), E(x['what']), E(x['kind']), pill(x['status']), src_links(x['sources'], 1)] for x in sorted(D['exploitation'], key=lambda x: x['when'])]
    body = f'''
<h1>Exploitation: the signals, in order</h1>
<p class="lead">A remote code execution bug is not an invisibility cloak. If millions of systems were being exploited, the signals would be everywhere: honeypots, WAF logs, national CERTs, the KEV catalog. What the captured sources carry is {len(D["exploitation"])} signals, from one honeypot hit four days before disclosure to one agency's unattributed <q>reports of active exploitation</q>, and no confirmed compromise of a named system. That is the state as of the latest capture, and this page will change.</p>
{table(['When (UTC)', 'Who', 'What', 'Kind', 'Status', 'Sources'], rows, 'ex')}
{section("look", "What exploitation would look like", '''
<ul>
<li><b>On the host:</b> CISA's signal is <q>PHP worker processes launching shells or downloading tools</q>. The exploit runs as the web worker, so a worker spawning <code>sh</code>, <code>curl</code> or <code>wget</code>, or writing outside its document root, is the thing to alert on.</li>
<li><b>In the request log:</b> CERT-FR's workaround is to block or monitor multipart requests, because the confirmed session path rides on session upload progress; php.net's limits are on decoded request size, field count, multipart part count, header count and nesting depth. Unusual values of those are the request-side signal for the OOM path.</li>
<li><b>What a clean log does not prove:</b> JPCERT warns that with several exploit paths, one detection rule can miss an attack and the absence of traces does not prove the absence of compromise. The UK NCSC says a system that cannot be patched or disabled should be assessed for backdoors.</li>
<li><b>Upstream:</b> Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads; a WAF is a signal source as well as a control, and the Swiss agency's caveat is that it is not a sufficient control on its own.</li>
</ul>
<p class="refs">''' + src_links(['cisa-alert-php-20261021', 'certfr-2026-ale-014', 'php-net-advisory', 'jpcert-at260033', 'ncsc-news-php', 'cloudflare-blog-php2shell-waf', 'ch-bacs-warnung-php'], 1) + '</p>')}
{section("kev", "The Known Exploited Vulnerabilities catalog", f'<p>CISA adds a CVE to KEV when it has reliable evidence of exploitation in the wild. At catalog version 2026.10.21, released 2026-10-21 14:04:39 UTC and fetched 2026-10-22 08:15 UTC, neither CVE-2026-109618 nor CVE-2026-109619 is listed; the catalog has 1,754 entries and its newest additions are dated 20 October. CISA\'s vulnerability-enrichment assessment on both CVE records at 14:34 UTC says exploitation <i>none</i>. This is a point-in-time negative finding; the vault keeps the file and its hash so that the time can be proven later. <span class="refs">{src_links(["cisa-kev-json", "cisa-kev-catalog", "cve-cve-2026-109618"], 1)}</span></p>')}
'''
    page('exploitation/index.html', 'Exploitation signals, in order', 'Every signal of php2shell exploitation in the captured sources, from an Amazon honeypot hit on 17 October to the KEV catalog, with what exploitation would look like on a host.', body, kind='story', topics='php2shell exploitation detection')

def build_discovery():
    cols = [
        ('Calif', ['2026-07-30 audit begins under Patch the Planet', '2026-08-01 multiple paths to RCE found', '2026-08-05 hash commitment posted on X', '2026-08-11 first bug reported to PHP', '2026-08-14 RCE PoC shared; confirmed 08-15', '2026-08-21 second bug reported'], ['calif-php2shell', 'x-lcfr-hax-hash-tweet']),
        ('OpenAI', ['2026-08-11 same root cause reported, same day as Calif (per the Foundation)', '2026-09-18 further attack vectors', 'coalition of maintainers, researchers and providers over two months', 'credit: amyb-oai on both advisories'], ['php-foundation-blog-security-release', 'x-openai-php2shell', 'github-ghsa-w8hw-w9fx-j79w']),
        ('Wiz', ['2026-08-19 first vulnerability found (Wiz Atlas, Gemini 4 Argon, GPT-5.6 Sol)', '2026-08-20 RCE confirmed on Drupal', '2026-08-21 RCE confirmed on WordPress', '2026-08-24 reported to PHP', '2026-09-21 PHP acknowledges', 'credit: sagitzadik-wiz'], ['wiz-blog-php2shell']),
        ('Before them', ['2024 Quarkslab audit (OSTIF, Sovereign Tech Agency) surfaces the OOM issue', '2024 a Foundation-contracted developer finds first signs; exploit theorised, no vector', 'credit: tomash-areion on both advisories, named nowhere else'], ['php-foundation-blog-security-release', 'calif-php2shell', 'github-ghsa-6wmf-4rv5-p3rp']),
    ]
    grid = ''.join(f'<div class="col"><h3>{E(name)}</h3><ul>{"".join(f"<li>{E(i)}</li>" for i in items)}</ul><p class="refs">{src_links(srcs, 1)}</p></div>' for name, items, srcs in cols)
    cl = [c for c in D['claims'] if c['topic'] == 'discovery']
    body = f'''
<h1>Who found it, and how</h1>
<p class="lead">Three research parties say they found php2shell, and all three say AI helped. Their own timelines, placed side by side, do not conflict on dates: Calif first (1 to 11 August), OpenAI the same day as Calif's report, Wiz independently eight days later. They conflict on framing: Wiz's <q>Wiz Research uncovers</q>, OpenAI's <q>frontier AI was able to find this vulnerability ahead of attackers</q>, and a Community Note on OpenAI's post pointing at Calif's August hash.</p>
<div class="cols">{grid}</div>
{section("ai", "What the AI did", '''
<p>The honest answer from the captured sources is: not enough is said. Calif says <q>No special harness, or access to models that weren't generally available to everyone were used in the initial bug discovery</q> and that the researcher <q>asked my LLM companion for help</q>; it names no model. Wiz names three tools and quotes Google DeepMind's head of Gemini security: <q>a single researcher completed in a week what previously would have taken a world-class team months of work.</q> OpenAI's blog, which reportedly names GPT-5.6 Sol, is behind a bot challenge from this capture environment. The PHP Foundation adds that the project was separately scanned with Anthropic's Claude Mythos through Alpha-Omega and that OpenAI's Daybreak Red validated reports and exploits.</p>
<p>What is established is the shape: a bug class seen in 2024 and left because nobody could prove exploitation, then three groups with model assistance finding working exploits within three weeks of each other in August 2026. The BBC's quote, <q>a complex chain of steps, at the edge of what human researchers could practically achieve</q>, is not on any captured researcher page.</p>
<p class="refs">''' + src_links(['calif-php2shell', 'wiz-blog-php2shell', 'openai-blog-coordinated-disclosure', 'php-foundation-blog-security-release', 'bbc-live-ckgel5xp2xv9t'], 1) + '</p>')}
{section("claims", "The claims on discovery", claim_rows(cl, 1))}
'''
    page('discovery/index.html', 'Who found php2shell, and what the AI did', 'Calif, OpenAI and Wiz each claim the discovery of php2shell; their own timelines side by side, the 2024 audit that saw it first, the credits on the advisories, and what the sources do and do not say about the models.', body, kind='story', topics='php2shell discovery ai')

def build_leak():
    evs = sorted([t for t in D['timeline'] if t.get('phase') in ('leak', 'release') or t['at'].startswith('2026-10-20')], key=lambda t: t['at'])
    rows = [[f'<span class="when">{E(fmt_at(t["at"]))}</span>', E(t['event']) + (f'<div class="note">{E(t["note"])}</div>' if t.get('note') else ''), pill(t['confidence']), src_links(t['sources'], 1)] for t in evs]
    cl = [c for c in D['claims'] if c['topic'] in ('leak', 'timing')]
    body = f'''
<h1>How the disclosure broke</h1>
<p class="lead">The plan was 22 October at 14:00 UTC. From about 15:00 UTC on 20 October the CVE IDs were loose with a wrong score; by 19:30 the project had pre-announced a release a day early; by 20:00 one of the reporters had published a demonstration video; by 23:00 mitigation advice was going to critical-infrastructure providers; by 02:00 on the 21st Amazon was seeing proof-of-concept attempts; by 03:02 Cloudflare's rules were live; by 07:41 Chainguard had shipped patched images; by 08:36 a sensor network had its first hit. The release went out at 13:34 UTC. Every one of those times is from a party's own account, and the parties disagree on what was leaked and by whom.</p>
{table(['When (UTC)', 'What', 'Time is', 'Sources'], rows, 'tl')}
{section("accounts", "Three accounts of what leaked", '''
<ul>
<li><b>The PHP Foundation:</b> the CVE IDs, a wrong release time and a wrong CVSS; <q>No technical details leaked.</q> Then Calif's video, then possibly the mitigation advice, then Chainguard's images.</li>
<li><b>Alexandre Daubois (PHP security team, writing personally):</b> an anonymous Hacker News post citing a reliable source, screenshots of it, a screenshot of the <q>PHP2Shell tool</q> credited to Calif.io <q>alongside the advisory</q>, a short exploitation video, and watchTowr confirming both CVE numbers in public.</li>
<li><b>The Hacker News:</b> <q>details about the CVE identifiers and a proof-of-concept (PoC) exploit leaked ahead of time</q>, and Amazon's evidence that somebody was trying an exploit four days before any of this.</li>
</ul>
<p>Calif's own write-up has a timeline that ends <q>October 21 Patched versions released</q> and does not mention a leak, a deleted video, or the Foundation's account. Chainguard's reply is behind a bot challenge; the search snippet says it does not dispute the time and denies leaking. The vault records both blocks.</p>
<p class="refs">''' + src_links(['php-foundation-blog-security-release', 'daubois-blog-php2shell-rumors', 'thehackernews-php2shell-4days', 'calif-php2shell', 'techzine-php-chainguard'], 1) + '</p>')}
{section("claims", "The claims on the leak and on timing", claim_rows(cl, 1))}
'''
    page('leak/index.html', 'How the coordinated disclosure broke', 'Hour by hour from the first circulation of the CVE IDs on 20 October to the release on 21 October: the pre-announcement, the deleted video, the early WAF rules, the embargo break, the first attempts, and the three accounts that disagree on what leaked.', body, kind='story', topics='php2shell leak disclosure')

def build_playbook():
    steps = [
        ('0', 'Know what you run', 'Inventory every system with PHP serving web requests, including the ones you did not build: appliances, vendor products, hosting panels, the thing marketing bought. Do not limit discovery to old versions. Note the SAPI (mod_php, FPM, cgi, FrankenPHP, LiteSpeed) and the PHP branch.', ['ncsc-news-php', 'cisa-alert-php-20261021', 'nsa-press-php-4630238', 'ncsc-nl-php2shell-software-list']),
        ('1', 'Patch, internet-facing first', 'Update to 8.5.12, 8.4.27, 8.3.36 or 8.2.35, or your distribution\'s backported package. Restart every worker; rebuild containers. For 7.4, 8.0 and 8.1 there is a source backport branch and no release: plan the migration now. Some third-party repositories (remirepo) had no packages on release day.', ['php-net-advisory', 'ch-bacs-warnung-php', 'github-php-src-branch-7.4-backport', 'certeu-sa-2026-018']),
        ('2', 'If you cannot patch today, apply the temporary mitigations', 'memory_limit=-1 where applications cannot override it; low post_max_size with proxy-level request limits; a cgroup memory limit instead of RLIMIT; session.upload_progress.enabled=0 then restart every worker; on 8.5 fatal_error_backtraces=0; pm.max_requests=1 on FPM. Each blocks a known path and none makes the installation safe.', ['php-net-advisory', 'github-ghsa-6wmf-4rv5-p3rp', 'ncsc-nl-php2shell']),
        ('3', 'Put something in front', 'A WAF may provide some protection (CISA); it is not sufficient on its own (Swiss BACS); it blocked what Cloudflare saw while attackers mutated payloads. CERT-FR\'s edge workaround is to block or monitor multipart Content-Type requests. Restrict access to the people and systems that need it.', ['cisa-alert-php-20261021', 'ch-bacs-warnung-php', 'cloudflare-blog-php2shell-waf', 'certfr-2026-ale-014']),
        ('4', 'Isolate or take offline', 'Where none of the above is feasible in time: CERT-EU, Canada and France say isolate internet-facing applications from public networks; the NSA and CISA say take the system offline until fully mitigated; the UK NCSC puts this fourth; Latvia geo-blocked state services from abroad for days. Decide who can make that call and how fast it can be executed, and write it down before you need it.', ['certeu-sa-2026-018', 'cccs-al26-026', 'certfr-2026-ale-014', 'nsa-x-2112903220209098897', 'cisa-alert-php-20261021', 'ncsc-news-php', 'certlv-php-preventive']),
        ('5', 'Look for compromise', 'PHP workers launching shells or downloading tools; unexpected files under the web root; outbound connections from the web tier; anomalous multipart or oversized requests. A clean log does not prove a clean system (JPCERT); a system that could not be patched or disabled promptly should be assessed for backdoors (NCSC UK).', ['cisa-alert-php-20261021', 'jpcert-at260033', 'ncsc-news-php', 'ncsc-nz-alert-php']),
        ('6', 'Verify, then keep watching', 'Confirm the running version after the restart, not the package version before it. Check vendors that bundle PHP for their own fixes. Watch for a follow-up release: a report that the 8.5.12 fix may be incomplete reached oss-security within two hours and has not been answered on-list.', ['ch-bacs-warnung-php', 'ncsc-nl-php2shell', 'openwall-oss-security-109619-thread']),
    ]
    rows = ''.join(f'<li><span class="n">{E(n)}</span><div><h3>{E(t)}</h3><p>{E(w)}</p><p class="refs">{src_links(s, 1)}</p></div></li>' for n, t, w, s in steps)
    body = f'''
<h1>If you run PHP</h1>
<p class="lead">Every agency's advice, merged into one ordered list, with the sentence each step comes from. This is a guide to what the sources say, assembled by agents and not reviewed by your security team; the php.net advisory is the authority and your national agency is the one that applies to you. Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says <q>isolate, then migrate</q>.</p>
<ol class="steps">{rows}</ol>
{section("plug", "Pulling the plug, as a capability", '''<p>Four agencies told organisations to be ready to take systems offline within hours. How long it takes you to do that for one system, cleanly, with a holding page and a way back, is a measurable property of your stack, and it is the property this incident tested. A system that can be removed from the internet in minutes without data loss is one you can afford to leave running until the patch is tested; a system that cannot is one you take offline early, because you will not be able to later. The site's own position is that the decision belongs to a named person and the execution belongs to a rehearsed runbook, and that the inventory in step 0 is where both start.</p>''')}
<p>The technical detail behind each step is on <a href="../flaws/index.html">the two flaws</a>; which versions and products are in scope is on <a href="../affected/index.html">affected systems</a>; what the agencies said, agency by agency, is on <a href="../agencies/index.html">the agencies</a>.</p>
'''
    page('playbook/index.html', 'If you run PHP: the steps, in order, with their sources', 'Inventory, patch, mitigate, shield, isolate or take offline, look for compromise, verify: every agency\'s php2shell advice merged into one ordered list with the sentence each step comes from.', body, kind='story', topics='php2shell playbook mitigation')

def build_briefings():
    aud = D['roles']['audiences']
    sel = {
        'board': dict(topics=['scale', 'exploitation', 'advice', 'impact'], intro='Three decisions sit with you: whether the organisation is exposed, what it costs to find out, and who may pull a system. The facts below are the ones those decisions turn on. Everything marked <i>reported</i> is one party\'s word; nothing below is a confirmed compromise anywhere.', ask=['Do we have an inventory of every system serving PHP, including vendor products? If not, that is the first spend.', 'Has every internet-facing system been patched and restarted, and has the running version been checked after the restart?', 'Who is authorised to take a system offline, how long does it take, and has it been rehearsed?', 'What would a compromise of our most exposed PHP system reach: which data, which credentials, which other systems?', 'What is our evidence that we were not exploited between the leak on 20 October and our patch?']),
        'security': dict(topics=['technical', 'exploitation', 'advice', 'scale'], intro='Patch order, mitigations, signals and the offline decision. The claims are grouped so that the ones your runbook depends on come first.', ask=['Internet-facing mod_php first, then FPM, then everything else; 7.4 to 8.1 need a migration plan, not a package.', 'Apply the temporary mitigations where patching slips, and record that each one blocks a known path only.', 'Alert on PHP workers spawning shells or fetching tools; log multipart and oversized requests at the edge.', 'Decide the isolate-or-offline threshold now and name who calls it.', 'Re-check KEV and oss-security daily: the exploitation picture and the incomplete-fix question will both move.']),
        'engineer': dict(topics=['technical'], intro='Versions, SAPIs, settings and what each does. The claims are the primary records\' own words where they exist.', ask=['Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker; rebuild images.', 'memory_limit=-1 via php_admin_value; post_max_size 8M or 32M; cgroup limits not RLIMIT; session.upload_progress.enabled=0 in php.ini or the pool, never ini_set; fatal_error_backtraces=0 on 8.5; pm.max_requests=1.', 'The CVE record calls 7.4 to 8.1 unaffected by omission; the backport branches say otherwise. Do not trust a scanner on this.', 'The 8.5.12 fix may have a follow-up; watch php.net and oss-security.', 'Verify the running version with phpinfo or php -v inside the container, after the restart.']),
        'journalist': dict(topics=['scale', 'discovery', 'leak', 'timing', 'advice'], intro='Which numbers hold up, who said what first, which quotes are on the page they are attributed to, and what nobody has verified. Every row links to the captured source so the quote can be checked against the bytes.', ask=['The 70% figure is a share of websites that use PHP, restated as a share of the Internet; no page on this beat sources it.', 'The release was 21 October 13:34 to 14:06 UTC, not 22 October; the php.net changelog still says 22.', 'The sentence the BBC attributes to the NCSC is not on the NCSC page as captured; the opening matches Canada\'s text.', 'Australia\'s agency gives no offline advice; the EU\'s says isolate.', 'Three parties claim discovery; their own dates do not conflict, their framing does. The Foundation says Calif and OpenAI reported the same root cause on the same day.']),
        'researcher': dict(topics=['technical', 'discovery', 'leak'], intro='Bug classes, what was demonstrated against what, credits, and the open technical questions.', ask=['Two classes: OOM longjmp leaving request memory uninitialised (CWE-416/755/824/1325/1419), and worker global state pointing at freed request memory across requests.', 'mod_php exploited pre-application with default limits; FPM via session upload progress for 109619; FPM for 109618 disputed between the GHSA and the Foundation blog.', 'Credits on both GHSAs: lcfr-hax, sagitzadik-wiz, amyb-oai, tomash-areion. The last is unexplained.', 'Open: the Fediverse report of a third bug or incomplete fix; Calif\'s hash pre-image; whether the embedded demo is the deleted video.', 'The fix changes the engine: soft OOM at a VM safe point, hard OOM via _exit(). Expect behavioural differences under memory pressure.']),
        'ciso': dict(topics=['exploitation', 'impact', 'advice', 'scale', 'technical'], intro='Exposure, evidence of non-compromise, and the board message. Three facts carry this briefing: the bug is in the runtime so your application code is not the question; attempts are in the millions at one CDN but no named victim is confirmed anywhere; and every agency says patch first, with offline as the fallback not the reflex.', ask=['Exposure is a list, not a percentage: every internet-facing system serving PHP, with SAPI, version and what sits behind it. Vendor appliances and hosting panels count.', 'Evidence of non-compromise means log review from 17 October (Amazon\'s earliest attempt), not from the 21st, and host checks for shells spawned by PHP workers, not just WAF hits.', 'The board line: a critical runtime flaw, patched on day one where we could, isolated where we could not, no evidence of compromise as of today, review continuing. Do not quote 70%.', 'Edge rules were live hours before disclosure; if you are behind a major CDN you had a stopgap you did not have to ask for. It is not a control you can rely on.', 'Expect a follow-up release: a report that the first fix is incomplete reached the security list within two hours.']),
        'cto': dict(topics=['technical', 'advice', 'timing'], intro='What the patch changes, what it breaks, and what to change afterwards. The fix is a redesign of how PHP handles running out of memory, so behaviour under memory pressure changes, and it touched 389 files.', ask=['Patch order: mod_php on the internet first; FPM next; everything else after. Restart every worker, rebuild every image, then verify the running version inside the container.', 'The new memory_hard_limit_percent and max_multipart_body_parts settings exist now; the defaults are conservative, and a system that used to survive on the edge of memory_limit may now _exit instead.', '7.4, 8.0 and 8.1 have a source backport and no release: that is a migration you are now doing, not a patch.', 'The engineering lesson is time-to-pull-the-plug: how long it takes to take one system off the internet cleanly, with a holding page and a way back, is a property of your platform and it was measured this week whether you wanted it or not.', 'What to change: an inventory that answers "where is PHP" in minutes; worker-process monitoring (a PHP worker spawning a shell is the signal); a rehearsed isolate runbook with a named owner.']),
        'cfo': dict(topics=['impact', 'scale', 'exploitation'], intro='The financial question has two sides and the evidence is lopsided: downtime is documented and measurable; breach is claimed and unconfirmed. Insurers are already treating this as an aggregation event.', ask=['Cost of acting: operators that pulled sites report hours to a day offline; one operator served 94% of its page views from cache through a 13-hour shutdown. Engineering time to patch, restart and verify is the main cost for most.', 'Cost of not acting: an unauthenticated code-execution flaw in the web tier; what it reaches is whatever that tier can reach, which is a question for the CISO\'s inventory, not for a percentage.', 'Insurance: Insurance Business reports underwriters watching for an aggregation event and asks whether business-interruption cover responds to a precautionary shutdown with no breach; that depends on wording and waiting periods. Ask the broker now, in writing.', 'Figures you will hear and should not use in a forecast: 70% of the Internet (a share of websites restated), 30 million websites (no basis), 22.6 million systems (method not given). Use your own inventory count.', 'No named organisation has confirmed a compromise as of the latest capture. That is a statement about evidence, not about safety.']),
        'appsec': dict(topics=['technical', 'advice', 'exploitation'], intro='Scope, settings and the pipeline change. The bug is below your applications: any PHP endpoint that reaches the runtime is a candidate, and the demonstrated paths run before application code.', ask=['In scope: every application on an affected runtime, including the ones with no uploads and no sessions; the session upload-progress path is on by default and needs no session_start().', 'Settings that bound the known paths, in the order of least breakage: session.upload_progress.enabled=0 (server-level, not ini_set); post_max_size low; max_input_nesting_level low; max_multipart_body_parts on patched builds; fatal_error_backtraces=0 on 8.5; pm.max_requests on FPM. None is a fix.', 'The runtime version in production is now an application-security finding: add it to the SBOM, fail the pipeline on an unfixed PHP, and check the running version after deploy, not the package version before.', 'Detection belongs at the edge and on the host, not in the app: the request shape (upload-progress field plus many array parts, oversized multipart bodies) and the process tree (a worker spawning a shell).', 'The public proof-of-concept code does not work as published, per VulnCheck and a lab reproduction; a scanner that fires on it is testing the wrong thing.']),
        'developer': dict(topics=['technical'], intro='Your code is not the problem and cannot be the fix. The flaw is in the C engine that runs it. What you can do is check the box you deploy to and avoid making the engine\'s job harder.', ask=['Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.', 'Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35. If your target is 8.1 or older there is no release; tell whoever owns the platform today.', 'Nothing in userland blocks the demonstrated paths: ini_set() runs too late, .user.ini runs too late, auto_prepend_file runs too late. The settings have to be in php.ini, the pool or the server config.', 'Fix attacker-reachable fatal errors and timeouts in your own code anyway: the advisory lists them as one of the paths for the stale-state bug.', 'After the patch, out-of-memory behaves differently: a delayed fatal at the next safe point instead of an abort, and a hard limit that ends the process. Code that caught the old behaviour in tests will see a change.']),
        'comms': dict(topics=['scale', 'impact', 'discovery', 'advice'], intro='What is true, what is not, and what you will be asked. The story most readers saw on the morning of 22 October carried three things this site could not confirm, and the questions will come from that story.', ask=['True and safe to say: two critical flaws in PHP itself, patched on 21 October; the organisation patched or isolated its systems; no evidence of compromise as of today, review continuing.', 'Not safe to say: "70% of the Internet" (a headline restating a share of websites), "the most severe ever" (a vendor\'s phrase), "exploited everywhere" (attempts against honeypots and CDNs, no named victim), "found by AI" without "by researchers using".', 'The questions: Were you hit? (answer with the evidence window: logs reviewed from 17 October.) Did you take sites down? (precaution, not incident, as Oxford City Council put it.) Why did it take so long? (the fix was authored on 18 October and released under a coordinated plan that leaked.)', 'Attribution: three research teams and the PHP Foundation each tell the discovery story differently; do not pick one. The flaw was seen in 2024 and not fixed because exploitation could not be shown.', 'Point at primary sources: php.net\'s advisory and your national agency. Do not link a vendor blog as the authority.']),
        'analyst': dict(topics=['discovery', 'leak', 'timing', 'scale', 'exploitation'], intro='What this incident says about coordinated disclosure once models can find bugs, and once a leak can become a proof of concept faster than a patch can ship. The claims below are the evidence; the reading is the site\'s.', ask=['The window between leak and release was 22.5 hours and the window between first honeypot hit and release was four days. Both are shorter than the two months the fix took.', 'Three AI-assisted teams converged on a bug class seen and shelved in 2024. The constraint that failed in 2024 was proving exploitability, and that is what models now appear to lower the cost of.', 'The defensive side moved early too: WAF rules 9 hours ahead, images 6 hours ahead (against the embargo), agencies within the hour. The system is faster in both directions.', 'The public numbers were not produced for decision-making and should not be used for it; the one agency that counted got about 6,000 in a country of 1.9 million people.', 'Agencies diverged on the hardest question, offline or not, along lines that look institutional rather than technical.']),
    }
    for a in aud:
        s = sel[a['id']]
        cl = [c for c in D['claims'] if c['topic'] in s['topics']]
        order = {t: i for i, t in enumerate(s['topics'])}
        cl.sort(key=lambda c: (order[c['topic']], list(STATUS_WORDS).index(c['status']) if c['status'] in STATUS_WORDS else 9))
        asks = ''.join(f'<li>{x}</li>' for x in s['ask'])
        openq = ''.join(f'<li>{o["html"]}</li>' for o in STORY['open'][:5])
        body = f'''
<p class="kicker">Briefing &middot; {E(a["name"])} &middot; from the same {C["claims"]} claims, selected and ordered for one reader</p>
<h1>{E(a["question"])}</h1>
<p class="lead">{s["intro"]}</p>
{section("decide", "What to decide or do", f'<ul class="asks">{asks}</ul>')}
{section("facts", "The facts this rests on", status_legend() + claim_rows(cl, 2))}
{section("open", "What is still open", f'<ul class="open">{openq}</ul>')}
<p>The full set of claims is on <a href="../../claims/index.html">every claim</a>; the ordered steps for a vulnerable system are on <a href="../../playbook/index.html">if you run PHP</a>. Other briefings: {" &middot; ".join(f'<a href="../{b["id"]}/index.html">{E(b["name"])}</a>' for b in aud if b["id"] != a["id"])}.</p>
'''
        page(f'briefings/{a["id"]}/index.html', f'Briefing for a {a["name"].lower()}: {a["question"]}', f'The php2shell story for a {a["name"].lower()}: what to decide, the claims it rests on with their status and sources, and what is still open.', body, kind='briefing', topics=f'php2shell briefing {a["id"]}')

def build_sources():
    kinds = Counter(s.get('kind') for s in D['sources'])
    rows = ''
    for s in D['sources']:
        caps = ''
        for c in s['captures']:
            files = ''.join(f'<li><code>{E(fn)}</code> <span class="h">{E(f["sha256"])}</span> <span class="small">{f["bytes"]:,} bytes</span></li>' for fn, f in sorted(c['files'].items()))
            err = f' <span class="small">error: {E(str(c["error"]))}</span>' if c.get('error') else ''
            caps += f'<details><summary>capture <code>{E(c["stamp"])}</code> &middot; HTTP {E(str(c.get("status")))} &middot; {E(str(c.get("final_url") or ""))}{err}</summary><ul class="files">{files}</ul></details>'
        raw = ''
        if s.get('raw_sha256'):
            raw = '<details><summary>raw, ' + str(len(s['raw_sha256'])) + ' files with SHA256SUMS</summary><ul class="files">' + ''.join(f'<li><code>{E(fn)}</code> <span class="h">{E(h)}</span></li>' for fn, h in s['raw_sha256'].items()) + '</ul></details>'
        rows += f'''<article class="source" id="{E(s["slug"])}">
<h3><a href="{E(s["slug"])}/index.html">{E(s.get("title") or s["slug"])}</a> <a class="small" href="{E(s["url"])}" rel="noopener nofollow">original &#8599;</a></h3>
<p class="meta"><b>{E(s.get("publisher") or "")}</b> &middot; {E(s.get("kind") or "")} &middot; {"primary" if s.get("primary") else "secondary"} &middot; {pill(s.get("status") or "")} &middot; published {E(str(s.get("published") or "not stated"))} &middot; added by <code>{E(s.get("added_by") or "")}</code> &middot; <code>{E(s["slug"])}</code></p>
<p class="small">{E(s.get("notes") or "")}</p>
{caps}{raw}
</article>'''
    kinds_t = table(['Kind', 'Sources'], [[E(k or 'other'), E(str(n))] for k, n in sorted(kinds.items(), key=lambda kv: (-kv[1], kv[0]))])
    body = f'''
<h1>Every source, every capture, every hash</h1>
<p class="lead">{C["sources"]} sources, {C["primary"]} of them primary, {C["captures"]} dated captures and {C["hashed"]} hashed files, from the evidence vault at commit <code>{E(D["vault"]["head"]["commit"] or "")}</code>. {C["blocked"]} sources could not be read because the site blocked an automated browser; the block, with the challenge page's hash, is the record. The captures are third-party pages held privately and are not republished; this page links to the originals and lists the SHA-256 of every captured file, so that anyone the vault is later opened to can check that the bytes are the ones the agents saw, at the minute they saw them.</p>
{kinds_t}
<p>Each capture holds <code>page.html</code> (as served), <code>rendered.html</code> (after scripts ran), <code>text.txt</code>, <code>screenshot.png</code>, <code>headers.json</code> and <code>provenance.json</code>. A <code>raw/</code> folder holds anything fetched another way, with its own checksum file. The manifest this page is built from is <a href="../data/sources.json">data/sources.json</a>.</p>
<div class="sources">{rows}</div>
'''
    page('sources/index.html', f'Every source: {C["sources"]} pages, {C["captures"]} captures, {C["hashed"]} hashes', f'The manifest of the php2shell evidence vault: every captured source with its publisher, kind, publication time, capture times, HTTP status and the SHA-256 of every captured file.', body, kind='evidence', topics='php2shell sources evidence')

def build_graph():
    claims = D['claims']
    used = OrderedDict()
    for c in claims:
        for s in c['sources']:
            if s in SOURCES:
                used.setdefault(s, 0)
                used[s] += 1
    src_list = sorted(used, key=lambda s: (-used[s], s))
    nodes = [{'id': 'claim:' + c['id'], 'kind': 'claim', 'label': c['claim'][:90], 'status': c['status'], 'topic': c['topic']} for c in claims]
    nodes += [{'id': 'source:' + s, 'kind': 'source', 'label': SOURCES[s].get('publisher') or s, 'publisher': SOURCES[s].get('publisher'), 'url': SOURCES[s]['url'], 'primary': bool(SOURCES[s].get('primary'))} for s in src_list]
    nodes += [{'id': 'event:' + str(i), 'kind': 'event', 'label': t['event'][:90], 'at': t['at']} for i, t in enumerate(D['timeline'])]
    edges = [{'from': 'claim:' + c['id'], 'to': 'source:' + s, 'rel': 'cites'} for c in claims for s in c['sources'] if s in SOURCES]
    edges += [{'from': 'event:' + str(i), 'to': 'source:' + s, 'rel': 'cites'} for i, t in enumerate(D['timeline']) for s in t['sources'] if s in SOURCES]
    graph = {'site': SITE, 'version': VERSION, 'vault_commit': D['vault']['head']['commit'], 'nodes': nodes, 'edges': edges,
             'note': 'A node is just a node; meaning lives in the edges. Every edge is a citation from a claim or an event to a captured source.'}
    write('data/graph.json', json.dumps(graph, indent=1, ensure_ascii=False) + '\n')
    # SVG: claims on the left, sources on the right
    rh = 16
    n_l, n_r = len(claims), len(src_list)
    H = max(n_l, n_r) * rh + 40
    W = 1000
    xl, xr = 330, 670
    y_l = {c['id']: 20 + i * (H - 40) / max(1, n_l - 1) for i, c in enumerate(claims)}
    y_r = {s: 20 + i * (H - 40) / max(1, n_r - 1) for i, s in enumerate(src_list)}
    lines = ''.join(f'<path class="e e-{E(c["status"])}" d="M{xl},{y_l[c["id"]]:.1f} C{xl+170},{y_l[c["id"]]:.1f} {xr-170},{y_r[s]:.1f} {xr},{y_r[s]:.1f}"/>' for c in claims for s in c['sources'] if s in y_r)
    left = ''.join(f'<a href="../claims/index.html#{E(c["id"])}"><text class="n n-{E(c["status"])}" x="{xl-6}" y="{y_l[c["id"]]+4:.1f}" text-anchor="end">{E(c["claim"][:46])}{"…" if len(c["claim"]) > 46 else ""}</text><circle class="d d-{E(c["status"])}" cx="{xl}" cy="{y_l[c["id"]]:.1f}" r="3"/></a>' for c in claims)
    right = ''.join(f'<a href="../sources/index.html#{E(s)}"><circle class="d d-src{" d-pri" if SOURCES[s].get("primary") else ""}" cx="{xr}" cy="{y_r[s]:.1f}" r="3"/><text class="n" x="{xr+6}" y="{y_r[s]+4:.1f}">{E(short_name(SOURCES[s]))} ({used[s]})</text></a>' for s in src_list)
    svg = f'<figure class="graph"><svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Claims on the left, sources on the right, one line per citation"><text class="t" x="{xl-6}" y="10" text-anchor="end">claims ({n_l})</text><text class="t" x="{xr+6}" y="10">sources cited ({n_r}), with how many claims cite each</text>{lines}{left}{right}</svg><figcaption>Every line is one citation. Colour is the claim\'s status: green confirmed, grey reported, amber disputed or contradicted, red unverified. A source with a filled dot is primary.</figcaption></figure>'
    body = f'''
<h1>The story as a graph</h1>
<p class="lead">{len(nodes)} nodes and {len(edges)} edges: {n_l} claims, {len(D["timeline"])} events and the {n_r} sources they cite. There is no second graph behind this one: the page, the briefings and the timeline are all drawn from the same rows, so the picture cannot disagree with the text. The JSON is <a href="../data/graph.json">data/graph.json</a>; this page shows the claims-to-sources slice.</p>
{svg}
{section("read", "How to read it", '''<ul>
<li>A claim with many lines to primary sources is well-founded; a claim with one line to a news page is one party's word relayed once.</li>
<li>The BBC live page sits near the top of the right column because the early claims all came through it; the work of the last day was to draw second lines from those claims to the pages the BBC was reporting on.</li>
<li>A source with no line is captured but not yet cited: a home page kept for context, a block recorded for the record, or a page whose claims nobody has traced yet. The sources page lists them all.</li>
<li>Events cite sources the same way; they are in the JSON and on the timeline, and are left off the drawing to keep it legible.</li>
</ul>''')}
'''
    page('graph/index.html', 'The story as a graph: claims, events and the sources they cite', f'{len(nodes)} nodes and {len(edges)} citation edges from the php2shell claims and timeline to the captured sources, drawn from the same rows as the text, with the JSON to download.', body, kind='evidence', topics='php2shell graph')

def build_method():
    v = D['vault']
    body = f'''
<h1>The method: capture, hash, claim, build, gate</h1>
<p class="lead">This site is the newsroom's <a href="{NEWSROOM}">PHP flaws section</a> taken to its conclusion: a site whose every sentence can be traced to bytes, rebuilt by a script from the vault, with no step a reader has to take on trust. It is also a test of the stack sgit.ai is building, and says so in its footer.</p>
{section("vault", "The evidence vault", f'''<p>A private, encrypted sgit vault, opened at {E(v["opened"])}, written to by {len(v["agents"])} agents and the editor. It holds {v["sources"]} sources and {v["captures"]} captures at commit <code>{E(v["head"]["commit"] or "")}</code>. Its protocol, in its own README: capture, don't paraphrase; captures are additive, never edited or deleted; one <code>source.json</code> and one <code>notes.md</code> per source, so agents never conflict on a shared manifest; claims and timeline rows in one file per agent; primary sources first, then news, then social posts, which get captured early because they get deleted; a blocked fetch is recorded with the block, so another agent can retry; and no keys or tokens in any file. The vault is private because it holds verbatim third-party pages for the record; this site publishes their hashes, their URLs and short quotations, and never the pages.</p>''')}
{section("status", "Five words for how far a claim can be trusted", status_legend() + '<p>A claim never gets a better word than its sources give it. A verbatim quote is marked as such and attributed to the page it is on; a quote attributed by one outlet to another party stays <i>reported</i> until the other party\'s page is captured and found to carry it. The one case so far where that check failed, the BBC\'s NCSC sentence, is on <a href="../agencies/index.html">the agencies page</a>.</p>')}
{section("determinism", "Deterministic, and why that matters", '''<p>The build reads <code>data/</code> and <code>VERSION</code> and writes every page. It has no clock, no random number and no network: run it twice and the output is byte-identical, which the gate checks. That means a page can be reproduced from the data at any version, a diff between two versions is a diff in the data, and a reader who doubts a page can rebuild it. Times on pages are the sources' times; the only date the site adds is the time of the latest capture, which is itself read from the vault.</p>
<ol>
<li><code>admin/build/export_vault.py --from &lt;vault clone&gt;</code> reads the vault and writes the manifest with every hash, the merged per-agent claims and timeline, the vault's HEAD and the software inventory counts. Never the captures.</li>
<li><code>admin/build/build.py</code> builds every page, its markdown twin, <code>data/graph.json</code> and <code>llms.txt</code>.</li>
<li><code>admin/build/validate.py</code> is the gate: every internal link resolves; every page is linked from somewhere and has a markdown twin and an llms.txt line; every claim and event cites a slug in the manifest; the build is byte-identical when run again; no em-dash in the site's prose; no credential shape anywhere in the tree.</li>
<li><code>admin/build/release.sh</code> bumps the version, builds, validates, runs the leak tripwire over the staged diff, pushes, and polls the live site for the new version before it will say the release is done.</li>
</ol>''')}
{section("agents", "For an agent", f'''<p>Everything on this site is in <code>data/</code> as JSON and every page has a markdown twin at the same path; <a href="../llms.txt">llms.txt</a> lists them. To add a source: capture it into the vault with the vault's tool, write its <code>source.json</code> and <code>notes.md</code>, add rows to your own <code>claims/&lt;agent&gt;.json</code> and <code>timeline/&lt;agent&gt;.json</code>, commit with your agent's name, push. To change this site: edit <code>data/</code>, run the build, run the gate. Do not edit a generated page; the build will overwrite it. The vault's claims and timeline files are exported as <a href="../data/vault-claims.json">vault-claims.json</a> and <a href="../data/vault-timeline.json">vault-timeline.json</a>; this site's own rows are in <a href="../data/claims.json">claims.json</a> and <a href="../data/timeline.json">timeline.json</a>, written by the agent <code>claude-story-site</code> from every note in the vault.</p>''')}
{section("replicate", "Replicate it for the next incident", '''<p>Nothing here is specific to PHP. The vault protocol, the capture tool, the five status words, the export, the build and the gate would carry a story about any incident, outage or disclosure. The repository is public under Apache-2.0 and CC BY 4.0; the next story starts by copying it, emptying <code>data/</code>, and opening a vault.</p>''')}
'''
    page('method/index.html', 'The method: capture, hash, claim, build, gate', 'How this site keeps evidence: the private vault and its protocol, the five status words, the deterministic build, the gate, and how an agent adds a source or replicates the whole thing for the next incident.', body, kind='free', topics='method provenance')

def build_team():
    r = D['roles']
    pipe = table(['Step', 'What', 'Who', 'How'], [[E(str(p['step'])), f'<b>{E(p["name"])}</b>', E(p['who']), E(p['what'])] for p in r['pipeline']])
    agents = ''.join(f'<article class="role" id="{E(a["id"])}"><h3>{E(a["name"])} <code>{E(a["id"])}</code></h3><p><b>Beat.</b> {E(a["beat"])}</p><p><b>The rule it enforces.</b> {E(a["rule"])}</p><p><b>The mistake behind the rule.</b> {E(a["mistake"])}</p></article>' for a in r['agents'])
    auds = ''.join(f'<li><a href="../briefings/{E(a["id"])}/index.html"><b>{E(a["name"])}</b></a>: {E(a["question"])}</li>' for a in r['audiences'])
    body = f'''
<h1>The team: one editor, a pipeline, and the agents on it</h1>
<p class="lead">The site is built and run by one person and a set of software agents, and this page is written for the agents. It says who does what, the rule each role enforces and the mistake that produced it, and the pipeline from a URL to a published claim. A new agent should be able to read this page and one role and begin.</p>
{section("editor", "The editor", f'<p><b>{E(r["human"]["name"])}</b>, {E(r["human"]["role"]).lower()}. {E(r["human"]["does"])} The brief that started this site is two voice memos and a message, published in full on <a href="../brief/index.html">the brief</a>.</p>')}
{section("pipeline", "The pipeline", pipe)}
{section("roles", "The roles", f'<div class="roles">{agents}</div>')}
{section("audiences", "The audiences", f'<ul>{auds}</ul>', "Each briefing is a role too: a reader whose question the site answers in one page.")}
{section("rules", "The rules every role shares", '''<ul>
<li><b>Capture, don't paraphrase.</b> A page you summarised but did not capture does not exist.</li>
<li><b>One file per agent per concern.</b> So a merge never asks a human to choose between two agents' edits.</li>
<li><b>Count, don't remember.</b> Every number on a page is computed from the thing it counts.</li>
<li><b>Five words, defined once.</b> Confirmed, reported, disputed, contradicted, unverified.</li>
<li><b>State the gap.</b> A blocked fetch, a missing primary source and an unverified quote are all published, not hidden.</li>
<li><b>Read keys yes, vault keys never.</b> And this vault's read key is not published either, because it holds third-party pages.</li>
<li><b>Verify live.</b> A release is done when the live site serves the version, not when the push succeeds.</li>
</ul>''')}
'''
    page('team/index.html', 'The team: the editor, the pipeline and the agents', 'Who does what on this site: the editor, the seven-step pipeline from URL to published claim, each agent role with the rule it enforces and the mistake behind it, and the six audiences.', body, kind='free', topics='team agents')

def build_billing():
    b = D['billing']
    kinds = table(['Kind', 'Price, read to the end', 'Pages', 'Why'], [[E(k['kind']), f'{k["price"]}p', E(k['pages']), E(k['why'])] for k in b['kinds']])
    designed = ''.join(f'<li><b>{E(d["what"])}.</b> {E(d["text"])}</li>' for d in b['designed'])
    cm = b['cost_model']
    unit_counts = {'data/vault.json: sources': C['sources'], 'data/vault.json: captures': C['captures'],
                   'data/sources.json: has_notes': sum(1 for s in D['sources'] if s.get('has_notes')),
                   'data/claims.json': C['claims'], 'data/timeline.json': C['events'], "the build's page list": None}
    rows, total = [], 0
    for u in cm['units']:
        n = unit_counts.get(u['count_from'])
        if n is None:
            n = sum(len(items) for _, items in NAV) + 2  # every page in the nav, plus top-up and topped-up
        cost = n * u['assumed_price_pence']
        total += cost
        rows.append([E(u['unit']), E(str(n)), f'{u["assumed_price_pence"]}p', f'{cost / 100:.2f}', E(u['why'])])
    cost_t = table(['Unit', 'Count', 'Assumed price', '£', 'Why that unit'], rows)
    runs = b['runs']
    body = f'''
<h1>The billing model</h1>
<p class="lead">Two layers, and the page is careful to say which is which. <b>What runs</b> is a reading meter: a few pence a page from credit kept in your browser, charged by how far down the page you read, never blocking, with the option to decline and say why. <b>What is designed</b> is paying for provenance rather than pages: a price per verified claim, a share for whoever created the fact, and a snapshot of the vault for a reader who wants the bytes. The first is the same component the newsroom runs; the second is argued here and built nowhere.</p>
{section("runs", "What runs: the reading meter", f'''<p>Every page carries <code>&lt;sg-meter&gt;</code>, SG Meter v1.3.1, vendored under <code>assets/components/</code> and loaded from this site only. You start with {runs["symbol"]}{runs["start"] / 100:.2f} of credit in this browser; the balance is in the top bar and goes below zero without anything being blocked. A page costs its price times the share of it you scrolled through, rounded to 5% and never less than a tenth, once per page per session. At the foot of each page you can rate how useful it was, which sets the price from free to double, or decline to pay with a reason. Nothing leaves the browser: no account, no cookie, no server of ours, no analytics listening to the meter's events. <a href="../account/index.html">Your reading account</a> shows the history and exports it as JSON.</p>''' + kinds + f'''<p>Top-ups are {runs["symbol"]}{runs["topup"]["amount"] / 100:.2f} of credit on a payment page. No payment link is configured for this site yet, so <a href="../account/top-up.html">the top-up page</a> runs the meter's simulated cart and says so. When a link is added, the credit is added on the return page without verifying the payment, because a static site has nowhere to receive a webhook; the meter's security model is explicit that this is an honesty box, not a paywall.</p>''')}
{section("designed", "What is designed: paying for provenance", f'<ul class="designed">{designed}</ul><p>None of this is live. The newsroom\'s pages on <a href="https://newsroom.sgit.ai/economics/index.html">paying the fact creator</a> and <a href="https://newsroom.sgit.ai/provenance/index.html">provenance as the product</a> carry the argument; this site is the first with a claim table granular enough to price.</p>')}
{section("cost", "What this story cost to assemble, as a model", f'<p>{E(cm["note"])}</p>' + cost_t + f'<p>Total at those assumptions: <b>£{total / 100:.2f}</b>. The counts are from the data files named; the prices are the site\'s assumptions and a reader is invited to substitute their own. What the model leaves out is the editor\'s time and the model inference behind each agent run, neither of which is counted anywhere yet; the honest column on this is <i>not measured</i>.</p>')}
{section("prices", "The prices, as data", f'<pre>{E(json.dumps({"storageKey": runs["storageKey"], "start": runs["start"], "symbol": runs["symbol"], "prices": runs["prices"], "topup": runs["topup"]}, indent=1))}</pre><p>This block is <code>data/billing.json</code>, which is also what every page\'s meter config is generated from, so the table above and the meter cannot disagree.</p>')}
'''
    page('billing/index.html', 'The billing model: what runs and what is designed', 'How this site is paid for: the reading meter that runs (pence per page, kept in your browser, never blocking), the provenance pricing that is designed (per claim, with a share for the fact creator), and a counted model of what the story cost to assemble.', body, kind='free', topics='billing meter economics')

def build_account():
    body = '''
<h1>Your reading account</h1>
<p class="lead">Everything the meter knows is in this browser: the balance, every page opened with the share read and what it cost, what you declined and why, and your top-ups. Export it as JSON; nothing is sent anywhere unless you choose to. A new browser or cleared site data starts again with the starting credit.</p>
<sg-meter view="account"></sg-meter>
<p>How the meter works, and why it works this way, is on <a href="../billing/index.html">the billing model</a>. The account needs JavaScript: the balance lives here, not on a server.</p>
'''
    page('account/index.html', 'Your reading account', 'The balance, history and receipts of your reading on this site, kept in your browser.', body, kind='free')
    body = '''
<h1>Top up</h1>
<p class="lead">Reading credit, paid on a payment page. No payment link is configured for this site yet, so what follows is the meter's simulated cart, which says it is simulated. When a link is added, this page will say so and the credit will be added on the return page without verifying the payment.</p>
<sg-meter view="topup"></sg-meter>
<p>Where your data is kept, and what can leave your browser, is on <a href="../billing/index.html">the billing model</a>. A payment returns to <a href="topped-up.html">the topped-up page</a>.</p>
'''
    page('account/top-up.html', 'Top up', 'Add reading credit to the balance kept in your browser.', body, kind='free')
    body = '''
<h1>Thank you</h1>
<p class="lead">If you arrived here from a payment page, the credit has been added to the balance in this browser. If you opened this page on its own, nothing is added and the meter says so.</p>
<sg-meter view="topped-up"></sg-meter>
<p><a href="index.html">Your reading account</a> &middot; <a href="../index.html">The front page</a></p>
'''
    page('account/topped-up.html', 'Topped up', 'The page a payment returns to.', body, kind='free')

def render_md_file(path):
    """A small markdown renderer for the brief and corrections files: headings, paragraphs, lists, code."""
    with open(os.path.join(ROOT, path), encoding='utf-8') as f:
        text = f.read()
    out, in_list, in_code = [], False, False
    for line in text.splitlines():
        if line.strip().startswith('```'):
            if in_code:
                out.append('</pre>'); in_code = False
            else:
                out.append('<pre>'); in_code = True
            continue
        if in_code:
            out.append(E(line)); continue
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            if in_list: out.append('</ul>'); in_list = False
            lvl = min(len(m.group(1)) + 1, 4)
            out.append(f'<h{lvl}>{E(m.group(2))}</h{lvl}>'); continue
        if re.match(r'^\s*[-*]\s+', line):
            if not in_list: out.append('<ul>'); in_list = True
            out.append('<li>' + inline_md(re.sub(r'^\s*[-*]\s+', '', line)) + '</li>'); continue
        if in_list: out.append('</ul>'); in_list = False
        if line.strip():
            out.append('<p>' + inline_md(line) + '</p>')
    if in_list: out.append('</ul>')
    if in_code: out.append('</pre>')
    return '\n'.join(out)

def inline_md(s):
    s = E(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" rel="noopener">\1</a>', s)
    return s

def build_brief():
    memos = []
    mdir = os.path.join(ROOT, 'admin', 'content', 'briefs', 'memos')
    for fn in sorted(os.listdir(mdir)):
        with open(os.path.join(mdir, fn), encoding='utf-8') as f:
            t = f.read()
        paras = ''.join(f'<p>{E(p.strip())}</p>' for p in re.split(r'\n\s*\n', t) if p.strip())
        memos.append(f'<details open><summary><code>{E(fn)}</code></summary><div class="memo">{paras}</div></details>')
    body = f'''
<h1>The brief, in full</h1>
<p class="lead">The document this site started from, published as written and never edited to look right afterwards. It is a written request and two voice memos from the editor, transcribed by a transcription service and reproduced verbatim, hesitations included. Where the brief turned out to be wrong, the finding goes in <a href="../corrections/index.html">corrections</a>, not here.</p>
{section("request", "The written request, 22 October 2026", render_md_file("admin/content/briefs/2026-10-22__brief.md"))}
{section("memos", "The two voice memos", "".join(memos))}
{section("status", "Status", '<p>Accepted by the editor on 22 October 2026 by sending it; the first release of the site is the reply. What was built against each point of the brief is in the <a href="../admin/index.html">reality file</a>.</p>')}
'''
    page('brief/index.html', 'The brief: a written request and two voice memos', 'The brief this site was built from, published in full: the editor\'s written request and two transcribed voice memos on mapping the PHP vulnerability as evidence.', body, kind='free')

def build_corrections():
    body = f'''
<h1>Corrections</h1>
<p class="lead">Where the brief was wrong, where a page was wrong, what was found and what was done instead. A correction is published above the mistake, dated, and the mistake stays visible. The file is <code>BRIEF-CORRECTIONS.md</code> in the repository.</p>
{render_md_file("BRIEF-CORRECTIONS.md")}
'''
    page('corrections/index.html', 'Corrections', 'Where the brief or a page of this site was wrong, what was found and what was done instead.', body, kind='free')

def build_admin():
    vs = D['versions']
    rows = ''.join(f'<article class="rel" id="v{E(v["version"])}"><h3>v{E(v["version"])} &middot; {E(v["date"])}</h3><p>{E(v["title"])}</p><p class="small">{E(v.get("summary") or "")} Vault commit <code>{E(v.get("vault_commit") or "")}</code>.{" Reconstructed after the fact." if v.get("reconstructed") else ""}</p><p class="small">Files: {", ".join(f"<code>{E(c)}</code>" for c in v.get("changes", []))}</p></article>' for v in vs['versions'])
    body = f'''
<h1>Release history</h1>
<p class="lead">One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v{E(vs["current"])}. The data is <a href="../data/versions.json">data/versions.json</a>.</p>
{rows}
'''
    page('admin/versions.html', 'Release history', 'Every release of this site, with what changed, why, and the vault commit it was built from.', body, kind='free')
    checks = [
        ('Every internal link resolves against the real file tree', 'a link to a page that does not exist'),
        ('Every page is linked from at least one other page', 'a page nothing can find, which is the same as unpublished'),
        ('Every page has a markdown twin and a line in llms.txt', 'a page an agent cannot read'),
        ('Every claim, event, number, agency and signal cites only slugs in the manifest', 'a citation to nothing'),
        ('The build is byte-identical when run twice', 'a clock, a random number or an unsorted set in the build'),
        ('No em-dash in the site\'s own prose', 'the estate\'s writing rule; third-party titles are exempt'),
        ('No sgit credential shape, private-key marker or cloud key prefix anywhere in the tree', 'a vault key in a data file'),
        ('No script, stylesheet or image loaded from another origin', 'a dependency fetched at run time'),
        ('data/ parses and every claim status is one of the five words', 'a sixth word that means nothing'),
    ]
    checks_t = table(['Check', 'What it would catch'], [[E(a), E(b)] for a, b in checks])
    body = f'''
<h1>Admin and engineering</h1>
<p class="lead">How the site is built, what the gate checks, where things are, and what exists against what the brief asked for. The site is static HTML built by one Python script with no dependencies beyond the standard library, deployed by GitHub Pages from the <code>dev</code> branch of <a href="{REPO_URL}">the repository</a>.</p>
{section("layout", "Where things are", table(['Thing', 'Where'], [
  ['The version, one number', '<code>VERSION</code>; shown in the top bar; bumped by the release script on every push'],
  ['The data every page is built from', '<code>data/*.json</code>; exported from the vault by <code>admin/build/export_vault.py</code> and authored by the story agent'],
  ['The build', '<code>admin/build/build.py</code>; deterministic; writes every page, twin, the graph and llms.txt into the repository root'],
  ['The gate', '<code>admin/build/validate.py</code>; the checks below; fails the release'],
  ['The release', '<code>admin/build/release.sh</code>; bump, build, validate, tripwire, push to dev, verify live'],
  ['The brief and its corrections', '<code>admin/content/briefs/</code>, <code>BRIEF-CORRECTIONS.md</code>'],
  ['The reality file', '<code>REALITY.md</code>: what exists, by domain, kept current by whoever ships'],
  ['The meter', '<code>assets/components/sg-meter/v1/v1.3/v1.3.1/</code> and <code>assets/components/base/v1/v1.0/v1.0.0/</code>, vendored, immutable paths'],
  ['Credentials', 'none in the repository; the vault key and the push token live in the agents\' sessions and in a gitignored tier, scanned by the tripwire'],
]))}
{section("section", "The admin section", '<ul><li><a href="board/index.html">The board</a>: the work, as rows.</li><li><a href="roles/index.html">Roles</a>: who does what, and how an agent joins.</li><li><a href="briefs/index.html">Briefs</a>: the build briefs, in full.</li><li><a href="vault/index.html">The vault, opened</a>: the read key and the browser link.</li><li><a href="telemetry/index.html">Who reads this site</a>: the telemetry lane and its counts.</li></ul>')}
{section("gate", "The gate", checks_t)}
{section("reality", "The reality file", render_md_file("REALITY.md"))}
{section("honest", "The honest column", '''<ul>
<li><b>Not measured:</b> the editor's time and the inference cost behind each agent run.</li>
<li><b>Not yet run:</b> the verifier role, which re-reads every claim against its capture text.</li>
<li><b>Not reviewed:</b> the playbook and the blast-radius section are the site's own synthesis of agency advice and have not been reviewed by a security team.</li>
<li><b>Not live:</b> everything on the billing page under "designed".</li>
<li><b>No tests beyond the gate:</b> the build has no unit tests; the gate is the whole automated enforcement surface.</li>
<li><b>No review folder yet:</b> the estate's guidance asks for <code>review/</code> from the first commit; this repository starts it from its next change.</li>
</ul>''')}
'''
    page('admin/index.html', 'Admin and engineering', 'How this site is built, the checks in its gate, where things are, the reality file and the honest column.', body, kind='free')

def build_llms():
    lines = [f'# {SITE}', '', f'> {STORY["description"]}', '', f'Site v{VERSION}. Data as of {STORY["data_as_of"]} (the latest capture in the evidence vault, commit {D["vault"]["head"]["commit"]}). Every page below has a markdown twin at the same path with .md; the data behind every page is in data/*.json. The evidence vault is private; its manifest with every hash is data/sources.json.', '']
    for label, items in NAV:
        lines.append(f'## {label}')
        for p, t in items:
            desc = next((d for pp, _, d, _ in PAGES if pp == p), '')
            lines.append(f'- [{t}]({BASE_URL}/{md_path(p)}): {desc}')
        lines.append('')
    lines.append('## Sources, one page each')
    for slug, src in SOURCES.items():
        lines.append(f'- [{src.get("title") or slug}]({BASE_URL}/sources/{slug}/index.md): {src.get("publisher") or ""}')
    lines.append('')
    lines.append('## Parties, one page each')
    for a in D['actors']:
        lines.append(f'- [{a["name"]}]({BASE_URL}/actors/{a["id"]}/index.md): {a["role"]}')
    lines.append('')
    lines += ['## Data', f'- [sources.json]({BASE_URL}/data/sources.json): the vault manifest with every capture and hash',
              f'- [claims.json]({BASE_URL}/data/claims.json): every claim with status, who says it and sources',
              f'- [timeline.json]({BASE_URL}/data/timeline.json): every dated event', f'- [numbers.json]({BASE_URL}/data/numbers.json): the scale figures and what each measures',
              f'- [agencies.json]({BASE_URL}/data/agencies.json): the agencies\' stances', f'- [affected.json]({BASE_URL}/data/affected.json): versions, SAPIs, mitigations',
              f'- [software.json]({BASE_URL}/data/software.json): the NCSC-NL inventory, parsed', f'- [exploitation.json]({BASE_URL}/data/exploitation.json): the signals',
              f'- [graph.json]({BASE_URL}/data/graph.json): nodes and citation edges', f'- [vault.json]({BASE_URL}/data/vault.json): the vault\'s head, counts and agents',
              f'- [billing.json]({BASE_URL}/data/billing.json): the meter configuration and the designed model', f'- [versions.json]({BASE_URL}/data/versions.json): release history',
              f'- [questions.json]({BASE_URL}/data/questions.json): the questions readers ask, each answer with its sources and the pages that carry it', '',
              '## Status words', *[f'- {k}: {v}' for k, v in STATUS_WORDS.items()], '',
              f'Newsroom section on the same story: {NEWSROOM}', f'Repository: {REPO_URL}', 'Licence: content CC BY 4.0, code Apache-2.0.', '']
    write('llms.txt', '\n'.join(lines))

def build_sitejs():
    write('assets/site.js', '''// php.oct-2026.story.sgit.ai: the menu toggle on narrow screens. Nothing else runs here.
(function () {
  var b = document.querySelector('.nav-toggle'), n = document.getElementById('nav-items');
  if (!b || !n) return;
  b.addEventListener('click', function () {
    var open = n.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.querySelectorAll('.ni > .nl').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      if (window.matchMedia('(max-width: 900px)').matches) { ev.preventDefault(); a.parentNode.classList.toggle('open'); }
    });
  });
})();
''')

def main():
    build_index(); build_flaws(); build_timeline(); build_discovery(); build_leak(); build_exploitation(); build_playbook()
    build_code(); build_review(); build_context(); build_impact(); build_defence()
    build_claims(); build_numbers(); build_agencies(); build_affected(); build_sources(); build_graph()
    build_source_pages(); build_actors()
    build_briefings(); build_method(); build_team(); build_billing(); build_account(); build_brief(); build_corrections(); build_admin()
    build_admin_section(); build_questions()
    build_llms(); build_sitejs()
    print(f'built {len(PAGES)} pages for v{VERSION}, data as of {STORY["data_as_of"]}, vault {D["vault"]["head"]["commit"]}')


# ----------------------------------------------------------------------------- pages added in v0.2

def mini_graph(center_label, center_cls, rings, depth):
    """A small radial SVG: the centre node and one ring of linked nodes. rings: list of (label, href, cls)."""
    n = len(rings)
    if n == 0:
        return ''
    import math
    W, H, R = 720, 60 + 22 * max(8, n), 0
    cx, cy = 180, H / 2
    out = []
    for i, (label, href, cls) in enumerate(rings):
        y = 20 + i * (H - 40) / max(1, n - 1)
        x = 420
        out.append(f'<path class="e e-{E(cls)}" d="M{cx},{cy:.1f} C{cx+120},{cy:.1f} {x-120},{y:.1f} {x},{y:.1f}"/>')
        out.append(f'<a href="{E(href)}"><circle class="d d-{E(cls)}" cx="{x}" cy="{y:.1f}" r="3.5"/><text class="n" x="{x+7}" y="{y+4:.1f}">{E(label[:58])}{"…" if len(label) > 58 else ""}</text></a>')
    out.append(f'<circle class="d d-{E(center_cls)}" cx="{cx}" cy="{cy:.1f}" r="7"/><text class="n t" x="{cx-10}" y="{cy+4:.1f}" text-anchor="end">{E(center_label[:40])}</text>')
    return f'<figure class="graph"><svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{E(center_label)} and what links to it">{"".join(out)}</svg></figure>'

def build_code():
    c = D['code']
    f, b = c['fix'], c['backport']
    areas = table(['Area', 'Files in the fix'], [[E(a), E(str(n))] for a, n in f['by_area']])
    merge = table(['When (UTC)', 'What'], [[E(fmt_at(t)), E(w)] for t, w in f['merge_path']])
    where = ''.join(f'<li><b>{E(w["layer"])}</b> {"&#10003; in scope" if w["in_scope"] else "&#10007; not where the bug is"}: {E(w["text"])}</li>' for w in c['where'])
    mech = ''.join(f'<li><b>{E(m["step"])}.</b> {E(m["text"])}</li>' for m in c['mechanism'])
    openq = ''.join(f'<li>{E(o)}</li>' for o in c['open'])
    hunks = '''<pre>/* Zend/zend_alloc.c, the fix: the allocator no longer jumps */
static zend_always_inline zend_result zend_mm_check_limit(zend_mm_heap *heap, size_t add_size, bool gc, bool *did_gc ...)
{
    /* Is the soft limit exceeded or going to be exceeded? */
    if (UNEXPECTED(heap->limit < heap->real_size || add_size > heap->limit - heap->real_size)) {
        if (gc && zend_mm_gc(heap)) { ... }
        if (!heap->fallible && add_size > heap->hard_limit - heap->real_size) {
            zend_mm_hard_limit_error(heap, add_size ...);        /* does not return: _exit() */
        }
        if (!gc || (heap->limit < heap->real_size || add_size > heap->limit - heap->real_size)) {
            if (!ZEND_HAS_OOM()) {
                zend_mm_delayed_error("Allowed memory size of %zu bytes exhausted (tried to allocate %zu bytes)", ...);
            }
            return heap->fallible ? FAILURE : SUCCESS;           /* the allocation goes ahead, or fails cleanly */
        }
    }
    return SUCCESS;
}

/* and what used to be there (the 7.4 branch shows the old shape being replaced) */
-	heap->overflow = 1;
-	zend_try {
-		zend_error_noreturn(E_ERROR, format, limit, ... size);
-	} zend_catch {
-	}  zend_end_try();
-	heap->overflow = 0;
-	zend_bailout();                                             /* longjmp out of the allocation */
-	exit(1);

/* Zend/zend_execute_API.c: the delayed error is handled at a safe point */
ZEND_API void ZEND_FASTCALL zend_handle_delayed_oom(void)
{
    ...
    if (execute_data) {
        EG(exception) = NULL;
        /* Object allocation should succeed unless it trips the hard limit */
        zend_throw_unwind_exit();                               /* unwind PHP frames in order */
    }
    zend_try { zend_error_zstr_at(E_ERROR, info->filename, info->lineno, info->message); } zend_catch { } zend_end_try();
    ...
    /* No userland frame to unwind: ... Let it propagate and abort the request, the way an immediate OOM does. */
    if (!execute_data) { zend_bailout(); }
}

/* main/main.c: two settings that did not exist before */
+	PHP_INI_ENTRY("max_multipart_body_parts",	"-1", PHP_INI_SYSTEM|PHP_INI_PERDIR, NULL)
+	PHP_INI_ENTRY("memory_hard_limit_percent",	NULL, PHP_INI_ALL, OnChangeMemoryHardLimitPercent)

/* main/main.c: the stale-state class, in one line */
 		for (i=0; i&lt;NUM_TRACK_VARS; i++) {
 			zval_ptr_dtor(&amp;PG(http_globals)[i]);
+			/* May be accessed before php_request_startup() */
+			ZVAL_UNDEF(&amp;PG(http_globals)[i]);
 		}</pre>'''
    body = f'''
<h1>The code: where the bug is, and what the fix does</h1>
<p class="lead">The editor's question was where the flaw actually lives: in PHP, in C, in the engine? The answer, read from the repository rather than from any article, is the Zend engine's memory manager and request lifecycle, in C, below every PHP application. This page is built from a clone of php/php-src: the fix commit, its parent, the branch it landed on, the end-of-life backport, and the diff between the last vulnerable and first fixed release. The patches and the commit metadata are in the vault with their hashes. <span class="refs">{src_links(c["sources"], 1)}</span></p>
{section("fix", "The fix commit", f'''<p><code>{E(f["commit"])}</code>, <b>{E(f["subject"])}</b>, by {E(f["author"])} with {E(", ".join(f["coauthors"]))}. Authored <b>{E(fmt_at(f["authored"]))}</b>; committed to the public branch <b>{E(fmt_at(f["committed"]))}</b>, six minutes after the planned release time. Parent <code>{E(f["parent"][:12])}</code>. The commit message, in full:</p><ul>{"".join(f"<li>{E(x)}</li>" for x in f["body"])}</ul><p>{f["files"]} files changed, {f["insertions"]:,} insertions, {f["deletions"]} deletions; {f["non_test_files"]} of the files are not tests.</p>''' + areas + '<p>Timing, from the commit and merge timestamps:</p>' + merge)}
{section("where", "Where the bug is", f'<ul>{where}</ul>')}
{section("mechanism", "What the fix does, step by step", f'<ol class="mech">{mech}</ol>', "The site's reading of the diff, checked against the two GitHub advisories. Each step names the function or file it comes from; the hunks below are verbatim.")}
{section("hunks", "The hunks that matter", hunks + '<p>The full engine, main and session hunks of the fix (157 KB) and the complete 7.4 backport patch are in the vault as <code>sources/' + E('github-php-src-fix-commit-3584a98bd') + '/raw/</code> with SHA-256 sums, and the file list of all 389 files beside them.</p>')}
{section("backport", "The end-of-life backport, and how it differs", f'<p>Branch <code>{E(b["branch"])}</code>, commit <code>{E(b["short"])}</code>, same title, same author, authored {E(fmt_at(b["authored"]))}. The commit says <q>{E(b["note_in_commit"])}</q>. {b["files"]} files: ' + ', '.join(f'<code>{E(x)}</code>' for x in b["files_list"]) + '. Instead of the delayed error and the unwind, every memory error calls a new <code>zend_mm_safe_error_ex</code> that prints the fatal and <code>_exit</code>s the process; the same globals are reset; a <code>max_multipart_body_parts</code> cap is added; the multipart header parser keeps only the two headers it uses; and the session upload-progress callback is disabled with a one-line <code>|| true</code>. A worker that dies on every out-of-memory cannot be exploited this way and will be worse at staying up.</p>')}
{section("open", "What the code does not tell us", f'<ul>{openq}</ul>')}
<p>How the bug is reached from a request is on <a href="../flaws/index.html">the two flaws</a>; what to watch for on a host is on <a href="../defence/index.html">detection and defence</a>.</p>
'''
    page('code/index.html', 'The code: where php2shell lives and what the fix does', 'Read from a clone of php/php-src: the fix commit (389 files, authored 18 October, public 21 October 14:06 UTC), the engine mechanism it replaces, the hunks that matter, and the end-of-life backport.', body, kind='analysis', topics='php2shell code engine fix')

def build_context():
    h = D['history']
    k = h['kev_catalog']
    rows = [[f'<b>{E(x["cve"])}</b><br><span class="small">{E(x["name"])}</span>', E(x['component']), E(x['published']), E(x['kev']), E(x['ransomware'] or '…'), E(x['response']), E(x['note']), src_links([x['source']], 1)] for x in h['comparators']]
    peryear = table(['Year', 'CVEs added to KEV'], [[E(y), E(str(n))] for y, n in k['per_year'].items()])
    permonth = table(['2026', 'Added'], [[E(m), E(str(n))] for m, n in k['2026_by_month'].items()])
    reading = ''.join(f'<li>{E(r)}</li>' for r in h['reading'])
    body = f'''
<h1>In context: php2shell against the flaws that came before</h1>
<p class="lead">The editor has worked in security long enough to remember Kaminsky's DNS flaw and Heartbleed, and asked whether this one is as big as the morning's coverage made it. The honest way to answer is a table: ten landmark flaws, each with its CVE record fetched into the vault and its row in CISA's Known Exploited Vulnerabilities catalog, captured on 22 October. The catalog is the one public, dated, machine-readable record of 'this was exploited', and php2shell is not in it yet.</p>
<p class="small">{E(h["note"])}</p>
{table(['CVE', 'Where it was', 'Published', 'Added to KEV', 'Ransomware use', 'What happened', 'Why it is here', 'Record'], rows, 'ctx')}
{section("kev", "The catalog itself, counted", f'<p>Catalog version {E(k["version"])}: {k["entries"]:,} entries, {k["ransomware_known"]} with known ransomware use, {k["php_related"]} with PHP in the vendor, product or name, of which three are PHP core: {"; ".join(E(x) for x in k["php_core"])}. Counted from the captured file. <span class="refs">{src_links([k["source"]], 1)}</span></p><div class="cols">{peryear}{permonth}</div>')}
{section("reading", "What the comparison says", f'<ol class="reading">{reading}</ol>', "The site's reading of the table above. Positions, with the evidence attached.")}
<p>The signals that would move php2shell into the catalog are on <a href="../exploitation/index.html">the exploitation page</a>; what was taken offline, and by whom, is on <a href="../impact/index.html">impact</a>.</p>
'''
    page('context/index.html', 'In context: php2shell against Kaminsky, Heartbleed, Shellshock, Log4Shell and the last PHP RCE', 'Ten landmark vulnerabilities with their CVE records and KEV rows, the KEV catalog counted, and what the comparison says about severity, exposure, urgency and the discovery pipeline.', body, kind='analysis', topics='php2shell history context kev')

def build_impact():
    im = D['impact']
    off = [[f'<b>{E(x["who"])}</b><br><span class="small">{E(x["country"])}</span>', E(x['what']), E(fmt_at(x['when'])), E(x['said_by']), pill(x['status']), src_links(x['sources'], 1)] for x in im['offline']]
    comp = [[E(x['claim']), E(x['basis']), pill(x['status']), src_links(x['sources'], 1)] for x in im['compromised']]
    body = f'''
<h1>Impact: what was taken offline, and what was compromised</h1>
<p class="lead">Two ledgers, because they measure different things. Taking a system offline is a decision an operator makes and can confirm, and the first table is full. Being compromised is a fact only evidence establishes, and the second table has, as of the latest capture, no confirmed entry. That gap is the most important finding on this site: the reported cost of php2shell so far is the cost of precaution.</p>
<p class="small">{E(im["note"])}</p>
{section("offline", "Taken offline", table(['Who', 'What happened', 'When', 'Who says so', 'Status', 'Sources'], off, 'imp'))}
{section("compromised", "Compromised", table(['Claim', 'Basis', 'Status', 'Sources'], comp, 'imp'))}
{section("reading", "What the two ledgers say together", '''<ul>
<li><b>Precaution was the dominant response</b>, and it was institutional: national CERTs, state IT providers and councils pulled sites on advice, often before the patch existed, and said so. The one operator who measured it served 94% of its traffic from cache for 13 hours.</li>
<li><b>Attempts are not compromises.</b> Cloudflare's millions and Amazon's honeypot hits are requests matching a shape at the edge or against a sensor. Nobody has published a count of successful exploitations, and the parties best placed to see one (CISA, Huntress, Imperva) report none.</li>
<li><b>Absence of evidence is weak here.</b> The detection authors are explicit that default web logs cannot show the attack shape and that no standard log carries the worker id the cross-request bug needs. A quiet log is not a clean host.</li>
<li><b>The question that would settle it</b> is one that no captured source answers: of the 1.57 million unpatched hosts Censys counted, how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell. That number is what 'blast radius' means at internet scale, and it does not exist yet.</li>
</ul>''')}
<p>What a compromise of one system would reach is on <a href="../flaws/index.html#blast">the blast-radius section</a>; how to tell is on <a href="../defence/index.html">detection and defence</a>.</p>
'''
    page('impact/index.html', 'Impact: taken offline versus compromised', 'Two ledgers for php2shell: every system reported taken offline with who said so, and every claim of compromise with its basis. As of the latest capture, no named organisation has confirmed a compromise.', body, kind='story', topics='php2shell impact outages')

def build_defence():
    d = D['defence']
    edge = [[f'<b>{E(x["vendor"])}</b>', E(x['what']), E(x['when']), E(x['caveat']), src_links(x['sources'], 1)] for x in d['edge']]
    sigs = ''.join(f'<li><b>{E(x["what"])}</b> ({E(x["who"])}). {E(x["text"])} <span class="refs">{src_links(x["sources"], 1)}</span></li>' for x in d['signatures'])
    signals = [[f'<b>{E(x["where"])}</b>', E(x['signal']), src_links(x['sources'], 1)] for x in d['signals']]
    expl = ''.join(f'<li><b>{E(x["who"])}.</b> {E(x["text"])} <span class="refs">{src_links(x["sources"], 1)}</span></li>' for x in d['exploitability'])
    body = f'''
<h1>Detection and defence: can it be blocked, can it be seen</h1>
<p class="lead">The editor's premise is that a zero-day is not an invisibility cloak: an exploit that runs code on a web server leaves a request in the log, a crash in the kernel, a child process in the tree. The captured sources agree, and they also say where the logs go blind. This page is what six edge vendors, three community rule sets and one detection guide say about blocking the request, and what the host shows once the request got through.</p>
{section("edge", "At the edge: what the WAF vendors deployed", table(['Vendor', 'What', 'When', 'Their own caveat', 'Sources'], edge, 'def') + '<p>Every one of them says the same two things: it is a stopgap, and patch anyway. The flaw fires during request set-up, so any URL that reaches PHP is a candidate and a rule can only match shape; a rule that blocks every multipart body also blocks every upload. And a WAF sees only the traffic routed through it: the detection guide\'s first step is a direct curl to the origin IP to prove there is no way round.</p>')}
{section("sigs", "Signatures", f'<ul>{sigs}</ul>')}
{section("host", "On the host: what exploitation looks like", table(['Where', 'Signal', 'Sources'], signals, 'def'))}
{section("hard", "How hard it is to exploit", f'<ul>{expl}</ul>', "The sources that temper the headline, and the one that says expect more.")}
{section("answer", "So: can it be detected?", '''<p>Yes, at two layers, and no at a third. <b>At the edge</b>, the known request shapes are distinctive and the vendors say their rules match them; the limit is variants and traffic that bypasses the edge. <b>On the host</b>, the strongest signal is the one that needs no signature: a PHP worker spawning a shell or a downloader when no application code ran. That is a process-tree rule, cheap to deploy, and the one the detection authors and CISA converge on. <b>In the default web log</b>, no: nginx's standard format records neither the content type nor the body, and the cross-request bug leaves no worker id anywhere a log would carry it. An organisation whose only telemetry is the access log cannot answer "were we hit" from it, which is the fact behind the agencies' advice to assess for backdoors rather than to look for a log line.</p>''')}
'''
    page('defence/index.html', 'Detection and defence: what blocks php2shell and what shows it', 'What Cloudflare, Akamai, Fastly, Imperva, AWS and Fortinet deployed and what each says it cannot do; the community Suricata, Sigma, Falco and ModSecurity rules; the host signals; and how hard the exploit is according to the vendors who tried.', body, kind='story', topics='php2shell detection waf signatures')

def build_source_pages():
    claims_by_src, events_by_src, nums_by_src, ag_by_src, ex_by_src = {}, {}, {}, {}, {}
    for c in D['claims']:
        for s in c['sources']: claims_by_src.setdefault(s, []).append(c)
    for t in D['timeline']:
        for s in t['sources']: events_by_src.setdefault(s, []).append(t)
    for n in D['numbers']:
        for s in n['sources']: nums_by_src.setdefault(s, []).append(n)
    for a in D['agencies']:
        for s in a['sources']: ag_by_src.setdefault(s, []).append(a)
    for x in D['exploitation']:
        for s in x['sources']: ex_by_src.setdefault(s, []).append(x)
    for slug, s in SOURCES.items():
        cl, ev, nu = claims_by_src.get(slug, []), events_by_src.get(slug, []), nums_by_src.get(slug, [])
        rings = [(c['claim'], f'../../claims/index.html#{c["id"]}', c['status']) for c in cl] + [(f'{fmt_at(t["at"])}: {t["event"]}', '../../timeline/index.html', 'event') for t in ev] + [(f'{n["value"]} {n["of"]}', f'../../numbers/index.html#{n["id"]}', n['status']) for n in nu]
        g = mini_graph(short_name(s), 'src' + (' d-pri' if s.get('primary') else ''), rings[:40], 2)
        caps = ''
        for c in s['captures']:
            files = ''.join(f'<li><code>{E(fn)}</code> <span class="h">{E(f["sha256"])}</span> <span class="small">{f["bytes"]:,} bytes</span></li>' for fn, f in sorted(c['files'].items()))
            err = f' <span class="small">error: {E(str(c["error"]))}</span>' if c.get('error') else ''
            caps += f'<details><summary>capture <code>{E(c["stamp"])}</code> &middot; HTTP {E(str(c.get("status")))} &middot; {E(str(c.get("final_url") or ""))}{err}</summary><ul class="files">{files}</ul></details>'
        raw = ''
        if s.get('raw_sha256'):
            raw = '<details><summary>raw, ' + str(len(s['raw_sha256'])) + ' files with SHA256SUMS</summary><ul class="files">' + ''.join(f'<li><code>{E(fn)}</code> <span class="h">{E(h)}</span></li>' for fn, h in s['raw_sha256'].items()) + '</ul></details>'
        notes = f'<div class="notes">{render_md_text(s["notes_md"])}</div>' if s.get('notes_md') else '<p class="small">No note has been written for this source yet; the row above is what the collector recorded.</p>'
        cl_t = claim_rows(cl, 2) if cl else '<p class="small">No claim cites this source yet.</p>'
        ev_t = table(['When', 'Event', 'Time is'], [[E(fmt_at(t['at'])), E(t['event']), pill(t['confidence'])] for t in ev], 'tl') if ev else '<p class="small">No timeline event cites this source yet.</p>'
        extra = ''
        if nu: extra += '<h3>Numbers from this source</h3>' + table(['Figure', 'Of', 'Status'], [[E(n['value']), E(n['of']), pill(n['status'])] for n in nu])
        if ag_by_src.get(slug): extra += '<h3>Agency rows from this source</h3><ul>' + ''.join(f'<li><a href="../../agencies/index.html">{E(a["agency"])}</a>: offline {pill(a["offline"])}</li>' for a in ag_by_src[slug]) + '</ul>'
        if ex_by_src.get(slug): extra += '<h3>Exploitation signals from this source</h3><ul>' + ''.join(f'<li><a href="../../exploitation/index.html">{E(fmt_at(x["when"]))}</a>: {E(x["what"][:160])}</li>' for x in ex_by_src[slug]) + '</ul>'
        body = f'''
<p class="kicker">Source &middot; {E(s.get("kind") or "")} &middot; {"primary" if s.get("primary") else "secondary"} &middot; {pill(s.get("status") or "")}</p>
<h1>{E(s.get("title") or slug)}</h1>
<p class="meta"><b>{E(s.get("publisher") or "")}</b> &middot; <a href="{E(s["url"])}" rel="noopener nofollow">{E(s["url"])}</a> &middot; published {E(str(s.get("published") or "not stated"))} &middot; added by <code>{E(s.get("added_by") or "")}</code> &middot; slug <code>{E(slug)}</code></p>
<p>{E(s.get("notes") or "")}</p>
{g}
{section("says", "What it says, as the collector read it", notes)}
{section("claims", "Claims that cite it", cl_t)}
{section("events", "Events that cite it", ev_t + extra)}
{section("bytes", "The bytes", (caps or "<p class=small>No browser capture; see raw.</p>") + raw + '<p class="small">The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. <a href="../index.html">Every source &rarr;</a></p>')}
'''
        page(f'sources/{slug}/index.html', f'Source: {s.get("title") or slug}', f'{s.get("publisher") or slug}: what it says, the claims and events that cite it, and the hashes of every captured file.', body, kind='evidence', topics='php2shell source')

def render_md_text(text):
    out, in_list = [], False
    for line in text.splitlines():
        m = re.match(r'^(#{1,4})\s+(.*)$', line)
        if m:
            if in_list: out.append('</ul>'); in_list = False
            out.append(f'<h4>{E(m.group(2))}</h4>'); continue
        if re.match(r'^\s*[-*]\s+', line):
            if not in_list: out.append('<ul>'); in_list = True
            out.append('<li>' + inline_md(re.sub(r'^\s*[-*]\s+', '', line)) + '</li>'); continue
        if in_list and line.startswith('  '):
            out[-1] = out[-1][:-5] + ' ' + inline_md(line.strip()) + '</li>'; continue
        if in_list: out.append('</ul>'); in_list = False
        if line.strip(): out.append('<p>' + inline_md(line) + '</p>')
    if in_list: out.append('</ul>')
    return '\n'.join(out)

def actor_claims(a):
    keys = [k.strip().lower() for k in re.split(r'[,/;()]| and |\bvia\b', a['name']) if len(k.strip()) > 3]
    out = []
    for c in D['claims']:
        by = c['by'].lower()
        if any(k in by for k in keys):
            out.append(c)
    return out

def build_actors():
    rows = []
    for a in D['actors']:
        cl = actor_claims(a)
        rows.append([f'<a href="{E(a["id"])}/index.html"><b>{E(a["name"])}</b></a>', E(a['role']), E(str(len(cl))), src_links(a['sources'], 1)])
    body = f'''
<h1>Who says what</h1>
<p class="lead">{len(D["actors"])} parties whose words this site quotes: maintainers, researchers, agencies, vendors, operators and reporters. Each has a page with the claims it makes, the sources those claims come from, and its own small graph. The count is of claims this site attributes to the party; a party with many claims and few primary sources is one whose word is being taken.</p>
{table(['Party', 'Role in the story', 'Claims', 'Sources'], rows, 'act')}
'''
    page('actors/index.html', 'Who says what: every party and its claims', f'{len(D["actors"])} parties in the php2shell story, each with the claims this site attributes to it and the sources behind them.', body, kind='evidence', topics='php2shell actors')
    for a in D['actors']:
        cl = actor_claims(a)
        rings = [(c['claim'], f'../../claims/index.html#{c["id"]}', c['status']) for c in cl] + [(SOURCES[s].get('title') or s, f'../../sources/{s}/index.html', 'src') for s in a['sources'] if s in SOURCES]
        g = mini_graph(a['name'], 'actor', rings[:40], 2)
        body = f'''
<p class="kicker">Party</p>
<h1>{E(a["name"])}</h1>
<p class="lead">{E(a["role"])}</p>
{g}
{section("claims", "Claims this site attributes to this party", claim_rows(cl, 2) if cl else '<p class="small">No claim row names this party in its "who says it" field; its sources are cited by other rows.</p>')}
{section("sources", "Its sources in the vault", '<ul>' + ''.join(f'<li><a href="../../sources/{E(s)}/index.html">{E(SOURCES[s].get("title") or s)}</a> <span class="small">{E(SOURCES[s].get("publisher") or "")}</span></li>' for s in a['sources'] if s in SOURCES) + '</ul>')}
<p><a href="../index.html">Every party &rarr;</a></p>
'''
        page(f'actors/{a["id"]}/index.html', f'{a["name"]}: what they say', f'{a["name"]}: {a["role"]}; the claims this site attributes to them and their sources.', body, kind='evidence', topics='php2shell actor')



# ----------------------------------------------------------------------------- the admin section (v0.2.3)

def build_admin_section():
    A = D['admin']
    st = Counter(b['status'] for b in A['board'])
    rows = [[E(b['id']), E(b['title']) + (f'<div class="note">{E(b["note"])}</div>' if b.get('note') else ''), pill(b['status']), E(b['owner']), E(b.get('version') or '')] for b in A['board']]
    body = f"""
<h1>The board</h1>
<p class="lead">The work, as rows in <code>data/admin.json</code>: {len(A["board"])} items, {st.get("open", 0)} open, {st.get("done", 0)} done. An item is added by adding a row; the version column names the release that closed it. Several agents work on this site and on the evidence vault; the board is where they see what is taken and what is waiting.</p>
{table(['#', 'Item', 'Status', 'Owner', 'Shipped in'], rows, 'board')}
<p>Who the owners are is on <a href="../roles/index.html">roles</a>; the briefs that open items are on <a href="../briefs/index.html">briefs</a>.</p>
"""
    page('admin/board/index.html', 'The board', 'The work on this site and its vault, as rows: what is open, who owns it, what shipped it.', body, kind='free')
    cards = ''.join(f'<article class="role" id="{E(r["id"])}"><h3>{E(r["name"])} <span class="small">{E(r["who"])}</span></h3><p><b>Owns.</b> {E(r["owns"])}</p><ul>{"".join(f"<li>{E(x)}</li>" for x in r["rules"])}</ul></article>' for r in A['roles'])
    body = f"""
<h1>Roles and responsibilities</h1>
<p class="lead">{len(A["roles"])} roles, each a row in <code>data/admin.json</code>: who fills it today, what it owns, and the rules it enforces. Several agents and one editor work on this site and on the evidence vault at once; the rule that keeps that from colliding is one file per agent per concern, in the vault and in the repository. A new agent reads this page, picks or is given a role, and begins; the pipeline it joins is on <a href="../../team/index.html">the team page</a>.</p>
<div class="roles">{cards}</div>
<h2>How to join</h2>
<ol>
<li>Clone the evidence vault with its read key to look, or ask the editor for the vault key to write. Read its <code>README.md</code>: the protocol is there.</li>
<li>Take a board item or open one with a brief. Write your claims and timeline rows in <code>claims/&lt;you&gt;.json</code> and <code>timeline/&lt;you&gt;.json</code>; never edit another agent's file.</li>
<li>In this repository, change <code>data/</code>, run <code>admin/build/build.py</code> and <code>admin/build/validate.py</code>, and release with <code>admin/build/release.sh</code>. Every push is a version.</li>
<li>Commit messages name the agent. Corrections go in <code>BRIEF-CORRECTIONS.md</code>, above the mistake.</li>
</ol>
"""
    page('admin/roles/index.html', 'Roles and responsibilities', 'The roles on this site and its vault, who fills each, what it owns and the rules it enforces; how a new agent joins.', body, kind='free')
    bdir = os.path.join(ROOT, 'admin', 'content', 'briefs')
    items = ''
    for fn in sorted(os.listdir(bdir), reverse=True):
        if fn.endswith('.md'):
            items += f'<article class="rel" id="{E(fn[:-3])}"><p class="kicker">{E(fn[:10])} &middot; <code>{E(fn)}</code></p>{render_md_file("admin/content/briefs/" + fn)}</article>'
    body = f"""
<h1>Briefs</h1>
<p class="lead">A brief is written before the work and published as written: what was asked, in whose words, what exists to build on, the design, what it cannot do, the deliverables and the open questions. The newsroom and the sgit.ai sites keep theirs the same way. The file is the record; this page renders <code>admin/content/briefs/</code>, newest first. The written request and the two voice memos that started the site are on <a href="../../brief/index.html">the brief</a>.</p>
{items}
"""
    page('admin/briefs/index.html', 'Briefs', 'The build briefs for this site, published in full before the work, newest first.', body, kind='free')
    v = A['evidence_vault']; vt = D['vault']
    body = f"""
<h1>The evidence vault, opened</h1>
<p class="lead">The vault behind every claim on this site, {vt["sources"]} sources and {vt["captures"]} captures at commit <code>{E(vt["head"]["commit"] or "")}</code>, opens read-only in the browser with the key below, the way every published vault on sgit.ai and the newsroom does. The key is a read key: derived one way from the vault key, it decrypts and cannot write, and there is no privilege inside it to escalate. It is published on purpose, so treat it as you would the content.</p>
<p class="kv"><b>Read key</b> <code>{E(v["read_key"])}</code></p>
<p><a class="door" href="{E(v["open_url"])}" rel="noopener"><b>Open the vault in the browser &rarr;</b><span>dev.vault.sgraph.ai decrypts it in your tab; the server that stores it cannot read it</span></a></p>
<pre>$ sgit clone {E(v["read_key"])}</pre>
<p class="caveat">{E(v["note"])}</p>
<h2>What is in it</h2>
<ul>
<li><code>sources/&lt;slug&gt;/</code>: one folder per source, with <code>source.json</code>, <code>notes.md</code>, dated <code>captures/</code> (page, rendered page, text, screenshot, headers, provenance with hashes) and <code>raw/</code> with <code>SHA256SUMS</code>.</li>
<li><code>claims/&lt;agent&gt;.json</code> and <code>timeline/&lt;agent&gt;.json</code>: one file per agent.</li>
<li><code>memos/</code>: the editor's voice memos; <code>notes/</code>: agents' working notes; <code>tools/</code>: the capture tool and the index builder.</li>
</ul>
<p>The manifest this site is built from, with every hash, is <a href="../../data/sources.json">data/sources.json</a>; the sources are listed on <a href="../../sources/index.html">every source</a>. The telemetry vault (<code>{E(A["telemetry_vault"]["id"])}</code>) is separate and private: {E(A["telemetry_vault"]["note"])}</p>
"""
    page('admin/vault/index.html', 'The evidence vault, opened', 'The read key to the evidence vault behind this site, the link that opens it in the browser, and what is in it.', body, kind='free')
    t = D['telemetry']; rep = TREP
    def tt(pairs, h):
        return table([h, 'Events'], [[E(str(k)), E(str(n))] for k, n in pairs]) if pairs else '<p class="small">Nothing yet.</p>'
    repo_html = '<p class="small">No report has been drained yet.</p>' if not rep else f"""
<p>Report as of <b>{E(rep["as_of"])}</b>: <b>{rep["events"]}</b> events from <b>{rep["sessions"]}</b> sessions ({rep["test_or_undecryptable"]} test or undecryptable rows excluded). {E(rep["note"])}</p>
<div class="cols">{tt(rep["by_country"], "Country")}{tt(rep["by_region"], "Region")}{tt(rep["by_referrer"], "Referrer host")}{tt(rep["by_screen"], "Screen")}</div>
<h3>By page</h3>{tt(rep["by_path"], "Page")}
<h3>By day</h3>{tt(rep["by_day"], "Day")}"""
    body = f"""
<h1>Who reads this site</h1>
<p class="lead">Every page sends one anonymous event to a write-only lane on a separate, private vault: which page, the referrer's host, the visitor's country, region and city from a geolocation lookup, language, screen class and time zone, with a random session id that lives in the tab. No IP address, no cookie, no name, no user-agent string. The event is encrypted in your browser to the key below before it leaves; the lane's reply is a blind <code>{{"ok": true}}</code>. Do Not Track and Global Privacy Control switch it off. The brief is on <a href="../briefs/index.html#2026-10-22__telemetry-over-an-append-lane">briefs</a>.</p>
<h2>What this page carries</h2>
<p>{E(t["what"])}</p>
<p class="kv"><b>Lane</b> vault <code>{E(t["vault_id"])}</code> on <code>{E(t["endpoint"])}</code> &middot; <b>append token</b> <code>{E(t["append_token"])}</code> (write-only; publishable by design) &middot; <b>encrypted to</b> <code>{E(t["recipient"]["fingerprint"])}</code></p>
<pre>{E(t["recipient"]["encrypt"])}</pre>
<p>The geolocation lookup goes to {" then ".join(f"<code>{E(u)}</code>" for u in t["geo"])}; that service sees your IP address and returns a country, a region and a city; the event keeps the three names and nothing else. The vault server sees that a lane received something, its size and the time, and the requesting IP, as any server does.</p>
<h2>The counts</h2>
{repo_html}
<h2>What the counts are worth</h2>
<ul>
<li>Every row is an untrusted claim: the token and the public key are on this page, so anyone can add rows or flood the lane (1000 pending per token, then the lane returns 507).</li>
<li>The counts are a floor: visitors with blockers, Do Not Track or Global Privacy Control do not appear.</li>
<li>Nobody can be identified from them, by design, and no row leaves the vault; the drainer publishes counts.</li>
</ul>
<p>Mechanics: <code>assets/telemetry.js</code> sends; <code>admin/build/telemetry_drain.py</code>, run by whoever holds the telemetry vault key, lists the lane with the enum key, fetches, decrypts with the private key, marks processed and writes <code>reports/</code>; <code>data/telemetry-report.json</code> is the latest report, copied into this repository at each drain.</p>
"""
    page('admin/telemetry/index.html', 'Who reads this site: anonymous telemetry over an append lane', 'What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.', body, kind='free')


# ----------------------------------------------------------------------------- the review layer (v0.2.5)

def build_review():
    R = D['review']
    by = {n['id']: n for n in R['nodes']}
    out_edges = {}
    for e in R['edges']:
        out_edges.setdefault(e['from'], []).append(e)
    rem = [n for n in R['nodes'] if n['layer'] == 'remediation' and n['id'] != 'fix-commit']
    vuln = [n for n in R['nodes'] if n['layer'] == 'vulnerability']
    # remediation cards, each linked to the code files that realise it
    cards = ''
    for n in rem:
        files = [by[e['to']] for e in out_edges.get(n['id'], []) if e['rel'] == 'realised in']
        addresses = [by[e['to']]['name'].split(':')[0] for e in out_edges.get(n['id'], []) if e['rel'] == 'addresses']
        fl = ''.join(f'<li><a href="{E(f.get("url") or "#")}" rel="noopener nofollow"><code>{E(f["name"][5:])}</code></a> <span class="small">+{f.get("add", 0)} / -{f.get("dele", 0)}</span></li>' for f in files)
        cards += f'<article class="cve" id="{E(n["id"])}"><h3><a href="ui/index.html#{E(n["id"])}">{E(n["name"])}</a></h3><p>{E(n["text"])}</p>' + (f'<p class="small"><b>Functions.</b> <code>{E(n["func"])}</code>{" &middot; <b>new setting</b> <code>" + E(n["ini"]) + "</code>" if n.get("ini") else ""}</p>' if n.get('func') else '') + (f'<p class="small">Addresses: {", ".join(E(a) for a in addresses)}</p>' if addresses else '') + (f'<ul class="files">{fl}</ul>' if fl else '') + '</article>'
    areas_t = table(['Area', 'Files', 'Added', 'Removed'], [[E(a), E(str(n)), E(str(ad)), E(str(de))] for a, n, ad, de in R['areas'][:20]], 'ctx')
    # the SVG: vulnerability on the right, the fix in the middle, remediation around it, code areas on the left
    body = f'''
<h1>The fix, mapped to the code</h1>
<p class="lead">The editor asked for the kind of source-code mapping we did at <a href="https://secrets.sgit.ai/review/">secrets.sgit.ai/review</a>: the project as layered graphs, the intent on one side and the code derived from the syntax tree on the other, with the join between them. Here the intent is the two flaws and the design of the patch; the code is what the patch changed in <a href="https://github.com/php/php-src">php-src</a>, read from the diff by a parser rather than a model. Three layers, {R["counts"]["nodes"]} nodes and {R["counts"]["edges"]} edges; <a href="ui/index.html">walk them in the navigator</a>, or read the map below.</p>
<p class="kv"><b>Commit</b> <code>{E(R["short"])}</code> &middot; <b>{R["counts"]["files"]}</b> files changed, {R["counts"]["engine_files"]} of them in the engine and bundled extensions traced here &middot; <b>{R["counts"]["areas"]}</b> areas</p>
{section("flaws", "The flaws", "".join(f'<p><b>{E(v["name"])}</b> {E(v["text"])} <span class="refs">{src_links([v["source"]], 1)}</span></p>' for v in vuln))}
{section("remediation", "What the fix does, and where", '<p>Each card is one thing the patch does, with the functions it uses and the files it changed. The text describes the remediation; how the flaw is reached is on <a href="../flaws/index.html">the two flaws</a> and <a href="../code/index.html">the code</a>, which this layer sits beside.</p>' + cards)}
{section("areas", "The change, by area", f'<p>The patch is {R["counts"]["files"]} files because the new allocation contract touched every place in the engine and the bundled extensions that used to abort on a failed allocation. The twenty largest areas:</p>' + areas_t + '<p>The full per-file data, with the functions each hunk changed, is <a href="../data/review.json">data/review.json</a> and <a href="../review/code/files.json">review/code/files.json</a>, derived from <code>git show</code> of the commit.</p>')}
{section("how", "How this was built", '<ul><li><b>The code layer</b> is derived by a parser from <code>git show -U0</code> of the fix commit: files, the functions each hunk falls in, the symbols the patch adds. Never a model, so it cannot invent a function that is not in the diff.</li><li><b>The remediation layer</b> is written from the commit message and the diff and checked against the two GitHub advisories; it is the one layer a person wrote, and it is marked as such.</li><li><b>The join</b> is the "realised in" edges from each remediation node to the files that carry it.</li><li>It follows the estate brief <a href="https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.html">Code review graphs in the repository</a>, at the smallest size that still maps a change to its code.</li></ul>')}
'''
    page('review/index.html', 'The fix, mapped to the code', 'The php2shell fix as layered graphs: the two flaws, the design of the patch, and the php-src files and functions it changed, derived from the diff.', body, kind='analysis', topics='php2shell code review')
    # the navigator
    body = f'''
<h1>Walk the graph</h1>
<p class="lead">The review graph in a navigator: the node in focus and its neighbours, laid out live, every node a link. Start at the fix and walk out to the flaws it closes or in to the files that carry it. The data is <a href="../../data/review.json">data/review.json</a>; the static map is <a href="../index.html">the fix mapped to the code</a>.</p>
<div id="rv" class="review-ui"><noscript>The navigator needs JavaScript. The same graph is on <a href="../index.html">the fix mapped to the code</a>.</noscript></div>
<script src="../../assets/review-nav.js" defer></script>
'''
    page('review/ui/index.html', 'Walk the graph: the fix and the code', 'A navigator over the php2shell review graph: the fix, the flaws it closes, and the files and functions it changed, each a link.', body, kind='evidence', topics='php2shell code review navigator')


# ----------------------------------------------------------------------------- questions, kept by the librarian (v0.2.6)

def q_link(path, depth):
    """A site page as a link with its own title, so a question points at pages, not paragraphs."""
    bare = path.split('#')[0]
    title = next((t for p, t, _, _ in PAGES if p == bare), None) or next((t for _, items in NAV for p, t in items if p == bare), bare)
    return f'<a href="{"../" * depth}{E(path)}">{E(title)}</a>'

def build_questions():
    Q = D['questions']
    qs = Q['questions']
    lib = Q['librarian']
    for i, q in enumerate(qs):
        paras = ''.join(f'<p>{a["html"]} <span class="refs">{src_links(a["sources"], 2)}</span></p>' for a in q['answer'])
        who = table(['If', 'Then'], [[E(w['if']), w['then']] for w in q['who']]) if q.get('who') else ''
        see = ''.join(f'<li>{q_link(p, 2)}</li>' for p in q['see'])
        nxt = qs[(i + 1) % len(qs)]
        url = f'{BASE_URL}/questions/{q["id"]}/index.html'
        body = f'''
<p class="kicker">Question &middot; kept by the {E(lib["name"].lower())} &middot; <code>{E(lib["address"])}</code></p>
<h1>{E(q["q"])}</h1>
<p class="small">How it was asked: {E(q["heard"])}</p>
{section("short", "The short answer", f'<p class="lead">{E(q["short"])}</p><p class="small">To paste back where it was asked: the paragraph above and <code>{E(url)}</code></p>')}
{section("who", "What it means for you", who) if who else ""}
{section("why", "The answer, with its sources", paras)}
{section("see", "The pages that carry it", f'<ul>{see}</ul>')}
<p>Next question: <a href="../{E(nxt["id"])}/index.html">{E(nxt["q"])}</a> &middot; <a href="../index.html">every question</a>. Nothing here is advice for your environment; the <a href="https://www.php.net/archive/2026.php#2026-10-21-5" rel="noopener">php.net advisory</a> and your national agency are the authorities.</p>
'''
        page(f'questions/{q["id"]}/index.html', q['q'], q['short'], body, kind='story', topics='php2shell questions')
    rows = [[f'<a href="{E(q["id"])}/index.html"><b>{E(q["q"])}</b></a>', E(q['short']), ' '.join(q_link(p, 1) for p in q['see'][:3])] for q in qs]
    seen = table(['Seen', 'What', 'State', 'Answered by'], [[E(x['seen']), f'<b>{E(x["publisher"])}</b>: <a href="{E(x["url"])}" rel="noopener nofollow">{E(x["title"])}</a><div class="note">{E(x["standfirst"])}</div>', E(x['state']), '<br>'.join(f'<a href="{E(a)}/index.html">{E(next(q["q"] for q in qs if q["id"] == a))}</a>' for a in x['answered_by'])] for x in Q['seen']])
    catalogue = ''
    for label, items in NAV:
        if label == 'Questions':
            continue
        lis = ''.join(f'<li>{q_link(p, 1)}: {E(next((d for pp, _, d, _ in PAGES if pp == p), ""))}</li>' for p, _ in items)
        catalogue += f'<h3>{E(label)}</h3><ul class="small">{lis}</ul>'
    body = f'''
<h1>Questions readers ask</h1>
<p class="lead">The questions people ask about php2shell when they see the headline, each with a short answer that can be pasted back where it was asked, the longer answer with its sources, and the pages that carry it. Kept by the {E(lib["name"].lower())}, <code>{E(lib["address"])}</code>: {E(lib["beat"])}.</p>
{section("questions", "The questions", table(['Question', 'The short answer', 'Read'], rows, 'claims'))}
{section("seen", "Seen by readers, not yet in the vault", seen + '<p class="small">An article a reader has seen is listed here until a collector captures it into the evidence vault. Until then it is not cited anywhere on this site; the answers above rest on what is captured.</p>')}
{section("catalogue", "The catalogue: every page, and what it answers", catalogue + '<p class="small">Every page also has a markdown twin, listed in <a href="../llms.txt">llms.txt</a>; the questions themselves are <a href="../data/questions.json">data/questions.json</a>.</p>')}
{section("ask", "Asking a new question", f'<p>{E(lib["rule"])} A question that is asked twice gets a page. The librarian\'s role, rules and the mistake behind them are on <a href="../team/index.html#librarian">the team page</a>.</p>')}
'''
    page('questions/index.html', 'Questions readers ask about php2shell', 'Can anything be done or do we wait for updates? Has anyone been hacked? Is it really most websites? Short answers to paste back, the sources behind them, and the pages that carry each one.', body, kind='story', topics='php2shell questions faq')


if __name__ == '__main__':
    main()
