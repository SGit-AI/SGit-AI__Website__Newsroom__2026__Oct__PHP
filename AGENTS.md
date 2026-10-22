# How to work on this site: guidance for every agent

Read this before your first commit, and again when the editor says it changed. It is short on purpose. Written by dev@php.newsroom at the editor's request on 22 October 2026; the editor's words: "push fast and furious to your own branches, have quality guidance, read coding.sgit.ai and nfrs.sgit.ai, take the security requirements into account, so that dev can see what everyone is doing and bring it in sooner rather than later."

## 1. Push to your own branch, early and often

- Work on a branch of your own: `claude/<what>-<session>` (the estate's convention, coding.sgit.ai process rules) or `<role>/<topic>` (for example `factcheck/desk`). One branch per piece of work.
- **Push after every step that builds**, and at least every 30 minutes while you work. Work in progress is welcome: say so in the commit message ("not a release; run 1 in progress"). A branch nobody can see cannot be merged, reviewed or built on.
- **Take in dev often**: `git fetch origin dev && git merge origin/dev`, then rebuild (`python3 admin/build/build.py`). Never hand-merge a generated page; resolve the source and rebuild. Never rewrite history on a branch you have pushed.
- **Do not push to `dev`.** dev@php.newsroom carries branches into dev, resolves what collides, runs the gate and releases (`admin/build/release.sh`). The exception is an explicit instruction from the editor. This is coding.sgit.ai's rule too: agents never push to dev directly.
- Say what is for dev in the commit: `Not a release: for dev@php.newsroom to carry into the next release.` and an `Agent: <your name>` line.

## 2. What a good commit contains

- Source, not output: `data/*.json`, `admin/content/`, `admin/build/*.py`, `assets/`. The pages, their markdown twins, `llms.txt`, `sitemap.xml` and `feeds/` are generated; `admin/build/outputs.txt` lists every generated file.
- **One file per agent per concern**, so two agents rarely touch the same lines: your own `admin/content/...` file, your own data file, your own block at the end of `build.py` with a header naming you.
- Board rows: add yours at the end of `data/admin.json`; expect dev@ to renumber them if another agent took the same ids first. Never edit or renumber someone else's row.
- A brief before a feature (`admin/content/briefs/`), then the work. Corrections go in `BRIEF-CORRECTIONS.md`, above the mistake. What exists goes in `REALITY.md`.
- The gate passes on your branch before you push (`python3 admin/build/validate.py`), or the commit says it does not and why.

## 3. Quality: coding.sgit.ai

Read https://coding.sgit.ai/ (and /rules/ for the 31 rules with their measured compliance). What applies most here:

- One idea per file and per function; a comment says why, not what; the file's first lines say what it is and where its brief is.
- A single source of truth, enforced by structure: a number on a page is generated from the data file that holds it, never typed twice.
- The build is deterministic and has no clock: the same data gives byte-identical pages. Python standard library only in `admin/build/`.
- Follow the practice the code shows when it differs from a stated rule, and say so.
- No mocks and no patches in tests; test against the real thing (the gate builds the whole site; browser checks run real Chromium).

## 4. Non-functional requirements: nfrs.sgit.ai

Read https://nfrs.sgit.ai/ and its topic map. Here that means:

- **Link the measurement, never restate it; generate or date every number.** Every figure on this site comes from a captured source or a data file, with its as-of time.
- Documentation is part of the work: every page has a markdown twin and a line in `llms.txt`; every data file is classified in `data/layers.json`.
- Version control and explainability: every release has a version and a sentence; every section and fact has a history (`data/sections.json`).
- Resilience: a page works without JavaScript wherever it can, and says what needs JavaScript where it cannot.

## 5. Security requirements

From sgit.ai/security and this site's own rules; the gate and `release.sh` check some of them, the rest are on you:

- **Never commit a secret**: no vault key (`sgit_private_vault_…`), private key, access token, enum key or passphrase, in any repository, page, log or commit message. Publishable by design: read keys (`sgit_public_read_…`), append tokens (write-only), public keys. If one leaks, say so at once; the rotation runbook is on sgit.ai.
- **Secrets travel sealed**: to a person's key on pki.sgit.ai, after checking the fingerprint, never in plain text in chat or a file.
- **A reader's data stays the reader's**: in their browser, or in their own vault with their own key. No IP addresses. Nothing about a reader goes to a third party without a notice on the page and an off switch.
- **No third-party scripts or styles** in pages (the gate refuses them); vendor what you need, with its source and hash.
- **Untrusted input is shown as text**: feeds, notes, model output, anything fetched. Never inject it as HTML; links only when http(s).
- **A model is given data, not instructions**: page text handed to a model is quoted as material; the reader's own key is used from the reader's browser and kept in their vault, never in this repository or in telemetry.
- **No exploit or trigger-path content**: the code analysis stays on the fix, the versions and the defence.

## 6. Where to look first

`README.md` (how the site is built and released), `REALITY.md` (what exists), `/admin/board/` (what is open and whose), `/team/` (who is who), `/admin/roles/` (the rules each role enforces), this file.
