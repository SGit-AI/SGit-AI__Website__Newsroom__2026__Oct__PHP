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
SITE_NAME = 'PHP October 2026'
BASE_URL = 'https://' + SITE
REPO_URL = 'https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP'
NEWSROOM = 'https://newsroom.sgit.ai/php-flaws/index.html'

def load(name):
    with open(os.path.join(DATA, name + '.json'), encoding='utf-8') as f:
        return json.load(f)

VERSION = open(os.path.join(ROOT, 'VERSION'), encoding='utf-8').read().strip()
D = {k: load(k) for k in ('story', 'claims', 'timeline', 'numbers', 'agencies', 'affected', 'exploitation',
                          'actors', 'roles', 'versions', 'billing', 'sources', 'vault', 'software',
                          'vault-claims', 'vault-timeline', 'code', 'history', 'impact', 'defence',
                          'personas', 'glossary', 'plain')}
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
    pub = re.sub(r'\s+,', ',', pub)
    return pub if len(pub) <= 34 else pub[:34].rsplit(' ', 1)[0].rstrip(',') + '…'

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
    ('Start here', [('start/index.html', 'Who are you? Pick a reader'), ('explained/index.html', 'Explained from the start'), ('glossary/index.html', 'Glossary: every term, in plain English')]),
    ('The story', [('index.html', 'Front page'), ('summary/index.html', 'The specialist summary'), ('flaws/index.html', 'The two flaws'), ('code/index.html', 'The code'), ('timeline/index.html', 'Timeline'),
                   ('discovery/index.html', 'Who found it'), ('leak/index.html', 'How disclosure broke'),
                   ('exploitation/index.html', 'Exploitation signals'), ('impact/index.html', 'Impact: offline vs compromised'),
                   ('defence/index.html', 'Detection and defence'), ('context/index.html', 'In context: 2008 to 2026'), ('playbook/index.html', 'If you run PHP')]),
    ('The evidence', [('claims/index.html', 'Every claim'), ('numbers/index.html', 'The numbers'), ('agencies/index.html', 'The agencies'),
                      ('affected/index.html', 'Affected systems'), ('affected/software.html', 'Software inventory'), ('sources/index.html', 'Every source'),
                      ('actors/index.html', 'Who says what'), ('graph/index.html', 'As a graph')]),
    ('Briefings', [(f'briefings/{a["id"]}/index.html', a['name']) for a in D['roles']['audiences']]),
    ('About', [('method/index.html', 'The method'), ('team/index.html', 'The team'), ('billing/index.html', 'The billing model'),
               ('account/index.html', 'Your reading account'), ('brief/index.html', 'The brief'),
               ('corrections/index.html', 'Corrections'), ('admin/versions.html', 'Release history'), ('admin/index.html', 'Admin & engineering')]),
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
    page_meter = '' if kind == 'free' else f'<sg-meter view="page" kind="{E(kind)}" date="{E(date or STORY["data_as_of"][:10])}" topics="{E(topics)}" title="{E(title)}"></sg-meter>'
    ld = {
        '@context': 'https://schema.org', '@type': ld_type, 'headline': title, 'description': description,
        'url': f'{BASE_URL}/{path}', 'isPartOf': {'@type': 'WebSite', 'name': SITE_NAME, 'url': BASE_URL},
        'license': 'https://creativecommons.org/licenses/by/4.0/', 'dateModified': STORY['data_as_of'][:10],
        'version': VERSION,
    }
    return f'''<!doctype html>
<html lang="en" data-root="{up}" data-path="{path}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)} &middot; {SITE_NAME}</title>
<meta name="description" content="{E(description)}">
<link rel="canonical" href="{BASE_URL}/{path}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:url" content="{BASE_URL}/{path}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(description)}">
<meta name="twitter:card" content="summary">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="icon" href="data:,">
<link rel="alternate" type="text/markdown" href="{up}{md_path(path)}">
<link rel="stylesheet" href="{up}assets/site.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/json" id="sg-meter-config">{meter_json}</script>
<script type="module" src="{up}assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js"></script>
<script src="{up}assets/personas.js" defer></script>
<script src="{up}assets/site.js" defer></script>
</head>
<body>
<nav class="site"><div class="row">
  <a class="brand" href="{up}index.html">PHP October<span> 2026</span></a>
  <a class="ver" href="{up}admin/versions.html#v{E(VERSION)}" title="Site release history: what v{E(VERSION)} changed">v{E(VERSION)}</a>
  <span class="status">{E(STORY["status"])} &middot; last checked {E(human_time(STORY["data_as_of"]))}</span>
  <span class="crumbs"><a href="https://newsroom.sgit.ai/">newsroom</a> / <a href="https://2026.newsroom.sgit.ai/">2026</a> / <a href="https://oct.2026.newsroom.sgit.ai/">October</a> / <b>PHP</b></span>
  <sg-meter view="balance"></sg-meter>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-items" aria-label="Menu">Menu</button>
  <div class="nav-items" id="nav-items">{''.join(nav_items)}<a class="nl ext" href="{up}llms.txt">llms.txt</a></div>
</div></nav>
<main>
{body}
{page_meter}
</main>
<footer class="site">
  <div class="row">
    <p><b>{SITE_NAME}</b> ({SITE}) tracks PHP news for one month. This month that is one story, the two critical PHP security flaws, followed as evidence: every claim with a status and its sources, every source captured, dated and hashed into a private vault. Built and run by one editor and a team of software agents; <a href="{up}team/index.html">the roles</a> and <a href="{up}method/index.html">the method</a> are public, and the site is rebuilt from the vault, never written by hand. One of the SGit Newsroom's story sites: up from here are <a href="https://oct.2026.newsroom.sgit.ai/">October 2026</a>, <a href="https://2026.newsroom.sgit.ai/">the year</a> and <a href="https://newsroom.sgit.ai/">the newsroom</a>, whose own section on the story is <a href="{NEWSROOM}">here</a>. Part of the <a href="https://sgit.ai/network/index.html">sgit.ai network</a>.</p>
    <p class="disc">&#9888; Participant disclosure: published by the sgit project, which builds the vault and metering stack this site runs on. Content CC BY 4.0 for this site's own text, tables and data; quoted words are their authors', linked; no third-party page is reproduced. Code Apache-2.0.</p>
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
    plain = D['plain']['pages'].get(path)
    if plain:
        body = body.replace('</h1>', f'</h1>\n<aside class="plainbox"><b>In plain English</b> {E(plain)}</aside>', 1)
    WORDS[path] = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<(svg|script|table).*?</\1>', ' ', body, flags=re.S)).split())
    html_out = layout(path, title, description, gloss(body, path), **kw)
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

# ----------------------------------------------------------------------------- readers: personas, glossary, reading time

WORDS = {}    # path -> words in the page body; filled by page(), read on the second pass
GLOSSED = {}  # path -> glossary ids linked on that page, in order of first use
TERMS = [t for t in D['glossary']['terms']]
TERM = {t['id']: t for t in TERMS}
GLOSS_RX = [(t, [re.compile(m) for m in t['match']]) for t in TERMS if t['match']]
PERSONAS = OrderedDict((p['id'], p) for p in D['personas']['personas'])
GROUPS = OrderedDict((g['id'], g) for g in D['personas']['groups'])
DEPTHS = D['personas']['depths']
AUD = {a['id']: a for a in D['roles']['audiences']}
FLAGSHIP = {'CVE-2026-109618': 'the out-of-memory flaw', 'CVE-2026-109619': 'the stale global state flaw'}
GLOSS_SKIP = {'a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4', 'svg', 'script', 'style', 'th', 'button', 'summary', 'title', 'label'}
CVE_RX = re.compile(r'\bCVE-\d{4}-\d{4,7}\b')

def minutes(path):
    return max(1, round(WORDS.get(path, 0) / 230))

def nav_title(path):
    if path.startswith('briefings/'):
        return 'Your briefing'
    for _, items in NAV:
        for p, t in items:
            if p == path:
                return t
    return path

def gloss(body, path):
    """Link the first use of every glossary term on the page, and every CVE ID, in text outside links, code and headings."""
    if path.startswith('glossary/'):
        return body
    up = '../' * path.count('/')
    used, out, skip = [], [], 0
    for tok in re.split(r'(<[^>]+>)', body):
        if tok.startswith('<'):
            m = re.match(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)', tok)
            if m and m.group(2).lower() in GLOSS_SKIP and not tok.endswith('/>'):
                skip = max(0, skip + (-1 if m.group(1) else 1))
            out.append(tok)
            continue
        if skip or not tok.strip():
            out.append(tok)
            continue
        spans = []
        for m in CVE_RX.finditer(tok):
            cve = m.group(0)
            if cve in FLAGSHIP:
                href = ('' if path == 'flaws/index.html' else f'{up}flaws/index.html') + f'#{cve}'
                tip = f'{cve}: {FLAGSHIP[cve]}, one of the two php2shell flaws. CVSS 9.2, critical. Fixed 21 October 2026.'
            elif 'cve-' + cve.lower() in SOURCES:
                href, tip = f'{up}sources/cve-{cve.lower()}/index.html', f'{cve}: an earlier flaw; its official record, as captured into the vault.'
            else:
                href, tip = f'https://www.cve.org/CVERecord?id={cve}', f'{cve}: its official record at cve.org.'
            ext = ' rel="noopener"' if href.startswith('http') else ''
            spans.append((m.start(), m.end(), f'<a class="cve-link" href="{href}"{ext} data-term="{cve}" data-tip="{E(tip)}">{cve}</a>'))
        for t, rxs in GLOSS_RX:
            if t['id'] in used:
                continue
            for rx in rxs:
                hit = next((m for m in rx.finditer(tok) if not any(a < m.end() and m.start() < b for a, b, _ in spans)), None)
                if hit:
                    spans.append((hit.start(), hit.end(), f'<a class="term" href="{up}glossary/index.html#{t["id"]}" data-term="{E(t["term"])}" data-tip="{E(t["short"])}">{hit.group(0)}</a>'))
                    used.append(t['id'])
                    break
        spans.sort()
        last, buf = 0, []
        for a, b, rep in spans:
            buf.append(tok[last:a]); buf.append(rep); last = b
        buf.append(tok[last:])
        out.append(''.join(buf))
    GLOSSED[path] = used
    return ''.join(out)

def avatar(p):
    return f'<span class="av av-{E(p["group"])}" aria-hidden="true">{E(p["person"][0])}</span>'

def depth_badge(d):
    d = str(d)
    return f'<span class="depth depth-{d}" title="{E(DEPTHS[d]["text"])}"><i></i><i></i><i></i>{E(DEPTHS[d]["label"])}</span>'

def path_minutes(p):
    return sum(minutes(x) for x in p['path'])

def door(p, depth=0):
    a = AUD[p['id']]
    return (f'<a class="door door-{E(p["group"])}" href="{"../" * depth}briefings/{E(p["id"])}/index.html" data-persona="{E(p["id"])}">'
            f'<span class="dh">{avatar(p)}<span><b>{E(p["label"])}</b><small>{E(p["person"])} &middot; {depth_badge(p["depth"])}</small></span></span>'
            f'<span class="dq">{E(a["question"])}</span>'
            f'<span class="dm">{len(p["path"])} reads &middot; about {path_minutes(p)} min <span class="go">Start &rarr;</span></span></a>')

def persona_doors(depth=0):
    out = ''
    for gid, g in GROUPS.items():
        ps = [p for p in PERSONAS.values() if p['group'] == gid]
        out += f'<div class="dgroup dgroup-{E(gid)}"><h3>{E(g["label"])}</h3><p class="small">{E(g["text"])}</p><div class="doors">{"".join(door(p, depth) for p in ps)}</div></div>'
    return f'<div class="dgroups">{out}</div>'

def reading_path(p, depth):
    items = ''.join(f'<li><a href="{"../" * depth}{E(x)}">{E(nav_title(x))}</a> <span class="small">{minutes(x)} min</span></li>' for x in p['path'])
    return f'<ol class="rpath">{items}</ol><p class="small">About {path_minutes(p)} minutes in all. Choose <i>read as {E(p["person"])}</i> and the bar under the menu keeps your place on every page.</p>'

def words_met(p, depth, limit=14):
    seen = []
    for x in p['path']:
        for t in GLOSSED.get(x, []):
            if t not in seen:
                seen.append(t)
    chips = ''.join(f'<a class="chip" href="{"../" * depth}glossary/index.html#{E(t)}" title="{E(TERM[t]["short"])}">{E(TERM[t]["term"])}</a>' for t in seen[:limit])
    return f'<p class="chips">{chips}</p>' if chips else ''

# ----------------------------------------------------------------------------- pages

def human_time(at):
    """2026-10-22T11:34Z as 22 October 2026, 11:34 UTC."""
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})T(\d{2}:\d{2})', at or '')
    if not m:
        return at
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return f'{int(m.group(3))} {months[int(m.group(2)) - 1]} {m.group(1)}, {m.group(4)} UTC'

PLAIN_STATUS = {'confirmed': 'Confirmed', 'reported': 'Reported', 'disputed': 'Disputed', 'contradicted': 'Contradicted', 'unverified': 'Unverified'}

def build_index():
    s, pl, im = STORY, D['plain'], D['impact']
    when = human_time(s['data_as_of'])
    fixed = ', '.join(D['affected']['fixed'][:-1]) + ' or ' + D['affected']['fixed'][-1]
    tiles = [
        ('ok', 'Is there a fix?', 'Yes', f'install PHP {fixed}', 'playbook/index.html'),
        ('bad', 'How serious?', 'Critical', '9.2 out of 10, both flaws', 'flaws/index.html'),
        ('warn', 'Are attackers trying?', 'Yes', 'millions of attempts, seen by one internet security company', 'exploitation/index.html'),
        ('info', 'Anyone confirmed hacked?', 'Not yet', 'no organisation, as of the latest check', 'impact/index.html'),
        ('warn', 'Websites taken offline', f'{len(im["offline"])} organisations', 'reported, as a precaution', 'impact/index.html'),
        ('info', "On the US 'used in attacks' list?", 'Not yet', "the US government's official list of flaws known to be used by attackers", 'exploitation/index.html#kev'),
        ('bad', 'What do governments say?', 'Update now', f'or take the website offline if you cannot; {C["agencies"]} agencies compared', 'agencies/index.html'),
    ]
    board = ''.join(f'<a class="tile tile-{t}" href="{h}"><span class="tl">{E(l)}</span><b>{E(v)}</b><span class="tn">{E(n)}</span></a>' for t, l, v, n, h in tiles)
    now = ''.join(f'<li>{E(x["text"])} <span class="refs">{src_links(x["sources"], 0)}</span></li>' for x in pl['now'])
    facts = ''.join(f'<li><span class="fs">{pill(f["status"])}</span><div><p>{E(f["text"])}</p><p class="ff"><span class="refs">{src_links(f["sources"], 0)}</span> <a href="{E(f["href"])}">More &rarr;</a></p></div></li>' for f in pl['facts'])
    unknown = ''.join(f'<li><a href="{E(u["href"])}">{E(u["text"])}</a></li>' for u in pl['unknown'])
    latest = ''.join(f'<li><span class="when">{E(x["when"])}</span><span>{E(x["text"])} <span class="refs">{src_links(x["sources"], 0)}</span></span></li>' for x in pl['latest'])
    moments = ''.join(f'<li class="m m-{E(m["tone"])}"><a href="{E(m["href"])}"><span class="mw">{E(m["when"])}</span><span class="mt">{E(m["what"])}</span></a><span class="refs">{src_links(m["sources"], 0)}</span></li>' for m in pl['moments'])
    legend = ''.join(f'<li>{pill(k)} {E(v)}</li>' for k, v in [('confirmed', 'two or more original sources agree'), ('reported', 'one party says so; nobody has contradicted it'), ('disputed', 'sources disagree'), ('unverified', 'nobody has been able to check it')])
    evidence = ''.join([
        stat(C['sources'], 'web pages saved as evidence, each with the time it was saved', 'sources/index.html'),
        stat(C['claims'], f'statements checked: {C["by_status"]["confirmed"]} confirmed, {C["by_status"]["disputed"] + C["by_status"]["contradicted"]} disputed, {C["by_status"]["unverified"]} unverified', 'claims/index.html'),
        stat(C['events'], 'dated events, from 2024 to today', 'timeline/index.html'),
        stat(C['agencies'], "government agencies' advice compared", 'agencies/index.html'),
    ])
    who_lead = f'The same evidence, put in order for {len(PERSONAS)} kinds of reader. Each starts with a thirty-second answer in plain words. <a href="start/index.html">How the readers are mapped</a>.'
    body = f'''
