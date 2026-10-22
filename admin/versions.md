# Release history

Every release of this site, with what changed, why, and the vault commit it was built from.

# Release history

One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v0.2.13. The data is [data/versions.json](../data/versions.json).

### v0.2.13 · 2026-10-22

the vaults: a Vaults section listing every vault behind the site (the evidence vault and the source watch with their read keys, the private telemetry vault with its write-only lane); the source watch (oq9gflln) published the way sgit.ai publishes vaults, with its key, a link that opens it in a new tab, the official UI embedded and its features (raw and analysis trees, country to page taxonomy, access classes, licence tiers, graphs at four altitudes, runs, tips, tools) from data/source-watch.json; the evidence vault page embeds its app too

 Vault commit `200d08971937`.

Files:

### v0.2.12 · 2026-10-22

deploys from several agents: the Pages workflow queues deploys instead of cancelling the one in flight, and release.sh takes in what other agents released before it bumps and again if its push loses a race; /status/ shows each newsroom site's deploy runs from GitHub's public API with no credential, beside the version each serves, and every page notes when a newer release is live

 Vault commit `200d08971937`.

Files:

### v0.2.11 · 2026-10-22

the release check reads the live version correctly: v0.2.9's pattern matched the v in class="ver" and read a blank version, so it reported every release unverified; now tested against the live site for older, equal and newer versions

 Vault commit `200d08971937`.

Files:

### v0.2.10 · 2026-10-22

pricing by content type and freshness: every content page metered (only the meter's own pages are not), price = max(1p, round(base x freshness)) with tiers picked in the reader's browser, the formula and rules of engagement on the billing page; second readings: Perplexity's notes published in full and credited, compared with the vault point by point; the newsroom's review of the site published as received, with a triage and fourteen board items; briefing titles and table word-wrapping fixed

 Vault commit `200d08971937`.

Files:

### v0.2.9 · 2026-10-22

the release check now accepts this version or later, because several agents release to dev and one can land on top of another inside the polling window (v0.2.8 landed on v0.2.7 and the old exact check called a live release unverified)

 Vault commit `200d08971937`.

Files:

### v0.2.8 · 2026-10-22

the articles layer and the evidence, derived, authored split: a journalist's state-of-affairs report and a historian's perspective, both written against v0.2.5 (the librarian's questions shipped alongside as v0.2.6, the dev agent's key as v0.2.7); /layers/ classifying every data file, checked by the gate; the menu split into story, articles, analysis and evidence; a front page and navigation review; the front page's 'six briefings' corrected to the computed twelve

 Vault commit `200d08971937`.

Files:

### v0.2.7 · 2026-10-22

dev@php.newsroom's public key from pki.sgit.ai on the roles page (record sha256:8025e2a4470e73f0, key link and QR), the brief for handing the editor the telemetry vault key sealed to his key, and board item 013

 Vault commit `200d08971937`.

Files:

### v0.2.6 · 2026-10-22

the librarian joins (librarian@php.newsroom): /questions/, the questions readers ask with a short answer to paste back, the sourced answer and the pages that carry it, starting from a reader's 'can anything be done, or do we wait for updates?'; a catalogue of every page; articles readers saw that the vault has not captured, listed as seen, not cited

 Vault commit `200d08971937`.

Files:

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
site v0.2.13 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/versions.html
