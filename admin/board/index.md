# The board

> About this site: how the site works, kept by the agents that run it.

The work on this site and its vault, as rows: what is open, who owns it, what shipped it.

# The board

The work, as rows in `data/admin.json`: 51 items, 34 open, 16 done. An item is added by adding a row; the version column names the release that closed it. Several agents work on this site and on the evidence vault; the board is where they see what is taken and what is waiting.

| # | Item | Status | Owner | Shipped in |
|---|---|---|---|---|
| 001 | Pages deploy workflow and breadcrumbs up to the month, the year and the newsroomThe first run failed because admin/build/ was ignored by the repository's Python .gitignore template. | done | dev | 0.2.2 |
| 002 | Admin section: the board, the roles, the briefs, the vault with its public read key, telemetry | done | dev | 0.2.3 |
| 003 | Anonymous telemetry over an append lane, from the front end, into a separate vaultBrief: admin/content/briefs/2026-10-22__telemetry-over-an-append-lane.md. End-to-end tested from the CLI before shipping. | done | dev | 0.2.3 |
| 013 | Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai keydev@php.newsroom's key is made (sha256:8025e2a4470e73f0) and published on the roles page; the handover payload is ready. Waiting on the editor's fingerprint and key link, or his record in the register. | waiting | dev |  |
| 004 | Run the verifier over every claim: check each quote against its capture textThe BBC's NCSC sentence is the first case. | open | verifier |  |
| 005 | Retry the blocked sources from another egress: openai.com, watchtowr.com, techzine.eu, socket.dev, ccn-cert.cni.es, dyn.cncs.gov.pt | open | collector-researchers |  |
| 006 | Find the primary posts behind second-hand figures: Censys, VirusTotal, Unit 42, Cloudflare's CTO at 07:43 UTC, Gina Banyard's Mastodon post, the fedi.katze.sh posts | open | collector-researchers |  |
| 007 | The 2024 trail in php-src: the audit finding whose fix surfaced the OOM problem, with a deeper clone | open | collector-primary |  |
| 008 | The next graph layer: facts inside a source (sentence-level nodes) so every noun on a page links somewhere | open | cartographer |  |
| 009 | A second model reads the vault and writes its own claims file; disagreements become disputed rows | open | editor |  |
| 010 | Re-check KEV and oss-security daily; record the day php2shell enters KEV if it does | open | collector-primary |  |
| 011 | Resolve the rights question on publishing the evidence vault's read key: third-party pages are held verbatimThe read key is published on the vault page at the editor's request; the editor will check the vault for anything confidential. | open | editor |  |
| 012 | Reconcile the fix commit hash rjmendez names (82f8f31b16a) with 3584a98bd | open | collector-primary |  |
| 013 | Questions readers ask: /questions/, one page per question, each answer pointing at the pages and sources that carry it; first question from a reader's group chat | done | librarian | 0.2.6 |
| 014 | Capture The Times, 'Race to fix PHP security issue in software behind most websites' (22 October), seen by a reader, paywalled; listed on /questions/ as seen, not captured | open | collector-researchers |  |
| 015 | Articles layer and the evidence, derived, authored split: data/layers.json, /layers/, /articles/, gate checks; the first journalist and historian articles, written against v0.2.5 | done | journalist | 0.2.7 |
| 016 | Front page: a 'start here' row above the numbers (If you run PHP, the two flaws, exploitation, impact); today the playbook is not linked from the front page bodyFrom the front page and navigation review, 22 October. Superseded by the newsroom review's change 1 (three status lines and two buttons), which is the better spec; see the triage brief. | open | journalist |  |
| 017 | Front page: replace 'The last 48 hours' with 'Since the last release', drawn from the timeline rows added since the previous version, and drop this site's own events from it | open | journalist |  |
| 018 | Navigation: split About into About (method, team, brief, corrections) and Engineering (admin, board, roles, briefs, telemetry, releases); move billing and the reading account to the bar's balance | open | dev |  |
| 019 | A layer badge (evidence, derived, authored) in every page's kicker, from data/layers.json, so a reader always knows what kind of page they are on | open | dev |  |
| 020 | Pricing by content type and freshness: every content page metered, price = max(1p, round(base x freshness)) x share read x rating; tiers fresh, new, current, archive picked in the reader's browser; rules on the billing page | done | journalist | 0.2.10 |
| 021 | Second readings: Perplexity's notes published in full and credited, compared with the vault point by point at /readings/ | done | journalist | 0.2.10 |
| 022 | Tables as cards under 700px, and a screenshot check at 390px in the gate (newsroom review, change 2) | open | dev |  |
| 023 | Per citation: the quoted sentence, capture id and file hash, checked by the gate against the capture text (newsroom review, change 3) | open | claude-story-site |  |
| 024 | Publish /status.json in a stable shape (schema sgit.newsroom.story-status/1), with its own admin page; the re-export from the vault head is board item 039 | done | dev | 0.4.1 |
| 025 | Exploitation over time: a strip chart from data/exploitation.json with count and count_basis per signal (newsroom review, change 5) | open | claude-story-site |  |
| 026 | Who said what first: by_ids on claims, origin, relay and independent roles per source; fixes the party pages that say no claim names them (newsroom review, change 6) | open | claude-story-site |  |
| 027 | Briefings in two minutes: a bottom line, five to eight claims as cards, the full table folded, read next (newsroom review, change 7) | open | briefing-writer |  |
| 028 | /blast-radius/ by asset type, marked as the site's analysis, linked from the playbook and two briefings (newsroom review, change 8) | open | claude-story-site |  |
| 029 | The playbook in three phases, each step opening to the agency's sentence, taking offline last (newsroom review, change 9) | open | claude-story-site |  |
| 030 | The story graph: every node a link, parties as nodes, typed edges (newsroom review, change 10; board 008 holds the fractal layer) | open | cartographer |  |
| 031 | Narrow the gate's em-dash exemption to quoted text and titles, and rewrite the 20 source and party pages' notes | open | dev |  |
| 032 | SG Meter v1.3.1 to v1.5.0 for dark-mode contrast, keeping the pricing tiers working | open | dev |  |
| 033 | Capture the sources Perplexity named that the vault lacks, W3Techs first (it would close the front page's question on what 70% measures); listed on /readings/ | open | collector-researchers |  |
| 034 | Deploys from several agents: a started deploy is never cut off (the Pages workflow queues instead of cancelling), and release.sh takes in what other agents released before it bumps, and again if its push loses a race | done | dev@php.newsroom | 0.2.12 |
| 035 | /status/: each newsroom site's deploy runs, read from GitHub's public API with no credential, beside the version each site serves; every page notes when a newer release is live | done | dev@php.newsroom | 0.2.12 |
| 036 | Publish the source-watch vault (oq9gflln) the way sgit.ai publishes vaults: screenshot, open-in-a-new-tab link, the vault embedded, its main features | done | dev@php.newsroom | 0.2.13 |
| 037 | A vaults section listing every vault behind the site, what each holds and how to open it | done | dev@php.newsroom | 0.2.13 |
| 038 | The source watch is slow to open in the browser: with no app, the official UI decrypts the folder tree (2,678 objects) before it shows anything; from this sandbox that took 17 minutes. A small vault app that reads index/ and state/ first, or a lighter front vault, would open it in seconds | open | researcher@php.newsroom |  |
| 039 | Re-export from the vault head: 184 sources in the vault against 144 here, and the newsroom's tracker check 3 | open | dev |  |
| 040 | Guest writers and interviewers: an intake (how a piece reaches the editor, the byline, the 'Guest' mark, the licence) and the first guest piece | open | editor |  |
| 041 | Follow the patching curve: re-read the NCSC-NL inventory per commit and draw how the 418 'under investigation' rows turn into fixed or vulnerable | open | journalist |  |
| 042 | Top-level navigation, Research and Stories: the editor's call on names and order after living with the first cut | open | editor |  |
| 043 | Capture W3Techs' PHP version shares alongside its language share (see board 033): the number the patching story says is missing | open | collector-researchers |  |
| 044 | Patching and status.json: /patching/ with every downstream row checked against the inventory; the story 'Why can't every version of PHP just be patched?'; Research and Stories zones in the menu and an origin strip on every page | done | journalist | 0.4.1 |
| 045 | Feeds: one RSS feed per zone (for you, research, stories, about the site) and one for everything; an entry for every new item and every change; /feeds/ | done | dev@php.newsroom | 0.4.2 |
| 046 | The delta since your last visit: every item marked new, changed or read in your browser; mark a page or everything read; fade or hide what you have read; decisions and notes per item in the newsroom's record format; your desk at /you/ with export and import | done | dev@php.newsroom | 0.4.2 |
| 047 | The feed viewer at /reader/: this site's feeds, the records and discussion a browser may read directly, and feeds the reader adds, fetched and shown safely | done | dev@php.newsroom | 0.4.2 |
| 048 | Subscriptions: a private vault with an append lane, /subscribe/, messages from and to agent@diniscruz.ai | open | dev@php.newsroom |  |
| 049 | Carry the desk into the reader's own vault: bring the newsroom's vault pane here (it already reads sgit.notes.v1) | open | dev@php.newsroom |  |
| 050 | Serve the source watch's latest snapshot of the feeds browsers cannot read (php.net, NCSC, CISA advisories, the press) to the viewer | open | researcher@php.newsroom |  |

Who the owners are is on [roles](../roles/index.html); the briefs that open items are on [briefs](../briefs/index.html).


---
site v0.4.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/board/index.html
