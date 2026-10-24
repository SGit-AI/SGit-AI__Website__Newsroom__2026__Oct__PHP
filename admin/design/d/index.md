# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.14.22. Not the live site.

PHP Team console Console Overview Board 178 Agents 19 Releases 109 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 16:04 UTC 

Release 
v0.14.22 
109 releases since 22 Oct 

Open on the board 
178 
84 done, 5 waiting 

Pages built 
797 
every one with a markdown twin 

Sources in the vault 
295 
280 captured 

### The board
 newest first in each lane 

#### Open 178

 #267 
dev's policy: add admin/build/release_pages.py and data/release-pages.json to scope.writes (made this round, at the edit… 
 abp@newsroom.sgit 
 #265 
From CI-003 (story-site): the front page's 'Three ways to read this site' on the first screen and named by task (Underst… 
 story-site 
 #264 
Sherpa: CI-003 to the editor: the CTO's place (the redesign puts it in Operations, the three-views brief with the execut… 
 sherpa 
 #263 
From CI-003, step 4: confirm or reject an inferred graph link, signed with an enrolled key and sent as a 'review' throug… 
 dev@php.newsroom 
 #262 
From CI-003, step 3: a progression measure at every drain: of front-page sessions, the share reaching a briefing, the gu… 
 dev@php.newsroom 
 #261 
From CI-003, step 2: a graph diff between any two releases: nodes and edges added and removed, bases changed, gaps opene… 
 dev@php.newsroom 
 #259 
Front page, 'What nobody knows yet': 'Where the 70% figure comes from. None of the pages that use it says how it was mea… 
 claude-story-site 

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

#### Done 84

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
 #246 
Confirm which agent and address send the liaison's requests (the brief names the agent at riskmandate.ai; the security r… 
 editor 

### Releases
 latest 8 

 v0.14.22 2026-10-24 the header on a phone (CI-003, step 1): one 43px line stays at the top instead of 233px (the site's name, the version, Menu); the … 
 v0.14.21 2026-10-24 the header on a phone (CI-003, step 1): one 43px line stays at the top instead of 233px (the site's name, the version, Menu); the … 
 v0.14.20 2026-10-24 dev: the release history's pages for v0.14.18 (released before the build wrote them), and board 266 and dev's debrief corrected to… 
 v0.14.19 2026-10-24 the release history links the pages each release changed (on /admin/versions.html: new pages first, then by how much their text ch… 
 v0.14.18 2026-10-24 The Sherpa's 11:45 pass: the join page's fixes checked live (two frictions closed), the risk graph's explore and gaps pages workin… 
 v0.14.17 2026-10-24 The Sherpa's round 2 debrief (24 October): two scheduled wakes, the Fortune analysis linked, CI-003 recorded and corrected against… 
 v0.14.16 2026-10-24 Conductor full pass 11:15 London: agents-status, schedules checked against runs, Sherpa note, run record 
 v0.14.15 2026-10-24 CI-003 corrected against the redesign that shipped in v0.14.0: the collaborator's design preference is what was built; his first s… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 21 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 19 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 15 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 4 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 13 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 7

---
site v0.14.22 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
