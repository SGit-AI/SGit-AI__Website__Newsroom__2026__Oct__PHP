# Release history

Every release of this site, with what changed, why, and the vault commit it was built from.

# Release history

One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v0.3.2. The data is [data/versions.json](../data/versions.json).

### v0.3.2 · 2026-10-22

every section versioned and every fact given a timeline: each briefing, front-page section and story page records the release that wrote it, with its history and a diff of every change; a page per fact, from publication to this site; what's new, release by release, with a feed; the fact pipeline; the editor interviewed in his own words; a sitemap, robots.txt and structured data for search engines

From the editor: what's new must be visible, every section must say which release wrote it, a version must move only when what its reader sees changes, and every fact needs a timeline. Vault commit `200d08971937`.

Files: `data/sections.json`, `data/interview.json`, `data/seo.json`, `admin/build/build.py`, `admin/build/seed_ledger.py`, `admin/build/validate.py`, `assets/site.css`, `assets/og-card.png`, `sitemap.xml`, `robots.txt`, `feed.xml`

### v0.3.1 · 2026-10-22

the site is renamed PHP October 2026, PHP news for the month rather than one nickname, and its front page is now jargon-free and about the current situation: right now, at a glance, the core facts each with its status and evidence, what nobody knows yet and the latest; the technical front page moved to the specialist summary

From the editor: the site should be named for PHP in October, not for the incident, so that it can carry whatever PHP news the month brings; and the first page must be readable by anyone. Vault commit `200d08971937`.

Files: `data/plain.json`, `data/story.json`, `admin/build/build.py`, `assets/site.css`, `BRIEF-CORRECTIONS.md`

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
site v0.3.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/versions.html
