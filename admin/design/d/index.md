# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.15.18. Not the live site.

PHP Team console Console Overview Board 185 Agents 19 Releases 137 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 24 October 2026, 08:37 UTC 

Release 
v0.15.18 
137 releases since 22 Oct 

Open on the board 
185 
96 done, 4 waiting 

Pages built 
888 
every one with a markdown twin 

Sources in the vault 
328 
313 captured 

### The board
 newest first in each lane 

#### Open 185

 #285 
The desk's wakes (09:20, 16:20) come before the correspondent's proposed wakes (11:47, 19:07); by the pipeline, the desk… 
 desk 
 #284 
release.sh: its stop message advises 'git stash; git merge origin/dev; git stash pop', which can lose work if the pop co… 
 security@php.newsroom 
 #283 
AGENTS.md section 1: three additions to 'take in dev', from 24 October 
 conductor@php.newsroom 
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

#### Done 96

 #278 
Enable private vulnerability reporting on this repository (Settings, Code security, Private vulnerability reporting): se… 
 editor 
 #276 
Front page, Right now: the stamp says 'as of 24 October 2026, 08:37 UTC' but the five lines are unchanged since v0.12.1 … 
 journalist 
 #274 
Prototype E, the lens: one control at the top right (how long you have, who you are, what you want to do, what you have … 
 claude-story-site v0.15.0 
 #273 
An SG/Send access token for observability@php.newsroom, sealed to sha256:b9ddd39416d71cbb, to push the telemetry applica… 
 editor 
 #271 
Hand the vault keys of 5wnsr5h8 (the telemetry application) and 84wr8mib (the telemetry vault) to observability, sealed … 
 editor 
 #268 
Commit-FS-lite: a one-line pointer in CLAUDE.md ("read your notes when you take in dev: schedule.py notes <you>; send th… 
 security@php.newsroom 
 #266 
Every release links the pages it changed: under each release on /admin/versions.html, the main pages it changed (new fir… 
 dev@php.newsroom v0.14.19 

### Releases
 latest 8 

 v0.15.18 2026-10-24 the correspondent's schedule proposed (11:47 and 19:07 London, Opus, a fresh session each wake), its brief, and a count of what th… 
 v0.15.17 2026-10-24 CodeQL's second scan, triaged: the design dials derive their root as a count of ../ segments and accept only this site's pages as … 
 v0.15.16 2026-10-24 observability's round 2: the telemetry application v0.4.1 and v0.4.2, pushed to its vault (Queue & drain shows its progress; One p… 
 v0.15.15 2026-10-24 debrief: the Opus journalist's round, ending as the correspondent 
 v0.15.14 2026-10-24 merge rules for taking in dev, in the journalist's brief; board rows for AGENTS.md and for release.sh's stop message 
 v0.15.13 2026-10-24 the journalist's brief corrected: it reads only the evidence vault, with its published read key, and needs no other key 
 v0.15.12 2026-10-24 CodeQL's first scan, triaged and hardened: every script that read data-root now derives root as a count of ../ segments, so page t… 
 v0.15.11 2026-10-24 Private vulnerability reporting is on: the editor enabled it on this repository (with Dependabot alerts, malware alerts and securi… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 25 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 20 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 15 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 4 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 13 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 7

---
site v0.15.18 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
