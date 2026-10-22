# Release history

Every release of this site, with what changed, why, and the vault commit it was built from.

# Release history

One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v0.2.5. The data is [data/versions.json](../data/versions.json).

### v0.2.5 · 2026-10-22

the review layer: the php2shell fix mapped to the php-src code as layered graphs (the flaws, what the fix does, the files and functions it changed, derived from the diff), a static map at /review/ and a no-library navigator at /review/ui/, after the secrets.sgit.ai review pages

 Vault commit `200d08971937`.

Files:

### v0.2.4 · 2026-10-22

five themes (Newsprint, Night, Paper, Blueprint, Ember) with a picker in the bar, vendored from newsroom.sgit.ai; all colour moved to theme tokens; the reading-meter ratings card dropped for the quiet balance

 Vault commit `200d08971937`.

Files:

### v0.2.3 · 2026-10-22

the admin section (board, roles, briefs, the evidence vault opened with its public read key, who reads this site), anonymous telemetry over an append lane into a separate vault with its drain script and first report, and the page meter in quiet mode

 Vault commit `200d08971937`.

Files:

### v0.2.2 · 2026-10-22

the build, gate and release scripts are now committed: the repository's Python .gitignore template had ignored admin/build/, which is why the first Pages run could not find the gate

 Vault commit `200d08971937`.

Files:

### v0.2.1 · 2026-10-22

a Pages deploy workflow that runs the gate on every push to dev, and breadcrumbs up to October 2026, the year and the newsroom

 Vault commit `200d08971937`.

Files:

### v0.2.0 · 2026-10-22

the code read from php-src, php2shell in context against ten earlier flaws, an impact ledger of offline versus compromised, detection and defence from six WAF vendors and three rule sets, six more briefings, a page per source and per party with its own graph, 86 new sources

 Vault commit `200d08971937`.

Files:

### v0.1.0 · 2026-10-22

The site exists: a story front, the two flaws, the timeline, every claim with a status, the numbers that do not add up, the agencies compared, the affected versions and software, the exploitation signals, a playbook, six briefings, every source with its hashes, the graph, the method, the team, the billing model and this history.

First release, built from the evidence vault at commit 379e3d7f172a (61 sources, 62 captures, 390 hashed files). Vault commit `379e3d7f172a`.

Files: `admin/build/build.py`, `admin/build/export_vault.py`, `admin/build/validate.py`, `admin/build/release.sh`, `data/*.json`, `assets/site.css`, `assets/components/sg-meter/v1/v1.3/v1.3.1/`


---
site v0.2.5 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/versions.html
