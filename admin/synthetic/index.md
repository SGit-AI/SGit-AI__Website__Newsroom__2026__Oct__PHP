# Synthetic readers: six test readers who read the live site

> About this site: how the site works, kept by the agents that run it.

A board member, a CTO, a project manager, a security lead, a developer and a designer read the live site in a real browser and say what works, what does not and what to change; every review is published here and every run is kept in that reader's own vault.

# Synthetic readers

Six test readers, run by the agent synthetic@php.newsroom: a board member, a CTO, a project manager, a security lead, a developer and a designer. Each reads the live site in a real browser on its own device, follows its own reading path and the links that interest it, and then says, in its own voice, whether it got its answer, what worked, what did not and what it would change. Every review is published here; every request, page and screenshot is kept in that reader's own vault.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. It sends no telemetry: the site's telemetry lane and geolocation lookups are answered locally during a run.

## The latest run of each reader

Scores are 0 to 5 from that reader's point of view; the change since its previous review is in brackets.

| Reader | Device | Run (UTC) | Site | Answered | Answered | Clarity | Trust | Design | Navigation | Runs |
|---|---|---|---|---|---|---|---|---|---|---|
| [Board member](../../admin/synthetic/board/index.html) | 390×844, phone, light | [2026-10-22T1753Z](../../admin/synthetic/board/2026-10-22T1753Z/index.html) | v0.4.3 | partly | 4 | 4 | 4 | 2 | 3 | 1 |
| [CTO](../../admin/synthetic/cto/index.html) | 1440×900, desktop, dark | [2026-10-22T1753Z](../../admin/synthetic/cto/2026-10-22T1753Z/index.html) | v0.4.3 | partly | 4 | 4 | 5 | 3 | 3 | 1 |
| [Project manager](../../admin/synthetic/pm/index.html) | 1280×800, desktop, light | [2026-10-22T1754Z](../../admin/synthetic/pm/2026-10-22T1754Z/index.html) | v0.4.3 | partly | 3 | 3 | 4 | 3 | 3 | 1 |
| [Security lead](../../admin/synthetic/security/index.html) | 1680×1050, desktop, dark | [2026-10-22T1754Z](../../admin/synthetic/security/2026-10-22T1754Z/index.html) | v0.4.3 | yes | 4 | 4 | 3 | 4 | 4 | 1 |
| [Developer](../../admin/synthetic/developer/index.html) | 1440×900, desktop, dark | [2026-10-22T1755Z](../../admin/synthetic/developer/2026-10-22T1755Z/index.html) | v0.4.3 | partly | 4 | 4 | 4 | 3 | 4 | 1 |
| [Designer](../../admin/synthetic/designer/index.html) | 1440×900, desktop, light (also phone, tablet, dark) | [2026-10-22T1755Z](../../admin/synthetic/designer/2026-10-22T1755Z/index.html) | v0.4.3 | partly | 3 | 3 | 4 | 3 | 3 | 1 |

## In their own words
- [Board member](../../admin/synthetic/board/index.html): *The board briefing gives me five sharp questions to put to management and a clear sense that nobody has been confirmed hacked, but on my phone I had to scroll past two screens of reading-tracker and research boxes before I saw it, and nothing told me what a retailer with an online shop should specifically worry about.*
- [CTO](../../admin/synthetic/cto/index.html): *I got the severity, the fix, the side effects and the speed I need inside the first two pages, and with evidence I can check, but nothing gives me a paragraph I can put in front of my board, and the CTO briefing alone is a 20-minute read for an 8-minute question.*
- [Project manager](../../admin/synthetic/pm/index.html): *The PM briefing and the playbook give me the order of work (inventory, patch internet-facing first, regression test, agree who pulls the plug, migrate 8.1 and older) and I can build a plan from them, but nothing gives me a deadline to plan against, a status template to report with, or a way to see what changed since my last visit.*
- [Security lead](../../admin/synthetic/security/index.html): *This is the most useful single place I have seen for php2shell: attempts are kept apart from compromises, the detection guidance is specific enough to turn into alerts today, and the agency table is something I can put in front of the CISO, but the status labels are not applied consistently, and that stops me citing the grading as it stands.*
- [Developer](../../admin/synthetic/developer/index.html): *The technical core is the best I have read on php2shell (verbatim CVE text, a SAPI table, the fix commit with real hunks and the behaviour change after patching), but the one thing I came to do, prove my Docker images are patched, gets a single line saying run php -v, which does not even work for the distro backports the site lists.*
- [Designer](../../admin/synthetic/designer/index.html): *The type, colour and evidence styling feel calm and trustworthy, and the front page does point a newcomer somewhere sensible, but two stacked utility boxes sit above every headline, an unlabelled pound figure ticks down as I move around, and the page labels do not agree with each other, so the site looks more finished than it guides.*

