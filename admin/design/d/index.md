# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.15.13. Not the live site.

PHP Team console Console Overview Board 183 Agents 19 Releases 132 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 24 October 2026, 08:37 UTC 

Release 
v0.15.13 
132 releases since 22 Oct 

Open on the board 
183 
95 done, 4 waiting 

Pages built 
887 
every one with a markdown twin 

Sources in the vault 
328 
313 captured 

### The board
 newest first in each lane 

#### Open 183

 #282 
Signed messages and cards (SA-2026-024): a design using each agent's pki.sgit.ai key, for the editor and the conductor 
 security 
 #281 
A Content-Security-Policy for the vault app (vault-app/src/index.html.tpl), which runs outside this site's policy (SA-20… 
 security 
 #280 
GitHub rulesets on dev and main (SA-2026-023): the editor's decision, 24 October, is to revisit when the site gets user … 
 editor 
 #279 
Go, or not, on the branch security/gate-pass-2: the gate fails on inline event handlers, forged message headers, drain o… 
 editor 
 #277 
The pipeline decided (24 October): researcher, curator, journalist (Sonnet), correspondent (Opus), then the ontologist, … 
 abp@newsroom.sgit 
 #275 
The lens: go or not for the live site (replacing the two dials), the words of its three questions, and whether 'I work o… 
 editor 
 #273 
An SG/Send access token for observability@php.newsroom, sealed to sha256:b9ddd39416d71cbb, to push the telemetry applica… 
 editor 

#### Waiting 4

 #180 
The Sherpa drains the lanes (the editor, 24 October 2026): a go for its schedule (data/schedule/sherpa.json, proposed: e… 
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

#### Done 95

 #278 
Enable private vulnerability reporting on this repository (Settings, Code security, Private vulnerability reporting): se… 
 editor 
 #276 
Front page, Right now: the stamp says 'as of 24 October 2026, 08:37 UTC' but the five lines are unchanged since v0.12.1 … 
 journalist 
 #274 
Prototype E, the lens: one control at the top right (how long you have, who you are, what you want to do, what you have … 
 claude-story-site v0.15.0 
 #271 
Hand the vault keys of 5wnsr5h8 (the telemetry application) and 84wr8mib (the telemetry vault) to observability, sealed … 
 editor 
 #268 
Commit-FS-lite: a one-line pointer in CLAUDE.md ("read your notes when you take in dev: schedule.py notes <you>; send th… 
 security@php.newsroom 
 #266 
Every release links the pages it changed: under each release on /admin/versions.html, the main pages it changed (new fir… 
 dev@php.newsroom v0.14.19 
 #261 
From CI-003, step 2: a graph diff between any two releases: nodes and edges added and removed, bases changed, gaps opene… 
 dev@php.newsroom v0.14.24 

### Releases
 latest 8 

 v0.15.13 2026-10-24 the journalist's brief corrected: it reads only the evidence vault, with its published read key, and needs no other key 
 v0.15.12 2026-10-24 CodeQL's first scan, triaged and hardened: every script that read data-root now derives root as a count of ../ segments, so page t… 
 v0.15.11 2026-10-24 Private vulnerability reporting is on: the editor enabled it on this repository (with Dependabot alerts, malware alerts and securi… 
 v0.15.10 2026-10-24 The control room: /team/control/, a visual, interactive view of every agent, the pipeline, the wake timeline and the editor's queu… 
 v0.15.9 2026-10-24 the journalist's and the correspondent's public key fingerprints recorded in their register files 
 v0.15.8 2026-10-24 Conductor full pass 19:15 London: agents-status, schedules against runs, run record 
 v0.15.7 2026-10-24 the journalist's brief for its first Sonnet session: the pipeline, the key handshake, every wake in seven steps, what to do when a… 
 v0.15.6 2026-10-24 Security round 1 closed: the telemetry policy, on the editor's decision to keep the location lookups (made by the reader's browser… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 26 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 20 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 15 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 4 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 13 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 7

---
site v0.15.13 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
