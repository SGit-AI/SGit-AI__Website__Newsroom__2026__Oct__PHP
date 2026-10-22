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

## Build, gate, release
- `admin/build/build.py`: deterministic, standard library only.
- `admin/build/validate.py`: links, orphans, twins, llms.txt, citations, determinism, em-dashes, credential shapes, external resources, version consistency.
- `admin/build/release.sh`: bump, build, validate, tripwire, push to dev, verify live.

## Billing
- SG Meter v1.3.1 vendored and running on every page with this site's prices; no payment link configured, so the top-up page runs the simulated cart.
- Everything under "designed" on the billing page: not built.

## Not built
- A verifier agent run; a review folder; a second model reading the vault; a fractal graph; a Stripe link; tests beyond the gate.
