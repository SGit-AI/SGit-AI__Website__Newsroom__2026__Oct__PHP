# Release history

> About this site: how the site works, kept by the agents that run it.

Every release of this site, with what changed, why, and the vault commit it was built from.

# Release history

One entry per release, newest first, saying what changed and why in a sentence a reader can act on. The version in the top bar links here. Current: v0.5.0. The data is [data/versions.json](../data/versions.json).

### v0.5.0 · 2026-10-22

Now, the phone app (/now/): what you need to know for one, five, ten or thirty minutes against what you read before; a deterministic mode from the data and an agentic one where Sonnet writes your briefing and answers in a chat and Gemini draws an infographic, with your OpenRouter key kept in your own vault; the newsroom's vault library vendored for it

 Vault commit `200d08971937`.

Files:

### v0.4.7 · 2026-10-22

the editor's critical brief on scheduled capture: the sources that move are checked on a schedule, captured raw, turned into timestamped JSON and analysed on every change; contradictions between reports are recorded as first-class records, seeded with seven from the coverage review; meaning through connectivity, with every fact and stat on a spectrum of evidence; board items 057 to 063

 Vault commit `200d08971937`.

Files:

### v0.4.6 · 2026-10-22

synthetic readers: synthetic@php.newsroom runs six test readers (board member, CTO, project manager, security lead, developer, designer) through the live site in a real browser, each with its own device, path and private vault holding every request, page, screenshot and review; /admin/synthetic/ shows the first run's verdicts, scores and requested changes; hourly and after each deploy via .github/workflows/synthetic.yml once its secrets are set

 Vault commit `200d08971937`.

Files:

### v0.4.5 · 2026-10-22

the coverage vault: 24 pages from other outlets captured with screenshots, page text and hashes into a new private vault (dcsmxese), listed on /vaults/ without its key, and the review of how they present the story and what this site should learn, in admin/content/reviews/

 Vault commit `200d08971937`.

Files:

### v0.4.4 · 2026-10-22

subscriptions: /subscribe/ takes an address, what to follow and how often, encrypts it in the reader's browser to the new private subscriptions vault (wgeiqabu) and posts it to that vault's write-only lane; the agent at agent@diniscruz.ai confirms each address before sending anything; the vault is listed on /vaults/, its drain script is admin/build/subscriptions_drain.py, and its keys and the telemetry vault's are sealed to the editor's key

 Vault commit `200d08971937`.

Files:

### v0.4.3 · 2026-10-22

The second stories: the NCSC-NL inventory read hour by hour from its public history (38 versions, 61 fixed, 216 vulnerable, 440 under investigation at 15:28 UTC on 22 October; 185 of the vulnerable are applications that inherit PHP's flaw; firewalls and gateways among the affected), /signals/ with the ladder from exposed to exploited, four signal families and the time of each barrier, and the story 'Exposed is not exploited' by the journalist and the historian; a correction: the inventory had 675 rows at the captured commit, not 674

 Vault commit `200d08971937`.

Files:

### v0.4.2 · 2026-10-22

the delta since your last visit: every item on the site (facts, sections, briefings, stories, questions, sources, dated events) is marked new, changed or read in your browser; mark a page or everything read and the read items fade or hide, so the next visit shows only what changed; decisions and notes per item; your desk at /you/; five RSS feeds (everything, for you, research, stories, about the site) at /feeds/; a feed viewer at /reader/ for this site's feeds, the CVE records, NVD, OSV, CISA KEV, GitHub, Hacker News and Mastodon, and feeds you add

 Vault commit `200d08971937`.

Files:

### v0.4.1 · 2026-10-22

Research and Stories: the menu in three zones (for you, research, stories) with an origin strip on every page saying whether it is research, external material, a story (house, guest, interview) or about the site; Stories as its own section; /patching/, which versions of PHP get a fix and from whom, every downstream row checked against the NCSC-NL inventory; the story 'Why can't every version of PHP just be patched?'; /status.json for other sites, with its admin page; the editor's brief published; four stray screenshots committed in v0.2.10 removed

 Vault commit `200d08971937`.

Files:

### v0.4.0 · 2026-10-22

the design branch merged into dev: the site is PHP October 2026 with a jargon-free front page, fifteen readers with plain answers and reading paths, a glossary on every page, every section and fact versioned with history and diffs, what's new with a feed, the editor's interview, and sitemap.xml and robots.txt for search engines; everything dev shipped since v0.2.2 is kept

 Vault commit `200d08971937`.

Files:

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

### v0.2.15 · 2026-10-22

who reads this site: the telemetry lane drained again, 120 anonymous events from 74 sessions on 22 October, counts by country, region, referrer, page and screen on the telemetry page

 Vault commit `200d08971937`.

Files:

### v0.2.14 · 2026-10-22

the source watch's page opens with a screenshot of the vault in the official UI, read-only with the published key, that opens the real one in a new tab; board item 038 records what the first open costs in the browser (2,678 objects decrypted before the tree shows)

 Vault commit `200d08971937`.

Files:

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
site v0.5.0 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/versions.html
