#!/usr/bin/env bash
# Bump, build, validate, tripwire, push, verify live. In that order, every time.
# Usage: admin/build/release.sh "<one sentence: what changed and why>" [patch|minor|major]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"; cd "$ROOT"
MSG="${1:?release message required}"; PART="${2:-patch}"
BRANCH="${RELEASE_BRANCH:-dev}"
OLD="$(cat VERSION)"; IFS=. read -r MA MI PA <<< "$OLD"
case "$PART" in major) MA=$((MA+1)); MI=0; PA=0;; minor) MI=$((MI+1)); PA=0;; *) PA=$((PA+1));; esac
NEW="$MA.$MI.$PA"
# 1. bump: VERSION and a release entry in data/versions.json (the entry's title is the message)
python3 - "$NEW" "$MSG" <<'PY'
import json, sys, datetime
new, msg = sys.argv[1], sys.argv[2]
p = 'data/versions.json'; j = json.load(open(p))
vault = json.load(open('data/vault.json'))
j['current'] = new
j['versions'].insert(0, {'version': new, 'date': datetime.date.today().isoformat(), 'title': msg, 'summary': '', 'changes': [], 'vault_commit': vault['head']['commit'], 'reconstructed': False})
json.dump(j, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
open('VERSION', 'w').write(new + '\n')
PY
echo "v$OLD -> v$NEW"
# 2. build  3. validate
python3 admin/build/build.py
python3 admin/build/validate.py
# 4. tripwire on the staged diff (credential shapes, including the secret part of any locally held vault key)
git add -A
if git diff --cached | grep -E -n 'sgit_private_(vault|read)_[0-9a-f]{12,}|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}' ; then
  echo "tripwire: credential shape in the staged diff; release aborted"; exit 1
fi
if [ -d .sg_vault/local ]; then
  for k in $(grep -rhoE '[a-z0-9]{8,}:[a-z0-9]{8}' .sg_vault/local 2>/dev/null | cut -d: -f1 | sort -u); do
    if git diff --cached | grep -q "$k"; then echo "tripwire: a locally held key's secret part is in the diff"; exit 1; fi
  done
fi
# 5. commit and push
if [ -n "${RELEASE_TRAILER:-}" ]; then git commit -q -m "v$NEW: $MSG" -m "$RELEASE_TRAILER"; else git commit -q -m "v$NEW: $MSG"; fi
git push -u origin "HEAD:$BRANCH"
# 6. verify live: poll the site for the version in the top bar
URL="https://$(cat CNAME)/index.html"
for i in $(seq 1 40); do
  if curl -fsS --max-time 20 "$URL" 2>/dev/null | grep -q ">v$NEW<"; then echo "live: $URL serves v$NEW"; exit 0; fi
  sleep 15
done
echo "NOT VERIFIED: $URL does not serve v$NEW after 10 minutes. The push succeeded; the release is not done."; exit 2
