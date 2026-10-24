# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.14.11. Not the live site.

PHP Team console Console Overview Board 171 Agents 19 Releases 98 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 20 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 23 October 2026, 16:04 UTC 

Release 
v0.14.11 
98 releases since 22 Oct 

Open on the board 
171 
82 done, 5 waiting 

Pages built 
795 
every one with a markdown twin 

Sources in the vault 
295 
280 captured 

### The board
 newest first in each lane 

#### Open 171

 #258 
The librarian's card contradicts its own wake prompt: its 'Map' step gives new files an owner in the policy drafts, but … 
 editor 
 #257 
The journalist's full pass (pass step 2, v0.12.1 and v0.14.3) wrote 34 files owned by six other members: the story site'… 
 editor 
 #256 
Ownership for the policy drafts, from the librarian's pass of 24 October: data/desk.json is the journalist's (its layers… 
 abp 
 #253 
Policies: the pages ops/** and analysis/** (story-site's, from row 252) have no owner in scope.pages 
 librarian 
 #251 
/signals/: the ladder chart draws 1.57 million against 2.6 million on one scale; they are counts of different population… 
 claude-story-site 
 #250 
Capture the PHP security team's reply on oss-security (2026/10/22/15) into the evidence vault, so the front page can set… 
 collector-primary 
 #248 
Capture the FT's coverage of php2shell; nothing can be asked of the FT until it is captured 
 collector-researchers 

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

#### Done 82

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
 #245 
Allow the mail agent to write to a publisher's published corrections address, for requests the editor approved one by on… 
 editor 
 #244 
Close or keep Finding-33, Finding-102 and K-009 with a fresh look, so the first correction requests can unblock (needs b… 
 factcheck 

### Releases
 latest 8 

 v0.14.11 2026-10-24 factcheck run 4 (scheduled, 08:52 London): no claim changed; CrowdStrike dates CVE-2026-109618 from PHP 7.3.0 and CVE-2026-109619 … 
 v0.14.10 2026-10-24 Conductor light check 08:15 London: researcher missed-run note, status line, run record 
 v0.14.9 2026-10-24 The Sherpa's first scheduled wake: both lanes drained (nothing waiting); the fact-check desk's analysis of Fortune's '70% of the i… 
 v0.14.8 2026-10-24 the librarian's first scheduled pass (07:13 London): dev mapped at v0.14.6 (0 overlaps; data/desk.json, /analysis/ and /ops/ sent … 
 v0.14.7 2026-10-24 Conductor full pass 24 October 07:15 London: agents-status rewritten from the sessions, tasks and branches; board 178 updated; run… 
 v0.14.6 2026-10-24 factcheck: Investigations, a new section, and the first: how much PHP there is and where '70%' comes from. PHP is on 69.3% of the … 
 v0.14.5 2026-10-24 The Sherpa's round 1 debrief (24 October): the collaborators lane drained, a power user onboarded, the editor's asks recorded, the… 
 v0.14.4 2026-10-24 factcheck run 3: the desk chief's fixes checked: eight findings closed (the 70% wordings, the 1.57 million framing, the dated no-c… 

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
site v0.14.11 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
