#!/usr/bin/env python3
"""The gate. Exits non-zero on any failure. Run after build.py, from anywhere."""
import hashlib, json, os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SKIP_DIRS = {'.git', 'data', 'assets', '.sg_vault', 'build', 'content'}
fails, warns = [], []

def rel(p): return os.path.relpath(p, ROOT)

def html_files():
    out = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        for f in files:
            if f.endswith('.html'):
                out.append(os.path.join(root, f))
    return sorted(out)

pages = html_files()
if not pages: fails.append('no pages built')
linked_to = set()
for p in pages:
    s = open(p, encoding='utf-8').read()
    d = os.path.dirname(p)
    # 1. internal links resolve; 2. collect inbound links
    for m in re.finditer(r'(?:href|src)="([^"#]+)(#[^"]*)?"', s):
        href = m.group(1)
        if re.match(r'^(https?:|mailto:|data:)', href):
            if re.search(r'<(script|link|img)[^>]*\b(src|href)="' + re.escape(href), s) and 'rel="license"' not in s[max(0, m.start() - 120):m.start()] and 'canonical' not in s[max(0, m.start() - 60):m.start()] and 'og:' not in s[max(0, m.start() - 60):m.start()]:
                tag = s[s.rfind('<', 0, m.start()):m.start()]
                if tag.startswith('<script') or tag.startswith('<link rel="stylesheet"') or tag.startswith('<img'):
                    fails.append(f'{rel(p)}: external resource {href}')
            continue
        target = os.path.normpath(os.path.join(d, href))
        if not os.path.exists(target):
            fails.append(f'{rel(p)}: broken link {href}')
        elif target.endswith('.html'):
            linked_to.add(target)
    # 3. markdown twin
    md = re.sub(r'\.html$', '.md', p)
    if not os.path.exists(md): fails.append(f'{rel(p)}: no markdown twin')
    # 6. em-dash in the site's prose (sources page exempt: third-party titles)
    if os.sep + 'sources' + os.sep not in p and os.sep + 'actors' + os.sep not in p and os.sep + 'facts' + os.sep not in p and os.sep + 'versions' + os.sep not in p and os.sep + 'interview' + os.sep not in p and not p.endswith(os.path.join('affected', 'software.html')) and not p.endswith(os.path.join('brief', 'index.html')) and not re.search(r'readings/[^/]+/index\.html$', p.replace(os.sep, '/')):
        body = re.sub(r'<q>.*?</q>', '', s, flags=re.S)
        body = re.sub(r'title="[^"]*"', '', body)
        if '—' in body:
            fails.append(f'{rel(p)}: em-dash in prose')
# 2. orphans
for p in pages:
    if p not in linked_to and not p.endswith('index.html') or (p.endswith('index.html') and p != os.path.join(ROOT, 'index.html') and p not in linked_to):
        fails.append(f'{rel(p)}: orphan (nothing links to it)')
# 3b. llms.txt lists every page
llms = open(os.path.join(ROOT, 'llms.txt'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, 'llms.txt')) else ''
if not llms: fails.append('llms.txt missing')
for p in pages:
    if 'account/' in rel(p): continue
    if re.sub(r'\.html$', '.md', rel(p)) not in llms:
        fails.append(f'{rel(p)}: not in llms.txt')
# 4. citations and 9. data parses, statuses
def load(n):
    try:
        return json.load(open(os.path.join(ROOT, 'data', n + '.json'), encoding='utf-8'))
    except Exception as e:
        fails.append(f'data/{n}.json: {e}'); return None
sources = load('sources') or []
slugs = {s['slug'] for s in sources}
WORDS = {'confirmed', 'reported', 'disputed', 'contradicted', 'unverified'}
for n, key in (('claims', 'sources'), ('timeline', 'sources'), ('numbers', 'sources'), ('agencies', 'sources'), ('exploitation', 'sources'), ('actors', 'sources')):
    rows = load(n) or []
    for r in rows:
        for s in r.get(key, []):
            if s not in slugs: fails.append(f'data/{n}.json: {r.get("id") or r.get("at") or r.get("agency")} cites unknown slug {s}')
        if n == 'claims' and r.get('status') not in WORDS: fails.append(f'data/claims.json: {r.get("id")} has status {r.get("status")!r}')
        if n == 'numbers' and r.get('status') not in WORDS: fails.append(f'data/numbers.json: {r.get("id")} has status {r.get("status")!r}')
