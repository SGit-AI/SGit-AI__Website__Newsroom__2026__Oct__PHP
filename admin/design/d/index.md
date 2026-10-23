# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.10.11. Not the live site.

PHP Team console Console Overview Board 121 Agents 16 Releases 62 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 13 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 01:20 UTC 

Release 
v0.10.11 
62 releases since 22 Oct 

Open on the board 
121 
47 done, 2 waiting 

Pages built 
622 
every one with a markdown twin 

Sources in the vault 
227 
212 captured 

### The board
 newest first in each lane 

#### Open 121

 #170 
From CI-002, step 5: a gaps page computed at every build from written rules (control with no path to a test, code with n… 
 dev@php.newsroom 
 #169 
From CI-002, step 4: an impact view: pick a function or file, climb the graph to remediations, vulnerabilities, weakness… 
 dev@php.newsroom 
 #168 
From CI-002, step 3: the fix commit's tests as nodes in the graph, joined to the remediation and code they exercise 
 dev@php.newsroom 
 #167 
From CI-002, step 2: a basis on every graph edge (source, code, inferred, confirmed, with its support), checked in build… 
 dev@php.newsroom 
 #166 
From CI-002 (the Sherpa's brief of 23 October, the risk graph as a tool), step 1: a focus view of the risk graph: open a… 
 dev@php.newsroom 
 #163 
Queue tasks from the page: a signed request from an enrolled key (the editor's) on /team/schedule/, drained into the sch… 
 conductor 
 #162 
The schedules of the curator and the researcher: how often, in which hours (the quiet hours are proposed as 22:00 to 07:… 
 editor 

#### Waiting 2

 #099 
Seal the conductor and collaborators lanes' secrets (enum keys, member tokens, key-pair passphrases) to the root: the se… 
 conductor 
 #013 
Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai key 
 dev 

#### Done 47

 #165 
The telemetry app v0.4.0 (UX vault 5wnsr5h8): new events on focus (at most once a minute); every mark a filter, Kibana-s… 
 dev@php.newsroom v0.10.10 
 #164 
The vault key is the master key: the telemetry (84wr8mib) and subscriptions (wgeiqabu) vaults each hold their drain key … 
 dev@php.newsroom v0.10.9 
 #159 
The schedule vault (weic8imn, public) and /team/schedule/, read live in the browser: every schedule, task queue and run … 
 conductor 
 #156 
Every agent releases its own finished work to dev with release.sh (the editor, 23 October): AGENTS.md section 1, CLAUDE.… 
 conductor 
 #151 
Views: the journalist's state of affairs as a versioned page (/views/state/), its own version numbers, a page per versio… 
 journalist 
 #150 
Act on the fact-check's corrections to the journalist's and the historian's stories: done for 'Where php2shell stands' a… 
 journalist 
 #146 
The updates: /updates/, /feeds/updates.xml, the guide (admin/content/updates/README.md), the digest tool (admin/build/up… 
 journalist 

### Releases
 latest 8 

 v0.10.11 2026-10-23 Ideas from collaborators, CI-002: the collaborator's ideas for turning the risk graph into a tool (start from one node, a basis on… 
 v0.10.10 2026-10-23 the telemetry app v0.4.0: new events checked on focus, every chart and cell a filter (click to keep, shift-click to exclude), colo… 
 v0.10.9 2026-10-23 the vault key is the master key: the telemetry and subscriptions vaults keep their drain keys inside, so whoever opens the telemet… 
 v0.10.8 2026-10-23 the scheduled curator is running: five wakes a day in UK daytime (08:00, 10:30, 13:00, 15:30, 18:00), no key rotation, its session… 
 v0.10.7 2026-10-23 schedule (/team/schedule/): every scheduled agent, its task queue and every run with its log, read live from a public vault (weic8… 
 v0.10.6 2026-10-23 the stamp says when the site last checked: 'last checked' is now the newest of the evidence vault's latest capture, the source wat… 
 v0.10.5 2026-10-23 guidance for every agent: release your own finished work to dev with release.sh once the gate passes, rather than leaving it on a … 
 v0.10.4 2026-10-23 the site catches up with its two vaults (evidence vault re-exported at f3c5db0d9873: 144 sources to 227, data as of 01:20 UTC on 2… 

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
site v0.10.11 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
