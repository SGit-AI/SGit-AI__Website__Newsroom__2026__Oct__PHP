# The source watch: every outside source on php2shell, watched and snapshotted

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The public source-watch vault: 328 pages from 175 publishers in 38 countries, re-read on a schedule, a snapshot kept on every change and every snapshot a graph. Its read key, the vault embedded, and what is in it.

[Vaults](../index.html) / The source watch

# The source watch: every outside source on php2shell, watched and snapshotted

A vault that does one thing. It watches every outside source on the story, 328 pages from 175 publishers in 38 countries, and on each run records what access it had and keeps a new snapshot whenever the content changed: the text, a screenshot, the HTML as served and as rendered, the headers and the sha256 of each, and a graph of what the page says and what changed since the last look. A small, focused Wayback Machine whose diffs are graphs. Run by **researcher@php.newsroom**; public, read-only.

The vault in the official UI, opened read-only with the published key. **Click the image to open the real one ↗**

Open it yourself. The read key is the whole credential, and it is published on purpose.
Read key: sgit_public_read_d0dc218a9bd0a85fc1737129c590a1d7bfafe82d444707f438810140ebaab277:oq9gflln
In the official UI: open it read-only in a new tab ↗ · From the command line: sgit clone sgit_public_read_d0dc218a9bd0a85fc1737129c590a1d7bfafe82d444707f438810140ebaab277:oq9gflln
A read key decrypts and cannot write; it is derived one way from the vault key, which is not published and never will be.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_d0dc218a9bd0a85fc1737129c590a1d7bfafe82d444707f438810140ebaab277%3Aoq9gflln) The vault has no app of its own yet, so it opens in the vault browser. It holds 3,711 files; the browser decrypts the folder tree before it lists it, so the first open takes minutes. `sgit clone` is the fast way in.

## What is in it

328pages watched175publishers38countries32languages440snapshots kept440graphs3runs3711files in the vault

Counts read from the vault's `index/counts.json`, `runs/` and `tips/` at head `9ba748ac18aa` by `admin/build/export_watch.py`; no capture is copied to this site. The vault's latest commit: *researcher@php.newsroom: tip 2026-10-22/001 (php2shell Checker extension), noise filter, run 2 over the 143 new pages, discovery scan*

## Raw and analysis are separate trees

Raw is what was served; analysis is what the watcher made of it, and it can be regenerated from raw plus the vocabularies plus the tools. That rule is how you tell the two apart. A snapshot in `raw/` is never edited or deleted: a new look at the page makes a new folder, and only when something changed. Every check, changed or not, is still a line in `checks/` with its status, access and hashes.

sources/////page.json raw////// text.txt screenshot.jpg page.html.gz rendered.html.gz headers.json meta.json provenance.json raw/...//checks/.jsonl graph/...//.json snapshot and change runs///// run.json graph.json changes.md index/ state/ taxonomy/ tips/ tools/ ## Country, then sector, then publisher, then page Country is where the publisher is based (`eu` for EU institutions, `int` for publishers with no single home, such as php.net); language is a property of the page. Sector is what kind of organisation publishes it, one per publisher; it classifies the publisher, never a claim.

| Country | Pages |
|---|---|
| `us` | 148 |
| `int` | 35 |
| `gb` | 25 |
| `fr` | 18 |
| `nl` | 14 |
| `ch` | 7 |
| `de` | 7 |
| `au` | 6 |
| `jp` | 6 |
| `eu` | 5 |
| `fi` | 5 |
| `in` | 5 |

| Sector | Pages |
|---|---|
| `cert` National cyber agency or CSIRT | 63 |
| `aggregator` News aggregator, search feed or tag stream | 54 |
| `news` General news | 52 |
| `tech-press` Technology and security press | 33 |
| `registry` Vulnerability registry | 28 |
| `security-vendor` Security, WAF, CDN or detection vendor | 21 |
| `project` The open-source project and its foundation | 16 |
| `affected` Affected organisation's own site | 15 |
| `social` Social platform post or account | 15 |
| `reference` Reference work | 10 |
| `research` Security researcher or research firm | 9 |
| `community` Forum, mailing list, gist or repository | 6 |
| `ai-lab` AI lab | 3 |
| `cloud` Cloud or hosting provider | 1 |
| `government` Other government body | 1 |
| `tool` Tool published for the incident | 1 |