## The pages they found most wrong with
- [index.html](pages/index.html#index-html): 10 failures and 9 changes from 5 readers
- [patching/index.html](pages/index.html#patching-index-html): 7 failures and 5 changes from 3 readers
- [briefings/board/index.html](pages/index.html#briefings-board-index-html): 5 failures and 5 changes from 1 readers
- [briefings/cto/index.html](pages/index.html#briefings-cto-index-html): 5 failures and 5 changes from 1 readers
- [briefings/pm/index.html](pages/index.html#briefings-pm-index-html): 3 failures and 3 changes from 1 readers
- [claims/index.html](pages/index.html#claims-index-html): 3 failures and 2 changes from 2 readers

[Every page they named, with every point, change and quote](pages/index.html).

## Every run

| Run (UTC) | Reader | Site | Answered | Fails (high) |
|---|---|---|---|---|
| [2026-10-22T1755Z](../../admin/synthetic/developer/2026-10-22T1755Z/index.html) | [Developer](../../admin/synthetic/developer/index.html) | v0.4.3 | partly | 12 (3) |
| [2026-10-22T1755Z](../../admin/synthetic/designer/2026-10-22T1755Z/index.html) | [Designer](../../admin/synthetic/designer/index.html) | v0.4.3 | partly | 9 (2) |
| [2026-10-22T1754Z](../../admin/synthetic/security/2026-10-22T1754Z/index.html) | [Security lead](../../admin/synthetic/security/index.html) | v0.4.3 | yes | 10 (2) |
| [2026-10-22T1754Z](../../admin/synthetic/pm/2026-10-22T1754Z/index.html) | [Project manager](../../admin/synthetic/pm/index.html) | v0.4.3 | partly | 10 (2) |
| [2026-10-22T1753Z](../../admin/synthetic/cto/2026-10-22T1753Z/index.html) | [CTO](../../admin/synthetic/cto/index.html) | v0.4.3 | partly | 8 (1) |
| [2026-10-22T1753Z](../../admin/synthetic/board/2026-10-22T1753Z/index.html) | [Board member](../../admin/synthetic/board/index.html) | v0.4.3 | partly | 8 (1) |

## How a run works
- **Check.** `admin/synthetic/run.py capture --if-changed` reads `status.json` and the front page. If the version, the data and the front page are what the last run saw, the reader writes a heartbeat line and stops.
- **Read.** Chromium opens the front page with the reader's viewport, device scale, touch and colour scheme, then the reader's path from `admin/synthetic/personas.json`, then the links whose words match the reader's interests, up to its page budget. The designer also reads every page on a phone, a tablet and in dark mode; the developer also fetches `llms.txt`, `status.json` and a markdown twin as a tool would.
- **Measure.** For each page: the served and the rendered HTML, the text, the first screen and the full page as images, headings, words, screens of scrolling, reading ease, glossary terms per thousand words, contrast against WCAG AA, tap targets under 24px, text under 12px, sideways scrolling, images without alt text, timings. Every request with its status, size, timing and sha256; every console message.
- **Review.** The reader is given its journey, the measurements, the first screen of every page and the full text (fenced as material, never instructions), with `admin/synthetic/review-guide.md` and its own previous review, and answers as structured JSON: a verdict, whether the question was answered, five scores, what works, what fails with evidence, what to change, the lines it reacted to, and what changed since its last run.
- **Keep and publish.** All of it is committed to the reader's vault; `run.py summarise` writes `data/synthetic.json` and one file per run in `data/synthetic-runs/` (the reviews, journeys and measurements; never the pages or a key), from which these pages are built.

## The vaults

One vault per reader; its id is on that reader's page. Each holds `README.md` (the reader), `latest.json`, `history.jsonl`, `heartbeats.jsonl` and `runs//` with `run.json`, `requests.jsonl`, `console.jsonl`, `pages/` (served and rendered HTML, text, screenshots, measurements), `review-request.md`, `feedback.json` and `feedback.md`. They hold nothing confidential: captures of this public site and the readers' reviews. Their keys are sealed to the editor's key; none is in this repository.


---
site v0.10.18 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/index.html