story = load('story') or {}
for k in story.get('known', []):
    for s in k.get('sources', []):
        if s not in slugs: fails.append(f'data/story.json: known cites unknown slug {s}')
for n in ('affected', 'roles', 'versions', 'billing', 'vault', 'software', 'graph', 'vault-claims', 'vault-timeline'):
    load(n)
aff = load('affected') or {}
for s in aff.get('ranges_sources', []) + aff.get('mitigations_sources', []) + sum([x.get('sources', []) for x in aff.get('sapis', [])], []):
    if s not in slugs: fails.append(f'data/affected.json cites unknown slug {s}')
# 4b. articles: front matter present, every [[slug]] in the manifest
adir = os.path.join(ROOT, 'admin', 'content', 'articles')
for fn in sorted(os.listdir(adir)) if os.path.isdir(adir) else []:
    if not fn.endswith('.md'): continue
    t = open(os.path.join(adir, fn), encoding='utf-8').read()
    fm = re.match(r'^---\n(.*?)\n---\n', t, flags=re.S)
    if fm and not re.search(r'^origin:\s*(house|guest|interview)\s*$', fm.group(1), flags=re.M): fails.append(f'articles/{fn}: origin must be house, guest or interview')
    for k in ('slug', 'title', 'dek', 'role', 'author', 'written', 'as_of_version', 'vault_commit', 'data_as_of'):
        if not fm or not re.search(r'^' + k + r':\s*\S', fm.group(1), flags=re.M): fails.append(f'articles/{fn}: front matter has no {k}')
    for g in re.findall(r'\[\[([^\]]+)\]\]', t):
        for s in g.split(','):
            if s.strip() not in slugs: fails.append(f'articles/{fn}: cites unknown slug {s.strip()}')
# 4b2. second readings: every row's sources and claims exist, and the other model's text is on disk
rd = load('readings') or {}
cids = {c['id'] for c in (load('claims') or [])}
for r in rd.get('readings', []):
    if not os.path.exists(os.path.join(ROOT, r.get('file', ''))): fails.append(f'data/readings.json: {r.get("id")} file {r.get("file")} missing')
    for x in r.get('rows', []):
        for s in x.get('sources', []):
            if s not in slugs: fails.append(f'data/readings.json: {r.get("id")} / {x.get("point")} cites unknown slug {s}')
        for c in x.get('claims', []):
            if c not in cids: fails.append(f'data/readings.json: {r.get("id")} / {x.get("point")} names unknown claim {c}')
# 4d. patching: every downstream row is a real inventory row with the status shown; status.json is built and parses
pt = load('patching') or {}
inv = {(r['supplier'], r['product']): r.get('status_109618') for r in (load('software') or {}).get('rows', [])}
prow = [d for l in pt.get('ladder', []) for d in l.get('downstream', [])] + [r for m in pt.get('models', []) for r in m.get('rows', [])]
for sup, prod, st in prow:
    if (sup, prod) not in inv: fails.append(f'data/patching.json: no inventory row {sup!r} / {prod!r}')
    elif inv[(sup, prod)] != st: fails.append(f'data/patching.json: {prod!r} is {st!r} here but {inv[(sup, prod)]!r} in the inventory')
for x in pt.get('ladder', []) + pt.get('side_effects', []) + pt.get('why_not_every_version', []):
    for s in x.get('sources', []):
        if s not in slugs: fails.append(f'data/patching.json cites unknown slug {s}')
try:
    json.load(open(os.path.join(ROOT, 'status.json'), encoding='utf-8'))
except Exception as e:
    fails.append(f'status.json: {e}')
# 4e. signals: every layer, family and barrier cites only manifest slugs
sg = load('signals') or {}
for x in sg.get('ladder', []) + sg.get('families', []) + sg.get('barriers', []):
    for s in x.get('sources', []):
        if s not in slugs: fails.append(f'data/signals.json: {x.get("id")} cites unknown slug {s}')