## What we can and cannot read

Every check classifies the answer it got. A page the watcher cannot read stays on the list: the challenge page's hash is the record, and the gap is published.

| Access | Pages | Means |
|---|---|---|
| `open` | 277 | Served the content to an anonymous browser. |
| `paywalled` | 1 | Served a subscription or registration wall instead of the content. We hold no licence to go past it. |
| `bot-challenge` | 33 | Served a bot or browser challenge (Cloudflare, Akamai, DataDome, PerimeterX, Vercel). The challenge page's hash is kept as the record. |
| `login-wall` | 0 | Wants a signed-in account (some social posts). |
| `geo-blocked` | 0 | Refused because of where the request came from. |
| `gone` | 5 | 404 or 410: the page no longer exists at this address. |
| `down` | 12 | 5xx, a timeout, a DNS failure or a refused connection: the site is not answering. For the affected sites this is the finding. |
| `not-attempted` | 0 | Listed, but the watcher is told not to fetch it (licence or editorial decision). |

Every publisher also has a licence tier, after the newsroom wires' sources policy. The vault keeps what was served either way; the tier governs what a site page shows of it.

| Tier | Publishers | What a site page may show |
|---|---|---|
| **A** | 64 | open or public-sector: keep and show |
| **B** | 97 | quote up to 25 words and link |
| **C** | 14 | link only |

## Graphs: one grammar at every altitude

Every graph in the vault uses the grammar in `taxonomy/verbs.json` (22 verbs): an edge is a verb with a named inverse, and there is no generic association edge ([graphs.sgit.ai](https://graphs.sgit.ai/)). The world graph alone has 589 nodes and 1190 edges. Entities (a CVE id, a PHP version, an organisation with this site's actor ids, a term with its translations) are where the altitudes join, and where the vault joins this site. What changed on a page is answered by a query over the change section, not by comparing two screenshots; the extractor is deterministic.

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
| `20261022T150854Z` | 143 | 328 | 143 | open 119, bot-challenge 15, down 5, gone 4 |
| `20261022T145444Z` | 1 | 328 | 1 | open 1 |
| `20261022T142033Z` | 184 | 184 | 125 | open 157, bot-challenge 18, down 7, paywalled 1, gone 1 |

## Tips

A tip is a claim that reached the newsroom from outside, recorded with how it arrived, what it says, the pages added to watch it, and what has to be checked before anything on this site relies on it. Its status uses this site's words.

Tip 2026-10-22/001 · received 2026-10-22T14:38:00+02:00 · reported

Their browser extension, php2shell-checker, was just approved on the Chrome Web Store. It checks whether a website runs outdated PHP or a supported PHP application such as WordPress. They describe it as privacy friendly and read-only, with nothing leaving the browser, and aimed at CISOs in the SME segment as easier than running scripts.

**Watched as** `us/tool/chrome-web-store/php2shell-checker`. **To check:** The publisher named on the store listing, and whether it matches who made the claim; The permissions the listing and the manifest ask for, against 'read-only, nothing leaves the browser'; The version history and user count, run by run; Whether it detects the fixed versions (8.5.12 and the backports) correctly.

## The tools

The watcher is in the vault, next to what it wrote: `capture_batch.mjs`, `discover.py`, `extract.py`, `import_evidence.py`, `lib.py`, `publishers_seed.py`, `seed_world.py`, `watch.py`.

python3 tools/watch.py run [--all] [--only ] [--limit N] [--commit] [--push] python3 tools/discover.py scan # feeds to candidate publishers python3 tools/discover.py promote --limit 30 python3 tools/watch.py add  --cc gb --sector news --publisher bbc The other vaults behind this site are on [the vaults](../index.html). The evidence vault, where the story was assembled by hand on the morning of 22 October, is [opened here](../../admin/vault/index.html).


---
site v0.7.0 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/vaults/source-watch/index.html
