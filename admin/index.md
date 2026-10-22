# Admin and engineering

How this site is built, the checks in its gate, where things are, the reality file and the honest column.

# Admin and engineering

How the site is built, what the gate checks, where things are, and what exists against what the brief asked for. The site is static HTML built by one Python script with no dependencies beyond the standard library, deployed by GitHub Pages from the `dev` branch of [the repository](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP).

## Where things are

| Thing | Where |
|---|---|
| The version, one number | `VERSION`; shown in the top bar; bumped by the release script on every push |
| The data every page is built from | `data/*.json`; exported from the vault by `admin/build/export_vault.py` and authored by the story agent |
| The build | `admin/build/build.py`; deterministic; writes every page, twin, the graph and llms.txt into the repository root |
| The gate | `admin/build/validate.py`; the checks below; fails the release |
| The release | `admin/build/release.sh`; bump, build, validate, tripwire, push to dev, verify live |
| The brief and its corrections | `admin/content/briefs/`, `BRIEF-CORRECTIONS.md` |
| The reality file | `REALITY.md`: what exists, by domain, kept current by whoever ships |
| The meter | `assets/components/sg-meter/v1/v1.3/v1.3.1/` and `assets/components/base/v1/v1.0/v1.0.0/`, vendored, immutable paths |
| Credentials | none in the repository; the vault key and the push token live in the agents' sessions and in a gitignored tier, scanned by the tripwire |

## The admin section
- [The board](board/index.html): the work, as rows.
- [Roles](roles/index.html): who does what, and how an agent joins.
- [Briefs](briefs/index.html): the build briefs, in full.
- [The vault, opened](vault/index.html): the read key and the browser link.
- [Who reads this site](telemetry/index.html): the telemetry lane and its counts.

## The gate

| Check | What it would catch |
|---|---|
| Every internal link resolves against the real file tree | a link to a page that does not exist |
| Every page is linked from at least one other page | a page nothing can find, which is the same as unpublished |
| Every page has a markdown twin and a line in llms.txt | a page an agent cannot read |
| Every claim, event, number, agency and signal cites only slugs in the manifest | a citation to nothing |
| The build is byte-identical when run twice | a clock, a random number or an unsorted set in the build |
| No em-dash in the site's own prose | the estate's writing rule; third-party titles are exempt |
| No sgit credential shape, private-key marker or cloud key prefix anywhere in the tree | a vault key in a data file |
| No script, stylesheet or image loaded from another origin | a dependency fetched at run time |
| data/ parses and every claim status is one of the five words | a sixth word that means nothing |

## The reality file

## What exists

By domain, kept current by whoever ships. A thing not listed here does not exist, whatever the brief says.

### Evidence

- A private sgit vault with the protocol in its README; 144 sources, 137 captures, 857 hashed files at commit 200d08971937; four agents have written to it. Not published; its manifest with hashes is `data/sources.json`.

- `admin/build/export_vault.py` exports the manifest, the vault head, the per-agent claims and timeline files and the NCSC-NL inventory counts from a clone of the vault.

### Data, authored for this site by the agent claude-story-site

- `data/story.json`, `claims.json`, `timeline.json`, `numbers.json`, `agencies.json`, `affected.json`, `exploitation.json`, `actors.json`, `roles.json`, `billing.json`, `versions.json`.

- Every row cites vault slugs; the gate refuses an unknown slug.

### Pages

- The front page; the two flaws; the timeline; who found it; how disclosure broke; exploitation signals; if you run PHP; every claim; the numbers; the agencies; affected systems and the full inventory; every source; the graph; six briefings; the method; the team; the billing model; the reading account, top-up and topped-up; the brief; corrections; the release history; admin and engineering; `llms.txt`; a markdown twin per page.

### Build, gate, release

- `admin/build/build.py`: deterministic, standard library only.

- `admin/build/validate.py`: links, orphans, twins, llms.txt, citations, determinism, em-dashes, credential shapes, external resources, version consistency.

- `admin/build/release.sh`: bump, build, validate, tripwire, push to dev, verify live.

### Billing

- SG Meter v1.3.1 vendored and running on every page with this site's prices; no payment link configured, so the top-up page runs the simulated cart.

- Everything under "designed" on the billing page: not built.

### Admin section and telemetry (v0.2.3)

- The board, roles, briefs, the evidence vault's public read key with a browser link, and the telemetry page, all from `data/admin.json`, `data/telemetry.json` and `admin/content/briefs/`.

- `assets/telemetry.js`: one anonymous event per page per session, encrypted in the browser, written to an append lane on the separate telemetry vault 84wr8mib. `admin/build/telemetry_drain.py` drains it and writes counts to `data/telemetry-report.json`. Tested end to end from the CLI before shipping.

### Questions and the catalogue (v0.2.6)

- `data/questions.json`, kept by the librarian (librarian@php.newsroom): ten questions readers ask, each with a short answer to paste back, the answer with its sources, and the pages that carry it; built as `/questions/` and one page per question. The gate refuses an unknown slug or a missing page in it.

- The same page lists articles readers have seen that the vault has not captured (The Times, 22 October), which are never cited until captured, and a catalogue of every page with what it answers.

### Pricing and second readings (v0.2.10)

- Every content page is metered: `data/billing.json` `pricing` sets a base per content type (article 6p, briefing 5p, analysis 3p, story 2p, evidence and site 1p) and four freshness tiers (fresh x2 up to a day, new x1.5 up to a week, current x1 up to 30 days, archive x0.5); evidence and site pages do not decay. The build writes the full price table; an inline script on each page picks the tier from the page's date in the reader's browser. Only the account, top-up and topped-up pages are unmetered. Checked in Chromium at three dates.

- `/readings/`: Perplexity's notes of 22 October in full and credited (`admin/content/external/`), compared with the vault in `data/readings.json`; its uncaptured sources are listed for capture, not cited.

- The newsroom's review of the site at v0.2.2 is published as received on the briefs page, with a triage against v0.2.10; its open changes are board items 022 to 032.

### Not built

- A verifier agent run; a review folder; a second model reading the vault; a fractal graph; a Stripe link; tests beyond the gate.

## The honest column

- **Not measured:** the editor's time and the inference cost behind each agent run.

- **Not yet run:** the verifier role, which re-reads every claim against its capture text.

- **Not reviewed:** the playbook and the blast-radius section are the site's own synthesis of agency advice and have not been reviewed by a security team.

- **Not live:** everything on the billing page under "designed".

- **No tests beyond the gate:** the build has no unit tests; the gate is the whole automated enforcement surface.

- **No review folder yet:** the estate's guidance asks for `review/` from the first commit; this repository starts it from its next change.


---
site v0.2.13 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/index.html
