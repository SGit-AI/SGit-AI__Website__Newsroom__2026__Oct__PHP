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

## 6. Vaults and keys: every vault listed, every key sealed

Added by conductor@php.newsroom at the editor's request, 23 October 2026: "a page on the website that lists the agent name and the vaults they created, just the vault ID, which is public anyway; it's the vault key that we can't share"; and "when I say send me a vault key or a QR code, every agent does it with the instructions on pki.sgit.ai".

**When you make a vault**

1. In the same commit, add a row to your own file, `data/vault-register/<you>.json` (make it if it is new: copy the shape of `conductor.json`): `id` (the eight-character vault ID), `what` (one line), `created` (the date), `key_sealed_to_root`. `/team/vaults/` lists every agent's vaults from these files. The build refuses anything in `id` that is not a bare vault ID. Never write a key, a read key you were not told to publish, an enum key, a token or a passphrase in it.
2. Before your session ends, seal the vault key to the root:

```
curl -sO https://pki.sgit.ai/agents/pki-agent.mjs          # into your scratchpad, not the repository
node pki-agent.mjs pin sha256:db7f79fdd87e030a             # the root, from CLAUDE.md, once per session
node pki-agent.mjs seal --from-vault <your clone> --name "<vault id> vault key" --expires 14 \
     --qr <scratchpad>/<vault id>.png --qr-link
```

   `seal --from-vault` reads the key straight from sgit and never prints it. It prints a `https://pki.sgit.ai/m/#m1.…` link that only the root's passkey opens. Put the date in `key_sealed_to_root` and tell the editor the link and when it expires.

**Record the keys you hold, not only the vaults you made**

In the same file, the `holds` list: one row for every key you were given or made, `{"id": "<vault id>", "key": "vault key" | "read key" | "append token", "from": "<who gave it, or 'made it'>", "since": "<date>"}`. Never the key itself: the build refuses anything in `key` but those three words. This is what lets the editor start a new session for you, or for an agent that takes over your work, with exactly the keys it needs. When a key is taken back or rotated, remove the row.

**The vault key is the whole boundary**

Whoever holds a vault's key must be able to do everything that vault is for, including draining its lane and decrypting what arrives: a vault app, the editor or another agent with the key, without anything from your session. That is sgit.ai's convention, "the vault key is the only secret" (sgit.ai/docs/append-lane-messaging.md, section 7.1), and `admin/build/postmaster.py` implements it here:

- the lane's enum key and the key pair's passphrase are derived from the vault's write key (HMAC-SHA256 with the labels in that file), never stored and never random;
- the key pair that decrypts what arrives lives inside the vault, at `.vault/postmaster/front-door-keypair/`, its private halves encrypted under that derived passphrase;
- `.vault/postmaster/lane.json` says which lane, which recipient key, and each sender's token (published, or derived from the vault key).

So: when you make a vault with a lane, set it up that way from the start. Never leave an enum key, a passphrase or a private key only in your session or your scratchpad: when your session ends, the vault would be undrainable. If your session's permissions stop you writing the key pair into the vault, say so and stop.

**When the editor asks you for a key, or a QR code of one**

- Seal it as above and send him two things: the sealed link, and the QR image (`--qr <file>.png --qr-link` makes one a phone's camera opens; send the file, do not describe it). Say which vault, and when the link expires.
- Any other secret (an enum key, a lane token, a passphrase) goes the same way: `seal --file <a file in your scratchpad> --name "…"`, then delete the file.
- Never the key itself: not in your reply, not in a file in the repository, not on a page, not in a commit message, not in a message to another agent. A vault ID is fine anywhere.
- If your session's permissions stop pki-agent, say so to the editor and stop. There is no plain-text fallback.

## 7. Where to look first

`README.md` (how the site is built and released), `REALITY.md` (what exists), `/admin/board/` (what is open and whose), `/team/` (who is who), `/admin/roles/` (the rules each role enforces), this file.
