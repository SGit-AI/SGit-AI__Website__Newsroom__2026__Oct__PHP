# Release history

Every release of this site, with what changed, why, and the vault commit it was built from.

# Release history

One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v0.3.0. The data is [data/versions.json](../data/versions.json).

### v0.3.0 · 2026-10-22

the first reader-first pass: fifteen named readers mapped by job and technical depth, a briefing for each opening with a thirty-second plain answer and a reading path, three new briefings (curious reader, website owner, project manager), a plain-English explainer, a glossary of 40 terms linked and hover-defined on first use on every page, every CVE ID linked, a plain-English line on every technical page, a reader bar that keeps your place, and a front page that leads with where things stand and who you are

Designed from the question the editor asked: who is reading, and what does the first screen do for them? The evidence is unchanged; every new sentence of fact cites the vault. Vault commit `200d08971937`.

Files: `data/personas.json`, `data/glossary.json`, `data/plain.json`, `data/roles.json`, `admin/build/build.py`, `admin/build/validate.py`, `assets/site.css`, `assets/personas.js`, `assets/site.js`

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
site v0.3.0 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/versions.html
