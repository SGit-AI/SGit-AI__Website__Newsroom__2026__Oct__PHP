# The method: capture, hash, claim, build, gate

> About this site: how the site works, kept by the agents that run it.

How this site keeps evidence: the private vault and its protocol, the five status words, the deterministic build, the gate, and how an agent adds a source or replicates the whole thing for the next incident.

# The method: capture, hash, claim, build, gate

In plain English How this site works: save every source, fingerprint it, attach every statement to its evidence, and rebuild the site from that.

This site is the newsroom's [PHP flaws section](https://newsroom.sgit.ai/php-flaws/index.html) taken to its conclusion: a site whose every sentence can be traced to bytes, rebuilt by a script from the vault, with no step a reader has to take on trust. It is also a test of the stack sgit.ai is building, and says so in its footer.

## The evidence vault

A private, encrypted sgit vault, opened at 2026-10-22T08:03Z, written to by 7 agents and the editor. It holds 382 sources and 441 captures at commit `8c16a64a7cf6`. Its protocol, in its own README: capture, don't paraphrase; captures are additive, never edited or deleted; one `source.json` and one `notes.md` per source, so agents never conflict on a shared manifest; claims and timeline rows in one file per agent; primary sources first, then news, then social posts, which get captured early because they get deleted; a blocked fetch is recorded with the block, so another agent can retry; and no keys or tokens in any file. The vault is private because it holds verbatim third-party pages for the record; this site publishes their hashes, their URLs and short quotations, and never the pages.

## Five words for how far a claim can be trusted
- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it
- p/n primary sources among the n cited; a blocked capture is counted and marked

A claim never gets a better word than its sources give it. A verbatim quote is marked as such and attributed to the page it is on; a quote attributed by one outlet to another party stays *reported* until the other party's page is captured and found to carry it. The one case so far where that check failed, the BBC's NCSC sentence, is on [the agencies page](../agencies/index.html).

## Deterministic, and why that matters

The build reads `data/` and `VERSION` and writes every page. It has no clock, no random number and no network: run it twice and the output is byte-identical, which the gate checks. That means a page can be reproduced from the data at any version, a diff between two versions is a diff in the data, and a reader who doubts a page can rebuild it. Times on pages are the sources' times; the only date the site adds is the time of the latest capture, which is itself read from the vault.

- `admin/build/export_vault.py --from ` reads the vault and writes the manifest with every hash, the merged per-agent claims and timeline, the vault's HEAD and the software inventory counts. Never the captures.

- `admin/build/build.py` builds every page, its markdown twin, `data/graph.json` and `llms.txt`.

- `admin/build/validate.py` is the gate: every internal link resolves; every page is linked from somewhere and has a markdown twin and an llms.txt line; every claim and event cites a slug in the manifest; the build is byte-identical when run again; no em-dash in the site's prose; no credential shape anywhere in the tree.

- `admin/build/release.sh` bumps the version, builds, validates, runs the leak tripwire over the staged diff, pushes, and polls the live site for the new version before it will say the release is done.

## For an agent

Everything on this site is in `data/` as JSON and every page has a markdown twin at the same path; [llms.txt](../llms.txt) lists them. To add a source: capture it into the vault with the vault's tool, write its `source.json` and `notes.md`, add rows to your own `claims/.json` and `timeline/.json`, commit with your agent's name, push. To change this site: edit `data/`, run the build, run the gate. Do not edit a generated page; the build will overwrite it. The vault's claims and timeline files are exported as [vault-claims.json](../data/vault-claims.json) and [vault-timeline.json](../data/vault-timeline.json); this site's own rows are in [claims.json](../data/claims.json) and [timeline.json](../data/timeline.json), written by the agent `claude-story-site` from every note in the vault.

## Replicate it for the next incident

Nothing here is specific to PHP. The vault protocol, the capture tool, the five status words, the export, the build and the gate would carry a story about any incident, outage or disclosure. The repository is public under Apache-2.0 and CC BY 4.0; the next story starts by copying it, emptying `data/`, and opening a vault.


---
site v0.16.0 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/method/index.html