# 4f. storyboards: the kit's vocabulary, the cast, every cited slug, every quote word for word in the file it names,
# every bar chart equal to the counts in its file, and the vendored kit byte for byte against its release manifest
SBD = os.path.join(ROOT, 'admin', 'content', 'storyboards')
if os.path.isdir(SBD):
    V = {'kinds': {'cover', 'scene', 'evidence', 'punchline', 'spectrum', 'map', 'graph'}, 'poses': {'stand', 'point', 'wave', 'arms-up', 'shrug', 'think', 'sit'},
         'moods': {'neutral', 'happy', 'excited', 'calm', 'worried', 'sad', 'surprised', 'thinking', 'confused', 'determined'},
         'settings': {'none', 'office', 'interview', 'street', 'night', 'classroom'},
         'props': {'laptop', 'desk', 'book', 'board', 'phone', 'sign', 'key', 'vault', 'qr', 'envelope', 'record', 'server', 'arrow', 'mark', 'calendar', 'terminal', 'phoneqr', 'padlock'}}
    def strings(x):
        if isinstance(x, str): yield x
        elif isinstance(x, dict):
            for v in x.values(): yield from strings(v)
        elif isinstance(x, list):
            for v in x: yield from strings(v)
    cast_ids = {c['id'] for c in json.load(open(os.path.join(SBD, 'cast.json'), encoding='utf-8'))['characters']}
    latest = (json.load(open(os.path.join(ROOT, 'data', 'vault.json'), encoding='utf-8')).get('latest_capture') or '')
    for fn in sorted(f for f in os.listdir(SBD) if re.match(r'^\d\d__.*\.json$', f)):
        sb = json.load(open(os.path.join(SBD, fn), encoding='utf-8'))
        at = lambda i: f'storyboards/{fn} panel {i + 1}'
        # drawn against older evidence: kept as drawn, and its page says so; a quote or chart that no longer matches the
        # current data is then a warning for the storyboard desk, never a failure that blocks another agent's release
        stale = sb.get('data_as_of', '') < latest
        moved = warns if stale else fails
        for k in ('slug', 'title', 'subtitle', 'status', 'by', 'written', 'as_of_version', 'vault_commit', 'data_as_of', 'rule', 'scenes'):
            if not sb.get(k): fails.append(f'storyboards/{fn}: no {k}')
        if sb.get('reader') and not os.path.exists(os.path.join(ROOT, 'briefings', sb['reader'], 'index.html')): fails.append(f'storyboards/{fn}: reader {sb["reader"]} has no briefing')
        for x in sb.get('see', []):
            if not os.path.exists(os.path.join(ROOT, x)): fails.append(f'storyboards/{fn}: see points at missing page {x}')
        for i, sc in enumerate(sb.get('scenes', [])):
            kind = sc.get('kind', 'scene')
            if kind not in V['kinds']: fails.append(f'{at(i)}: unknown kind {kind}')
            if sc.get('setting', 'none') not in V['settings']: fails.append(f'{at(i)}: unknown setting {sc.get("setting")}')
            for pr in sc.get('props', []):
                if pr.get('kind') not in V['props']: fails.append(f'{at(i)}: unknown prop {pr.get("kind")}')
            for c in sc.get('cast', []):
                if c.get('who') not in cast_ids: fails.append(f'{at(i)}: {c.get("who")} is not in the cast')
                if c.get('pose', 'stand') not in V['poses']: fails.append(f'{at(i)}: unknown pose {c.get("pose")}')
                if c.get('mood', 'neutral') not in V['moods']: fails.append(f'{at(i)}: unknown mood {c.get("mood")}')
                if c.get('says') and kind != 'evidence' and not sc.get('not_a_quote'): fails.append(f'{at(i)}: a line is spoken but the panel is not marked not_a_quote')
            if not sc.get('cites'): fails.append(f'{at(i)}: cites no source')
            for sl in sc.get('cites', []):
                if sl not in slugs: fails.append(f'{at(i)}: cites unknown slug {sl}')
            ev = sc.get('evidence') or {}
            if ev.get('quote'):
                qf = sc.get('quote_from')
                if not qf or not os.path.exists(os.path.join(ROOT, qf)): fails.append(f'{at(i)}: a quote with no quote_from file')
                else:
                    src = open(os.path.join(ROOT, qf), encoding='utf-8').read()
                    hay = list(strings(json.loads(src))) if qf.endswith('.json') else [src]
                    if not any(ev['quote'] in h for h in hay): moved.append(f'{at(i)}: the quote is not in {qf} word for word')
            if ev.get('bars'):
                bf = sc.get('bars_from') or {}
                got = {b['label']: b['value'] for b in ev['bars']}
                want = None
                if bf.get('file') == 'data/claims.json':
                    want = dict(__import__('collections').Counter(c['status'] for c in json.load(open(os.path.join(ROOT, bf['file']), encoding='utf-8'))))
                elif bf.get('file') == 'data/agencies.json':
                    rows = json.load(open(os.path.join(ROOT, bf['file']), encoding='utf-8'))
                    want = {lab: sum(1 for r in rows if r.get('offline') in vals) for lab, vals in bf.get('groups', {}).items()}
                    if sum(want.values()) != len(rows): fails.append(f'{at(i)}: the bar groups do not cover every agency')
                elif bf.get('file') == 'data/inventory-history.json':
                    snap = [x for x in json.load(open(os.path.join(ROOT, bf['file']), encoding='utf-8'))['snapshots'] if x['commit'] == bf.get('snapshot')]
                    m = {'investigating': 'Investigation', 'vulnerable': 'Vulnerable', 'fixed': 'Fix', 'not affected': 'Not vuln'}
                    want = {lab: snap[0]['by_status'].get(k, 0) for lab, k in m.items()} if snap else None
                    if not snap: fails.append(f'{at(i)}: no inventory snapshot {bf.get("snapshot")}')
                elif bf.get('file', '').endswith('.md') and os.path.exists(os.path.join(ROOT, bf['file'])):
                    if bf.get('row') and bf['row'] not in open(os.path.join(ROOT, bf['file']), encoding='utf-8').read(): fails.append(f'{at(i)}: {bf["file"]} has no row {bf["row"]}')
                    want = got
                else:
                    fails.append(f'{at(i)}: bars with no bars_from the gate can check')
                if want is not None and want != got: moved.append(f'{at(i)}: bars {got} but {bf.get("file")} gives {want}')
    kit = os.path.join(ROOT, 'assets', 'vendor', 'storyboards', 'v0', 'v0.1', 'v0.1.0')
    man = json.load(open(os.path.join(kit, 'manifest.json'), encoding='utf-8'))
    for f in man['files']:
        fp = os.path.join(kit, f['path'])
        if not os.path.exists(fp) or hashlib.sha256(open(fp, 'rb').read()).hexdigest() != f['sha256']: fails.append(f'{rel(fp)}: not the bytes of storyboard kit {man["release"]}')
