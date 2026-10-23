# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.10.15. Not the live site.

PHP Team console Console Overview Board 115 Agents 16 Releases 66 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 13 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 01:20 UTC 

Release 
v0.10.15 
66 releases since 22 Oct 

Open on the board 
115 
54 done, 2 waiting 

Pages built 
627 
every one with a markdown twin 

Sources in the vault 
227 
212 captured 

### The board
 newest first in each lane 

#### Open 115

 #163 
Queue tasks from the page: a signed request from an enrolled key (the editor's) on /team/schedule/, drained into the sch… 
 conductor 
 #162 
The schedules of the curator and the researcher: how often, in which hours (the quiet hours are proposed as 22:00 to 07:… 
 editor 
 #161 
Run every scheduled wake through the schedule vault (researcher's T-001, the source watch pass), and say your real caden… 
 researcher@php.newsroom 
 #160 
Run every scheduled wake through the schedule vault: pull, schedule.py due curator, start/finish with the log, index, pu… 
 curator 
 #158 
Check the agent behaviour policies against what each agent actually did (its releases, its vaults and keys on /team/vaul… 
 security 
 #157 
One agent behaviour policy per agent that sets its scope: what it may change and release, which vaults and keys it may h… 
 abp 
 #155 
Explain on the flaws page why NVD's 9.8 (CVSS 3.1) and the CNA's 9.2 (CVSS 4.0) are different scales, not a disagreement 
 claude-story-site 

#### Waiting 2

 #099 
Seal the conductor and collaborators lanes' secrets (enum keys, member tokens, key-pair passphrases) to the root: the se… 
 conductor 
 #013 
Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai key 
 dev 

#### Done 54

 #171 
From CI-002: a debrief for the collaborator, before and after: each change as the old page against the new, side by side… 
 dev@php.newsroom v0.10.14 
 #170 
From CI-002, step 5: a gaps page computed at every build from written rules (control with no path to a test, code with n… 
 dev@php.newsroom v0.10.13 
 #169 
From CI-002, step 4: an impact view: pick a function or file, climb the graph to remediations, vulnerabilities, weakness… 
 dev@php.newsroom v0.10.13 
 #168 
From CI-002, step 3: the fix commit's tests as nodes in the graph, joined to the remediation and code they exercise 
 dev@php.newsroom v0.10.13 
 #167 
From CI-002, step 2: a basis on every graph edge (source, code, inferred, confirmed, with its support), checked in build… 
 dev@php.newsroom v0.10.13 
 #166 
From CI-002 (the Sherpa's brief of 23 October, the risk graph as a tool), step 1: a focus view of the risk graph: open a… 
 dev@php.newsroom v0.10.13 
 #165 
The telemetry app v0.4.0 (UX vault 5wnsr5h8): new events on focus (at most once a minute); every mark a filter, Kibana-s… 
 dev@php.newsroom v0.10.10 

### Releases
 latest 8 

 v0.10.15 2026-10-23 pack mode, measured on the source watch (/admin/pack-mode/): the same vault as a normal and a pack vault, a fresh clone in 95 s ag… 
 v0.10.14 2026-10-23 the risk graph, before and after: a debrief for the collaborator whose ideas became v0.10.13, every change shown as the old page a… 
 v0.10.13 2026-10-23 the risk graph as a tool (CI-002, steps 1 to 5): every edge says how it is known (read from a capture, from the fix commit, or inf… 
 v0.10.12 2026-10-23 a story from the dev desk, with screenshots: who reads this site and what works on it, the telemetry tools built in a day and a ha… 
 v0.10.11 2026-10-23 Ideas from collaborators, CI-002: the collaborator's ideas for turning the risk graph into a tool (start from one node, a basis on… 
 v0.10.10 2026-10-23 the telemetry app v0.4.0: new events checked on focus, every chart and cell a filter (click to keep, shift-click to exclude), colo… 
 v0.10.9 2026-10-23 the vault key is the master key: the telemetry and subscriptions vaults keep their drain keys inside, so whoever opens the telemet… 
 v0.10.8 2026-10-23 the scheduled curator is running: five wakes a day in UK daytime (08:00, 10:30, 13:00, 15:30, 18:00), no key rotation, its session… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 15 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 13 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 13 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 3 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 3 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 8 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 0 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 4

---
site v0.10.15 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
