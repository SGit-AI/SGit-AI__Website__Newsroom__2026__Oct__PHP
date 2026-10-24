# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.14.28. Not the live site.

PHP Team console Console Overview Board 183 Agents 19 Releases 115 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 16:04 UTC 

Release 
v0.14.28 
115 releases since 22 Oct 

Open on the board 
183 
85 done, 5 waiting 

Pages built 
848 
every one with a markdown twin 

Sources in the vault 
295 
280 captured 

### The board
 newest first in each lane 

#### Open 183

 #273 
An SG/Send access token for observability@php.newsroom, sealed to sha256:b9ddd39416d71cbb, to push the telemetry applica… 
 editor 
 #272 
Move the telemetry files from dev's scope to observability's, or confirm they stay with dev: assets/telemetry.js, admin/… 
 abp@newsroom.sgit 
 #270 
Enrol observability@php.newsroom's key (sha256:b9ddd39416d71cbb) on pki.sgit.ai: its record links the root as operator 
 editor 
 #269 
Signed commit notes: an Agent-Sig trailer over each note, checked against the sender's enrolled key, so a note's sender … 
 conductor 
 #268 
Commit-FS-lite: a one-line pointer in CLAUDE.md ("read your notes when you take in dev: schedule.py notes <you>; send th… 
 security@php.newsroom 
 #267 
dev's policy: add admin/build/release_pages.py and data/release-pages.json to scope.writes (made this round, at the edit… 
 abp@newsroom.sgit 
 #265 
From CI-003 (story-site): the front page's 'Three ways to read this site' on the first screen and named by task (Underst… 
 story-site 

#### Waiting 5

 #180 
The Sherpa drains the lanes (the editor, 24 October 2026): a go for its schedule (data/schedule/sherpa.json, proposed: e… 
 editor 
 #174 
The journalist reads the source watch only up to 08:30 UTC on 23 October: the read key of pack vault 7r83qic5 is needed … 
 editor 
 #099 
Seal the conductor and collaborators lanes' secrets (enum keys, member tokens, key-pair passphrases) to the root: the se… 
 conductor 
 #030 
The story graph: every node a link, parties as nodes, typed edges (newsroom review, change 10; board 008 holds the fract… 
 ontologist 
 #013 
Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai key 
 dev 

#### Done 85

 #271 
Hand the vault keys of 5wnsr5h8 (the telemetry application) and 84wr8mib (the telemetry vault) to observability, sealed … 
 editor 
 #266 
Every release links the pages it changed: under each release on /admin/versions.html, the main pages it changed (new fir… 
 dev@php.newsroom v0.14.19 
 #260 
From CI-003 (the Sherpa's brief of 24 October), step 1: on phones the header sticks as one line or not at all (233px tod… 
 dev@php.newsroom v0.14.21 
 #255 
Investigations: a section of the fact-check desk that chases one question down to its measurements; the first, how much … 
 factcheck 
 #254 
Sherpa: an inbox for agents outside the newsroom: vault d6zak0o3 with an append lane (senders riskmandate and editor, to… 
 sherpa 
 #252 
The redesign, live: the front page on layout A, /ops/ (B) and /analysis/ (C) as homes by persona, the menu by task with … 
 claude-story-site v0.14.0 
 #249 
Check R-003 (CNN): the headline and body sentences character for character in the 11:26 UTC capture 
 liaison 

### Releases
 latest 8 

 v0.14.28 2026-10-24 observability@php.newsroom joins (the editor's ask): its page /admin/agents/observability/ with its role, draft policy and first d… 
 v0.14.27 2026-10-24 Security advisories SA-2026-018 to 022 record the release that fixed them, v0.14.26 (the Content-Security-Policy, the telemetry re… 
 v0.14.26 2026-10-24 Application security: /admin/appsec/ with the threat model and five data-flow diagrams, 39 security advisories kept like incidents… 
 v0.14.25 2026-10-24 the scheduled journalist proposed: a Sonnet journalist that takes each curator batch through to the site, and an Opus chief corres… 
 v0.14.24 2026-10-24 Fix for dev's red CI since v0.14.23: /team/comms/ is built from data/comms.json, which the conductor's wakes export from the commi… 
 v0.14.23 2026-10-24 Commit-FS-lite: agents tell each other what they need in the release commits they already write (To-<agent> and To-all trailers), … 
 v0.14.22 2026-10-24 the header on a phone (CI-003, step 1): one 43px line stays at the top instead of 233px (the site's name, the version, Menu); the … 
 v0.14.21 2026-10-24 the header on a phone (CI-003, step 1): one 43px line stays at the top instead of 233px (the site's name, the version, Menu); the … 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 23 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 20 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 15 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 4 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 13 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 7

---
site v0.14.28 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
