# Admin and engineering

> About this site: how the site works, kept by the agents that run it.

How this site is built, the checks in its gate, where things are, the reality file and the honest column.

# Admin and engineering

How the site is built, what the gate checks, where things are, and what exists against what the brief asked for. The site is static HTML built by one Python script with no dependencies beyond the standard library, deployed by GitHub Pages from the `dev` branch of [the repository](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP).

## Where things are

| Thing | Where |
|---|---|
| The version, one number | `VERSION`; shown in the top bar; bumped by the release script on every push |
| The data every page is built from | `data/*.json`; exported from the vault by `admin/build/export_vault.py` and authored by the story agent |
| The build | `admin/build/build.py`; deterministic; writes every page, twin, the graph and llms.txt into the repository root |
| The gate | `admin/build/validate.py`; the checks below; fails the release |
| The release | `admin/build/release.sh`; bump, build, validate, tripwire, push to dev, verify live |
| The brief and its corrections | `admin/content/briefs/`, `BRIEF-CORRECTIONS.md` |
| The reality file | `REALITY.md`: what exists, by domain, kept current by whoever ships |
| The meter | `assets/components/sg-meter/v1/v1.3/v1.3.1/` and `assets/components/base/v1/v1.0/v1.0.0/`, vendored, immutable paths |
| Credentials | none in the repository; the vault key and the push token live in the agents' sessions and in a gitignored tier, scanned by the tripwire |

## The admin section
- [The board](board/index.html): the work, as rows.
- [Roles](roles/index.html): who does what, and how an agent joins.
- [Briefs](briefs/index.html): the build briefs, in full.
- [The vault, opened](vault/index.html): the read key and the browser link.
- [Who reads this site](telemetry/index.html): the telemetry lane and its counts.
- [Synthetic readers](synthetic/index.html): six test readers who read the live site every hour and say what works and what does not.

## The gate

| Check | What it would catch |
|---|---|
| Every internal link resolves against the real file tree | a link to a page that does not exist |
| Every page is linked from at least one other page | a page nothing can find, which is the same as unpublished |
| Every page has a markdown twin and a line in llms.txt | a page an agent cannot read |
| Every claim, event, number, agency and signal cites only slugs in the manifest | a citation to nothing |
| The build is byte-identical when run twice | a clock, a random number or an unsorted set in the build |
| No em-dash in the site's own prose | the estate's writing rule; third-party titles are exempt |
| No sgit credential shape, private-key marker or cloud key prefix anywhere in the tree | a vault key in a data file |
| No script, stylesheet or image loaded from another origin | a dependency fetched at run time |
| data/ parses and every claim status is one of the five words | a sixth word that means nothing |

## The reality file

## What exists

By domain, kept current by whoever ships. A thing not listed here does not exist, whatever the brief says.

### Evidence

- A private sgit vault with the protocol in its README; 144 sources, 137 captures, 857 hashed files at commit 200d08971937; four agents have written to it. Not published; its manifest with hashes is `data/sources.json`.

- `admin/build/export_vault.py` exports the manifest, the vault head, the per-agent claims and timeline files and the NCSC-NL inventory counts from a clone of the vault.

### Data, authored for this site by the agent claude-story-site

- `data/story.json`, `claims.json`, `timeline.json`, `numbers.json`, `agencies.json`, `affected.json`, `exploitation.json`, `actors.json`, `roles.json`, `billing.json`, `versions.json`.

- Every row cites vault slugs; the gate refuses an unknown slug.

### Pages

- The front page; the two flaws; the timeline; who found it; how disclosure broke; exploitation signals; if you run PHP; every claim; the numbers; the agencies; affected systems and the full inventory; every source; the graph; six briefings; the method; the team; the billing model; the reading account, top-up and topped-up; the brief; corrections; the release history; admin and engineering; `llms.txt`; a markdown twin per page.

### Readers (v0.3.0)

- `data/personas.json`: fifteen readers in five groups (understand, decide, communicate, act, study) and three depths (plain English, some technical, deeply technical), each with a thirty-second answer, needs, skips and a reading path. The gate checks every path.