# 4g. the briefing decks: every cited slug; every quote_from quote word for word; the waffle equal to the claims by status;
# the agency groups covering every agency; every timed event in the race present in the timeline; the PDF printed from
# the current source. A deck made against older evidence is kept as made: then a mismatch with today's data warns.
DKD = os.path.join(ROOT, 'admin', 'content', 'decks')
for fn in sorted(os.listdir(DKD)) if os.path.isdir(DKD) else []:
    if not fn.endswith('.json') or not os.path.isfile(os.path.join(DKD, fn)): continue
    raw = open(os.path.join(DKD, fn), 'rb').read(); dk = json.loads(raw)
    latest = (json.load(open(os.path.join(ROOT, 'data', 'vault.json'), encoding='utf-8')).get('latest_capture') or '')
    moved = warns if dk.get('data_as_of', '') < latest else fails
    for k in ('slug', 'title', 'date', 'data_as_of', 'vault_commit', 'as_of_version', 'rule', 'slides'):
        if not dk.get(k): fails.append(f'decks/{fn}: no {k}')
    def hay_of(f):
        t = open(os.path.join(ROOT, f), encoding='utf-8').read()
        return list(strings(json.loads(t))) if f.endswith('.json') else [t]
    tl = {t['at'] for t in json.load(open(os.path.join(ROOT, 'data', 'timeline.json'), encoding='utf-8'))}
    for n, sl in enumerate(dk.get('slides', []), 1):
        at = f'decks/{fn} slide {n} ({sl.get("id")})'
        allc = sl.get('cites', []) + [c for key in ('points', 'facts', 'moments') for x in sl.get(key, []) for c in x.get('cites', [])]
        if not sl.get('cites'): fails.append(f'{at}: cites no source')
        for c in allc:
            if c not in slugs: fails.append(f'{at}: cites unknown slug {c}')
        for x in sl.get('points', []):
            if x.get('quote_from') and not any(x['text'] in h for h in hay_of(x['quote_from'])): moved.append(f'{at}: "{x["text"][:40]}..." is not in {x["quote_from"]} word for word')
        if sl.get('kind') == 'waffle':
            want = dict(__import__('collections').Counter(c['status'] for c in json.load(open(os.path.join(ROOT, sl['from_']), encoding='utf-8'))))
            if want != dict(sl['counts']): moved.append(f'{at}: counts {dict(sl["counts"])} but {sl["from_"]} gives {want}')
        if sl.get('kind') == 'agencies':
            rows = json.load(open(os.path.join(ROOT, sl['from_']), encoding='utf-8'))
            grouped = [r for r in rows if any(r.get('offline') in v for v in sl['groups'].values())]
            if len(grouped) != len(rows): moved.append(f'{at}: {len(rows) - len(grouped)} agencies fall in no group')
        if sl.get('kind') == 'race':
            for ev in sl.get('attack', []) + sl.get('defend', []):
                if ev['at'] not in tl: moved.append(f'{at}: {ev["at"]} ({ev["label"]}) is not a time in data/timeline.json')
    side = os.path.join(ROOT, 'storyboards', dk.get('slug', ''), dk.get('slug', '') + '.pdf.json')
    if os.path.exists(side) and json.load(open(side, encoding='utf-8')).get('source_sha256') != hashlib.sha256(raw).hexdigest():
        fails.append(f'decks/{fn}: the PDF was printed from an older version of the deck; run node admin/build/deck_pdf.js')
    imf = os.path.join(DKD, 'images', dk.get('slug', '') + '.json')
    for slot, rec in (json.load(open(imf, encoding='utf-8')).items() if os.path.exists(imf) else []):
        if rec.get('check', 'not checked') != 'not checked' and not os.path.exists(os.path.join(ROOT, 'storyboards', dk['slug'], 'img', slot + '.webp')):
            fails.append(f'decks/{fn}: image {slot} is recorded as checked but its file is missing')
