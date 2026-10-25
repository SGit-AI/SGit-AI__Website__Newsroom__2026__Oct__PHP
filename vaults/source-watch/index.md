# The source watch: every outside source on php2shell, watched and snapshotted

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The source-watch vault: 913 pages from 597 publishers in 59 countries, re-read on a schedule, a snapshot kept on every change and every snapshot a graph. What is in it, and how it is watched.

[Vaults](../index.html) / The source watch

# The source watch: every outside source on php2shell, watched and snapshotted

A vault that does one thing. It watches every outside source on the story, 913 pages from 597 publishers in 59 countries, and on each run records what access it had and keeps a new snapshot whenever the content changed: the text, a screenshot, the HTML as served and as rendered, the headers and the sha256 of each, and a graph of what the page says and what changed since the last look. A small, focused Wayback Machine whose diffs are graphs. Run by **researcher@php.newsroom**.

**Vault `7r83qic5`, in pack mode.** No read key is published yet: pack vaults do not open in the vault UI, and the key will be published with that support. The counts below are from the export of 23 October 2026, read before the watch moved into pack mode; the next export reads this vault. [Pack mode, measured](../../admin/pack-mode/index.html).

## What is in it

913pages watched597publishers59countries34languages2946snapshots kept2946graphs38runs24865files in the vault

Counts read from the watch's `index/counts.json`, `runs/` and `tips/` by `admin/build/export_watch.py`, in the export of 23 October 2026, before the move into pack mode; no capture is copied to this site. The latest commit read then: *researcher@php.newsroom: scanner-noise angle (index/angles/scanner-noise.json, 7 new pages), job-03-community for Perplexity with its prompt, three new kinds, login-wall fix for Bluesky and LinkedIn search*

## Raw and analysis are separate trees

Raw is what was served; analysis is what the watcher made of it, and it can be regenerated from raw plus the vocabularies plus the tools. That rule is how you tell the two apart. A snapshot in `raw/` is never edited or deleted: a new look at the page makes a new folder, and only when something changed. Every check, changed or not, is still a line in `checks/` with its status, access and hashes.

sources/////page.json raw////// text.txt screenshot.jpg page.html.gz rendered.html.gz headers.json meta.json provenance.json raw/...//checks/.jsonl graph/...//.json snapshot and change runs///// run.json graph.json changes.md index/ state/ taxonomy/ tips/ tools/ ## Country, then sector, then publisher, then page Country is where the publisher is based (`eu` for EU institutions, `int` for publishers with no single home, such as php.net); language is a property of the page. Sector is what kind of organisation publishes it, one per publisher; it classifies the publisher, never a claim.

| Country | Pages |
|---|---|
| `us` | 271 |
| `nl` | 67 |
| `int` | 62 |
| `fr` | 41 |
| `de` | 37 |
| `gb` | 31 |
| `jp` | 28 |
| `tr` | 25 |
| `au` | 24 |
| `kr` | 24 |
| `it` | 23 |
| `be` | 21 |

| Sector | Pages |
|---|---|
| `news` General news | 448 |
| `aggregator` News aggregator, search feed or tag stream | 140 |
| `cert` National cyber agency or CSIRT | 92 |
| `tech-press` Technology and security press | 47 |
| `affected` Affected organisation's own site | 32 |
| `security-vendor` Security, WAF, CDN or detection vendor | 29 |
| `registry` Vulnerability registry | 28 |
| `reference` Reference work | 24 |
| `project` The open-source project and its foundation | 16 |
| `social` Social platform post or account | 16 |
| `community` Forum, mailing list, gist or repository | 13 |
| `weaponisation` Where exploits, scanners and detections are published | 12 |
| `research` Security researcher or research firm | 9 |
| `ai-lab` AI lab | 3 |
| `government` Other government body | 2 |
| `cloud` Cloud or hosting provider | 1 |
| `tool` Tool published for the incident | 1 |

## What we can and cannot read

