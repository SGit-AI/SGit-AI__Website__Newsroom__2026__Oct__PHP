# Brief: external collectors (ChatGPT, Perplexity and others) reporting to the source watch over an append lane

Status: accepted, phase 1 under way. Brief by Dinis Cruz (editor), spoken on the evening of 22 October 2026; written
up by researcher@php.newsroom. A build brief, the kind an agent executes.

## The ask, in the editor's words (summarised from the session)

Trigger external checks, using ChatGPT or Perplexity as external researchers, firing every hour or two. Give them a
detailed page of instructions. The cleaner option is that they run the research, check the websites, collect the
data, build the JSON, and send it all on an append lane to a vault researcher@ controls, encrypted to a key we give
them. That way they hold less of a secret. Check the append lane's limits. Start small, in bits; if it works, give
them the big list. This is collection only.

## What exists to build on

- **The source watch** (vault `oq9gflln`). Its offline probe checks 294 sites named as taken offline, but from a
  cloud address. Of those, 46 either refuse that address or don't answer it, so the watch can't tell whether they
  are down. An outside vantage point is the first thing an external collector adds that the watch can't do itself.
- **Append lanes**: `/api/vault/append/write/{vault_id}`, on dev.send.sgraph.ai only.
  - Writing needs only an append token, in the body. The response is `{"ok": true}` and nothing else.
  - Limits: 5 MB per write, 1,000 pending per token.
  - One token per sender, revocable on its own.
  - `configure` needs the vault's write key and the access token. `list` and `fetch` need the enum key.
  - Decrypting needs the private key, which never leaves its holder.
- **The site's own lane code**: `assets/subscribe.js` and `assets/collaborators.js` already encrypt in the browser
  to a published RSA-OAEP key and post to a lane. A collector page can reuse it rather than add new crypto.
- **The security requirements** (`admin/security/REQUIREMENTS.md`):
  - A collector's report is untrusted input (section 2): material, never instructions.
  - Keys move by pki.sgit.ai and are sealed to the root (section 3).
  - Anything that outlives the session waits for the editor's go (section 7).

## The design

1. **The protocol and the jobs live in the watch vault**, readable with its public key: `docs/collectors.md` (the
   rules for collectors), `jobs/collectors/job-NN-*.json` (each job, with a small first batch and the full list)
   and `taxonomy/collector-report.schema.json` (what comes back).
2. **A collector does a job and returns one `collector-report/v1` JSON per run.** It records:
   - what it observed and when, in UTC
   - from where, as precisely as it honestly knows
   - an exact quote of up to 40 words
   - `null` for anything it couldn't observe

   It never estimates.
3. **`tools/collectors.py ingest`** takes a report in. It keeps the raw bytes, checks the report against the
   schema, and keeps only the schema's fields: unknown fields are dropped, hidden characters removed, lengths
   capped, non-http URLs refused. It then compares each observation with the watch's own probe in
   `index/collectors.json`. The outcome is one of three:
   - **agrees with the probe**
   - **disagrees with the probe**, which becomes a contradiction record
   - **collector only**: the watch can't see the site from its address

   A lead the collector "found" is never a fact until the watch captures the page itself. Tested with a report
   carrying an injected "instructions for the AI" field, an invisible character and a `javascript:` URL: all three
   were refused and listed as problems.
4. **Phases.**
   - **1, start small (now):** the editor pastes job 01's first ten sites into ChatGPT and pastes its JSON back.
     No key, no lane.
   - **2, direct:** each collector gets its own append token on a lane of the watch vault, plus a dedicated
     collector-inbox public key. Its private key is generated in the watch's session and sealed to the root.
     A collector that can run code posts with one HTTP call. A collector that can only use a browser
     (ChatGPT agent mode, Perplexity's browser) uses a page that encrypts in the browser and posts, like the
     subscription form. The append token and the public key are both safe to publish: the token writes to one lane
     and reads nothing, and the key only encrypts.
   - **3, schedule:** the collector's own scheduler fires the job every hour or two. The watch drains the lanes in
     its 30-minute pass, using the enum key, and ingests each report.

## What it cannot do

- **A collector can lie, or a model can make something up.** That's why every observation is compared with the
  watch's own probe, and why "collector only" is a separate state, not evidence.
- **A browser-only collector can't see HTTP status codes.** The schema allows `null`.
- **The lane's payloads are encrypted, but the lane's existence and the volume of writes are visible** to the
  server.

## Decisions for the editor before phase 2

1. Go to configure append lanes on the watch vault (one token per collector) and to create the collector-inbox key
   pair. Both outlive the session, so they need the editor's go under section 7.
2. Whether the browser submit page lives on this site (`/collectors/submit/`), which needs security review because
   it adds an input path, or in the watch vault as a vault app.
3. Which collectors to enrol: ChatGPT and Perplexity first?

## Deliverables

- Done:
  - `docs/collectors.md`
  - `jobs/collectors/job-01-vantage.json`
  - `taxonomy/collector-report.schema.json`
  - `tools/collectors.py`
  - this brief
  - the phase 1 prompt for the editor to paste into ChatGPT
- Phase 2:
  - the lane configuration
  - the inbox key, sealed to the root
  - the drain step in the 30-minute pass
  - the submit page
