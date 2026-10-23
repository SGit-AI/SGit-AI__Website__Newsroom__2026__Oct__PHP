# What's new: every change, release by release

> About this site: how the site works, kept by the agents that run it.

What changed on this site in each release: new facts, facts whose status changed, the briefings that moved for each reader and the sections that were rewritten.

The story · what's new

# What's new

Every release of this site, newest first, with what changed in it for readers: facts added, facts whose status changed, the briefings that moved and the sections that were rewritten. Releases you have not seen since your last visit are marked. To follow along, subscribe to [the feed](../feed.xml).

New evidence (for example the first confirmed compromise of a named organisation) reaches this page only once it has been captured into the evidence vault and turned into a fact with sources. Until then it is not on this site, however widely it is reported.

## v0.9.2 · 23 October 2026new since your last visit

the vault key is the whole boundary: whoever holds a vault's key can drain its lane (the enum key and the key pair's passphrase derived from the vault key, the key pair inside the vault), and the keys each agent holds listed on /team/vaults/; the editor's first key enrolled; his feedback on /join/ answered: where this device's key stands, one wording for Feedback, up to three screenshots

No reader-facing section changed in this release.

## v0.9.1 · 23 October 2026new since your last visit

vaults (/team/vaults/): every vault each agent made, listed by agent and by ID only, with whether its key is sealed to the editor; and guidance every agent reads (AGENTS.md section 6, CLAUDE.md): add a vault's ID when you make it, seal its key to the root with pki-agent, and when asked for a key send the sealed link and its QR code, never the key

No reader-facing section changed in this release.

## v0.9.0 · 23 October 2026new since your last visit

The Sherpa joins (/sherpa/): the agent that walks with the reader; readers' feedback recorded and answered point by point (UF-001 from a power user, UF-002 from an agent testing the invitation link), with both interface bugs reproduced; ideas from collaborators set against what the site has today (CI-001); the friction log of what gets in readers' way, with who can fix each; and the Sherpa on the team

No reader-facing section changed in this release.

## v0.8.4 · 23 October 2026new since your last visit