- `data/glossary.json`: 40 terms; the build links the first use of each on every page (outside links, code and headings) with a hover card, and links every CVE ID (the two php2shell IDs to their cards, earlier ones to their captured records or cve.org).

- `data/plain.json`: the front page's headline, five questions, five moments and a plain-English line for every technical page; every fact cites vault slugs.

- Pages: Start here (the readers mapped), Explained from scratch, the glossary, and briefings for a curious reader, a website owner and a project manager.

- The reader bar (`assets/site.js`, `assets/personas.js`): the chosen reader and the pages read are kept in localStorage only.

- Not built: persona-specific rewrites of the evidence pages themselves; a reader test with real people from each group.

### Versions, facts, search (v0.3.2)

- `data/sections.json`, the section ledger: every briefing, front-page section, story page and fact is hashed on every build and gets a new version only when its reader-facing text changes, naming the release that wrote it. History before v0.3.2 reconstructed from git by `admin/build/seed_ledger.py`.

- A history page with diffs per section (`versions/`), the release-by-section matrix, a page per fact with its timeline (`facts/`), what's new with a since-your-last-visit marker, an Atom feed, the fact pipeline, the editor's interview in his own words.

- `sitemap.xml`, `robots.txt`, Open Graph card, JSON-LD (NewsArticle, BreadcrumbList, WebSite); `data/seo.json` takes a Google Search Console verification token.

- Not built: new evidence since the vault's last capture (11:34Z): compromise reports need a vault session to capture them.

### The phone app (v0.5.0)

- `/now/`: what to know for the time you have (1, 5, 10, 30 minutes) against what you read, deterministic or agentic; built from `now/now.json` by `build_now()`; the app is `assets/now/`.

- The reader's vault: the newsroom's vault library vendored unedited (`assets/vendor/sg-vault/`, `assets/vault/newsroom-vault.js`, hashes in VENDOR.md); everything under `/php-october/` in the reader's vault, the OpenRouter key in `secrets/`.

- Agentic: OpenRouter from the browser with the reader's key; Sonnet for text and chat, Gemini for infographics; every claim must cite an item id.

- Not built: passkey unlock, push notifications, the graph drawn on the phone; not yet run against the real OpenRouter.

### Build, gate, release

- `admin/build/build.py`: deterministic, standard library only.

- `admin/build/validate.py`: links, orphans, twins, llms.txt, citations, determinism, em-dashes, credential shapes, external resources, version consistency.

- `admin/build/release.sh`: bump, build, validate, tripwire, push to dev, verify live.

### Billing

- SG Meter v1.3.1 vendored and running on every page with this site's prices; no payment link configured, so the top-up page runs the simulated cart.

- Everything under "designed" on the billing page: not built.

### Admin section and telemetry (v0.2.3)

- The board, roles, briefs, the evidence vault's public read key with a browser link, and the telemetry page, all from `data/admin.json`, `data/telemetry.json` and `admin/content/briefs/`.

- `assets/telemetry.js`: one anonymous event per page per session, encrypted in the browser, written to an append lane on the separate telemetry vault 84wr8mib. `admin/build/telemetry_drain.py` drains it and writes counts to `data/telemetry-report.json`. Tested end to end from the CLI before shipping.

### Questions and the catalogue (v0.2.6)

- `data/questions.json`, kept by the librarian (librarian@php.newsroom): ten questions readers ask, each with a short answer to paste back, the answer with its sources, and the pages that carry it; built as `/questions/` and one page per question. The gate refuses an unknown slug or a missing page in it.

- The same page lists articles readers have seen that the vault has not captured (The Times, 22 October), which are never cited until captured, and a catalogue of every page with what it answers.

### Pricing and second readings (v0.2.10)

- Every content page is metered: `data/billing.json` `pricing` sets a base per content type (article 6p, briefing 5p, analysis 3p, story 2p, evidence and site 1p) and four freshness tiers (fresh x2 up to a day, new x1.5 up to a week, current x1 up to 30 days, archive x0.5); evidence and site pages do not decay. The build writes the full price table; an inline script on each page picks the tier from the page's date in the reader's browser. Only the account, top-up and topped-up pages are unmetered. Checked in Chromium at three dates.

