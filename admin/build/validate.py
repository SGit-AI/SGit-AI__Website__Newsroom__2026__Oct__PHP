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
    if os.sep + 'sources' + os.sep not in p and os.sep + 'actors' + os.sep not in p and not p.endswith(os.path.join('affected', 'software.html')) and not p.endswith(os.path.join('brief', 'index.html')):
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
# 5. determinism: rebuild into a temp copy and compare hashes
def tree_hash():
    h = hashlib.sha256()
    for p in pages + sorted(re.sub(r'\.html$', '.md', p) for p in pages) + [os.path.join(ROOT, 'llms.txt'), os.path.join(ROOT, 'data', 'graph.json')]:
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
for f in ('assets/components/sg-meter/v1/v1.3/v1.3.1/sg-meter.js', 'assets/components/base/v1/v1.0/v1.0.0/sg-component.js', 'assets/site.css', 'assets/site.js', 'assets/personas.js', 'CNAME', '.nojekyll', 'VERSION', '.github/workflows/pages.yml'):
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
