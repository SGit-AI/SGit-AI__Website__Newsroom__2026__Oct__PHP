#!/usr/bin/env python3
"""Build php.oct-2026.story.sgit.ai from data/ into the repository root.

Deterministic: the same data/ and VERSION produce byte-identical output. There is no clock in
this file. Every page gets a markdown twin at the same path, and llms.txt lists every page.
Run: python3 admin/build/build.py        (from the repository root or anywhere)
"""
import html, json, math, os, re, sys
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
                          'personas', 'glossary', 'plain', 'interview', 'seo',
                          'admin', 'telemetry', 'review', 'layers', 'questions', 'readings', 'patching', 'pipeline', 'vaults', 'source-watch', 'feed-sources', 'inventory-history', 'signals', 'subscriptions', 'compromise', 'stack')}
TREP = load('telemetry-report') if os.path.exists(os.path.join(DATA, 'telemetry-report.json')) else None
TPUB = load('telemetry-public') if os.path.exists(os.path.join(DATA, 'telemetry-public.json')) else None
WORLD = load('world')
SYN = load('synthetic') if os.path.exists(os.path.join(DATA, 'synthetic.json')) else None
SOURCES = OrderedDict((s['slug'], s) for s in D['sources'])
STORY = D['story']
if D['vault'].get('latest_capture'):
    STORY['data_as_of'] = D['vault']['latest_capture']  # the time of the latest capture in the vault, never a clock

E = html.escape

def J(o, **kw):
    """JSON for inside a <script> element: '<', '>' and '&' as \\u escapes, so no string in the data can close the element."""
    return json.dumps(o, **kw).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')

def U(u, fallback='#'):
    """An href from data, escaped. Only http(s), mailto and scheme-less (relative or fragment) URLs pass; javascript:, data: and the rest become the fallback."""
    u = str(u or '').strip()
    if re.match(r'(https?://|mailto:)', u, re.I) or (u and ':' not in re.split(r'[/?#]', u, maxsplit=1)[0]):
        return E(u)
    return E(fallback)

ARTICLES_DIR = os.path.join(ROOT, 'admin', 'content', 'articles')

def load_articles():
    """Every article in admin/content/articles/: a front matter block of key: value lines, then markdown. Newest first."""
    out = []
    for fn in sorted(os.listdir(ARTICLES_DIR)) if os.path.isdir(ARTICLES_DIR) else []:
        if not fn.endswith('.md'):
            continue
        text = open(os.path.join(ARTICLES_DIR, fn), encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, flags=re.S)
        if not m:
            sys.exit(f'article {fn}: no front matter')
        meta = dict(re.match(r'^(\w+):\s*(.*)$', l).groups() for l in m.group(1).splitlines() if l.strip())
        meta['file'], meta['text'] = fn, m.group(2)
        meta['cites'] = list(OrderedDict.fromkeys(x.strip() for g in re.findall(r'\[\[([^\]]+)\]\]', meta['text']) for x in g.split(',')))
        out.append(meta)
    return sorted(out, key=lambda a: (a['written'], a['file']), reverse=True)

ARTICLES = load_articles()

# The two halves of the site, and what each page is. Research: material collected from outside and what this
# site derives from it. Stories: written here, signed and dated. Every page carries one of these at its top.
ZONES = OrderedDict([('Start here', 'For you'), ('Questions', 'For you'), ('Briefings', 'For you'), ('Yours', 'For you'), ('The incident', 'Research'),
                     ('The analysis', 'Research'), ('The evidence', 'Research'), ('GRC', 'Research'), ('Stories', 'Stories'), ('About', 'Site')])
ORIGINS = {
    'house': {'short': 'House', 'label': 'Story', 'text': 'written here by this site, signed and dated'},
    'guest': {'short': 'Guest', 'label': 'Story, guest', 'text': 'written by a guest writer, published here under their name'},
    'interview': {'short': 'Interview', 'label': 'Story, interview', 'text': 'an interview conducted for this site, the answers in the interviewee\'s own words'},
}
AUTHOR_ROLES = OrderedDict([('journalist', 'Journalist'), ('historian', 'Historian'), ('journalist-historian', 'Journalist and historian'), ('cyber', 'Cyber desk')])

# ----------------------------------------------------------------------------- small helpers

STATUS_WORDS = OrderedDict([
    ('confirmed', 'two or more primary sources agree, or the fact was counted from a captured file'),
    ('reported', 'one party says so, and it has not been contradicted'),
    ('disputed', 'the sources disagree, and both readings are shown'),
    ('contradicted', 'a primary source says otherwise'),
    ('unverified', 'even the reporting outlet could not check it'),
])

def pill(status):
    w = re.match(r'[a-z]*', (status or '').lower()).group(0)  # the leading word, without the ';' or ':' that may follow it
    cls = w if w in STATUS_WORDS else 'other'
    m = re.match(r'^(\w+)([;:,]?\s+[(;:]?.*)$', status or '') if cls != 'other' else None
    if m and len(status) > 24:  # a status word with a qualifier: the word is the pill, the qualifier wraps beside it
        return f'<span class="st st-{cls}">{E(m.group(1))}</span> <span class="small">{E(m.group(2).strip(" ;:,"))}</span>'
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
    ('Questions', [('questions/index.html', 'Questions readers ask')] + [(f'questions/{q["id"]}/index.html', q['q']) for q in D['questions']['questions']]),
    ('Briefings', [(f'briefings/{a["id"]}/index.html', a['name']) for a in D['roles']['audiences']]),
    ('Yours', [('collaborators/index.html', 'Power users: start here'), ('join/index.html', 'Join: a key for feedback'), ('feedback/index.html', 'Feedback from collaborators'), ('join/invite/index.html', 'Invite someone'), ('now/index.html', 'Now: the phone app'), ('you/index.html', 'Your desk: new, changed, notes'), ('stack/index.html', 'Your stack: the blast radius'), ('reader/index.html', 'The feed viewer'), ('feeds/index.html', 'Feeds (RSS)'), ('subscribe/index.html', 'Subscribe by email')]),
    ('The incident', [('index.html', 'Front page'), ('whatsnew/index.html', "What's new"), ('summary/index.html', 'The specialist summary'), ('flaws/index.html', 'The two flaws'), ('code/index.html', 'The code'), ('timeline/index.html', 'Timeline'),
                   ('discovery/index.html', 'Who found it'), ('leak/index.html', 'How disclosure broke'),
                   ('exploitation/index.html', 'Exploitation signals'), ('compromise/index.html', 'No named compromise: the evidence'), ('review/index.html', 'The fix, mapped to the code'), ('review/ui/index.html', 'Walk the graph'), ('impact/index.html', 'Impact: offline vs compromised'),
                   ('defence/index.html', 'Detection and defence'), ('context/index.html', 'In context: 2008 to 2026'), ('playbook/index.html', 'If you run PHP'), ('patching/index.html', 'Patching: who gets a fix'), ('patching/inventory/index.html', 'The inventory, hour by hour'), ('signals/index.html', 'The second stories: signals')]),
    ('The analysis', [('claims/index.html', 'Every claim'), ('factcheck/index.html', 'Fact-check: how sure we are'), ('numbers/index.html', 'The numbers'), ('agencies/index.html', 'The agencies'),
                      ('affected/index.html', 'Affected systems'), ('actors/index.html', 'Who says what'), ('graph/index.html', 'As a graph'),
                      ('readings/index.html', 'From outside: other models and sites')] + [(f'readings/{r["id"]}/index.html', f'{r["model"]}\'s notes, in full') for r in D['readings']['readings']]),
    ('The evidence', [('sources/index.html', 'Every source'), ('affected/software.html', 'Software inventory'), ('admin/vault/index.html', 'The vault, opened'),
                      ('layers/index.html', 'Evidence, derived, authored'),
                      ('pipeline/index.html', 'The fact pipeline'), ('versions/index.html', 'How the story changed'),
                      ('vaults/index.html', 'Every vault behind this site')] + [(x['page'], x['name']) for x in D['vaults']['vaults']]),
    ('GRC', [('grc/index.html', 'GRC: risks, owners, standards'), ('grc/risks/index.html', 'The risk register'), ('grc/stakeholders/index.html', 'Stakeholders and their registers'),
             ('grc/frameworks/index.html', 'Frameworks: GDPR, NIS2, CRA, ISO, NIST'), ('grc/graph/index.html', 'The risk graph'), ('grc/network/index.html', 'From the sgit network')]),
    ('Stories', [('articles/index.html', 'All stories, written here')] + [(f'articles/{a["slug"]}/index.html', f'{ORIGINS[a["origin"]]["short"]} · {AUTHOR_ROLES.get(a["role"], a["role"])}: {a["title"].split(":")[0].split("?")[0]}') for a in ARTICLES] + [('interview/index.html', 'Interview: the editor')]),
    ('About', [('method/index.html', 'The method'), ('admin/design/index.html', 'Design: the redesign, in mockups'), ('team/index.html', 'The team'), ('billing/index.html', 'The billing model'),
               ('account/index.html', 'Your reading account'), ('brief/index.html', 'The brief'),
               ('corrections/index.html', 'Corrections'), ('admin/versions.html', 'Release history'), ('status/index.html', 'Pipeline: what is deploying'), ('admin/index.html', 'Admin & engineering'), ('admin/agents/index.html', 'Guidance for agents'),
               ('admin/status-json/index.html', 'status.json: the feed for other sites'), ('admin/board/index.html', 'The board'), ('admin/roles/index.html', 'Roles'),] + ([('admin/keys/index.html', 'Keys and secrets')] if os.path.exists(os.path.join(DATA, 'keys.json')) else []) + [ ('admin/briefs/index.html', 'Briefs'), ('admin/telemetry/index.html', 'Who reads this site'), ('admin/synthetic/index.html', 'Synthetic readers')]),
]

PAGES = []  # (path, title, description) in order, for llms.txt

# Pricing (data/billing.json, pricing): a page's kind is its content type; a type that decays gets its freshness tier
# appended in the reader's browser, from the page's date, before the meter reads it. The build stays clock-free.
PRICE_TYPES = {t['type']: t for t in D['billing']['pricing']['types']}
_tiers = D['billing']['pricing']['tiers']
FRESHNESS_JS = ('<script>(function(m){var a=(Date.now()-Date.parse(m.getAttribute("date")))/864e5;m.setAttribute("kind",m.getAttribute("kind")+"_"+('
                + ''.join(f'a<={t["max_days"]}?"{t["tier"]}":' for t in _tiers if t['max_days'] is not None)
                + f'"{_tiers[-1]["tier"]}"))}})(document.currentScript.previousElementSibling)</script>')

def layout(path, title, description, body, kind='site', date=None, topics='', ld_type='Article', origin=None, byline=None):
    depth = path.count('/')
    up = '../' * depth
    PAGES.append((path, title, description, kind))
    here = path
    nav_items, zone = [], None
    for label, items in NAV:
        if ZONES.get(label, '') != zone:
            zone = ZONES.get(label, '')
            if zone:
                nav_items.append(f'<span class="zone zone-{zone.split()[0].lower()}">{E(zone)}</span>')
        active = any(p == here for p, _ in items)
        subs = ''.join(f'<a class="sl{" here" if p == here else ""}" href="{up}{p}">{E(t)}</a>' for p, t in items)
        nav_items.append(f'<div class="ni"><a class="nl{" here" if active else ""}" href="{up}{items[0][0]}">{E(label)}<span class="caret">&#9662;</span></a><div class="sub">{subs}</div></div>')
    cfg = D['billing']['runs']
    meter_cfg = {
        'storageKey': cfg['storageKey'], 'start': cfg['start'], 'symbol': cfg['symbol'],
        'prices': cfg['prices'],
        'newDays': cfg['newDays'], 'minDepth': cfg['minDepth'], 'topup': cfg['topup'],
        'links': {'account': 'account/index.html', 'topup': 'account/top-up.html'},
        'links2': {'newsroom': 'account/index.html', 'personas': 'account/index.html'},
        'root': up,
    }
    meter_json = J(meter_cfg, sort_keys=True, separators=(',', ':'))
    page_meter = '' if PRICE_TYPES[kind]['base'] == 0 else f'<sg-meter view="page" quiet kind="{E(kind)}" date="{E(date or STORY["data_as_of"][:10])}" topics="{E(topics)}" title="{E(title)}"></sg-meter>' + (FRESHNESS_JS if PRICE_TYPES[kind]['decays'] else '')
    ld = {
        '@context': 'https://schema.org', '@type': ld_type, 'headline': title, 'description': description,
        'url': f'{BASE_URL}/{path}', 'isPartOf': {'@type': 'WebSite', 'name': SITE_NAME, 'url': BASE_URL},
        'license': 'https://creativecommons.org/licenses/by/4.0/', 'dateModified': STORY['data_as_of'][:10],
        'version': VERSION, 'inLanguage': 'en', 'image': f'{BASE_URL}/{SEO.get("image", "assets/og-card.png")}',
        'datePublished': SEO.get('date_published', '2026-10-22'), 'mainEntityOfPage': f'{BASE_URL}/{path}',
        'author': {'@type': 'Person', 'name': SEO.get('author', 'Dinis Cruz')},
        'publisher': {'@type': 'Organization', 'name': SEO.get('publisher', 'SGit Newsroom'), 'url': SEO.get('publisher_url', 'https://newsroom.sgit.ai/')},
    }
    verify = f'\n<meta name="google-site-verification" content="{E(SEO["google_site_verification"])}">' if SEO.get('google_site_verification') else ''
    crumbs = [{'@type': 'ListItem', 'position': 1, 'name': SITE_NAME, 'item': f'{BASE_URL}/index.html'}]
    for label, items in NAV:
        if any(p == path for p, _ in items) and path != 'index.html':
            crumbs.append({'@type': 'ListItem', 'position': 2, 'name': label, 'item': f'{BASE_URL}/{items[0][0]}'})
            break
    if path != 'index.html':
        crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1, 'name': title, 'item': f'{BASE_URL}/{path}'})
    ld = [ld, {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': crumbs}]
    if path == 'index.html':
        ld.append({'@context': 'https://schema.org', '@type': 'WebSite', 'name': SITE_NAME, 'url': BASE_URL + '/', 'description': STORY['description'], 'inLanguage': 'en'})
    return f'''<!doctype html>
<html lang="en" data-root="{up}" data-path="{path}" data-ver="{VERSION}">
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
<meta name="twitter:card" content="summary_large_image">
<meta property="og:image" content="{BASE_URL}/{SEO.get('image', 'assets/og-card.png')}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="author" content="{E(SEO.get('author', ''))}">{verify}
<link rel="alternate" type="application/atom+xml" title="{SITE_NAME}: what's new" href="{up}feed.xml">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<link rel="icon" href="data:,">
<link rel="alternate" type="text/markdown" href="{up}{md_path(path)}">
{feed_links(path)}
<link rel="stylesheet" href="{up}assets/site.css">
<link rel="stylesheet" href="{up}assets/themes/themes.css">
<link rel="stylesheet" href="{up}assets/themes/site-tokens.css">
<script type="application/ld+json">{J(ld, ensure_ascii=False)}</script>
<script type="application/json" id="sg-meter-config">{meter_json}</script>
<script type="module" src="{up}assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js"></script>
<script src="{up}assets/personas.js" defer></script>
<script src="{up}assets/site.js" defer></script>
<script src="{up}assets/reader-state.js" defer></script>
<script src="{up}assets/site-tools.js" defer></script>
<script src="{up}assets/telemetry.js" defer></script>
</head>
<body>
<nav class="site"><div class="row">
  <script src="{up}assets/themes/themes.js"></script>
  <a class="brand" href="{up}index.html">PHP October<span> 2026</span></a>
  <a class="ver" href="{up}admin/versions.html#v{E(VERSION)}" title="Site release history: what v{E(VERSION)} changed">v{E(VERSION)}</a>
  <span class="status">{E(STORY["status"])} &middot; last checked {E(human_time(STORY["data_as_of"]))}</span>
  <span class="crumbs"><a href="https://newsroom.sgit.ai/">newsroom</a> / <a href="https://2026.newsroom.sgit.ai/">2026</a> / <a href="https://oct.2026.newsroom.sgit.ai/">October</a> / <b>PHP</b></span>
  <div class="tools"><div class="theme-pick"></div><sg-meter view="balance"></sg-meter></div>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-items" aria-label="Menu">Menu</button>
  <div class="nav-items" id="nav-items">{''.join(nav_items)}</div>
</div></nav>
<main>
{origin_strip(path, kind, origin, byline)[0]}
{body}
{page_meter}
</main>
<footer class="site">
  <div class="row">
    <p><b>{SITE_NAME}</b> ({SITE}) tracks PHP news for one month. This month that is one story, the two critical PHP security flaws, followed as evidence: every claim with a status and its sources, every source captured, dated and hashed into a private vault. Built and run by one editor and a team of software agents; <a href="{up}team/index.html">the roles</a> and <a href="{up}method/index.html">the method</a> are public, and the site is rebuilt from the vault, never written by hand. One of the SGit Newsroom's story sites: up from here are <a href="https://oct.2026.newsroom.sgit.ai/">October 2026</a>, <a href="https://2026.newsroom.sgit.ai/">the year</a> and <a href="https://newsroom.sgit.ai/">the newsroom</a>, whose own section on the story is <a href="{NEWSROOM}">here</a>. Part of the <a href="https://sgit.ai/network/index.html">sgit.ai network</a>.</p>
    <p class="disc">&#9888; Participant disclosure: published by the sgit project, which builds the vault and metering stack this site runs on. Content CC BY 4.0 for this site's own text, tables and data; quoted words are their authors', linked; no third-party page is reproduced. Code Apache-2.0.</p>
    <p class="small">&#9673; This page sends one anonymous usage event (page, referrer host, country and region, no IP, no cookie) to a write-only vault lane; <a href="{up}admin/telemetry/index.html">what is sent and what is counted</a>. Honoured: Do Not Track and Global Privacy Control.</p>
    <p class="small">site v{E(VERSION)} &middot; evidence vault commit {E(D["vault"]["head"]["commit"] or "unknown")} &middot; <a href="{up}admin/index.html">engineering</a> &middot; <a href="{up}{md_path(path)}">this page as markdown</a> &middot; <a href="{up}llms.txt">llms.txt</a> &middot; <a href="{REPO_URL}">GitHub</a></p>
  </div>
</footer>
</body>
</html>
'''

def origin_strip(path, kind, origin=None, byline=None):
    """What this page is: research, external material, a story (house, guest, interview) or about the site. (html, markdown line)"""
    up = '../' * path.count('/')
    if origin in ORIGINS:
        o = ORIGINS[origin]; cls, label, text = 'story', o['label'], o['text'] + (f'. {byline}' if byline else '')
    elif origin == 'external' or path.startswith('readings/') and path != 'readings/index.html':
        cls, label, text = 'external', 'Research, external', 'material from outside, published as received and credited; not written here'
    elif kind in ('site', 'account') or path.startswith(('admin/', 'account/')):
        cls, label, text = 'site', 'About this site', 'how the site works, kept by the agents that run it'
    else:
        cls, label, text = 'research', 'Research', 'collected from outside sources and what this site derives from them; every fact links to a saved copy of its source'
    html_line = f'<p class="origin o-{cls}"><b>{E(label)}</b> <span>{E(text)}</span> <a href="{up}layers/index.html">Research or story?</a></p>'
    return html_line, f'{label}: {text}.'

def md_path(path):
    return re.sub(r'\.html$', '.md', path)

OUTPUTS = set()  # every file this build writes; admin/build/outputs.txt, read by release.sh to resolve merges

def write(path, content):
    full = os.path.realpath(os.path.join(ROOT, path))
    if not full.startswith(os.path.realpath(ROOT) + os.sep) or any(p.startswith('.') for p in os.path.relpath(full, os.path.realpath(ROOT)).split(os.sep)):
        raise SystemExit(f'build: refusing to write outside the site tree: {path!r}')
    OUTPUTS.add(path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

def page(path, title, description, body, **kw):
    plain = D['plain']['pages'].get(path)
    if plain:
        body = body.replace('</h1>', f'</h1>\n<aside class="plainbox"><b>In plain English</b> {E(plain)}</aside>', 1)
    WORDS[path] = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<(svg|script|table).*?</\1>', ' ', body, flags=re.S)).split())
    md_text = f'# {title}\n\n{description}\n\n' + to_markdown(body)
    sec = ledger_for_page(path, md_text)
    hbody = body
    if sec:
        badge = vbadge(section_id(path), path.count('/'), 'This briefing' if path.startswith('briefings/') else 'This page')
        hbody = body.replace('</h1>', '</h1>\n' + badge, 1)
    html_out = layout(path, title, description, gloss(hbody, path), **kw)
    write(path, html_out)
    md_text = md_text.replace('\n\n', '\n\n> ' + origin_strip(path, kw.get('kind', 'site'), kw.get('origin'), kw.get('byline'))[1] + '\n\n', 1)
    write(md_path(path), md_text + f'\n\n---\nsite v{VERSION} · data as of {STORY["data_as_of"]} · vault commit {D["vault"]["head"]["commit"]} · {BASE_URL}/{path}\n')

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
        rows.append([f'{it_ledger("fact-" + c["id"])}<span id="{E(c["id"])}">{E(c["claim"])}</span>{note} <a class="flink" href="{"../" * depth}facts/{E(c["id"])}/index.html">fact timeline &rarr;</a>', E(c['by']), pill(c['status']), assure(c['id']), wt, src_links(c['sources'], depth)])
    return table(['Claim', 'Who says it', 'Status', f'<a href="{"../" * depth}factcheck/index.html">Fact-check</a>', 'Primary', 'Sources'], rows, 'claims')

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
        ('warn', 'Does it reach you?', 'Check your stack', 'describe what you run and see what an attacker could reach in it', 'stack/index.html'),
        ('warn', 'Are attackers trying?', 'Yes', 'millions of attempts, seen by one internet security company', 'exploitation/index.html'),
        ('info', 'Anyone confirmed hacked?', 'Not yet', 'no organisation, as of the latest check', 'impact/index.html'),
        ('warn', 'Websites taken offline', f'{len(im["offline"])} organisations', 'reported, as a precaution', 'impact/index.html'),
        ('info', "On the US 'used in attacks' list?", 'Not yet', "the US government's official list of flaws known to be used by attackers", 'exploitation/index.html#kev'),
        ('bad', 'What do governments say?', 'Update now', f'or take the website offline if you cannot; {C["agencies"]} agencies compared', 'agencies/index.html'),
    ]
    board = ''.join(f'<a class="tile tile-{t}" href="{h}"><span class="tl">{E(l)}</span><b>{E(v)}</b><span class="tn">{E(n)}</span></a>' for t, l, v, n, h in tiles)
    now = ''.join(f'<li>{E(x["text"])} <span class="refs">{src_links(x["sources"], 0)}</span></li>' for x in pl['now'])
    facts = ''.join(f'<li><span class="fs">{pill(f["status"])}</span><div><p>{E(f["text"])}</p><p class="ff"><span class="refs">{src_links(f["sources"], 0)}</span> <a href="{U(f["href"])}">More &rarr;</a></p></div></li>' for f in pl['facts'])
    unknown = ''.join(f'<li><a href="{U(u["href"])}">{E(u["text"])}</a></li>' for u in pl['unknown'])
    latest = ''.join(f'<li><span class="when">{E(x["when"])}</span><span>{E(x["text"])} <span class="refs">{src_links(x["sources"], 0)}</span></span></li>' for x in pl['latest'])
    moments = ''.join(f'<li class="m m-{E(m["tone"])}"><a href="{E(m["href"])}"><span class="mw">{E(m["when"])}</span><span class="mt">{E(m["what"])}</span></a><span class="refs">{src_links(m["sources"], 0)}</span></li>' for m in pl['moments'])
    legend = ''.join(f'<li>{pill(k)} {E(v)}</li>' for k, v in [('confirmed', 'two or more original sources agree'), ('reported', 'one party says so; nobody has contradicted it'), ('disputed', 'sources disagree'), ('unverified', 'nobody has been able to check it')])
    evidence = ''.join([
        stat(C['sources'], 'web pages saved as evidence, each with the time it was saved', 'sources/index.html'),
        stat(C['claims'], f'statements checked: {C["by_status"]["confirmed"]} confirmed, {C["by_status"]["disputed"] + C["by_status"]["contradicted"]} disputed, {C["by_status"]["unverified"]} unverified', 'claims/index.html'),
        stat(C['events'], 'dated events, from 2024 to today', 'timeline/index.html'),
        stat(C['agencies'], "government agencies' advice compared", 'agencies/index.html'),
    ])
    def fsec(sid, title, text):
        ledger('front-' + sid, 'Front page: ' + title, 'front', 'index.html', text, scope='front')
        return vbadge('front-' + sid, 0, 'This section')
    b_now = fsec('now', 'right now', '\n'.join(f'{x["text"]} [{", ".join(x["sources"])}]' for x in pl['now']))
    b_glance = fsec('glance', 'at a glance', '\n'.join(f'{l}: {v} ({n})' for t, l, v, n, h in tiles))
    b_facts = fsec('facts', 'the core facts', '\n'.join(f'{f["status"]}: {f["text"]} [{", ".join(f["sources"])}]' for f in pl['facts']))
    b_unknown = fsec('unknown', 'what nobody knows yet', '\n'.join(u['text'] for u in pl['unknown']))
    b_latest = fsec('latest', 'latest', '\n'.join(f'{x["when"]}: {x["text"]} [{", ".join(x["sources"])}]' for x in pl['latest']))
    who_lead = f'The same evidence, put in order for {len(PERSONAS)} kinds of reader. Each starts with a thirty-second answer in plain words. <a href="start/index.html">How the readers are mapped</a>.'
    body = f'''
<header class="hero hero2">
  <p class="kicker">PHP news &middot; October 2026 &middot; <span class="live">{E(s["status"])}</span> &middot; last checked {E(when)}</p>
  <h1>{E(pl["headline"])}</h1>
  <p class="deck">{E(pl["deck"])}</p>
  <div class="ctas"><a class="cta cta-pri" href="#now">What is happening now</a><a class="cta" href="#who">The briefing for you</a><a class="cta" href="explained/index.html">Explain it from the start</a><a class="cta" href="stack/index.html">Check your stack</a><a class="cta" href="now/index.html">On your phone: Now &rarr;</a></div>
  <p class="aka">{E(pl["aka"])}</p>
</header>
<section id="now"><h2>Right now</h2><p class="small">As of {E(when)}, the time of the latest page this site saved.</p><ul class="nowlist">{now}</ul>{b_now}</section>
{section("state", "At a glance", f'<div class="tiles">{board}</div>{b_glance}')}
{section("facts", "The core facts, and the evidence for each", f'<ul class="legend">{legend}</ul><ol class="facts">{facts}</ol>{b_facts}', "Each fact links to the original pages it rests on: the PHP project, government agencies, the researchers. Click a source to see when it was saved and its fingerprint.")}
{section("unknown", "What nobody knows yet", f'<ul class="unknown">{unknown}</ul>{b_unknown}', "Stated, not papered over. This site will update each one when the evidence does.")}
{section("latest", "Latest", f'<ol class="latest">{latest}</ol><p><a href="timeline/index.html">Everything, in order, on the timeline &rarr;</a> &middot; <a href="whatsnew/index.html">What changed on this site, release by release &rarr;</a></p>{b_latest}')}
{section("who", "The briefing for you", item('home-who', 'front', 'for-you', 'The briefing for you: fifteen readers', 'index.html#who', re.sub(r'\d+', '#', persona_doors()), REL_DATE.get(VERSION, '')) + persona_doors(), who_lead)}
{section("moments", "How it unfolded", item('home-moments', 'front', 'research', 'How it unfolded: five moments', 'index.html#moments', moments, REL_DATE.get(VERSION, '')) + f'<ol class="moments">{moments}</ol>')}
{section("stories", "Stories: written here", item('home-stories', 'front', 'stories', 'Stories: written here', 'index.html#stories', re.sub(r'\d+', '#', stories_row()), REL_DATE.get(VERSION, '')) + stories_row(), "Everything above is research: collected from outside sources, each fact linked to a saved copy. These are written here, signed and dated, and kept as written.")}
{section("evidence", "How this site knows", item('home-how', 'front', 'site', 'How this site knows', 'index.html#evidence', 'how this site knows: saved, fingerprinted, agents for one editor', REL_DATE.get(VERSION, '')) + f'<div class="stats">{evidence}</div><p>Every page this site relies on was saved at the moment it was read, with a fingerprint that proves it has not been altered since, so a fact can be checked even if the original page changes or disappears. Nothing here is advice for your own systems; for that, read <a href="https://www.php.net/archive/2026.php#2026-10-21-5" rel="noopener">the PHP project\'s announcement</a> and your national cyber agency. The site is put together by software agents working for one editor, Dinis Cruz; <a href="method/index.html">how it works</a>.</p><p>Already know the vocabulary? <a href="summary/index.html">The specialist summary</a> has the technical version of this page, with every number and the full last 48 hours.</p>')}
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
        rows = [[f'{it_event(t)}<span class="when">{E(fmt_at(t["at"]))}</span>', E(t['event']) + (f'<div class="note">{E(t["note"])}</div>' if t.get('note') else ''), pill(t['confidence']), src_links(t['sources'], 1)] for t in evs if t.get('phase') == ph]
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

KIND_INK = {'attempts': 'var(--warm)', 'vendor-exploitation': 'var(--bad-ink)', 'no-success-known': 'var(--ok-ink)',
            'named-organisation': 'var(--accent)', 'allegation': 'var(--dim)', 'official-signal': 'var(--accent-dk)'}

def build_compromise():
    """One statement and the evidence behind it, row by row, with what each kind of evidence can and cannot show.
    Drawn from data/compromise.json; maps evidence, makes no assessment of risk."""
    C = D['compromise']; rows, kinds = C['rows'], C['kinds']
    kname = {k['id']: k['name'] for k in kinds}
    def where(r):
        out = src_links(r['sources'], 1) if r.get('sources') else ''
        if r.get('watch'):
            out += f' <span class="note">source watch: <code>{E(r["watch"])}</code></span>'
        return out
    # 1. the evidence by kind, as bars
    counts = [(k, sum(1 for r in rows if r['kind'] == k['id'])) for k in kinds]
    mx = max(n for _, n in counts) or 1; W, bh = 640, 26
    bars = ''.join(f'<text x="0" y="{i*bh+17}" style="font-size:12px;fill:var(--fg)">{E(k["name"])}</text>'
                   f'<rect x="280" y="{i*bh+5}" width="{int(320*n/mx)}" height="16" rx="3" style="fill:{KIND_INK[k["id"]]}"/>'
                   f'<text x="{288+int(320*n/mx)}" y="{i*bh+18}" style="font-size:12px;font-weight:700;fill:var(--fg)">{n}</text>' for i, (k, n) in enumerate(counts))
    chart_kinds = (f'<figure class="graph"><svg viewBox="0 0 {W} {len(counts)*bh+8}" width="100%" role="img" aria-label="Statements on this page by kind">{bars}</svg>'
                   f'<figcaption>{len(rows)} statements on this page, by what kind of evidence they are. A count of statements, not of events: one party can report millions of attempts in one statement.</figcaption></figure>')
    # 2. the timeline, one lane per kind
    import datetime as _dt
    def t(w):
        w = w if 'T' in w else w + 'T12:00Z'
        return _dt.datetime.strptime(w.replace('Z', ''), '%Y-%m-%dT%H:%M')
    t0, t1 = _dt.datetime(2026, 10, 17), _dt.datetime(2026, 10, 23)
    X0, X1, lane = 200, 630, 28
    def x(w): return X0 + (X1 - X0) * (t(w) - t0).total_seconds() / (t1 - t0).total_seconds()
    ticks = ''.join(f'<line x1="{x(f"2026-10-{d}T00:00Z"):.0f}" x2="{x(f"2026-10-{d}T00:00Z"):.0f}" y1="10" y2="{len(kinds)*lane}" style="stroke:var(--line);stroke-width:1"/>'
                    f'<text x="{x(f"2026-10-{d}T00:00Z")+3:.0f}" y="{len(kinds)*lane+18}" style="font-size:10px;fill:var(--dim)">{d} Oct</text>' for d in range(17, 23))
    asof = f'<line x1="{x(C["as_of"]):.0f}" x2="{x(C["as_of"]):.0f}" y1="10" y2="{len(kinds)*lane}" style="stroke:var(--fg);stroke-dasharray:3 3"/><text x="{x(C["as_of"])-4:.0f}" y="8" text-anchor="end" style="font-size:10px;font-weight:700;fill:var(--fg)">as of 22 Oct 20:50</text>'
    lanes = ''.join(f'<text x="0" y="{i*lane+22}" style="font-size:11px;fill:var(--fg)">{E(k["name"])}</text>' for i, k in enumerate(kinds))
    li = {k['id']: i for i, k in enumerate(kinds)}
    dots = ''.join(f'<circle cx="{x(r["when"]):.1f}" cy="{li[r["kind"]]*lane+18}" r="5" style="fill:{KIND_INK[r["kind"]]};fill-opacity:.8"><title>{E(r["when"])} · {E(r["who"])}</title></circle>' for r in rows)
    chart_time = (f'<figure class="graph"><svg viewBox="0 0 640 {len(kinds)*lane+26}" width="100%" role="img" aria-label="The statements over time, one lane per kind">{ticks}{lanes}{dots}{asof}</svg>'
                  f'<figcaption>Each dot is one statement on this page, placed at the time the source gives (noon where it gives only a date). Hover a dot for who said it.</figcaption></figure>')
    # 3. the layers, as an infographic (not to scale)
    L = C['layers']; lh = 52
    shapes = ''.join(f'<rect x="{10+i*25}" y="{i*lh}" width="{620-i*50}" height="{lh-8}" rx="4" style="fill:var(--panel);stroke:{["var(--warm)","var(--bad-ink)","var(--accent)","var(--fg)"][i]};stroke-width:2"/>'
                     f'<text x="320" y="{i*lh+19}" text-anchor="middle" style="font-size:13px;font-weight:700;fill:var(--fg)">{E(l["value"])} · {E(l["label"])}</text>'
                     f'<text x="320" y="{i*lh+35}" text-anchor="middle" style="font-size:10.5px;fill:var(--dim)">{E(l["note"])}</text>' for i, l in enumerate(L))
    chart_layers = (f'<figure class="graph"><svg viewBox="0 0 640 {len(L)*lh}" width="100%" role="img" aria-label="From attempts to a named compromise: what each layer of evidence holds">{shapes}</svg>'
                    f'<figcaption>Not to scale. Each layer is a different kind of statement, and a statement in one layer does not move a case into the next: an attempt is not a compromise, and a vendor\'s report without a victim is not a victim\'s statement. The bottom layer is the statement this page is about.</figcaption></figure>')
    searched = '<div class="stats">' + ''.join(stat(f'{s["count"]:,}', f'{E(s["what"])}: {E(s["unit"])}<br><small>{E(s["detail"])}</small>') for s in C['searched']) + '</div>'
    kind_tables = ''
    for k in kinds:
        rs = [r for r in rows if r['kind'] == k['id']]
        if not rs: continue
        head = ['When', 'Who', 'What they said'] + (['Reading'] if k['id'] == 'named-organisation' else []) + ['Where it is held']
        body_rows = [[E(fmt_at(r['when'])), f'<b>{E(r["who"])}</b>', E(r['says'])] + ([E(r.get('reading', ''))] if k['id'] == 'named-organisation' else []) + [where(r)] for r in sorted(rs, key=lambda r: r['when'])]
        kind_tables += section('k-' + k['id'], f'{E(k["name"])} <small>({len(rs)})</small>', table(head, body_rows),
                               f'This kind of statement can show {E(k["can"])}. It cannot show {E(k["cannot"])}.')
    body = f"""
<h1>{E(C["statement"])}</h1>
<p class="lead">This page holds the evidence behind one statement, as of <b>{E(fmt_at(C["as_of"]))}</b>: every statement found about attacks on, or compromises of, real systems through php2shell, sorted by what kind of evidence it is, with the words of the party that made it and where its capture is held. It makes no assessment of risk. The statement's status is <b>{E(C["status"])}</b>: {E(C["status_note"])} It is <a href="../claims/index.html#{E(C["claim"])}">claim {E(C["claim"])}</a>.</p>
{section("searched", "What was searched", searched, "Where the statement was checked. A statement that something does not exist is only as good as the search behind it.")}
{section("layers", "From attempts to a named compromise", chart_layers)}
{section("kinds", "The evidence, by kind", chart_kinds + chart_time)}
{kind_tables}
{section("change", "What would change the statement", "<ul>" + "".join(f"<li>{E(w)}</li>" for w in C["would_change_it"]) + "</ul><p>The source watch checks the official lists and the named organisations' pages every 30 minutes; this page is rebuilt from data/compromise.json when the evidence changes.</p>")}
{section("ledger", "The disagreements, recorded", "<p>Where sources disagree, the disagreement is a record of its own in the source watch's contradiction ledger, with both statements and their captures: " + ", ".join(f"<code>contradictions/{E(c)}.json</code>" for c in C["contradictions"]) + ".</p>")}
{section("how", "How this page is made", '<p>Every row is in <a href="../data/compromise.json">data/compromise.json</a>. Rows with sources cite captures in the evidence vault, which the build checks. Rows marked <i>source watch</i> cite a dated snapshot folder in the source-watch vault (<a href="../vaults/source-watch/index.html">oq9gflln</a>), read with its published key; they move into the evidence vault as the evidence curator promotes them. Statements read in another language carry the reader&rsquo;s English translation beside the verbatim original in the watch&rsquo;s <code>translations/</code> files. The charts are drawn from the same rows when the site is built.</p>')}
"""
    page('compromise/index.html', 'No named organisation has said it was compromised through php2shell: the evidence', f'The evidence behind one statement, as of {fmt_at(C["as_of"])}: attempts, vendor reports, statements that no success is known, named organisations, allegations and official lists, each with its source.', body, kind='story', topics='php2shell exploitation compromise evidence')

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
<p>To do step 0 and see what steps 1 to 4 mean for your own systems, describe them in <a href="../stack/index.html">your stack</a>: it checks each PHP runtime against both flaws and shows what an attacker who reaches one could touch.</p>
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
        'dpo': dict(topics=['impact', 'exploitation', 'advice', 'technical'], intro='Four questions, in order: is personal data on a system that was exposed, has anything happened to it, does that make it a personal data breach, and what goes on the record. A vulnerability is not a breach, and an outage you chose is not one either; a sign that someone ran code on a system holding personal data is where the assessment starts. Written by the GRC desk; the full register is at <a href="../../grc/index.html">GRC</a>.', ask=['<b>Find the personal data first.</b> Ask the CTO or security lead for the list of internet-facing PHP systems (vendor products and hosting panels count), and mark which hold or reach personal data: accounts, orders, case files, the database the application logs into. Code execution on the server gives an attacker what the PHP process can read, usually including the database credentials in its configuration.', '<b>Exposed is not breached.</b> An unpatched system is a risk under Article 32 to treat and record, not a breach under Article 33. As of the last check, no named organisation has said it was compromised through php2shell; attempts are widely reported and two vendors report successful exploitation without naming a victim. <a href="../../compromise/index.html">What that statement rests on</a>.', '<b>When the 72-hour clock starts.</b> Under Article 33 it runs from when you become aware, with reasonable certainty, that personal data was affected: a web shell, a PHP worker spawning a shell, an unexplained database export on a system holding personal data. Ask the security lead to tell you the hour that happens, not the day after, and start the assessment then.', '<b>A precautionary shutdown is a decision, not a breach.</b> Taking a service offline on purpose to protect it is not an accidental or unlawful loss of availability. Record who decided, when, for how long, and that no personal data was lost.', '<b>Ask your processors in writing.</b> A host or managed platform is a processor under Article 28 and must tell you of a breach without undue delay (Article 33(2)). Ask each one: have you updated PHP on the systems that process our data, since when, have you seen any sign of compromise, and will you tell us within hours if you do? Keep the replies.', '<b>Document either way.</b> Article 33(5) asks you to record every breach; accountability under Article 5(2) asks you to show your reasoning when you decide something is not one. Record: the systems and the personal data on each, the date each was patched or isolated, the log review window (from 17 October, the earliest reported attempt, not from the 21st), what was found, and the decision with its reasons and who made it.', '<b>If it becomes a breach.</b> Notify the supervisory authority within 72 hours unless the breach is unlikely to result in a risk to people (Article 33), and tell the people affected without undue delay if the risk to them is high (Article 34). Coordinate with whoever owns the NIS2 or DORA report: the same incident can start a 24-hour clock there.']),
        'analyst': dict(topics=['discovery', 'leak', 'timing', 'scale', 'exploitation'], intro='What this incident says about coordinated disclosure once models can find bugs, and once a leak can become a proof of concept faster than a patch can ship. The claims below are the evidence; the reading is the site\'s.', ask=['The window between leak and release was 22.5 hours and the window between first honeypot hit and release was four days. Both are shorter than the two months the fix took.', 'Three AI-assisted teams converged on a bug class seen and shelved in 2024. The constraint that failed in 2024 was proving exploitability, and that is what models now appear to lower the cost of.', 'The defensive side moved early too: WAF rules 9 hours ahead, images 6 hours ahead (against the embargo), agencies within the hour. The system is faster in both directions.', 'The public numbers were not produced for decision-making and should not be used for it; the one agency that counted got about 6,000 in a country of 1.9 million people.', 'Agencies diverged on the hardest question, offline or not, along lines that look institutional rather than technical.']),
    }
    for a in aud:
        s = sel[a['id']]
        p = PERSONAS[a['id']]
        BRIEF_TOPICS[a['id']] = s['topics']
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
        who = a['name'][0].lower() + a['name'][1:] if a['name'][1:2].islower() else a['name']  # keep CFO, PHP, AppSec as written
        who = ('an ' if who[0] in 'aeiou' else 'a ') + who
        page(f'briefings/{a["id"]}/index.html', f'Briefing for {who}: {a["question"]}', f'The php2shell story for {who}: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.', body, kind='briefing', topics=f'php2shell briefing {a["id"]}')

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
        rows += f'''<article class="source" id="{E(s["slug"])}">{it_source(s)}
<h3><a href="{E(s["slug"])}/index.html">{E(s.get("title") or s["slug"])}</a> <a class="small" href="{U(s["url"])}" rel="noopener nofollow">original &#8599;</a></h3>
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
    page('method/index.html', 'The method: capture, hash, claim, build, gate', 'How this site keeps evidence: the private vault and its protocol, the five status words, the deterministic build, the gate, and how an agent adds a source or replicates the whole thing for the next incident.', body, kind='site', topics='method provenance')

TEAM = load('team')
GROUP_AV = {'humans': 'decide', 'coordination': 'communicate', 'site': 'act', 'evidence': 'understand', 'writing': 'study', 'testing': 'study'}
KIND_LABEL = {'human': 'human', 'agent': 'agent', 'role': 'role, no agent of its own yet'}

def member_tasks(mid):
    owners = TEAM['board_owners']
    return [b for b in D['admin']['board'] if owners.get(b['owner']) == mid]

def member_initials(m):
    w = re.findall(r'[A-Za-z]+', m['alias'].lstrip('@'))
    caps = re.findall(r'[A-Z]', m['alias'])
    return (''.join(caps[:2]) if len(caps) >= 2 else (w[0][:2] if w else '?')).upper()

def member_card(m, depth):
    t = member_tasks(m['id']); st = Counter(b['status'] for b in t)
    counts = f'{st.get("open", 0)} open' + (f', {st["waiting"]} waiting' if st.get('waiting') else '') + f', {st.get("done", 0)} done'
    return (f'<a class="door door-{GROUP_AV[m["group"]]}" id="{E(m["id"])}" href="{"../" * depth}team/{E(m["id"])}/index.html">'
            f'<span class="dh"><span class="av av-{GROUP_AV[m["group"]]}">{E(member_initials(m))}</span><span><b>{E(m["name"])}</b>'
            f'<small>{E(m["alias"])} &middot; {E(m["role"])}</small></span></span>'
            f'<span class="dq">{E(m["summary"])}</span>'
            f'<span class="dm"><span>{E(KIND_LABEL[m["kind"]] if m["status"] == "active" else m["status"])}</span><span>{counts}</span></span></a>')

def task_table(rows, depth):
    if not rows: return '<p class="small">None.</p>'
    return table(['#', 'Task', 'Status', 'Shipped in'], [[E(b['id']), E(b['title']) + (f'<div class="note">{E(b["note"])}</div>' if b.get('note') else ''), pill(b['status']), E(b.get('version') or '')] for b in rows], 'board')

def build_team():
    r = D['roles']; T = TEAM; M = T['members']
    by_id = {m['id']: m for m in M}
    allt = [b for m in M for b in member_tasks(m['id'])]
    st = Counter(b['status'] for b in allt)
    stats = ''.join(stat(n, l) for n, l in [(len(M), 'members'), (sum(m['kind'] == 'human' for m in M), 'humans'), (sum(m['kind'] == 'agent' for m in M), 'agents'),
                                            (sum(m['kind'] == 'role' for m in M), 'roles not yet filled'), (st.get('open', 0), 'open tasks'), (st.get('waiting', 0), 'waiting'), (st.get('done', 0), 'done')])
    groups = ''.join(f'<section id="g-{E(g["id"])}"><h3>{E(g["name"])}</h3><p class="small">{E(g["about"])}</p><div class="doors">{"".join(member_card(m, 1) for m in M if m["group"] == g["id"])}</div></section>' for g in T['groups'])
    run = ''.join(f'<li><b>{E(p["name"])}</b> ({E(p["who"])}). {E(p["what"])}</li>' for p in T['cycle']['phases'])
    pipe = table(['Step', 'What', 'Who', 'How'], [[E(str(p['step'])), f'<b>{E(p["name"])}</b>', E(p['who']), E(p['what'])] for p in r['pipeline']])
    auds = ''.join(f'<li><a href="../briefings/{E(a["id"])}/index.html"><b>{E(a["name"])}</b></a>: {E(a["question"])}</li>' for a in r['audiences'])
    humans = ' and '.join(f'<a href="{E(m["id"])}/index.html">{E(m["name"])}</a> ({E(m["role"].lower())})' for m in M if m['kind'] == 'human')
    body = f'''
<h1>The team: two people and the agents that work with them</h1>
<p class="lead">This site is built and run by {humans}, and a team of software agents, with help from <a href="../collaborators/index.html">collaborators</a> who use it as it grows. Every member, human or agent, has a page: what they own, the rules they work by, the pages that are their home on this site, what they have shipped and the tasks they hold now. A new agent should be able to read this page and its own and begin. The roster is <a href="../data/team.json">data/team.json</a>, kept by <a href="conductor/index.html">the conductor</a>.</p>
<div class="stats">{stats}</div>
{section("members", "Who is on it", groups)}
{section("run", "How the team runs", f'<p class="caveat">{E(T.get("now", ""))}</p><p>{E(T["cycle"]["about"])}</p><ol>{run}</ol><p>Where every agent is right now, what each waits for and from whom: <a href="status/index.html">status</a>. Every vault the agents made, by ID: <a href="vaults/index.html">vaults</a>. What the agents run on their own, when, and every run they made: <a href="runs/index.html">runs</a>.</p><p>The team talks through three vaults: the conductor vault, which says where the team is; the issues vault, one task queue per member; and the mail vault, where members write to each other. <a href="channels/index.html">How the team talks</a> says what each holds and the rules.</p>')}
{section("pipeline", "The pipeline", pipe, "How a URL becomes a published claim, and who does each step.")}
{section("audiences", "The audiences", f'<ul>{auds}</ul>', "Each briefing is a role too: a reader whose question the site answers in one page.")}
{section("rules", "The rules every member shares", '''<ul>
<li><b>Capture, don't paraphrase.</b> A page you summarised but did not capture does not exist.</li>
<li><b>One file per agent per concern.</b> So a merge never asks a human to choose between two agents' edits.</li>
<li><b>Write only in your own folder.</b> Your queue, your mailbox, your claims file. To ask another member for work, send it mail; the owner opens the task.</li>
<li><b>Count, don't remember.</b> Every number on a page is computed from the thing it counts.</li>
<li><b>Five words, defined once.</b> Confirmed, reported, disputed, contradicted, unverified.</li>
<li><b>State the gap.</b> A blocked fetch, a missing primary source, an unverified quote and a blocked task are all published, not hidden.</li>
<li><b>Read keys yes, vault keys never.</b> And this vault's read key is not published either, because it holds third-party pages.</li>
<li><b>Verify live.</b> A release is done when the live site serves the version, not when the push succeeds.</li>
</ul>''')}
'''
    page('team/index.html', 'The team: the people, the agents and how they work together', f'Every member of the team that runs this site, {sum(m["kind"] == "human" for m in M)} people and {len(M) - sum(m["kind"] == "human" for m in M)} agents and roles, with a page each: role, what they own, their tasks and what they shipped; how a run works, the pipeline and the {len(r["audiences"])} audiences.', body, kind='site', topics='team agents')

    legacy = {a['id']: a for a in r['agents']}
    legacy.update({'story-site': legacy.get('claude-story-site', {}), 'newsroom-lead': legacy.get('claude-newsroom-lead', {})})
    for m in M:
        t = member_tasks(m['id'])
        opn = [b for b in t if b['status'] == 'open']; wait = [b for b in t if b['status'] == 'waiting']; done = [b for b in t if b['status'] == 'done']
        lg = legacy.get(m['id']) or {}
        home = ''.join(f'<a class="door door-{GROUP_AV[m["group"]]}" href="../../{E(h)}"><b>{E(n)}</b><span>{E(h)}</span></a>' for h, n in m['home'])
        addr = m.get('address') or (m['mail'] + '@php.newsroom')
        facts = [('Kind', E(KIND_LABEL[m['kind']])), ('Status', E(m['status'])), ('Alias', f'<code>{E(m["alias"])}</code>'), ('Known as', f'<code>{E(addr)}</code>')]
        if m.get('joined'): facts.append(('Joined', E(m['joined'])))
        kv = ' &middot; '.join(f'<b>{k}</b> {v}' for k, v in facts)
        mistake = f'<p><b>The mistake behind the rules.</b> {E(lg["mistake"])}</p>' if lg.get('mistake') else ''
        beat = f'<p><b>Beat.</b> {E(lg["beat"])}</p>' if lg.get('beat') else ''
        achieved = ''.join(f'<li>{E(x)}</li>' for x in m['achieved'])
        waiting_on = ''
        if m['kind'] == 'human' and opn:
            waiting_on = section('waiting', 'Waiting on ' + E(m['name'].split()[0]), task_table(opn, 2), 'Decisions and work only a person can supply. Each is a card in this member\'s queue in the issues vault, and the conductor names it in every digest until it is answered.')
        tasks = '' if (m['kind'] == 'human' and opn) else section('tasks', 'Open tasks', task_table(opn, 2))
        body = f'''
<p class="crumb"><a href="../index.html">The team</a> / {E(m["name"])}</p>
<h1>{E(m["name"])}: {E(m["role"].lower() if m["kind"] != "human" else m["role"])}</h1>
<p class="lead">{E(m["summary"])}</p>
<p class="kv">{kv}</p>
{beat}
{section("owns", "What they own", "<ul>" + "".join(f"<li>{E(x)}</li>" for x in m["owns"]) + "</ul>")}
{section("rules", "The rules they work by", "<ul>" + "".join(f"<li>{E(x)}</li>" for x in m["rules"]) + "</ul>" + mistake)}
{section("home", "Their home on this site", f'<div class="doors">{home}</div>')}
{waiting_on}
{tasks}
{section("blocked", "Waiting on someone else", task_table(wait, 2)) if wait else ''}
{section("achieved", "What they have done", (f'<ul>{achieved}</ul>' if achieved else '<p class="small">Nothing yet.</p>') + (f'<h3>Closed on the board</h3>{task_table(done, 2)}' if done else ''))}
{section("reach", "How to reach them", f'<ul><li><b>Mail</b>: an <code>.eml</code> in <code>mail/mailroom/{E(m["mail"])}/</code> in the mail vault (<code>fmb2tpl2</code>).</li><li><b>Their queue</b>: <code>issues/{E(m["id"])}/open|blocked|done/</code> in the issues vault (<code>zjruy9vk</code>). Read it; do not write in it.</li><li><b>Their page in the conductor vault</b>: <code>team/members/{E(m["id"])}.md</code>.</li></ul><p class="small">What the three vaults are and who holds their keys: <a href="../channels/index.html">how the team talks</a>.</p>')}
'''
        page(f'team/{m["id"]}/index.html', f'{m["name"]}, {m["role"].lower() if m["kind"] != "human" else m["role"]}: the team', f'{m["name"]} ({m["alias"]}) on the team behind this site: {m["summary"]}', body, kind='site', topics='team agents')

    chans = ''.join(f'''<section class="vcard" id="{E(c["id"])}"><h2>{E(c["name"])} <span class="st">private</span></h2>
<p class="kv"><b>Vault</b> <code>{E(c["vault"])}</code> &middot; <b>written by</b> {E(c["writes"])} &middot; <b>read by</b> {E(c["reads"])}</p>
<p>{E(c["holds"])}</p><p class="small"><b>How.</b> {E(c["how"])}</p></section>''' for c in T['channels'])
    cond = by_id['conductor']
    body = f'''
<p class="crumb"><a href="../index.html">The team</a> / How the team talks</p>
<h1>How the team talks: three vaults and one run</h1>
<p class="lead">The members of this team, two people and the agents, do not share a chat. They coordinate through three encrypted vaults, using two protocols from the sgit.ai estate: Email-FS-lite for messages and Issues-FS-lite for tasks. Every message and every change of a task is a file, and every cycle is one commit, so the history of the vaults is the record of who asked for what, who took it and when it was done.</p>
{chans}
{section("run", "The run", f'<p>{E(T["cycle"]["about"])}</p><ol>{run}</ol>')}
{section("protocols", "The two protocols", '''<ul>
<li><b>Email-FS-lite.</b> To send, a member writes an <code>.eml</code> file into the recipient's <code>mailroom/</code> and a copy into its own <code>outbox/</code>; the recipient moves it into its <code>inbox/</code>, and into <code>done/</code> when the work is finished. Messages are never edited or deleted, only moved. <a href="https://sgraph.ai/en-gb/library/how-it-works/email-fs-lite">The reference</a>.</li>
<li><b>Issues-FS-lite.</b> Each member's tasks are markdown files in its own <code>open/</code>, <code>blocked/</code> and <code>done/</code> folders; opening, blocking, unblocking and closing a task are four moves. Anyone may read any queue; only its owner writes in it. <a href="https://issues-fs.sgit.ai/lite/index.html">The reference</a>.</li>
<li><b>The conductor's lane.</b> A write-only channel on the conductor vault: a member encrypts a message to the conductor's public key (<code>sha256:742d442b1c5b07bd</code>) and appends it with its own token, which can write and cannot read. The conductor drains it at every run with <code>admin/build/conductor_drain.py</code>.</li>
</ul>''')}
{section("keys", "Keys", '<p>None of the three vaults is published. The conductor holds their keys; every member gets the conductor vault\'s read key and the keys to the issues and mail vaults privately, and its own lane token, in the way the editor decides (<a href="../../admin/board/index.html">board</a> 070). No key or token is on this site or in its repository.</p>')}
{section("board", "The board", f'<p>The site\'s <a href="../../admin/board/index.html">board</a> moved into the issues vault on 22 October 2026: each row became a card in its owner\'s queue. The vault is now the truth; <code>admin/build/issues_sync.py import</code> writes the board on this site from it before a release, so the board here is a snapshot as of the release that built it.</p>')}
<p>The channels are kept by <a href="../{E(cond["id"])}/index.html">{E(cond["name"])}</a>.</p>
'''
    page('team/channels/index.html', 'How the team talks: three vaults and one run', 'The three private vaults the team coordinates through (the conductor vault, Issues-FS-lite tasks and Email-FS-lite mail), the run that opens and closes every scheduled cycle, and the rules.', body, kind='site', topics='team agents')

def build_billing():
    b = D['billing']
    P = b['pricing']; pr = b['runs']['prices']
    tier_h = [f'{E(t["tier"].capitalize())}<br><span class="small">{"up to " + str(t["max_days"]) + " day" + ("s" if t["max_days"] > 1 else "") if t["max_days"] else "older"}, &times;{t["multiplier"]:g}</span>' for t in P['tiers']]
    kinds = table(['Type', 'Layer', 'Base'] + tier_h + ['Pages', 'Why'], [[f'<b>{E(t["type"])}</b>', E(t['layer']), f'{t["base"]}p'] + [f'{pr[t["type"] + "_" + tr["tier"]]}p' if t['decays'] else (f'{pr[t["type"]]}p' if i == 0 else '&middot;') for i, tr in enumerate(P['tiers'])] + [E(t['pages']), E(t['why'])] for t in P['types']])
    kinds = f'<h3>The formula</h3><p class="kv"><code>{E(P["formula"])}</code>, with a floor of {P["floor"]}p.</p>' + kinds + f'<p class="small">A dot means the price does not decay: the type costs the same at any age. {E(P["age_from"])}</p><h3>The rules of engagement</h3><ol>' + ''.join(f'<li>{E(r)}</li>' for r in P['rules']) + '</ol>' + ''.join(f'<p class="small"><b>{E(t["tier"].capitalize())}.</b> {E(t["why"])}</p>' for t in P['tiers'])
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
{section("prices", "The prices, as data", f'<pre>{E(json.dumps({"storageKey": runs["storageKey"], "start": runs["start"], "symbol": runs["symbol"], "prices": runs["prices"], "topup": runs["topup"]}, indent=1, sort_keys=True))}</pre><p>This block is <code>data/billing.json</code>, which is also what every page\'s meter config is generated from, so the table above and the meter cannot disagree.</p>')}
'''
    page('billing/index.html', 'The billing model: what runs and what is designed', 'How this site is paid for: the reading meter that runs (pence per page, kept in your browser, never blocking), the provenance pricing that is designed (per claim, with a share for the fact creator), and a counted model of what the story cost to assemble.', body, kind='site', topics='billing meter economics')

def build_account():
    body = '''
<h1>Your reading account</h1>
<p class="lead">Everything the meter knows is in this browser: the balance, every page opened with the share read and what it cost, what you declined and why, and your top-ups. Export it as JSON; nothing is sent anywhere unless you choose to. A new browser or cleared site data starts again with the starting credit.</p>
<sg-meter view="account"></sg-meter>
<p>How the meter works, and why it works this way, is on <a href="../billing/index.html">the billing model</a>. The account needs JavaScript: the balance lives here, not on a server.</p>
'''
    page('account/index.html', 'Your reading account', 'The balance, history and receipts of your reading on this site, kept in your browser.', body, kind='account')
    body = '''
<h1>Top up</h1>
<p class="lead">Reading credit, paid on a payment page. No payment link is configured for this site yet, so what follows is the meter's simulated cart, which says it is simulated. When a link is added, this page will say so and the credit will be added on the return page without verifying the payment.</p>
<sg-meter view="topup"></sg-meter>
<p>Where your data is kept, and what can leave your browser, is on <a href="../billing/index.html">the billing model</a>. A payment returns to <a href="topped-up.html">the topped-up page</a>.</p>
'''
    page('account/top-up.html', 'Top up', 'Add reading credit to the balance kept in your browser.', body, kind='account')
    body = '''
<h1>Thank you</h1>
<p class="lead">If you arrived here from a payment page, the credit has been added to the balance in this browser. If you opened this page on its own, nothing is added and the meter says so.</p>
<sg-meter view="topped-up"></sg-meter>
<p><a href="index.html">Your reading account</a> &middot; <a href="../index.html">The front page</a></p>
'''
    page('account/topped-up.html', 'Topped up', 'The page a payment returns to.', body, kind='account')

def render_md_file(path):
    """A small markdown renderer for the brief and corrections files: headings, paragraphs, lists, code."""
    full = os.path.realpath(os.path.join(ROOT, path))
    allowed = [os.path.realpath(os.path.join(ROOT, n)) for n in ('BRIEF-CORRECTIONS.md', 'REALITY.md', 'README.md', 'AGENTS.md')]
    if not (full.startswith(os.path.realpath(os.path.join(ROOT, 'admin', 'content')) + os.sep) or full in allowed):
        raise SystemExit(f'build: render_md_file reads only admin/content/ and the top-level notes, not {path!r}')
    with open(full, encoding='utf-8') as f:
        text = f.read()
    out, in_list, in_code, rows = [], False, False, []
    def flush():
        if rows:
            out.append(table([inline_md(c) for c in rows[0]], [[inline_md(c) for c in r] for r in rows[1:]])); rows.clear()
    for line in text.splitlines():
        if not in_code and line.strip().startswith('|'):
            if in_list: out.append('</ul>'); in_list = False
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if not all(re.match(r'^:?-+:?$', c) for c in cells):
                rows.append(cells)
            continue
        flush()
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
        m = re.match(r'^!\[([^\]]+)\]\((assets/briefs/[a-z0-9-]+\.png)\)$', line.strip())
        if m:
            # a picture in a brief: only a PNG committed under assets/briefs/, sized from its own header
            src = os.path.join(ROOT, m.group(2))
            if not os.path.isfile(src):
                raise SystemExit(f'build: {path} shows {m.group(2)}, which is not in the repository')
            with open(src, 'rb') as f:
                head = f.read(24)
            w, h = int.from_bytes(head[16:20], 'big'), int.from_bytes(head[20:24], 'big')
            out.append(f'<figure class="shot"><img src="../../{E(m.group(2))}" alt="{E(m.group(1))}" width="{w}" height="{h}" loading="lazy"></figure>'); continue
        if line.startswith('>'):
            q = inline_md(re.sub(r'^>\s?', '', line))
            if out and out[-1].endswith('</p></blockquote>'):
                out[-1] = out[-1][:-len('</p></blockquote>')] + ' ' + q + '</p></blockquote>'
            else:
                out.append('<blockquote><p>' + q + '</p></blockquote>')
            continue
        if line.strip():
            out.append('<p>' + inline_md(line) + '</p>')
    flush()
    if in_list: out.append('</ul>')
    if in_code: out.append('</pre>')
    return '\n'.join(out)

def inline_md(s):
    s = E(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])', r'<i>\1</i>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s"<>]+)\)', r'<a href="\2" rel="noopener">\1</a>', s)
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
    page('brief/index.html', 'The brief: a written request and two voice memos', 'The brief this site was built from, published in full: the editor\'s written request and two transcribed voice memos on mapping the PHP vulnerability as evidence.', body, kind='site')

def build_corrections():
    body = f'''
<h1>Corrections</h1>
<p class="lead">Where the brief was wrong, where a page was wrong, what was found and what was done instead. A correction is published above the mistake, dated, and the mistake stays visible. The file is <code>BRIEF-CORRECTIONS.md</code> in the repository.</p>
{render_md_file("BRIEF-CORRECTIONS.md")}
'''
    page('corrections/index.html', 'Corrections', 'Where the brief or a page of this site was wrong, what was found and what was done instead.', body, kind='site')

def build_admin():
    vs = D['versions']
    rows = ''.join(f'<article class="rel" id="v{E(v["version"])}"><h3>v{E(v["version"])} &middot; {E(v["date"])}</h3><p>{E(v["title"])}</p><p class="small">{E(v.get("summary") or "")} Vault commit <code>{E(v.get("vault_commit") or "")}</code>.{" Reconstructed after the fact." if v.get("reconstructed") else ""}</p><p class="small">Files: {", ".join(f"<code>{E(c)}</code>" for c in v.get("changes", []))}</p></article>' for v in vs['versions'])
    body = f'''
<h1>Release history</h1>
<p class="lead">One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v{E(vs["current"])}. The data is <a href="../data/versions.json">data/versions.json</a>.</p>
{rows}
'''
    page('admin/versions.html', 'Release history', 'Every release of this site, with what changed, why, and the vault commit it was built from.', body, kind='site')
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
{section("section", "The admin section", '<ul><li><a href="board/index.html">The board</a>: the work, as rows.</li><li><a href="roles/index.html">Roles</a>: who does what, and how an agent joins.</li><li><a href="briefs/index.html">Briefs</a>: the build briefs, in full.</li><li><a href="vault/index.html">The vault, opened</a>: the read key and the browser link.</li><li><a href="telemetry/index.html">Who reads this site</a>: the telemetry lane and its counts.</li><li><a href="synthetic/index.html">Synthetic readers</a>: six test readers who read the live site every hour and say what works and what does not.</li></ul>')}
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
    page('admin/index.html', 'Admin and engineering', 'How this site is built, the checks in its gate, where things are, the reality file and the honest column.', body, kind='site')

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
    lines.append('## Facts, one page each, with a timeline and every version')
    for c in D['claims']:
        lines.append(f'- [{c["claim"][:100]}]({BASE_URL}/facts/{c["id"]}/index.md): {c["status"]}')
    lines.append('')
    lines.append('## Version histories, one per section')
    for sid, sec in LEDGER['sections'].items():
        if sec['kind'] != 'fact':
            lines.append(f'- [{sec["title"]}]({BASE_URL}/versions/{sid}/index.md): {len(sec["versions"])} versions')
    lines.append('')
    lines.append('## The team, one page per member')
    lines.append(f'- [How the team talks: three vaults and one run]({BASE_URL}/team/channels/index.md): the conductor, issues and mail vaults, the run, the rules')
    lines.append(f'- [Vaults: who made each one]({BASE_URL}/team/vaults/index.md): every vault each agent made, by ID only, and whether its key is sealed to the editor')
    lines.append(f'- [Status]({BASE_URL}/team/status/index.md): where every agent is, what it waits for, the branches waiting for dev')
    lines.append(f'- [Runs]({BASE_URL}/team/runs/index.md): what the agents run on their own, the quiet hours, and every recorded run')
    for m in TEAM['members']:
        lines.append(f'- [{m["name"]}]({BASE_URL}/team/{m["id"]}/index.md): {m["role"]}; {m["summary"]}')
    lines.append('')
    lines.append("## The Sherpa and the feedback from collaborators, one page each")
    for p, t, d, _ in PAGES:
        if p.startswith(('sherpa/', 'feedback/')):
            lines.append(f'- [{t}]({BASE_URL}/{md_path(p)}): {d}')
    lines.append('')
    lines.append('## Parties, one page each')
    for a in D['actors']:
        lines.append(f'- [{a["name"]}]({BASE_URL}/actors/{a["id"]}/index.md): {a["role"]}')
    lines.append('')
    lines.append('## GRC: one page per risk, stakeholder register and framework')
    nav_paths = {p for _, items in NAV for p, _ in items}
    for p, t, d, _ in PAGES:
        if p.startswith('grc/') and p not in nav_paths:
            lines.append(f'- [{t}]({BASE_URL}/{md_path(p)}): {d}')
    lines += [f'- [grc.json]({BASE_URL}/data/grc.json): stakeholders, weaknesses and risks', f'- [grc-frameworks.json]({BASE_URL}/data/grc-frameworks.json): the frameworks and controls mapped',
              f'- [grc-graph.json]({BASE_URL}/data/grc-graph.json): the risk graph, every edge a verb with its inverse', '']
    lines += ['## Data', f'- [sources.json]({BASE_URL}/data/sources.json): the vault manifest with every capture and hash',
              f'- [claims.json]({BASE_URL}/data/claims.json): every claim with status, who says it and sources',
              f'- [timeline.json]({BASE_URL}/data/timeline.json): every dated event', f'- [numbers.json]({BASE_URL}/data/numbers.json): the scale figures and what each measures',
              f'- [agencies.json]({BASE_URL}/data/agencies.json): the agencies\' stances', f'- [affected.json]({BASE_URL}/data/affected.json): versions, SAPIs, mitigations',
              f'- [software.json]({BASE_URL}/data/software.json): the NCSC-NL inventory, parsed', f'- [exploitation.json]({BASE_URL}/data/exploitation.json): the signals',
              f'- [graph.json]({BASE_URL}/data/graph.json): nodes and citation edges', f'- [layers.json]({BASE_URL}/data/layers.json): which file is evidence, derived, authored or site', f'- [vault.json]({BASE_URL}/data/vault.json): the vault\'s head, counts and agents',
              f'- [billing.json]({BASE_URL}/data/billing.json): the meter configuration and the designed model', f'- [versions.json]({BASE_URL}/data/versions.json): release history',

              f'- [questions.json]({BASE_URL}/data/questions.json): the questions readers ask, each answer with its sources and the pages that carry it', '',
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
        steps += '<li class="' + (cur ? 'here' : done ? 'seen' : '') + '"><a href="' + root + esc(x[0]) + '" title="' + esc(x[1]) + ', ' + esc(String(x[2])) + ' min">' + (i + 1) + '</a></li>';
      });
      var nx = next ? '<span class="nx">Next: <a href="' + root + esc(next[0]) + '">' + esc(next[1]) + '</a> <small>' + esc(String(next[2])) + ' min</small></span>'
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

  // Since your last visit: the release you last saw is remembered, and what's new marks every release after it.
  var ver = html.getAttribute('data-ver') || '', lastVer = get('p2s.ver');
  function newer(a, b) { var x = a.split('.'), y = b.split('.'); for (var i = 0; i < 3; i++) { var d = (+x[i] || 0) - (+y[i] || 0); if (d) return d > 0; } return false; }
  if (ver && lastVer && lastVer !== ver) set('p2s.since', lastVer);
  if (ver) set('p2s.ver', ver);
  var since = get('p2s.since');
  if (since) {
    document.querySelectorAll('[data-rel]').forEach(function (el) { if (newer(el.getAttribute('data-rel'), since)) el.classList.add('unseen'); });
  }

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

// A note in the bar when this page is older than the release the site now serves (one same-origin read of /VERSION).
(function () {
  var v = document.querySelector('nav.site .ver'), root = document.documentElement.getAttribute('data-root') || '';
  if (v && window.fetch) fetch(root + 'VERSION?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.ok ? r.text() : ''; }).then(function (t) {
    var live = (t || '').trim(), mine = v.textContent.replace(/^v/, '');
    if (!/^\d+\.\d+\.\d+$/.test(live)) return;
    var a1 = live.split('.').map(Number), b1 = mine.split('.').map(Number), d = 0;
    for (var i = 0; i < 3 && !d; i++) d = a1[i] - (b1[i] || 0);
    if (d <= 0) return;
    var a = document.createElement('a'); a.className = 'ver newer'; a.href = root + 'status/index.html';
    a.title = 'This page is v' + mine + '; the site now serves v' + live + '. Reload for the new release; the pipeline page shows what changed and what is deploying.';
    a.textContent = 'v' + live + ' is live: reload'; v.insertAdjacentElement('afterend', a);
  }).catch(function () {});
})();
''')

def build_all():
    PAGES.clear()
    build_flaws(); build_timeline(); build_discovery(); build_leak(); build_exploitation(); build_compromise(); build_playbook()
    build_code(); build_context(); build_impact(); build_defence()
    build_claims(); build_numbers(); build_agencies(); build_affected(); build_sources(); build_graph()
    build_source_pages(); build_actors()
    build_explained(); build_glossary(); build_briefings(); build_start(); build_summary(); build_index()
    build_method(); build_team(); build_collaborators(); build_runs(); build_join(); build_status_page(); build_vault_register(); build_billing(); build_account(); build_brief(); build_corrections(); build_admin()
    build_interview(); build_facts(); build_versions(); build_whatsnew(); build_pipeline()
    build_review(); build_admin_section(); build_keys(); build_status(); build_vaults(); build_feeds_page(); build_you(); build_stack(); build_reader(); build_subscribe(); build_agents_guide(); build_questions(); build_articles(); build_layers(); build_readings(); build_patching(); build_inventory(); build_signals(); build_status_json(); build_factcheck(); build_grc(); build_sherpa()

def main():
    # Two passes: the first measures every page (reading time, terms used), the second writes pages that cite those measures.
    build_all()
    build_all()
    build_now(); build_llms(); _design_made = __import__('design').build(globals()); open(os.path.join(ROOT, 'llms.txt'), 'a', encoding='utf-8').write(__import__('design').llms_lines(_design_made, BASE_URL)); build_sitejs(); build_personas_js(); build_feed(); build_seo(); save_ledger(); build_feeds_xml(); build_stack_catalogue(); save_items()
    write('admin/build/outputs.txt', '\n'.join(sorted(OUTPUTS | {'admin/build/outputs.txt'})) + '\n')
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
<p class="meta"><b>{E(s.get("publisher") or "")}</b> &middot; <a href="{U(s["url"])}" rel="noopener nofollow">{E(s["url"])}</a> &middot; published {E(str(s.get("published") or "not stated"))} &middot; added by <code>{E(s.get("added_by") or "")}</code> &middot; slug <code>{E(slug)}</code></p>
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

def build_keys():
    if not os.path.exists(os.path.join(DATA, 'keys.json')):
        return  # data/keys.json is not in the repository yet (.gitignore's keys*.json rule held it back): board, security@
    """admin/keys/: the root, every agent's key, every vault and where its key is kept, the rules of engagement and how to
    hand a key over. From data/keys.json; public keys, fingerprints and vault ids only."""
    K = load('keys')
    r = K['root']
    fp = lambda x: f'<code>{E(x)}</code>' if x else '<span class="dim">none</span>'
    rules = ''.join(f'<li><b>{E(a)}</b> {E(b)}</li>' for a, b in K['rules'])
    agents = table(['Agent', 'Key', 'Record (signing fingerprint)', 'Status', 'Operated until'],
                   [[E(a['name']), E(a['kind']), fp(a['record']), E(a['status']), E(a['until'] or '')] for a in K['agents']], 't keys')
    with_root = sum(1 for v in K['vaults'] if v['key_with_root'].startswith('opened'))
    vaults = table(['Vault', 'Id', 'Access', 'Made by', 'Key with the root', 'Next'],
                   [[E(v['name']), f'<code>{E(v["id"])}</code>', E(v['access']), E(v['made_by']), E(v['key_with_root']), E(v['action'])] for v in K['vaults']], 't keys')
    shared = ''.join(f'<li><b>{E(a)}</b>: {E(b)}</li>' for a, b in K['shared'])
    made = sum(1 for a in K['agents'] if a['record'] and a['kind'] != 'person' and a['status'].startswith('in the register'))
    body = f"""
<h1>Keys: who holds what, and how a secret moves</h1>
<p class="lead">Every agent on this newsroom gets its own key pair on <a href="{U(K['register'])}" rel="noopener">pki.sgit.ai</a>, to sign what it writes and to receive a secret meant for it alone. The editor's key is the root. As of {E(K['as_of'])}, {made} of {len(K['agents']) - 1} agents have a live key in the register and {with_root} of {len(K['vaults'])} vault keys are confirmed in the editor's hands. This page holds public keys, fingerprints and vault ids only. No secret is ever on it.</p>
<h2>The root</h2>
<p><b>{E(r['name'])}</b>: record {fp(r['record'])} (signing), encryption key {fp(r['encryption'])}, made {E(r['made'])}; {E(r['where'])}.</p>
<p>Agents pin it from {E(r['pinned_in'])}. A fingerprint on a website can be changed by whoever changes the website, so the pin comes from an agent's instructions and the register confirms it.</p>
<h2>Rules of engagement</h2>
<ol>{rules}</ol>
<h2>The agents</h2>
{agents}
<h2>The vaults</h2>
<p>Every vault's key reaches the editor, sealed to the root, so none is lost when the session that made it ends. "Unknown" means nobody has recorded a handover: the agent that made the vault does it next.</p>
{vaults}
<h2>Shared vaults</h2>
<ul>{shared}</ul>
<p>Several agents write to a shared vault with its vault key, which the editor seals to each of them; sgit keeps every change, who made it, and the history. Readers who only read get a read key.</p>
<h2>An agent with no key yet</h2>
<p>In its session, with the root from its instructions (the full steps are at <a href="{U(K['handover'])}" rel="noopener">pki.sgit.ai/handover.md</a>, section C):</p>
<pre><code>curl -sO {E(K['tool'])}
node pki-agent.mjs keygen --name "&lt;role&gt;@php.newsroom" --runtime "claude-code, cloud session" --session
node pki-agent.mjs operator {E(r['record'])} --policy admin/security/REQUIREMENTS.md
node pki-agent.mjs submission --out my-record.json
node pki-agent.mjs whoami</code></pre>
<p>It says its fingerprint in the session and gives the editor <code>my-record.json</code> (public). The editor compares the fingerprint, signs it on pki.sgit.ai, and the agent's row above gets its record.</p>
<h2>Handing over a vault key</h2>
<pre><code>node pki-agent.mjs pin {E(r['record'])}
node pki-agent.mjs root
node pki-agent.mjs seal --from-vault &lt;the vault's folder&gt; --name "vault key: &lt;name&gt; (&lt;id&gt;)" --qr vault-key.png</code></pre>
<p>Sealed to the root by default; add <code>--to &lt;fingerprint&gt;</code> for an agent the editor names, and the root still gets its copy. The agent then tells the editor, in the session, four things: the vault's name and id, the recipient, its own fingerprint, and the sealed link or QR image. The sealed link is safe to show: only the recipient's key opens it. The editor opens it on <a href="https://pki.sgit.ai/m/index.html" rel="noopener">pki.sgit.ai/m/</a>, files the key in his vault of vaults, and the vault's row above changes to "opened".</p>
<p class="small">{'The editor publishes an inbox on his record: agents can also deliver with <code>pki-agent send</code> into it.' if r.get('inbox') else 'The editor has no inbox (append lane) on his record yet. When he publishes one, agents deliver sealed keys straight into it with <code>pki-agent send</code>, and none waits on a session being read.'}</p>
<p>The rules every agent works to are in <code>admin/security/REQUIREMENTS.md</code>; who does what is on <a href="../roles/index.html">roles</a>.</p>
"""
    page('admin/keys/index.html', 'Keys: who holds what, and how a secret moves', 'The newsroom\'s keys: the editor\'s root key, every agent\'s key pair on pki.sgit.ai, every vault and whether its key is safe with the editor, the rules of engagement, and how an agent hands a vault key over. No secrets.', body, kind='site')


# ----------------------------------------------------------------------------- who reads this site, in public (v0.8.4)

TG = [('readers', 'tg1'), ('us', 'tg2'), ('synthetic', 'tg3'), ('crawlers', 'tg4')]

def telemetry_hourly_svg(P):
    H = P['hourly']; G = P['groups']; W, HH, pl, pb, pt = 960, 200, 34, 24, 8
    n = len(H); bw = (W - pl) / max(n, 1)
    tot = [sum(h[1]) for h in H]; mx = max(tot + [1]); step = max(5, -(-mx // 4 // 5) * 5); top = step * -(-mx // step)
    y = lambda v: pt + (HH - pt - pb) * (1 - v / top)
    out = [f'<svg class="tchart" viewBox="0 0 {W} {HH}" role="img" aria-label="Page views per hour, by group">']
    for v in range(0, top + 1, step):
        out.append(f'<line x1="{pl}" x2="{W}" y1="{y(v):.1f}" y2="{y(v):.1f}" class="tgrid"/><text x="{pl - 6}" y="{y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    every = max(1, -(-n // ((W - pl) // 44)))
    for k, h in enumerate(H):
        base, x, w = 0, pl + k * bw + 1, max(1, bw - 2)
        tip = E(h[0].replace('T', ' ') + ':00 UTC: ' + ', '.join(f'{P["labels"][g].split(":")[0]} {h[1][i]}' for i, g in enumerate(G)))
        out.append(f'<g><title>{tip}</title>')
        for i, g in enumerate(G):
            v = h[1][i]
            if not v: continue
            y0, y1 = y(base), y(base + v)
            out.append(f'<rect x="{x:.1f}" y="{y1:.1f}" width="{w:.1f}" height="{max(0.5, y0 - y1 - 1):.1f}" class="{dict(TG)[g]}"/>')
            base += v
        out.append(f'<rect x="{pl + k * bw:.1f}" y="{pt}" width="{bw:.1f}" height="{HH - pt - pb}" fill="transparent"/></g>')
        if k % every == 0:
            lab = h[0][8:10] + ' Oct' if h[0][11:] == '00' else h[0][11:] + ':00'
            out.append(f'<text x="{pl + k * bw + bw / 2:.1f}" y="{HH - 7}" text-anchor="middle">{lab}</text>')
    out.append(f'<line x1="{pl}" x2="{W}" y1="{HH - pb}" y2="{HH - pb}" class="taxis"/></svg>')
    return ''.join(out)

def telemetry_map_svg(P):
    rows = {c: (v, s) for c, v, s in P['readers']['countries'] if c}
    mx = max([v for v, s in rows.values()] + [1])
    steps = [0.18, 0.34, 0.52, 0.72, 0.92]
    def op(v):
        import math
        return steps[min(4, int(4.999 * math.log(v) / math.log(mx))) if mx > 1 else 0]
    out = [f'<svg class="tmap" viewBox="0 0 {WORLD["width"]:g} {WORLD["height"]:g}" role="img" aria-label="Readers by country">']
    for code, c in WORLD['countries'].items():
        r = rows.get(code)
        title = E(f'{c["name"]}: {r[0]} page views, {r[1]} sessions' if r else f'{c["name"]}: no readers yet')
        out.append(f'<path d="{E(c["d"])}" class="{"tg1" if r else "tm0"}"{f" fill-opacity=\"{op(r[0])}\"" if r else ""}><title>{title}</title></path>')
    out.append('</svg>')
    ramp = ''.join(f'<i class="tg1" style="opacity:{o}"></i>' for o in steps)
    return ''.join(out) + f'<p class="tramp">fewer {ramp} more page views (log scale; most: {mx})</p>'

def telemetry_public_html():
    P = TPUB
    if not P:
        return '<p class="small">No public stats yet.</p>'
    T, R = P['totals'], P['readers']
    pv = next((x for x in D['vaults']['vaults'] if x['slug'] == 'telemetry-public'), None)
    legend = ''.join(f'<span><i class="{c}"></i>{E(P["labels"][g])}</span>' for g, c in TG)
    groups = table(['Group', 'Page views', 'Sessions', 'Of which declared'], [[f'<i class="tsw {c}"></i> {E(P["labels"][g])}', str(T[g]['views']), str(T[g]['sessions']), str(T[g]['declared'])] for g, c in TG])
    countries = table(['Country', 'Page views', 'Sessions'], [[f'<code>{E(c or "?")}</code> {E(WORLD["countries"].get(c, {}).get("name", "not known"))}', str(v), str(n)] for c, v, n in R['countries']])
    rules = ''.join(f'<li><b>{E(x["how"])}.</b> {E(x["text"])}</li>' for x in P['method']['classes'])
    live = vault_live(pv['read_key'], True, 2, 'The same counts, and more, in the public stats vault: its own app, updated at every drain.') if pv else ''
    return f"""<p>Not everyone who opens a page is a reader. Each session (one browser tab) is put in one of four groups: <b>readers</b>; <b>the editor, team and power users</b>; <b>synthetic</b> visitors, the headless browsers of this site's own agents and of anyone testing it; and <b>crawlers</b>, search engines rendering the pages. As of <b>{E(P["as_of"])}</b>, since {E(P["first"])}:</p>
{groups}
<p class="tlegend">{legend}</p>
<div class="tfig">{telemetry_hourly_svg(P)}</div>
<p class="small">Page views per UTC hour, stacked by group. Hover a column for its numbers.</p>
<h3>Where readers are</h3>
<p>Readers only: {R["views"]} page views in {R["sessions"]} sessions, {R["read_on"]} of which read more than one page; {len([c for c in R["countries"] if c[0]])} countries. Country from a lookup in the reader's browser; nothing finer is published.</p>
<div class="tfig">{telemetry_map_svg(P)}</div>
<details><summary>Every country</summary>{countries}</details>
<h3>How the groups are told apart</h3>
<ol>{rules}</ol>
<p>{E(P["method"]["note"])}</p>
<div class="twho" id="twho"><p><b>This browser counts as:</b> <span class="small">(kept in this browser only; the next page you open sends it)</span></p><p class="twho-b"></p></div>
<script>(function(){{var box=document.querySelector('#twho .twho-b');if(!box)return;var k='p2s.telemetry.who',cur='';try{{cur=localStorage.getItem(k)||''}}catch(e){{}}
[['','work it out'],['editor','the editor'],['team','team'],['power-user','a power user'],['reader','a reader']].forEach(function(o){{var b=document.createElement('button');b.type='button';b.className='rs-b'+(cur===o[0]?' on':'');b.textContent=o[1];b.setAttribute('aria-pressed',String(cur===o[0]));
b.addEventListener('click',function(){{try{{if(o[0])localStorage.setItem(k,o[0]);else localStorage.removeItem(k)}}catch(e){{}}cur=o[0];box.querySelectorAll('button').forEach(function(x,i){{x.className='rs-b';x.setAttribute('aria-pressed','false')}});b.className='rs-b on';b.setAttribute('aria-pressed','true')}});box.appendChild(b)}})}})()</script>
<h3>The public stats vault</h3>
<p>The curated counts above are written at every drain into a public vault, <code>{E(pv["id"]) if pv else ""}</code>, by <code>admin/build/telemetry_publish.py</code> (run by <code>admin/build/telemetry_flow.sh</code>): per hour and per day by group, and over readers only, countries, devices, languages, versions, pages and referrer hosts. No row, session id, city, region, time zone or time finer than the hour leaves the private vault. Its read key is published here.</p>
{vault_note(pv["read_key"]) if pv else ""}
{live}
"""

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
    page('admin/board/index.html', 'The board', 'The work on this site and its vault, as rows: what is open, who owns it, what shipped it.', body, kind='site')
    def pki_html(r):
        k = r.get('pki')
        if not k: return ''
        return (f'<p><b>Public key on pki.sgit.ai.</b> record <code>{E(k["record"])}</code>, encryption <code>{E(k["encryption"])}</code>, made {E(k["made"])}. '
                f'<a href="{U(k["key_link"])}" rel="noopener">Open the key link</a> (pki.sgit.ai recomputes the fingerprint in your browser). {E(k["note"])}</p>'
                f'<p><img src="../../{E(k["qr"])}" alt="QR code of dev@php.newsroom\'s public key" width="180" height="180" style="background:#fff;padding:4px;border-radius:6px"></p>')
    cards = ''.join(f'<article class="role" id="{E(r["id"])}"><h3>{E(r["name"])} <span class="small">{E(r["who"])}</span></h3><p><b>Owns.</b> {E(r["owns"])}</p><ul>{"".join(f"<li>{E(x)}</li>" for x in r["rules"])}</ul>{pki_html(r)}</article>' for r in A['roles'])
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
    page('admin/roles/index.html', 'Roles and responsibilities', 'The roles on this site and its vault, who fills each, what it owns and the rules it enforces; how a new agent joins.', body, kind='site')
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
    page('admin/briefs/index.html', 'Briefs', 'The build briefs for this site, published in full before the work, newest first.', body, kind='site')
    v = A['evidence_vault']; vt = D['vault']
    body = f"""
<h1>The evidence vault, opened</h1>
<p class="crumb"><a href="../../vaults/index.html">Vaults</a> / The evidence vault</p>
<p class="lead">The vault behind every claim on this site, {vt["sources"]} sources and {vt["captures"]} captures at commit <code>{E(vt["head"]["commit"] or "")}</code>, opens read-only in the browser with the key below, the way every published vault on sgit.ai and the newsroom does. The key is a read key: derived one way from the vault key, it decrypts and cannot write, and there is no privilege inside it to escalate. It is published on purpose, so treat it as you would the content.</p>
<p class="kv"><b>Read key</b> <code>{E(v["read_key"])}</code></p>
<p><a class="door" href="{U(v["open_url"])}" rel="noopener"><b>Open the vault in the browser &rarr;</b><span>dev.vault.sgraph.ai decrypts it in your tab; the server that stores it cannot read it</span></a></p>
<pre>$ sgit clone {E(v["read_key"])}</pre>
<p class="caveat">{E(v["note"])}</p>
{vault_live(v["read_key"], True, 2, 'The vault opens in its own app first: sources, captures, claims, the timeline, memos and notes, read from the vault as it is now. The vault browser is under it.')}
<h2>What is in it</h2>
<ul>
<li><code>sources/&lt;slug&gt;/</code>: one folder per source, with <code>source.json</code>, <code>notes.md</code>, dated <code>captures/</code> (page, rendered page, text, screenshot, headers, provenance with hashes) and <code>raw/</code> with <code>SHA256SUMS</code>.</li>
<li><code>claims/&lt;agent&gt;.json</code> and <code>timeline/&lt;agent&gt;.json</code>: one file per agent.</li>
<li><code>memos/</code>: the editor's voice memos; <code>notes/</code>: agents' working notes; <code>tools/</code>: the capture tool and the index builder.</li>
</ul>
<p>The manifest this site is built from, with every hash, is <a href="../../data/sources.json">data/sources.json</a>; the sources are listed on <a href="../../sources/index.html">every source</a>. The telemetry vault (<code>{E(A["telemetry_vault"]["id"])}</code>) is separate and private: {E(A["telemetry_vault"]["note"])}</p>
"""
    page('admin/vault/index.html', 'The evidence vault, opened', 'The read key to the evidence vault behind this site, the link that opens it in the browser, and what is in it.', body, kind='site')
    t = D['telemetry']; rep = TREP
    def tt(pairs, h):
        return table([h, 'Events'], [[E(str(k)), E(str(n))] for k, n in pairs]) if pairs else '<p class="small">Nothing yet.</p>'
    repo_html = '<p class="small">No report has been drained yet.</p>' if not rep else f"""
<p>Report as of <b>{E(rep["as_of"])}</b>: <b>{rep["events"]}</b> events from <b>{rep["sessions"]}</b> sessions ({rep["test_or_undecryptable"]} test or undecryptable rows excluded). {E(rep["note"])}</p>
<div class="cols">{tt(rep["by_country"], "Country")}{tt(rep["by_region"], "Region")}{tt(rep["by_referrer"], "Referrer host")}{tt(rep["by_screen"], "Screen")}</div>
<h3>By page</h3>{tt(rep["by_path"], "Page")}
<h3>By day</h3>{tt(rep["by_day"], "Day")}"""
    public_html = telemetry_public_html()
    body = f"""
<h1>Who reads this site</h1>
<p class="lead">Every page sends one anonymous event to a write-only lane on a separate, private vault: which page, the referrer's host, the visitor's country, region and city from a geolocation lookup, language, screen class and time zone, with a random session id that lives in the tab. No IP address, no cookie, no name, no user-agent string; since v0.8.4, whether the browser is automated (by class: a crawler's name, webdriver, headless) and, if this browser holds a key from <a href="../../join/index.html">/join/</a> or was set below, its role (editor, team, power user), never who. The event is encrypted in your browser to the key below before it leaves; the lane's reply is a blind <code>{{"ok": true}}</code>. Do Not Track and Global Privacy Control switch it off. The brief is on <a href="../briefs/index.html#2026-10-22__telemetry-over-an-append-lane">briefs</a>.</p>
<h2>What this page carries</h2>
<p>{E(t["what"])}</p>
<p class="kv"><b>Lane</b> vault <code>{E(t["vault_id"])}</code> on <code>{E(t["endpoint"])}</code> &middot; <b>append token</b> <code>{E(t["append_token"])}</code> (write-only; publishable by design) &middot; <b>encrypted to</b> <code>{E(t["recipient"]["fingerprint"])}</code></p>
<pre>{E(t["recipient"]["encrypt"])}</pre>
<p>The geolocation lookup goes to {" then ".join(f"<code>{E(u)}</code>" for u in t["geo"])}; that service sees your IP address and returns a country, a region and a city; the event keeps the three names and nothing else. The vault server sees that a lane received something, its size and the time, and the requesting IP, as any server does.</p>
<h2>Who is who</h2>
{public_html}
<h2>Every event, every group</h2>
<p class="small">The drainer's own report, over every event: readers, the editor and power users, agents and crawlers together.</p>
{repo_html}
<h2>What the counts are worth</h2>
<ul>
<li>Every row is an untrusted claim: the token and the public key are on this page, so anyone can add rows or flood the lane (1000 pending per token, then the lane returns 507).</li>
<li>The counts are a floor: visitors with blockers, Do Not Track or Global Privacy Control do not appear.</li>
<li>Nobody can be identified from them, by design, and no row leaves the vault; the drainer publishes counts.</li>
</ul>
<p>Mechanics: <code>assets/telemetry.js</code> sends; <code>admin/build/telemetry_drain.py</code>, run by whoever holds the telemetry vault key, lists the lane with the enum key, fetches, decrypts with the private key, marks processed and writes <code>reports/</code>; <code>data/telemetry-report.json</code> is the latest report, copied into this repository at each drain. The same drain runs in the browser: open the telemetry vault with its vault key and its Queue &amp; drain page shows what waits in the lane and drains it, with the same steps and the same files, publishing the commit before it marks anything processed.</p>
"""
    page('admin/telemetry/index.html', 'Who reads this site: anonymous telemetry over an append lane', 'What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.', body, kind='site')
    if SYN: build_synthetic()


def build_synthetic():
    # data/synthetic.json is written by admin/synthetic/run.py summarise from each reader's vault; this page only shows it
    def txt(x): return E(str(x or '').replace('\u2014', ', '))
    def pg(x):
        x = (x or '').split('#')[0].strip('` ')
        return f'<a href="../../{E(x)}">{E(x)}</a>' if x and os.path.isfile(os.path.join(ROOT, x)) else f'<code>{txt(x)}</code>'
    P = SYN['personas']
    def score(l, k): return str(l.get('scores', {}).get(k, '')) if l.get('reviewed') else ''
    rows = [[f'<a href="#{E(p["id"])}">{E(p["name"])}</a>', f'{p["device"]["width"]}&times;{p["device"]["height"]}, {E(p["color_scheme"] or "")}', E(p['latest'].get('run', 'not yet')), 'v' + E(p['latest'].get('site_version', '')), E(p['latest'].get('answered_question', '')),
             *[score(p['latest'], k) for k in ('answered', 'clarity', 'trust', 'design', 'navigation')], f'<code>{E(p["vault_id"] or "")}</code>', str(p['runs'])] for p in P]
    cards = []
    for p in P:
        l = p['latest']
        fails = ''.join(f'<li><b>{txt(x["severity"])}</b> {txt(x["point"])} ({pg(x["page"])}): {txt(x["evidence"])}</li>' for x in l.get('top_fails', []))
        changes = ''.join(f'<li>{txt(c["change"])} ({pg(c["page"])}, {txt(c["effort"])}): {txt(c["why"])}</li>' for c in l.get('top_changes', []))
        ck = l.get('checks', {})
        cards.append(f"""<section id="{E(p["id"])}"><h2>{E(p["name"])}</h2>
<p>{txt(p["who"])} <b>Question:</b> {txt(p["question"])}</p>
{f'<blockquote>{txt(l["verdict"])}</blockquote>' if l.get("verdict") else '<p class="small">Captured, not yet reviewed.</p>'}
<p class="kv"><b>Run</b> {E(l.get("run", ""))} on v{E(l.get("site_version", ""))} &middot; <b>pages</b> {l.get("totals", {}).get("pages", 0)} &middot; <b>requests</b> {l.get("totals", {}).get("requests", 0)} &middot; <b>instrument flags</b> {ck.get("high", 0)} high, {ck.get("medium", 0)} medium, {ck.get("low", 0)} low &middot; <b>vault</b> <code>{E(p["vault_id"] or "")}</code></p>
{f'<h3>What did not work</h3><ul>{fails}</ul>' if fails else ''}{f'<h3>What this reader would change first</h3><ol>{changes}</ol>' if changes else ''}</section>""")
    body = f"""
<h1>Synthetic readers</h1>
<p class="lead">Six test readers, run by the agent synthetic@php.newsroom: a board member, a CTO, a project manager, a security lead, a developer and a designer. Each reads the live site in a real browser on its own device, follows its own reading path and the links that interest it, and then says, in its own voice, whether it got its answer, what worked, what did not and what it would change. Every request, page, screenshot and review goes into that reader's own private vault.</p>
<p class="caveat">A synthetic reader is a test instrument, not a reader. Its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. It sends no telemetry: the site's telemetry lane and geolocation lookups are answered locally during a run.</p>
{section("now", "The latest run", table(['Reader', 'Device', 'Run (UTC)', 'Site', 'Answered', 'Ans.', 'Clarity', 'Trust', 'Design', 'Nav.', 'Vault', 'Runs'], rows), 'Scores are 0 to 5 from that reader\'s point of view.')}
{''.join(cards)}
{section("how", "How a run works", '''<ol>
<li><b>Check.</b> <code>admin/synthetic/run.py capture --if-changed</code> reads <code>status.json</code> and the front page. If the version, the data and the front page are what the last run saw, the reader writes a heartbeat line and stops.</li>
<li><b>Read.</b> Chromium opens the front page with the reader's viewport, device scale, touch and colour scheme, then the reader's path from <code>admin/synthetic/personas.json</code>, then the links whose words match the reader's interests, up to its page budget. The designer also reads every page on a phone, a tablet and in dark mode; the developer also fetches <code>llms.txt</code>, <code>status.json</code> and a markdown twin as a tool would.</li>
<li><b>Measure.</b> For each page: the served and the rendered HTML, the text, the first screen and the full page as images, headings, words, screens of scrolling, reading ease, glossary terms per thousand words, contrast against WCAG AA, tap targets under 24px, text under 12px, horizontal overflow, images without alt text, timings. Every request with its status, size, timing and sha256; every console message.</li>
<li><b>Review.</b> The reader is given its journey, the measurements, the first screen of every page and the full text, with <code>admin/synthetic/review-guide.md</code>, and answers as structured JSON: a verdict, whether the question was answered, five scores, what works, what fails with evidence, what to change, the lines it reacted to, and what changed since its last run. The review is written by the Claude API when the run has a key, or by an agent session.</li>
<li><b>Keep.</b> All of it is committed and pushed to the reader's vault; <code>run.py summarise</code> writes this page's data, <code>data/synthetic.json</code>, with no keys in it.</li>
</ol>''')}
{section("vaults", "The vaults", '<p>One private vault per reader, ids in the table above. Each holds <code>README.md</code> (the reader), <code>latest.json</code>, <code>history.jsonl</code>, <code>heartbeats.jsonl</code> and <code>runs/&lt;run&gt;/</code> with <code>run.json</code>, <code>requests.jsonl</code>, <code>console.jsonl</code>, <code>pages/</code>, <code>review-request.md</code>, <code>feedback.json</code> and <code>feedback.md</code>. The vault keys are held by the editor and the agent that runs the readers; none is in this repository.</p>')}
"""
    page('admin/synthetic/index.html', 'Synthetic readers: six test readers who read the live site every hour', 'A board member, a CTO, a project manager, a security lead, a developer and a designer read the live site in a real browser and say what works, what does not and what to change; every run is kept in that reader\'s own vault.', body, kind='site')


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
        fl = ''.join(f'<li><a href="{U(f.get("url"))}" rel="noopener nofollow"><code>{E(f["name"][5:])}</code></a> <span class="small">+{f.get("add", 0)} / -{f.get("dele", 0)}</span></li>' for f in files)
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


# ----------------------------------------------------------------------------- articles and layers (v0.2.6)

def article_inline(s, depth):
    """Inline markdown for articles: [[slug, slug]] citations, [text](/site/path) links, `code`, bold, italic."""
    s = E(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\[\[([^\]]+)\]\]', lambda m: '<span class="refs">' + src_links([x.strip() for x in m.group(1).split(',')], depth) + '</span>', s)
    s = re.sub(r'\[([^\]]+)\]\(/([^)]*)\)', lambda m: f'<a href="{"../" * depth}{E(m.group(2))}">{m.group(1)}</a>' if re.fullmatch(r'[A-Za-z0-9/._#-]*', m.group(2)) else m.group(0), s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s"<>]+)\)', r'<a href="\2" rel="noopener">\1</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', s)
    return s

def render_article(text, depth):
    out, lst, rows = [], None, []
    def flush():
        if rows:
            out.append(table([article_inline(c, depth) for c in rows[0]], [[article_inline(c, depth) for c in r] for r in rows[1:]])); rows.clear()
    for line in text.splitlines():
        if line.strip().startswith('|'):
            if lst:
                out.append(f'</{lst}>'); lst = None
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if not all(re.match(r'^:?-+:?$', c) for c in cells):
                rows.append(cells)
            continue
        flush()
        m = re.match(r'^(#{2,4})\s+(.*)$', line)
        item = re.match(r'^(?:-|\d+\.)\s+(.*)$', line)
        kind = ('ol' if re.match(r'^\d+\.', line) else 'ul') if item else None
        if lst and kind != lst:
            out.append(f'</{lst}>'); lst = None
        if m:
            out.append(f'<h{len(m.group(1))}>{article_inline(m.group(2), depth)}</h{len(m.group(1))}>')
        elif item:
            if not lst:
                out.append(f'<{kind}>'); lst = kind
            out.append(f'<li>{article_inline(item.group(1), depth)}</li>')
        elif line.strip():
            out.append(f'<p>{article_inline(line, depth)}</p>')
    flush()
    if lst:
        out.append(f'</{lst}>')
    return '\n'.join(out)

def article_stamp(a):
    return f'site v{E(a["as_of_version"])} &middot; vault commit <code>{E(a["vault_commit"])}</code> &middot; data as of {E(a["data_as_of"])}'

def stories_row():
    cards = ''.join(f'<a class="door" href="articles/{E(a["slug"])}/index.html"><b>{E(a["title"])}</b><span>{E(ORIGINS[a["origin"]]["short"])} story &middot; {E(AUTHOR_ROLES.get(a["role"], a["role"]))} &middot; {E(a["written"])}</span></a>' for a in ARTICLES[:3])
    cards += f'<a class="door" href="interview/index.html"><b>{E(D["interview"]["title"])}</b><span>Interview &middot; the editor, in his own words</span></a>'
    return f'<div class="doors">{cards}</div><p><a href="articles/index.html">All stories &rarr;</a></p>'

def articles_row():
    if not ARTICLES:
        return ''
    cards = ''.join(f'<a class="door" href="articles/{E(a["slug"])}/index.html"><b>{E(a["title"])}</b><span>{E(AUTHOR_ROLES.get(a["role"], a["role"]))} &middot; {E(a["written"])} &middot; written against v{E(a["as_of_version"])}</span></a>' for a in ARTICLES[:4])
    return section('articles', 'Articles, signed and dated', f'<div class="doors">{cards}</div><p><a href="articles/index.html">All articles &rarr;</a> The pages of this site are rebuilt from the vault on every release; an article is written once, against the evidence as it stood, and says which version that was.</p>')

def build_articles():
    for a in ARTICLES:
        role = AUTHOR_ROLES.get(a['role'], a['role'])
        moved = '' if a['data_as_of'] >= STORY['data_as_of'] else f'<p class="caveat"><b>The evidence has moved since this was written.</b> This article was written against data as of {E(a["data_as_of"])}; the site now has data as of {E(STORY["data_as_of"])}. The <a href="../../index.html">front page</a> and <a href="../../claims/index.html">every claim</a> are current; this article is kept as written.</p>'
        others = ''.join(f'<li><a href="../{E(b["slug"])}/index.html">{E(b["title"])}</a> <span class="small">{E(AUTHOR_ROLES.get(b["role"], b["role"]))}, {E(b["written"])}</span></li>' for b in ARTICLES if b is not a)
        cited = section("cited", "Sources cited", f'<p>{len(a["cites"])} captured sources, in the order this article first cites them. Each opens on its page with its capture times and hashes.</p><p class="refs">{src_links(a["cites"], 2)}</p>')
        more = section("more", "Other articles", f'<ul>{others}</ul>') if others else ''
        body = f"""
<article class="piece">
<p class="kicker">Story &middot; {E(ORIGINS[a["origin"]]["short"])} &middot; {E(role)} &middot; {E(a["written"])}</p>
<h1>{E(a["title"])}</h1>
<p class="lead">{E(a["dek"])}</p>
<p class="kv"><b>By</b> the {E(role.lower())} {"roles, agents" if "," in a["author"] else "role, agent"} <code>{E(a["author"])}</code> &middot; <b>written against</b> {article_stamp(a)}</p>
{moved}
{render_article(a["text"], 2)}
</article>
{cited}
{more}
<p class="small">Source file: <code>admin/content/articles/{E(a["file"])}</code>, in the authored layer; see <a href="../../layers/index.html">evidence, derived, authored</a>.</p>
"""
        page(f'articles/{a["slug"]}/index.html', a['title'], a['dek'], body, kind='article', date=a['written'], topics=f'php2shell {a["role"]}', ld_type='NewsArticle', origin=a['origin'], byline=f'By the {role.lower()} {"roles, agents" if "," in a["author"] else "role, agent"} {a["author"]}')
    def card(a):
        return f'<article class="rel">{it_story(a)}<h3><a href="{E(a["slug"])}/index.html">{E(a["title"])}</a></h3><p>{E(a["dek"])}</p><p class="small">{E(ORIGINS[a["origin"]]["short"])} &middot; {E(AUTHOR_ROLES.get(a["role"], a["role"]))} &middot; {E(a["written"])} &middot; <code>{E(a["author"])}</code> &middot; {article_stamp(a)} &middot; {len(a["cites"])} sources cited</p></article>'
    house = ''.join(card(a) for a in ARTICLES if a['origin'] == 'house')
    guests = ''.join(card(a) for a in ARTICLES if a['origin'] == 'guest') or '<p>None yet. A guest writer or interviewer sends a piece to the editor; it is published here under their own name, marked <b>Guest</b> on every page, with the same rule as everything else: a fact names its source. Opinion is theirs and says so.</p>'
    iv = D['interview']
    interviews = ''.join(card(a) for a in ARTICLES if a['origin'] == 'interview') + f'<article class="rel"><h3><a href="../interview/index.html">{E(iv["title"])}</a></h3><p>{E(iv["description"])}</p><p class="small">Interview &middot; the editor\'s own words, quoted verbatim</p></article>'
    body = f"""
<h1>Stories: written here</h1>
<p class="lead">This site has two halves. <b>Research</b> is material collected from outside (agencies, researchers, vendors, the press, other models, other websites) and what this site derives from it: claims with a status, the timeline, the numbers. It is rebuilt from the evidence on every release. <b>Stories</b> are written here: reporting, analysis, opinion and interviews, each signed and dated, and kept as written. A story says which version of the evidence it was written against, so a reader can see what was known when.</p>
<p>Every page on the site says at its top which half it belongs to. In a story, a fact still carries its source; a judgement is the writer's, and says so.</p>
{section("house", "House stories", f'<p>Written by this site\'s own roles: the <b>journalist</b> reports and follows the second stories; the <b>historian</b> sets events against what came before.</p>{house}')}
{section("interviews", "Interviews", interviews)}
{section("guests", "Guest writers and interviewers", guests)}
"""
    page('articles/index.html', 'Stories: written here, signed and dated', f'{len(ARTICLES)} stories about the PHP flaws written for this site, plus the editor\'s interview: house stories by the journalist and historian, interviews, and guest pieces, each pinned to the evidence it was written against.', body, kind='site')

def build_layers():
    L = D['layers']
    names = {l['id']: l['name'] for l in L['layers']}
    def link(f):
        u = f.get('used_on')
        return f'<a href="../{E(u)}">{E(u)}</a>' if u else ''
    out = ''
    for l in L['layers']:
        rows = [[f'<code>{E(f["path"])}</code>', E(f['by']), E(f['from']), link(f)] for f in L['files'] if f['layer'] == l['id']]
        out += section('l-' + l['id'], l['name'], table(['File', 'Made by', 'From', 'Shown on'], rows), f'{E(l["what"])} <b>Rule.</b> {E(l["rule"])}')
    counts = Counter(f['layer'] for f in L['files'])
    tally = ' &middot; '.join(f'<b>{counts[l["id"]]}</b> {E(names[l["id"]].lower())}' for l in L['layers'])
    body = f"""
<h1>Evidence, derived, authored</h1>
<p class="lead">This site mixes kinds of material, and a reader should always be able to tell which one they are looking at. {E(L["note"])}</p>
<p class="kv">{tally}</p>
<ul>
<li><b>Evidence</b> answers <i>what was captured?</i> The pages that show it are <a href="../sources/index.html">every source</a>, <a href="../affected/software.html">the software inventory</a> and <a href="../admin/vault/index.html">the vault, opened</a>.</li>
<li><b>Derived</b> answers <i>what does the evidence say?</i> The story pages and the analysis (<a href="../claims/index.html">claims</a>, <a href="../numbers/index.html">numbers</a>, <a href="../agencies/index.html">agencies</a>) are built from it, and change when it changes.</li>
<li><b>Authored</b> answers <i>what did someone conclude, and when?</i> <a href="../articles/index.html">Articles</a> and <a href="../brief/index.html">the brief</a> are signed and dated.</li>
</ul>
{out}
<p>The classification is <a href="../data/layers.json">data/layers.json</a>; the gate fails a release if a file in <code>data/</code> is missing from it.</p>
"""
    page('layers/index.html', 'Evidence, derived, authored: what each file is', 'Every file this site is built from, sorted into evidence captured from the vault, transformations derived by agents, signed and dated articles, and the files that run the site.', body, kind='site')


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
    rows = [[f'{it_question(q)}<a href="{E(q["id"])}/index.html"><b>{E(q["q"])}</b></a>', E(q['short']), ' '.join(q_link(p, 1) for p in q['see'][:3])] for q in qs]
    seen = table(['Seen', 'What', 'State', 'Answered by'], [[E(x['seen']), f'<b>{E(x["publisher"])}</b>: <a href="{U(x["url"])}" rel="noopener nofollow">{E(x["title"])}</a><div class="note">{E(x["standfirst"])}</div>', E(x['state']), '<br>'.join(f'<a href="{E(a)}/index.html">{E(next(q["q"] for q in qs if q["id"] == a))}</a>' for a in x['answered_by'])] for x in Q['seen']])
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


# ----------------------------------------------------------------------------- second readings: other models, checked against the vault (v0.2.10)

def build_readings():
    R = D['readings']
    verdicts = {v['id']: v for v in R['verdicts']}
    claim_ids = {c['id'] for c in D['claims']}
    out = ''
    for r in R['readings']:
        tally = Counter(x['verdict'] for x in r['rows'])
        rows = [[f'<b>{E(x["point"])}</b><div class="note">section {E(x["section"])}</div>', E(x['found']), pill(verdicts[x['verdict']]['name']),
                 E(x['vault']) + ('<div class="note">' + ', '.join(f'<a href="../claims/index.html#{E(c)}">{E(c)}</a>' for c in x['claims'] if c in claim_ids) + '</div>' if x['claims'] else ''),
                 src_links(x['sources'], 1)] for x in r['rows']]
        leads = ''.join(f'<li><a href="{U(l["url"])}" rel="noopener nofollow">{E(l["what"])}</a> <span class="small">{E(l["priority"])}</span></li>' for l in r['leads'])
        out += section(r['id'], f'{E(r["model"])}: {E(r["title"])}', f'''<p>{E(r["how"])} <a href="{E(r["id"])}/index.html">The notes in full &rarr;</a></p>
<p class="kv">{" &middot; ".join(f"<b>{tally[v['id']]}</b> {E(v['name'])}" for v in R["verdicts"] if tally[v["id"]])}</p>
{table(["Point", f"What {E(r['model'])} found", "Against the vault", "What the vault holds", "Sources"], rows, "claims")}
<h3>Sources {E(r["model"])} named that the vault has not captured</h3>
<p>Listed for the collectors, in the order they should be captured. None is cited on this site until it is captured; this list is the whole of what they are used for.</p>
<ul>{leads}</ul>''')
        notes = render_md_file(r['file'])
        body = f'''
<p class="kicker">Second reading &middot; by {E(r["model"])} &middot; compiled {E(r["compiled"])}</p>
<div class="caveat"><p><b>This page is {E(r["model"])}'s text, not this site's.</b> {E(r["how"])} It is published in full and unedited, credited to {E(r["model"])}, from <code>{E(r["file"])}</code>. Its links go to the open web; none of its sources is cited by this site until a collector has captured it. Where it agrees or disagrees with the evidence vault is on <a href="../index.html#{E(r["id"])}">second readings</a>.</p></div>
<div class="memo">{notes}</div>
'''
        page(f'readings/{r["id"]}/index.html', f'{r["model"]}\'s notes on php2shell, in full', f'{r["title"]}: the notes {r["model"]} compiled on {r["compiled"]}, published in full and credited, with the comparison against the evidence vault one page up.', body, kind='evidence', topics=f'php2shell {r["model"].lower()} second reading')
    legend = '<ul class="legend">' + ''.join(f'<li>{pill(v["name"])} {E(v["what"])}</li>' for v in R['verdicts']) + '</ul>'
    body = f'''
<h1>Second readings: other models, checked against the vault</h1>
<p class="lead">The editor's first memo asked for more than one model to read this story. The vault was read by Claude agents; this page sets readings by other models beside it, point by point. Each other model's text is published in full and credited, and nothing in it is cited on this site until a collector has captured its source.</p>
{legend}
{out}
<p class="small">The comparison rows are <a href="../data/readings.json">data/readings.json</a>, in the derived layer; the other models' text is in the authored layer (<a href="../layers/index.html">evidence, derived, authored</a>). The gate checks every source and claim a row cites.</p>
'''
    page('readings/index.html', 'Second readings: other models, checked against the vault', 'Another model\'s notes on php2shell, published in full and credited, set beside the evidence vault point by point: where they agree, where the vault resolves or goes further, and the new leads for capture.', body, kind='analysis', topics='php2shell second reading models')


# ----------------------------------------------------------------------------- the pipeline (v0.2.12)

def build_status():
    P = D['pipeline']
    cfg = J({'api': P['api'], 'sites': P['sites']}, sort_keys=True, separators=(',', ':'))
    cards = ''.join(f"""
<section id="{E(x["id"])}" class="pl-site">
<h2><a href="{E(x["site"])}">{E(x["name"])}</a></h2>
<p class="kv"><a href="https://github.com/{E(x["repo"])}/actions/workflows/{E(x["workflow"])}"><span class="pl-badge" data-badge="https://github.com/{E(x["repo"])}/actions/workflows/{E(x["workflow"])}/badge.svg?branch={E(x["branch"])}">the deploy workflow's runs on GitHub</span></a> &middot; repository <a href="https://github.com/{E(x["repo"])}"><code>{E(x["repo"])}</code></a> &middot; branch <code>{E(x["branch"])}</code> &middot; served version <a href="{E(x["site"])}VERSION"><code>{E(x["site"])}VERSION</code></a></p>
<div id="pl-{E(x["id"])}"><div class="pl-live"><p class="small">Reading GitHub&hellip; (this part and the badge need JavaScript; the links above do not)</p></div></div>
</section>""" for x in P['sites'])
    body = f"""
<h1>The pipeline: what is live, what is deploying</h1>
<p class="lead">Several agents release to these sites. Each push to <code>dev</code> starts a GitHub Actions run that runs the gate and deploys to GitHub Pages. This page reads those runs from GitHub's public API in your browser, with no credential anywhere: the repositories are public, and so is everything below. Beside each site's runs is the version that site serves now, read from its own <code>VERSION</code> file.</p>
<p><button id="pl-refresh" type="button">Refresh now</button> <span id="pl-rate" class="small"></span></p>
{cards}
<h2>How to read it</h2>
<ul>
<li><span class="st st-confirmed">deployed</span> the run passed the gate and published its commit. The row marked <b>&#9664; live</b> is the version the site serves.</li>
<li><span class="st st-reported">deploying</span> <span class="st st-reported">queued</span> in the pipeline now. Deploys never cut each other off: a started deploy finishes, then the newest waiting push goes.</li>
<li><span class="st">superseded</span> GitHub keeps one waiting run per site; a push overtaken while it waited is cancelled, and the newer run behind it ships its commit too. Nothing is lost.</li>
<li><span class="st st-failed">failed</span> the gate or the deploy failed; the site keeps serving the last good release. <span class="st st-unverified">cancelled</span> cancelled with nothing newer behind it: the next push or a re-run deploys.</li>
</ul>
<p>Every page of this site also checks, once, whether the site now serves a newer release than the page in front of you, and says so beside the version in the bar.</p>
<h2>What it costs and what it shows</h2>
<p>{E(P["about"])} GitHub allows {E(P["anonymous_limit"])}; this page spends one call per site per refresh: every five minutes, every twenty seconds for a site with a run in flight, and none while the tab is hidden. The badges are images GitHub serves, loaded by the same script, and do not count. Commit messages, run numbers and the agent named in a commit's <code>Agent:</code> line are public on GitHub already; this page shows them, and sends nothing anywhere else.</p>
<p>For agents: <code>admin/build/release.sh "&lt;what changed and why&gt;"</code> takes in whatever other agents released before it bumps, and if its push loses a race it takes that in too and releases again on top, so two agents can release minutes apart without either push being rejected or either deploy being lost. The list of the sites read here is <a href="../data/pipeline.json">data/pipeline.json</a>.</p>
<script type="application/json" id="pipeline-config">{cfg}</script>
<script src="../assets/pipeline.js" defer></script>
"""
    page('status/index.html', 'The pipeline: what is live, what is deploying', 'Each newsroom site\'s deploy runs, read in your browser from GitHub\'s public API with no credential, beside the version the site serves now: what is live, what is deploying, what was superseded, what failed.', body, kind='site')


# ----------------------------------------------------------------------------- the vaults (v0.2.13)

def vault_open_url(read_key):
    """The official UI's read-only link for a published read key: the key travels in the fragment, never to a server."""
    rk, vid = read_key.rsplit(':', 1)
    return f'https://dev.vault.sgraph.ai/en-gb/#{rk}%3A{vid}'

def vault_note(read_key):
    """The note box every published vault gets on sgit.ai: the key, the link that opens it, the clone command."""
    return f"""<div class="vnote"><b>Open it yourself. The read key is the whole credential, and it is published on purpose.</b><br>
Read key: <code>{E(read_key)}</code><br>
In the official UI: <a href="{E(vault_open_url(read_key))}" rel="noopener" target="_blank">open it read-only in a new tab &#8599;</a> &middot; From the command line: <code>sgit clone {E(read_key)}</code><br>
<span class="small">A read key decrypts and cannot write; it is derived one way from the vault key, which is not published and never will be.</span></div>"""

def vault_live(read_key, app, depth, lead):
    """The embedded vault: the official SG/Vault UI in a frame, handed the read key over postMessage (assets/vendor/vault-ui-embed.js)."""
    rk, vid = read_key.rsplit(':', 1)
    up = '../' * depth
    return f"""<h2>See it live, here</h2>
<p class="openrow"><a class="btn-open" href="{E(vault_open_url(read_key))}" rel="noopener" target="_blank">Open the vault in a new tab &#8599;</a> <span class="small">{lead}</span></p>
<div class="sgv-uiembed" data-vault="{E(vid)}" data-readkey="{E(rk.replace("sgit_public_read_", ""))}" data-app="{1 if app else 0}"></div>
<script src="{up}assets/vendor/vault-ui-embed.js" defer></script>"""

def build_vaults():
    VS = D['vaults']['vaults']; W = D['source-watch']; ev = D['admin']['evidence_vault']; vt = D['vault']; tl = D['telemetry']
    keys = {'evidence': ev['read_key'], 'source-watch': W['read_key']}
    facts = {'evidence': f'{vt["sources"]} sources, {vt["captures"]} captures, {vt["hashed_files"]} hashed files; head <code>{E(vt["head"]["commit"] or "")}</code>',
             'source-watch': f'{W["pages"]} pages from {W["publishers"]} publishers in {len(W["country"])} countries and {len(W["lang"])} languages; {W["snapshots"]} snapshots, {len(W["runs"])} runs; head <code>{E(W["head"]["commit"])}</code>',
             'telemetry': f'lane <code>{E(tl["vault_id"])}</code> on <code>{E(tl["endpoint"])}</code>; events encrypted to <code>{E(tl["recipient"]["fingerprint"])}</code>',
             'subscriptions': f'lane <code>{E(D["subscriptions"]["vault_id"])}</code> on <code>{E(D["subscriptions"]["endpoint"])}</code>; requests encrypted to <code>{E(D["subscriptions"]["recipient"]["fingerprint"])}</code>'}
    lanes = {'telemetry': tl['append_token'], 'subscriptions': D['subscriptions']['append_token'], 'collaborators': load('collaborators')['lane']['append_token']}
    cards = ''
    for x in VS:
        k = keys.get(x['slug']) or x.get('read_key')
        how = (f'<p class="kv"><b>Not published:</b> the vault key. {E(x.get("note", ""))}</p>' if not k and x['slug'] not in lanes else f'<p class="kv"><b>Read key</b> <code>{E(k)}</code></p><p><a href="{E(vault_open_url(k))}" rel="noopener" target="_blank">Open read-only in a new tab &#8599;</a> &middot; <code>sgit clone {E(k)}</code></p>' if k else
               f'<p class="kv"><b>Not published:</b> the vault key, the lane\'s enum key and the key pair\'s passphrase. <b>Published:</b> the write-only append token <code>{E(lanes.get(x["slug"], ""))}</code>, which adds rows and reads nothing.</p>')
        cards += f"""<section class="vcard" id="{E(x["slug"])}">
<h2><a href="../{E(x["page"])}">{E(x["name"])}</a> <span class="st {'st-confirmed' if k else ''}">{E(x["access"])}</span></h2>
<p class="kv"><b>Vault</b> <code>{E(x["id"])}</code> &middot; {facts.get(x["slug"], E(x.get("facts", "")))}{' &middot; opens in its own app' if x["app"] else ''}</p>
<p>{E(x["holds"])}</p>
<p class="small"><b>Written by</b> {E(x["writers"])}. Data on this site: <a href="../{E(x["data"])}">{E(x["data"])}</a>.</p>
{how}
</section>"""
    body = f"""
<h1>The vaults behind this site</h1>
<p class="lead">This site is rebuilt from vaults, never written by hand. {len(VS)} vaults sit behind it. Three are public and open read-only in your browser with the keys below (the evidence, the source watch, and the public face of the telemetry, its curated counts); two are private and receive through write-only lanes, one the site's anonymous telemetry, one subscription requests; one is private and is an application only, the telemetry app, versioned in its own vault, which the telemetry vault links inside itself and opens as its dashboard (an earlier dashboard vault, linked the other way round, is superseded); one is private and never published, because it holds other people's pages; and three are the team's own, private, through which <a href="../team/channels/index.html">the team talks</a>: the conductor vault, the issues and the mail. Every vault is encrypted in the client; the server that stores it holds ciphertext and nothing else.</p>
<div class="caveat"><p>{E(D["vaults"]["about"])}</p></div>
{cards}
<p class="small">The list is <a href="../data/vaults.json">data/vaults.json</a>. The other vaults of the sgit.ai network, published the same way, are at <a href="https://sgit.ai/demos/vaults/index.html">sgit.ai's vaults</a>.</p>
"""
    page('vaults/index.html', 'The vaults behind this site', 'Every vault this site is built from: the evidence vault and the source watch, both public with their read keys, and the private telemetry vault with its write-only lane; what each holds, who writes to it and how to open it.', body, kind='site')

    # the source watch, published the way sgit.ai publishes a vault
    acc = {a['id']: a['means'] for a in W['access_classes']}
    sect = {x['id']: x['name'] for x in W['sectors']}
    stats = ''.join(stat(n, l) for n, l in [(W['pages'], 'pages watched'), (W['publishers'], 'publishers'), (len(W['country']), 'countries'), (len(W['lang']), 'languages'),
                                            (W['snapshots'], 'snapshots kept'), (W['graphs'], 'graphs'), (len(W['runs']), 'runs'), (W['files'], 'files in the vault')])
    top_c = table(['Country', 'Pages'], [[f'<code>{E(c)}</code>', str(n)] for c, n in sorted(W['country'].items(), key=lambda kv: (-kv[1], kv[0]))[:12]])
    top_s = table(['Sector', 'Pages'], [[f'<code>{E(c)}</code> {E(sect.get(c, ""))}', str(n)] for c, n in sorted(W['sector'].items(), key=lambda kv: (-kv[1], kv[0]))])
    acc_t = table(['Access', 'Pages', 'Means'], [[pill(k) if k in STATUS_WORDS else f'<code>{E(k)}</code>', str(W['access'].get(k, 0)), E(m)] for k, m in acc.items()])
    tiers = {'A': 'open or public-sector: keep and show', 'B': 'quote up to 25 words and link', 'C': 'link only'}
    tier_t = table(['Tier', 'Publishers', 'What a site page may show'], [[f'<b>{t}</b>', str(W['tiers'].get(t, 0)), E(w)] for t, w in tiers.items()])
    alt_t = table(['Altitude', 'What it describes'], [[f'<b>{E(k)}</b>', E(v if isinstance(v, str) else json.dumps(v))] for k, v in W['altitudes'].items()])
    runs_t = table(['Run (UTC)', 'Due', 'Watched', 'Changed', 'Access'], [[f'<code>{E(r["run"])}</code>', str(r['pages_due']), str(r['pages_total']), str(r['changed']),
                    ', '.join(f'{E(k)} {n}' for k, n in sorted((r.get('access') or {}).items(), key=lambda kv: -kv[1]))] for r in reversed(W['runs'])])
    tips = ''.join(f"""<article class="rel"><p class="kicker">Tip {E(t["id"])} &middot; received {E(t["received"] or "")} &middot; {pill(t["status"] or "unverified")}</p>
<p>{E(t["says"] or "")}</p><p class="small"><b>Watched as</b> {", ".join(f"<code>{E(w)}</code>" for w in t["watched_as"])}. <b>To check:</b> {"; ".join(E(c) for c in t["to_check"])}.</p></article>""" for t in W['tips'])
    shot = 'assets/vaults/source-watch.png'  # captured from the official UI with the read key; the figure appears once it is in the repository
    hero = (f"""<figure class="shot"><a href="{E(vault_open_url(W["read_key"]))}" rel="noopener" target="_blank"><img src="../../{shot}" alt="The source-watch vault open in the official SG/Vault UI, read-only." width="1280" height="800" loading="eager"></a>
<figcaption>The vault in the official UI, opened read-only with the published key. <b>Click the image to open the real one &#8599;</b></figcaption></figure>""" if os.path.exists(os.path.join(ROOT, shot)) else '')
    body = f"""
<p class="crumb"><a href="../index.html">Vaults</a> / The source watch</p>
<h1>The source watch: every outside source on php2shell, watched and snapshotted</h1>
<p class="lead">A vault that does one thing. It watches every outside source on the story, {W["pages"]} pages from {W["publishers"]} publishers in {len(W["country"])} countries, and on each run records what access it had and keeps a new snapshot whenever the content changed: the text, a screenshot, the HTML as served and as rendered, the headers and the sha256 of each, and a graph of what the page says and what changed since the last look. A small, focused Wayback Machine whose diffs are graphs. Run by <b>researcher@php.newsroom</b>; public, read-only.</p>
{hero}
{vault_note(W["read_key"])}
{vault_live(W["read_key"], False, 2, f'The vault has no app of its own yet, so it opens in the vault browser. It holds {W["files"]:,} files; the browser decrypts the folder tree before it lists it, so the first open takes minutes. <code>sgit clone</code> is the fast way in.')}
<h2>What is in it</h2>
<div class="stats">{stats}</div>
<p class="small">Counts read from the vault's <code>index/counts.json</code>, <code>runs/</code> and <code>tips/</code> at head <code>{E(W["head"]["commit"])}</code> by <code>admin/build/export_watch.py</code>; no capture is copied to this site. The vault's latest commit: <q>{E(W["head"]["message"])}</q></p>

<h2>Raw and analysis are separate trees</h2>
<div class="wt-row"><div><p>Raw is what was served; analysis is what the watcher made of it, and it can be regenerated from raw plus the vocabularies plus the tools. That rule is how you tell the two apart. A snapshot in <code>raw/</code> is never edited or deleted: a new look at the page makes a new folder, and only when something changed. Every check, changed or not, is still a line in <code>checks/</code> with its status, access and hashes.</p></div>
<pre>sources/&lt;country&gt;/&lt;sector&gt;/&lt;publisher&gt;/&lt;page&gt;/page.json
raw/&lt;country&gt;/&lt;sector&gt;/&lt;publisher&gt;/&lt;page&gt;/&lt;UTC&gt;/
    text.txt  screenshot.jpg  page.html.gz  rendered.html.gz
    headers.json  meta.json  provenance.json
raw/.../&lt;page&gt;/checks/&lt;date&gt;.jsonl
graph/.../&lt;page&gt;/&lt;UTC&gt;.json   snapshot and change
runs/&lt;Y&gt;/&lt;M&gt;/&lt;D&gt;/&lt;HHMMSS&gt;/
    run.json  graph.json  changes.md
index/  state/  taxonomy/  tips/  tools/</pre></div>

<h2>Country, then sector, then publisher, then page</h2>
<p>Country is where the publisher is based (<code>eu</code> for EU institutions, <code>int</code> for publishers with no single home, such as php.net); language is a property of the page. Sector is what kind of organisation publishes it, one per publisher; it classifies the publisher, never a claim.</p>
<div class="cols">{top_c}{top_s}</div>

<h2>What we can and cannot read</h2>
<p>Every check classifies the answer it got. A page the watcher cannot read stays on the list: the challenge page's hash is the record, and the gap is published.</p>
{acc_t}
<p>Every publisher also has a licence tier, after the newsroom wires' sources policy. The vault keeps what was served either way; the tier governs what a site page shows of it.</p>
{tier_t}

<h2>Graphs: one grammar at every altitude</h2>
<p>Every graph in the vault uses the grammar in <code>taxonomy/verbs.json</code> ({W["verbs"]} verbs): an edge is a verb with a named inverse, and there is no generic association edge (<a href="https://graphs.sgit.ai/">graphs.sgit.ai</a>). The world graph alone has {W["world_graph"]["nodes"]} nodes and {W["world_graph"]["edges"]} edges. Entities (a CVE id, a PHP version, an organisation with this site's actor ids, a term with its translations) are where the altitudes join, and where the vault joins this site. What changed on a page is answered by a query over the change section, not by comparing two screenshots; the extractor is deterministic.</p>
{alt_t}

<h2>The runs</h2>
<p>A run captures the pages that are due: hourly for the story, daily for background pages about earlier incidents. Feeds and APIs are fetched without a browser; everything else goes through Chromium at 1280 wide. The first run was a diff against the evidence vault's morning captures, imported as this vault's first snapshots.</p>
{runs_t}

<h2>Tips</h2>
<p>A tip is a claim that reached the newsroom from outside, recorded with how it arrived, what it says, the pages added to watch it, and what has to be checked before anything on this site relies on it. Its status uses this site's words.</p>
{tips}

<h2>The tools</h2>
<p>The watcher is in the vault, next to what it wrote: {", ".join(f"<code>{E(t)}</code>" for t in W["tools"])}.</p>
<pre>python3 tools/watch.py run [--all] [--only &lt;text&gt;] [--limit N] [--commit] [--push]
python3 tools/discover.py scan            # feeds to candidate publishers
python3 tools/discover.py promote --limit 30
python3 tools/watch.py add &lt;url&gt; --cc gb --sector news --publisher bbc</pre>
<p class="small">The other vaults behind this site are on <a href="../index.html">the vaults</a>. The evidence vault, where the story was assembled by hand on the morning of 22 October, is <a href="../../admin/vault/index.html">opened here</a>.</p>
"""
    page('vaults/source-watch/index.html', 'The source watch: every outside source on php2shell, watched and snapshotted', f'The public source-watch vault: {W["pages"]} pages from {W["publishers"]} publishers in {len(W["country"])} countries, re-read on a schedule, a snapshot kept on every change and every snapshot a graph. Its read key, the vault embedded, and what is in it.', body, kind='evidence', topics='php2shell vault source watch')

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
    page('start/index.html', 'Who is reading? The readers of this site, mapped', f'{len(PERSONAS)} kinds of reader, from someone who has never heard of PHP to the people who maintain it, mapped by what they need to do and how technical they want it, each with a thirty-second answer and a reading path.', body, kind='site', topics='php2shell readers personas')

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
    page('explained/index.html', 'The PHP security flaws, explained from the start', 'No technical background assumed: what PHP is, what went wrong, why it is called php2shell, what the CVE numbers mean, why websites went offline, whether anyone was hacked, and what to do now.', body, kind='story', topics='php2shell explainer plain english')

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
            ext = f' &middot; <a href="{U(t["ext"])}" rel="noopener">the authority &#8599;</a>' if t.get('ext') else ''
            items += f'<article class="gterm" id="{E(t["id"])}"><h3>{E(t["term"])}</h3><p class="gshort">{E(t["short"])}</p><p>{E(t["long"])}</p><p class="small"><a href="../{E(t["more"])}">Where it matters in this story &rarr;</a>{ext}</p></article>'
        out += f'<section id="l-{E(L)}" class="gletter"><h2>{E(L)}</h2>{items}</section>'
    body = f'''
<p class="kicker">Start here &middot; {depth_badge(1)}</p>
<h1>Glossary: every term, in plain English</h1>
<p class="lead">{len(TERMS)} words this story cannot avoid, each explained for someone who has never worked in security, and each in the sense it has in this story. On every other page, the first use of each of these words is underlined and links here.</p>
<nav class="toc jump">{jump}</nav>
{out}
'''
    page('glossary/index.html', 'Glossary: every php2shell term in plain English', f'{len(TERMS)} terms from the php2shell story (PHP, CVE, CVSS, remote code execution, WAF, KEV and more), each explained in plain English, in the sense it has in this story.', body, kind='site', topics='php2shell glossary')

def build_personas_js():
    data = {'depths': {k: v['label'] for k, v in DEPTHS.items()}, 'personas': OrderedDict()}
    for p in PERSONAS.values():
        data['personas'][p['id']] = {'person': p['person'], 'label': p['label'], 'group': p['group'], 'depth': p['depth'],
                                     'path': [[x, nav_title(x), minutes(x)] for x in p['path']]}
    write('assets/personas.js', '// Generated by admin/build/build.py from data/personas.json: the readers, their paths and reading times.\nwindow.P2S = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n')



# ----------------------------------------------------------------------------- v0.3.2: every section versioned, every fact with a timeline

import difflib, hashlib

LEDGER_PATH = os.path.join(DATA, 'sections.json')
LEDGER = json.load(open(LEDGER_PATH, encoding='utf-8')) if os.path.exists(LEDGER_PATH) else {'sections': OrderedDict()}
LEDGER['note'] = ('The section ledger. Every major section of the site, every briefing and every fact is a projection of the data; '
                  'its text is hashed on every build, and a new version is recorded only when that text changes. A version names the site '
                  'release that created it and the date of that release. Versions marked reconstructed were rebuilt from the markdown twins '
                  'and data files of earlier releases in git. Written by admin/build/build.py; never edit by hand.')
RELEASES = list(reversed(D['versions']['versions']))  # oldest first
REL_DATE = {r['version']: r['date'] for r in RELEASES}
SEO = D.get('seo') or {}
PAGE_VERSIONED = ['summary/index.html', 'flaws/index.html', 'code/index.html', 'timeline/index.html', 'discovery/index.html', 'leak/index.html',
                  'exploitation/index.html', 'impact/index.html', 'defence/index.html', 'context/index.html', 'playbook/index.html',
                  'claims/index.html', 'numbers/index.html', 'agencies/index.html', 'affected/index.html', 'actors/index.html',
                  'explained/index.html', 'glossary/index.html', 'method/index.html', 'interview/index.html']

def norm_md(md):
    """The text a section is versioned on: the markdown twin without its footer, links reduced to their words."""
    md = md.split('\n\n---\nsite v')[0]
    md = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md)
    md = md.replace(" fact timeline →", "")  # a navigation link added to claim rows in v0.3.2, not content
    md = re.sub(r'[ \t]+\n', '\n', md)
    return re.sub(r'\n{3,}', '\n\n', md).strip()

def briefing_norm(md):
    """A briefing's text without what changes when other pages change: reading times and the glossary chips."""
    md = norm_md(md)
    md = re.sub(r'\n## Words you will meet\n.*?(?=\n## |\Z)', '\n', md, flags=re.S)
    md = re.sub(r' ?\b\d+ min\b', '', md)
    md = re.sub(r'About \d+ minutes in all\. ?', '', md)
    md = re.sub(r' &middot; from the same \d+ claims, selected and ordered for one reader| · from the same \d+ claims, selected and ordered for one reader', '', md)
    return md.strip()

def section_id(path):
    if path.startswith('briefings/'):
        return 'briefing-' + path.split('/')[1]
    return 'page-' + re.sub(r'/index\.html$|\.html$', '', path).replace('/', '-')

def ledger(sid, title, kind, path, text, scope='everyone', site=None, date=None, reconstructed=False):
    """Record a section's text; return its ledger entry. Idempotent: the same text never makes a second version."""
    site, date = site or VERSION, date or REL_DATE.get(site or VERSION, '')
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]
    sec = LEDGER['sections'].setdefault(sid, {'title': title, 'kind': kind, 'path': path, 'scope': scope, 'versions': []})
    sec.update({'title': title, 'kind': kind, 'path': path, 'scope': scope})
    vs = sec['versions']
    if vs and vs[-1]['hash'] == h:
        return sec
    if vs and vs[-1]['site'] == site and not reconstructed:
        if len(vs) >= 2 and vs[-2]['hash'] == h:
            vs.pop()
        else:
            vs[-1].update({'hash': h, 'text': text})
        return sec
    vs.append({'v': len(vs) + 1, 'hash': h, 'site': site, 'date': date, 'reconstructed': reconstructed, 'text': text})
    return sec

def ledger_for_page(path, md):
    if path.startswith('briefings/'):
        a = AUD.get(path.split('/')[1])
        return ledger(section_id(path), f'Briefing: {a["name"] if a else path}', 'briefing', path, briefing_norm(md), scope=path.split('/')[1])
    if path in PAGE_VERSIONED:
        return ledger(section_id(path), nav_title(path), 'page', path, norm_md(md))
    return None

def save_ledger():
    OUTPUTS.add('data/sections.json')
    out = json.dumps(LEDGER, indent=1, ensure_ascii=False) + '\n'
    old = open(LEDGER_PATH, encoding='utf-8').read() if os.path.exists(LEDGER_PATH) else ''
    if out != old:
        write('data/sections.json', out)

def nice_date(d):
    return human_time(d + 'T00:00').replace(', 00:00 UTC', '') if d else ''

def vbadge(sid, depth, label='This section'):
    sec = LEDGER['sections'].get(sid)
    if not sec or not sec['versions']:
        return ''
    v, n, up = sec['versions'][-1], len(sec['versions']), '../' * depth
    hist = f'<a href="{up}versions/{E(sid)}/index.html">{"history and changes, " + str(n - 1) + " earlier" if n > 1 else "history"}</a>'
    scope = ' data-scope="page"' if label in ('This page', 'This briefing') else ''
    return (f'<p class="vbadge"><span class="it" data-item="{E(sid)}" data-h="{E(v["hash"])}" data-n="{v["v"]}"{scope}></span><span class="vb-v">{E(label)} v{v["v"]}</span> written in site <a href="{up}admin/versions.html#v{E(v["site"])}">v{E(v["site"])}</a>'
            f' on {E(nice_date(v["date"]))} &middot; {hist}</p>')

def word_diff(a, b):
    ta, tb = re.split(r'(\s+)', a), re.split(r'(\s+)', b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            out.append(E(''.join(ta[i1:i2])))
        else:
            if i2 > i1: out.append(f'<del>{E("".join(ta[i1:i2]))}</del>')
            if j2 > j1: out.append(f'<ins>{E("".join(tb[j1:j2]))}</ins>')
    return ''.join(out)

def diff_html(a, b):
    """Line diff of two versions, with a word diff inside lines that were edited rather than replaced."""
    al, bl = a.splitlines(), b.splitlines()
    sm = difflib.SequenceMatcher(None, al, bl, autojunk=False)
    out, added, removed = [], 0, 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            lines = al[i1:i2]
            if len(lines) > 3:
                out.append(f'<div class="dl dl-ctx">{E(lines[0])}</div><div class="dl dl-skip">{len(lines) - 2} unchanged lines</div><div class="dl dl-ctx">{E(lines[-1])}</div>')
            else:
                out.extend(f'<div class="dl dl-ctx">{E(x)}</div>' for x in lines)
        elif op == 'replace' and i2 - i1 == j2 - j1 and sum(len(x) for x in al[i1:i2]) < 6000:
            for x, y in zip(al[i1:i2], bl[j1:j2]):
                out.append(f'<div class="dl dl-chg">{word_diff(x, y)}</div>')
                added += 1; removed += 1
        else:
            out.extend(f'<div class="dl dl-del">{E(x)}</div>' for x in al[i1:i2])
            out.extend(f'<div class="dl dl-ins">{E(x)}</div>' for x in bl[j1:j2])
            removed += i2 - i1; added += j2 - j1
    return f'<div class="diff">{"".join(out)}</div>', added, removed

def fact_text(c):
    return f'{c["claim"]}\nWho says it: {c["by"]}\nStatus: {c["status"]}\nTopic: {c["topic"]}\nSources: {", ".join(c["sources"])}'

def fact_field(text, field):
    m = re.search(r'^' + field + r': (.*)$', text, flags=re.M)
    return m.group(1) if m else ''

def parse_when(s):
    """A sortable ISO-ish instant from the shapes the manifest uses, or None."""
    if not s:
        return None
    s = str(s)
    m = re.match(r'^(\d{8})T(\d{2})(\d{2})(\d{2})Z', s)
    if m:
        d = m.group(1)
        return f'{d[:4]}-{d[4:6]}-{d[6:]}T{m.group(2)}:{m.group(3)}Z'
    m = re.match(r'^(\d{4}-\d{2}-\d{2})(?:[T ](\d{2}:\d{2}))?', s)
    if m:
        return m.group(1) + ('T' + m.group(2) + 'Z' if m.group(2) else '')
    m = re.match(r'^(\d{4})$', s)
    return m.group(1) if m else None

def fact_projections(c):
    """Where a fact is shown: the briefings whose selection includes its topic, and the pages that list it."""
    out = [(f'briefings/{pid}/index.html', PERSONAS[pid]) for pid, sel in BRIEF_TOPICS.items() if c['topic'] in sel and pid in PERSONAS]
    return out

BRIEF_TOPICS = {}  # filled by build_briefings: persona id -> topics

def build_facts():
    for c in D['claims']:
        ledger('fact-' + c['id'], c['claim'][:90], 'fact', f'facts/{c["id"]}/index.html', fact_text(c), scope='fact')
    for c in D['claims']:
        sec = LEDGER['sections']['fact-' + c['id']]
        evs = []
        for s in c['sources']:
            if s not in SOURCES:
                continue
            row = SOURCES[s]
            pw = parse_when(row.get('published'))
            if pw:
                evs.append((pw, 'pub', f'{short_name(row)} publishes <a href="../../sources/{E(s)}/index.html">{E((row.get("title") or s)[:110])}</a>'))
            caps = sorted(parse_when(x.get('stamp')) or '' for x in row.get('captures', []))
            if caps and caps[0]:
                evs.append((caps[0], 'cap', f'Saved into the evidence vault: {short_name(row)}' + (f', then {len(caps) - 1} more capture{"s" if len(caps) > 2 else ""}' if len(caps) > 1 else '')))
        prev = None
        for v in sec['versions']:
            st = fact_field(v['text'], 'Status')
            if prev is None:
                what = f'Enters this site as {pill(st)} in v{E(v["site"])}'
            elif fact_field(prev['text'], 'Status') != st:
                what = f'Status changes from {pill(fact_field(prev["text"], "Status"))} to {pill(st)} in v{E(v["site"])}'
            else:
                what = f'Reworded or re-sourced in v{E(v["site"])}'
            evs.append((v['date'] + 'T23:59Z', 'site', what + (' <span class="small">(reconstructed from git)</span>' if v.get('reconstructed') else '')))
            prev = v
        evs.sort(key=lambda e: e[0])
        rail = ''.join(f'<li class="tk tk-{k}"><span class="when">{E(fmt_at(w) if "T" in w and not w.endswith("T23:59Z") else w[:10])}</span><span>{t}</span></li>' for w, k, t in evs)
        rows = []
        for i, v in enumerate(sec['versions']):
            d = ''
            if i:
                d, _, _ = diff_html(sec['versions'][i - 1]['text'], v['text'])
            rows.append(f'<details{" open" if i == len(sec["versions"]) - 1 else ""}><summary>v{v["v"]} &middot; site v{E(v["site"])} &middot; {E(nice_date(v["date"]))} &middot; {pill(fact_field(v["text"], "Status"))}</summary>{d or "<pre>" + E(v["text"]) + "</pre>"}</details>')
        proj = fact_projections(c)
        pj = ''.join(f'<a class="pchip" href="../../{E(p)}">{avatar(pp)}<span><b>{E(pp["person"])}</b><small>{E(pp["label"])}</small></span></a>' for p, pp in proj)
        g = mini_graph('fact ' + c['id'], c['status'], [(SOURCES[s].get('title') or s, f'../../sources/{s}/index.html', 'src') for s in c['sources'] if s in SOURCES], 2)
        body = f'''
<p class="kicker">Fact &middot; {E(c["topic"])} &middot; {pill(c["status"])}</p>
<h1>{E(c["claim"])}</h1>
<p class="meta"><b>Who says it:</b> {E(c["by"])} &middot; <b>Sources:</b> {src_links(c["sources"], 2)}</p>
{f'<p class="note">{E(c["note"])}</p>' if c.get("note") else ""}
{fc_section(c["id"])}
{section("timeline", "This fact over time", f'<ol class="rail">{rail}</ol><p class="small">Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.</p>')}
{section("graph", "What it rests on", g)}
{section("where", "Where this fact appears", (f'<p>In the briefings for:</p><div class="pchips">{pj}</div>' if pj else '<p class="small">Not in any briefing yet.</p>') + f'<p>And on <a href="../../claims/index.html#{E(c["id"])}">every claim</a>.</p>')}
{section("versions", "Every version of this fact", "".join(rows))}
'''
        page(f'facts/{c["id"]}/index.html', f'Fact: {c["claim"][:80]}', f'{c["claim"]} Who says it, its status ({c["status"]}), its sources, and its timeline from publication to this site.', body, kind='evidence', topics='php2shell fact')

def history_page(sid, sec):
    vs = sec['versions']
    items = []
    for i in range(len(vs) - 1, -1, -1):
        v = vs[i]
        if i:
            d, add, rem = diff_html(vs[i - 1]['text'], v['text'])
            head = f'{add} lines added or changed, {rem} removed or changed, against v{vs[i - 1]["v"]}'
        else:
            d, head = f'<pre class="vtext">{E(v["text"][:20000])}</pre>', 'the first version'
        items.append(f'<details id="v{v["v"]}"{" open" if i == len(vs) - 1 else ""}><summary><b>v{v["v"]}</b> &middot; site <a href="../../admin/versions.html#v{E(v["site"])}">v{E(v["site"])}</a> &middot; {E(nice_date(v["date"]))}{" &middot; reconstructed from git" if v.get("reconstructed") else ""} &middot; {head} &middot; <code>{E(v["hash"])}</code></summary>{d}</details>')
    scope = sec.get('scope')
    who = f' It is written for {E(PERSONAS[scope]["person"])}, {E(PERSONAS[scope]["label"].lower())}.' if scope in PERSONAS else ''
    body = f'''
<p class="kicker">Version history &middot; {E(sec["kind"])}</p>
<h1>{E(sec["title"])}: every version</h1>
<p class="lead">This section is a projection of the site's data, rebuilt on every release.{who} A new version is recorded only when the text a reader sees changes, so a release that changed something elsewhere leaves this section's version alone. It has {len(vs)} version{"s" if len(vs) != 1 else ""}; the newest is first, and each is shown as the changes from the one before. <a href="../../{E(sec["path"])}">Read the current version &rarr;</a></p>
{"".join(items)}
<p><a href="../index.html">Every section, across every release &rarr;</a></p>
'''
    page(f'versions/{sid}/index.html', f'{sec["title"]}: version history', f'Every version of the section "{sec["title"]}" on {SITE_NAME}, with the site release that created it and the changes between versions.', body, kind='site')

def build_versions():
    secs = [(sid, s) for sid, s in LEDGER['sections'].items() if s['kind'] != 'fact']
    for sid, s in secs:
        history_page(sid, s)
    rels = [r['version'] for r in RELEASES]
    head = ''.join(f'<th class="rv"><a href="../admin/versions.html#v{E(r)}">{E(r)}</a></th>' for r in rels)
    groups = [('front', 'The front page'), ('briefing', 'The briefings, one per reader'), ('page', 'The story and evidence pages')]
    rows = ''
    for kind, label in groups:
        rows += f'<tr class="vg"><th colspan="{len(rels) + 1}">{E(label)}</th></tr>'
        for sid, s in secs:
            if s['kind'] != kind:
                continue
            made = {v['site']: v for v in s['versions']}
            first = s['versions'][0]['site']
            cells = ''
            alive = False
            for r in rels:
                alive = alive or r == first
                if r in made:
                    cells += f'<td><a class="vc vc-new" href="{E(sid)}/index.html#v{made[r]["v"]}" title="v{made[r]["v"]} written in {E(r)}">v{made[r]["v"]}</a></td>'
                else:
                    cells += f'<td><span class="vc{" vc-same" if alive else ""}" title="{"unchanged" if alive else "did not exist"}"></span></td>'
            who = avatar(PERSONAS[s['scope']]) + ' ' if s.get('scope') in PERSONAS else ''
            rows += f'<tr><th class="vn">{who}<a href="{E(sid)}/index.html">{E(s["title"])}</a></th>{cells}</tr>'
    facts = [s for s in LEDGER['sections'].values() if s['kind'] == 'fact']
    frow = ''
    for r in rels:
        added = sum(1 for s in facts if s['versions'][0]['site'] == r)
        changed = sum(1 for s in facts for i, v in enumerate(s['versions']) if i and v['site'] == r and fact_field(v['text'], 'Status') != fact_field(s['versions'][i - 1]['text'], 'Status'))
        reworded = sum(1 for s in facts for i, v in enumerate(s['versions']) if i and v['site'] == r) - changed
        frow += f'<td class="fc">{f"<b>+{added}</b>" if added else ""}{f"<br><span>{changed} status</span>" if changed else ""}{f"<br><span>{reworded} edited</span>" if reworded else ""}</td>'
    body = f'''
<p class="kicker">The evidence &middot; versions</p>
<h1>How the story changed, release by release</h1>
<p class="lead">Every section of this site is a projection of the evidence, and every projection is versioned. Across: each release of the site. Down: the front page's sections, each reader's briefing, and the story and evidence pages. A filled cell is a new version written in that release; a faint cell is a section that existed and did not change. A new fact for engineers moves the engineer's briefing and leaves the board's alone, and this table is where that shows.</p>
<div class="tw vt"><table class="vmatrix"><thead><tr><th>Section</th>{head}</tr></thead><tbody>{rows}<tr class="vg"><th colspan="{len(rels) + 1}">The facts</th></tr><tr><th class="vn"><a href="../claims/index.html">{len(facts)} facts</a>: added, status changes, edits</th>{frow}</tr></tbody></table></div>
<p class="small">Versions before v0.3.2 are reconstructed from each release's markdown twins and data files in git. The ledger itself is <a href="../data/sections.json">data/sections.json</a>. What each release changed, in a sentence, is the <a href="../admin/versions.html">release history</a>; what changed for readers is <a href="../whatsnew/index.html">what's new</a>.</p>
'''
    page('versions/index.html', 'How the story changed, release by release', 'Every section of the site, every reader\'s briefing and every fact, versioned across every release: what changed, when, and in which release.', body, kind='site')

def changes_in(rel):
    secs, facts_new, facts_status, facts_edit = [], [], [], []
    for sid, s in LEDGER['sections'].items():
        for i, v in enumerate(s['versions']):
            if v['site'] != rel:
                continue
            if s['kind'] == 'fact':
                fid = sid[5:]
                if i == 0:
                    facts_new.append((fid, s, v))
                elif fact_field(v['text'], 'Status') != fact_field(s['versions'][i - 1]['text'], 'Status'):
                    facts_status.append((fid, s, v, s['versions'][i - 1]))
                else:
                    facts_edit.append((fid, s, v))
            else:
                secs.append((sid, s, v, i))
    return secs, facts_new, facts_status, facts_edit

def build_whatsnew():
    out = ''
    for r in reversed(RELEASES):
        rel = r['version']
        secs, fn, fs, fe = changes_in(rel)
        parts = []
        if fs:
            parts.append('<h3>Facts whose status changed</h3><ul>' + ''.join(f'<li><a href="../facts/{E(f)}/index.html">{E(s["title"])}</a>: {pill(fact_field(p["text"], "Status"))} &rarr; {pill(fact_field(v["text"], "Status"))}</li>' for f, s, v, p in fs) + '</ul>')
        if fn:
            parts.append(f'<h3>{len(fn)} new fact{"s" if len(fn) != 1 else ""}</h3><ul class="cmp">' + ''.join(f'<li><a href="../facts/{E(f)}/index.html">{E(s["title"])}</a> {pill(fact_field(v["text"], "Status"))}</li>' for f, s, v in fn[:40]) + ('<li>and more on <a href="../claims/index.html">every claim</a></li>' if len(fn) > 40 else '') + '</ul>')
        if fe:
            parts.append(f'<p class="small">{len(fe)} fact{"s" if len(fe) != 1 else ""} reworded or re-sourced: ' + ', '.join(f'<a href="../facts/{E(f)}/index.html">{E(f)}</a>' for f, s, v in fe[:30]) + '.</p>')
        readers = [(sid, s, v, i) for sid, s, v, i in secs if s['kind'] == 'briefing']
        if readers:
            parts.append('<h3>Briefings that changed</h3><div class="pchips">' + ''.join(f'<a class="pchip" href="../versions/{E(sid)}/index.html#v{v["v"]}">{avatar(PERSONAS[s["scope"]]) if s["scope"] in PERSONAS else ""}<span><b>{E(PERSONAS[s["scope"]]["person"]) if s["scope"] in PERSONAS else ""}</b><small>{E(s["title"].replace("Briefing: ", ""))} &middot; {"new" if i == 0 else "v" + str(v["v"])}</small></span></a>' for sid, s, v, i in readers) + '</div>')
        others = [(sid, s, v, i) for sid, s, v, i in secs if s['kind'] != 'briefing']
        if others:
            parts.append('<h3>Sections that changed</h3><ul class="cmp">' + ''.join(f'<li><a href="../versions/{E(sid)}/index.html#v{v["v"]}">{E(s["title"])}</a> {"(new)" if i == 0 else "v" + str(v["v"])}</li>' for sid, s, v, i in others) + '</ul>')
        out += f'<article class="rel wn" id="v{E(rel)}" data-rel="{E(rel)}"><h2>v{E(rel)} &middot; {E(nice_date(r["date"]))}<span class="newmark">new since your last visit</span></h2><p>{E(r["title"])}</p>{"".join(parts) or "<p class=small>No reader-facing section changed in this release.</p>"}</article>'
    body = f'''
<p class="kicker">The story &middot; what's new</p>
<h1>What's new</h1>
<p class="lead">Every release of this site, newest first, with what changed in it for readers: facts added, facts whose status changed, the briefings that moved and the sections that were rewritten. Releases you have not seen since your last visit are marked. To follow along, subscribe to <a href="../feed.xml">the feed</a>.</p>
<p class="caveat">New evidence (for example the first confirmed compromise of a named organisation) reaches this page only once it has been captured into the evidence vault and turned into a fact with sources. Until then it is not on this site, however widely it is reported.</p>
{out}
'''
    page('whatsnew/index.html', "What's new: every change, release by release", 'What changed on this site in each release: new facts, facts whose status changed, the briefings that moved for each reader and the sections that were rewritten.', body, kind='site', topics='php october 2026 updates')

def build_pipeline():
    srcs = D['sources']
    captured = sum(1 for s in srcs if s.get('status') == 'captured')
    blocked = sum(1 for s in srcs if s.get('status') in ('blocked', 'failed'))
    noted = sum(1 for s in srcs if s.get('has_notes'))
    cited = {x for c in D['claims'] for x in c['sources']} | {x for t in D['timeline'] for x in t['sources']}
    claims = len(D['claims'])
    proj = sum(1 for s in LEDGER['sections'].values() if s['kind'] != 'fact')
    stages = [
        ('Found', C['sources'], 'sources the agents found and logged in the vault', 'sources/index.html'),
        ('Saved', captured, f'captured as served and as rendered, each file hashed; {blocked} blocked by bot checks, the block recorded', 'sources/index.html'),
        ('Read', noted, 'with a collector\'s note of what the page actually says', 'sources/index.html'),
        ('Cited', len(cited & set(SOURCES)), 'cited by at least one fact or timeline event', 'graph/index.html'),
        ('Facts', claims, f'facts, each with who says it and a status: {C["by_status"]["confirmed"]} confirmed', 'claims/index.html'),
        ('Sections', proj, 'versioned sections and briefings built from those facts', 'versions/index.html'),
        ('Readers', len(PERSONAS), 'kinds of reader, each with a briefing', 'start/index.html'),
    ]
    mx = max(n for _, n, _, _ in stages)
    funnel = ''.join(f'<a class="fn" href="../{h}"><span class="fl">{E(l)}</span><span class="fb"><i style="width:{max(4, round(100 * n / mx))}%"></i></span><b>{n}</b><span class="ft">{E(t)}</span></a>' for l, n, t, h in stages)
    facts = [s for s in LEDGER['sections'].values() if s['kind'] == 'fact']
    order = ['confirmed', 'reported', 'disputed', 'contradicted', 'unverified']
    bars = ''
    for r in RELEASES:
        cnt = Counter()
        for s in facts:
            live = [v for v in s['versions'] if [x['version'] for x in RELEASES].index(v['site']) <= [x['version'] for x in RELEASES].index(r['version'])]
            if live:
                cnt[fact_field(live[-1]['text'], 'Status')] += 1
        total = sum(cnt.values())
        segs = ''.join(f'<i class="sb sb-{k}" style="flex:{cnt[k]}" title="{cnt[k]} {k}"></i>' for k in order if cnt[k])
        bars += f'<div class="sbr"><span class="sbl">v{E(r["version"])}</span><span class="sbb">{segs}</span><b>{total}</b></div>'
    body = f'''
<p class="kicker">The evidence &middot; the pipeline</p>
<h1>The fact pipeline: from a web page to a reader</h1>
<p class="lead">Every fact on this site has travelled the same path: a source is found, saved and fingerprinted, read, cited by a fact with a status, built into sections, and selected for the readers it matters to. Each bar is a count at that stage, as of this release; each links to the stage itself.</p>
<div class="funnel">{funnel}</div>
{section("status", "The facts by status, release by release", f'<div class="sbars">{bars}</div>' + status_legend(), "How many facts the site carried in each release and how far each could be trusted. A fact that moves from reported to confirmed is a second primary source found; one that moves the other way is a correction.")}
{section("verify", "Verification: what runs and what does not", """<ul class="howlist">
<li><b>Runs on every build:</b> every fact cites only sources that exist in the vault's manifest; every link resolves; every section's text is hashed and versioned; the site is byte-identical when rebuilt.</li>
<li><b>Runs when an agent writes a fact:</b> the status word is chosen from the sources it cites, and a fact never gets a better word than its sources give it.</li>
<li><b>Not yet run:</b> an independent verifier that re-reads every fact against the saved text of its sources, and a second model reading the vault. Both are on the list; neither has happened, and this line will change when they do.</li>
</ul>""")}
{section("each", "Every fact has its own timeline", '<p>Each fact has a page of its own: when each of its sources was published, when it was saved, when it entered this site and every change of wording or status since, the sources it rests on as a graph, and the briefings it appears in. Start from <a href="../claims/index.html">every claim</a> and follow the timeline link on any row.</p>')}
'''
    page('pipeline/index.html', 'The fact pipeline: from a web page to a reader', 'How a source becomes a fact and a fact reaches a reader on this site: found, saved, read, cited, given a status, built into versioned sections and selected per reader, with counts at every stage and the facts by status in every release.', body, kind='site', topics='provenance pipeline verification')

def build_interview():
    iv = D['interview']
    qa = ''.join(f'<div class="iq" id="q{i + 1}"><h3>{E(x["q"])}</h3><blockquote><p>{E(x["a"])}</p><footer>{E(x["from"])}</footer></blockquote></div>' for i, x in enumerate(iv['qa']))
    pending = ''.join(f'<li>{E(q)}</li>' for q in iv['pending'])
    body = f'''
<p class="kicker">About &middot; interview</p>
<h1>{E(iv["title"])}</h1>
<p class="lead">{E(iv["intro"])}</p>
<p class="caveat">{E(iv["method"])}</p>
{qa}
{section("pending", "Not yet answered", f'<p>The questions for the next round, in the editor\'s own time:</p><ul>{pending}</ul>')}
'''
    page('interview/index.html', iv['title'], iv['description'], body, kind='article', topics='interview editor', origin='interview', byline='The editor, Dinis Cruz, in his own words; the questions by the agent that builds the site')

def build_feed():
    items = ''
    for r in reversed(RELEASES):
        u = f'{BASE_URL}/whatsnew/index.html#v{r["version"]}'
        items += (f'<entry><title>{E("v" + r["version"] + ": " + r["title"][:140])}</title><id>{u}</id><link href="{u}"/>'
                  f'<updated>{r["date"]}T00:00:00Z</updated><summary>{E(r["title"] + (" " + r["summary"] if r.get("summary") else ""))}</summary></entry>\n')
    updated = RELEASES[-1]['date'] + 'T00:00:00Z'
    write('feed.xml', f'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
<title>{E(SITE_NAME)}: what's new</title>
<subtitle>{E(STORY["description"])}</subtitle>
<link href="{BASE_URL}/feed.xml" rel="self"/>
<link href="{BASE_URL}/"/>
<id>{BASE_URL}/</id>
<updated>{updated}</updated>
<author><name>Dinis Cruz</name></author>
{items}</feed>
''')

def page_lastmod(path):
    sec = LEDGER['sections'].get(section_id(path))
    if sec and sec['versions']:
        return sec['versions'][-1]['date']
    if path.startswith('facts/'):
        s = LEDGER['sections'].get('fact-' + path.split('/')[1])
        if s: return s['versions'][-1]['date']
    return RELEASES[-1]['date']

def build_seo():
    urls = []
    for p, _, _, kind in PAGES:
        if p.startswith('account/top') or p == 'account/topped-up.html':
            continue
        pr = '1.0' if p == 'index.html' else '0.8' if p.count('/') == 1 and not p.startswith(('versions/', 'admin/', 'account/')) else '0.5'
        urls.append(f'<url><loc>{BASE_URL}/{p}</loc><lastmod>{page_lastmod(p)}</lastmod><priority>{pr}</priority></url>')
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>\n')
    write('robots.txt', f'# {SITE_NAME}. Everything here is public; agents are welcome, and llms.txt lists the markdown twins.\nUser-agent: *\nAllow: /\nDisallow: /account/top-up.html\nDisallow: /account/topped-up.html\n\nSitemap: {BASE_URL}/sitemap.xml\n')


# ----------------------------------------------------------------------------- patching, and status.json (v0.4.1)

def inv_row(sup, prod):
    return next((r for r in D['software']['rows'] if r['supplier'] == sup and r['product'] == prod), None)

def build_patching():
    P = D['patching']
    inv = f'<a href="../affected/software.html">the NCSC-NL inventory</a>'
    def chip(sup, prod, st):
        r = inv_row(sup, prod)
        ver = f' <span class="small">{E(r["version"][:60])}</span>' if r and r.get('version') else ''
        return f'<li><b class="{"okw" if st == "Fix" else "badw"}">{"fixed" if st == "Fix" else "still affected"}</b> {E(sup)}: {E(prod)}{ver}</li>'
    ladder = table(['PHP branch', 'Upstream', 'What the PHP project shipped', 'In the CVE record', 'Downstream, at the inventory commit', 'Sources'],
                   [[f'<b>{E(l["branch"])}</b>', E(l['upstream']), E(l['fix']), E(l['in_cve']), '<ul class="inv">' + ''.join(chip(*d) for d in l['downstream']) + '</ul>', src_links(l['sources'], 1)] for l in P['ladder']], 'ladder')
    models = ''.join(f'<article class="role" id="m-{E(m["id"])}"><h3>{E(m["name"])}</h3><p>{E(m["what"])}</p><ul class="inv">{"".join(chip(*r) for r in m["rows"])}</ul></article>' for m in P['models'])
    fx = ''.join(f'<li><b>{E(x["what"])}.</b> {E(x["text"])} <span class="refs">{src_links(x["sources"], 1)}</span></li>' for x in P['side_effects'])
    why = ''.join(f'<li>{E(x["text"])} <span class="refs">{src_links(x["sources"], 1)}</span></li>' for x in P['why_not_every_version'])
    sw = D['software']['by_status_109618']
    story = next((a for a in ARTICLES if a['slug'] == 'why-not-patch-every-version'), None)
    body = f'''
<h1>Patching: which versions get a fix, and from whom</h1>
<p class="lead">{E(P["note"])}</p>
<p class="kv"><b>{sw.get("Fix", 0)}</b> fixed &middot; <b>{sw.get("Vulnerable", 0)}</b> still affected &middot; <b>{sw.get("Investigation", 0)}</b> under investigation &middot; <b>{sw.get("Not vuln", 0)}</b> not affected, of {D["software"]["count"]} products in {inv} at commit <code>{E(D["software"]["commit"])}</code> <span class="refs">{src_links([P["inventory_source"]], 1)}</span></p>
{section("ladder", "The version ladder", ladder, "Each PHP branch, what the PHP project itself shipped for it, and some of the companies that shipped a fix for it anyway, or had not yet.")}
{section("why", "Why not every version", f'<ul>{why}</ul>')}
{section("models", "How a fix reaches a server", f'<p>The same fix arrives in very different ways depending on who a site gets its PHP from. Read from {inv}, row by row.</p><div class="roles">{models}</div>')}
{section("effects", "What the fix changes", f'<p>The reason an operator hesitates: the fix is not invisible.</p><ul>{fx}</ul>')}
{section("open", "Not known yet", "<ul>" + "".join(f"<li>{E(o)}</li>" for o in P["open"]) + "</ul>")}
<p>{f'The story behind this page is <a href="../articles/{E(story["slug"])}/index.html">{E(story["title"])}</a>, with the editor\'s argument on who should own patching.' if story else ''} The data is <a href="../data/patching.json">data/patching.json</a>; the gate checks that every downstream row names a product in the inventory with the status shown.</p>
'''
    page('patching/index.html', 'Patching: which versions get a fix, and from whom', 'Which PHP versions the PHP project fixed, which it left to others, which nobody upstream fixed, and how the fix reaches a server: patched for you, rebuild yourself, a system update, extended support, a hosting panel, or still waiting.', body, kind='analysis', topics='php2shell patching versions backports')

STATUS_FACTS = ['two-cves-9.2', 'no-confirmed-compromise', 'cisa-none']

def build_status_json():
    """status.json: a small, stable, machine-readable summary for the newsroom and other sites. No clock: every value is data."""
    cl = {c['id']: c for c in D['claims']}
    latest = ARTICLES[0] if ARTICLES else None
    st = OrderedDict([
        ('schema', 'sgit.newsroom.story-status/1'),
        ('site', SITE), ('name', SITE_NAME), ('url', BASE_URL + '/index.html'),
        ('story', 'php2shell'), ('cves', STORY['cves']), ('status', STORY['status'].lower()),
        ('version', VERSION), ('data_as_of', STORY['data_as_of']), ('vault_commit', D['vault']['head']['commit']),
        ('counts', OrderedDict([('sources', C['sources']), ('captures', C['captures']), ('claims', C['claims']),
                                ('claims_by_status', OrderedDict((k, C['by_status'][k]) for k in STATUS_WORDS)), ('events', C['events']),
                                ('agencies', C['agencies']), ('offline_reported', len(D['impact']['offline'])), ('compromises_confirmed', 0)])),
        ('headline_facts', [OrderedDict([('id', i), ('text', cl[i]['claim']), ('status', cl[i]['status']), ('url', f'{BASE_URL}/claims/index.html#{i}'), ('sources', cl[i]['sources'])]) for i in STATUS_FACTS]),
        ('latest_story', OrderedDict([('title', latest['title']), ('url', f'{BASE_URL}/articles/{latest["slug"]}/index.html'), ('written', latest['written']), ('origin', latest['origin'])]) if latest else None),
        ('links', OrderedDict([('front', f'{BASE_URL}/index.html'), ('sources', f'{BASE_URL}/sources/index.html'), ('claims', f'{BASE_URL}/claims/index.html'),
                               ('stories', f'{BASE_URL}/articles/index.html'), ('releases', f'{BASE_URL}/admin/versions.html'), ('llms', f'{BASE_URL}/llms.txt')])),
    ])
    text = json.dumps(st, indent=1, ensure_ascii=False) + '\n'
    write('status.json', text)
    rows = [[f'<code>{E(k)}</code>', E(json.dumps(v, ensure_ascii=False)[:160])] for k, v in st.items()]
    body = f'''
<h1>status.json: this site's state, for other sites</h1>
<p class="lead">One small file at the site root, <a href="../../status.json">/status.json</a>, that another site or an agent can read instead of scraping pages: the story's status, the version, when the evidence was last checked, the counts, three headline facts with their status and sources, and the latest story. The SGit Newsroom's front page reads it while the story is developing, and its tracker checks for it before the newsroom's own section on the story becomes a pointer here.</p>
<p class="kv"><b>Schema</b> <code>{E(st["schema"])}</code> &middot; <b>rebuilt</b> on every release, from the same data as the pages, with no clock: if the evidence has not changed, neither has the file.</p>
{table(["Field", "Value now"], rows)}
<h2>The rules</h2>
<ul>
<li>Fields are only ever added. A reader of version 1 keeps working.</li>
<li>A headline fact is a claim id from <a href="../../claims/index.html">every claim</a>; its text and status are the claim's, never rewritten for the feed.</li>
<li><code>data_as_of</code> is the time of the latest capture in the evidence vault, not the time of the build.</li>
<li>No personal data, no credential, nothing that is not already on a page.</li>
</ul>
<pre>{E(text)}</pre>
'''
    page('admin/status-json/index.html', 'status.json: the feed for other sites', 'The machine-readable summary of this site at /status.json: status, version, data time, counts, headline facts and the latest story, for the newsroom and other agents.', body, kind='site')


# ----------------------------------------------------------------------------- the inventory over time, and the signals (v0.4.2)

# Status colours from the dataviz reference status palette (validated: adjacent CVD separation >= 10.6 in light and
# dark); the same in every theme by design, and never used for anything but a status. Text stays in text tokens.
INV_ST = OrderedDict([('Fix', ('Fixed', '#0ca30c')), ('Not vuln', ('Not affected', '#8a8f98')),
                      ('Vulnerable', ('Vulnerable', '#d03b3b')), ('Investigation', ('Under investigation', '#fab219'))])

def _mins(at):
    from datetime import datetime, timezone
    if re.match(r'^\d{4}-\d{2}-\d{2}$', at):
        at += 'T00:00Z'
    return int(datetime.strptime(at, '%Y-%m-%dT%H:%MZ').replace(tzinfo=timezone.utc).timestamp() // 60)

def _hm(at):
    return human_time(at) if 'T' in at else nice_date(at)

def inventory_chart(snaps, marks):
    S = [s for s in snaps if s['rows']]
    W, H, L, R, T, B = 760, 300, 44, 168, 14, 42
    x0, x1 = _mins(S[0]['at']), _mins(S[-1]['at']) + 30
    ymax = int(math.ceil(max(s['rows'] for s in S) / 200.0) * 200)
    X = lambda m: L + (m - x0) * (W - L - R) / (x1 - x0)
    Y = lambda v: T + (H - T - B) * (1 - v / ymax)
    out = [f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-labelledby="inv-t inv-d"><title id="inv-t">The NCSC-NL inventory by status, commit by commit</title>'
           f'<desc id="inv-d">{len(S)} commits from {_hm(S[0]["at"])} to {_hm(S[-1]["at"])}; the same numbers are in the table below.</desc>']
    for v in range(0, ymax + 1, 200):
        out.append(f'<line class="grid" x1="{L}" x2="{W - R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/><text class="ax" x="{L - 6}" y="{Y(v) + 4:.1f}" text-anchor="end">{v}</text>')
    lows, labels = [0] * len(S), []
    for st, (label, col) in INV_ST.items():
        highs = [lo + s['by_status'].get(st, 0) for lo, s in zip(lows, S)]
        top, bot = [], []
        for i, s in enumerate(S):
            xa, xb = X(_mins(s['at'])), X(_mins(S[i + 1]['at']) if i + 1 < len(S) else x1)
            top += [(xa, Y(highs[i])), (xb, Y(highs[i]))]
            bot += [(xa, Y(lows[i])), (xb, Y(lows[i]))]
        pts = top + bot[::-1]
        out.append(f'<path class="band" fill="{col}" d="M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + 'Z"/>')
        n, mid = S[-1]['by_status'].get(st, 0), (Y(lows[-1]) + Y(highs[-1])) / 2
        if n:
            labels.append([mid, col, f'{label} {n}'])
        lows = highs
    # direct labels at the right edge: thin bands put them on top of each other, so space them at least 14px apart
    labels.sort(key=lambda l: -l[0])
    for i in range(1, len(labels)):
        labels[i][0] = min(labels[i][0], labels[i - 1][0] - 14)
    for y, col, text in labels:
        out.append(f'<g class="dl"><rect x="{W - R + 8}" y="{y - 5:.1f}" width="10" height="10" rx="2" fill="{col}"/><text x="{W - R + 23}" y="{y + 4:.1f}">{E(text)}</text></g>')
    for m_at, m_label in marks:
        mx = X(_mins(m_at))
        if L <= mx <= W - R:
            out.append(f'<line class="mark" x1="{mx:.1f}" x2="{mx:.1f}" y1="{T}" y2="{H - B}"/><text class="ax" x="{mx + 4:.1f}" y="{T + 10}">{E(m_label)}</text>')
    for t in ('2026-10-21T12:00Z', '2026-10-21T18:00Z', '2026-10-22T00:00Z', '2026-10-22T06:00Z', '2026-10-22T12:00Z'):
        tx = X(_mins(t))
        if L <= tx <= W - R:
            out.append(f'<text class="ax" x="{tx:.1f}" y="{H - B + 16}" text-anchor="middle">{t[8:10]} Oct {t[11:16]}</text>')
    out.append(f'<text class="ax" x="{L}" y="{H - 6}">UTC; rows in the inventory</text>')
    for i, s in enumerate(S):
        xa, xb = X(_mins(s['at'])), X(_mins(S[i + 1]['at']) if i + 1 < len(S) else x1)
        tip = f'{_hm(s["at"])}, commit {s["commit"]}: {s["rows"]} rows; ' + ', '.join(f'{s["by_status"].get(k, 0)} {v[0].lower()}' for k, v in INV_ST.items())
        out.append(f'<rect class="hit" x="{xa:.1f}" y="{T}" width="{max(xb - xa, 1):.1f}" height="{H - T - B}"><title>{E(tip)}</title></rect>')
    out.append('</svg>')
    legend = '<ul class="legend">' + ''.join(f'<li><span class="sw" style="background:{c}"></span>{E(l)}</li>' for l, c in INV_ST.values()) + '</ul>'
    return legend + ''.join(out)

def build_inventory():
    H_ = D['inventory-history']; S = [s for s in H_['snapshots'] if s['rows']]
    first, last = S[0], S[-1]
    rel = '2026-10-21T14:00Z'
    chart = inventory_chart(H_['snapshots'], [(rel, 'release 14:00'), ('2026-10-22T08:40Z', 'vault capture')])
    tab = table(['When (UTC)', 'Commit', 'Rows'] + [v[0] for v in INV_ST.values()],
                [[E(_hm(s['at'])), f'<code>{E(s["commit"])}</code>', str(s['rows'])] + [str(s['by_status'].get(k, 0)) for k in INV_ST] for s in S])
    moves = Counter((c['from'], c['to']) for c in H_['changes'])
    name = lambda k: 'added to the list' if k == 'added' else (INV_ST[k][0].lower() if k in INV_ST else k)
    mv = table(['From', 'To', 'Rows'], [[E(name(a)), E(name(b)), str(n)] for (a, b), n in sorted(moves.items(), key=lambda kv: -kv[1])])
    cls = OrderedDict((c['id'], c) for c in H_['classes'])
    cc = Counter((r[3], r[2]) for r in H_['head_rows'])
    ct = table(['What kind of row', 'Rows'] + [v[0] for v in INV_ST.values()],
               [[E(c['name']), str(sum(cc[(cid, k)] for k in list(INV_ST) + ['none']))] + [str(cc[(cid, k)] or '') for k in INV_ST] for cid, c in cls.items() if any(cc[(cid, k)] for k in list(INV_ST) + ['none'])], 'ctx')
    sec = [r for r in H_['head_rows'] if r[3] == 'security-vendor']
    secv = ', '.join(f'<b>{E(r[1])}</b> ({E(r[0])})' for r in sec if r[2] == 'Vulnerable')
    secc = Counter(r[0] for r in sec if r[2] == 'Investigation')
    firstfix = OrderedDict()
    for c in H_['changes']:
        if c['to'] == 'Fix' and c['supplier'] not in firstfix:
            firstfix[c['supplier']] = c
    ff = table(['Recorded fixed (UTC)', 'Hours after release', 'Supplier', 'First product'], [[E(_hm(c['at'])), f'{(_mins(c["at"]) - _mins(rel)) / 60:.1f}', E(s_), E(c['product'])] for s_, c in list(firstfix.items())[:24]])
    lf = last['by_status']
    body = f'''
<h1>The inventory, hour by hour: fixed, vulnerable, still under investigation</h1>
<p class="lead">The Dutch NCSC keeps a public list of software that ships or depends on PHP, with a status for each product. This site captured it once, at 08:40 UTC on 22 October. Its git history shows the rest: {len(S)} versions from {E(_hm(first["at"]))} to {E(_hm(last["at"]))}, each read from the commit that made it. At the last one, {lf.get("Fix", 0)} of {last["rows"]} rows were fixed, {lf.get("Vulnerable", 0)} vulnerable and {lf.get("Investigation", 0)} still under investigation, about {(_mins(last["at"]) - _mins(rel)) / 60:.0f} hours after the release.</p>
<figure>{chart}<figcaption>Rows by status at every commit of the inventory that changed it. Hover a column for the commit and its counts; the table below has the same numbers. Read from a clone of <a href="{E(H_["source"])}">{E(H_["source"])}</a> at <code>{E(H_["head"])}</code>.</figcaption></figure>
<details><summary>The same numbers as a table</summary>{tab}</details>
{section("reading", "How to read it", f"""<ul>
<li><b>Vulnerable mostly means inherited.</b> {cc[("inherited", "Vulnerable")]} of the {lf.get("Vulnerable", 0)} vulnerable rows are applications the inventory marks <q>affected when deployed on an affected web-serving PHP runtime</q>. Their fix is patching PHP underneath them, not a release from their maker, so they stay vulnerable in the list whatever the server does. That is why only {moves[("Vulnerable", "Fix")]} row moved from vulnerable to fixed.</li>
<li><b>Fixes came from the people who ship PHP.</b> Operating systems, container images, platforms and hosting panels: the {lf.get("Fix", 0)} fixed rows are almost all runtimes, recorded from 15:30 UTC on 21 October.</li>
<li><b>The investigation pile grew while it shrank.</b> {moves[("Investigation", "Vulnerable")]} rows were resolved to vulnerable and {moves[("Investigation", "Fix")]} to fixed, and {moves[("added", "Investigation")]} new rows arrived under investigation.</li>
<li><b>The boxes in front run PHP too.</b> Vulnerable: {secv}. Under investigation: {", ".join(f"{E(k)} ({n})" for k, n in secc.most_common())}.</li>
</ul>""")}
{section("moves", "Every change of status", mv + "<p class=small>Between consecutive commits, per row. A row added already fixed counts as added.</p>")}
{section("kinds", "What kind of rows they are", ct + f"<p class=small>Read from each row's own <q>CVE assessment</q> line by {len(cls)} rules, applied in order; the rules are in <code>admin/build/inventory_history.py</code> and in <a href=\"../../data/inventory-history.json\">the data</a>. The words matched are the inventory's; the grouping is this site's.</p>")}
{section("first", "When each supplier was first recorded fixed", ff + "<p class=small>The time the inventory recorded the fix, not the time the supplier shipped it.</p>")}
{section("method", "Where this comes from", f"""<p>{E(H_["read_from"])}. Commits are content-addressed: anyone with a clone can check every number here against the commit named. The self-check: {E(H_["self_check"])}. That one row is a correction to this site's earlier counts, on <a href="../../corrections/index.html">corrections</a>. The vault holds the inventory at one commit; the history is not yet captured into it (board).</p>""")}
<p>The patching ladder, version by version, is on <a href="../index.html">Patching</a>; the signals this belongs to are on <a href="../../signals/index.html">The second stories</a>.</p>
'''
    page('patching/inventory/index.html', 'The inventory, hour by hour: fixed, vulnerable, still under investigation', f'The NCSC-NL php2shell inventory across {len(S)} commits: how {last["rows"]} products moved between fixed, vulnerable and under investigation after the release, what kind of products they are, and when each supplier was first recorded fixed.', body, kind='analysis', topics='php2shell patching inventory over time')

def _tl(at, x0, x1, w=240):
    """A one-row timeline cell: available from `at` to the right edge; a whole day when only the date is known."""
    if not at:
        return f'<svg class="tlc" viewBox="0 0 {w} 16" width="{w}" height="16" aria-hidden="true"><line class="grid" x1="0" x2="{w}" y1="8" y2="8"/></svg>'
    X = lambda m: max(0, min(w, (m - x0) * w / (x1 - x0)))
    if 'T' in at:
        a = X(_mins(at))
        return f'<svg class="tlc" viewBox="0 0 {w} 16" width="{w}" height="16" aria-hidden="true"><line class="grid" x1="0" x2="{w}" y1="8" y2="8"/><line class="avail" x1="{a:.1f}" x2="{w}" y1="8" y2="8"/><circle class="avail-d" cx="{a:.1f}" cy="8" r="4"/></svg>'
    a, b = X(_mins(at)), X(_mins(at) + 1440)
    return f'<svg class="tlc" viewBox="0 0 {w} 16" width="{w}" height="16" aria-hidden="true"><line class="grid" x1="0" x2="{w}" y1="8" y2="8"/><rect class="day" x="{a:.1f}" y="3" width="{b - a:.1f}" height="10" rx="2"/><line class="avail" x1="{b:.1f}" x2="{w}" y1="8" y2="8"/></svg>'

def _bar(l, top, w=140):
    """A cell mark for the ladder: a linear bar against the largest count of hosts (the units are the same), a line for
    zero, a dashed box for a layer nobody has measured, nothing for a share or for attempts (other units)."""
    if l['kind'] == 'count' and l.get('n'):
        return f'<svg class="tlc bar" viewBox="0 0 {w} 14" width="{w}" height="14" aria-hidden="true"><rect class="lb" x="0" y="2" width="{w * l["n"] / top:.1f}" height="10" rx="2"/></svg>'
    if l['kind'] == 'zero':
        return f'<svg class="tlc bar" viewBox="0 0 {w} 14" width="{w}" height="14" aria-hidden="true"><line class="zero" x1="1.5" x2="1.5" y1="0" y2="14"/></svg>'
    if l['kind'] == 'unknown':
        return f'<svg class="tlc bar" viewBox="0 0 {w} 14" width="{w}" height="14" aria-hidden="true"><rect class="unk" x="0.5" y="2.5" width="{w - 1}" height="9" rx="2"/></svg>'
    return ''

def build_signals():
    G = D['signals']; fam = {f['id']: f for f in G['families']}
    top = max(l.get('n') or 0 for l in G['ladder'] if l['kind'] == 'count')
    ladder = table(['Layer', 'How many', '', 'Signal', 'Status', 'Sources'],
                   [[f'<b>{E(l["layer"])}</b><div class="note">{E(l["of"])}</div>', f'<b>{E(l["value"])}</b>', _bar(l, top), f'<a href="#f-{E(l["family"])}">{E(fam[l["family"]]["name"].replace(" signals", "")) if l["family"] in fam else "exposure"}</a>', pill(l['status']), src_links(l['sources'], 1)] for l in G['ladder']], 'ladder')
    fams = ''.join(f'''<article class="role" id="f-{E(f["id"])}"><h3>{E(f["name"])}</h3><p><i>{E(f["question"])}</i></p><p><b>Now.</b> {E(f["now"])} <span class="refs">{src_links(f["sources"], 1)}</span></p><p><b>What would change it.</b> {E(f["watch"])}</p><p class="small"><a href="../{E(f["page"])}">Where this site tracks it &rarr;</a></p></article>''' for f in G['families'])
    x0, x1 = _mins('2026-10-21T00:00Z'), _mins('2026-10-22T16:00Z')
    bars = table(['Barrier', 'Available', '21 Oct 00:00 &rarr; 22 Oct 16:00 UTC', 'A compromise after it says the organisation had', 'Sources'],
                 [[f'<b>{E(b["what"])}</b>', E(_hm(b['at'])) if b['at'] else '<i>not a release</i>', _tl(b['at'], x0, x1) + f'<div class="note">{E(b["at_note"])}</div>', E(b['gap']), src_links(b['sources'], 1)] for b in G['barriers']], 'ladder')
    reading = ''.join(f'<li>{E(r)}</li>' for r in G['reading'])
    story = next((a for a in ARTICLES if a['slug'] == 'exposed-is-not-exploited'), None)
    body = f'''
<h1>The second stories: exposed, attempted, exploited, and what was within reach</h1>
<p class="lead">{E(G["note"])}</p>
{section("ladder", "From exposed to what matters", f'<p>Each layer is a smaller population than the one above, until the evidence runs out. The two bars are counts of the same thing, hosts, on one linear scale: 1.57 million of 2.6 million were unpatched on the first day; a dashed box is a layer nobody has measured; a single line is zero. The units change down the ladder, from a share of websites to hosts to attempts, and the ladder says so rather than drawing them as one funnel.</p>{ladder}')}
{section("families", "The four kinds of signal", f'<div class="roles">{fams}</div>', "The editor's four families: what each would show, what it shows now, and what would change it.")}
{section("barriers", "Every barrier has a time", f'<p>The barriers between this bug and a breach, with the moment each became available. A dot is a stated time; a band is a day with no time given. Read across: a compromise after the dot says something about the organisation, not only about PHP.</p>{bars}')}
{section("reading", "The reading", f'<ul>{reading}</ul><p class="small">This page is the site\'s analysis, marked as research because every row rests on captured sources; the argument it supports is made in {f"<a href=../articles/{E(story["slug"])}/index.html>{E(story['title'])}</a>" if story else "a story"}.</p>')}
'''
    page('signals/index.html', 'The second stories: exposed, attempted, exploited, and what was within reach', 'php2shell as signals: the ladder from websites that use PHP to the sites that were exploited and held something worth reaching, the four kinds of signal and what each shows now, and the time each barrier became available.', body, kind='analysis', topics='php2shell signals exposure reach second stories')


# ----------------------------------------------------------------------------- items and feeds (v0.4.2)
# Everything a reader can read here is an item with a stable id and a hash of what it says. The ledger's sections,
# pages, briefings and facts keep their own versions (data/sections.json); stories, questions, sources and timeline
# events are versioned here, by hash only, in data/items.json, which the build reads back so an item keeps its
# version until what it says changes. The pages carry each item's id and hash in a hidden marker (.it); the reader's
# browser compares them with what it last read (assets/reader-state.js). The feeds are made from the same items.
import datetime
from email.utils import format_datetime

ITEMS_PATH = os.path.join(DATA, 'items.json')
ITEMS_PREV = (json.load(open(ITEMS_PATH, encoding='utf-8')).get('items', {}) if os.path.exists(ITEMS_PATH) else {})
ITEMS = OrderedDict()
FEED_ZONES = OrderedDict([('all', ('Everything', 'every new or changed fact, page, briefing, story, question, source and dated event')),
                          ('for-you', ('For you', 'the questions readers ask, the briefings, and the start-here pages')),
                          ('research', ('Research', 'the incident, the analysis and the evidence: facts, sources captured, dated events')),
                          ('stories', ('Stories', 'stories written here, signed and dated')),
                          ('site', ('About the site', 'the method, the vaults, the billing model and the site\'s own pages'))])
KIND_WORD = {'fact': 'Fact', 'page': 'Page', 'briefing': 'Briefing', 'front': 'Front page', 'story': 'Story', 'question': 'Question', 'source': 'Source', 'event': 'Timeline'}

def zone_of(path):
    for label, items in NAV:
        if any(pp == path for pp, _ in items):
            return {'For you': 'for-you', 'Research': 'research', 'Stories': 'stories', 'Site': 'site'}.get(ZONES.get(label, ''), 'site')
    if path.startswith(('facts/', 'sources/', 'actors/')):
        return 'research'
    if path.startswith('articles/'):
        return 'stories'
    if path.startswith(('briefings/', 'questions/')):
        return 'for-you'
    return 'site'

def item(iid, kind, zone, title, path, text, date):
    """Register an item, keep its version while its hash holds; return the hidden marker that goes on the page."""
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()[:12]
    prev = ITEMS_PREV.get(iid)
    if prev and prev.get('hash') == h:
        v, first, changed, d = prev['v'], prev['first'], prev['changed'], prev['date']
    elif prev:
        v, first, changed, d = prev['v'] + 1, prev['first'], VERSION, REL_DATE.get(VERSION) or date
    else:
        v, first, changed, d = 1, VERSION, VERSION, date or REL_DATE.get(VERSION, '')
    ITEMS[iid] = {'kind': kind, 'zone': zone, 'title': title, 'path': path, 'hash': h, 'v': v, 'first': first, 'changed': changed, 'date': d}
    return f'<span class="it" data-item="{E(iid)}" data-h="{h}" data-n="{v}"></span>'

def it_ledger(sid):
    sec = LEDGER['sections'].get(sid)
    if not sec or not sec['versions']:
        return ''
    v = sec['versions'][-1]
    return f'<span class="it" data-item="{E(sid)}" data-h="{E(v["hash"])}" data-n="{v["v"]}"></span>'

def event_id(t):
    when = re.sub(r'[^0-9T]', '', t['at'])[:13]
    return 'ev-' + when + '-' + hashlib.sha256((t['at'] + '|' + ','.join(t['sources'])).encode()).hexdigest()[:6]

def it_event(t):
    return item(event_id(t), 'event', 'research', t['event'][:120], 'timeline/index.html',
                json.dumps([t['event'], t['confidence'], t['sources'], t.get('note')], ensure_ascii=False), parse_when(t['at']) or '')

def it_source(src):
    caps = sorted(parse_when(c.get('stamp')) or '' for c in src.get('captures', []))
    text = json.dumps([src.get('title'), src.get('status'), src.get('url'), [c.get('stamp') for c in src.get('captures', [])], src.get('notes_md') or ''], ensure_ascii=False)
    return item('src-' + src['slug'], 'source', 'research', ((src.get('publisher') or '') + ': ' + (src.get('title') or src['slug']))[:140],
                f'sources/{src["slug"]}/index.html', text, caps[-1] if caps else '')

def it_question(q):
    return item('q-' + q['id'], 'question', 'for-you', q['q'], f'questions/{q["id"]}/index.html', json.dumps(q, ensure_ascii=False, sort_keys=True), '')

def it_story(a):
    return item('story-' + a['slug'], 'story', 'stories', a['title'], f'articles/{a["slug"]}/index.html', a.get('text') or a['title'], str(a.get('written') or ''))

def all_items():
    """The ledger's items and the registry's, one list: what data/items.json and the feeds are made from."""
    out = OrderedDict()
    for sid, sec in LEDGER['sections'].items():
        if not sec['versions']:
            continue
        v = sec['versions'][-1]
        z = 'research' if sec['kind'] in ('front', 'fact') else 'for-you' if sec['kind'] == 'briefing' else zone_of(sec['path'])
        out[sid] = {'kind': sec['kind'], 'zone': z, 'title': sec['title'], 'path': sec['path'] + ('#' + sid[len('front-'):] if sec['kind'] == 'front' else ''),
                    'hash': v['hash'], 'v': v['v'], 'first': sec['versions'][0]['site'], 'changed': v['site'], 'date': v['date'],
                    'history': f'versions/{sid}/index.html'}
    for iid, it in ITEMS.items():
        out[iid] = it
    return out

def rfc822(d):
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?', d or '') or re.match(r'^(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?', REL_DATE.get(VERSION) or '2026-10-22')
    hh, mm = (int(m.group(4)), int(m.group(5))) if m.group(4) else (0, 0)
    return format_datetime(datetime.datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), hh, mm, tzinfo=datetime.timezone.utc))

def feed_entries(zone):
    """One entry per item version the build knows: the ledger keeps every version; the registry its current one."""
    out = []
    for iid, it in all_items().items():
        if zone != 'all' and it['zone'] != zone:
            continue
        sec = LEDGER['sections'].get(iid)
        versions = [(x['v'], x['date'], x['site']) for x in sec['versions']] if sec else [(it['v'], it['date'], it['changed'])]
        for n, date, site in versions:
            out.append({'id': iid, 'n': n, 'date': date or REL_DATE.get(site, ''), 'site': site, 'it': it})
    out.sort(key=lambda e: (e['date'] or '', e['site'], e['id'], e['n']), reverse=True)
    return out[:150 if zone == 'all' else 80]

def build_feeds_xml():
    for zone, (name, what) in FEED_ZONES.items():
        items = ''
        for e in feed_entries(zone):
            it = e['it']
            word = 'New' if e['n'] == 1 else f'Updated (v{e["n"]})'
            desc = f'{KIND_WORD.get(it["kind"], it["kind"].title())}. ' + (f'{word} in site v{e["site"]}.' if e['id'] in LEDGER['sections'] or e['n'] > 1 else f'Dated {e["date"].replace("T", " ").rstrip("Z")}.')
            if it.get('history') and e['n'] > 1:
                desc += f' What changed: {BASE_URL}/{it["history"]}'
            title = KIND_WORD.get(it['kind'], '') + ': ' + it['title'] + ('' if e['n'] == 1 else ' (updated)')
            items += (f'<item><title>{E(title)}</title><link>{E(BASE_URL + "/" + it["path"])}</link>'
                      f'<guid isPermaLink="false">{E(e["id"])}@v{e["n"]}</guid><pubDate>{rfc822(e["date"])}</pubDate>'
                      f'<category>{E(it["kind"])}</category><description>{E(desc)}</description></item>\n')
        head = ('<?xml version="1.0" encoding="utf-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
                f'<title>{E(SITE_NAME)}: {E(name)}</title>\n<link>{BASE_URL}/</link>\n'
                f'<atom:link href="{BASE_URL}/feeds/{zone}.xml" rel="self" type="application/rss+xml"/>\n'
                f'<description>{E(SITE_NAME)}: {E(what)}. A new entry when an item is new, and again each time what it says changes.</description>\n'
                f'<language>en-gb</language>\n<lastBuildDate>{rfc822(REL_DATE.get(VERSION, ""))}</lastBuildDate>\n')
        write(f'feeds/{zone}.xml', head + items + '</channel>\n</rss>\n')

def save_items():
    OUTPUTS.add('data/items.json')
    doc = {'about': 'Every item a reader can read on this site, with its id, zone, link and the hash of what it says now. '
                    'assets/reader-state.js compares the hashes with what the reader last read, in their browser.',
           'site': VERSION, 'items': all_items()}
    out = json.dumps(doc, indent=0, ensure_ascii=False) + '\n'
    old = open(ITEMS_PATH, encoding='utf-8').read() if os.path.exists(ITEMS_PATH) else ''
    if out != old:
        write('data/items.json', out)

def feed_links(path):
    up, z = '../' * path.count('/'), zone_of(path)
    out = f'<link rel="alternate" type="application/rss+xml" title="{E(SITE_NAME)}: everything new and changed" href="{up}feeds/all.xml">'
    if z != 'all':
        out += f'\n<link rel="alternate" type="application/rss+xml" title="{E(SITE_NAME)}: {E(FEED_ZONES[z][0])}" href="{up}feeds/{z}.xml">'
    return out

def build_feeds_page():
    rows = ''.join(f'<article class="feedrow"><h3>{E(name)} <code>feeds/{z}.xml</code></h3><p>{E(what[0].upper() + what[1:])}.</p>'
                   f'<p class="small"><a href="../feeds/{z}.xml">The feed</a> &middot; <a href="../reader/index.html#site-{z}">read it here, with what you have read marked</a> &middot; '
                   f'or copy <code>{BASE_URL}/feeds/{z}.xml</code> into any feed reader</p></article>' for z, (name, what) in FEED_ZONES.items())
    body = f"""
<h1>Feeds: what is new and what changed, wherever you read</h1>
<p class="lead">Five RSS feeds: one for everything, one for each part of the site. An item enters a feed when it is new, and again every time what it says changes, so a fact that moves from reported to confirmed reaches you as an entry of its own, with a link to what changed. The release log has an Atom feed of its own, <a href="../feed.xml">feed.xml</a>.</p>
{rows}
<h2>Feeds from elsewhere</h2>
<p>The <a href="../reader/index.html">feed viewer</a> reads these feeds, the outside sources a browser is allowed to read directly (the CVE records, NVD, OSV, CISA's list of exploited flaws, Hacker News, Mastodon, GitHub), and any feed you add. What you have read is kept in your browser, with the rest of <a href="../you/index.html">your desk</a>.</p>
"""
    page('feeds/index.html', 'Feeds: what is new and what changed', 'RSS feeds for everything new and changed on this site and for each of its parts: an entry for every new item and every change, and where to read them.', body, kind='site')


# ----------------------------------------------------------------------------- yours: your desk and the feed viewer (v0.4.2)

def build_you():
    body = """
<h1>Your desk: what is new to you, and what changed since you read it</h1>
<p class="lead">This site keeps track of what you have read, in your browser, so the next visit costs you only what changed. Mark an item read (the circle beside it), or the whole page, or everything at once: from then on you see only what is new, and anything that changes after you read it comes back marked as changed, with a link to the change. The <b>&#8943;</b> beside any item takes a decision (read later, follow up, not for me) or a note of your own: a correction, a comment, an idea.</p>
<div id="desk"><p class="small">Your desk needs JavaScript: it is built in your browser from what this browser has kept.</p></div>
<h2>Where this is kept</h2>
<p>Only in this browser: what you read is under <code>p2s.reader.v1</code>, your decisions and notes under <code>sgit.notes.v1</code> in the same record format as <a href="https://newsroom.sgit.ai/">newsroom.sgit.ai</a>, the feeds you add under <code>p2s.feeds.v1</code>. Nothing is sent anywhere. Export your desk to keep it or to move it to another browser; the next step, from the newsroom, is to carry it into a vault of your own, encrypted, across your devices. How the site decides what is new and changed is in <a href="../admin/briefs/index.html#2026-10-22__feeds-the-delta-and-subscriptions">the brief</a>.</p>
<script src="../assets/desk.js" defer></script>
"""
    page('you/index.html', 'Your desk: what is new to you, and what changed', 'What is new to you on this site and what changed since you read it, by part of the site; what you put aside; your notes; all kept in your browser, exportable.', body, kind='account')

def build_reader():
    F = D['feed-sources']
    cfg = J({'feeds': F['feeds']}, ensure_ascii=False, separators=(',', ':'))
    body = f"""
<h1>The feed viewer: this site, the records, and your own feeds</h1>
<p class="lead">Every feed here is read by your browser, directly from its publisher, and what you have read in each is kept with the rest of <a href="../you/index.html">your desk</a>: the next time you come, a feed shows you only what is new or changed. This site's own <a href="../feeds/index.html">feeds</a> are first; then the outside sources a browser is allowed to read (the CVE records, NVD, OSV, CISA's catalog of exploited flaws, GitHub, Wikipedia, Hacker News, Mastodon); then the ones that do not allow it, and why. Add any feed you like below the list.</p>
<div id="viewer" class="fv"><p class="small">The viewer needs JavaScript.</p></div>
<script type="application/json" id="viewer-config">{cfg}</script>
<h2>What the viewer does with a feed</h2>
<ul>
<li>Your browser fetches it, with no cookies and no referrer, from the publisher; nothing goes through this site or anyone else.</li>
<li>Only https feeds, and never an address on your own network. At most 2 MB is read (5 MB for a records API), within 15 seconds.</li>
<li>A feed is shown as text: titles and summaries are parsed by the browser and only their words kept, so nothing in a feed can run on this page. Links open in a new tab, only when they are web links.</li>
<li>A publisher that does not allow other sites' pages to read its feed (no CORS header) cannot be read here. The viewer says so rather than routing it through a third party, which would see what you read. {E(F["about"].split(". ")[0])} on {E(F["checked"])}.</li>
</ul>
<script src="../assets/feed-viewer.js" defer></script>
"""
    page('reader/index.html', 'The feed viewer: this site, the records, and your own feeds', 'Read this site\'s feeds, the CVE records, NVD, OSV, CISA KEV, GitHub, Wikipedia, Hacker News and Mastodon, and any feed you add, in your browser, with what you have read marked and only what is new shown next time.', body, kind='account')


# ----------------------------------------------------------------------------- your stack: the blast radius (v0.8.1)

def stack_catalogue():
    """data/stack.json joined with the ranges, SAPIs and mitigations (affected), the edge vendors (defence) and the
    NCSC-NL inventory (software), for assets/stack.js. Everything in it is already published on this site."""
    st, a = D['stack'], D['affected']
    for v in st['vulns']:
        for slug in v['sources']:
            if slug not in SOURCES: sys.exit(f'data/stack.json: {v["id"]} cites unknown source {slug}')
    ctl = []
    for c in st['controls']:
        m = a['mitigations'][c['mitigation']]
        ctl.append(dict({k: c[k] for k in c if k != 'mitigation'}, what=m['what'], caveat=m['caveat'], **{'for': m['for']}))
    inv = []
    for r in D['software']['rows']:
        note = (r['notes'] or '').split('\n')
        inv.append([r['supplier'], r['product'], r['version'], r['status_109618'], r['status_109619'],
                    (note[-1] if len(note) > 1 else note[0])[:280], (r['links'] or [''])[0]])
    items = [[iid, it['title'], it['path'], it['kind']] for iid, it in all_items().items() if it.get('path')]
    return {'schema': st['schema'], 'site': VERSION, 'data_as_of': STORY['data_as_of'],
            'kinds': st['kinds'], 'links': st['links'], 'sensitivity': st['sensitivity'], 'controls': ctl, 'vulns': st['vulns'],
            'ranges': a['ranges'], 'ranges_note': a['ranges_note'], 'fixed': a['fixed'],
            'sapis': [{k: x[k] for k in ('sapi', 'risk', 'text')} for x in a['sapis']],
            'edge': [{k: x[k] for k in ('vendor', 'what', 'when', 'caveat')} for x in D['defence']['edge']],
            'inventory': {'source': D['software']['source'], 'commit': D['software']['commit'], 'licence': D['software']['licence'],
                          'columns': ['supplier', 'product', 'version', 'status_109618', 'status_109619', 'note', 'link'], 'rows': inv},
            'items': items, 'examples': st['examples'], 'pulse': st['pulse']}

def build_stack_catalogue():
    write('stack/catalogue.json', json.dumps(stack_catalogue(), ensure_ascii=False, separators=(',', ':'), sort_keys=False) + '\n')

def build_stack():
    st = D['stack']
    kinds = ''.join(f'<li><b>{E(k["name"])}.</b> {E(k["what"])}</li>' for k in st['kinds'])
    vulns = ''.join(f'<li><a href="../{U(v["page"])}">{E(v["id"])}</a>: {E(v["name"])}. Scope: {E(v["scope"])}; at worst {E(v["impact"])}.</li>' for v in st['vulns'])
    body = f"""
<h1>Your stack: what php2shell can reach in it</h1>
<p class="lead">Describe what you run, the way you would draw it on a whiteboard: what the internet reaches, what sits in front, the applications, the PHP under them and where it comes from, and what each can reach. The tool checks every PHP runtime against the two flaws with what this site knows (the version ranges, how PHP serves requests, the settings that reduce exposure, the edge rules, the NCSC-NL inventory) and shows the blast radius: what an attacker who runs code as your PHP worker can touch. Then it lists what on this site is about your stack.</p>
<div id="stack" class="sk"><p class="small">The tool needs JavaScript: it runs in your browser, on <a href="catalogue.json">its catalogue</a>, and sends nothing anywhere.</p></div>
<h2>How it decides</h2>
<ul>
<li><b>The version.</b> A runtime on a supported branch is affected below the fixed release ({E(', '.join(D['affected']['fixed']))}) and fixed at or above it. 8.1, 8.0 and 7.4 are affected with no upstream release, only backport branches; earlier versions have no fix at all. {E(D['affected']['ranges_note'])}</li>
<li><b>Where the PHP comes from.</b> A distribution package or a vendor image keeps its own version number when it backports a fix, so a version that looks old can be fixed. When the runtime is provided by a product in the inventory, the inventory's status for that product wins over the version number, and the tool says so.</li>
<li><b>How it serves requests.</b> The risk is for PHP serving web requests; Apache mod_php is where remote code execution was demonstrated. CLI, cron and queue workers are outside the advisory's scope.</li>
<li><b>Whether it can be reached.</b> A runtime the internet reaches, through an edge or not, is exposed; one reached only from inside is not exposed from the internet, which is not the same as safe.</li>
<li><b>What reduces it.</b> Each setting and each edge rule is shown with its caveat. None of them turns an affected runtime into a fixed one: updating is the only reliable mitigation.</li>
<li><b>The blast radius.</b> Remote code execution runs as the PHP worker, so everything an affected runtime runs, and everything it or its applications can reach, is in the blast radius; what those can reach in turn is one step further.</li>
</ul>
<p>The kinds of component:</p>
<ul>{kinds}</ul>
<p>What is checked today:</p>
<ul>{vulns}</ul>
<p class="small">{E(st['pulse'])}</p>
<h2>Where your stack is kept</h2>
<p>In this browser, under <code>p2s.stack.v1</code>, and in your own vault when you open it in the Ask pane (under <code>/php-october/stack/</code>, encrypted here before it leaves), with the rest of what you keep on this site. Export it as a file to share it with your team; import theirs. Nothing about your stack is sent to this site or anyone else. A stack describes your systems: treat the file as you would an architecture diagram.</p>
<p class="small">This is a first version, a thinking tool and not a scanner: it knows only what you tell it and what this site has captured. Check every finding against your own systems and your vendor's advisory.</p>
<script src="../assets/stack.js" defer></script>
"""
    page('stack/index.html', 'Your stack: what php2shell can reach in it', 'Describe what you run, the internet, the edge, the applications, the PHP and where it comes from, and what each can reach; see which runtimes the two flaws affect, the blast radius, what to do first and what on this site is about your stack. In your browser and your own vault.', body, kind='account')

# ----------------------------------------------------------------------------- subscriptions (v0.4.3)

def build_subscribe():
    sc = D['subscriptions']
    cfg = J({k: sc[k] for k in ('contact', 'endpoint', 'vault_id', 'append_token', 'recipient', 'zones', 'cadences')}, ensure_ascii=False, separators=(',', ':'))
    zones = ''.join(f'<label class="sub-c"><input type="checkbox" name="zones" value="{E(z)}"{" checked" if z == "all" else ""}> {E(t)}</label>' for z, t in sc['zones'])
    cads = ''.join(f'<label class="sub-c"><input type="radio" name="cadence" value="{E(c)}"{" checked" if i == 1 else ""}> {E(t)}</label>' for i, (c, t) in enumerate(sc['cadences']))
    mail = f'mailto:{sc["contact"]}?subject=' + 'Subscribe%20to%20PHP%20October%202026' + '&body=' + 'Please%20subscribe%20me.%20Follow%3A%20everything%20%2F%20research%20%2F%20for%20you%20%2F%20stories.%20How%20often%3A%20as%20it%20changes%20%2F%20daily%20%2F%20weekly.'
    body = f"""
<h1>Subscribe: what changed, sent to you</h1>
<p class="lead">The cheapest way to follow this story is to be told only what changed. Pick what to follow and how often, and the agent at <a href="mailto:{E(sc["contact"])}">{E(sc["contact"])}</a> sends it: a message per release that changes what you follow, or a digest. No account; one address. Or skip email entirely: the <a href="../feeds/index.html">feeds</a> carry the same changes.</p>
<form id="sub-form" class="subform" autocomplete="on">
<p><label>Your email address<br><input type="email" name="email" required maxlength="254" placeholder="you@example.org"></label></p>
<fieldset><legend>What to follow</legend>{zones}</fieldset>
<fieldset><legend>How often</legend>{cads}</fieldset>
<p><label>Anything we should know (optional)<br><textarea name="note" rows="2" maxlength="500"></textarea></label></p>
<p class="sub-hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
<p><button class="cta cta-pri" type="submit" name="kind" value="subscribe">Subscribe</button> <button class="cta" type="submit" name="kind" value="unsubscribe" formnovalidate>Unsubscribe this address</button></p>
<p id="sub-out" role="status" aria-live="polite"></p>
</form>
<script type="application/json" id="sub-config">{cfg}</script>
<p>Rather write? <a href="{E(mail)}">Email {E(sc["contact"])}</a> and say what you want to follow.</p>
<h2>What happens to your address</h2>
<ul>
<li>It is encrypted in your browser, to the subscriptions vault's key (<code>{E(sc["recipient"]["fingerprint"])}</code>), and posted to a write-only lane on that private vault (<code>{E(sc["vault_id"])}</code>). The lane answers the same whatever arrives, so this page can say it was sent, never that it was received.</li>
<li>Anyone can type any address, so the agent writes to it first and sends nothing more until the address answers. Unsubscribe here, or by answering any message.</li>
<li>It is kept in that vault and nowhere else: not on this site, not in its repository, not in its telemetry. The vault's key is held by the editor and the agent that sends.</li>
<li>Messages come from {E(sc["contact"])}, the agent the editor runs and reads, until the newsroom has a domain of its own for them.</li>
</ul>
<script src="../assets/subscribe.js" defer></script>
"""
    page('subscribe/index.html', 'Subscribe: what changed, sent to you', 'Follow the PHP flaws story by email: everything or one part of the site, as it changes or as a digest; the address encrypted in your browser and confirmed before anything is sent.', body, kind='account')




# ----------------------------------------------------------------------------- the phone app: Now (v0.5.0)
# The editor's brief: admin/content/briefs/2026-10-22__brief__the-phone-app.md. One page, now/index.html, built for a
# phone: what do I need to know, given how long I have (one, five, ten or thirty minutes), against what I read before.
# Two modes. Deterministic: the items, their order and their connections come from the data and nothing else.
# Agentic: the same items handed to a model (OpenRouter, with the reader's own key kept in the reader's own vault), for
# a briefing in prose, an infographic and a chat. The page is a shell; now/now.json is everything it reads; assets/now.js
# is the app. The reader's state lives in this browser (assets/reader-state.js, shared with the rest of the site) and,
# when the reader opens a vault, in that vault under /php-october/.

NOW_MODELS = {'text': 'anthropic/claude-sonnet-5.5', 'image': 'google/gemini-3.1-flash-image'}
NOW_KIND_WEIGHT = {'front': 100, 'fact': 80, 'event': 60, 'question': 55, 'briefing': 50, 'story': 45, 'page': 30, 'source': 10}

def now_summary(iid, it):
    """The words the app shows for an item: what it says now, in a sentence or two, and its connections."""
    k, links, status = it['kind'], [], ''
    if k == 'fact':
        c = next((c for c in D['claims'] if 'fact-' + c['id'] == iid), None)
        if c:
            status = c['status']
            links = [['source', s, short_name(SOURCES[s]), f'sources/{s}/index.html'] for s in c['sources'] if s in SOURCES]
            links += [['briefing', p, PERSONAS[p]['label'], f'briefings/{p}/index.html'] for p, t in BRIEF_TOPICS.items() if c['topic'] in t and p in PERSONAS]
            claim = c['claim'].rstrip()
            return f'{claim}{"" if claim.endswith((".", "?", "!")) else "."} Who says it: {c["by"]}.', status, links
    if k == 'event':
        t = next((t for t in D['timeline'] if event_id(t) == iid), None)
        if t:
            links = [['source', s, short_name(SOURCES[s]), f'sources/{s}/index.html'] for s in t['sources'] if s in SOURCES]
            return f'{fmt_at(t["at"])}: {t["event"]}', t.get('confidence', ''), links
    if k == 'question':
        q = next((q for q in D['questions']['questions'] if 'q-' + q['id'] == iid), None)
        if q:
            return q.get('short') or q['q'], '', [['page', p, nav_title(p), p] for p in (q.get('see') or [])[:4]]
    if k == 'briefing':
        p = PERSONAS.get(iid.replace('briefing-', ''))
        if p:
            return p['answer'], '', [['page', x, nav_title(x), x] for x in p['path'][1:]]
    if k == 'front':
        sec = LEDGER['sections'].get(iid)
        if sec:
            t = re.sub(r'\s*\[[^\]]*\]', '', sec['versions'][-1]['text'])
            t = re.sub(r'(?m)^(confirmed|reported|disputed|contradicted|unverified): ', '', t)
            t = ' '.join(x.strip().rstrip('.') + '.' for x in t.split('\n') if x.strip())
            return (t[:420].rsplit('. ', 1)[0] + '.') if len(t) > 420 else t, '', []
    if k == 'source':
        s = SOURCES.get(iid.replace('src-', ''))
        if s:
            return (s.get('notes') or s.get('title') or '')[:300], s.get('status', ''), []
    if k == 'story':
        a = next((a for a in ARTICLES if 'story-' + a.get('slug', '') == iid), None)
        if a:
            return (a.get('dek') or a.get('standfirst') or a.get('text') or a['title'])[:400], '', []
    return D['plain']['pages'].get(it['path'], '') or it['title'], '', []

def build_now():
    items = []
    for iid, it in all_items().items():
        text, status, links = now_summary(iid, it)
        words = len((it['title'] + ' ' + text).split())
        title = it['title']
        if it['kind'] == 'fact':
            c = next((c for c in D['claims'] if 'fact-' + c['id'] == iid), None)
            title = c['claim'] if c else title
        items.append({'id': iid, 'kind': it['kind'], 'zone': it['zone'], 'title': title, 'path': it['path'], 'hash': it['hash'],
                      'v': it['v'], 'first': it['first'], 'changed': it['changed'], 'date': it['date'], 'text': text, 'status': status,
                      'links': links[:8], 'w': NOW_KIND_WEIGHT.get(it['kind'], 20), 'sec': max(10, round(words / 230 * 60)),
                      'history': it.get('history', '')})
    pl = D['plain']
    doc = {
        'about': 'Everything the phone app (now/) reads, built from the same data as every page: the items a reader can read, '
                 'with what each says now, its hash, its connections and its reading time; the situation; the readers; the facts '
                 'for grounding a model. Deterministic: the same data produces the same file.',
        'site': VERSION, 'data_as_of': STORY['data_as_of'], 'when': human_time(STORY['data_as_of']),
        'releases': [{'version': r['version'], 'date': r['date'], 'title': r['title']} for r in reversed(RELEASES)][:20],
        'headline': pl['headline'], 'deck': re.sub(r'<[^>]+>', '', pl['deck']),
        'now': [{'text': x['text'], 'sources': [[s, short_name(SOURCES[s])] for s in x['sources'] if s in SOURCES]} for x in pl['now']],
        'unknown': [u['text'] for u in pl['unknown']],
        'facts': [{'text': f['text'], 'status': f['status'], 'href': f['href']} for f in pl['facts']],
        'personas': [{'id': p['id'], 'person': p['person'], 'label': p['label'], 'group': p['group'], 'depth': p['depth'], 'answer': p['answer'],
                      'path': p['path']} for p in PERSONAS.values()],
        'claims': [{'id': c['id'], 'status': c['status'], 'claim': c['claim'], 'by': c['by'], 'topic': c['topic']} for c in D['claims']],
        'models': NOW_MODELS,
        'vault': {'endpoint': 'https://dev.send.sgraph.ai', 'folder': '/php-october'},
        'items': items,
    }
    write('now/now.json', json.dumps(doc, ensure_ascii=False, separators=(',', ':')) + '\n')
    write('now/manifest.webmanifest', json.dumps({
        'name': 'PHP October 2026: Now', 'short_name': 'PHP Now', 'start_url': './index.html', 'scope': './', 'display': 'standalone',
        'background_color': '#f7f6f2', 'theme_color': '#8a2416', 'description': 'What you need to know about the PHP flaws, for the time you have.',
        'icons': [{'src': '../assets/now/icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '../assets/now/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]},
        indent=1) + '\n')
    title = 'Now: PHP October on your phone'
    desc = 'What you need to know about the PHP flaws for the time you have, one, five, ten or thirty minutes, against what you read before; deterministic from the data, or written by a model with your own key kept in your own vault, with a chat.'
    PAGES.append(('now/index.html', title, desc, 'account'))
    html_out = f'''<!doctype html>
<html lang="en" data-root="../" data-path="now/index.html" data-ver="{VERSION}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#8a2416">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="PHP Now">
<title>{E(title)} &middot; {SITE_NAME}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{BASE_URL}/now/index.html">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="../assets/now/icon-192.png">
<link rel="icon" href="data:,">
<link rel="alternate" type="text/markdown" href="index.md">
<link rel="stylesheet" href="../assets/now/now.css">
<script src="../assets/reader-state.js" defer></script>
<script src="../assets/telemetry.js" defer></script>
<script type="module" src="../assets/now/now.js"></script>
</head>
<body>
<div id="app" class="app">
<header class="top"><a class="brand" href="../index.html">PHP October<span> 2026</span></a><span class="b-now">Now</span><button class="vchip" id="vchip" type="button">This phone only</button></header>
<main id="view"><section class="card"><h1>What you need to know, for the time you have</h1><p>{E(pl["headline"])}. {E(re.sub(r"<[^>]+>", "", pl["deck"]))}</p><p>This app needs JavaScript. Without it, start from <a href="../index.html">the front page</a> or <a href="../whatsnew/index.html">what's new</a>.</p></section></main>
<nav class="tabs" id="tabs"><a href="#now" data-tab="now">Now</a><a href="#chat" data-tab="chat">Ask</a><a href="#vault" data-tab="vault">Vault &amp; keys</a></nav>
</div>
</body>
</html>
'''
    write('now/index.html', html_out)
    md = f'''# {title}

{desc}

> For you: an app in your browser, kept by the agents that run this site.

The phone app at {BASE_URL}/now/index.html answers one question: what do I need to know now, given how long I have? Choose one, five, ten or thirty minutes; it shows what is new or changed since you last read it, most important first, until the time is used. If nothing is new, it says so.

## Two modes

- **Deterministic**: the items, their order and their connections (each fact to its sources and to the briefings that carry it) come from the site's data and nothing else. The same data gives the same answer.
- **Agentic**: the same items handed to a model through OpenRouter with your own key: a briefing in prose for your time budget (Claude Sonnet), an infographic (Gemini), and a chat grounded in the site's facts. Every generated piece says which model wrote it from which items, and links each claim back to its fact.

## Your vault

Open a vault (an sgit vault key; a newsroom.sgit.ai reader vault works) or create one, and the app keeps in it, encrypted in your browser before it leaves: what you have read, your settings, your OpenRouter key, your chats and what the models made for you, under `/php-october/`. Without a vault, what you have read is kept in this browser only and the agentic mode is off.

The data the app reads is [now.json]({BASE_URL}/now/now.json). The brief is on [the briefs page]({BASE_URL}/admin/briefs/index.html).

---
site v{VERSION} · data as of {STORY["data_as_of"]} · {BASE_URL}/now/index.html
'''
    write('now/index.md', md)
# ----------------------------------------------------------------------------- the fact-check desk (factcheck@php.newsroom)

FC = load('factcheck') if os.path.exists(os.path.join(DATA, 'factcheck.json')) else None
FCA = {a['id']: a for a in FC['assessments']} if FC else {}
FCL = {l['n']: l for l in FC['levels']} if FC else {}
FC_KIND_WORD = {'record': 'Record', 'event': 'Event', 'state': 'State', 'count': 'Count', 'quote': 'Quote', 'attribution': 'Attribution', 'reading': 'Opinion', 'advice': 'Advice'}

def assure(cid, short=False):
    """The desk's grade for a claim as a badge: the level's code, name and a six-dot meter, so it never rests on colour alone."""
    a = FCA.get(cid)
    if not a:
        return '<span class="as as-none" title="Not yet checked by the fact-check desk">not checked</span>'
    n = a['display']
    lv = FCL[n]
    dots = '&#9679;' * n + '&#9675;' * (6 - n)
    if a['verdict'] == 'refuted':
        b = f'<span class="as as-ref" title="Refuted: a stronger source says otherwise">refuted</span>'
    else:
        b = f'<span class="as as-{n}" title="{E(lv["means"])}"><b>{E(lv["code"])}</b> {E(lv["name"])}<i aria-hidden="true">{dots}</i></span>'
    if short:
        return b
    extra = ''
    if a['kind'] == 'reading':
        extra += ' <span class="as-k">opinion</span>'
    if a.get('tension', 'none') not in ('none',):
        extra += f' <span class="as-k as-t">{E(a["tension"].replace("-", " "))}</span>'
    if a.get('status_fit') == 'overstated':
        extra += ' <span class="as-k as-t" title="The status word claims more than the evidence carries">status overstated</span>'
    return b + extra

def fc_status_line(cid, depth):
    a = FCA.get(cid)
    if not a:
        return ''
    t = ''.join(f' <a href="{"../" * depth}factcheck/index.html#{E(l)}">{E(l)}</a>' for l in a.get('tickets', []))
    return f'<div class="note"><b>Fact-check:</b> {assure(cid)} {E(a["reason"])}{(" Tickets:" + t) if t else ""}</div>'

def fc_section(cid):
    a = FCA.get(cid)
    if not a:
        return section('factcheck', 'Fact-check', '<p class="small">Not yet checked by the <a href="../../factcheck/index.html">fact-check desk</a>.</p>') if FC else ''
    rows = [[f'<a href="../../sources/{E(x["source"])}/index.html">{E(x["source"])}</a>' if x['source'] in SOURCES else f'{E(x["source"])} <span class="small">(in the vault, not yet on this site)</span>',
             E(x['result']), f'<q>{E(x["excerpt"])}</q>' if x.get('excerpt') else '<i>nothing that carries it</i>', f'<code title="{E(x.get("file", ""))}">{E((x.get("sha256") or "")[:16])}</code>'] for x in a.get('checked', [])]
    tk = ', '.join(f'<a href="../../factcheck/index.html#{E(l)}">{E(l)}</a>' for l in a.get('tickets', []))
    inner = (f'<p>{assure(cid)} &middot; {E(FC_KIND_WORD.get(a["kind"], a["kind"]))} &middot; verdict: <b>{E(a["verdict"].replace("-", " "))}</b>'
             f'{" &middot; the status word overstates the evidence" if a.get("status_fit") == "overstated" else ""}{" &middot; the status word understates the evidence" if a.get("status_fit") == "understated" else ""}</p>'
             f'<p>{E(a["reason"])}</p>' + (table(['Capture checked', 'Result', 'What it says', 'sha256 of the text read'], rows) if rows else '') +
             (f'<p>Open tickets: {tk}.</p>' if tk else '') + f'<p class="small">Graded in {E(a.get("run", ""))}, resting on captures up to {E(fmt_at(parse_when(a.get("as_of")) or "") if a.get("as_of") else "")}. The scale is on <a href="../../factcheck/index.html#ladder">the fact-check page</a>.</p>')
    return section('factcheck', 'Fact-check', inner)

def build_factcheck():
    if not FC:
        return
    A, K, T, R = FC['assessments'], FC['contradictions'], FC['tickets'], FC['runs']
    claims = {c['id']: c for c in D['claims']}
    by_lv = Counter(a['display'] for a in A if a['verdict'] != 'refuted')
    refuted = sum(1 for a in A if a['verdict'] == 'refuted')
    flagged = {c for t in T if t['type'] in ('finding', 'gap') and t['severity'] in ('medium', 'high') and t['status'] in ('open', 'acknowledged') for c in t['claims']}
    comfy = [a for a in A if a['display'] >= 5 and a['verdict'] == 'holds' and a.get('tension', 'none') == 'none' and a['kind'] != 'reading' and a['id'] not in flagged]
    over = [a for a in A if a.get('status_fit') == 'overstated']
    open_t = [t for t in T if t['status'] in ('open', 'proposed', 'acknowledged')]
    last = R[-1] if R else {}
    ladder = table(['Level', 'Means', 'Claims now'], [[f'<span class="as as-{l["n"]}"><b>{E(l["code"])}</b> {E(l["name"])}<i aria-hidden="true">{"&#9679;" * l["n"] + "&#9675;" * (6 - l["n"])}</i></span>', E(l['means']), str(by_lv.get(l['n'], 0))] for l in FC['levels']] +
                   [['<span class="as as-ref">refuted</span>', 'A stronger source says otherwise', str(refuted)]])
    rows = []
    for a in sorted(A, key=lambda a: (-a['display'] if a['verdict'] != 'refuted' else 1, a['id'])):
        c = claims[a['id']]
        tk = ' '.join(f'<a href="#{E(l)}">{E(l)}</a>' for l in a.get('tickets', []))
        rows.append(f'<tr data-lv="{-1 if a["verdict"] == "refuted" else a["display"]}" data-kind="{E(a["kind"])}" data-t="{E(a.get("tension", "none"))}" data-v="{E(a["verdict"])}" data-f="{1 if a["id"] in flagged else 0}">'
                    f'<td><a href="../facts/{E(a["id"])}/index.html">{E(c["claim"])}</a><div class="note">{E(a["reason"])}</div></td>'
                    f'<td>{assure(a["id"])}</td><td>{E(FC_KIND_WORD.get(a["kind"], a["kind"]))}</td><td>{E(a["verdict"].replace("-", " "))}</td><td>{pill(c["status"])}</td><td>{tk}</td></tr>')
    th = ''.join(f'<th>{h}</th>' for h in ['Claim, and why it is graded so', 'Fact-check', 'Kind', 'Verdict', 'Site status', 'Tickets'])
    grid = f'<div class="tw"><table class="t fc-grid"><thead><tr>{th}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
    filt = '''<form class="fc-filter" aria-label="Filter claims by assurance"><label>Show claims graded at least <select id="fc-min"><option value="-1">everything, refuted too</option><option value="0">A0</option><option value="2">A2 Reported</option><option value="4">A4 Corroborated</option><option value="5">A5 Confirmed</option><option value="6">A6 Established</option></select></label>
<label><input type="checkbox" id="fc-op" checked> include opinions</label> <label><input type="checkbox" id="fc-tn" checked> include contested</label> <button type="button" id="fc-comfy">Only what I can be very sure of</button> <span id="fc-n" class="small"></span></form>
<script>(function(){var m=document.getElementById("fc-min"),o=document.getElementById("fc-op"),t=document.getElementById("fc-tn"),n=document.getElementById("fc-n"),rs=document.querySelectorAll(".fc-grid tbody tr");
function f(){var k=0;rs.forEach(function(r){var s=+r.dataset.lv>=+m.value&&(o.checked||r.dataset.kind!=="reading")&&(t.checked||r.dataset.t==="none");if(+m.value>=5&&(r.dataset.v!=="holds"||r.dataset.f==="1"))s=false;r.hidden=!s;if(s)k++});n.textContent=k+" of "+rs.length+" claims shown";}
[m,o,t].forEach(function(x){x.addEventListener("change",f)});document.getElementById("fc-comfy").addEventListener("click",function(){m.value="5";o.checked=false;t.checked=false;f()});f();})();</script>'''
    ks = []
    for k in K:
        st = ''.join(f'<li><b>{E(s["who"])}</b>{(", " + E(s["when"])) if s.get("when") else ""}: <q>{E(s["says"])}</q> <span class="small">{E(s.get("measures", ""))}</span> {src_links([x for x in s.get("sources", []) if x in SOURCES], 1)}{"".join(f" <span class=small>(outside the vault: {E(u)})</span>" for u in s.get("outside", []))}</li>' for s in k['statements'])
        ks.append(f'<article class="role" id="{E(k["id"])}"><h3>{E(k["measure"])} <span class="st st-{"contradicted" if k["status"] == "open" else "confirmed"}">{E(k["status"])}</span></h3><ul>{st}</ul><p><b>The desk\'s reading.</b> {E(k["reading"])}</p>{("<p><b>What would settle it.</b> " + E(k["settle"]) + "</p>") if k.get("settle") else ""}<p class="small">{E(k["id"])}{(" &middot; ticket " + E(k["ticket"])) if k.get("ticket") else ""}{(" &middot; claims: " + ", ".join(f"<a href=../facts/{E(c)}/index.html>{E(c)}</a>" for c in k.get("claims", []))) if k.get("claims") else ""}</p></article>')
    def trow(t):
        extra = ''
        if t['type'] == 'evidence' and t.get('url'):
            extra = f'<div class="note">Found at <a href="{E(t["url"])}" rel="noopener">{E(re.sub(r"^https?://", "", t["url"])[:70])}</a>, {E(t["retrieved_at"])}, sha256 <code>{E(t["sha256"][:16])}</code>. Not cited until captured.{(" <q>" + E(t["excerpt"]) + "</q>") if t.get("excerpt") else ""}</div>'
        about = ', '.join(f'<a href="../facts/{E(c)}/index.html">{E(c)}</a>' for c in t['claims'] if c in claims)
        return [f'<span id="{E(t["label"])}">{E(t["label"])}</span>', f'<b>{E(t["title"])}</b><div class="note">{E(t["description"])}</div>{extra}', E(t['severity']), f'<span class="st st-{"unverified" if t["status"] in ("open", "proposed") else "confirmed"}">{E(t["status"])}</span>', about]
    groups = OrderedDict([('finding', 'Findings: things on this site to change'), ('contradiction', 'Contradictions between sources'), ('gap', 'Evidence gaps'), ('evidence', 'New evidence found outside the vault')])
    tix = ''.join(section('t-' + g, f'{title} ({sum(1 for t in T if t["type"] == g)})', table(['Ticket', 'What', 'Severity', 'Status', 'About'], [trow(t) for t in T if t['type'] == g])) for g, title in groups.items() if any(t['type'] == g for t in T))
    runs = table(['Run', 'Against', 'Checked', 'Opened', 'Summary'], [[E(r['id']), f'site v{E(r["site_version"])}, vault <code>{E(r["vault_commit"])}</code>', E(r['checked']), E(str(r.get('opened', ''))), E(r['summary'])] for r in reversed(R)])
    body = f'''
<h1>Fact-check: how sure can you be of each claim</h1>
<p class="lead">Every claim on this site has a status word chosen by the agent that wrote it. The fact-check desk grades each one again, independently, by opening the captures it cites and reading them: what kind of statement it is (a record, a count, a quote, an opinion), how strong the evidence is on a scale from A0 to A6, whether anything contradicts it, and whether the status word claims more than the evidence carries. Where the answer is "not as far as the site says", it opens a ticket. It highlights; it does not fix.</p>
<p><b>{len(A)} of {len(claims)} claims graded</b>{(", last run " + E(last.get("id", "")) + " against vault commit <code>" + E(last.get("vault_commit", "")) + "</code>") if last else ""}. <b>{len(comfy)}</b> can be relied on without reservation (A5 or A6, holding as worded, uncontested, not an opinion, and no open finding against their wording). <b>{len(over)}</b> carry a status word stronger than their evidence. <b>{len(open_t)}</b> tickets are open.</p>
{section("ladder", "The spectrum of evidence", ladder + '<p>A level is earned from captures the desk opened and read, never from how often a thing is repeated: ten outlets restating one headline are one source. An open contradiction caps a claim at A1 and a dispute at A2 until it is explained. An opinion is shown as an opinion and never rises above A3 as a fact; the facts under it are graded in its note. Absence of evidence is <i>not shown</i>, which is not the same as false.</p>')}
{section("claims", "Every claim, graded", filt.split("<script>")[0] + grid + "<script>" + filt.split("<script>")[1], 'Pick how sure you need to be. "Only what I can be very sure of" shows claims at A5 or A6 that hold as worded, are not contested, are not opinions, and have no open finding of medium or high severity against them.')}
{section("contradictions", "The contradiction ledger", "".join(ks) or "<p>None recorded yet.</p>", "Where the reporting disagrees. Each record keeps every statement, who made it and when, what each actually measures, and the desk's reading of why they differ. A contradiction is not resolved by picking a winner; it is explained, or it stays open.")}
{tix}
{section("runs", "Runs", runs, "Each run is checked against a stated site version and vault commit, so its grades can be repeated by anyone with the vault's read key.")}
{section("how", "How the desk works", '<p>The desk is <code>factcheck@php.newsroom</code>. Its role, the full model and the runbook a scheduled run follows are in <a href="' + REPO_URL + '/blob/dev/admin/factcheck/README.md">admin/factcheck/README.md</a>; its tickets are an <a href="https://issues-fs.sgit.ai/">Issues-FS</a> graph in <code>admin/factcheck/.issues/</code>, typed nodes and typed edges in plain JSON files; its grades are <a href="../data/factcheck.json">data/factcheck.json</a>. Mode one checks every claim against the evidence vault. Mode two goes outside for the weak and the contested, and records what it finds as a request to capture, never as a citation.</p>')}
'''
    page('factcheck/index.html', 'Fact-check: how sure can you be of each claim', f'Every claim on the PHP flaws site graded independently by the fact-check desk on a spectrum of evidence from A0 to A6, with a filter for only what can be relied on, the contradiction ledger, and the open tickets.', body, kind='analysis', topics='php2shell fact-check assurance')


# ----------------------------------------------------------------------------- guidance for every agent (v0.5.3)

def build_agents_guide():
    body = f"""
<p class="crumb"><a href="../index.html">Admin</a> / Guidance for agents</p>
<div class="memo">{render_md_file('AGENTS.md')}</div>
<p class="small">The source is <code>AGENTS.md</code> at the root of the repository; every agent reads it there or here.</p>
"""
    page('admin/agents/index.html', 'How to work on this site: guidance for every agent', 'Push to your own branch early and often and let dev@php.newsroom carry it into dev; quality from coding.sgit.ai, non-functional requirements from nfrs.sgit.ai, and the security requirements.', body, kind='site')

# ----------------------------------------------------------------------------- the collaborators (conductor@php.newsroom)
# The editor's brief, 22 October 2026: a page he can send people he knows, who become the site's power users: they read
# what is new when asked, as one of the site's readers, and send feedback; the asks also go to an email list and a
# WhatsApp group the editor runs. data/collaborators.json holds the asks; assets/collaborators.js sends the join and
# feedback forms, encrypted in the browser, to the private collaborators vault's write-only lane.

def ask_message(a, persons, channel):
    """The message the editor pastes into the WhatsApp group or the email list for one ask: plain text, full URLs."""
    url = f'{BASE_URL}/collaborators/index.html#ask-{a["id"]}'
    news = '\n'.join(f'- {t}: {BASE_URL}/{p}' for p, t, _ in a['new'])
    qs = '\n'.join(f'{i + 1}. {q}' for i, q in enumerate(a['questions']))
    readers = ', '.join(persons[r]['label'] for r in a['readers'] if r in persons)
    if channel == 'whatsapp':
        return (f'{a["day"]}: {a["title"]}\n\nNew on PHP October 2026:\n{news}\n\nRead it as one of the site\'s readers ({readers}, or any other on Start here) '
                f'and tell us:\n{qs}\n\nReply here, or use the form (it goes straight to the team): {url}')
    return (f'Subject: PHP October 2026, ask {a["id"]}: {a["title"]}\n\nHello,\n\nHere is what we would like you to look at this time ({a["day"]}).\n\n'
            f'What is new:\n{news}\n\nWhat to do:\n' + '\n'.join(f'{i + 1}. {s}' for i, s in enumerate(a['steps'])) +
            f'\n\nThe questions:\n{qs}\n\nReply to this email, say it in the WhatsApp group, or use the form at {url}\n\nThank you,\nDinis')

def build_collaborators():
    C = load('collaborators'); persons = {p['id']: p for p in D['personas']['personas']}
    readers = [[p['id'], p['label']] for p in D['personas']['personas']]
    cfg = J({'contact': C['contact'], 'endpoint': C['lane']['endpoint'], 'vault_id': C['lane']['vault_id'], 'append_token': C['lane']['append_token'],
             'recipient': C['lane']['recipient'], 'readers': readers, 'asks': [a['id'] for a in C['asks']]}, ensure_ascii=False, separators=(',', ':'))
    ropts = '<option value="">(none in particular)</option>' + ''.join(f'<option value="{E(i)}">{E(l)}</option>' for i, l in readers)
    aopts = ''.join(f'<option value="{E(a["id"])}">{E(a["id"])}: {E(a["title"])}</option>' for a in C['asks']) + '<option value="">Something else</option>'
    def ask_html(a, latest):
        news = ''.join(f'<a class="door" href="../{U(p)}"><b>{E(t)}</b><span>{E(w)}</span></a>' for p, t, w in a['new'])
        rd = ', '.join(f'<a href="../briefings/{E(r)}/index.html">{E(persons[r]["label"])}</a>' for r in a['readers'] if r in persons)
        msgs = (f'<details><summary>The message for the WhatsApp group</summary><pre class="msg">{E(ask_message(a, persons, "whatsapp"))}</pre></details>'
                f'<details><summary>The message for the email list</summary><pre class="msg">{E(ask_message(a, persons, "email"))}</pre></details>')
        return f'''<section class="vcard" id="ask-{E(a["id"])}"><h3>{"This ask: " if latest else ""}{E(a["day"])}, ask {E(a["id"])}: {E(a["title"])}</h3>
<p class="small">New since v{E(a["since"])}. Read it as: {rd}, or <a href="../start/index.html">any other reader</a>.</p>
<div class="doors">{news}</div>
<h4>What to do</h4><ol>{"".join(f"<li>{E(x)}</li>" for x in a["steps"])}</ol>
<h4>The questions</h4><ol>{"".join(f"<li>{E(x)}</li>" for x in a["questions"])}</ol>
{msgs}</section>'''
    asks = sorted(C['asks'], key=lambda a: a['date'], reverse=True)
    latest = ask_html(asks[0], True) if asks else '<p>No ask yet.</p>'
    earlier = ''.join(ask_html(a, False) for a in asks[1:]) or '<p class="small">None yet: this is the first.</p>'
    li = lambda xs: '<ul>' + ''.join(f'<li>{E(x)}</li>' for x in xs) + '</ul>'
    chans = ''.join(f'<li><b>{E(n)}.</b> {E(t)}</li>' for n, t in C['channels'])
    thanks = ', '.join(E(x) for x in C['thanks']) or 'Nobody yet: be the first.'
    ed = C['editor']
    body = f'''
<h1>Power users: start here</h1>
<p class="lead">This site is being built in public, every day, by {E(ed["name"])} and a team of AI agents. We are looking for people who will use it as it grows: read what is new when we ask, as the kind of reader you are, and tell us what works and what does not. {E(C["time"])} If you have not seen agentic workflows doing real work, this is a close look at one.</p>
<p><a class="cta cta-pri" href="#start">Start here</a> <a class="cta" href="#ask-{E(asks[0]["id"]) if asks else ""}">See the latest ask</a> <a class="cta" href="#feedback">Send feedback</a> <a class="cta" href="#join">Join</a></p>
{section("start", "Start here: your first fifteen minutes", '<ol class="steps">' + ''.join(f'<li><a href="../{U(h)}"><b>{E(t)}</b></a>: {E(w)}</li>' for t, h, w in C['start']) + '</ol><p class="small">That is all there is to joining in: after this, each ask tells you what to look at.</p>')}
{section("ask", "The latest ask", latest)}
{section("what", "What we ask of you", li(C["what_we_ask"]))}
{section("get", "What you get", li(C["what_you_get"]))}
{section("how", "How it works", f'<ul>{chans}</ul><p>The readers you can read as are on <a href="../start/index.html">Start here</a>: each has a plain answer, what it needs and a reading path. The team you are helping is on <a href="../team/index.html">the team page</a>.</p>')}
<section id="join"><h2>Join</h2>
<p><b>Have an invitation?</b> Open it: it lands on <a href="../join/index.html">Join</a>, which makes your key in one tap, and then the <b>Feedback</b> button at the top of every page sends signed feedback, with screenshots.</p>
<p>No invitation yet? Know {E(ed["name"].split()[0])}? <a href="{U(ed["linkedin"])}" rel="noopener">Message him on LinkedIn</a>, or fill this in. He reads every request and adds you to the email list, and to the WhatsApp group if you ask.</p>
<form id="join-form" class="subform" autocomplete="on">
<p><label>Your name<br><input type="text" name="name" required maxlength="120"></label></p>
<p><label>Your email address<br><input type="email" name="email" required maxlength="254" placeholder="you@example.org"></label></p>
<p><label>How you know {E(ed["name"].split()[0])}, or how you found this (optional)<br><input type="text" name="knows" maxlength="300"></label></p>
<p><label>The reader closest to you (optional)<br><select name="reader">{ropts}</select></label></p>
<p><label class="sub-c"><input type="checkbox" name="whatsapp" value="yes"> Add me to the WhatsApp group too ({E(ed["name"].split()[0])} will ask for your number; it is not collected here)</label></p>
<p><label>Anything else (optional)<br><textarea name="note" rows="2" maxlength="1000"></textarea></label></p>
<p class="sub-hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
<p><button class="cta cta-pri" type="submit">Ask to join</button></p>
<p id="join-out" role="status" aria-live="polite"></p>
</form></section>
<section id="feedback"><h2>Send feedback</h2>
<p>On an ask, or on anything else on the site. Short is fine. Your name and address are optional here.</p>
<form id="fb-form" class="subform" autocomplete="on">
<p><label>Which ask<br><select name="ask">{aopts}</select></label></p>
<p><label>Which reader you read as (optional)<br><select name="reader">{ropts}</select></label></p>
<p><label>Which page (optional)<br><input type="text" name="page" maxlength="300" placeholder="paste the address, or describe it"></label></p>
<p><label>What worked<br><textarea name="worked" rows="3" maxlength="3000"></textarea></label></p>
<p><label>What did not, or what you expected and could not find<br><textarea name="missing" rows="3" maxlength="3000"></textarea></label></p>
<p><label>What you would do next, or anything that contradicts something else on the site<br><textarea name="next" rows="3" maxlength="3000"></textarea></label></p>
<p><label>Your name (optional)<br><input type="text" name="name" maxlength="120"></label></p>
<p><label>Your email, if you want a reply (optional)<br><input type="email" name="email" maxlength="254"></label></p>
<p class="sub-hp" aria-hidden="true"><label>Leave this empty <input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>
<p><button class="cta cta-pri" type="submit">Send feedback</button></p>
<p id="fb-out" role="status" aria-live="polite"></p>
</form></section>
<script type="application/json" id="collab-config">{cfg}</script>
<p class="small">The forms need JavaScript, because they encrypt in your browser. Without it, write to <a href="mailto:{E(C["contact"])}">{E(C["contact"])}</a> or message {E(ed["name"].split()[0])} on LinkedIn.</p>
{section("earlier", "Earlier asks", earlier)}
{section("privacy", "What happens to what you send", f'<ul><li>It is encrypted in your browser to the collaborators vault\'s key (<code>{E(C["lane"]["recipient"]["fingerprint"])}</code>) and posted to a write-only lane on that private vault (<code>{E(C["lane"]["vault_id"])}</code>). The lane answers the same whatever arrives, so this page can say it was sent, never that it arrived.</li><li>It stays in that vault: not on this site, not in its repository, not in its telemetry. The editor and the conductor read it. Feedback becomes work on <a href="../admin/board/index.html">the board</a> in the team\'s words, never with your name unless you agree.</li><li>No phone number is collected here. WhatsApp is the editor\'s own group; he asks for your number himself.</li><li>Anyone can type anything into a form, so a request is read by a person before anyone is added or written to.</li></ul>')}
{section("thanks", "Thank you", f'<p>{thanks}</p>')}
<script src="../assets/collaborators.js" defer></script>
'''
    page('collaborators/index.html', 'Power users: start here', 'Where a power user of PHP October 2026 starts: the first fifteen minutes, the latest ask (what is new, what to do, the questions), the messages for the email list and the WhatsApp group, a form to join and a form for feedback, both encrypted in your browser.', body, kind='account')


# ----------------------------------------------------------------------------- what runs on its own, and every run (conductor@php.newsroom)
# The editor, 22 October 2026: keep track of which agents run on a schedule, so that nothing runs overnight; and one
# page that captures every agent's execution, each run with changes leaving an article. data/schedules.json is the
# register; the runs are read from the data each agent already publishes (releases, source watch, fact-check desk,
# synthetic readers), so the page adds no run of its own and cannot drift from them.
import datetime as _dt
from zoneinfo import ZoneInfo as _ZI

def cron_field(f, lo, hi):
    """The values one field of a five-field cron expression names: *, */n, a-b, a-b/n, and lists of those."""
    out = set()
    for part in f.split(','):
        rng, _, step = part.partition('/')
        a, b = (lo, hi) if rng == '*' else (tuple(int(x) for x in rng.split('-')) if '-' in rng else (int(rng), int(rng) if not step else hi))
        out.update(range(a, b + 1, int(step or 1)))
    return sorted(out)

def schedule_times(s, day):
    """The UTC times a schedule fires on one day: from its cron, or every N minutes for a self-scheduling chain."""
    start = _dt.datetime.combine(day, _dt.time(0, 0), tzinfo=_dt.timezone.utc)
    if s['kind'] == 'chain':
        return [start + _dt.timedelta(minutes=m) for m in range(0, 24 * 60, s['every_minutes'])]
    mi, ho = s['cron'].split()[:2]
    return [start.replace(hour=h, minute=m) for h in cron_field(ho, 0, 23) for m in cron_field(mi, 0, 59)]

def in_quiet(t, q):
    """True when a UTC time falls in the quiet hours, read in the quiet hours' own time zone."""
    loc = t.astimezone(_ZI(q['tz'])).strftime('%H:%M')
    return loc >= q['from'] or loc < q['to']

def all_runs(S):
    """Every execution the site's data records, newest first: (when, member, what, run id, changed, summary, link)."""
    runs = []
    for v in D['versions']['versions']:
        runs.append((v['date'], 'dev', 'Release', 'v' + v['version'], True, v['title'], 'admin/versions.html'))
    for r in D['source-watch']['runs']:
        runs.append((r['started'], 'researcher', 'Source watch pass', r['run'], r.get('changed', 0) > 0,
                     f'{r.get("pages_due", 0)} pages due, {r.get("changed", 0)} changed', 'vaults/source-watch/index.html'))
    fdir = os.path.join(ROOT, 'admin', 'factcheck', 'runs')
    for fn in sorted(os.listdir(fdir)) if os.path.isdir(fdir) else []:
        if fn.endswith('.json'):
            r = json.load(open(os.path.join(fdir, fn), encoding='utf-8'))
            runs.append((r.get('started', ''), 'verifier', 'Fact-check run', r['id'], bool(r.get('opened')), r.get('opened') or r.get('checked', ''), 'factcheck/index.html'))
    for p in (SYN or {}).get('personas', []):
        l = p.get('latest') or {}
        if l.get('run'):
            ch = l.get('checks', {})
            runs.append((l.get('finished', l['run']), 'synthetic', f'Synthetic reader: {p["name"]}', f'{p["id"]}/{l["run"]}', bool(l.get('top_fails')),
                         f'site v{l.get("site_version", "")}: {ch.get("high", 0)} high, {ch.get("medium", 0)} medium checks; answered the question {l.get("answered_question", "")}', 'admin/synthetic/index.html'))
    return sorted(runs, key=lambda r: (r[0], r[3]), reverse=True)

def build_runs():
    S = load('schedules'); q = S['quiet_hours']; day = _dt.date.fromisoformat(q['as_of'])
    members = {m['id']: m for m in TEAM['members']}
    who = lambda mid: f'<a href="../{E(mid)}/index.html">{E(members[mid]["name"])}</a>' if mid in members else E(mid)
    rows, night_total = [], 0
    for s in S['schedules']:
        ts = schedule_times(s, day); night = sorted((t for t in ts if in_quiet(t, q)), key=lambda t: (t.astimezone(_ZI(q['tz'])).hour < 12, t.astimezone(_ZI(q['tz'])).strftime('%H:%M')))  # evening first
        night_total += len(night)
        first = ', '.join(t.astimezone(_ZI(q['tz'])).strftime('%H:%M') for t in night[:6]) + (' and more' if len(night) > 6 else '')
        rows.append([f'<b>{E(s["name"])}</b><div class="note">{E(s["does"])}</div>', who(s['member']), E(s['where']),
                     E(s['cadence']) + (f'<div class="note"><code>{E(s["cron"])}</code></div>' if s.get('cron') else ''),
                     f'{len(ts)} a day', (f'<span class="st st-contradicted">{len(night)} at night</span><div class="note">{first} London</div>' if night else '<span class="st st-confirmed">none</span>'),
                     E(s['status']), E(s['proposed'])])
    reg = table(['Schedule', 'Who', 'Where', 'How often', 'Runs', 'In quiet hours', 'Status', 'Proposed'], rows, 'board')
    by_run = {a.get('run'): a for a in ARTICLES if a.get('run')}
    runs = all_runs(S)
    missing = [r for r in runs if r[4] and r[2] != 'Release' and r[3] not in by_run]
    def art(r):
        a = by_run.get(r[3])
        if a: return f'<a href="../../articles/{E(a["slug"])}/index.html">{E(a["title"].split(":")[0])}</a>'
        if r[2] == 'Release': return '<span class="small">its release note</span>'
        return '<span class="st st-disputed">missing</span>' if r[4] else '<span class="small">no changes, none needed</span>'
    erows = [[E(r[0]), who(r[1]), E(r[2]), f'<code>{E(r[3])}</code>', E(r[5]), 'yes' if r[4] else 'no', art(r), f'<a href="../../{U(r[6])}">output</a>'] for r in runs]
    counts = Counter(r[1] for r in runs)
    stats = ''.join(stat(n, l) for n, l in [(len(S['schedules']), 'schedules'), (night_total, 'runs a night, today'), (len(runs), 'runs recorded'), (len(missing), 'runs with changes and no article')])
    body = f'''
<p class="crumb"><a href="../index.html">The team</a> / Runs</p>
<h1>Runs: what the agents do on their own, and every time they did it</h1>
<p class="lead">{E(S["about"])}</p>
<div class="stats">{stats}</div>
{section("quiet", "Quiet hours", f'<p><b>{E(q["from"])} to {E(q["to"])} {E(q["tz"])}.</b> {E(q["rule"])}</p><p class="caveat">Status: {E(q["status"])}. Counted for {E(q["as_of"])}; the clocks go back on 25 October, which moves a UTC schedule an hour later in London.</p>')}
{section("schedules", "What runs on its own", reg, f"As observed on {S['observed']}. A schedule changes only with the editor's go; a workflow change goes to a branch for security review first.")}
{section("articles", "Every run with changes leaves an article", f'<p>{E(S["article_rule"])}</p>')}
{section("runs", "Every run", table(['When', 'Who', 'What', 'Run', 'Summary', 'Changes', 'Article', 'Output'], erows, 'board'), "Newest first, read from the data each agent publishes: the release history, the source watch, the fact-check desk's runs and the synthetic readers' latest run each. " + ", ".join(f"{E(members[m]['name']) if m in members else E(m)}: {n}" for m, n in counts.most_common()) + ".")}
'''
    page('team/runs/index.html', 'Runs: what the agents do on their own, and every time they did it', 'The register of every schedule the team runs (who, where, how often, how many runs fall in the quiet hours) and every recorded run, newest first, with the article each run with changes should leave.', body, kind='site', topics='team agents')


# ----------------------------------------------------------------------------- GRC: fractal risk registers (grc@php.newsroom)
# The brief is admin/content/briefs/2026-10-22__brief__grc-fractal-risk-registers.md. The data is data/grc.json (stakeholders,
# weaknesses, risks) and data/grc-frameworks.json (the standards); the build writes data/grc-graph.json. Every reference is
# checked here and the build stops on an unknown one: a risk can only point at a claim, source, story, page, team member,
# code node or control that exists. Edges follow the sgit graph grammar: every edge is a verb with a named inverse.

GRC = load('grc') if os.path.exists(os.path.join(DATA, 'grc.json')) else None
GRCF = load('grc-frameworks') if os.path.exists(os.path.join(DATA, 'grc-frameworks.json')) else None
GRC_NETWORK = load('grc-network') if os.path.exists(os.path.join(DATA, 'grc-network.json')) else None

# The part a stakeholder plays in a risk, as the verb from the risk to the stakeholder and its inverse.
GRC_AS_VERB = {'owner': ('owned_by', 'owns'), 'bearer': ('borne_by', 'bears'), 'treater': ('treated_by', 'treats'),
               'source': ('raised_by', 'raises'), 'informer': ('informed_by', 'informs'), 'regulator': ('regulated_by', 'regulates')}
GRC_VERBS = OrderedDict([
    ('part_of', 'has_part'), ('arises_from', 'gives_rise_to'), ('backed_by', 'evidences'), ('fixed_by', 'fixes'),
    ('realised_in', 'realises'), ('located_in', 'location_of'), ('protected_by', 'protects'), ('governed_by', 'governs'),
    ('concerns', 'concerned_in'), ('told_in', 'tells'), ('tracked_by', 'tracks'), ('briefed_by', 'briefs'), ('cites', 'cited_by'), ('shown_on', 'shows'),
] + [v for v in GRC_AS_VERB.values()])
GRC_CAT = OrderedDict([('security', 'Security'), ('supply-chain', 'Supply chain'), ('process', 'Disclosure process'), ('operational', 'Operational'),
                       ('compliance', 'Compliance'), ('governance', 'Governance'), ('reputational', 'Reputational'), ('strategic', 'Strategic'), ('ai', 'AI and agents')])

def grc_score(r):
    return r['likelihood'] * r['impact']

def grc_band(s):
    return 'critical' if s >= 20 else 'high' if s >= 12 else 'medium' if s >= 6 else 'low'

def grc_pill(r):
    s = grc_score(r)
    return f'<span class="gr gr-{grc_band(s)}" title="likelihood {r["likelihood"]} x impact {r["impact"]}"><b>{s}</b> {grc_band(s)}</span>'

def grc_index():
    """Every lookup the pages need, built once, with every reference checked."""
    S = OrderedDict((s['id'], s) for s in GRC['stakeholders'])
    R = OrderedDict((r['id'], r) for r in GRC['risks'])
    W = OrderedDict((w['id'], w) for w in GRC['weaknesses'])
    FW = OrderedDict((f['id'], f) for f in GRCF['frameworks'])
    CTL = OrderedDict((f'{f["id"]}:{c["id"]}', (f, c)) for f in GRCF['frameworks'] for c in f['controls'])
    claims = {c['id']: c for c in D['claims']}
    rev = {n['id']: n for n in D['review']['nodes']}
    arts = {a['slug']: a for a in ARTICLES}
    members = {m['id']: m for m in TEAM['members']}
    auds = {a['id'] for a in D['roles']['audiences']}
    actors = {a['id'] for a in D['actors']}
    bad = []
    def page_ok(p):
        return os.path.exists(os.path.join(ROOT, p.split('#')[0])) or any(p.split('#')[0] == x[0] for x in PAGES)
    for s in S.values():
        if s['parent'] is not None and s['parent'] not in S: bad.append(f'stakeholder {s["id"]}: unknown parent {s["parent"]}')
        if s.get('audience') and s['audience'] not in auds: bad.append(f'stakeholder {s["id"]}: unknown audience {s["audience"]}')
        if s.get('member') and s['member'] not in members: bad.append(f'stakeholder {s["id"]}: unknown member {s["member"]}')
        bad += [f'stakeholder {s["id"]}: unknown actor {a}' for a in s.get('actors', []) if a not in actors]
    for w in W.values():
        bad += [f'weakness {w["id"]}: unknown code-graph node {v}' for v in w.get('vulns', []) + w.get('remediation', []) if v not in rev]
        bad += [f'weakness {w["id"]}: no file {p} in this repository' for p in w.get('code', []) if not os.path.exists(os.path.join(ROOT, p))]
    for r in R.values():
        if r['parent'] is not None and r['parent'] not in R: bad.append(f'risk {r["id"]}: unknown parent {r["parent"]}')
        for a in r['assign']:
            if a['to'] not in S: bad.append(f'risk {r["id"]}: assigned to unknown stakeholder {a["to"]}')
            if a['as'] not in GRC_AS_VERB: bad.append(f'risk {r["id"]}: unknown part {a["as"]}')
        bad += [f'risk {r["id"]}: unknown weakness {x}' for x in r['weaknesses'] if x not in W]
        bad += [f'risk {r["id"]}: concerns unknown vulnerability {x}' for x in r.get('concerns', []) if x not in rev or rev[x]['layer'] != 'vulnerability']
        bad += [f'risk {r["id"]}: unknown claim {x}' for x in r['claims'] if x not in claims]
        bad += [f'risk {r["id"]}: cites unknown slug {x}' for x in r.get('sources', []) if x not in SOURCES]
        bad += [f'risk {r["id"]}: unknown control {x}' for x in r['frameworks'] if x not in CTL]
        bad += [f'risk {r["id"]}: unknown story {x}' for x in r['stories'] if x not in arts]
        bad += [f'risk {r["id"]}: unknown team member {x}' for x in r['team'] if x not in members]
        bad += [f'risk {r["id"]}: no page {x}' for x in r['pages'] + [c['page'] for c in r['controls']] if not page_ok(x)]
        if r['category'] not in GRC_CAT: bad.append(f'risk {r["id"]}: unknown category {r["category"]}')
        if not (1 <= r['likelihood'] <= 5 and 1 <= r['impact'] <= 5): bad.append(f'risk {r["id"]}: rating out of 1 to 5')
        if not r['assign']: bad.append(f'risk {r["id"]}: assigned to nobody')
        if not any(a['as'] == 'owner' for a in r['assign']): bad.append(f'risk {r["id"]}: has no owner')
    if bad:
        sys.exit('grc: ' + '; '.join(bad))
    kids_s, kids_r = {}, {}
    for s in S.values(): kids_s.setdefault(s['parent'], []).append(s['id'])
    for r in R.values(): kids_r.setdefault(r['parent'], []).append(r['id'])
    return dict(S=S, R=R, W=W, FW=FW, CTL=CTL, claims=claims, rev=rev, arts=arts, members=members, kids_s=kids_s, kids_r=kids_r)

def grc_below(kids, root):
    out, stack = [], [root]
    while stack:
        x = stack.pop(0); out.append(x); stack[0:0] = kids.get(x, [])
    return out

def grc_ancestors(items, x):
    out = []
    while items[x]['parent'] is not None:
        x = items[x]['parent']; out.append(x)
    return out

def grc_path(G, rid):
    """The chain from a risk down to the code and across to stories and roles, own and through its parents."""
    R, W, rev = G['R'], G['W'], G['rev']
    line = [rid] + grc_ancestors(R, rid)
    ws = list(OrderedDict.fromkeys(w for x in line[:1] for w in R[x]['weaknesses']))
    vulns = list(OrderedDict.fromkeys([v for x in line for w in R[x]['weaknesses'] for v in W[w].get('vulns', [])] + [v for x in line for v in R[x].get('concerns', [])]))
    rem = list(OrderedDict.fromkeys([n for w in ws for n in W[w].get('remediation', [])] +
                                    [e['from'] for e in D['review']['edges'] if e['rel'] == 'addresses' and e['to'] in vulns]))
    code = list(OrderedDict.fromkeys(e['to'] for e in D['review']['edges'] if e['rel'] == 'realised in' and e['from'] in rem))
    repo = list(OrderedDict.fromkeys(p for w in ws for p in W[w].get('code', [])))
    stories = list(OrderedDict.fromkeys(s for x in line for s in R[x]['stories']))
    roles = list(OrderedDict.fromkeys(a['to'] for x in [rid] + line[1:] + grc_below(G['kids_r'], rid)[1:] for a in R[x]['assign'] if G['S'][a['to']]['kind'] == 'role'))
    team = list(OrderedDict.fromkeys(m for x in line for m in R[x]['team']))
    return dict(weaknesses=ws, vulns=vulns, remediation=rem, code=code, repo=repo, stories=stories, roles=roles, team=team,
                own_stories=R[rid]['stories'], through=line[1:])

def grc_graph(G):
    """data/grc-graph.json: one node per thing, one edge per verb, the inverse named on the edge."""
    nodes, edges, seen = [], [], set()
    def node(i, kind, label, href):
        if i not in seen:
            seen.add(i); nodes.append({'id': i, 'kind': kind, 'label': label, 'href': href})
    def edge(a, verb, b):
        edges.append({'from': a, 'rel': verb, 'inverse': GRC_VERBS[verb], 'to': b})
    for s in G['S'].values():
        node('stakeholder:' + s['id'], 'role' if s['kind'] == 'role' else 'stakeholder', s['name'], f'grc/stakeholders/{s["id"]}/index.html')
        if s['parent']: edge('stakeholder:' + s['id'], 'part_of', 'stakeholder:' + s['parent'])
        if s.get('audience'):
            a = next(x for x in D['roles']['audiences'] if x['id'] == s['audience'])
            node('briefing:' + a['id'], 'briefing', a['name'], f'briefings/{a["id"]}/index.html'); edge('stakeholder:' + s['id'], 'briefed_by', 'briefing:' + a['id'])
        if s.get('member'):
            m = G['members'][s['member']]; node('member:' + m['id'], 'member', m['name'], f'team/{m["id"]}/index.html'); edge('stakeholder:' + s['id'], 'tracked_by', 'member:' + m['id'])
    for w in G['W'].values():
        node('weakness:' + w['id'], 'weakness', w['name'], f'grc/graph/index.html#{w["id"]}')
        for v in w.get('vulns', []):
            node('vulnerability:' + v, 'vulnerability', G['rev'][v]['name'], 'review/index.html#flaws'); edge('weakness:' + w['id'], 'arises_from', 'vulnerability:' + v)
        for p in w.get('code', []):
            node('repo:' + p, 'code', p, f'{REPO_URL}/blob/dev/{p}'); edge('weakness:' + w['id'], 'located_in', 'repo:' + p)
    for e in D['review']['edges']:
        if e['rel'] not in ('addresses', 'realised in'):
            continue
        a, b = G['rev'][e['from']], G['rev'][e['to']]
        if e['rel'] == 'addresses':
            node('remediation:' + a['id'], 'remediation', a['name'], f'review/index.html#{a["id"]}'); node('vulnerability:' + b['id'], 'vulnerability', b['name'], 'review/index.html#flaws')
            edge('vulnerability:' + b['id'], 'fixed_by', 'remediation:' + a['id'])
        elif e['rel'] == 'realised in':
            node('remediation:' + a['id'], 'remediation', a['name'], f'review/index.html#{a["id"]}'); node('code:' + b['id'], 'code', b['name'].replace('file ', ''), 'review/index.html#areas')
            edge('remediation:' + a['id'], 'realised_in', 'code:' + b['id'])
    for r in G['R'].values():
        rn = 'risk:' + r['id']
        node(rn, 'risk', r['title'], f'grc/risks/{r["id"]}/index.html')
        if r['parent']: edge(rn, 'part_of', 'risk:' + r['parent'])
        for a in r['assign']: edge(rn, GRC_AS_VERB[a['as']][0], 'stakeholder:' + a['to'])
        for w in r['weaknesses']: edge(rn, 'arises_from', 'weakness:' + w)
        for v in r.get('concerns', []): edge(rn, 'concerns', 'vulnerability:' + v)
        for c in r['claims']:
            cl = G['claims'][c]; node('claim:' + c, 'claim', cl['claim'][:90], f'facts/{c}/index.html'); edge(rn, 'backed_by', 'claim:' + c)
            for s in cl['sources']:
                if s in SOURCES: node('source:' + s, 'source', SOURCES[s].get('publisher') or s, f'sources/{s}/index.html'); edge('claim:' + c, 'cites', 'source:' + s)
        for i, c in enumerate(r['controls']):
            node(f'treatment:{r["id"]}.{i + 1}', 'treatment', c['text'], c['page']); edge(rn, 'protected_by', f'treatment:{r["id"]}.{i + 1}')
        for x in r['frameworks']:
            f, c = G['CTL'][x]; node('control:' + x, 'control', f'{f["name"]} {c["id"]}: {c["title"]}', f'grc/frameworks/{f["id"]}/index.html#{grc_cid(c["id"])}'); edge(rn, 'governed_by', 'control:' + x)
        for s in r['stories']:
            a = G['arts'][s]; node('story:' + s, 'story', a['title'], f'articles/{s}/index.html'); edge(rn, 'told_in', 'story:' + s)
        for m in r['team']:
            mm = G['members'][m]; node('member:' + m, 'member', mm['name'], f'team/{m}/index.html'); edge(rn, 'tracked_by', 'member:' + m)
        for p in r['pages']:
            node('page:' + p, 'page', nav_title(p) if p in TITLES else p, p); edge(rn, 'shown_on', 'page:' + p)
    return nodes, edges

TITLES = {}

def grc_cid(cid):
    return 'c-' + re.sub(r'[^a-z0-9]+', '-', cid.lower()).strip('-')

def grc_s_link(G, sid, depth):
    return f'<a href="{"../" * depth}grc/stakeholders/{E(sid)}/index.html">{E(G["S"][sid]["name"])}</a>'

def grc_r_link(G, rid, depth, pill=True):
    r = G['R'][rid]
    return f'<a href="{"../" * depth}grc/risks/{E(rid)}/index.html">{E(rid.upper())} {E(r["title"])}</a>' + (f' {grc_pill(r)}' if pill else '')

def grc_c_link(G, x, depth):
    f, c = G['CTL'][x]
    return f'<a href="{"../" * depth}grc/frameworks/{E(f["id"])}/index.html#{grc_cid(c["id"])}" title="{E(c["title"])}">{E(f["name"])} {E(c["id"])}</a>'

def grc_heat(G, rids, depth):
    """Likelihood up, impact across: a 5 by 5 grid with each risk's id in its cell. Readable without colour: the score is in each cell."""
    R = G['R']
    rows = ''
    for l in range(5, 0, -1):
        cells = ''
        for i in range(1, 6):
            here = [x for x in rids if R[x]['likelihood'] == l and R[x]['impact'] == i]
            ids = ' '.join(f'<a href="{"../" * depth}grc/risks/{E(x)}/index.html" title="{E(R[x]["title"])}">{E(x.upper())}</a>' for x in here)
            cells += f'<td class="hm hm-{grc_band(l * i)}"><span class="hs">{l * i}</span> {ids}</td>'
        rows += f'<tr><th scope="row">{l} {E(GRC["scales"]["likelihood"][l - 1]["name"])}</th>{cells}</tr>'
    head = ''.join(f'<th scope="col">{i} {E(GRC["scales"]["impact"][i - 1]["name"])}</th>' for i in range(1, 6))
    return f'<div class="tw"><table class="t heat"><thead><tr><th>Likelihood / impact</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'

def grc_register(G, rids, depth, sid=None):
    """A register: one row per risk, the part the stakeholder plays, and whether it is assigned here or arrives through a part of it."""
    R, S = G['R'], G['S']
    rows = []
    below = set(grc_below(G['kids_s'], sid)) if sid else set()
    for x in sorted(rids, key=lambda x: (-grc_score(R[x]), x)):
        r = R[x]
        if sid:
            mine = [a for a in r['assign'] if a['to'] == sid]
            thru = [a for a in r['assign'] if a['to'] in below and a['to'] != sid]
            part = ', '.join(f'<b>{E(a["as"])}</b>' for a in mine) or '<i>through</i> ' + ', '.join(f'{grc_s_link(G, a["to"], depth)} ({E(a["as"])})' for a in thru)
        else:
            part = ', '.join(f'{grc_s_link(G, a["to"], depth)} <span class="small">{E(a["as"])}</span>' for a in r['assign'])
        rows.append([grc_r_link(G, x, depth, pill=False), grc_pill(r), E(GRC_CAT[r['category']]), part,
                     ', '.join(grc_c_link(G, c, depth) for c in r['frameworks'][:4]) + (f' <span class="small">+{len(r["frameworks"]) - 4}</span>' if len(r['frameworks']) > 4 else '')])
    return table(['Risk', 'Rating', 'Kind', 'Part played' if sid else 'Assigned to', 'Controls'], rows)

def grc_path_svg(G, rid, P):
    """One risk's chain in columns, every line a real edge: stories and roles tell and act on the risk, stakeholders carry it,
    it arises from weaknesses, which arise from vulnerabilities, fixed by parts of the fix, realised in code."""
    S, R, W, rev = G['S'], G['R'], G['W'], G['rev']
    cols = [
        ('Told in', [('s:' + s, G['arts'][s]['title'].split(':')[0], f'../../../articles/{s}/index.html', 'sy') for s in P['stories']]),
        ('Acted on by', [('o:' + s, S[s]['name'], f'../../stakeholders/{s}/index.html', 'ro') for s in P['roles']] + [('m:' + m, G['members'][m]['name'], f'../../../team/{m}/index.html', 'tm') for m in P['team']]),
        ('Carried by', [('a:' + a['to'], f'{S[a["to"]]["name"]} ({a["as"]})', f'../../stakeholders/{a["to"]}/index.html', 'st') for a in R[rid]['assign']]),
        ('Risk', [('r', rid.upper() + ' ' + R[rid]['title'], 'index.html', 'risk')]),
        ('Arises from', [('w:' + w, W[w]['name'], f'../../graph/index.html#{w}', 'wk') for w in P['weaknesses']]),
        ('Vulnerability', [('v:' + v, rev[v]['name'].split(':')[0], '../../../review/index.html#flaws', 'vu') for v in P['vulns']]),
        ('Fixed by', [('f:' + n, rev[n]['name'], f'../../../review/index.html#{n}', 'fx') for n in P['remediation']]),
        ('Code', [('c:' + c, rev[c]['name'].replace('file ', ''), '../../../review/index.html#areas', 'cd') for c in P['code']] + [('p:' + p, p, f'{REPO_URL}/blob/dev/{p}', 'cd') for p in P['repo']]),
    ]
    links = [(k, 'r') for k, *_ in cols[0][1] + cols[1][1] + cols[2][1]]
    wv = set()
    for w in P['weaknesses']:
        for v in W[w].get('vulns', []):
            if v in P['vulns']: links.append(('w:' + w, 'v:' + v)); wv.add(v)
        for p in W[w].get('code', []): links.append(('w:' + w, 'p:' + p))
        for n in W[w].get('remediation', []): links.append(('w:' + w, 'f:' + n))
    links += [('r', 'w:' + w) for w in P['weaknesses']] + [('r', 'v:' + v) for v in P['vulns'] if v not in wv]
    links += [('v:' + e['to'], 'f:' + e['from']) for e in D['review']['edges'] if e['rel'] == 'addresses' and e['to'] in P['vulns'] and e['from'] in P['remediation']]
    links += [('f:' + e['from'], 'c:' + e['to']) for e in D['review']['edges'] if e['rel'] == 'realised in' and e['from'] in P['remediation'] and e['to'] in P['code']]
    rh, cw = 20, 150
    H = 44 + rh * max(max(len(c[1]) for c in cols), 2)
    pos, out = {}, []
    for ci, (title, items) in enumerate(cols):
        x = ci * cw + 6
        out.append(f'<text class="t" x="{x}" y="14">{E(title)}</text>')
        if not items:
            out.append(f'<text class="n gap" x="{x}" y="36">none yet</text>')
        top = 34 + (H - 44 - rh * len(items)) / 2 if ci == 3 else 34
        for i, (k, label, href, cls) in enumerate(items):
            y = top + i * rh
            pos[k] = (x, y)
            out.append(f'<a href="{E(href)}"><title>{E(label)}</title><circle class="d g-{cls}" cx="{x + 3}" cy="{y:.1f}" r="4"/><text class="n" x="{x + 11}" y="{y + 4:.1f}">{E(label[:20])}{"…" if len(label) > 20 else ""}</text></a>')
    lines = []
    for a, b in links:
        if a in pos and b in pos:
            (x1, y1), (x2, y2) = sorted([pos[a], pos[b]])
            x1 += 7; x2 -= 1
            lines.append(f'<path class="e" d="M{x1},{y1:.1f} C{x1 + 55},{y1:.1f} {x2 - 55},{y2:.1f} {x2},{y2:.1f}"/>')
    return (f'<figure class="graph gpath"><svg viewBox="0 0 {cw * len(cols)} {H:.0f}" width="100%" role="img" aria-label="The path from this risk to the stories and roles on one side and its weaknesses, vulnerabilities, fixes and code on the other">{"".join(lines)}{"".join(out)}</svg>'
            '<figcaption>The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.</figcaption></figure>')

def grc_coverage(G, P_all):
    keys = [('vulns', 'a vulnerability'), ('code', 'code'), ('stories', 'a story'), ('roles', 'a role inside an organisation'), ('team', 'a member of this team')]
    out = []
    for k, label in keys:
        have = [x for x in G['R'] if P_all[x][k] or (k == 'code' and P_all[x]['repo'])]
        out.append((k, label, have, [x for x in G['R'] if x not in have]))
    return out

def build_grc():
    if not (GRC and GRCF):
        return
    for p, t, *_ in PAGES:
        TITLES[p] = t
    G = grc_index()
    S, R, W, FW, CTL = G['S'], G['R'], G['W'], G['FW'], G['CTL']
    P_all = {x: grc_path(G, x) for x in R}
    nodes, edges = grc_graph(G)
    write('data/grc-graph.json', json.dumps({'site': SITE, 'version': VERSION, 'kept_by': GRC['kept_by'], 'as_of': GRC['as_of'],
                                            'verbs': [{'verb': v, 'inverse': i} for v, i in GRC_VERBS.items()],
                                            'note': 'Every edge is a verb with its inverse named. A risk arises from a weakness, which arises from a vulnerability, which is fixed by a remediation, realised in code; the risk is backed by claims that cite sources, owned, borne and treated by stakeholders, governed by controls, told in stories and tracked by team members.',
                                            'nodes': nodes, 'edges': edges}, indent=1, ensure_ascii=False) + '\n')
    top = [x for x in R if R[x]['parent'] is None]
    cov = grc_coverage(G, P_all)
    fam = {f['id']: f for f in GRCF['families']}
    used_ctl = Counter(c for r in R.values() for c in r['frameworks'])
    kinds = Counter(n['kind'] for n in nodes)
    acc = '<p>No risk on this register is <b>accepted</b>. An acceptance is an act by the holder of a risk, for a stated interval, and nobody can accept on anyone else\'s behalf; this desk records risks and their holders, it does not accept for them. Until a holder accepts, funds or fixes, each risk stands as it is rated here.</p>'
    nav = '<p class="crumb"><a href="{u}grc/index.html">GRC</a> &middot; <a href="{u}grc/risks/index.html">Risks</a> &middot; <a href="{u}grc/stakeholders/index.html">Stakeholders</a> &middot; <a href="{u}grc/frameworks/index.html">Frameworks</a> &middot; <a href="{u}grc/graph/index.html">The graph</a> &middot; <a href="{u}grc/network/index.html">From the network</a></p>'
    # --- the front page of the section
    stats = ''.join(stat(n, l) for n, l in [(len(R), 'risks'), (len(top), 'at the top'), (len(S), 'stakeholders'), (sum(1 for s in S.values() if s['kind'] == 'role'), 'roles'),
                                           (len(W), 'weaknesses'), (len(FW), 'frameworks'), (len(used_ctl), 'controls mapped'), (len(edges), 'edges')])
    covt = table(['Every risk reaches', 'Risks that do', 'Risks that do not yet'],
                 [[E(label), f'{len(have)} of {len(R)}', ', '.join(grc_r_link(G, x, 1, pill=False) for x in miss) or 'none'] for k, label, have, miss in cov])
    scales = table(['', 'Likelihood', 'Impact'], [[str(i + 1), f'<b>{E(l["name"])}</b>: {E(l["means"])}', f'<b>{E(m["name"])}</b>: {E(m["means"])}'] for i, (l, m) in enumerate(zip(GRC['scales']['likelihood'], GRC['scales']['impact']))])
    parts = table(['Part', 'Means', 'Edge'], [[f'<b>{E(a["name"])}</b>', E(a['means']), f'<code>{GRC_AS_VERB[a["id"]][0]}</code> / <code>{GRC_AS_VERB[a["id"]][1]}</code>'] for a in GRC['scales']['as']])
    body = f'''
{nav.format(u="../")}
<h1>GRC: the risks of php2shell, who carries them, and the standards that govern them</h1>
<p class="lead">A register of every risk in this story, broken down until each piece has someone who can act on it, and assigned to every stakeholder who carries part of it. The registers are fractal: the PHP project, a hosting provider, a council, a board and a developer each have one, and each is the same register read at a different scale. Every risk is backed by claims already on this site, and joined, edge by edge, to the weakness behind it, the vulnerability, the part of the fix that addresses it, the code that changed, the stories that tell it, the roles that act on it, and the controls in GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO 27001, NIST and the rest.</p>
<div class="stats">{stats}</div>
{section("heat", "Where the risks sit", grc_heat(G, list(R), 1), "Likelihood up, impact across; the number in each cell is the score, likelihood times impact. Click an id for the risk.")}
{section("top", "The ten risks at the top", grc_register(G, top, 1), "Each breaks down into the narrower risks it is made of; the full register is on the risks page.")}
{section("path", "From a risk to the code, the story and the role", '<p>The editor\'s test for this section: a path in the graph from every risk to the vulnerabilities, the code, the stories and the roles. The build walks it for every risk and the table below is the count; the gaps are listed by name, not hidden. A risk with no vulnerability is not a gap in itself: some risks here arise from how disclosure, regulation or this newsroom works, and their weaknesses point at the code in this repository that guards them instead.</p>' + covt)}
{section("model", "How the registers work", '<ul><li><b>A stakeholder is a node in a tree.</b> A sector holds organisations, an organisation holds roles. The same register is read at every level: a stakeholder\'s register is what is assigned to it plus everything that arrives through the parts below it.</li><li><b>A risk is a node in a tree.</b> A broad risk holds the narrower risks it is made of, until each can be owned.</li><li><b>One risk, many stakeholders.</b> Each assignment says the part played: owner, bearer, treater, source, informer or regulator. Two stakeholders that share a risk are connected; the stakeholders page shows by how much.</li><li><b>Every edge is a verb with a named inverse</b>, following the <a href="https://graphs.sgit.ai/v1/grammar/edge-set.html">sgit graph grammar</a>: a risk <i>arises from</i> a weakness, which <i>gives rise to</i> it; a risk is <i>owned by</i> a stakeholder, who <i>owns</i> it.</li><li><b>A rating is a judgement.</b> Likelihood and impact on a scale of 1 to 5, each with its basis in a sentence, as at the vault\'s last capture.</li></ul>' + acc + scales + parts)}
{section("files", "The data", f'<p>Authored: <a href="../data/grc.json">data/grc.json</a> ({len(S)} stakeholders, {len(W)} weaknesses, {len(R)} risks) and <a href="../data/grc-frameworks.json">data/grc-frameworks.json</a> ({len(FW)} frameworks, {len(CTL)} controls). Generated on every build: <a href="../data/grc-graph.json">data/grc-graph.json</a>, {len(nodes)} nodes and {len(edges)} edges. The build refuses a risk that points at a claim, source, story, page, member, code node or control that does not exist, and a risk with no owner. Kept by <a href="../team/grc/index.html">the GRC desk</a>.</p>')}
'''
    page('grc/index.html', 'GRC: the risks of php2shell, who carries them, and the standards that govern them', f'{len(R)} risks in a fractal register assigned to {len(S)} stakeholders, each joined to the weakness, vulnerability, fix, code, stories and roles behind it, and mapped to {len(used_ctl)} controls in {len(FW)} frameworks including GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO 27001 and NIST CSF.', body, kind='analysis', topics='php2shell grc risk register')
    # --- the full register
    def tree(x, depth=0):
        r = R[x]
        own = ', '.join(f'{grc_s_link(G, a["to"], 1 + 1)}' for a in r['assign'] if a['as'] == 'owner')
        row = f'<tr class="lvl-{depth}"><td style="padding-left:{0.5 + depth * 1.4}rem">{grc_r_link(G, x, 2, pill=False)}</td><td>{grc_pill(r)}</td><td>{E(GRC_CAT[r["category"]])}</td><td>{own}</td><td>{len(r["assign"])}</td><td>{len(r["frameworks"])}</td></tr>'
        return row + ''.join(tree(k, depth + 1) for k in G['kids_r'].get(x, []))
    th = ''.join(f'<th>{h}</th>' for h in ['Risk', 'Rating', 'Kind', 'Owned by', 'Stakeholders', 'Controls'])
    reg = f'<div class="tw"><table class="t grc-tree"><thead><tr>{th}</tr></thead><tbody>{"".join(tree(x) for x in top)}</tbody></table></div>'
    bycat = table(['Kind', 'Risks', 'Highest'], [[E(n), str(sum(1 for r in R.values() if r['category'] == c)), grc_r_link(G, max((x for x in R if R[x]['category'] == c), key=lambda x: grc_score(R[x])), 2)] for c, n in GRC_CAT.items() if any(r['category'] == c for r in R.values())])
    body = f'''
{nav.format(u="../../")}
<h1>The risk register: every risk, as a tree</h1>
<p class="lead">{len(R)} risks, {len(top)} at the top and {len(R) - len(top)} beneath them. A risk beneath another is a part of it narrow enough to own. Sorted as the tree; each row links to the risk's page with its full path.</p>
{reg}
{section("kinds", "By kind", bycat)}
{section("accept", "Acceptance", acc)}
'''
    page('grc/risks/index.html', 'The risk register: every php2shell risk, as a tree', f'All {len(R)} risks in the fractal register, with their rating, kind, owner and the number of stakeholders and controls each touches.', body, kind='analysis', topics='php2shell grc risk register')
    # --- one page per risk
    for x, r in R.items():
        P = P_all[x]
        anc = list(reversed(grc_ancestors(R, x)))
        crumb = ' / '.join([f'<a href="../index.html">Risks</a>'] + [grc_r_link(G, a, 3, pill=False) for a in anc] + [E(x.upper())])
        assign = table(['Stakeholder', 'Part', 'Why', 'Its register'], [[grc_s_link(G, a['to'], 3), f'<b>{E(a["as"])}</b>', E(a['why']), (lambda n: f'{n} risk' + ('' if n == 1 else 's'))(len(grc_s_rids(G, a['to'])))] for a in r['assign']])
        kids = G['kids_r'].get(x, [])
        sub = section('parts', 'The risks this one is made of', grc_register(G, kids, 3)) if kids else ''
        cl = table(['Claim', 'Status', 'Fact-check', 'Sources'], [[f'<a href="../../../facts/{E(c)}/index.html">{E(G["claims"][c]["claim"])}</a>', pill(G['claims'][c]['status']), assure(c, short=True), src_links(G['claims'][c]['sources'], 3)] for c in r['claims']]) if r['claims'] else '<p>No claim on this site carries this risk: it rests on how this newsroom works, set out on the pages linked below.</p>'
        ctl = table(['Treatment', 'Status', 'Where'], [[E(c['text']), f'<span class="gt gt-{E(c["status"])}">{E(c["status"].replace("-", " "))}</span>', f'<a href="../../../{E(c["page"])}">{E(TITLES.get(c["page"].split("#")[0], c["page"]))}</a>'] for c in r['controls']])
        fw = table(['Framework', 'Control', 'What it asks', 'Family'], [[f'<a href="../../frameworks/{E(CTL[c][0]["id"])}/index.html">{E(CTL[c][0]["name"])}</a>', f'<a href="../../frameworks/{E(CTL[c][0]["id"])}/index.html#{grc_cid(CTL[c][1]["id"])}">{E(CTL[c][1]["id"])}</a>', E(CTL[c][1]['title']), E(fam[CTL[c][0]['family']]['name'])] for c in r['frameworks']])
        ws = ''.join(f'<li><b>{E(W[w]["name"])}.</b> {E(W[w]["about"])}</li>' for w in P['weaknesses'])
        stor = ''.join(f'<li><a href="../../../articles/{E(s)}/index.html">{E(G["arts"][s]["title"])}</a>{"" if s in P["own_stories"] else " <span class=small>(through " + E(R[r["parent"]]["title"] if r["parent"] else "") + ")</span>"}</li>' for s in P['stories']) or '<li>No story on this site tells this risk yet.</li>'
        pages_ = ' &middot; '.join(f'<a href="../../../{E(p)}">{E(TITLES.get(p.split("#")[0], p))}</a>' for p in r['pages'])
        shares = Counter(b['to'] for a in r['assign'] for y in R if y != x for b in R[y]['assign'] if b['to'] == a['to'])
        body = f'''
<p class="crumb">{crumb}</p>
<h1>{E(x.upper())}: {E(r["title"])}</h1>
<p class="lead">{E(r["statement"])}</p>
<p class="kv"><b>Rating</b> {grc_pill(r)} &middot; <b>Likelihood</b> {r["likelihood"]} {E(GRC["scales"]["likelihood"][r["likelihood"] - 1]["name"])} &middot; <b>Impact</b> {r["impact"]} {E(GRC["scales"]["impact"][r["impact"] - 1]["name"])} &middot; <b>Kind</b> {E(GRC_CAT[r["category"]])} &middot; <b>Acceptance</b> not recorded</p>
<p class="note"><b>Basis.</b> {E(r["basis"])}</p>
{section("path", "The path", grc_path_svg(G, x, P))}
{section("assigned", "Who carries it", assign, "One risk, assigned to every stakeholder that carries part of it, with the part each plays.")}
{sub}
{section("weak", "What it arises from", "<ul>" + ws + "</ul>")}
{section("evidence", "The evidence", cl)}
{section("treat", "Treatments", ctl)}
{section("controls", "The standards that govern it", fw)}
{section("stories", "The stories that tell it", "<ul>" + stor + "</ul>" + ("<p>On this site: " + pages_ + "</p>" if pages_ else ""))}
'''
        page(f'grc/risks/{x}/index.html', f'{x.upper()}: {r["title"]}', r['statement'][:300], body, kind='analysis', topics='php2shell grc risk')
    # --- stakeholders
    def stree(sid, depth=0):
        s = S[sid]
        n_own = sum(1 for r in R.values() for a in r['assign'] if a['to'] == sid)
        n_all = len(grc_s_rids(G, sid))
        row = f'<tr><td style="padding-left:{0.5 + depth * 1.4}rem">{grc_s_link(G, sid, 2)}</td><td>{E(s["kind"])}</td><td>{n_own}</td><td>{n_all}</td></tr>'
        return row + ''.join(stree(k, depth + 1) for k in G['kids_s'].get(sid, []))
    th = ''.join(f'<th>{h}</th>' for h in ['Stakeholder', 'Kind', 'Assigned here', 'In its register'])
    st_tree = f'<div class="tw"><table class="t grc-tree"><thead><tr>{th}</tr></thead><tbody>{stree("world")}</tbody></table></div>'
    lvl1 = G['kids_s']['world']
    pairs = {}
    for r in R.values():
        groups = sorted({next((g for g in lvl1 if a['to'] in grc_below(G['kids_s'], g)), 'world') for a in r['assign']} - {'world'})
        for i, a in enumerate(groups):
            for b in groups[i + 1:]:
                pairs[(a, b)] = pairs.get((a, b), 0) + 1; pairs[(b, a)] = pairs[(a, b)]
    mh = ''.join(f'<th scope="col" title="{E(S[g]["name"])}">{E(S[g]["name"].split()[0] if S[g]["name"].split()[0] not in ("The", "Everyone") else S[g]["name"].split()[1])}</th>' for g in lvl1)
    mrows = ''.join(f'<tr><th scope="row">{grc_s_link(G, a, 2)}</th>' + ''.join(f'<td class="mx">{"&middot;" if a == b else (pairs.get((a, b)) or "")}</td>' for b in lvl1) + '</tr>' for a in lvl1)
    matrix = f'<div class="tw"><table class="t mxt"><thead><tr><th></th>{mh}</tr></thead><tbody>{mrows}</tbody></table></div>'
    body = f'''
{nav.format(u="../../")}
<h1>Stakeholders: a register for each, at every scale</h1>
<p class="lead">{len(S)} stakeholders in one tree, from everyone with PHP in the path down to the roles inside a single organisation. Each has a register: the risks assigned to it, and the risks that arrive through the parts beneath it. The register belongs to the stakeholder, so it reads the same whether the stakeholder is a sector, a council or a CISO.</p>
{st_tree}
{section("connected", "How the stakeholders are connected", matrix, "The number in a cell is how many risks the two groups share: a risk assigned to someone in one and someone in the other. A risk that joins many groups is one no single party can treat alone.")}
'''
    page('grc/stakeholders/index.html', 'Stakeholders: a php2shell risk register for each, at every scale', f'{len(S)} stakeholders in one tree, each with its own risk register, and the risks that connect them.', body, kind='analysis', topics='php2shell grc stakeholders')
    for sid, s in S.items():
        rids = grc_s_rids(G, sid)
        anc = list(reversed(grc_ancestors(S, sid)))
        crumb = ' / '.join([f'<a href="../index.html">Stakeholders</a>'] + [grc_s_link(G, a, 3) for a in anc] + [E(s['name'])])
        kids = G['kids_s'].get(sid, [])
        kid_l = ''.join(f'<li>{grc_s_link(G, k, 3)}: {len(grc_s_rids(G, k))} risks</li>' for k in kids)
        own_ids = [r['id'] for r in R.values() if any(a['to'] == sid for a in r['assign'])]
        sharers = Counter(a['to'] for x in own_ids for a in R[x]['assign'] if a['to'] != sid)
        sh = ', '.join(f'{grc_s_link(G, o, 3)} ({n})' for o, n in sharers.most_common(12))
        extra = []
        if s.get('audience'):
            a = next(y for y in D['roles']['audiences'] if y['id'] == s['audience'])
            extra.append(f'<a href="../../../briefings/{E(a["id"])}/index.html">the briefing for a {E(a["name"].lower())}</a>')
        if s.get('member'):
            extra.append(f'<a href="../../../team/{E(s["member"])}/index.html">their team page</a>')
        if s.get('actors'):
            extra.append('in the story as ' + ', '.join(f'<a href="../../../actors/index.html#{E(a)}">{E(next(y["name"] for y in D["actors"] if y["id"] == a).split("(")[0].strip())}</a>' for a in s['actors']))
        ctls = Counter(c for x in rids for c in R[x]['frameworks'])
        fwc = Counter(CTL[c][0]['id'] for c in ctls)
        fw_line = ', '.join(f'<a href="../../frameworks/{E(f)}/index.html">{E(FW[f]["name"])}</a> ({n})' for f, n in fwc.most_common())
        body = f'''
<p class="crumb">{crumb}</p>
<h1>{E(s["name"])}: its risk register</h1>
<p class="lead">{E(s["about"])}</p>
<p class="kv"><b>Kind</b> {E(s["kind"])} &middot; <b>Assigned here</b> {len(own_ids)} &middot; <b>In its register</b> {len(rids)}{(" &middot; " + " &middot; ".join(extra)) if extra else ""}</p>
{section("register", "The register", grc_register(G, rids, 3, sid) if rids else "<p>No risk is assigned here or below.</p>", "Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.")}
{section("heat", "Where its risks sit", grc_heat(G, rids, 3)) if rids else ""}
{section("parts", "Its parts", "<ul>" + kid_l + "</ul>") if kids else ""}
{section("shares", "Who it shares risks with", "<p>" + sh + "</p>") if sh else ""}
{section("standards", "The standards its register touches", "<p>" + fw_line + "</p>") if fw_line else ""}
'''
        page(f'grc/stakeholders/{sid}/index.html', f'{s["name"]}: its php2shell risk register', f'The fractal risk register for {s["name"]}: {len(rids)} risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.', body, kind='analysis', topics='php2shell grc stakeholder')
    # --- frameworks
    fams = ''
    for f0 in GRCF['families']:
        rows = [[f'<a href="{E(f["id"])}/index.html"><b>{E(f["name"])}</b></a><div class="note">{E(f["full"])}</div>', E(f['version']), str(sum(1 for c in f['controls'] if f'{f["id"]}:{c["id"]}' in used_ctl)) + f' of {len(f["controls"])}', str(len({x for x in R if any(c.startswith(f["id"] + ":") for c in R[x]["frameworks"])})), E(f['why'])] for f in GRCF['frameworks'] if f['family'] == f0['id']]
        fams += section('f-' + f0['id'], E(f0['name']), table(['Framework', 'Version', 'Controls used', 'Risks', 'Why it is here'], rows), E(f0['about']))
    fh = ''.join(f'<th scope="col"><a href="{E(f["id"])}/index.html">{E(f["name"].split()[0])}</a></th>' for f in GRCF['frameworks'])
    frows = ''.join(f'<tr><th scope="row">{grc_r_link(G, x, 2, pill=False)}</th>' + ''.join(f'<td class="mx">{sum(1 for c in R[x]["frameworks"] if c.startswith(f["id"] + ":")) or ""}</td>' for f in GRCF['frameworks']) + '</tr>' for x in R)
    fmx = f'<div class="tw"><table class="t mxt"><thead><tr><th>Risk</th>{fh}</tr></thead><tbody>{frows}</tbody></table></div>'
    body = f'''
{nav.format(u="../../")}
<h1>Frameworks: the law, the standards and the controls each risk maps to</h1>
<p class="lead">{len(FW)} frameworks, {len(CTL)} clauses and controls, {len(used_ctl)} of them mapped to at least one risk. A mapping says which control a holder of the risk will be asked about, by an auditor, a regulator or a board; it does not say the control is in place. Control titles are this desk's short paraphrase; each framework links to its official text.</p>
{fams}
{section("matrix", "Risks against frameworks", fmx, "How many of each framework's controls each risk maps to.")}
'''
    page('grc/frameworks/index.html', 'Frameworks: php2shell risks mapped to GDPR, NIS2, CRA, DORA, the EU AI Act, ISO 27001 and NIST', f'{len(FW)} frameworks and {len(CTL)} controls, and which php2shell risks map to each.', body, kind='analysis', topics='php2shell grc frameworks')
    for f in GRCF['frameworks']:
        rows = []
        for c in f['controls']:
            k = f'{f["id"]}:{c["id"]}'
            rs = [x for x in R if k in R[x]['frameworks']]
            holders = Counter(a['to'] for x in rs for a in R[x]['assign'] if a['as'] in ('owner', 'regulator'))
            rows.append([f'<span id="{grc_cid(c["id"])}"><b>{E(c["id"])}</b></span>', E(c['title']), '<br>'.join(grc_r_link(G, x, 3) for x in rs) or '<i>no risk mapped</i>',
                         ', '.join(grc_s_link(G, h, 3) for h, _ in holders.most_common(5))])
        body = f'''
<p class="crumb"><a href="../index.html">Frameworks</a> / {E(f["name"])}</p>
<h1>{E(f["name"])}: the php2shell risks it governs</h1>
<p class="lead">{E(f["why"])}</p>
<p class="kv"><b>Full name</b> {E(f["full"])} &middot; <b>Publisher</b> {E(f["publisher"])} &middot; <b>Version</b> {E(f["version"])} &middot; <a href="{U(f["url"])}">the official text</a></p>
{section("controls", "Clauses and controls", table(["Control", "What it asks (paraphrased)", "Risks mapped", "Owned or regulated by"], rows))}
'''
        page(f'grc/frameworks/{f["id"]}/index.html', f'{f["name"]}: the php2shell risks it governs', f'Each {f["name"]} clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.', body, kind='analysis', topics='php2shell grc ' + f['id'])
    # --- the graph
    kinds_t = table(['Kind of node', 'How many'], [[E(k), str(n)] for k, n in kinds.most_common()])
    verbs_t = table(['Verb', 'Inverse', 'Edges'], [[f'<code>{E(v)}</code>', f'<code>{E(i)}</code>', str(sum(1 for e in edges if e['rel'] == v))] for v, i in GRC_VERBS.items() if any(e['rel'] == v for e in edges)])
    wl = ''.join(f'<article class="role" id="{E(w["id"])}"><h3>{E(w["name"])}</h3><p>{E(w["about"])}</p><p class="small">Gives rise to: {", ".join(grc_r_link(G, x, 2, pill=False) for x in R if w["id"] in R[x]["weaknesses"])}'
                 + (f'<br>Arises from: {", ".join(E(G["rev"][v]["name"]) for v in w.get("vulns", []))}' if w.get('vulns') else '')
                 + (f'<br>In this repository: {", ".join(f"<a href={chr(34)}{REPO_URL}/blob/dev/{E(p)}{chr(34)}><code>{E(p)}</code></a>" for p in w.get("code", []))}' if w.get('code') else '') + '</p></article>' for w in W.values())
    # the overview drawing: top risks in the middle, groups on the left, weaknesses then vulnerabilities on the right
    lft, mid, rgt, rr = lvl1, top, list(W), [v for v in G['rev'] if G['rev'][v]['layer'] == 'vulnerability']
    H = 40 + 20 * max(len(lft), len(mid), len(rgt))
    def ys(n): return [30 + i * (H - 50) / max(1, n - 1) for i in range(n)]
    yl, ym, yw, yv = dict(zip(lft, ys(len(lft)))), dict(zip(mid, ys(len(mid)))), dict(zip(rgt, ys(len(rgt)))), dict(zip(rr, [H / 3, 2 * H / 3]))
    X = [190, 420, 640, 930]
    ln = []
    for x in mid:
        for g in sorted({next((g for g in lft if a['to'] in grc_below(G['kids_s'], g)), None) for r2 in grc_below(G['kids_r'], x) for a in R[r2]['assign']} - {None}):
            ln.append(f'<path class="e" d="M{X[0]},{yl[g]:.1f} C{X[0] + 110},{yl[g]:.1f} {X[1] - 110},{ym[x]:.1f} {X[1]},{ym[x]:.1f}"/>')
        for w in sorted({w for r2 in grc_below(G['kids_r'], x) for w in R[r2]['weaknesses']}):
            ln.append(f'<path class="e e-w" d="M{X[1]},{ym[x]:.1f} C{X[1] + 100},{ym[x]:.1f} {X[2] - 100},{yw[w]:.1f} {X[2]},{yw[w]:.1f}"/>')
    for w in rgt:
        for v in W[w].get('vulns', []):
            ln.append(f'<path class="e e-v" d="M{X[2]},{yw[w]:.1f} C{X[2] + 110},{yw[w]:.1f} {X[3] - 110},{yv[v]:.1f} {X[3]},{yv[v]:.1f}"/>')
    tx = [f'<text class="t" x="{X[0] - 6}" y="12" text-anchor="end">stakeholders</text><text class="t" x="{X[1]}" y="12" text-anchor="middle">risks at the top</text><text class="t" x="{X[2] + 6}" y="12">weaknesses</text><text class="t" x="{X[3] - 6}" y="12" text-anchor="end">vulnerabilities</text>']
    tx += [f'<a href="../stakeholders/{E(g)}/index.html"><text class="n" x="{X[0] - 8}" y="{yl[g] + 3:.1f}" text-anchor="end">{E(S[g]["name"][:34])}</text><circle class="d g-st" cx="{X[0]}" cy="{yl[g]:.1f}" r="3.5"/></a>' for g in lft]
    tx += [f'<a href="../risks/{E(x)}/index.html"><circle class="d g-risk" cx="{X[1]}" cy="{ym[x]:.1f}" r="5"/><text class="n rl" x="{X[1]}" y="{ym[x] - 7:.1f}" text-anchor="middle">{E(x.upper())} {E(R[x]["title"][:40])}{"…" if len(R[x]["title"]) > 40 else ""}</text></a>' for x in mid]
    tx += [f'<a href="#{E(w)}"><circle class="d g-wk" cx="{X[2]}" cy="{yw[w]:.1f}" r="3.5"/><text class="n" x="{X[2] + 8}" y="{yw[w] + 3:.1f}">{E(W[w]["name"][:36])}{"…" if len(W[w]["name"]) > 36 else ""}</text></a>' for w in rgt]
    tx += [f'<a href="../../review/index.html#flaws"><circle class="d g-vu" cx="{X[3]}" cy="{yv[v]:.1f}" r="5"/><text class="n" x="{X[3]}" y="{yv[v] + 18:.1f}" text-anchor="middle">{E(G["rev"][v]["name"].split(":")[0])}</text></a>' for v in rr]
    svg = f'<figure class="graph"><svg viewBox="0 0 1000 {H:.0f}" width="100%" role="img" aria-label="Stakeholder groups joined to the ten top risks, the risks to the weaknesses they arise from, and the weaknesses to the two vulnerabilities">{"".join(ln)}{"".join(tx)}</svg><figcaption>A line from a stakeholder group to a risk means someone in the group carries part of it or of a risk beneath it; a line from a risk to a weakness means the risk, or one beneath it, arises from it; the weaknesses on the two CVEs reach the fix and the code on <a href="../../review/index.html">the code review graph</a>. Each risk\'s own page draws its whole path.</figcaption></figure>'
    body = f'''
{nav.format(u="../../")}
<h1>The risk graph: stakeholders, risks, weaknesses, vulnerabilities, code</h1>
<p class="lead">{len(nodes)} nodes and {len(edges)} edges, built from the register on every release and joined to the graphs already on this site: the claims and their sources (<a href="../../graph/index.html">the story graph</a>) and the fix and the code it changed (<a href="../../review/index.html">the code review graph</a>). One graph, no copies: a claim, a source or a file is the same node here as there. The JSON is <a href="../../data/grc-graph.json">data/grc-graph.json</a>.</p>
{svg}
{section("weaknesses", "The weaknesses", wl, "What the risks arise from. Two are the CVEs themselves; the rest are conditions of the ecosystem, the disclosure process and this newsroom, each joined to the risks it gives rise to and, where there is one, to the code.")}
{section("kinds", "What is in it", kinds_t)}
{section("verbs", "The verbs", verbs_t, "Every edge is a verb read from the first node to the second; its inverse is read back. No edge says only that two things are related.")}
'''
    page('grc/graph/index.html', 'The risk graph: php2shell stakeholders, risks, weaknesses, vulnerabilities and code', f'{len(nodes)} nodes and {len(edges)} typed edges joining every php2shell risk to its stakeholders, weaknesses, vulnerabilities, fixes, code, claims, stories, roles and controls.', body, kind='analysis', topics='php2shell grc graph')
    build_grc_network(G, nav)

def grc_s_rids(G, sid):
    below = set(grc_below(G['kids_s'], sid))
    return [r['id'] for r in G['R'].values() if any(a['to'] in below for a in r['assign'])]

def build_grc_network(G, nav):
    """What the rest of the sgit network already holds on risk and on these standards, and which of it bears on which risk."""
    if not GRC_NETWORK:
        return
    N = GRC_NETWORK
    for it in N['items']:
        bad = [x for x in it.get('risks', []) if x not in G['R']] + [x for x in it.get('frameworks', []) if x not in G['FW']]
        if bad:
            sys.exit(f'grc-network: {it["id"]} names unknown risks or frameworks {bad}')
    groups = ''
    for g in N['groups']:
        rows = [[f'<a href="{U(it["url"])}"><b>{E(it["title"])}</b></a>' + (f'<div class="note">vault <code>{E(it["vault"])}</code></div>' if it.get('vault') else ''), E(it.get('date', '')), E(it['what']),
                 ', '.join(grc_r_link(G, x, 2, pill=False) for x in it.get('risks', [])) or '<i>the model</i>', ', '.join(f'<a href="../frameworks/{E(f)}/index.html">{E(G["FW"][f]["name"])}</a>' for f in it.get('frameworks', []))]
                for it in N['items'] if it['group'] == g['id']]
        groups += section('n-' + g['id'], E(g['name']), table(['Material', 'Date', 'What it holds, as its publisher describes it', 'Bears on', 'Frameworks'], rows), E(g['about']))
    gaps = ''.join(f'<li>{E(x)}</li>' for x in N.get('gaps', []))
    body = f'''
{nav.format(u="../../")}
<h1>From the network: what the sgit sites already hold on risk</h1>
<p class="lead">{E(N["about"])}</p>
{groups}
{section("gaps", "What the network does not have yet", "<ul>" + gaps + "</ul>") if gaps else ""}
<p class="small">Third-party and sibling material, described in its publisher's own terms and linked, not reproduced. Vaults are named by id; each opens from its publisher's page with the read key published there. Surveyed {E(N["surveyed"])}.</p>
'''
    page('grc/network/index.html', 'From the network: sgit risk models, vaults and standards graphs mapped to php2shell', 'The risk models, fractal registers, semantic graphs and standards vaults across the sgit network, and which php2shell risks and frameworks each bears on.', body, kind='analysis', topics='php2shell grc network', origin='external')

# ----------------------------------------------------------------------------- joining: a key, and feedback from any page (conductor@php.newsroom)
# The editor's memo of 22 October 2026: feedback from any page, signed, after an onboarding as simple as a QR code. The
# brief: admin/content/briefs/2026-10-22__brief__feedback-keys-and-review.md. The page is a shell; assets/feedback/join.js
# makes the key and sends the enrolment; data/contributors.json lists the invitations (hashes) and the enrolled keys.

def build_join():
    C = load('contributors')
    roles = dict(C['roles'])
    keys = table(['Handle', 'Role', 'Signing key', 'Device', 'Enrolled'], [[E(k['handle']), E(k['role']), f'<code>{E(k["signing_fingerprint"])}</code>', E(k['device']), E(k['enrolled'])] for k in C['keys']]) if C['keys'] else '<p class="small">None yet.</p>'
    body = f'''
<p class="crumb"><a href="../collaborators/index.html">Power users</a> / Join</p>
<h1>Join: a key for this device, in one tap</h1>
<p class="lead">To give feedback on this site you sign it with a key of your own, so the team knows who it came from. Getting one is one tap: open the invitation the editor sent you (a link or a QR code), and this page makes a key on this device and sends it to him.</p>
<noscript><p class="sub-err">This page needs JavaScript: the key is made in your browser.</p></noscript>
<div id="join-app" class="subform"><p class="small">Loading…</p></div>
{section("how", "How it works", '''<ol>
<li><b>An invitation.</b> Ask Dinis, by email or on WhatsApp, or with <a href="../collaborators/index.html#join">the join form</a>. He makes it on his phone (<a href="invite/index.html">Invite</a>) and sends you a link or a QR code meant for you alone.</li>
<li><b>One tap.</b> The link opens this page, which makes a key pair in your browser: one half signs, the other half is public. The signing half stays in this browser and cannot be copied out of it, by this site or anyone else.</li>
<li><b>Enrolled.</b> Your public key goes to the team, encrypted, with the invitation. When the invitation's signature checks out, your key is added to the list below; from then on what you sign shows as yours.</li>
<li><b>Feedback from any page.</b> Press <b>Feedback</b>, next to Ask at the top of every page: say what is wrong, unclear, missing or good, with a screenshot if you like, and send. It is signed with your key and encrypted to the team.</li>
</ol>''')}
{section("keys", "Enrolled keys", keys, "Handles and fingerprints only, never a name. " + "; ".join(f"{E(r)}: {E(t)}" for r, t in C["roles"]) + ".")}
{section("limits", "What it does not do", '''<ul>
<li>A key belongs to one browser on one device. Another device needs its own invitation; clearing this site's data deletes the key.</li>
<li>An invitation is a credential until it is used: whoever opens it first can join with it. Each one enrols at most three devices and expires in two weeks.</li>
<li>A signature proves which key wrote a message, not who holds the key: that is what the editor's enrolment adds.</li>
</ul><p class="small">Keys are in pki.sgit.ai's and sgit's format, so <code>sgit pki verify</code> checks every signature. The brief is on <a href="../admin/briefs/index.html#2026-10-22__brief__feedback-keys-and-review">briefs</a>.</p>''')}
<script type="module" src="../assets/feedback/join.js"></script>
'''
    body2 = f'''
<p class="crumb"><a href="../../collaborators/index.html">Power users</a> / <a href="../index.html">Join</a> / Invite</p>
<h1>Invite someone: a link and a QR code, signed on this device</h1>
<p class="lead">For a key that may invite ({E(", ".join(C["rules"]["may_invite"]))}). Give the person a handle (never their name), pick a role and how long the invitation lasts, and this page signs it with this device's key and shows a QR code, a link and a share button. Nothing is stored anywhere: when they join, the invitation is checked against your key, and their key is enrolled.</p>
<noscript><p class="sub-err">This page needs JavaScript: the invitation is signed in your browser.</p></noscript>
<div id="invite-app"><p class="small">Loading\u2026</p></div>
<p class="small">An invitation enrols at most {C["rules"]["devices_per_invitation"]} devices and is a credential until it is used: send it to one person, in a private message.</p>
<script type="module" src="../../assets/feedback/invite.js"></script>
'''
    page('join/invite/index.html', 'Invite someone: a link and a QR code, signed on this device', 'For the editor: make an invitation to give signed feedback on this site, as a QR code, a link and a share button, signed in the browser with an enrolled key.', body2, kind='account')
    page('join/index.html', 'Join: a key for this device, in one tap', 'Open the invitation the editor sent you and this page makes a key on your device, so the feedback you send from any page is signed as yours; the enrolled keys, as handles and fingerprints.', body, kind='account')

# ----------------------------------------------------------------------------- where every agent is (conductor@php.newsroom)
# The editor's memo of 23 October 2026 (admin/content/briefs/2026-10-23__brief__day-two-situation-awareness.md): the
# status of every agent, the vaults and the desk. data/agents-status.json is the conductor's snapshot, read from the
# sessions, the branches and the schedules without asking any agent; this page draws it.

def build_status_page():
    S = load('agents-status')
    members = {m['id']: m for m in TEAM['members']}
    STATE = {'working': 'confirmed', 'blocked': 'contradicted', 'review ready': 'disputed', 'completed': 'reported'}
    def who(a):
        m = members.get(a['member'])
        return f'<a href="../{E(a["member"])}/index.html">{E(a["agent"])}</a>' if m else E(a['agent'])
    order = {'blocked': 0, 'review ready': 1, 'working': 2, 'completed': 3}
    ag = sorted(S['agents'], key=lambda a: (order.get(a['state'], 9), a['last']))
    rows = [[who(a), f'<span class="st st-{STATE.get(a["state"], "other")}">{E(a["state"])}</span>', E(a['last'].replace('T', ' ')), E(a['did']),
             E(a['waiting']) + (f'<div class="note">on: {E(a["on"])}</div>' if a['on'] else ''), ('$' + format(a['cost'], '.2f')) if a['cost'] is not None else '']
            for a in ag]
    st = Counter(a['state'] for a in S['agents'])
    on_ed = sum(1 for a in S['agents'] if 'editor' in a['on'])
    total = sum(a['cost'] for a in S['agents'] if a['cost'] is not None)
    stats = ''.join(stat(n, l) for n, l in [(len(S['agents']), 'agents'), (st.get('working', 0), 'working'), (st.get('blocked', 0), 'blocked'), (on_ed, 'waiting on the editor'),
                                            (len(S['branches']), 'branches waiting for dev'), ('$' + str(round(total)), 'spent, sessions so far')])
    body = f'''
<p class="crumb"><a href="../index.html">The team</a> / Status</p>
<h1>Status: where every agent is</h1>
<p class="lead">{E(S["about"])}</p>
<p class="kv"><b>As of</b> {E(S["as_of"].replace("T", " "))} UTC &middot; <b>live site</b> v{E(S["live_version"])}</p>
<div class="stats">{stats}</div>
{section("decisions", "What needs a decision first", "<ol>" + "".join(f"<li>{E(x)}</li>" for x in S["decisions"]) + "</ol>")}
{section("agents", "Every agent", table(["Agent", "State", "Last activity (UTC)", "Last did", "Waiting for", "Cost"], rows, "board"), "Blocked first, then ready for review, then working, then done.")}
{section("branches", "Branches waiting to be carried into dev", table(["Branch", "By", "Commits ahead", "What"], [[f"<code>{E(b)}</code>", E(w), str(n), E(t)] for b, w, n, t in S["branches"]], "board"), "Agents push to their own branches; dev@php.newsroom carries them into dev and releases. Until then, none of this is on the site.")}
{section("schedules", "What ran on its own", table(["Schedule", "State"], [[E(a), E(b)] for a, b in S["schedules"]]), 'The register of schedules and every recorded run is on <a href="../runs/index.html">runs</a>.')}
{section("freshness", "How fresh this site\'s data is", table(["Data", "As of", "Note"], [[E(a), E(b), E(c)] for a, b, c in S["freshness"]]), "The vaults move ahead of the site; a fact reaches the site only when its vault is exported and the site released.")}
'''
    page('team/status/index.html', 'Status: where every agent is', 'Every agent on the team: what it last did, what it waits for and from whom, the branches waiting for dev, what ran on a schedule and how fresh the data is; a snapshot by the conductor.', body, kind='site', topics='team agents')

# ----------------------------------------------------------------------------- the vaults each agent made (conductor@php.newsroom)
# The editor, 23 October 2026: a page that lists every agent and the vaults it created, by ID only; the ID is public, the
# key never is. Each agent keeps its own file, data/vault-register/<agent>.json, and adds a row in the same commit as the
# vault (AGENTS.md, section 7). The build refuses anything in an id field that is not a bare vault id.

def build_vault_register():
    d = os.path.join(DATA, 'vault-register')
    regs = [json.load(open(os.path.join(d, f), encoding='utf-8')) for f in sorted(os.listdir(d)) if f.endswith('.json')]
    members = {m['id']: m for m in TEAM['members']}
    KINDS = ('vault key', 'read key', 'append token')
    for r in regs:
        for v in r['vaults'] + r.get('holds', []):
            if not re.fullmatch(r'[0-9a-z]{8}', v['id']): sys.exit(f'data/vault-register: {r["agent"]}: {v["id"][:12]}... is not a vault id; a key never goes here')
        for h in r.get('holds', []):
            if h['key'] not in KINDS: sys.exit(f'data/vault-register: {r["agent"]}: "key" names what kind of key is held ({", ".join(KINDS)}), never the key itself')
    sealed = lambda s: s[:10] if re.match(r'\d{4}-\d{2}-\d{2}$', s) else s
    secs = ''
    for r in sorted(regs, key=lambda r: (r['agent'] != 'conductor@php.newsroom', r['agent'])):
        m = members.get(r['member'])
        name = f'<a href="../{E(r["member"])}/index.html">{E(r["agent"])}</a>' if m else E(r['agent'])
        rows = [[f'<code>{E(v["id"])}</code>', E(v['what']), E(v['created']), E(sealed(v['key_sealed_to_root']))] for v in r['vaults']]
        held = r.get('holds', [])
        hrows = [[f'<code>{E(h["id"])}</code>', E(h['key']), E(h['from']), E(h['since'])] for h in held]
        htab = (f'<h4>Keys it holds</h4>{table(["Vault ID", "Kind of key", "From", "Since"], hrows)}' if held
                else '<p class="small"><b>Keys it holds:</b> not recorded yet.</p>')
        secs += f'<section class="vcard"><h3>{name} <span class="small">{len(r["vaults"])} vault{"s" if len(r["vaults"]) != 1 else ""} made</span></h3>{table(["Vault ID", "What it holds", "Created", "Key sealed to the root"], rows)}{htab}<p class="small">{E(r["note"])}</p></section>'
    n = sum(len(r['vaults']) for r in regs)
    unsealed = sum(1 for r in regs for v in r['vaults'] if not re.match(r'\d{4}-\d{2}-\d{2}|sealed', v['key_sealed_to_root']))
    body = f'''
<p class="crumb"><a href="../index.html">The team</a> / Vaults</p>
<h1>Vaults: who made each one, and who holds which keys</h1>
<p class="lead">Every vault the agents on this team have made, listed by the agent that made it, and the keys each agent holds. A vault ID is public: it names the vault and opens nothing. A vault key is never published, here or anywhere; it is sealed to the editor's key on pki.sgit.ai before the agent's session ends, so it is never lost with the session. {n} vaults; for {unsealed} of them, the sealing is not recorded yet.</p>
{secs}
{section("rules", "The rules", '''<ul>
<li><b>Record the keys you hold</b>, not only the vaults you made: every vault key, read key or append token you were given, by vault ID, the kind of key and who gave it (the <code>holds</code> list in your file). It is what lets the editor start a new session for you with the right keys. Never the key itself.</li>
<li><b>The vault key is the whole boundary.</b> Whoever holds a vault's key can do everything with it, including draining its lane: the lane's enum key and the key pair's passphrase are derived from the vault key, and the key pair lives inside the vault, encrypted (sgit.ai, the vault key is the only secret). No secret a vault needs lives only in a session.</li>
<li><b>Make a vault, add a row.</b> In the same commit, in your own file: <code>data/vault-register/&lt;you&gt;.json</code>, with the ID, what it holds, the date, and when its key was sealed to the root. The build refuses anything that is not a bare vault ID.</li>
<li><b>Seal every key to the root</b> (<code>sha256:db7f79fdd87e030a</code>) with pki.sgit.ai's agent tool before your session ends, and record the date.</li>
<li><b>Asked for a key, or a QR code of it?</b> Seal it and send the sealed link and its QR code; never the key itself, in a page, a file, a commit, a chat or a message. The steps are in <code>AGENTS.md</code>, section 7, and on <a href="../../admin/agents/index.html">guidance for agents</a>.</li>
</ul>''')}
<p class="small">What each vault is for, and the published read keys and write-only lanes, are on <a href="../../vaults/index.html">the vaults behind this site</a>.</p>
'''
    page('team/vaults/index.html', 'Vaults: who made each one', 'Every vault the team\'s agents have made, listed by agent, by ID only, with whether its key is sealed to the editor; the rules for making a vault and handing over its key.', body, kind='site', topics='team agents')


# ----------------------------------------------------------------------------- the Sherpa: readers' feedback and friction (sherpa@php.newsroom)
# The Sherpa walks with the reader and proposes; it fixes nothing on other members' pages. Its data is its own:
# admin/sherpa/feedback.json (one record per reader message, UF-nnn) and admin/sherpa/friction-log.json. The role is
# admin/sherpa/README.md. Readers are never named; their words are shown as theirs, as received, and only as text.

SHERPA_DIR = os.path.join(ROOT, 'admin', 'sherpa')
SHERPA_SEEN = {'yes': ('st-confirmed', 'reproduced'), 'partly': ('st-disputed', 'partly'), 'no': ('st-contradicted', 'not reproduced'), 'n/a': (None, 'nothing to reproduce')}
SHERPA_SEVERITY = {'high': 'st-contradicted', 'medium': 'st-disputed', 'low': 'st-unverified'}

def sherpa_load(name):
    with open(os.path.join(SHERPA_DIR, name + '.json'), encoding='utf-8') as f:
        return json.load(f)

def sherpa_who(mid, depth):
    m = {x['id']: x for x in TEAM['members']}.get(mid)
    return f'<a href="{"../" * depth}team/{E(mid)}/index.html">{E(m["name"])}</a>' if m else E(mid)

def sherpa_pill(cls, label):
    return f'<span class="st {cls}">{E(label)}</span>' if cls else f'<span class="small">{E(label)}</span>'

def sherpa_shot(up, src, cap):
    return f'<figure class="shot"><img src="{up}{U(src)}" alt="{E(cap)}" loading="lazy" style="max-width:100%;height:auto"><figcaption>{E(cap)}</figcaption></figure>'

def sherpa_doc(r):
    """The document a feedback record was received as, in blocks the comments anchor to. A record imported in full has
    admin/sherpa/documents/<id>.json; otherwise its points' own words are the document, one block each."""
    if r.get('document'):
        return sherpa_load('documents/' + r['document'])['blocks']
    return [{'id': f'p{p["n"]}', 't': 'q', 'text': p['words'], 'kind': p['kind']} for p in r['points']]

def sherpa_blocks_of(r, p):
    return p.get('blocks') or [f'p{p["n"]}']

def sherpa_block_html(r, b, up):
    t = b['t']
    if t in ('h2', 'h3'):
        return f'<h3 class="fv-h">{E(b["text"])}</h3>'
    if t == 'li':
        return f'<p class="fv-li">{E(b["text"])}</p>'
    if t == 'img':
        alt = f'Screenshot from the report: {b["src"].rsplit(".", 1)[0].split("-", 1)[-1].replace("-", " ")}'
        return f'<figure class="shot"><img src="{up}assets/sherpa/{E(r["id"].lower())}/{U(b["src"])}" alt="{E(alt)}" loading="lazy"></figure>'
    if t == 'row':
        return '<div class="fv-cells">' + ''.join(f'<span>{E(c)}</span>' for c in b['cells']) + '</div>'
    if t == 'q':
        return f'<p><span class="small">{E(b.get("kind", ""))}</span><br><q>{E(b["text"])}</q></p>'
    return f'<p>{E(b["text"])}</p>'

def sherpa_card(r, p, d):
    if p.get('held'):
        return f'<div class="fv-card" id="c{p["n"]}"><b>{E(r["id"])}.{p["n"]}: held</b><p>{E(p["comment"])}</p></div>'
    also = (', with ' + ', '.join(sherpa_who(x, d) for x in p['also'])) if p.get('also') else ''
    sev = sherpa_pill(SHERPA_SEVERITY[p['severity']], p['severity']) if p.get('severity') else ''
    return f'''<div class="fv-card" id="c{p["n"]}"><b>{E(r["id"])}.{p["n"]} · {E(p["kind"])}</b> {sherpa_pill(*SHERPA_SEEN[p["replicated"]])} {sev}
<p>{E(p["comment"])}</p>{f'<p class="small"><b>Evidence.</b> {E(p["evidence"])}</p>' if p.get("evidence") else ""}
<p><b>Recommend.</b> {E(p["recommendation"])}</p>
<p class="small">Who can act: {sherpa_who(p["owner"], d)}{also}{(" · friction " + E(p["friction"])) if p.get("friction") else ""}</p></div>'''

def sherpa_nav(FB, CI, cur, up):
    def item(href, label, sub, on):
        return f'<a href="{href}"{" aria-current=page" if on else ""}><b>{E(label)}</b><span>{E(sub)}</span></a>'
    groups = [("From readers and power users", [r for r in FB if r.get('tester') != 'agent']), ("Tests by agents", [r for r in FB if r.get('tester') == 'agent'])]
    out = item(f'{up}feedback/index.html', 'All feedback', 'the section, with its numbers', cur == 'home')
    for name, rs in groups:
        out += f'<p class="fv-g">{E(name)}</p>' + ''.join(item(f'{up}feedback/{E(r["id"].lower())}/index.html', r['id'], (r.get('who') or r['reader'].split(',')[0])[:60], cur == r['id']) for r in rs)
    out += '<p class="fv-g">Ideas from collaborators</p>' + ''.join(item(f'{up}sherpa/ideas/{E(c["id"].lower())}/index.html', c['id'], c['name_on_site'] or c['handle'], False) for c in CI)
    out += '<p class="fv-g">What happens next</p>' + item(f'{up}feedback/briefs/index.html', 'The briefs', 'to the conductor, and to other teams', cur == 'briefs')
    return f'<nav class="fv-nav" aria-label="Feedback">{out}</nav>'

def sherpa_brief_of(r, d):
    by = {}
    for p in r['points']:
        if p['kind'] == 'praise' or p.get('held'):
            continue
        by.setdefault(p['owner'], []).append(p)
    if not by:
        return '<p>Nothing to brief: praise only.</p>'
    out = ''
    for own, ps in by.items():
        out += f'<h3>For {sherpa_who(own, d)}</h3><ol>' + ''.join(f'<li>{E(p["recommendation"])} <span class="small">({E(r["id"])}.{p["n"]}{(", " + E(p["friction"])) if p.get("friction") else ""})</span></li>' for p in ps) + '</ol>'
    return '<p>Everything goes to the conductor, who hands each part to the member named. What this record asks of each member:</p>' + out

def sherpa_viewer(r, FB, CI, d):
    up = '../' * d
    blocks = sherpa_doc(r)
    first, at = {}, {}
    for p in r['points']:
        bs = sherpa_blocks_of(r, p)
        first.setdefault(bs[0], []).append(p)
        for b in bs[1:]:
            at.setdefault(b, []).append(p)
    rows = ''
    for b in blocks:
        cards = ''.join(sherpa_card(r, p, d) for p in first.get(b['id'], []))
        refs = ''.join(f'<a class="fv-ref" href="#c{p["n"]}">{E(r["id"])}.{p["n"]}</a>' for p in at.get(b['id'], []))
        rows += f'<div class="fv-row" id="{E(b["id"])}"><div class="fv-b" data-b="{E(b["id"])}">{sherpa_block_html(r, b, up)}</div><aside class="fv-c">{cards}{refs}</aside></div>'
    kinds = Counter(p['kind'] for p in r['points'])
    chips = ''.join(f'<a class="fv-chip fv-k-{E(p["kind"])}" href="#c{p["n"]}" title="{E(p["kind"])}">{p["n"]}</a>' for p in r['points'])
    return f'''<div class="fv-map"><span class="small">Points, in order ({", ".join(f"{n} {E(k)}" for k, n in kinds.most_common())}):</span> {chips}</div>
<div class="fv-doc" data-doc="{E(r["id"])}"><div class="fv-row fv-head"><div>The document, as received</div><div>The Sherpa's comments</div></div>{rows}</div>'''

def build_sherpa_feedback(r, FB, CI):
    d = 2; up = '../' * d
    pages_read = ', '.join(f'<a href="{up}{U(pth)}">{E(pth)}</a>{(" (" + E(how) + ")") if how else ""}' for pth, how in r['pages_read'])
    who = "A test by an agent, not a person: its findings are prompts to re-check, not evidence about readers." if r.get("tester") == "agent" else "Readers are never named here."
    facts = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in [('From', f'{E(r["reader"])}. {who}'), ('How it came', E(r['channel']) + ((', about ask ' + E(r['ask'])) if r.get('ask') else '')),
        ('Received', E(r['received'])), ('Site version', f'v{E(r["site_version"])}. {E(r["site_version_note"])}'), ('Progress', E(r['progress'])), ('Pages read', pages_read)])
    nr = ''.join(f'<li>{E(x)}</li>' for x in r.get('not_reproduced', []))
    title = f'{r["id"]}: feedback of {r["received"]}, on v{r["site_version"]}'
    body = f'''
<link rel="stylesheet" href="{up}assets/sherpa/viewer.css">
<p class="crumb"><a href="../index.html">Feedback from collaborators</a> / {E(r["id"])}</p>
<div class="fv">{sherpa_nav(FB, CI, r["id"], up)}<div class="fv-main">
<h1>{E(title)}</h1>
<p class="lead">{E(r["summary"])}</p>
<dl class="fv-facts">{facts}</dl>
{section("doc", "The document and the Sherpa's comments, side by side", sherpa_viewer(r, FB, CI, d), "Select any text in the document to highlight it and add a note of your own; your notes stay in this browser, and you can export them.")}
{section("mine", "Your notes", '<div id="fv-notes"><p class="small">None yet. Select text in the document to add one. This needs JavaScript; notes are kept in this browser only.</p></div>')}
{section("brief", "The brief", sherpa_brief_of(r, d))}
{section("open", "Not reproduced, and the reply", f"<ul>{nr}</ul><p>{E(r.get('reply', ''))}</p>")}
</div></div>
<script type="module" src="{up}assets/sherpa/viewer.js"></script>
'''
    page(f'feedback/{r["id"].lower()}/index.html', title, r['summary'], body, kind='site', topics='readers feedback collaborators')
def build_feedback_section(FB, CI, FL):
    d = 1; up = '../'
    ST = sherpa_load('collab-stats')
    opn = [f for f in FL['frictions'] if f['status'] != 'closed']
    pts = [p for r in FB for p in r['points']]
    stats = ''.join(stat(n, l) for n, l in [(len(FB), 'pieces of feedback'), (len(pts), 'points answered'), (sum(p['replicated'] == 'yes' for p in pts), 'reproduced by the Sherpa'),
        (len(opn), 'frictions open'), (ST['power_users_joined'], 'power users joined'), (ST['signed_messages'], 'signed messages received'), (len(CI), 'conversations of ideas')])
    rows = [[f'<a href="{E(r["id"].lower())}/index.html">{E(r["id"])}</a>', E(r['received']), 'v' + E(r['site_version']), E(r.get('who') or r['reader'][:70]), 'agent test' if r.get('tester') == 'agent' else 'person',
             str(len(r['points'])), E(r['summary'])] for r in FB]
    body = f'''
<link rel="stylesheet" href="{up}assets/sherpa/viewer.css">
<p class="crumb"><a href="../collaborators/index.html">Power users</a> / Feedback from collaborators</p>
<div class="fv">{sherpa_nav(FB, CI, "home", up)}<div class="fv-main">
<h1>Feedback from collaborators</h1>
<p class="lead">Everything the power users and collaborators have told us about this site, each piece kept whole, with the Sherpa's comment beside every part of it, what was reproduced, and the brief it turned into. Kept by <a href="../sherpa/index.html">the Sherpa</a>. People are not named; tests run by agents are marked as tests.</p>
<div class="stats">{stats}</div>
<p class="small">{E(ST["note"])}</p>
{section("all", "Every piece of feedback", table(["Id", "Received", "Version", "From", "Kind", "Points", "In short"], rows, "board"))}
{section("next", "What happens next", '<p>Each piece of feedback becomes frictions in <a href="../sherpa/index.html#friction">the friction log</a> and a line in <a href="briefs/index.html">the brief to the conductor</a>, who hands it to the member who owns the page. When a fix ships, the Sherpa checks it on the live site and closes the friction.</p>')}
</div></div>
'''
    page('feedback/index.html', 'Feedback from collaborators', 'Every piece of feedback from power users and collaborators, kept whole and answered point by point beside it, with the numbers and the briefs it turned into.', body, kind='site', topics='readers feedback collaborators')
    by = {}
    for f in opn:
        by.setdefault(f['owner'], []).append(f)
    order = sorted(by, key=lambda o: (-sum(f['severity'] == 'high' for f in by[o]), o))
    inner = ''
    for own in order:
        fs = sorted(by[own], key=lambda f: ({'high': 0, 'medium': 1, 'low': 2}[f['severity']], f['id']))
        inner += f'<h3>For {sherpa_who(own, 2)}</h3><ol>' + ''.join(f'<li>{sherpa_pill(SHERPA_SEVERITY[f["severity"]], f["severity"])} <b>{E(f["page"])}:</b> {E(f.get("proposal") or f.get("expected", ""))} <span class="small">({E(f["id"])}; seen v{E(f["first_seen"])} to v{E(f["last_seen"])}; {E(f.get("source", "the Sherpa"))})</span></li>' for f in fs) + '</ol>'
    BR = sherpa_load('briefs')
    ext = ''
    for t in BR['teams']:
        ext += f'<h3>For <a href="{U(t["url"])}">{E(t["name"])}</a></h3><ol>' + ''.join(f'<li>{sherpa_pill(SHERPA_SEVERITY[i["severity"]], i["severity"])} <b>{E(i["title"])}.</b> {E(i["what"])} <i>Evidence:</i> {E(i["evidence"])} <i>Proposal:</i> {E(i["proposal"])}</li>' for i in t['items']) + '</ol>'
    body = f'''
<link rel="stylesheet" href="{up}../assets/sherpa/viewer.css">
<p class="crumb"><a href="../index.html">Feedback from collaborators</a> / The briefs</p>
<div class="fv">{sherpa_nav(FB, CI, "briefs", "../../")}<div class="fv-main">
<h1>The briefs: what the feedback asks of each team</h1>
<p class="lead">One brief to the conductor, built from every open friction, grouped by the member who owns the page and ordered by severity; the conductor hands each part on. Then the requirements for teams outside this newsroom. Every line names where it came from.</p>
{section("conductor", "To the conductor", inner)}
{section("other", "To other teams", ext)}
</div></div>
'''
    page('feedback/briefs/index.html', 'The briefs: what the feedback asks of each team', 'The brief to the conductor from every open friction, by owner and severity, and the requirements for teams outside the newsroom (pki.sgit.ai).', body, kind='site', topics='readers feedback briefs')

SHERPA_KIND = {'comment': 'Comments', 'idea': 'Ideas', 'question': 'Questions', 'offer': 'The offer'}

def sherpa_idea(c, it, d):
    up = '../' * d
    links = ' · '.join(f'<a href="{up}{U(p)}">{E(t)}</a>' for p, t in it['links'])
    also = (', with ' + ', '.join(sherpa_who(x, d) for x in it['also'])) if it.get('also') else ''
    return f'''<article class="fbpoint" id="i{it["n"]}">
<h3>{E(c["id"])}.{it["n"]}: {E(it["kind"])}, {E(", ".join(it["tags"]))}</h3>
<blockquote><p><q>{E(it["words"])}</q></p><footer>In the collaborator's words, as received</footer></blockquote>
<p><b>Where the site stands today.</b> {E(it["today"])}</p>
<p class="small">See: {links}</p>
<p><b>What is missing.</b> {E(it["gap"])}</p>
<p><b>The Sherpa recommends.</b> {E(it["recommendation"])}</p>
<p class="small">Who could take it: {sherpa_who(it["owner"], d)}{also}.</p>
</article>'''

def build_sherpa_ideas(c):
    d = 3
    who = c['name_on_site'] or c['handle']
    title = f'{c["id"]}: comments, questions and ideas from {who}'
    ex = table(['When', 'Who', 'What was said'], [[E(w), E(x), E(t)] for w, x, t in c['exchange']], 'board')
    idx = table(['#', 'Kind', 'About', 'Who could take it'], [[f'<a href="#i{it["n"]}">{it["n"]}</a>', E(it['kind']), E(', '.join(it['tags'])), sherpa_who(it['owner'], d)] for it in c['items']], 'board')
    groups = ''
    for k, label in SHERPA_KIND.items():
        its = [it for it in c['items'] if it['kind'] == k]
        if its:
            groups += section(f'k-{k}', label, ''.join(sherpa_idea(c, it, d) for it in its))
    stats = ''.join(stat(sum(it['kind'] == k for it in c['items']), SHERPA_KIND[k].lower()) for k in SHERPA_KIND)
    body = f'''
<p class="crumb"><a href="../../index.html">The Sherpa</a> / <a href="../../index.html#ideas">Ideas from collaborators</a> / {E(c["id"])}</p>
<h1>{E(title)}</h1>
<p class="lead">{E(c["summary"])}</p>
<div class="stats">{stats}</div>
{section("record", "The record", f"""<ul>
<li><b>From:</b> {E(who)}. {E(c["name_note"]) if not c["name_on_site"] else ""}</li>
<li><b>How it came:</b> {E(c["channel"])}, {E(c["from"])} to {E(c["to"])}.</li>
<li><b>Checked against:</b> site v{E(c["site_version"])}.</li>
</ul>""")}
{section("exchange", "The conversation, in short", ex, "Summarised; the collaborator's own words are quoted under each item below.")}
{section("index", "At a glance", idx, "Each item: the collaborator's words, where the site stands today with links, what is missing, what the Sherpa recommends, and who could take it. Answers to the questions are the editor's; the Sherpa only says what exists.")}
{groups}
{section("reply", "The reply", f"<p>{E(c['reply'])}</p>")}
'''
    page(f'sherpa/ideas/{c["id"].lower()}/index.html', title, c['summary'], body, kind='site', topics='collaborators ideas graph')

def build_sherpa():
    FB, FL = sherpa_load('feedback')['feedback'], sherpa_load('friction-log')
    CI = sherpa_load('ideas')['conversations']
    for r in FB:
        build_sherpa_feedback(r, FB, CI)
    for c in CI:
        build_sherpa_ideas(c)
    build_feedback_section(FB, CI, FL)
    me = [m for m in TEAM['members'] if m['id'] == 'sherpa'][0]
    fbrows = [[f'<a href="../feedback/{E(r["id"].lower())}/index.html">{E(r["id"])}</a>', E(r['received']), 'v' + E(r['site_version']), E(r['reader']), E(r['progress']),
               str(len(r['points'])), str(sum(p['replicated'] == 'yes' for p in r['points'])), E(r['summary'])] for r in FB]
    frows = [[E(f['id']), E(f['page']), E(f['stage']), sherpa_pill(SHERPA_SEVERITY[f['severity']], f['severity']), sherpa_who(f['owner'], 1), E(f['status']),
              f'v{E(f["first_seen"])} to v{E(f["last_seen"])}', E(f.get('proposal', f.get('expected', '')))] for f in FL['frictions']]
    opn = [f for f in FL['frictions'] if f['status'] != 'closed']
    stats = ''.join(stat(n, l) for n, l in [(len(FB), 'reader messages'), (sum(len(r['points']) for r in FB), 'points answered'), (len(opn), 'frictions open'), (sum(f['severity'] == 'high' for f in opn), 'of them high')])
    help_ = '''<ul>
<li><b>Not sure where to start?</b> <a href="../start/index.html">Tell the site who you are</a> and it gives you a short reading path for your job and the time you have.</li>
<li><b>New to the story?</b> <a href="../explained/index.html">It is explained from scratch</a>, and <a href="../glossary/index.html">the glossary</a> has every specialist word.</li>
<li><b>Have a question?</b> Press <b>Ask</b> at the top of any page.</li>
<li><b>Something wrong, unclear or missing?</b> Tell us: <b>Feedback</b> at the top of any page if you have a key, <a href="../collaborators/index.html">the forms for power users</a>, or an email to the editor. However it reaches us, I record it here with an id, the date and the version you read, and answer it point by point.</li>
</ul>'''
    how = '<ul>' + ''.join(f'<li>{E(x)}</li>' for x in me['rules']) + '</ul><p class="small">The role in full: <code>admin/sherpa/README.md</code>. My page on the team: <a href="../team/sherpa/index.html">the Sherpa</a>.</p>'
    body = f'''
<p class="crumb"><a href="../team/index.html">The team</a> / The Sherpa</p>
<h1>I'm the Sherpa. I'm here to help you find your way.</h1>
<p class="lead">I'm one of the agents that run this site. My job is you: the question you came with, the first screen you see, whether you got your answer, and where you go next. When something here gets in your way, I write it down, find out why, and ask the member who owns that page to fix it. I don't change other members' pages myself; I make sure the right one knows, and I check afterwards that it helped.</p>
<div class="stats">{stats}</div>
{section("help", "How I can help you now", help_)}
{section("feedback", "What readers told us", table(["Id", "Received", "Version", "From", "Progress", "Points", "Reproduced", "In short"], fbrows, "board"), "Every message from a reader, one page each, answered point by point. Readers are not named; their words are shown as they wrote them.")}
{section("ideas", "Ideas from collaborators", table(["Id", "From", "When", "Comments", "Ideas", "Questions", "In short"], [[f'<a href="ideas/{E(c["id"].lower())}/index.html">{E(c["id"])}</a>', E(c["name_on_site"] or c["handle"]), f'{E(c["from"])} to {E(c["to"])}', *[str(sum(it["kind"] == k for it in c["items"])) for k in ("comment", "idea", "question")], E(c["summary"])] for c in CI], "board"), "What collaborators think this site should become, one page per conversation, each item set against what the site has today.")}
{section("friction", "What gets in readers' way", table(["Id", "Where", "Stage", "Severity", "Who can act", "Status", "Seen", "What I propose"], frows, "board"), "The friction log: every struggle a reader met, from real readers, the synthetic readers and my own walks of the site, with who can fix it. A friction closes when the trail shows it helped, not when a commit says so.")}
{section("how", "How I work", how)}
'''
    page('sherpa/index.html', "The Sherpa: I'm here to help you find your way", "The Sherpa, the agent that walks with the reader: how to find your path on this site, every message readers have sent answered point by point, and the friction log of what gets in readers' way, with who can fix it.", body, kind='site', topics='readers feedback')


if __name__ == '__main__':
    main()