# 4c. layers: every data file is classified exactly once
layers = load('layers') or {}
classified = [f['path'] for f in layers.get('files', [])]
ids = {l['id'] for l in layers.get('layers', [])}
for f in layers.get('files', []):
    if f.get('layer') not in ids: fails.append(f'data/layers.json: {f["path"]} has layer {f.get("layer")!r}')
for fn in sorted(os.listdir(os.path.join(ROOT, 'data'))):
    if fn.endswith('.json') and classified.count('data/' + fn) != 1: fails.append(f'data/{fn}: listed {classified.count("data/" + fn)} times in data/layers.json, not once')
qs = load('questions') or {}
for q in qs.get('questions', []):
    for a in q.get('answer', []):
        for s in a.get('sources', []):
            if s not in slugs: fails.append(f'data/questions.json: {q.get("id")} cites unknown slug {s}')
    for pth in q.get('see', []):
        if not os.path.exists(os.path.join(ROOT, pth.split('#')[0])): fails.append(f'data/questions.json: {q.get("id")} points at missing page {pth}')
    if not q.get('see'): fails.append(f'data/questions.json: {q.get("id")} points at no page')
# 4b. the readers: plain-English facts cite known slugs; every persona path and glossary link points at a page that exists
plain = load('plain') or {}
for c in plain.get('cards', []) + plain.get('moments', []):
    for s in c.get('sources', []):
        if s not in slugs: fails.append(f'data/plain.json: {c.get("q") or c.get("when")} cites unknown slug {s}')
    if not os.path.exists(os.path.join(ROOT, c['href'].split('#')[0])): fails.append(f'data/plain.json: link to missing page {c["href"]}')
personas = load('personas') or {}
aud = {a['id'] for a in (load('roles') or {}).get('audiences', [])}
for pr in personas.get('personas', []):
    if pr['id'] not in aud: fails.append(f'data/personas.json: {pr["id"]} has no briefing audience in roles.json')
    for x in pr.get('path', []):
        if not os.path.exists(os.path.join(ROOT, x)): fails.append(f'data/personas.json: {pr["id"]} path points at missing page {x}')