<header class="hero hero2">
  <p class="kicker">PHP news &middot; October 2026 &middot; <span class="live">{E(s["status"])}</span> &middot; last checked {E(when)}</p>
  <h1>{E(pl["headline"])}</h1>
  <p class="deck">{E(pl["deck"])}</p>
  <div class="ctas"><a class="cta cta-pri" href="#now">What is happening now</a><a class="cta" href="#who">The briefing for you</a><a class="cta" href="explained/index.html">Explain it from the start</a></div>
  <p class="aka">{E(pl["aka"])}</p>
</header>
<section id="now"><h2>Right now</h2><p class="small">As of {E(when)}, the time of the latest page this site saved.</p><ul class="nowlist">{now}</ul></section>
{section("state", "At a glance", f'<div class="tiles">{board}</div>')}
{section("facts", "The core facts, and the evidence for each", f'<ul class="legend">{legend}</ul><ol class="facts">{facts}</ol>', "Each fact links to the original pages it rests on: the PHP project, government agencies, the researchers. Click a source to see when it was saved and its fingerprint.")}
{section("unknown", "What nobody knows yet", f'<ul class="unknown">{unknown}</ul>', "Stated, not papered over. This site will update each one when the evidence does.")}
{section("latest", "Latest", f'<ol class="latest">{latest}</ol><p><a href="timeline/index.html">Everything, in order, on the timeline &rarr;</a></p>')}
{section("who", "The briefing for you", persona_doors(), who_lead)}
{section("moments", "How it unfolded", f'<ol class="moments">{moments}</ol>')}
{section("evidence", "How this site knows", f'<div class="stats">{evidence}</div><p>Every page this site relies on was saved at the moment it was read, with a fingerprint that proves it has not been altered since, so a fact can be checked even if the original page changes or disappears. Nothing here is advice for your own systems; for that, read <a href="https://www.php.net/archive/2026.php#2026-10-21-5" rel="noopener">the PHP project\'s announcement</a> and your national cyber agency. The site is put together by software agents working for one editor, Dinis Cruz; <a href="method/index.html">how it works</a>.</p><p>Already know the vocabulary? <a href="summary/index.html">The specialist summary</a> has the technical version of this page, with every number and the full last 48 hours.</p>')}
'''
    page('index.html', s['title'], s['description'], body, kind='story', topics='php october 2026 overview', ld_type='NewsArticle')

def build_summary():
    s = STORY
    known = ''.join(f'<li>{k["html"]} <span class="refs">{src_links(k["sources"], 1)}</span></li>' for k in s['known'])
    openq = ''.join(f'<li>{o["html"]}</li>' for o in s['open'])
    stats = ''.join([
        stat(C['sources'], 'sources in the evidence vault', 'sources/index.html', 1),
        stat(C['captures'], 'dated captures, each file hashed', 'sources/index.html', 1),
        stat(C['claims'], f'claims with a status: {C["by_status"]["confirmed"]} confirmed, {C["by_status"]["disputed"] + C["by_status"]["contradicted"]} disputed or contradicted, {C["by_status"]["unverified"]} unverified', 'claims/index.html', 1),
        stat(C['events'], 'dated events on the timeline', 'timeline/index.html', 1),
        stat(C['agencies'], 'national agencies compared', 'agencies/index.html', 1),
        stat(len(D['impact']['offline']), 'operators reported offline, 0 confirmed compromises', 'impact/index.html', 1),
        stat(C['software'], 'products in the NCSC-NL inventory', 'affected/software.html', 1),
    ])
    latest = sorted([t for t in D['timeline'] if t['at'] >= '2026-10-20'], key=lambda t: t['at'])[-8:]
    latest_rows = [[f'<span class="when">{E(fmt_at(t["at"]))}</span>', E(t['event']), src_links(t['sources'], 1)] for t in latest]
    numrow = ''.join(f'<a class="num" href="../numbers/index.html#{E(n["id"])}"><b>{E(n["value"])}</b><span>{E(n["of"])}</span>{pill(n["status"])}</a>' for n in D['numbers'][:6])
    body = f'''
