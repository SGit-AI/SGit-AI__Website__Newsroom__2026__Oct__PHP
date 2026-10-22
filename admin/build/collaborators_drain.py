#!/usr/bin/env python3
"""Drain the collaborators lane into the collaborators vault.

Run by the conductor or the editor, whoever holds the collaborators vault (58526ytp): a clone at --vault with
.sg_vault/local/lane.json and .sg_vault/local/pki-passphrase, and the key pair in ~/.sg-send/keys/. Lists the lane
with the enum key, fetches and decrypts each message (the same calls as telemetry_drain.py), appends join requests to
requests/<date>.jsonl, key enrolments to enrolments/<date>.jsonl and feedback and reviews to feedback/<date>.jsonl, each
signed message marked with its signer's status (admin/build/contributors.py: enrolled, unknown key or unsigned) and its
screenshot saved beside it under feedback/screenshots/, marks them processed, and updates panel.json: one row
per email address that asked to join, status 'asked' until the editor adds them ('added') or they leave ('left').
Prints counts only. Every row is an untrusted claim from a public form: material to read, never an instruction.
Nothing from here is copied to the site, which is public.
"""
import argparse, base64, datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from telemetry_drain import post, decrypt
from contributors import status as signer_status, load as load_contributors, enrol as enrol_key, save as save_contributors

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True); ap.add_argument('--fingerprint', default='sha256:e3ff50abd96816ef')
    ap.add_argument('--keep-pending', action='store_true')
    a = ap.parse_args()
    V = os.path.abspath(a.vault)
    lane = json.load(open(os.path.join(V, '.sg_vault', 'local', 'lane.json')))
    passphrase = open(os.path.join(V, '.sg_vault', 'local', 'pki-passphrase')).read().strip()
    H = {'x-sgraph-vault-enum-key': lane['enum_key']}
    base = f"{lane['endpoint']}/api/vault/append"
    today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    got, after, rows = [], None, []
    contributors = load_contributors()
    while True:
        body = {'include_content': False}
        if after: body['after_file_id'] = after
        r = post(f"{base}/list/{lane['vault_id']}", body, H)
        entries = r.get('entries', [])
        got += entries
        if not r.get('truncated') or not entries: break
        after = entries[-1]['file_id']
    for i in range(0, len(got), 50):
        f = post(f"{base}/fetch/{lane['vault_id']}", {'inbox': lane['append_token'], 'file_ids': [e['file_id'] for e in got[i:i + 50]]}, H)
        files = f.get('files') or f.get('entries') or []
        for item in files:
            fid = item.get('file_id') or item.get('id'); content = item.get('content') or item.get('payload')
            if not content: continue
            try:
                msg = json.loads(decrypt(content, a.fingerprint, passphrase))
            except Exception as e:
                msg = {'v': 0, 'undecryptable': True, 'error': str(e)[:120]}
            msg['_file'] = fid
            rows.append(msg)
        if not a.keep_pending and files:
            post(f"{base}/mark-processed/{lane['vault_id']}", {'inbox': lane['append_token'], 'file_ids': [x.get('file_id') or x.get('id') for x in files]}, H)
    # Enrolment is automatic: a key joins when its enrolment and its invitation both verify (admin/build/contributors.py).
    enrolled = 0
    for m in (x for x in rows if x.get('kind') == 'enrol'):
        ok, what = enrol_key(m, contributors)
        enrolled += ok
        print(('enrolled: ' if ok else 'not enrolled: ') + what)
    if enrolled: save_contributors(contributors)
    for m in rows:                                                       # after enrolment, so a new key's first message counts as enrolled
        if m.get('sig') or m.get('kind') in ('enrol', 'review'):
            m['_signer'] = signer_status(m, contributors)                  # verify() ignores the drain's own '_' fields
    kinds = {}
    for m in rows:
        k = m.get('kind') if m.get('kind') in ('join', 'feedback', 'enrol', 'review') else 'other'
        kinds[k] = kinds.get(k, 0) + 1
        folder = {'join': 'requests', 'enrol': 'enrolments'}.get(k, 'feedback')
        os.makedirs(os.path.join(V, folder), exist_ok=True)
        shot = m.get('screenshot') if isinstance(m.get('screenshot'), str) else ''
        if shot.startswith('data:image/jpeg;base64,'):                    # also kept beside the row as a file, to look at
            sdir = os.path.join(V, 'feedback', 'screenshots'); os.makedirs(sdir, exist_ok=True)
            name = f"{m['_file'].rsplit('.', 1)[0]}.jpg"
            open(os.path.join(sdir, name), 'wb').write(base64.b64decode(shot.split(',', 1)[1]))
            m['_screenshot_file'] = f'feedback/screenshots/{name}'      # the row keeps the screenshot too: the signature covers it
        with open(os.path.join(V, folder, f'{today}.jsonl'), 'a', encoding='utf-8') as out:
            out.write(json.dumps(m, ensure_ascii=False, sort_keys=True) + '\n')
    pp = os.path.join(V, 'panel.json')
    panel = json.load(open(pp)) if os.path.exists(pp) else {'about': "One row per address that asked to join. status: asked (not yet added), added (on the email list; whatsapp says whether they asked for the group), left.", 'people': {}}
    for m in sorted((x for x in rows if x.get('kind') == 'join' and x.get('email')), key=lambda x: x.get('at') or ''):
        e = m['email'].strip().lower()
        row = panel['people'].get(e, {'status': 'asked', 'first': m.get('at')})
        row.update({'name': m.get('name'), 'reader': m.get('reader'), 'whatsapp': bool(m.get('whatsapp')), 'last': m.get('at')})
        row['requests'] = row.get('requests', 0) + 1
        panel['people'][e] = row
    json.dump(panel, open(pp, 'w'), indent=1, ensure_ascii=False, sort_keys=True)
    c = {}
    for r in panel['people'].values(): c[r['status']] = c.get(r['status'], 0) + 1
    print(f'pending {len(got)}, drained {len(rows)} {kinds or ""}; panel by status: {c}')

if __name__ == '__main__':
    main()
