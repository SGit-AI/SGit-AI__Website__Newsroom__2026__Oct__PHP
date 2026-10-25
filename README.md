# SGit-AI__Website__Newsroom__2026__Oct__PHP

> **This repository is closing (the editor, 25 October 2026).** The site is now six repositories, each with its own gate, release and address; the brief every agent must read is on the team site: https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__brief__the-split-for-every-agent/ (every repository is public: read any of them; write only the ones your card names, and ask the editor for each). **Do not start new work here.** Until dev flips the direction (step A: the records, the data and the sources move out and this repository only builds; board row 336), a wake that must release writes here as its card says, and nothing else; after the flip, only dev's chain commits here; after the cutover, this repository is archived read-only as `…__PHP__v1`.

The repository for **php.oct.2026.newsroom.sgit.ai**: a fact-driven, agent-run tracker for the two PHP flaws of October 2026 (CVE-2026-109618 and CVE-2026-109619, "php2shell"), built from a private evidence vault, deterministic, with provenance on every line.

- Deployed by `.github/workflows/pages.yml` on every push to `dev` (Pages source: GitHub Actions); the workflow runs the gate first.
- The site is static HTML in the repository root, built by `admin/build/build.py` from `data/*.json` and `VERSION`, deployed by GitHub Pages from the `dev` branch.
- `admin/build/export_vault.py --from <vault clone>` refreshes `data/` from the evidence vault (manifest with hashes, per-agent claims and timeline, the NCSC-NL inventory). The captures themselves are never copied here.
- `admin/build/validate.py` is the gate; `admin/build/release.sh "<what changed and why>"` is the only way a release happens.
- Pipeline: https://php.oct.2026.newsroom.sgit.ai/status/index.html shows each newsroom site's deploy runs and the version each serves, read from GitHub's public API with no credential. Badge: ![deploy](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP/actions/workflows/pages.yml/badge.svg?branch=dev)

**Agents: read [AGENTS.md](AGENTS.md) first.** Push work in progress to your own branch; when it is finished and the gate passes, release it to dev yourself with `admin/build/release.sh` (the editor's rule, 23 October 2026).

## Releasing when several agents push to `dev`

- Any agent releasing its own finished work runs `admin/build/release.sh "<what changed and why>"` with the changes uncommitted (or committed locally, not pushed). It fetches `origin/dev` first and takes in whatever other agents released, so your release is one commit on top of theirs and its version is the next one after theirs.
- Conflicts in files the build writes (listed in `admin/build/outputs.txt`) and in `VERSION` and `data/versions.json` resolve to origin's side, since the script rebuilds and re-bumps them. A conflict in a source file (`data/*.json`, `admin/build/*.py`, `assets/`, content) stops the release with exit 3 and your work left uncommitted: merge it by hand and run the script again.
- If the push is rejected because another release landed while yours was building, the script undoes its bump, takes that release in and goes again, up to five times.
- Never edit a generated `.html` or `.md` page by hand: the next release from any agent overwrites it.
- The Pages workflow queues deploys and never cancels one that has started. GitHub keeps one waiting run per site, so a push overtaken while it waits shows as cancelled; the newer run behind it deploys its commit too, and /status/ marks such runs as superseded.
- The brief is in `admin/content/briefs/`; corrections in `BRIEF-CORRECTIONS.md`; what exists in `REALITY.md`.
- Every page has a markdown twin; `llms.txt` lists them. Status words: confirmed, reported, disputed, contradicted, unverified, defined on the method page.

This site's own text, tables and data are CC BY 4.0 and its code Apache-2.0. Everything else belongs to its authors and is credited to its source: quoted words are theirs and linked, the NCSC-NL inventory is EUPL-1.2, and no third-party page is reproduced. Part of the sgit.ai network; the newsroom's own section on the story is at https://newsroom.sgit.ai/php-flaws/index.html.