<p class="kicker">The story &middot; for specialists</p>
<h1>The specialist summary: php2shell, CVE-2026-109618 and CVE-2026-109619</h1>
<p class="lead">{s["lead_html"]}</p>
<div class="stats">{stats}</div>
<p class="caveat">{s["caveat_html"]}</p>
{section("numbers", "Six numbers, and what each one measures", f'<div class="nums">{numrow}</div><p>The figures in circulation range from 2.6 million hosts to 70% of the Internet. They are not contradictory so much as incommensurable: each measures a different thing. <a href="../numbers/index.html">The numbers page</a> says what each one counts, who said it, and whether anyone has checked it.</p>')}
{section("known", "What is established", f'<ul class="known">{known}</ul>')}
{section("open", "What is not", f'<ul class="open">{openq}</ul>', "Open questions, stated rather than papered over. Each one names what would close it.")}
{section("latest", "The last 48 hours", table(["When (UTC)", "What", "Source"], latest_rows, "tl") + '<p><a href="../timeline/index.html">The whole timeline &rarr;</a> runs from the 2024 audit to the latest capture, with every time stated as its source states it and every conversion marked.</p>')}
{section("how", "How this site works", '<p>Every source is captured into a private, encrypted vault, each file hashed at capture time; every claim carries one of five status words and the sources that earn it; the site is a deterministic build of the vault, and a gate refuses a broken link, an unsourced claim or a credential. <a href="../method/index.html">The method</a>, <a href="../team/index.html">the team</a> and <a href="../billing/index.html">the billing model</a> are published.</p>')}
'''
    page('summary/index.html', 'The specialist summary: CVE-2026-109618 and CVE-2026-109619', 'The technical summary of the two PHP flaws of October 2026: what is established with its sources, the six scale figures, the open questions and the last 48 hours.', body, kind='story', topics='php2shell summary')

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
        'everyone': dict(topics=['impact', 'exploitation', 'scale'], intro='You do not need to know anything about computers to follow this. Below are the five things worth knowing, then the evidence behind them, folded away until you want it.', ask=['<b>PHP is not on your phone or laptop.</b> It runs on the servers that build websites. This is a problem for the organisations that run those websites, and it is theirs to fix.', '<b>Nothing to install, nothing to change</b> on your own devices because of this. Be wary of any message that says otherwise and asks you to click or download something: scammers use headlines like this one.', '<b>If a website you use was down on 21 or 22 October, it was most likely a precaution.</b> Dutch government services such as DigiD were taken offline on purpose, as a precaution; that is a decision, not a sign of a break-in.', '<b>Nobody has confirmed being hacked through this yet.</b> Attackers have been trying, in large numbers, and that may change; this site will say so when the evidence does.', '<b>The big numbers in the headlines are not what they sound like.</b> 70% is roughly the share of websites built with PHP, not a share of the Internet that is broken. <a href="../../numbers/index.html">The numbers page</a> explains each one.']),
        'site-owner': dict(topics=['technical', 'advice', 'exploitation'], intro='You do not need to understand the bug to deal with it. What you need is to know whose job the update is, and the exact question to ask. This page gives you both.', ask=['<b>Find out whether your site runs on PHP.</b> WordPress, WooCommerce, Drupal, Joomla, Magento, PrestaShop, Moodle and most hosting control panels do. If you are not sure, ask whoever built the site.', '<b>Updating WordPress, plugins or themes does not fix this.</b> The flaw is in PHP itself, one layer down. It has to be fixed on the server.', '<b>If someone hosts the site for you</b>, send them this, in writing: <i>Has PHP on the server running my site been updated to 8.5.12, 8.4.27, 8.3.36 or 8.2.35, or to your distribution\'s fixed package, and have the PHP processes been restarted since? If my site is on PHP 8.1 or older, what is your plan?</i> Keep the reply.', '<b>If you run the server yourself</b>, update PHP today and restart it. The <a href="../../playbook/index.html">step-by-step list</a> has the temporary settings for a server you cannot update straight away.', '<b>If your site is on PHP 8.1 or older</b>, there is no ready-made fix. Ask your developer or host about moving to a supported version now; it is overdue anyway.', '<b>Keep calm about being hacked.</b> No organisation has confirmed a break-in as of the latest capture. If your host updated promptly, you are in the same position as almost everyone else.']),
        'pm': dict(topics=['advice', 'impact', 'timing'], intro='This is a platform event, not an application bug, so it lands on every team that ships anything running on PHP at once. Plan for it the way you would plan for a datacentre move: an inventory, an owner per system, a date, a test.', ask=['<b>Get the list.</b> Which systems run PHP, who owns each, and which are on the internet. Vendor products and hosting panels count. Without the list nothing else can be scheduled.', '<b>Get a date per system.</b> Updating PHP means installing the fixed version, restarting, rebuilding containers and re-testing. Internet-facing systems first.', '<b>Budget for regression testing.</b> The fix changes how PHP behaves when it runs short of memory: a system that used to limp along may now stop cleanly. Load tests are worth running before the release, not after.', '<b>Plan for precautionary downtime.</b> Agencies advise isolating or taking offline what cannot be updated in time. Agree with stakeholders now who can make that call, how long it may last, and what users see meanwhile.', '<b>Treat PHP 8.1 and older as a project.</b> There is no ready-made release for them. Moving to a supported version is a migration with its own scope and schedule.', '<b>Expect a second round.</b> A report that the first fix may be incomplete is open. Keep a slot free in the next fortnight.']),
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
        p = PERSONAS[a['id']]
        cl = [c for c in D['claims'] if c['topic'] in s['topics']]
        order = {t: i for i, t in enumerate(s['topics'])}
        cl.sort(key=lambda c: (order[c['topic']], list(STATUS_WORDS).index(c['status']) if c['status'] in STATUS_WORDS else 9))
        asks = ''.join(f'<li>{x}</li>' for x in s['ask'])
        openq = ''.join(f'<li>{o["html"]}</li>' for o in STORY['open'][:5])
        needs = ''.join(f'<li>{E(x)}</li>' for x in p['needs'])
        skips = ''.join(f'<li>{E(x)}</li>' for x in p['skip'])
        facts = status_legend() + claim_rows(cl, 2)
        if p['depth'] == 1:
            facts = f'<details class="evidence"><summary>Show the {len(cl)} claims behind this briefing, each with its status and sources</summary>{facts}</details><p class="small">Every sentence above rests on these rows. They are folded away because they are written in the sources\' own vocabulary; the glossary explains each term.</p>'
        others = ' &middot; '.join(f'<a href="../{b["id"]}/index.html">{E(PERSONAS[b["id"]]["label"])}</a>' for b in aud if b['id'] != a['id'])
        body = f'''
