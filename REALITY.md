# What exists

By domain, kept current by whoever ships. A thing not listed here does not exist, whatever the brief says.

## Evidence
- A private sgit vault with the protocol in its README; 144 sources, 137 captures, 857 hashed files at commit 200d08971937; four agents have written to it. Not published; its manifest with hashes is `data/sources.json`.
- `admin/build/export_vault.py` exports the manifest, the vault head, the per-agent claims and timeline files and the NCSC-NL inventory counts from a clone of the vault.

## Data, authored for this site by the agent claude-story-site
- `data/story.json`, `claims.json`, `timeline.json`, `numbers.json`, `agencies.json`, `affected.json`, `exploitation.json`, `actors.json`, `roles.json`, `billing.json`, `versions.json`.
- Every row cites vault slugs; the gate refuses an unknown slug.

## Pages
- The front page; the two flaws; the timeline; who found it; how disclosure broke; exploitation signals; if you run PHP; every claim; the numbers; the agencies; affected systems and the full inventory; every source; the graph; six briefings; the method; the team; the billing model; the reading account, top-up and topped-up; the brief; corrections; the release history; admin and engineering; `llms.txt`; a markdown twin per page.

## Readers (v0.3.0)
- `data/personas.json`: fifteen readers in five groups (understand, decide, communicate, act, study) and three depths (plain English, some technical, deeply technical), each with a thirty-second answer, needs, skips and a reading path. The gate checks every path.
- `data/glossary.json`: 40 terms; the build links the first use of each on every page (outside links, code and headings) with a hover card, and links every CVE ID (the two php2shell IDs to their cards, earlier ones to their captured records or cve.org).
- `data/plain.json`: the front page's headline, five questions, five moments and a plain-English line for every technical page; every fact cites vault slugs.
- Pages: Start here (the readers mapped), Explained from scratch, the glossary, and briefings for a curious reader, a website owner and a project manager.
- The reader bar (`assets/site.js`, `assets/personas.js`): the chosen reader and the pages read are kept in localStorage only.
- Not built: persona-specific rewrites of the evidence pages themselves; a reader test with real people from each group.

## Versions, facts, search (v0.3.2)
- `data/sections.json`, the section ledger: every briefing, front-page section, story page and fact is hashed on every build and gets a new version only when its reader-facing text changes, naming the release that wrote it. History before v0.3.2 reconstructed from git by `admin/build/seed_ledger.py`.
- A history page with diffs per section (`versions/`), the release-by-section matrix, a page per fact with its timeline (`facts/`), what's new with a since-your-last-visit marker, an Atom feed, the fact pipeline, the editor's interview in his own words.
- `sitemap.xml`, `robots.txt`, Open Graph card, JSON-LD (NewsArticle, BreadcrumbList, WebSite); `data/seo.json` takes a Google Search Console verification token.
- Not built: new evidence since the vault's last capture (11:34Z): compromise reports need a vault session to capture them.

## Build, gate, release
- `admin/build/build.py`: deterministic, standard library only.
- `admin/build/validate.py`: links, orphans, twins, llms.txt, citations, determinism, em-dashes, credential shapes, external resources, version consistency.
- `admin/build/release.sh`: bump, build, validate, tripwire, push to dev, verify live.

## Billing
- SG Meter v1.3.1 vendored and running on every page with this site's prices; no payment link configured, so the top-up page runs the simulated cart.
- Everything under "designed" on the billing page: not built.

## Not built
- A verifier agent run; a review folder; a second model reading the vault; a fractal graph; a Stripe link; tests beyond the gate.
