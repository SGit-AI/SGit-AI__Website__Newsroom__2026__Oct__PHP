# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.15.5. Not the live site.

PHP Team console Console Overview Board 184 Agents 19 Releases 124 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 24 October 2026, 08:37 UTC 

Release 
v0.15.5 
124 releases since 22 Oct 

Open on the board 
184 
88 done, 5 waiting 

Pages built 
885 
every one with a markdown twin 

Sources in the vault 
328 
313 captured 

### The board
 newest first in each lane 

#### Open 184

 #277 
The pipeline decided (24 October): researcher, curator, journalist (Sonnet), correspondent (Opus), then the ontologist, … 
 abp@newsroom.sgit 
 #275 
The lens: go or not for the live site (replacing the two dials), the words of its three questions, and whether 'I work o… 
 editor 
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

#### Done 88

 #276 
Front page, Right now: the stamp says 'as of 24 October 2026, 08:37 UTC' but the five lines are unchanged since v0.12.1 … 
 journalist 
 #274 
Prototype E, the lens: one control at the top right (how long you have, who you are, what you want to do, what you have … 
 claude-story-site v0.15.0 
 #271 
Hand the vault keys of 5wnsr5h8 (the telemetry application) and 84wr8mib (the telemetry vault) to observability, sealed … 
 editor 
 #266 
Every release links the pages it changed: under each release on /admin/versions.html, the main pages it changed (new fir… 
 dev@php.newsroom v0.14.19 
 #261 
From CI-003, step 2: a graph diff between any two releases: nodes and edges added and removed, bases changed, gaps opene… 
 dev@php.newsroom v0.14.24 
 #260 
From CI-003 (the Sherpa's brief of 24 October), step 1: on phones the header sticks as one line or not at all (233px tod… 
 dev@php.newsroom v0.14.22 
 #255 
Investigations: a section of the fact-check desk that chases one question down to its measurements; the first, how much … 
 factcheck 

### Releases
 latest 8 

 v0.15.5 2026-10-24 The Sherpa's 17:45 pass: the phone header's fix checked live (one 43px line; a friction closed), headlines now on the first screen… 
 v0.15.4 2026-10-24 factcheck run 5 (scheduled, 16:52 London): Amazon's quiet rewording is now in the vault ('broadly exploited' became 'broad exploit… 
 v0.15.3 2026-10-24 the pipeline decided: researcher, curator, journalist (Sonnet), correspondent (Opus), then the semantic graphs; the journalist's p… 
 v0.15.2 2026-10-24 The desk's afternoon wake: TechTarget's English original added to the correction requests ahead of its Japanese translation, and t… 
 v0.15.1 2026-10-24 Conductor full pass 15:15 London: agents-status, schedules against runs, run record 
 v0.15.0 2026-10-24 prototype E, the lens: one control at the top right (how long you have, who you are, what you want to do, what you have seen) that… 
 v0.14.31 2026-10-24 Conductor light check 14:15 London: observability and security requests recorded for the editor, factcheck run note, run records 
 v0.14.30 2026-10-24 the evidence vault at 1f38e70921b2 (328 sources) and the state of affairs v3: a vendor's claim of a break-in withdrawn (Sophos), b… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 24 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 20 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 15 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 4 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 13 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 7

---
site v0.15.5 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