<p class="kicker">Briefing for {E(p["person"])}, {E(p["label"].lower())} &middot; {depth_badge(p["depth"])} &middot; from the same {C["claims"]} claims, selected and ordered for one reader</p>
<h1>{E(a["question"])}</h1>
<div class="answer">{avatar(p)}<div><p class="kicker">The answer in thirty seconds</p><p>{E(p["answer"])}</p><p><a class="cta cta-pri" href="../../{E(p["path"][1])}" data-persona="{E(p["id"])}">Read the site as {E(p["person"])} &rarr;</a></p></div></div>
<p class="lead">{s["intro"]}</p>
{section("decide", "What to decide or do", f'<ul class="asks">{asks}</ul>')}
{section("path", "Your reading path", reading_path(p, 2) + '<div class="cols2"><div><h3>What this briefing covers</h3><ul>' + needs + '</ul></div><div><h3>What you can skip</h3><ul>' + skips + '</ul></div></div>')}
{section("words", "Words you will meet", words_met(p, 2) + '<p class="small">Each is underlined where it first appears; hover or tap for a one-line definition, or open <a href="../../glossary/index.html">the glossary</a>.</p>')}
{section("facts", "The facts this rests on", facts)}
{section("open", "What is still open", f'<ul class="open">{openq}</ul>')}
<p>The full set of claims is on <a href="../../claims/index.html">every claim</a>; the ordered steps for a vulnerable system are on <a href="../../playbook/index.html">if you run PHP</a>. Other readers: {others}.</p>
'''
        page(f'briefings/{a["id"]}/index.html', f'Briefing for a {a["name"].lower()}: {a["question"]}', f'The php2shell story for a {a["name"].lower()}: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.', body, kind='briefing', topics=f'php2shell briefing {a["id"]}')

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
    page('team/index.html', 'The team: the editor, the pipeline and the agents', f'Who does what on this site: the editor, the seven-step pipeline from URL to published claim, each agent role with the rule it enforces and the mistake behind it, and the {len(r["audiences"])} audiences.', body, kind='free', topics='team agents')

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
    lines = [f'# {SITE_NAME} ({SITE})', '', f'> {STORY["description"]}', '', f'Site v{VERSION}. Data as of {STORY["data_as_of"]} (the latest capture in the evidence vault, commit {D["vault"]["head"]["commit"]}). Every page below has a markdown twin at the same path with .md; the data behind every page is in data/*.json. The evidence vault is private; its manifest with every hash is data/sources.json.', '']
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
              f'- [billing.json]({BASE_URL}/data/billing.json): the meter configuration and the designed model', f'- [versions.json]({BASE_URL}/data/versions.json): release history', '',
              '## Status words', *[f'- {k}: {v}' for k, v in STATUS_WORDS.items()], '',
              f'Newsroom section on the same story: {NEWSROOM}', f'Repository: {REPO_URL}', 'Licence: content CC BY 4.0, code Apache-2.0.', '']
    write('llms.txt', '\n'.join(lines))

def build_sitejs():
    write('assets/site.js', r'''// php.oct.2026.newsroom.sgit.ai: the menu on narrow screens, the reader bar, and the glossary hover cards.