who reads this site, by group: every session a reader, the editor, a power user or team member, synthetic (agents and tests) or a crawler, declared by the browser from now on (automation by class, the role of a /join/ key or of this browser's setting) and inferred before; the groups, an hourly chart and a world map of readers on /admin/telemetry/; and a public stats vault (0cfkdcvh, read key published) with its own app, updated at every drain by admin/build/telemetry_flow.sh

No reader-facing section changed in this release.

## v0.8.3 · 23 October 2026new since your last visit

your stack linked from the front page (a Check your stack button and a Does it reach you? tile, the tiles now two rows of four) and from step 0 of If you run PHP; the telemetry lane drained on the morning of 23 October: 483 events overnight, 758 in all

No reader-facing section changed in this release.

## v0.8.2 · 23 October 2026new since your last visit

status (/team/status/): where every agent is on the morning of 23 October, what each last did and waits for and from whom, the eleven branches waiting for dev, what ran on a schedule overnight, how fresh the site's data is against its vaults; and the brief for day two, situation awareness

### Sections that changed
- [If you run PHP](../versions/page-playbook/index.html#v3) v3
- [Front page: at a glance](../versions/front-glance/index.html#v2) v2

## v0.8.1 · 23 October 2026new since your last visit

your stack, the blast radius (/stack/): describe what you run, the internet, the edge, the applications, the platforms and PHP runtimes, data, secrets and services, and see each runtime against both CVEs (versions, backports in the inventory, SAPI, exposure, settings, edge rules), the blast radius as a graph, what to do first and what on the site is about your stack, kept in your browser and your vault; and the warning and info colours restored on every page (their tokens were mapped to themselves since v0.2.4)

No reader-facing section changed in this release.

## v0.8.0 · 22 October 2026new since your last visit

feedback from any page, signed: a Feedback button beside Ask on every page (what is wrong, unclear, missing or good, with a screenshot), signed with a key made on the reader's device; /join/ makes the key from an invitation in one tap and /join/invite/ makes invitations in the browser, as a QR code and a share button, signed by the editor's key; keys are enrolled automatically when both signatures check; and the brief for the organisation as a digital twin

No reader-facing section changed in this release.

## v0.7.0 · 22 October 2026new since your last visit

power users, start here (/collaborators/): a generic onboarding for the people the editor nudges in his WhatsApp group and by email, the latest ask with its messages, and join and feedback forms encrypted to a private vault; runs (/team/runs/): every schedule the agents run, the quiet hours, and every recorded run with the article it should leave

No reader-facing section changed in this release.

## v0.6.0 · 22 October 2026new since your last visit

GRC: a new section, /grc/, with fractal risk registers for php2shell (34 risks assigned to 53 stakeholders, each joined to its weakness, CVE, fix, code, stories and roles, mapped to 95 controls in 20 frameworks including GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO 27001 and NIST), and the data protection officer added to the readers with a briefing on exposure, the GDPR 72-hour clock and what to document

No reader-facing section changed in this release.

## v0.5.10 · 22 October 2026new since your last visit

the telemetry vault-in-vault turned around: the application moves to a versioned vault of its own (5wnsr5h8, v0.1.1, eight pages), the telemetry vault imports it and drains its own lane from the browser (40 events drained that way, 275 from 176 sessions now), and the dashboard vault i4diy82d is superseded

No reader-facing section changed in this release.

## v0.5.9 · 22 October 2026new since your last visit

no named organisation has said it was compromised through php2shell: claim no-confirmed-compromise reworded with its time (20:50 UTC, 22 October) and moved from confirmed to reported, the plain-English lines that said nobody had confirmed a break-in corrected, and a page of its own (/compromise/) mapping the evidence behind the statement: what was searched, 33 statements by kind with their sources or source-watch snapshots, the layers from attempts to a named compromise, a timeline, and what would change it

### Briefings that changed
JJordanBoard member or executive · v7SSamSecurity lead · v6DDrewPHP or platform engineer · v7RRowanJournalist · v6AAshSecurity researcher · v6BBlakeAnalyst or advisor · v7RRobinCISO · v7AAveryCTO · v6QQuinnCFO · v7JJamieHead of AppSec · v6LLeeDeveloper · v5RRileyMedia and communications team · v6AAlexCurious reader · v5CCaseyWebsite owner · v4TTaylorProject or programme manager · v5MMorganData protection officer · new
## v0.5.8 · 22 October 2026new since your last visit

factcheck run 2: the PHP security team answered the 'incomplete fix' report publicly at 09:11 UTC on 22 October (unrelated crash bug, nothing to do with the RCE), so the front page's 'not answered publicly yet' is out of date; contradiction K-011 and five pieces of outside evidence; KEV still lists neither CVE; no claim changed and no run-1 ticket can close yet; the desk now publishes to dev on the editor's instruction

### Facts whose status changed
- [As of 20:50 UTC on 22 October, no named organisation has said it was compromised through p](../facts/no-confirmed-compromise/index.html): confirmed → reported

### Briefings that changed
JJordanBoard member or executive · v6RRobinCISO · v6QQuinnCFO · v6RRileyMedia and communications team · v5AAlexCurious reader · v4TTaylorProject or programme manager · v4
### Sections that changed
- [Every claim](../versions/page-claims/index.html#v6) v6
- [Impact: offline vs compromised](../versions/page-impact/index.html#v5) v5
- [In context: 2008 to 2026](../versions/page-context/index.html#v3) v3
- [The specialist summary](../versions/page-summary/index.html#v2) v2
- [Front page: right now](../versions/front-now/index.html#v2) v2
- [Front page: the core facts](../versions/front-facts/index.html#v2) v2

## v0.5.7 · 22 October 2026new since your last visit

the telemetry dashboard: a new private vault (i4diy82d) holding a vault app over the telemetry vault, which is linked inside it read-only (vault-in-vault), so the app always draws the latest drain; listed on /vaults/

No reader-facing section changed in this release.

## v0.5.6 · 22 October 2026new since your last visit

who reads this site: the telemetry lane drained again, 235 anonymous events from 161 sessions on 22 October; the subscriptions lane drained, nothing waiting

No reader-facing section changed in this release.

## v0.5.5 · 22 October 2026new since your last visit

two more branches carried in: security@php.newsroom's first pass (the security requirements, security_check.py in the gate and in release.sh, hardened build, workflows and drains, the rules of engagement for keys, the root pinned in CLAUDE.md; /admin/keys/ waits for data/keys.json) and the fact-check desk's run 1 (all 70 claims graded against the vault, 10 contradictions, /factcheck/)

No reader-facing section changed in this release.

## v0.5.4 · 22 October 2026new since your last visit

Ask, on every page: a pane on the right where you talk to the site with your own OpenRouter key; the model calls the site's read-only tools itself (search, items, pages, what is new to you, your notes, the situation), every call shown, every fact cited to an item; it can only propose marking items read or adding a note, and does nothing without your Allow; the tools are also published as window.__tools for any agent in your browser; your key, your reading record, notes, feeds and chats are kept in your vault, the same one the phone app opens

No reader-facing section changed in this release.

## v0.5.3 · 22 October 2026new since your last visit

guidance for every agent, AGENTS.md and /admin/agents/: push to your own branch after every step that builds and take in dev often, dev@php.newsroom carries branches into dev and releases; quality from coding.sgit.ai, non-functional requirements from nfrs.sgit.ai, and the security requirements (no secret in any repository, secrets sealed to pki.sgit.ai keys, readers' data in their browser or their own vault, untrusted input shown as text, a model given data not instructions)

No reader-facing section changed in this release.

## v0.5.2 · 22 October 2026new since your last visit

two branches carried into dev: researcher@ and cyber@php.newsroom join with the cyber desk's first piece, 'Patch at the speed of Metasploit' (board items renumbered 076 to 079 after the conductor's); and the fact-check desk as pushed, its model, contradiction ledger and /factcheck/, run 1 in progress

No reader-facing section changed in this release.

## v0.5.1 · 22 October 2026new since your last visit

the team: every member, human and agent, with a page (role, what they own, tasks, what they shipped), Vicky joins as project manager and the conductor as conductor and comms; the team coordinates through three private vaults, the conductor vault with an append lane, the issues vault (Issues-FS-lite, the board moved into it) and the mail vault (Email-FS-lite); /team/channels/ and the run

No reader-facing section changed in this release.

## v0.5.0 · 22 October 2026new since your last visit

Now, the phone app (/now/): what you need to know for one, five, ten or thirty minutes against what you read before; a deterministic mode from the data and an agentic one where Sonnet writes your briefing and answers in a chat and Gemini draws an infographic, with your OpenRouter key kept in your own vault; the newsroom's vault library vendored for it

No reader-facing section changed in this release.

## v0.4.7 · 22 October 2026new since your last visit

the editor's critical brief on scheduled capture: the sources that move are checked on a schedule, captured raw, turned into timestamped JSON and analysed on every change; contradictions between reports are recorded as first-class records, seeded with seven from the coverage review; meaning through connectivity, with every fact and stat on a spectrum of evidence; board items 057 to 063

### Briefings that changed
JJordanBoard member or executive · v5SSamSecurity lead · v5DDrewPHP or platform engineer · v6RRowanJournalist · v5AAshSecurity researcher · v5BBlakeAnalyst or advisor · v6RRobinCISO · v5AAveryCTO · v5QQuinnCFO · v5JJamieHead of AppSec · v5LLeeDeveloper · v4RRileyMedia and communications team · v4AAlexCurious reader · v3CCaseyWebsite owner · v3TTaylorProject or programme manager · v3
### Sections that changed
- [Who found it](../versions/page-discovery/index.html#v5) v5
- [How disclosure broke](../versions/page-leak/index.html#v5) v5
- [Every claim](../versions/page-claims/index.html#v5) v5

## v0.4.6 · 22 October 2026new since your last visit

synthetic readers: synthetic@php.newsroom runs six test readers (board member, CTO, project manager, security lead, developer, designer) through the live site in a real browser, each with its own device, path and private vault holding every request, page, screenshot and review; /admin/synthetic/ shows the first run's verdicts, scores and requested changes; hourly and after each deploy via .github/workflows/synthetic.yml once its secrets are set

No reader-facing section changed in this release.

## v0.4.5 · 22 October 2026new since your last visit

the coverage vault: 24 pages from other outlets captured with screenshots, page text and hashes into a new private vault (dcsmxese), listed on /vaults/ without its key, and the review of how they present the story and what this site should learn, in admin/content/reviews/

No reader-facing section changed in this release.

## v0.4.4 · 22 October 2026new since your last visit

subscriptions: /subscribe/ takes an address, what to follow and how often, encrypts it in the reader's browser to the new private subscriptions vault (wgeiqabu) and posts it to that vault's write-only lane; the agent at agent@diniscruz.ai confirms each address before sending anything; the vault is listed on /vaults/, its drain script is admin/build/subscriptions_drain.py, and its keys and the telemetry vault's are sealed to the editor's key

No reader-facing section changed in this release.

## v0.4.3 · 22 October 2026new since your last visit

The second stories: the NCSC-NL inventory read hour by hour from its public history (38 versions, 61 fixed, 216 vulnerable, 440 under investigation at 15:28 UTC on 22 October; 185 of the vulnerable are applications that inherit PHP's flaw; firewalls and gateways among the affected), /signals/ with the ladder from exposed to exploited, four signal families and the time of each barrier, and the story 'Exposed is not exploited' by the journalist and the historian; a correction: the inventory had 675 rows at the captured commit, not 674

No reader-facing section changed in this release.

## v0.4.2 · 22 October 2026new since your last visit

the delta since your last visit: every item on the site (facts, sections, briefings, stories, questions, sources, dated events) is marked new, changed or read in your browser; mark a page or everything read and the read items fade or hide, so the next visit shows only what changed; decisions and notes per item; your desk at /you/; five RSS feeds (everything, for you, research, stories, about the site) at /feeds/; a feed viewer at /reader/ for this site's feeds, the CVE records, NVD, OSV, CISA KEV, GitHub, Hacker News and Mastodon, and feeds you add

No reader-facing section changed in this release.

## v0.4.1 · 22 October 2026new since your last visit

Research and Stories: the menu in three zones (for you, research, stories) with an origin strip on every page saying whether it is research, external material, a story (house, guest, interview) or about the site; Stories as its own section; /patching/, which versions of PHP get a fix and from whom, every downstream row checked against the NCSC-NL inventory; the story 'Why can't every version of PHP just be patched?'; /status.json for other sites, with its admin page; the editor's brief published; four stray screenshots committed in v0.2.10 removed

No reader-facing section changed in this release.

## v0.4.0 · 22 October 2026new since your last visit

the design branch merged into dev: the site is PHP October 2026 with a jargon-free front page, fifteen readers with plain answers and reading paths, a glossary on every page, every section and fact versioned with history and diffs, what's new with a feed, the editor's interview, and sitemap.xml and robots.txt for search engines; everything dev shipped since v0.2.2 is kept

No reader-facing section changed in this release.

## v0.3.2 · 22 October 2026new since your last visit

every section versioned and every fact given a timeline: each briefing, front-page section and story page records the release that wrote it, with its history and a diff of every change; a page per fact, from publication to this site; what's new, release by release, with a feed; the fact pipeline; the editor interviewed in his own words; a sitemap, robots.txt and structured data for search engines

### Briefings that changed
DDrewPHP or platform engineer · v5BBlakeAnalyst or advisor · v5RRobinCISO · v4AAveryCTO · v4QQuinnCFO · v4JJamieHead of AppSec · v4
### Sections that changed
- [Exploitation signals](../versions/page-exploitation/index.html#v5) v5
- [Impact: offline vs compromised](../versions/page-impact/index.html#v4) v4
- [Front page: right now](../versions/front-now/index.html#v1) (new)
- [Front page: at a glance](../versions/front-glance/index.html#v1) (new)
- [Front page: the core facts](../versions/front-facts/index.html#v1) (new)
- [Front page: what nobody knows yet](../versions/front-unknown/index.html#v1) (new)
- [Front page: latest](../versions/front-latest/index.html#v1) (new)
- [Interview: the editor](../versions/page-interview/index.html#v1) (new)

## v0.3.1 · 22 October 2026new since your last visit

the site is renamed PHP October 2026, PHP news for the month rather than one nickname, and its front page is now jargon-free and about the current situation: right now, at a glance, the core facts each with its status and evidence, what nobody knows yet and the latest; the technical front page moved to the specialist summary

### Briefings that changed
JJordanBoard member or executive · v4SSamSecurity lead · v4DDrewPHP or platform engineer · v4RRowanJournalist · v4AAshSecurity researcher · v4BBlakeAnalyst or advisor · v4RRobinCISO · v3AAveryCTO · v3QQuinnCFO · v3JJamieHead of AppSec · v3LLeeDeveloper · v3RRileyMedia and communications team · v3AAlexCurious reader · v2CCaseyWebsite owner · v2TTaylorProject or programme manager · v2
### Sections that changed
- [Timeline](../versions/page-timeline/index.html#v4) v4
- [Who found it](../versions/page-discovery/index.html#v4) v4
- [How disclosure broke](../versions/page-leak/index.html#v4) v4
- [Exploitation signals](../versions/page-exploitation/index.html#v4) v4
- [Every claim](../versions/page-claims/index.html#v4) v4
- [The numbers](../versions/page-numbers/index.html#v4) v4
- [The code](../versions/page-code/index.html#v3) v3
- [Impact: offline vs compromised](../versions/page-impact/index.html#v3) v3
- [Detection and defence](../versions/page-defence/index.html#v3) v3
- [Who says what](../versions/page-actors/index.html#v3) v3
- [Explained from the start](../versions/page-explained/index.html#v2) v2
- [The specialist summary](../versions/page-summary/index.html#v1) (new)

## v0.3.0 · 22 October 2026new since your last visit

the first reader-first pass: fifteen named readers mapped by job and technical depth, a briefing for each opening with a thirty-second plain answer and a reading path, three new briefings (curious reader, website owner, project manager), a plain-English explainer, a glossary of 40 terms linked and hover-defined on first use on every page, every CVE ID linked, a plain-English line on every technical page, a reader bar that keeps your place, and a front page that leads with where things stand and who you are

### Briefings that changed
JJordanBoard member or executive · v3SSamSecurity lead · v3DDrewPHP or platform engineer · v3RRowanJournalist · v3AAshSecurity researcher · v3BBlakeAnalyst or advisor · v3RRobinCISO · v2AAveryCTO · v2QQuinnCFO · v2JJamieHead of AppSec · v2LLeeDeveloper · v2RRileyMedia and communications team · v2AAlexCurious reader · newCCaseyWebsite owner · newTTaylorProject or programme manager · new
### Sections that changed
- [The two flaws](../versions/page-flaws/index.html#v2) v2
- [Timeline](../versions/page-timeline/index.html#v3) v3
- [Who found it](../versions/page-discovery/index.html#v3) v3
- [How disclosure broke](../versions/page-leak/index.html#v3) v3
- [Exploitation signals](../versions/page-exploitation/index.html#v3) v3
- [If you run PHP](../versions/page-playbook/index.html#v2) v2
- [Every claim](../versions/page-claims/index.html#v3) v3
- [The numbers](../versions/page-numbers/index.html#v3) v3
- [The agencies](../versions/page-agencies/index.html#v2) v2
- [Affected systems](../versions/page-affected/index.html#v2) v2
- [The method](../versions/page-method/index.html#v3) v3
- [The code](../versions/page-code/index.html#v2) v2
- [Impact: offline vs compromised](../versions/page-impact/index.html#v2) v2
- [Detection and defence](../versions/page-defence/index.html#v2) v2
- [In context: 2008 to 2026](../versions/page-context/index.html#v2) v2
- [Who says what](../versions/page-actors/index.html#v2) v2
- [Explained from the start](../versions/page-explained/index.html#v1) (new)
- [Glossary: every term, in plain English](../versions/page-glossary/index.html#v1) (new)

## v0.2.15 · 22 October 2026new since your last visit

who reads this site: the telemetry lane drained again, 120 anonymous events from 74 sessions on 22 October, counts by country, region, referrer, page and screen on the telemetry page

No reader-facing section changed in this release.

## v0.2.14 · 22 October 2026new since your last visit

the source watch's page opens with a screenshot of the vault in the official UI, read-only with the published key, that opens the real one in a new tab; board item 038 records what the first open costs in the browser (2,678 objects decrypted before the tree shows)

No reader-facing section changed in this release.

## v0.2.13 · 22 October 2026new since your last visit

the vaults: a Vaults section listing every vault behind the site (the evidence vault and the source watch with their read keys, the private telemetry vault with its write-only lane); the source watch (oq9gflln) published the way sgit.ai publishes vaults, with its key, a link that opens it in a new tab, the official UI embedded and its features (raw and analysis trees, country to page taxonomy, access classes, licence tiers, graphs at four altitudes, runs, tips, tools) from data/source-watch.json; the evidence vault page embeds its app too

No reader-facing section changed in this release.

## v0.2.12 · 22 October 2026new since your last visit

deploys from several agents: the Pages workflow queues deploys instead of cancelling the one in flight, and release.sh takes in what other agents released before it bumps and again if its push loses a race; /status/ shows each newsroom site's deploy runs from GitHub's public API with no credential, beside the version each serves, and every page notes when a newer release is live

No reader-facing section changed in this release.

## v0.2.11 · 22 October 2026new since your last visit

the release check reads the live version correctly: v0.2.9's pattern matched the v in class="ver" and read a blank version, so it reported every release unverified; now tested against the live site for older, equal and newer versions

No reader-facing section changed in this release.

## v0.2.10 · 22 October 2026new since your last visit

pricing by content type and freshness: every content page metered (only the meter's own pages are not), price = max(1p, round(base x freshness)) with tiers picked in the reader's browser, the formula and rules of engagement on the billing page; second readings: Perplexity's notes published in full and credited, compared with the vault point by point; the newsroom's review of the site published as received, with a triage and fourteen board items; briefing titles and table word-wrapping fixed

No reader-facing section changed in this release.

## v0.2.9 · 22 October 2026new since your last visit

the release check now accepts this version or later, because several agents release to dev and one can land on top of another inside the polling window (v0.2.8 landed on v0.2.7 and the old exact check called a live release unverified)

No reader-facing section changed in this release.

## v0.2.8 · 22 October 2026new since your last visit

the articles layer and the evidence, derived, authored split: a journalist's state-of-affairs report and a historian's perspective, both written against v0.2.5 (the librarian's questions shipped alongside as v0.2.6, the dev agent's key as v0.2.7); /layers/ classifying every data file, checked by the gate; the menu split into story, articles, analysis and evidence; a front page and navigation review; the front page's 'six briefings' corrected to the computed twelve

No reader-facing section changed in this release.

## v0.2.7 · 22 October 2026new since your last visit

dev@php.newsroom's public key from pki.sgit.ai on the roles page (record sha256:8025e2a4470e73f0, key link and QR), the brief for handing the editor the telemetry vault key sealed to his key, and board item 013

No reader-facing section changed in this release.

## v0.2.6 · 22 October 2026new since your last visit

the librarian joins (librarian@php.newsroom): /questions/, the questions readers ask with a short answer to paste back, the sourced answer and the pages that carry it, starting from a reader's 'can anything be done, or do we wait for updates?'; a catalogue of every page; articles readers saw that the vault has not captured, listed as seen, not cited

No reader-facing section changed in this release.

## v0.2.5 · 22 October 2026new since your last visit

the review layer: the php2shell fix mapped to the php-src code as layered graphs (the flaws, what the fix does, the files and functions it changed, derived from the diff), a static map at /review/ and a no-library navigator at /review/ui/, after the secrets.sgit.ai review pages

No reader-facing section changed in this release.

## v0.2.4 · 22 October 2026new since your last visit

five themes (Newsprint, Night, Paper, Blueprint, Ember) with a picker in the bar, vendored from newsroom.sgit.ai; all colour moved to theme tokens; the reading-meter ratings card dropped for the quiet balance

No reader-facing section changed in this release.

## v0.2.3 · 22 October 2026new since your last visit

the admin section (board, roles, briefs, the evidence vault opened with its public read key, who reads this site), anonymous telemetry over an append lane into a separate vault with its drain script and first report, and the page meter in quiet mode

No reader-facing section changed in this release.

## v0.2.2 · 22 October 2026new since your last visit

the build, gate and release scripts are now committed: the repository's Python .gitignore template had ignored admin/build/, which is why the first Pages run could not find the gate

No reader-facing section changed in this release.

## v0.2.1 · 22 October 2026new since your last visit

a Pages deploy workflow that runs the gate on every push to dev, and breadcrumbs up to October 2026, the year and the newsroom

No reader-facing section changed in this release.

## v0.2.0 · 22 October 2026new since your last visit

the code read from php-src, php2shell in context against ten earlier flaws, an impact ledger of offline versus compromised, detection and defence from six WAF vendors and three rule sets, six more briefings, a page per source and per party with its own graph, 86 new sources

### Facts whose status changed
- [Amazon and Cloudflare saw sites being probed for the flaw](../facts/probing/index.html): reported → confirmed

### 21 new facts
- [Exploit attempts across Cloudflare's network: thousands in the ten hours before announceme](../facts/cf-millions/index.html) reported
- [No traffic matching the php2shell exploit patterns was seen during Imperva's pre-disclosur](../facts/imperva-none/index.html) reported
- [No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no pub](../facts/huntress-none/index.html) reported
- [watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild](../facts/watchtowr-itw/index.html) unverified
- [As of 20:50 UTC on 22 October, no named organisation has said it was compromised through p](../facts/no-confirmed-compromise/index.html) confirmed
- [None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechani](../facts/pocs-wrong/index.html) reported
- [Triggering the bug is much easier than turning it into code execution; the CVSS vector say](../facts/ac-high/index.html) confirmed
- [The fix was authored on 18 October at 15:26 UTC and entered the public branches at 14:06 U](../facts/fix-authored/index.html) confirmed
- [Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on o](../facts/fix-engine/index.html) confirmed
- [Patching the demonstrated paths does not make the bailout mechanism safe; more paths shoul](../facts/more-paths/index.html) reported
- [Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akam](../facts/waf-nine-hours/index.html) confirmed
- [The Dutch NCSC took its own site offline as a precaution, as did DigiD, MijnOverheid and O](../facts/nl-offline/index.html) confirmed
- [Finland's state IT provider Valtori restricted public traffic to government web services f](../facts/fi-offline/index.html) reported
- [The Wikimedia Foundation took down a number of systems 'as a precautionary measure until t](../facts/wikimedia-precaution/index.html) reported
- [Weird Gloop turned off its wiki web servers for 13 hours and still served about 94% of pag](../facts/weirdgloop-13h/index.html) confirmed
- [Edinburgh council's site went offline late on 21 October; the council called it 'essential](../facts/edinburgh/index.html) reported
- [Oxford City Council: 'a precaution because of a worldwide issue with the underlying techno](../facts/oxford/index.html) reported
- [Edinburgh and Oxford councils, the Met Police and the Office for Budget Responsibility wer](../facts/uk-list/index.html) reported
- [Quarkslab's published audit summary lists 27 findings, two redacted because their fixes we](../facts/quarkslab-redacted/index.html) reported
- [Chainguard's team found the same bugs independently with an AI harness and a frontier mode](../facts/lorenc-ai-found/index.html) reported
- [The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure a](../facts/kev-precedent/index.html) confirmed

3 facts reworded or re-sourced: [scale-2.6m-hosts](../facts/scale-2.6m-hosts/index.html), [chainguard](../facts/chainguard/index.html), [amazon-honeypot](../facts/amazon-honeypot/index.html).

### Briefings that changed
JJordanBoard member or executive · v2SSamSecurity lead · v2DDrewPHP or platform engineer · v2RRowanJournalist · v2AAshSecurity researcher · v2BBlakeAnalyst or advisor · v2RRobinCISO · newAAveryCTO · newQQuinnCFO · newJJamieHead of AppSec · newLLeeDeveloper · newRRileyMedia and communications team · new
### Sections that changed
- [Timeline](../versions/page-timeline/index.html#v2) v2
- [Who found it](../versions/page-discovery/index.html#v2) v2
- [How disclosure broke](../versions/page-leak/index.html#v2) v2
- [Exploitation signals](../versions/page-exploitation/index.html#v2) v2
- [Every claim](../versions/page-claims/index.html#v2) v2
- [The numbers](../versions/page-numbers/index.html#v2) v2
- [The method](../versions/page-method/index.html#v2) v2
- [The code](../versions/page-code/index.html#v1) (new)
- [Impact: offline vs compromised](../versions/page-impact/index.html#v1) (new)
- [Detection and defence](../versions/page-defence/index.html#v1) (new)
- [In context: 2008 to 2026](../versions/page-context/index.html#v1) (new)
- [Who says what](../versions/page-actors/index.html#v1) (new)

## v0.1.0 · 22 October 2026new since your last visit

The site exists: a story front, the two flaws, the timeline, every claim with a status, the numbers that do not add up, the agencies compared, the affected versions and software, the exploitation signals, a playbook, six briefings, every source with its hashes, the graph, the method, the team, the billing model and this history.

### 49 new facts
- [Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fix](../facts/two-cves-9.2/index.html) confirmed
- [The flaws are CVSS 10.0](../facts/cvss-10/index.html) contradicted
- [Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any app](../facts/rce-modphp/index.html) confirmed
- [Remote code execution is confirmed on PHP-FPM](../facts/rce-fpm/index.html) disputed
- [The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the ](../facts/fix-bailout/index.html) confirmed
- [The 8.5.12 fix may be incomplete, or there is a third, different bug](../facts/fix-incomplete/index.html) unverified
- [All PHP versions from 5 onwards are affected by at least one of the flaws](../facts/versions-old/index.html) disputed
- [Updating is the only complete mitigation; the configuration measures reduce exposure to sp](../facts/only-update/index.html) confirmed
- [A web application firewall may provide some protection until systems are patched](../facts/waf/index.html) disputed
- [Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcu](../facts/wordpress-drupal/index.html) reported
- [Roughly 70% of the Internet is affected](../facts/scale-70pc-internet/index.html) unverified
- [PHP is used by almost 70% of websites](../facts/scale-70pc-websites/index.html) reported
- [Something like 30 million websites could be affected](../facts/scale-30m/index.html) reported
- [PHP is exposed on about 2.6 million internet-facing hosts, of which Censys counted 1.57 mi](../facts/scale-2.6m-hosts/index.html) reported
- [About 6,000 potentially affected resources in Latvia, a few hundred in the public sector](../facts/scale-latvia/index.html) reported
- [674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, ](../facts/scale-ncsc-nl/index.html) confirmed
- [The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet init](../facts/ai-found/index.html) reported
- [Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 1](../facts/who-first/index.html) confirmed
- [OpenAI independently reported the same root cause on 11 August, with further vectors on 18](../facts/openai-same-day/index.html) reported
- [Wiz Research independently discovered the first flaw on 19 August and reported on 24 Augus](../facts/wiz-independent/index.html) reported
- [The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-](../facts/four-reporters/index.html) confirmed
- [The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and t](../facts/quarkslab-2024/index.html) confirmed
- [Frontier AI found the flaw ahead of attackers, giving defenders time to prepare](../facts/ahead-of-attackers/index.html) disputed
- [The most severe flaws ever detected by AI](../facts/most-severe/index.html) reported
- [On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social me](../facts/leak-cve-ids/index.html) reported
- [The leak started with an anonymous Hacker News post citing a reliable source, which came d](../facts/leak-hn/index.html) reported
- [watchTowr confirmed in public that the bugs were real and posted both CVE numbers before t](../facts/leak-watchtowr/index.html) reported
- [Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of con](../facts/leak-video/index.html) reported
- [Mitigation advice given to a few critical-infrastructure providers from about 23:00 UTC on](../facts/leak-mitigations/index.html) reported
- [Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built i](../facts/chainguard/index.html) disputed
- [The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the](../facts/release-moved/index.html) confirmed
- [The flaws were disclosed on 22 October 2026](../facts/disclosure-22oct/index.html) contradicted
- [The fixes were released at 14:00 UTC on 21 October](../facts/release-time/index.html) disputed
- [The pre-announcement was published at 19:30 UTC on 20 October](../facts/preannounce-time/index.html) disputed
- [There is no evidence yet that hackers have exploited the flaw](../facts/no-exploitation/index.html) reported
- [CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities ](../facts/cisa-none/index.html) confirmed
- [Reports of active exploitation exist](../facts/nz-active/index.html) reported
- [An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; pro](../facts/amazon-honeypot/index.html) reported
- [Cloudflare observed attack traffic targeting its customers after the leak, with attackers ](../facts/cloudflare-traffic/index.html) reported
- [Amazon and Cloudflare saw sites being probed for the flaw](../facts/probing/index.html) reported
- and more on [every claim](../claims/index.html)

### Briefings that changed
JJordanBoard member or executive · newSSamSecurity lead · newDDrewPHP or platform engineer · newRRowanJournalist · newAAshSecurity researcher · newBBlakeAnalyst or advisor · new
### Sections that changed
- [The two flaws](../versions/page-flaws/index.html#v1) (new)
- [Timeline](../versions/page-timeline/index.html#v1) (new)
- [Who found it](../versions/page-discovery/index.html#v1) (new)
- [How disclosure broke](../versions/page-leak/index.html#v1) (new)
- [Exploitation signals](../versions/page-exploitation/index.html#v1) (new)
- [If you run PHP](../versions/page-playbook/index.html#v1) (new)
- [Every claim](../versions/page-claims/index.html#v1) (new)
- [The numbers](../versions/page-numbers/index.html#v1) (new)
- [The agencies](../versions/page-agencies/index.html#v1) (new)
- [Affected systems](../versions/page-affected/index.html#v1) (new)
- [The method](../versions/page-method/index.html#v1) (new)


---
site v0.9.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/whatsnew/index.html
