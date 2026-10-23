# Synthetic readers: six test readers who read the live site every hour

> About this site: how the site works, kept by the agents that run it.

A board member, a CTO, a project manager, a security lead, a developer and a designer read the live site in a real browser and say what works, what does not and what to change; every run is kept in that reader's own vault.

# Synthetic readers

Six test readers, run by the agent synthetic@php.newsroom: a board member, a CTO, a project manager, a security lead, a developer and a designer. Each reads the live site in a real browser on its own device, follows its own reading path and the links that interest it, and then says, in its own voice, whether it got its answer, what worked, what did not and what it would change. Every request, page, screenshot and review goes into that reader's own private vault.

A synthetic reader is a test instrument, not a reader. Its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. It sends no telemetry: the site's telemetry lane and geolocation lookups are answered locally during a run.

## The latest run

Scores are 0 to 5 from that reader's point of view.

| Reader | Device | Run (UTC) | Site | Answered | Ans. | Clarity | Trust | Design | Nav. | Vault | Runs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [Board member](#board) | 390×844, light | 2026-10-22T1753Z | v0.4.3 | partly | 4 | 4 | 4 | 2 | 3 | `1zq458zk` | 1 |
| [CTO](#cto) | 1440×900, dark | 2026-10-22T1753Z | v0.4.3 | partly | 4 | 4 | 5 | 3 | 3 | `wlhgl8pk` | 1 |
| [Project manager](#pm) | 1280×800, light | 2026-10-22T1754Z | v0.4.3 | partly | 3 | 3 | 4 | 3 | 3 | `9p6jpsd2` | 1 |
| [Security lead](#security) | 1680×1050, dark | 2026-10-22T1754Z | v0.4.3 | yes | 4 | 4 | 3 | 4 | 4 | `vjsqjhvp` | 1 |
| [Developer](#developer) | 1440×900, dark | 2026-10-22T1755Z | v0.4.3 | partly | 4 | 4 | 4 | 3 | 4 | `3l7tzwh9` | 1 |
| [Designer](#designer) | 1440×900, light | 2026-10-22T1755Z | v0.4.3 | partly | 3 | 3 | 4 | 3 | 3 | `dpdx3q13` | 1 |

## Board member

A non-executive director of a mid-sized retailer whose online shop runs on PHP. Not technical. Reads on a phone between meetings. **Question:** Is my company exposed, is management handling it, and what should I ask at the next board meeting?

The board briefing gives me five sharp questions to put to management and a clear sense that nobody has been confirmed hacked, but on my phone I had to scroll past two screens of reading-tracker and research boxes before I saw it, and nothing told me what a retailer with an online shop should specifically worry about.

**Run** 2026-10-22T1753Z on v0.4.3 · **pages** 6 · **requests** 102 · **instrument flags** 0 high, 7 medium, 9 low · **vault** `1zq458zk`

### What did not work
- **high** On a phone the first screen of every page is site machinery, not the story: version badge, a £ meter, a reading tracker with 'fade / hide / show' buttons and a 'Research' box. On the board briefing the thirty-second answer only begins at the very bottom of the first screen. ([briefings/board/index.html](../../briefings/board/index.html)): fold.png shows 'Your reading: on this page 35 new, 0 changed, 0 read', 'Mark this page read', 'Mark everything read', 'Read items: fade hide show', the RESEARCH box and the 'New to this story?' banner before 'THE ANSWER IN THIRTY SECONDS' appears at the bottom edge.

### What this reader would change first
- Move the reading tracker, £ meter and Research box below the article on phones (or collapse them into one line), so the thirty-second answer is the first thing on the first screen. ([briefings/board/index.html](../../briefings/board/index.html), medium): Between meetings I have seconds; today I scroll past controls I never use before I learn whether to worry.
- Add two or three sentences on cost: what downtime has looked like for organisations so far (for example Weird Gloop's 13 hours) and what a breach would put at risk, with a link to the CFO briefing. ([briefings/board/index.html](../../briefings/board/index.html), small): The headline asks 'what is it costing us' and the page never answers it.
- Add one line for organisations that sell online: shop platforms such as Magento and WordPress shops run on PHP, and a compromise could reach customer data and payment settings. ([briefings/board/index.html](../../briefings/board/index.html), small): It would tell me in one sentence that my company is squarely in scope and why it matters to us.

## CTO

CTO of a SaaS company with a PHP monolith and a dozen PHP microservices on containers. Technical, short of time, accountable for the call. **Question:** How bad is this for us, what is the fix and its side effects, how fast must we move, and what do I tell the board?

I got the severity, the fix, the side effects and the speed I need inside the first two pages, and with evidence I can check, but nothing gives me a paragraph I can put in front of my board, and the CTO briefing alone is a 20-minute read for an 8-minute question.

**Run** 2026-10-22T1753Z on v0.4.3 · **pages** 8 · **requests** 136 · **instrument flags** 0 high, 0 medium, 4 low · **vault** `wlhgl8pk`

### What did not work
- **high** No board-ready summary anywhere on my path: the CTO briefing headline question drops 'what do I tell the board', and the Board member briefing is a separate path. ([briefings/cto/index.html](../../briefings/cto/index.html)): Headline: 'What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?' No section addresses board messaging; the board appears only as 'Board member or executive' in the Other readers list at the foot.

### What this reader would change first
- Add a 'What to tell the board' box of four or five sentences (severity and evidence, our likely exposure class, the fix and its risk, the timeline, what is still unknown) just under the thirty-second answer. ([briefings/cto/index.html](../../briefings/cto/index.html), small): It is a quarter of my question and the one I have to answer in person, and right now I have to assemble it myself.
- Split the claims table into 'Decide on these' (severity, fix, FPM, EOL, WAF, side effects) and 'Background' (timing and attribution disputes), collapsing the second. ([briefings/cto/index.html](../../briefings/cto/index.html), small): The briefing tells me to skip the disclosure politics, then makes me read them to find the FPM and EOL rows.
- Give the Docker Official Image row the fixed tags or the date the images were rebuilt, and add one line on how to verify the PHP version inside a running container. ([patching/index.html](../../patching/index.html), small): We run a dozen microservices on containers and 'rebuild every image' is only useful if I know which base image is safe.

## Project manager

Delivery manager running the patch programme across forty client websites at an agency. Some technical understanding, lives in plans and status updates. **Question:** What has to happen, in what order, by when, and how do I report progress?

The PM briefing and the playbook give me the order of work (inventory, patch internet-facing first, regression test, agree who pulls the plug, migrate 8.1 and older) and I can build a plan from them, but nothing gives me a deadline to plan against, a status template to report with, or a way to see what changed since my last visit.

**Run** 2026-10-22T1754Z on v0.4.3 · **pages** 7 · **requests** 119 · **instrument flags** 0 high, 4 medium, 6 low · **vault** `9p6jpsd2`

### What did not work
- **high** No deadline anywhere. The guidance says 'now', 'this week' and 'the next fortnight' but never states whether any agency set a due date, so I cannot put a hard date on the plan or tell a client how late is too late. ([briefings/pm/index.html](../../briefings/pm/index.html)): 'Expect unplanned work this week' and 'Keep a slot free in the next fortnight'; the playbook steps carry no dates at all.
- **high** Nothing on how to report progress, although the briefing's own question promises 'what do I tell stakeholders'. There is no status template, no suggested measures (systems inventoried, patched, verified, offline) and no wording for a client update. ([briefings/pm/index.html](../../briefings/pm/index.html)): 'What this briefing covers' lists 'what to tell stakeholders about downtime', but the page body only says 'Agree with stakeholders now who can make that call'.

### What this reader would change first
- Add a 'Deadlines' line at the top of the PM briefing stating whether any agency set a due date (and that CISA has not listed these flaws in KEV, so no federal due date), plus a recommended internal target such as internet-facing patched within N days. ([briefings/pm/index.html](../../briefings/pm/index.html), small): I plan against dates; 'this week' and 'next fortnight' cannot go in a programme plan or a client SLA conversation.
- Add a 'How to report progress' section with a copyable status table (system, owner, PHP version, hosting route, patched yes/no, verified running version, offline yes/no, next date) and a two-line stakeholder update template. ([briefings/pm/index.html](../../briefings/pm/index.html), medium): Reporting is half my question and the briefing title promises it; with forty clients I need one consistent format.
- Add a 'Changed in the last 24 hours' block at the top of the timeline and the PM briefing, listing only rows added or changed since the previous day. ([timeline/index.html](../../timeline/index.html), medium): My daily routine is 'what moved since yesterday'; the read-tracking bar does not help on a first visit or on a new device.

## Security lead

Head of security operations at a bank. Expert. Needs detection, exploitation status and sources that can be cited to the CISO. **Question:** Is it exploited in the wild, how do I detect it, what do the agencies say, and how good is the evidence?

This is the most useful single place I have seen for php2shell: attempts are kept apart from compromises, the detection guidance is specific enough to turn into alerts today, and the agency table is something I can put in front of the CISO, but the status labels are not applied consistently, and that stops me citing the grading as it stands.

**Run** 2026-10-22T1754Z on v0.4.3 · **pages** 9 · **requests** 153 · **instrument flags** 0 high, 0 medium, 6 low · **vault** `vjsqjhvp`

### What did not work
- **high** The site contradicts itself about whether Amazon's own post was captured, while still grading the claim built on it as CONFIRMED. ([exploitation/index.html](../../exploitation/index.html)): The exploitation row for Alan Woodward reads 'Cloudflare's own post confirms attack traffic, Amazon's own post not found', but claims/index.html grades 'Amazon and Cloudflare saw sites being probed' CONFIRMED with 'confirmed by both companies' own posts', and sources/index.html lists the captured 'Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog' (capture 20261022T111755Z).
- **high** CONFIRMED is used for single-source items although the site's own definition requires two or more primary sources or a count from a captured file. ([claims/index.html](../../claims/index.html)): The legend says 'CONFIRMED two or more primary sources agree, or the fact was counted from a captured file', yet the CISA offline-advice claim is 'CONFIRMED 1/1', Latvia's restrictions 'CONFIRMED 1/1' and Weird Gloop 'CONFIRMED 1/1'. On exploitation/index.html, CCCS, CERT.LV and the CISA ADP row are each 'CONFIRMED (PRIMARY)' on one source.

### What this reader would change first
- Re-run the status rules across every table so that a one-source primary item is REPORTED (or add a named 'PRIMARY, single source' grade to the legend), and use one grade per claim on every page. ([claims/index.html](../../claims/index.html), medium): I cannot hand the CISO a grading scheme that breaks its own definition. Consistency is what makes the labels citable.
- Fix the Woodward row to say Amazon's own post was captured, and link the Amazon claim to the aws-security-blog-madpot capture. ([exploitation/index.html](../../exploitation/index.html), small): This is the single clearest self-contradiction on the exploitation question, which is the question I most need to get right.
- Make the signal count 19 distinct events (or say '20 rows, 19 events'), merging the two Amazon 17 October rows. ([exploitation/index.html](../../exploitation/index.html), small): Double counting weakens a page whose whole value is careful counting.

## Developer

Senior PHP developer maintaining Laravel apps and the Docker images they run on. Reads code, diffs and changelogs; uses LLM tools and wants machine-readable formats. **Question:** What exactly is the bug, which versions and SAPIs, what does the fix change, and how do I verify my images are patched?

The technical core is the best I have read on php2shell (verbatim CVE text, a SAPI table, the fix commit with real hunks and the behaviour change after patching), but the one thing I came to do, prove my Docker images are patched, gets a single line saying run php -v, which does not even work for the distro backports the site lists.

**Run** 2026-10-22T1755Z on v0.4.3 · **pages** 8 · **requests** 136 · **instrument flags** 0 high, 0 medium, 3 low · **vault** `3l7tzwh9`

### What did not work
- **high** There is no real verification step for container images: one sentence about php -v, no docker run command, no image tags, no check that works on a distro backport. ([briefings/developer/index.html](../../briefings/developer/index.html)): The only instruction is 'Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.' Nothing on the page or the reading path adds to it.
- **high** Comparing the php -v output with the fixed version list gives the wrong answer for distro backports, and the site itself lists them as fixed. An Ubuntu Noble box reports 8.3.6, which is below 8.3.36, yet the site marks that package as fixed. ([patching/index.html](../../patching/index.html)): 'fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13' against the briefing's 'Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35'. No version-independent check is offered, such as testing whether the new max_multipart_body_parts setting exists.
- **high** The Docker Official Image row, the one I care most about, has no tag, version or digest, so I cannot tell which php:* tags are fixed or whether my pinned digest is. ([patching/index.html](../../patching/index.html)): 'fixed Docker Official Images maintainers: Docker Official Image: php' with no version text, while the Debian, Red Hat and Bref rows all carry versions.

### What this reader would change first
- Add a 'Verify your image' block with copy-paste commands: docker run --rm  php -v, plus a check that does not depend on the version number (for example whether php -r 'var_dump(ini_get("max_multipart_body_parts"));' returns a value, if the site can confirm it marks a patched build) and the distro changelog check for backports. ([briefings/developer/index.html](../../briefings/developer/index.html), medium): This is the half of my question the site does not answer, and php -v alone gives the wrong result on the Ubuntu and Red Hat backports the site lists as fixed.
- Give the Docker Official Image row the fixed tags (8.5.12, 8.4.27, 8.3.36, 8.2.35 for each variant: cli, fpm, apache, alpine) and the date the images were rebuilt. ([patching/index.html](../../patching/index.html), small): I run on php:*-fpm and php:*-apache bases; without tags I cannot check my Dockerfiles or pinned digests.
- Add a fixed_versions map per branch and an affected_ranges field to status.json, and link data/affected.json from its links block. ([status.json](../../status.json), small): Then a CI step or an LLM tool can gate on the data instead of parsing a prose headline.

## Designer

Product and content designer. Judges hierarchy, typography, layout, consistency, accessibility and whether the site guides a newcomer. Checks phone, tablet and desktop, light and dark. **Question:** Does the site look and feel trustworthy, does it guide a newcomer, and does it work on every screen for every reader?

The type, colour and evidence styling feel calm and trustworthy, and the front page does point a newcomer somewhere sensible, but two stacked utility boxes sit above every headline, an unlabelled pound figure ticks down as I move around, and the page labels do not agree with each other, so the site looks more finished than it guides.

**Run** 2026-10-22T1755Z on v0.4.3 · **pages** 7 · **requests** 119 · **instrument flags** 0 high, 2 medium, 22 low · **vault** `dpdx3q13`

### What did not work
- **high** On a phone the site chrome eats most of the first screen: masthead, a theme dot, a price pill, the 'New to this story?' banner, the 'Your reading' panel and the RESEARCH band all come before the headline. ([claims/index.html](../../claims/index.html)): Phone metrics put the h1 at 590px on claims and 550px on index.html in an 812px-tall screen; on briefings/everyone the thirty-second answer box only starts at the very bottom edge of fold-phone.png.
- **high** An unlabelled money figure sits in the masthead and changes from page to page with no explanation, which reads as a charge and undermines trust for a newcomer. ([index.html](../../index.html)): Desktop pill shows '£4.99' on index.html, '£4.96' on briefings/everyone, '£4.95' on claims and glossary, '£4.94' on explained; the phone shows '£5.00', '£4.98' and '£4.97'. Nothing on the visible page says what it is.

### What this reader would change first
- On phone, move the 'Your reading' panel and the RESEARCH / ABOUT band below the h1 and standfirst (or collapse them into one line), so the headline is in the top third of the first screen. ([index.html](../../index.html), medium): The headline is the one thing to read first and on a phone it currently starts two-thirds of the way down on every page.
- Label the pound pill in the masthead (for example 'Reading credit: £4.95, free') or hide it until the reader opens the account menu. ([index.html](../../index.html), small): An unexplained, falling money figure is the single biggest trust risk for a newcomer.
- Make the band, kicker and highlighted menu item come from one source, so glossary and explained both say the same section, and the Stories page says STORIES. ([glossary/index.html](../../glossary/index.html), small): The site promises each page states which half it belongs to; inconsistent labels break that promise visibly.

## How a run works

- **Check.** `admin/synthetic/run.py capture --if-changed` reads `status.json` and the front page. If the version, the data and the front page are what the last run saw, the reader writes a heartbeat line and stops.

- **Read.** Chromium opens the front page with the reader's viewport, device scale, touch and colour scheme, then the reader's path from `admin/synthetic/personas.json`, then the links whose words match the reader's interests, up to its page budget. The designer also reads every page on a phone, a tablet and in dark mode; the developer also fetches `llms.txt`, `status.json` and a markdown twin as a tool would.

- **Measure.** For each page: the served and the rendered HTML, the text, the first screen and the full page as images, headings, words, screens of scrolling, reading ease, glossary terms per thousand words, contrast against WCAG AA, tap targets under 24px, text under 12px, horizontal overflow, images without alt text, timings. Every request with its status, size, timing and sha256; every console message.

- **Review.** The reader is given its journey, the measurements, the first screen of every page and the full text, with `admin/synthetic/review-guide.md`, and answers as structured JSON: a verdict, whether the question was answered, five scores, what works, what fails with evidence, what to change, the lines it reacted to, and what changed since its last run. The review is written by the Claude API when the run has a key, or by an agent session.

- **Keep.** All of it is committed and pushed to the reader's vault; `run.py summarise` writes this page's data, `data/synthetic.json`, with no keys in it.

## The vaults

One private vault per reader, ids in the table above. Each holds `README.md` (the reader), `latest.json`, `history.jsonl`, `heartbeats.jsonl` and `runs//` with `run.json`, `requests.jsonl`, `console.jsonl`, `pages/`, `review-request.md`, `feedback.json` and `feedback.md`. The vault keys are held by the editor and the agent that runs the readers; none is in this repository.


---
site v0.9.0 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/index.html