// The reader you pick and the pages you have opened are kept in this browser's localStorage and nowhere else.
(function () {
  var b = document.querySelector('.nav-toggle'), n = document.getElementById('nav-items');
  if (b && n) {
    b.addEventListener('click', function () {
      var open = n.classList.toggle('open');
      b.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.ni > .nl').forEach(function (a) {
      a.addEventListener('click', function (ev) {
        if (window.matchMedia('(max-width: 900px)').matches) { ev.preventDefault(); a.parentNode.classList.toggle('open'); }
      });
    });
  }

  var html = document.documentElement, root = html.getAttribute('data-root') || '', here = html.getAttribute('data-path') || '';
  function get(k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { if (v === null) window.localStorage.removeItem(k); else window.localStorage.setItem(k, v); } catch (e) {} }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var seen = [];
  try { seen = JSON.parse(get('p2s.seen') || '[]') || []; } catch (e) { seen = []; }
  if (here && seen.indexOf(here) < 0) { seen.push(here); set('p2s.seen', JSON.stringify(seen.slice(-500))); }

  // The reader bar, under the menu on every page.
  var bar = null;
  function renderBar() {
    var P = window.P2S && window.P2S.personas, id = get('p2s.persona'), p = P && id && P[id];
    var nav = document.querySelector('nav.site');
    if (!nav) return;
    if (!bar) { bar = document.createElement('div'); bar.className = 'pbar'; nav.parentNode.insertBefore(bar, nav.nextSibling); }
    document.querySelectorAll('.door.mine').forEach(function (d) { d.classList.remove('mine'); });
    if (p) {
      html.setAttribute('data-depth', String(p.depth));
      var mine = document.querySelector('.door[data-persona="' + id + '"]');
      if (mine) mine.classList.add('mine');
      var steps = '', next = null;
      p.path.forEach(function (x, i) {
        var done = seen.indexOf(x[0]) >= 0, cur = x[0] === here;
        if (!next && !done && !cur) next = x;
        steps += '<li class="' + (cur ? 'here' : done ? 'seen' : '') + '"><a href="' + root + x[0] + '" title="' + esc(x[1]) + ', ' + x[2] + ' min">' + (i + 1) + '</a></li>';
      });
      var nx = next ? '<span class="nx">Next: <a href="' + root + next[0] + '">' + esc(next[1]) + '</a> <small>' + next[2] + ' min</small></span>'
                    : '<span class="nx">Path read. <a href="' + root + 'start/index.html">Try another reader</a></span>';
      bar.className = 'pbar';
      bar.innerHTML = '<div class="row"><span class="av av-' + esc(p.group) + '" aria-hidden="true">' + esc(p.person.charAt(0)) + '</span>' +
        '<span class="who">Reading as <a href="' + root + 'briefings/' + esc(id) + '/index.html"><b>' + esc(p.person) + '</b>, ' + esc(p.label.toLowerCase()) + '</a></span>' +
        '<ol class="steps-mini" aria-label="Your reading path">' + steps + '</ol>' + nx +
        '<a class="chg" href="' + root + 'start/index.html">Change</a><button type="button" class="x" data-persona-clear aria-label="Stop reading as ' + esc(p.person) + '">&times;</button></div>';
      bar.hidden = false;
    } else {
      html.removeAttribute('data-depth');
      if (get('p2s.nudge') === 'off' || here === 'index.html' || here === 'start/index.html') { bar.hidden = true; bar.innerHTML = ''; return; }
      bar.className = 'pbar pbar-new';
      bar.innerHTML = '<div class="row"><span class="who">New to this story? <a href="' + root + 'start/index.html">Tell us who you are</a> for a briefing and a reading path, or start with <a href="' + root + 'explained/index.html">the plain-English explainer</a>.</span>' +
        '<button type="button" class="x" data-nudge-off aria-label="Hide this">&times;</button></div>';
      bar.hidden = false;
    }
  }
  document.addEventListener('click', function (ev) {
    var t = ev.target.closest ? ev.target : null;
    if (!t) return;
    var pick = t.closest('[data-persona]');
    if (pick) { set('p2s.persona', pick.getAttribute('data-persona')); }
    if (t.closest('[data-persona-clear]')) { ev.preventDefault(); set('p2s.persona', null); renderBar(); }
    if (t.closest('[data-nudge-off]')) { ev.preventDefault(); set('p2s.nudge', 'off'); renderBar(); }
  });
  renderBar();

  // Glossary hover cards: the first use of a term on a page carries its one-line definition.
  var tip = null, tipFor = null;
  function showTip(a) {
    var text = a.getAttribute('data-tip');
    if (!text) return;
    if (!tip) { tip = document.createElement('div'); tip.className = 'tip'; tip.id = 'p2s-tip'; tip.setAttribute('role', 'tooltip'); document.body.appendChild(tip); }
    tip.innerHTML = '<b>' + esc(a.getAttribute('data-term') || '') + '</b> ' + esc(text) + '<small>Open the glossary &rarr;</small>';
    tip.style.display = 'block';
    var w = Math.min(330, window.innerWidth - 24), r = a.getBoundingClientRect();
    tip.style.width = w + 'px';
    tip.style.left = Math.max(12, Math.min(r.left, window.innerWidth - w - 12)) + 'px';
    var top = r.bottom + 8;
    if (top + tip.offsetHeight > window.innerHeight - 8) top = Math.max(8, r.top - 8 - tip.offsetHeight);
    tip.style.top = top + 'px';
    a.setAttribute('aria-describedby', 'p2s-tip');
    tipFor = a;
  }
  function hideTip() { if (tip) tip.style.display = 'none'; if (tipFor) tipFor.removeAttribute('aria-describedby'); tipFor = null; }
  document.addEventListener('mouseover', function (ev) { var a = ev.target.closest && ev.target.closest('a[data-tip]'); if (a) showTip(a); });
  document.addEventListener('mouseout', function (ev) { var a = ev.target.closest && ev.target.closest('a[data-tip]'); if (a) hideTip(); });
  document.addEventListener('focusin', function (ev) { var a = ev.target.closest && ev.target.closest('a[data-tip]'); if (a) showTip(a); else hideTip(); });
  document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') hideTip(); });
  window.addEventListener('scroll', hideTip, { passive: true });
})();
''')

def build_all():
    PAGES.clear()
    build_flaws(); build_timeline(); build_discovery(); build_leak(); build_exploitation(); build_playbook()
    build_code(); build_context(); build_impact(); build_defence()
    build_claims(); build_numbers(); build_agencies(); build_affected(); build_sources(); build_graph()
    build_source_pages(); build_actors()
    build_explained(); build_glossary(); build_briefings(); build_start(); build_summary(); build_index()
    build_method(); build_team(); build_billing(); build_account(); build_brief(); build_corrections(); build_admin()

def main():
    # Two passes: the first measures every page (reading time, terms used), the second writes pages that cite those measures.
    build_all()
    build_all()
    build_llms(); build_sitejs(); build_personas_js()
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


# ----------------------------------------------------------------------------- pages added in v0.3: the readers

def build_start():
    cols = ''.join(f'<div class="mh">{depth_badge(d)}<small>{E(DEPTHS[d]["text"])}</small></div>' for d in ('1', '2', '3'))
    rows = ''
    for gid, g in GROUPS.items():
        cells = ''
        for d in (1, 2, 3):
            ps = [p for p in PERSONAS.values() if p['group'] == gid and p['depth'] == d]
            chips = ''.join(f'<a class="pchip" href="#p-{E(p["id"])}">{avatar(p)}<span><b>{E(p["person"])}</b><small>{E(p["label"])}</small></span><span class="pd">{depth_badge(d)}</span></a>' for p in ps)
            cells += f'<div class="mc">{chips}</div>'
        rows += f'<div class="mr"><div class="ml"><b>{E(g["label"])}</b><small>{E(g["text"])}</small></div>{cells}</div>'
    grid = f'<div class="pmap"><div class="mr mhead"><div class="ml"></div>{cols}</div>{rows}</div>'
    cards = ''
    for p in PERSONAS.values():
        a = AUD[p['id']]
        cards += f'''<article class="pcard" id="p-{E(p["id"])}">
