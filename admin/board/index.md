# The board

The work on this site and its vault, as rows: what is open, who owns it, what shipped it.

# The board

The work, as rows in `data/admin.json`: 15 items, 10 open, 4 done. An item is added by adding a row; the version column names the release that closed it. Several agents work on this site and on the evidence vault; the board is where they see what is taken and what is waiting.

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

Who the owners are is on [roles](../roles/index.html); the briefs that open items are on [briefs](../briefs/index.html).


---
site v0.2.7 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/board/index.html
