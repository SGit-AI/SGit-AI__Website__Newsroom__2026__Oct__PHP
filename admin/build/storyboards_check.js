#!/usr/bin/env node
// Runs the storyboard kit's own validator (formats.js, vendored v0.1.0) over every storyboard in
// admin/content/storyboards/. The gate (validate.py) checks the same vocabulary in Python; this is the kit's word on it.
// Usage: node admin/build/storyboards_check.js
const fs = require('fs'), path = require('path');
const ROOT = path.resolve(__dirname, '..', '..');
const F = require(path.join(ROOT, 'assets/vendor/storyboards/v0/v0.1/v0.1.0/formats.js'));
const dir = path.join(ROOT, 'admin/content/storyboards');
const cast = JSON.parse(fs.readFileSync(path.join(dir, 'cast.json'), 'utf8'));
let bad = 0, n = 0;
for (const f of fs.readdirSync(dir).filter(f => /^\d\d__.*\.json$/.test(f)).sort()) {
  const sb = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  const errs = F.validate(sb, cast, { props: F.PACKS.security });
  n++; bad += errs.length;
  console.log(`${errs.length ? 'FAIL' : 'ok  '} ${f}: ${sb.scenes.length} panels` + (errs.length ? '\n  ' + errs.join('\n  ') : ''));
}
console.log(`${n} storyboards, ${bad} problems`);
process.exit(bad ? 1 : 0);