<header>{avatar(p)}<div><h3>{E(p["person"])}, {E(p["label"].lower())}</h3><p class="small">{E(GROUPS[p["group"]]["label"])} &middot; {depth_badge(p["depth"])}</p></div></header>
<p><b>Who.</b> {E(p["who"])}</p>
<p><b>Their question.</b> <i>{E(a["question"])}</i></p>
<div class="cols2"><div><h4>Needs</h4><ul>{"".join(f"<li>{E(x)}</li>" for x in p["needs"])}</ul></div><div><h4>Can skip</h4><ul>{"".join(f"<li>{E(x)}</li>" for x in p["skip"])}</ul></div></div>
<div class="answer answer-s"><div><p class="kicker">The answer in thirty seconds</p><p>{E(p["answer"])}</p></div></div>
<h4>Reading path</h4>{reading_path(p, 1)}
<h4>Words they will meet</h4>{words_met(p, 1, 10)}
<p><a class="cta cta-pri" href="../briefings/{E(p["id"])}/index.html" data-persona="{E(p["id"])}">Read as {E(p["person"])} &rarr;</a></p>
</article>'''
    body = f'''
<p class="kicker">Start here</p>
<h1>Who is reading? The site's readers, mapped</h1>
<p class="lead">A story like this one is read by people who have never heard of PHP and by people who maintain it. A page written for one of them fails the other. So before anything else, this site names its readers: {len(PERSONAS)} of them, by what they need to do and how much technical language they can take. Every reader gets a briefing that opens with a thirty-second answer, and a reading path through the rest of the site.</p>
{section("map", "The map", grid, "Across: how much technical language the reader wants. Down: what they need to do with the story. Pick the one closest to you.")}
{section("how", "How the site changes once you pick", """<ul class="howlist">
<li><b>A briefing written for you.</b> The thirty-second answer first, then what to decide or do, then the evidence. For plain-English readers the evidence is folded away until asked for.</li>
<li><b>A reading path that follows you.</b> Choose <i>read as</i> and a bar under the menu shows where you are on your path, what you have read and what to read next, on every page. It is kept in this browser only; nothing is sent anywhere.</li>
<li><b>Every term explained where it appears.</b> The first use of each specialist word on a page is underlined; hover or tap it for a one-line definition, or follow it to <a href="../glossary/index.html">the glossary</a>. Every CVE number links to what it is.</li>
<li><b>A plain-English line at the top of every technical page</b>, so a reader who lands on the code or the inventory knows in one sentence what it is and whether they need it.</li>
<li><b>The same evidence for everyone.</b> No briefing adds a claim. Each selects and orders the same rows, with the same status words and sources, so two readers can disagree about what to do and not about what happened.</li>
</ul>""")}
{section("readers", "The readers, one by one", f'<div class="pcards">{cards}</div>')}
{section("why", "Why name readers at all", "<p>The first version of this site opened with a sentence that was accurate and unreadable to most of the people who arrived on it: two CVE numbers, a nickname, and the words unauthenticated remote code execution. Accuracy is necessary and not sufficient. A board member who cannot tell what a CVE is will repeat the headline instead; a website owner who does not know the fix is in PHP rather than in WordPress will update the wrong thing. The readers on this page are the editor's working list, and the list will change as readers write in.</p>")}
'''
    page('start/index.html', 'Who is reading? The readers of this site, mapped', f'{len(PERSONAS)} kinds of reader, from someone who has never heard of PHP to the people who maintain it, mapped by what they need to do and how technical they want it, each with a thirty-second answer and a reading path.', body, kind='free', topics='php2shell readers personas')

def build_explained():
    srcs = lambda *x: f'<span class="refs">{src_links(list(x), 1)}</span>'
    body = f'''