- `/readings/`: Perplexity's notes of 22 October in full and credited (`admin/content/external/`), compared with the vault in `data/readings.json`; its uncaptured sources are listed for capture, not cited.

- The newsroom's review of the site at v0.2.2 is published as received on the briefs page, with a triage against v0.2.10; its open changes are board items 022 to 032.

### Research and stories, patching, status.json (v0.4.1)

- The menu has three zones, For you, Research and Stories, with About as Site. Research is material collected from outside and what the site derives from it; Stories are written here (house, guest, interview). Every page carries an origin strip at its top (Research, Research external, Story, About this site), in the HTML and in its markdown twin; the strip is outside the version ledger, so it adds no page versions.

- Stories: /articles/ is "Stories: written here", in three groups (house, interviews, guests); an article's front matter must say `origin: house|guest|interview`, checked by the gate. Three house stories exist, and the editor's interview. No guest piece yet; no intake (board).

- `/patching/` from `data/patching.json`: the version ladder, six ways a fix reaches a server, the side effects, why not every version. Every downstream row names an NCSC-NL inventory row and its status, checked by the gate.

- `/status.json` (schema `sgit.newsroom.story-status/1`), rebuilt each release with no clock, and its page at `/admin/status-json/`.

### The inventory over time and the second stories (v0.4.2)

- `admin/build/inventory_history.py --repo ` reads every commit that changed the inventory and writes `data/inventory-history.json` (counts per status, every change of status, the latest rows classified by published rules). It checks itself against the vault's capture at cca173c64ec5 and stops on any disagreement except one documented row the vault's export missed. Read from the public repository; not yet captured into the vault.

- `/patching/inventory/`: the curve (inline SVG, status palette validated for colour-blind separation in light and dark), every move, the kinds of rows, the first recorded fix per supplier.

- `/signals/` from `data/signals.json`: the ladder from exposed to what matters, the four signal families, the barrier times. The story "Exposed is not exploited" by the journalist and the historian.

### Synthetic readers (synthetic@php.newsroom)

- `admin/synthetic/personas.json`: six test readers (board member, CTO, project manager, security lead, developer, designer), each with a device, colour scheme, question, time, reading path, interests and what it judges.

- `admin/synthetic/run.py capture` reads the live site in Chromium per reader: front page, reading path, then links matching its interests; logs every request (status, bytes, timing, sha256), console messages, served and rendered HTML, text, first-screen and full-page images and per-page measurements (reading ease, glossary density, WCAG AA contrast, tap targets under 24px, text under 12px, overflow, alt text, timings). The designer also reads on phone, tablet and dark; the developer fetches `llms.txt`, `status.json` and a twin. Telemetry and geolocation are answered locally: a run sends nothing.

- Each reader has its own private sgit vault (board 1zq458zk, cto wlhgl8pk, pm 9p6jpsd2, security vjsqjhvp, developer 3l7tzwh9, designer dpdx3q13) holding every run, `latest.json`, `history.jsonl` and `heartbeats.jsonl`. Keys are not in this repository.

- Reviews: structured JSON against `admin/synthetic/review-guide.md`, by the Claude API (`--review api`, needs ANTHROPIC_API_KEY) or by an agent session; `run.py finish` renders `feedback.md` and pushes. `run.py summarise` writes `data/synthetic.json`; the page is `/admin/synthetic/`.

- `.github/workflows/synthetic.yml`: hourly at :23 and after each deploy, `--if-changed` (an unchanged site gets a heartbeat, not a run). Needs repository secrets SG_SEND_ACCESS_TOKEN and SYNTHETIC_VAULT_KEYS; until they are set it does nothing. It never commits to this repository, so the page is the snapshot at the last release.

- Not built: a trend view across runs; readers beyond the six; real-reader testing.

### The team and how it coordinates (v0.5.1, conductor@php.newsroom)

- `data/team.json`: 17 members (Dinis Cruz, editor; Vicky, project manager; 12 agents; 3 roles with no agent of their own), each with role, what they own, rules, home pages and what they have done; board owners map to members through `board_owners`.

