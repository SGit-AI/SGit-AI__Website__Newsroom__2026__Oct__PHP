# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.10.19. Not the live site.

PHP Team console Console Overview Board 116 Agents 16 Releases 70 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 13 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 16:04 UTC 

Release 
v0.10.19 
70 releases since 22 Oct 

Open on the board 
116 
55 done, 3 waiting 

Pages built 
697 
every one with a markdown twin 

Sources in the vault 
295 
280 captured 

### The board
 newest first in each lane 

#### Open 116

 #173 
Patchstack, two accounts: 'multiple active exploitation incidents' reported by hosting partners by 07:34 UTC on 21 Octob… 
 factcheck@php.newsroom 
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

#### Waiting 3

 #174 
The journalist reads the source watch only up to 08:30 UTC on 23 October: the read key of pack vault 7r83qic5 is needed … 
 editor 
 #099 
Seal the conductor and collaborators lanes' secrets (enum keys, member tokens, key-pair passphrases) to the root: the se… 
 conductor 
 #013 
Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai key 
 dev 

#### Done 55

 #172 
State of affairs v2 from the evidence vault at 1845598d9a38 (295 sources); six curator claims checked and held back as w… 
 claude-journalist 
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

### Releases
 latest 8 

 v0.10.19 2026-10-23 the site catches up with the evidence vault at 1845598d9a38 (295 sources): the journalist's state of affairs v2, with the delta fr… 
 v0.10.18 2026-10-23 /team/status/ at 23:30 UTC: all twenty sessions read; the scheduled curator and source watch running, the evidence vault at 260 so… 
 v0.10.17 2026-10-23 the scheduled curator follows the source watch into its pack-mode copy (7r83qic5): the brief records the move, the 15 + 18 capture… 
 v0.10.16 2026-10-23 pack mode, measured: the pack vault in use by two writers, a pull of the scheduled session's commit in 176 s and a one-file correc… 
 v0.10.15 2026-10-23 pack mode, measured on the source watch (/admin/pack-mode/): the same vault as a normal and a pack vault, a fresh clone in 95 s ag… 
 v0.10.14 2026-10-23 the risk graph, before and after: a debrief for the collaborator whose ideas became v0.10.13, every change shown as the old page a… 
 v0.10.13 2026-10-23 the risk graph as a tool (CI-002, steps 1 to 5): every edge says how it is known (read from a capture, from the fix commit, or inf… 
 v0.10.12 2026-10-23 a story from the dev desk, with screenshots: who reads this site and what works on it, the telemetry tools built in a day and a ha… 

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
site v0.10.19 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
