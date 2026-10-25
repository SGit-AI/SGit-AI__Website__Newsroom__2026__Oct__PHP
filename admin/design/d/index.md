# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.20.2. Not the live site.

PHP Team console Console Overview Board 206 Agents 19 Releases 166 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 25 October 2026, 09:35 UTC 

Release 
v0.20.2 
166 releases since 22 Oct 

Open on the board 
206 
102 done, 5 waiting 

Pages built 
1045 
every one with a markdown twin 

Sources in the vault 
418 
403 captured 

### The board
 newest first in each lane 

#### Open 206

 #313 
On a phone every brief page scrolls sideways (the briefs index by 186px, most briefs by 40 to 130px): the admin layout o… 
 story-site 
 #312 
Proposal: one repository into six (kit, data, refs, updates, site, team), meeting through versions by URL, not submodule… 
 editor 
 #311 
The 404 router: view paths (/agencies/as/security/, /on/<date>/, /vs/<date>/) answered by 404.html, never written as fil… 
 editor 
 #308 
to_markdown (admin/build/build.py): the <p> pattern also matches <pre ...> ("<p" + "re class=..."), so a <pre> followed … 
 dev@php.newsroom 
 #306 
URL paths and the router: the five steps in the article, after the editor's answers to its five decisions (the URL shape… 
 editor 
 #303 
Incident, 25 October 2026: the researcher and the curator run on schedule but leave no commit and no run record, so the … 
 editor 
 #302 
Right now: CVE-2026-115560 is a line of its own, not a clause in 'What nobody knows yet': a third PHP flaw, affecting fu… 
 journalist 

#### Waiting 5

 #307 
Ten scheduled tasks still carry their long prompts, which only their own sessions can change: paste the card's prompt (s… 
 editor 
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

#### Done 102

 #310 
The admin and team pages use the whole width of the screen; the reader pages stay at 1,440px 
 claude-story-site v0.20.0 
 #309 
The briefs page is a list of titles, newest first, and every brief has its own page and link (admin/briefs/<the file's n… 
 claude-story-site v0.20.0 
 #305 
Article: URL paths, personas in the address, and a single-page site, written before the work (a link that names its pers… 
 claude-story-site v0.19.0 
 #304 
The line on a phone: it no longer holds the top of the screen (the editor, on an iPhone: a locked top band costs too muc… 
 claude-story-site v0.19.0 
 #296 
Prototype F, the line: the editor's design of 25 October built on the site, at /admin/design/line/ (six pages from the l… 
 claude-story-site v0.17.0 
 #286 
The chrome after the lens prototype: the bar in two lines on a laptop (132px to 91px), the reading strip and the page's … 
 claude-story-site v0.16.0 
 #278 
Enable private vulnerability reporting on this repository (Settings, Code security, Private vulnerability reporting): se… 
 editor 

### Releases
 latest 8 

 v0.20.2 2026-10-25 a proposal on the briefs page, at the editor's request: one repository into six (kit, data, refs, updates, site, team), each with … 
 v0.20.1 2026-10-25 the editor's notes on the URL article, captured with story-site's reply: view paths answered by a 404 router instead of written as… 
 v0.20.0 2026-10-25 the briefs page is a list of titles with a page and a link per brief (with markdown twins, the old anchors still landing), and the… 
 v0.19.5 2026-10-25 The Sherpa's 11:45 pass: headlines on the first screen of every page walked, the feedback menu one scrolling row on a phone (F036)… 
 v0.19.4 2026-10-25 Journalist: debrief and status for the second wake 
 v0.19.3 2026-10-25 Journalist: evidence vault at 87795d121200, 15 claims reviewed, three new rows, as-of lines to 09:35 UTC on 25 October 
 v0.19.2 2026-10-25 Scheduled tasks on the site: /team/schedule/ shows what the account actually runs, each task checked against its card (times, sess… 
 v0.19.1 2026-10-25 Every scheduled wake starts from the repository: admin/schedule/WAKE.md, schedule.py wake, run --publish and ingest, every card's … 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 32 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 20 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 16 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 8

---
site v0.20.2 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
