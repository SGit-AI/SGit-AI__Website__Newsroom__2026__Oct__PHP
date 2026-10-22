#!/usr/bin/env python3
"""Drain the subscriptions lane into the subscriptions vault.

Run by whoever holds the subscriptions vault (wgeiqabu): a clone at --vault with .sg_vault/local/lane.json and
.sg_vault/local/pki-passphrase, and the key pair in ~/.sg-send/keys/ (identity/private/ in the vault holds a
copy). Lists the lane with the enum key, fetches and decrypts each request (the same calls as
telemetry_drain.py), appends them to requests/<date>.jsonl, marks them processed, and updates subscribers.json:
one row per address with its latest request and status (requested, left; confirmed is set by the agent at
agent@diniscruz.ai when the address answers). Nothing from here is ever copied to the site, which is public.
"""
import argparse, datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from telemetry_drain import post, decrypt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True); ap.add_argument('--fingerprint', default='sha256:fccac5cde1503b62')
    ap.add_argument('--keep-pending', action='store_true')
    a = ap.parse_args()
    V = os.path.abspath(a.vault)
    lane = json.load(open(os.path.join(V, '.sg_vault', 'local', 'lane.json')))
    passphrase = open(os.path.join(V, '.sg_vault', 'local', 'pki-passphrase')).read().strip()
    H = {'x-sgraph-vault-enum-key': lane['enum_key']}
    base = f"{lane['endpoint']}/api/vault/append"
    today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    os.makedirs(os.path.join(V, 'requests'), exist_ok=True)
    got, after, rows = [], None, []
    while True:
        body = {'include_content': False}
        if after: body['after_file_id'] = after
        r = post(f"{base}/list/{lane['vault_id']}", body, H)
        entries = r.get('entries', [])
        got += entries
        if not r.get('truncated') or not entries: break
        after = entries[-1]['file_id']
    for i in range(0, len(got), 50):
        batch = got[i:i + 50]
        f = post(f"{base}/fetch/{lane['vault_id']}", {'inbox': lane['append_token'], 'file_ids': [e['file_id'] for e in batch]}, H)
        files = f.get('files') or f.get('entries') or []
        for item in files:
            fid = item.get('file_id') or item.get('id'); content = item.get('content') or item.get('payload')
            if not content: continue
            try:
                req = json.loads(decrypt(content, a.fingerprint, passphrase))
            except Exception as e:
                req = {'v': 0, 'undecryptable': True, 'error': str(e)[:120]}
            req['_file'] = fid
            rows.append(req)
        if not a.keep_pending and files:
            post(f"{base}/mark-processed/{lane['vault_id']}", {'inbox': lane['append_token'], 'file_ids': [x.get('file_id') or x.get('id') for x in files]}, H)
    with open(os.path.join(V, 'requests', f'{today}.jsonl'), 'a', encoding='utf-8') as f:
        for q in rows: f.write(json.dumps(q, ensure_ascii=False, sort_keys=True) + '\n')
    sp = os.path.join(V, 'subscribers.json')
    subs = json.load(open(sp)) if os.path.exists(sp) else {'about': 'One row per address. status: requested (unconfirmed), confirmed (the address answered), left.', 'subscribers': {}}
    for q in sorted((x for x in rows if x.get('email')), key=lambda x: x.get('at') or ''):
        e = q['email'].strip().lower()
        row = subs['subscribers'].get(e, {'status': 'requested', 'first': q.get('at')})
        if q.get('kind') == 'unsubscribe':
            row['status'] = 'left'
        else:
            row.update({'zones': q.get('zones'), 'cadence': q.get('cadence')})
            if row.get('status') == 'left': row['status'] = 'requested'
        row['last'] = q.get('at'); row['requests'] = row.get('requests', 0) + 1
        subs['subscribers'][e] = row
    json.dump(subs, open(sp, 'w'), indent=1, ensure_ascii=False, sort_keys=True)
    c = {}
    for r in subs['subscribers'].values(): c[r['status']] = c.get(r['status'], 0) + 1
    print(f'pending {len(got)}, drained {len(rows)}; addresses by status: {c}')

if __name__ == '__main__':
    main()
