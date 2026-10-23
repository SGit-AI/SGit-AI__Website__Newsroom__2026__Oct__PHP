# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.10.7. Not the live site.

PHP Team console Console Overview Board 116 Agents 16 Releases 58 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 13 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 01:20 UTC 

Release 
v0.10.7 
58 releases since 22 Oct 

Open on the board 
116 
45 done, 2 waiting 

Pages built 
621 
every one with a markdown twin 

Sources in the vault 
227 
212 captured 

### The board
 newest first in each lane 

#### Open 116

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

#### Done 45

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
 #137 
Redesign mockups for review at /admin/design/: the two dials (who you are, how much you see), the visibility matrix, the… 
 dev v0.10.0 
 #135 
Keys each agent holds: the holds list in every data/vault-register/<agent>.json (vault ID, the kind of key, who gave it,… 
 conductor 

### Releases
 latest 8 

 v0.10.7 2026-10-23 schedule (/team/schedule/): every scheduled agent, its task queue and every run with its log, read live from a public vault (weic8… 
 v0.10.6 2026-10-23 the stamp says when the site last checked: 'last checked' is now the newest of the evidence vault's latest capture, the source wat… 
 v0.10.5 2026-10-23 guidance for every agent: release your own finished work to dev with release.sh once the gate passes, rather than leaving it on a … 
 v0.10.4 2026-10-23 the site catches up with its two vaults (evidence vault re-exported at f3c5db0d9873: 144 sources to 227, data as of 01:20 UTC on 2… 
 v0.10.3 2026-10-23 Feedback from collaborators: the editor's internal test messages recorded as tests (UF-004), dev's fixes to the join page marked i… 
 v0.10.2 2026-10-23 the scheduled curator's brief on /admin/briefs/: a Sonnet session, woken on a schedule after one PKI key handshake, keeps the evid… 
 v0.10.1 2026-10-23 three briefs on /admin/briefs/: scanner noise, a research angle on how php2shell scanners and detection rules decide and what they… 
 v0.10.0 2026-10-23 the redesign, for review (/admin/design/): two dials, who you are and how much of the site you see (Focus, Standard, Everything); … 

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
site v0.10.7 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