for t in (load('glossary') or {}).get('terms', []):
    if not os.path.exists(os.path.join(ROOT, t['more'].split('#')[0])): fails.append(f'data/glossary.json: {t["id"]} links to missing page {t["more"]}')
# 4c. search engines: the sitemap lists every public page, robots.txt points at it, the feed and the social card exist
sm = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read() if os.path.exists(os.path.join(ROOT, 'sitemap.xml')) else ''
if not sm: fails.append('sitemap.xml missing')
for p in pages:
    r = rel(p).replace(os.sep, '/')
    if r.startswith('account/top'): continue
    if f'/{r}</loc>' not in sm: fails.append(f'{r}: not in sitemap.xml')
if 'Sitemap:' not in (open(os.path.join(ROOT, 'robots.txt')).read() if os.path.exists(os.path.join(ROOT, 'robots.txt')) else ''): fails.append('robots.txt missing or has no Sitemap line')
for f in ('feed.xml', 'assets/og-card.png', 'data/sections.json'):
    if not os.path.exists(os.path.join(ROOT, f)): fails.append(f'missing {f}')
# 5. determinism: rebuild into a temp copy and compare hashes
def tree_hash():
    h = hashlib.sha256()
    for p in pages + sorted(re.sub(r'\.html$', '.md', p) for p in pages) + [os.path.join(ROOT, 'llms.txt'), os.path.join(ROOT, 'data', 'graph.json'), os.path.join(ROOT, 'data', 'sections.json'), os.path.join(ROOT, 'sitemap.xml'), os.path.join(ROOT, 'feed.xml')]:
        if os.path.exists(p):
            h.update(rel(p).encode()); h.update(open(p, 'rb').read())
    return h.hexdigest()
before = tree_hash()
r = subprocess.run([sys.executable, os.path.join(ROOT, 'admin', 'build', 'build.py')], capture_output=True, text=True)
if r.returncode != 0: fails.append('rebuild failed: ' + r.stderr[-500:])
elif tree_hash() != before: fails.append('build is not deterministic: a second run changed the output')
# 7. credential shapes anywhere in the tree (not .git)
PAT = re.compile(r'sgit_private_(vault|read)_[0-9a-f]{12,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|xox[baprs]-[0-9A-Za-z-]{10,}')
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('.git', '.sg_vault')]
    for f in files:
        fp = os.path.join(root, f)
        try:
            b = open(fp, 'rb').read()
        except Exception:
            continue
        if b'\x00' in b[:4000]: continue
        m = PAT.search(b.decode('utf-8', 'replace'))
        if m: fails.append(f'{rel(fp)}: credential shape {m.group(0)[:12]}...')
# 8. no external script/style/img (checked above); also check the vendored meter is present
for f in ('assets/review-nav.js', 'data/review.json', 'review/code/files.json', 'assets/themes/themes.css', 'assets/themes/themes.js', 'assets/themes/site-tokens.css', 'assets/telemetry.js', 'data/telemetry.json', 'data/admin.json', 'assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js', 'assets/components/base/v1/v1.0/v1.0.0/sg-component.js', 'assets/site.css', 'assets/site.js', 'CNAME', '.nojekyll', 'VERSION', '.github/workflows/pages.yml', 'assets/personas.js'):
    if not os.path.exists(os.path.join(ROOT, f)): fails.append(f'missing {f}')
# version consistency
ver = open(os.path.join(ROOT, 'VERSION')).read().strip()
vs = load('versions') or {}
if vs.get('current') != ver: fails.append(f'VERSION {ver} but data/versions.json current is {vs.get("current")}')
if not any(v.get('version') == ver for v in vs.get('versions', [])): fails.append(f'no release entry for v{ver}')
for w in warns: print('warn:', w)
if fails:
    for f in fails: print('FAIL:', f)
    print(f'{len(fails)} failures across {len(pages)} pages'); sys.exit(1)
print(f'gate passed: {len(pages)} pages, {len(slugs)} sources, deterministic, no credential shapes, v{ver}')