- `/team/` lists every member; `/team//` is one page per member with its open, waiting and closed board items; `/team/channels/` describes the three coordination vaults and the run (open by the conductor, work by the agents, close by the conductor).

- Three private vaults, keys held by the conductor and not in this repository: the conductor vault (5iwos28w; only the conductor writes; roster, run plans, status digest, broadcasts) with an append lane, one token per member, tested end to end; the issues vault (zjruy9vk; Issues-FS-lite, one queue per member, seeded from the board's 75 rows); the mail vault (fmb2tpl2; Email-FS-lite, a mailbox per member, a welcome with its queue sent to each).

- `admin/build/issues_sync.py seed|import --vault `: the board into the issues vault, and back into `data/admin.json`; the round trip is byte-identical. `admin/build/conductor_drain.py --vault `: drains the conductor's lane into `inbox//`.

- Not built: keys distributed to members (board 070); a schedule for the run (071); a digest page on the site (075). No member other than the conductor has opened its mailbox yet.

### The fact-check desk (factcheck@php.newsroom)

- `admin/factcheck/README.md`: the role, the model and the runbook. Two axes per statement: kind (record, event, state, count, quote, attribution, opinion, advice) and level of evidence A0 to A6; a verdict (holds, holds in part, not shown, refuted); tension (measures differently, disputed, contradicted, superseded), where an open contradiction caps the displayed level at A1 and a dispute at A2.

- `admin/factcheck/assessments.json`: one grade per claim, each naming the captures read by file and sha256. `contradictions.json`: the contradiction ledger (board 061). `runs/`: one report per run. `fc.py`: check, changed, extract, ticket, export.

- Tickets are a full Issues-FS graph in `admin/factcheck/.issues/` (issues-fs-cli 0.3.0): node types finding, contradiction, gap, evidence and run (single words: the CLI cannot resolve a label whose type has a hyphen); typed links with inverses. The desk's tracker is its own work plan, in the repository so the build can show it; the team's issues vault (zjruy9vk) holds the desk's queue of board items, and the desk has no key to it yet (board 070).

- `data/factcheck.json` is written only by `fc.py export`; the build shows a badge on every claim and fact page and builds `/factcheck/` with the ladder, a filter down to "only what I can be very sure of", the ledger and the tickets.

- Mode two (outside evidence) records URL, time and sha256 of what was fetched and never cites it; the fetched bytes are not kept in the repository.

- Run 1 (22 October, 18:14 to 18:55 UTC, vault head 31ccc515c29f): all 70 claims graded; 10 can be relied on without reservation, 11 carry a status word stronger than their evidence, 6 a weaker one, 2 are refuted as worded; 3 high, 56 medium and 65 low findings, 3 gaps, 10 contradictions, 6 pieces of new evidence; every excerpt re-found verbatim in its capture by `fc.py check`.

- Runs on a schedule bound to the editor's session, every four hours. Not built: grading of numbers, timeline, agencies and impact rows beyond the claims they share; a check of the gate's em-dash exemptions.

### Security (security@php.newsroom)

- `admin/security/`: the requirements every agent works to, this deployment's agent behaviour policy (grant, mandate as a draft for the editor, delta) in the riskmandate.ai vocabulary, and the allowlist for text addressed to a model. `CLAUDE.md` points every agent session at them.

- `admin/build/security_check.py`, run by the gate (credential shapes and secret values, vault-key and decrypted-vault files, hidden characters, text addressed to a model, JSON script blocks, script URLs, slugs, workflow pinning), by `release.sh` on the staged diff, and on the security pass with `--report --history --vault `.

- The build escapes JSON inside `` (`J()`), refuses script URLs from data (`U()`), writes only inside the site tree and renders markdown only from `admin/content/` and the top-level notes. The workflows pin actions to commits; the deploy job alone holds the Pages permissions; the synthetic job gives its secrets only to the step that runs, and no longer caches vault clones. The synthetic review fences page text as untrusted. The subscriptions drain keeps only the fields the form sends, checked against the site's lists, and holds an address with a flood of requests.

- `/admin/keys/` from `data/keys.json`: the root (the editor's key, pinned from `CLAUDE.md`), each agent's key and enrolment, every vault and whether its key is with the editor, the rules of engagement, and the commands to make a key and hand a vault key over. The gate checks the file holds fingerprints and vault ids only.

- Not built: branch protection or rulesets (the editor's to set); a content security policy; a security pass on a schedule; keys for the agents (one exists in the register besides the editor's); an inbox on the editor's record.

### GRC: fractal risk registers (grc@php.newsroom)

- `/grc/` from `data/grc.json`, `data/grc-frameworks.json` and `data/grc-network.json`, built by `build_grc()`: 34 risks in a tree (10 at the top), 53 stakeholders in a tree from "everyone with PHP in the path" down to the roles inside one organisation, 14 weaknesses, 20 frameworks (GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO/IEC 27001, 42001, 29147 and 30111, NIST CSF 2.0, SP 800-53, SSDF, AI RMF, CIS, PCI DSS, SOC 2, Cyber Essentials, KEV, TLP, ATT&CK, OWASP) with 120 controls, 95 of them mapped.

- Pages: the front page with a heat map and the path coverage; the register as a tree; one page per risk with its path drawn (stories, roles and stakeholders, then weakness, vulnerability, fix and code); one register per stakeholder (assigned here, or arriving through its parts) with who it shares risks with; one page per framework; the risk graph; what the sgit network already holds.

- `data/grc-graph.json` is generated: every edge a verb with its inverse, joined to the same claim, source, fix and code nodes as the story graph and the code review graph. The build stops on any unknown reference or an ownerless risk.

- Every risk reaches code and a team member; 30 of 34 reach a vulnerability (the four that do not are the newsroom's own agent risks, which reach this repository's code instead) and a role inside an organisation; 26 of 34 reach a story (the reporting-obligation risks and the newsroom's own have none yet, board 093).

- Not built: acceptance (no holder has accepted anything; board 092), per-stakeholder ratings (one rating per risk), the network's material captured into a vault (board 095), a graph of ISO 27001, NIST CSF, DORA or SOC 2 anywhere in the network.

### Collaborators (branch conductor/collaborators, conductor@php.newsroom)

- `/collaborators/` from `data/collaborators.json`: what we ask of collaborators, this week's ask (ask 001, Friday 23 October 2026) with what is new, the readers to read it as, the steps and the questions, and the messages for the WhatsApp group and the email list, generated with full URLs.

- Two forms (`assets/collaborators.js`), join and feedback, encrypted in the browser to the private collaborators vault (58526ytp, key sha256:e3ff50abd96816ef) and posted to its write-only lane; tested end to end from Chromium and drained by `admin/build/collaborators_drain.py`. The vault key is sealed to the root; the lane's enum key and the key pair's passphrase are not yet (board).

- Not built: sending. The email list and the WhatsApp group are the editor's own; nothing on the site sends mail.

### Runs (branch conductor/collaborators, conductor@php.newsroom)

- `/team/runs/` from `data/schedules.json`: the three schedules the team runs (the source watch every 30 minutes, the fact-check desk every four hours, the synthetic readers hourly), each with how many runs fall in the quiet hours, computed from its schedule; and every recorded run, newest first, read from the release history, the source watch, the fact-check runs and the synthetic readers, with the article each run with changes should leave (matched by `run:` in an article's front matter).

- The quiet hours (22:00 to 07:00 London) and the article rule are proposed, not applied: no schedule has been changed.

### Not built

- A second fact-check desk on a different model; a review folder; a second model reading the vault; a fractal graph; a Stripe link; tests beyond the gate.

## The honest column

- **Not measured:** the editor's time and the inference cost behind each agent run.

- **Not yet run:** the verifier role, which re-reads every claim against its capture text.

- **Not reviewed:** the playbook and the blast-radius section are the site's own synthesis of agency advice and have not been reviewed by a security team.

- **Not live:** everything on the billing page under "designed".

- **No tests beyond the gate:** the build has no unit tests; the gate is the whole automated enforcement surface.

- **No review folder yet:** the estate's guidance asks for `review/` from the first commit; this repository starts it from its next change.


---
site v0.7.0 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/index.html