<p class="kicker">Start here &middot; {depth_badge(1)}</p>
<h1>The PHP security flaws, explained from the start</h1>
<p class="lead">No technical background assumed. Seven short answers, in the order people usually ask them, each linking to the page with the evidence. Words in the dotted underline are explained when you hover or tap them.</p>
<nav class="toc"><a href="#php">What is PHP?</a><a href="#what">What went wrong?</a><a href="#nickname">Why php2shell?</a><a href="#cve">What are the numbers?</a><a href="#offline">Why did sites go offline?</a><a href="#hacked">Was anyone hacked?</a><a href="#now">What happens now?</a><a href="#trust">How to read this site</a></nav>
<section id="php"><h2>1. What is PHP, and is it on my computer?</h2>
<p>PHP is a programming language for websites. When you open a page on a site built with it, a program on the website's server, written in PHP, puts the page together (your name, the latest posts, the basket) and sends the result to your browser. WordPress, which runs a very large number of blogs, shops and company sites, is written in PHP; so are Drupal, Joomla, Moodle, Magento and the software behind Wikipedia.</p>
<p><b>PHP runs on servers, not on your phone or laptop.</b> This story is about the organisations that run websites. Visitors are affected only indirectly: if a site they use is broken into, or is taken offline as a precaution.</p>
<div class="flow" role="img" aria-label="A normal visit: your browser asks a web server running PHP for a page; PHP reads the database and files and builds the page.">
<div class="lane"><span class="lane-l">A normal visit</span><div class="fsteps"><div class="fstep">Your browser<small>asks for a page</small></div><span class="farr" aria-hidden="true">&rarr;</span><div class="fstep">The website's server, running PHP<small>builds the page</small></div><span class="farr" aria-hidden="true">&rarr;</span><div class="fstep">Database and files<small>the site's content and settings</small></div></div></div>
</div>
</section>
<section id="what"><h2>2. What went wrong?</h2>
<p>Two bugs were found deep inside PHP itself, not in any one website. Both are in how PHP cleans up after something goes wrong while it is handling a request.</p>
<p>An analogy. Think of PHP as the kitchen behind every page a website serves. When an order is impossible (it needs more than the kitchen is allowed to use), the cook abandons it. The flaws are in how the kitchen abandons and tidies up: in some cases it leaves the counter half cleared, and the next step, or the next order, uses what was left as if it were fresh. A customer who knows this can send an order designed to leave exactly the right things on the counter, so that the kitchen ends up following the customer's instructions instead of the menu.</p>
<div class="flow" role="img" aria-label="The attack: an attacker anywhere, with no password, sends a crafted request; PHP's error handling goes wrong; the attacker's commands run on the server.">
<div class="lane lane-bad"><span class="lane-l">The attack</span><div class="fsteps"><div class="fstep bad">Anyone on the internet<small>no account, no password</small></div><span class="farr" aria-hidden="true">&rarr;</span><div class="fstep bad">A crafted request<small>pushes PHP into its error path</small></div><span class="farr" aria-hidden="true">&rarr;</span><div class="fstep bad">The clean-up goes wrong<small>leftover memory is trusted</small></div><span class="farr" aria-hidden="true">&rarr;</span><div class="fstep bad">The attacker's commands run<small>on the server, as the website</small></div></div></div>
<div class="reach"><div><b>What that can reach</b><ul><li>the website's own code and settings</li><li>passwords stored in those settings, such as the database's</li><li>files the website can read or write</li><li>other systems that trust this server</li></ul></div><div><b>What it does not automatically reach</b><ul><li>systems the server is not allowed to talk to</li><li>passwords that were never on that server</li><li>your own phone or computer</li></ul></div></div>
</div>
<p>In the jargon, this is <i>unauthenticated remote code execution</i>: no login needed, from anywhere, and the attacker's code runs. It is the most serious kind of flaw there is, which is why the response was so loud. The researchers proved it end to end against the most traditional way of running PHP, inside the Apache web server, before any of the website's own code had run. That last point matters: <b>it does not matter how well a website is written</b>; if PHP underneath it is unpatched, it is in scope. {srcs("php-net-advisory", "github-ghsa-w8hw-w9fx-j79w", "github-ghsa-6wmf-4rv5-p3rp")}</p>
<p>The technical version is on <a href="../flaws/index.html">the two flaws</a>, and the code itself on <a href="../code/index.html">the code</a>.</p>
</section>
<section id="nickname"><h2>3. Why is it called php2shell?</h2>
<p>Serious flaws get nicknames so people can talk about them: Heartbleed, Shellshock, Log4Shell. <b>php2shell</b> reads as <i>PHP to shell</i>. A shell is the command line an administrator types into; getting a shell on a server means being able to run commands on it. So the name is the whole attack in one word: start with a PHP website, end with a command line on its server. The US NSA wrote it PHP2Shell. {srcs("nsa-x-2112903220209098897", "calif-php2shell")}</p>
</section>
<section id="cve"><h2>4. What are CVE-2026-109618 and CVE-2026-109619?</h2>
<p>They are the official names. A CVE number is a serial number for a security flaw, so that vendors, governments and journalists know they mean the same bug: CVE, the year the number was reserved, and a sequence number. Each has a public record saying what is affected and how bad it is.</p>
<div class="cols2"><div class="col"><h3>CVE-2026-109618</h3><p>PHP running out of memory mid-request can leave memory half set up, and the clean-up that follows can be steered by an attacker. Severity 9.2 out of 10.</p></div><div class="col"><h3>CVE-2026-109619</h3><p>Leftover settings from one visitor's request can point at memory that has been released, and the next request on the same worker uses it. Severity 9.2 out of 10.</p></div></div>
<p>Both are fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October 2026. Older versions (8.1 and before) are past their support date and got no ready-made fix. {srcs("cve-cve-2026-109618", "cve-cve-2026-109619", "php-net-advisory")}</p>
</section>
<section id="offline"><h2>5. Why did governments tell people to take websites offline?</h2>
<p>Because an unpatched website with this flaw can be taken over by anyone, and updating every server takes time. The US NSA and CISA said: if you cannot update, take the system offline until you can. The UK's NCSC put that fourth on its list, after updating and temporary fixes; several European agencies said isolate it; others did not mention it at all. Dutch government services, including the DigiD login many Dutch citizens use, were taken offline as a precaution. {srcs("nsa-x-2112903220209098897", "cisa-alert-php-20261021", "ncsc-news-php", "rijksoverheid-ncsc-php-news")}</p>
<p>Taking a site offline is a decision an organisation makes, not evidence it was attacked. The <a href="../agencies/index.html">agencies page</a> sets the sixteen sets of advice side by side.</p>
</section>
<section id="hacked"><h2>6. Was anyone actually hacked?</h2>
<p>Not that anyone has confirmed, as of the latest evidence this site holds. Attackers have certainly been trying: Cloudflare says it saw millions of attempts across its network, and Amazon says a decoy server was hit four days before the fix was public. But an attempt is not a success, no named organisation has said it was broken into, and the US list of flaws known to be exploited did not include either of these when last checked. That can change quickly, and this site will say so when the evidence does. {srcs("x-eastdakota-php2shell-stats", "thehackernews-php2shell-4days", "cisa-kev-json")}</p>
<p>The details: <a href="../impact/index.html">who went offline and who was compromised</a>, and <a href="../exploitation/index.html">every sign of exploitation, in order</a>.</p>
</section>
<section id="now"><h2>7. What happens now?</h2>
<ul class="howlist">
<li><b>If you only use websites:</b> nothing to do. Ignore messages that tell you to install anything because of this; that is a scam pattern.</li>
<li><b>If you own a website:</b> ask whoever hosts it whether PHP has been updated and restarted. <a href="../briefings/site-owner/index.html">The website owner's briefing</a> has the exact question to send.</li>
<li><b>If you run systems:</b> update, restart, verify, and look for signs of compromise. <a href="../playbook/index.html">The step-by-step list</a> has every agency's advice in order.</li>
<li><b>If you decide or communicate:</b> <a href="../start/index.html">pick your briefing</a>.</li>
</ul>
</section>
<section id="trust"><h2>How to read this site</h2>
<p>Every statement on this site carries one of five words, so you can tell a fact from a rumour at a glance:</p>
{status_legend()}
<p>Every one of those statements links to the pages it comes from, and every one of those pages was saved, dated and fingerprinted when it was read, so that it can be checked later even if the original changes. <a href="../method/index.html">How that works</a>.</p>
</section>
'''
    page('explained/index.html', 'The PHP security flaws, explained from the start', 'No technical background assumed: what PHP is, what went wrong, why it is called php2shell, what the CVE numbers mean, why websites went offline, whether anyone was hacked, and what to do now.', body, kind='free', topics='php2shell explainer plain english')

def build_glossary():
    terms = sorted(TERMS, key=lambda t: t['term'].lower())
    letters = OrderedDict()
    for t in terms:
        letters.setdefault(t['term'][0].upper(), []).append(t)
    jump = ''.join(f'<a href="#l-{E(L)}">{E(L)}</a>' for L in letters)
    out = ''
    for L, ts in letters.items():
        items = ''
        for t in ts:
            ext = f' &middot; <a href="{E(t["ext"])}" rel="noopener">the authority &#8599;</a>' if t.get('ext') else ''
            items += f'<article class="gterm" id="{E(t["id"])}"><h3>{E(t["term"])}</h3><p class="gshort">{E(t["short"])}</p><p>{E(t["long"])}</p><p class="small"><a href="../{E(t["more"])}">Where it matters in this story &rarr;</a>{ext}</p></article>'
        out += f'<section id="l-{E(L)}" class="gletter"><h2>{E(L)}</h2>{items}</section>'
    body = f'''
<p class="kicker">Start here &middot; {depth_badge(1)}</p>
<h1>Glossary: every term, in plain English</h1>
<p class="lead">{len(TERMS)} words this story cannot avoid, each explained for someone who has never worked in security, and each in the sense it has in this story. On every other page, the first use of each of these words is underlined and links here.</p>
<nav class="toc jump">{jump}</nav>
{out}
'''
    page('glossary/index.html', 'Glossary: every php2shell term in plain English', f'{len(TERMS)} terms from the php2shell story (PHP, CVE, CVSS, remote code execution, WAF, KEV and more), each explained in plain English, in the sense it has in this story.', body, kind='free', topics='php2shell glossary')

def build_personas_js():
    data = {'depths': {k: v['label'] for k, v in DEPTHS.items()}, 'personas': OrderedDict()}
    for p in PERSONAS.values():
        data['personas'][p['id']] = {'person': p['person'], 'label': p['label'], 'group': p['group'], 'depth': p['depth'],
                                     'path': [[x, nav_title(x), minutes(x)] for x in p['path']]}
    write('assets/personas.js', '// Generated by admin/build/build.py from data/personas.json: the readers, their paths and reading times.\nwindow.P2S = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')


if __name__ == '__main__':
    main()