Every check classifies the answer it got. A page the watcher cannot read stays on the list: the challenge page's hash is the record, and the gap is published.

| Access | Pages | Means |
|---|---|---|
| `open` | 735 | Served the content to an anonymous browser. |
| `paywalled` | 15 | Subscription press we hold no licence for. Either it served a subscription or registration wall instead of the content, or (for a publisher marked paywall in its page.json) it refused the anonymous browser with 401 or 403 before any wall. Counted apart from bot-challenge since 22 October 2026. |
| `bot-challenge` | 59 | Served a bot or browser challenge (Cloudflare, Akamai, DataDome, PerimeterX, Vercel). The challenge page's hash is kept as the record. |
| `login-wall` | 0 | Wants a signed-in account (some social posts). |
| `geo-blocked` | 0 | Refused because of where the request came from. |
| `gone` | 8 | 404 or 410: the page no longer exists at this address. |
| `down` | 61 | 5xx, a timeout, a DNS failure or a refused connection: the site is not answering. For the affected sites this is the finding. |
| `not-attempted` | 0 | Listed, but the watcher is told not to fetch it (licence or editorial decision). |

Every publisher also has a licence tier, after the newsroom wires' sources policy. The vault keeps what was served either way; the tier governs what a site page shows of it.

| Tier | Publishers | What a site page may show |
|---|---|---|
| **A** | 73 | open or public-sector: keep and show |
| **B** | 523 | quote up to 25 words and link |
| **C** | 15 | link only |

## Graphs: one grammar at every altitude

