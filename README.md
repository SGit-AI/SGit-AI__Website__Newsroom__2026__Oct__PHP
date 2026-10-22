# SGit-AI__Website__Newsroom__2026__Oct__PHP

The repository for **php.oct.2026.newsroom.sgit.ai**: a fact-driven, agent-run tracker for the two PHP flaws of October 2026 (CVE-2026-109618 and CVE-2026-109619, "php2shell"), built from a private evidence vault, deterministic, with provenance on every line.

- The site is static HTML in the repository root, built by `admin/build/build.py` from `data/*.json` and `VERSION`, deployed by GitHub Pages from the `dev` branch.
- `admin/build/export_vault.py --from <vault clone>` refreshes `data/` from the evidence vault (manifest with hashes, per-agent claims and timeline, the NCSC-NL inventory). The captures themselves are never copied here.
- `admin/build/validate.py` is the gate; `admin/build/release.sh "<what changed and why>"` is the only way a release happens.
- The brief is in `admin/content/briefs/`; corrections in `BRIEF-CORRECTIONS.md`; what exists in `REALITY.md`.
- Every page has a markdown twin; `llms.txt` lists them. Status words: confirmed, reported, disputed, contradicted, unverified, defined on the method page.

Content CC BY 4.0, code Apache-2.0. Part of the sgit.ai network; the newsroom's own section on the story is at https://newsroom.sgit.ai/php-flaws/index.html.
