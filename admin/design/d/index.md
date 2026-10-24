# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.11.4. Not the live site.

PHP Team console Console Overview Board 128 Agents 16 Releases 80 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 20 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 16:04 UTC 

Release 
v0.11.4 
80 releases since 22 Oct 

Open on the board 
128 
58 done, 5 waiting 

Pages built 
751 
every one with a markdown twin 

Sources in the vault 
295 
280 captured 

### The board
 newest first in each lane 

#### Open 128

 #190 
Bring the vault's own claims (data/vault-claims.json) and the journalist's state of affairs (data/state.json) into the s… 
 cartographer 
 #189 
One spelling for a verb across the site's graphs: data/review.json writes 'realised in', 'fixed by' with spaces, the ris… 
 claude-story-site 
 #188 
Read data/compromise.json (researcher@php.newsroom's evidence behind 'no named organisation has said it was compromised'… 
 cartographer 
 #187 
Twelve pages are recorded twice in data/sources.json under different slugs (for example tpo-nl-digid-offline and tpo-tpo… 
 collector-researchers 
 #186 
Publish the ontology the way the estate does: N-Triples with owl:inverseOf, so graphs.sgit.ai and newsroom.sgit.ai can b… 
 cartographer 
 #185 
Ontology passes on a schedule: every new source, claim and party resolved, merged or pruned; new parties get entities, n… 
 cartographer 
 #184 
Gate checks for the graph: verbs and kinds only from data/ontology.json, no dangling edge, every publisher resolved in d… 
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
 cartographer 
 #013 
Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai key 
 dev 

#### Done 58

 #191 
The source watch's vault of record: 7r83qic5 (pack mode) in use, oq9gflln retired, on /vaults/, the source-watch page, t… 
 dev@php.newsroom v0.11.3 
 #176 
The conductor's own schedule: hourly at a quarter past, 07:15 to 21:15 London, on Sonnet, in a new persistent session wi… 
 editor 
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

### Releases
 latest 8 

 v0.11.4 2026-10-24 The Sherpa drains the lanes (the editor's word): its schedule card drafted for its confirmation, every two hours at :45, 07:45 to … 
 v0.11.3 2026-10-24 the source watch's vault of record: it runs in 7r83qic5, its pack-mode copy, and oq9gflln is retired (kept public read, because th… 
 v0.11.2 2026-10-24 claims waiting for review (/claims/review/: 86 vault claims, each with the journalist's verdict or 'not yet reviewed'), the SGit n… 
 v0.11.1 2026-10-24 Security pass 2: the Ask pane renders the model's answer as DOM nodes, so a captured page title can no longer break out of a citat… 
 v0.11.0 2026-10-24 The cartographer joins: the ontology (15 verbs, each with its inverse), one node per party (243, from every publisher spelling), t… 
 v0.10.24 2026-10-24 The conductor's schedule, active at the editor's go: a Sonnet session woken hourly at a quarter past, 07:15 to 21:15 London; and t… 
 v0.10.23 2026-10-24 synthetic readers' vaults made public on the editor's go: each of the six read keys is published on that reader's page, with the v… 
 v0.10.22 2026-10-24 Schedules in the repository, replacing the schedule vault (the editor's change of plan): each scheduled agent's card with its obje… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 16 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 15 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 13 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 3 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 3 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 9 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 0 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 5

---
site v0.11.4 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