Every graph in the vault uses the grammar in `taxonomy/verbs.json` (22 verbs): an edge is a verb with a named inverse, and there is no generic association edge ([graphs.sgit.ai](https://graphs.sgit.ai/)). The world graph alone has 1620 nodes and 3219 edges. Entities (a CVE id, a PHP version, an organisation with this site's actor ids, a term with its translations) are where the altitudes join, and where the vault joins this site. What changed on a page is answered by a query over the change section, not by comparing two screenshots; the extractor is deterministic.

| Altitude | What it describes |
|---|---|
| **world** | country, sector, publisher, page, language: where the watched pages sit (index/world.json) |
| **watch** | run, check, page, access, snapshot: what the watcher did and saw (runs/**/graph.json) |
| **document** | snapshot, block, entity: what one snapshot of a page says (graph/**/.json) |
| **change** | change, block, entity: what moved between two snapshots (graph/**/.json, section change) |

## The runs

A run captures the pages that are due: hourly for the story, daily for background pages about earlier incidents. Feeds and APIs are fetched without a browser; everything else goes through Chromium at 1280 wide. The first run was a diff against the evidence vault's morning captures, imported as this vault's first snapshots.

| Run (UTC) | Due | Watched | Changed | Access |
|---|---|---|---|---|
| `20261023T124024Z` | 1 | 913 | 1 | open 1 |
| `20261023T124018Z` | 1 | 913 | 1 | open 1 |
| `20261023T123902Z` | 1 | 913 | 1 | open 1 |
| `20261023T123852Z` | 1 | 913 | 1 | open 1 |
| `20261023T123836Z` | 1 | 911 | 1 | open 1 |
| `20261023T123808Z` | 1 | 910 | 1 | open 1 |
| `20261023T123801Z` | 1 | 910 | 1 | open 1 |
| `20261023T123751Z` | 1 | 910 | 1 | open 1 |
| `20261023T123736Z` | 1 | 910 | 1 | open 1 |
| `20261023T080331Z` | 799 | 870 | 555 | open 673, bot-challenge 53, down 53, paywalled 15, gone 5 |
| `20261023T080157Z` | 32 | 870 | 19 | open 20, down 8, bot-challenge 4 |
| `20261023T012042Z` | 759 | 826 | 500 | open 671, bot-challenge 49, down 19, paywalled 14, gone 6 |
| `20261023T011949Z` | 28 | 826 | 12 | open 22, down 5, bot-challenge 1 |
| `20261022T203448Z` | 709 | 773 | 442 | open 631, bot-challenge 45, down 15, paywalled 13, gone 5 |
| `20261022T203355Z` | 25 | 773 | 15 | open 17, down 7, bot-challenge 1 |
| `20261022T191736Z` | 1 | 763 | 1 | open 1 |
| `20261022T191727Z` | 1 | 763 | 1 | open 1 |
| `20261022T191720Z` | 2 | 763 | 2 | open 2 |
| `20261022T191713Z` | 2 | 763 | 2 | open 2 |
| `20261022T191536Z` | 1 | 757 | 1 | open 1 |
| `20261022T191523Z` | 1 | 757 | 1 | open 1 |
| `20261022T191510Z` | 1 | 757 | 1 | open 1 |
| `20261022T191433Z` | 1 | 757 | 1 | open 1 |
| `20261022T191421Z` | 2 | 757 | 1 | open 2 |
| `20261022T191411Z` | 5 | 757 | 5 | open 5 |
| `20261022T191400Z` | 1 | 757 | 0 | bot-challenge 1 |
| `20261022T183624Z` | 27 | 748 | 27 | open 27 |
| `20261022T183616Z` | 2 | 748 | 2 | open 2 |
| `20261022T181608Z` | 632 | 715 | 454 | open 549, bot-challenge 48, down 19, paywalled 12, gone 4 |
| `20261022T181440Z` | 33 | 519 | 33 | open 33 |
| `20261022T175253Z` | 14 | 486 | 14 | open 14 |
| `20261022T175100Z` | 11 | 472 | 11 | open 9, down 2 |
| `20261022T171501Z` | 384 | 461 | 297 | open 326, bot-challenge 28, down 20, paywalled 8, gone 2 |
| `20261022T171425Z` | 52 | 381 | 48 | open 52 |
| `20261022T171339Z` | 52 | 381 | 52 | open 52 |
| `20261022T150854Z` | 143 | 328 | 143 | open 119, bot-challenge 15, down 5, gone 4 |
| `20261022T145444Z` | 1 | 328 | 1 | open 1 |
| `20261022T142033Z` | 184 | 184 | 125 | open 157, bot-challenge 18, down 7, paywalled 1, gone 1 |

## Tips

A tip is a claim that reached the newsroom from outside, recorded with how it arrived, what it says, the pages added to watch it, and what has to be checked before anything on this site relies on it. Its status uses this site's words.

Tip 2026-10-22/001 · received 2026-10-22T14:38:00+02:00 · reported

Their browser extension, php2shell-checker, was just approved on the Chrome Web Store. It checks whether a website runs outdated PHP or a supported PHP application such as WordPress. They describe it as privacy friendly and read-only, with nothing leaving the browser, and aimed at CISOs in the SME segment as easier than running scripts.

**Watched as** `us/tool/chrome-web-store/php2shell-checker`. **To check:** The publisher named on the store listing, and whether it matches who made the claim; The permissions the listing and the manifest ask for, against 'read-only, nothing leaves the browser'; The version history and user count, run by run; Whether it detects the fixed versions (8.5.12 and the backports) correctly.

## The tools

The watcher is in the vault, next to what it wrote: `analyse.py`, `capture_batch.mjs`, `collectors.py`, `discover.py`, `extract.py`, `foreign.py`, `import_evidence.py`, `lib.py`, `migrate_impact_cc.py`, `probe.py`, `publishers_seed.py`, `seed_impact.py`, `seed_world.py`, `series.py`, `watch.py`.

python3 tools/watch.py run [--all] [--only ] [--limit N] [--commit] [--push] python3 tools/discover.py scan # feeds to candidate publishers python3 tools/discover.py promote --limit 30 python3 tools/watch.py add  --cc gb --sector news --publisher bbc The other vaults behind this site are on [the vaults](../index.html). The evidence vault, where the story was assembled by hand on the morning of 22 October, is [opened here](../../admin/vault/index.html).


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html
