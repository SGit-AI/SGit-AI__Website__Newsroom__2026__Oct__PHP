#!/usr/bin/env python3
"""Checking what a contributor signed: the same canonical bytes the browser signs (assets/feedback/identity.js), and
`sgit pki verify` to check the signature. Kept by conductor@php.newsroom; the brief is
admin/content/briefs/2026-10-22__brief__feedback-keys-and-review.md.

A message carries its signer's public bundle; verify() checks that the bundle's signing key is the one its fingerprint
names, that `from` is that fingerprint, and that the signature over canon(message without sig) + "\\n" is good. That proves
which key wrote it. Whether that key belongs to a contributor is data/contributors.json's question (status()).
Standard library and the sgit CLI only.
"""
import base64, hashlib, json, os, subprocess, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def canon(v):
    """pki.sgit.ai's canonical JSON, as JavaScript writes it: keys sorted, no whitespace, non-ASCII left as it is."""
    if isinstance(v, float): raise ValueError('a signed message carries no non-integer numbers')
    if isinstance(v, list): return '[' + ','.join(canon(x) for x in v) + ']'
    if isinstance(v, dict): return '{' + ','.join(json.dumps(k, ensure_ascii=False) + ':' + canon(v[k]) for k in sorted(v)) + '}'
    return json.dumps(v, ensure_ascii=False)

def fingerprint(pem_text):
    """sgit's fingerprint of a public key: sha256: and the first 16 hex of the SHA-256 of its SPKI bytes."""
    body = ''.join(l for l in pem_text.strip().splitlines() if not l.startswith('-----'))
    return 'sha256:' + hashlib.sha256(base64.b64decode(body)).hexdigest()[:16]

def verify(msg):
    """(True, '') when the message is signed by the key in its own bundle; (False, why) otherwise."""
    b, sig, frm = msg.get('bundle') or {}, msg.get('sig'), msg.get('from')
    if not sig or not frm: return False, 'unsigned'
    if not b.get('sign') or fingerprint(b['sign']) != b.get('signing_fingerprint') or frm != b.get('signing_fingerprint'):
        return False, 'the bundle does not match the signer'
    body = {k: v for k, v in msg.items() if k != 'sig' and not k.startswith('_')}   # '_' fields are the drain's, added after signing
    with tempfile.TemporaryDirectory() as d:
        home = os.path.join(d, 'home'); os.makedirs(home)
        env = dict(os.environ, HOME=home)                                   # a throwaway keystore: importing never touches the real one
        bp, mp, sp = (os.path.join(d, n) for n in ('bundle.json', 'msg.bin', 'msg.bin.sig'))
        json.dump(b, open(bp, 'w'))
        open(mp, 'wb').write((canon(body) + '\n').encode())
        json.dump({'signature': sig, 'fingerprint': frm}, open(sp, 'w'))
        subprocess.run(['sgit', 'pki', 'import', bp], env=env, capture_output=True, timeout=60)
        r = subprocess.run(['sgit', 'pki', 'verify', '--json', mp, sp], env=env, capture_output=True, text=True, timeout=60)
    try: res = json.loads(r.stdout or '{}')
    except ValueError: res = {}
    return (True, '') if res.get('valid') is True else (False, str(res.get('error') or r.stderr or 'the signature does not verify').strip()[-200:])

def load():
    return json.load(open(os.path.join(ROOT, 'data', 'contributors.json'), encoding='utf-8'))

def status(msg, data=None):
    """'enrolled' (a known contributor's key), 'unknown key' (signed, not enrolled), or 'unsigned' / why it failed."""
    ok, why = verify(msg)
    if not ok: return why
    keys = {k['signing_fingerprint']: k for k in (data or load())['keys']}
    return 'enrolled' if msg['from'] in keys else 'unknown key'
