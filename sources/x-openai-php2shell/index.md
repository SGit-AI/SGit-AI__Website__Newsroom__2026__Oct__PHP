# Source: OpenAI on X: OpenAI models helped researchers ... discover critical security flaws in PHP

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

OpenAI (@OpenAI): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · social · primary · captured

# OpenAI on X: OpenAI models helped researchers ... discover critical security flaws in PHP

**OpenAI (@OpenAI)** · [https://x.com/OpenAI/status/2112907856018309586](https://x.com/OpenAI/status/2112907856018309586) · published 2026-10-21T14:04Z · added by `collector-researchers` · slug `x-openai-php2shell`

Shown '14:04 · 21 Oct 2026', 5.2m views. Full text captured (stands in for the blocked openai.com post). Carries an X Community Note disputing OpenAI's discovery role and linking lcfr_hax.

## What it says, as the collector read it

#### OpenAI on X, 21 Oct 2026 14:04 UTC

- Full text (verbatim): "OpenAI models helped researchers—operating as part of our Patch the Planet initiative—discover critical security flaws in PHP, an open-source programming language used to run an estimated 70% of websites. Over the past two months, we led a coalition of maintainers, researchers, and security providers to prepare fixes and protections ahead of disclosure. This duration was necessary because the fix was quite intricate and required a major change to the PHP engine. ... Due to the severity of these flaws and PHP's widespread use, we consider this bug to be one of the most impactful vulnerabilities in recent memory. It also marks a new phase, where AI can find security bugs with internet-scale impact. This is an example of the Defender's Window in action: to our knowledge, frontier AI was able to find this vulnerability ahead of attackers, giving defenders time to prepare."

- Links to openai.com/index/coordina… = "Patch the Planet: global response coordination as agents uncover critical vulnerabilities" (blocked; see openai-blog-coordinated-disclosure).

- X COMMUNITY NOTE (as displayed): "OpenAI may claim a role in the coordinated response and patching process. But the initial discovery and exploit development, however, occurred several months earlier by an independent researcher. x.com/lcfr_hax/statu…" (the note's "several months" is itself inaccurate: Aug 5 to Oct 21 is under 3 months).

- Wording difference: BBC quotes "one of the most impactful security issues in recent memory"; the tweet says "one of the most impactful vulnerabilities in recent memory". The blog may use "security issues" — unverified (blocked).

- "ahead of attackers" conflicts with Amazon's Oct 17 MadPot attempt (thehackernews-php2shell-4days) and Cloudflare's report of attack traffic after the leak.

- Reply (third party): "Patching the planet by prematurely leaking vuln details? Sure."

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| PHP is used by almost 70% of websites whose server-side language is knownNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. [fact timeline →](../../facts/scale-70pc-websites/index.html) | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | **A2** Reported●●○○○○ measures differently | 3/3 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. [fact timeline →](../../facts/ai-found/index.html) | BBC; OpenAI; Calif; Wiz | reported | **A3** Echoed●●●○○○ opinion measures differently | 3/4 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Frontier AI found the flaw ahead of attackers, giving defenders time to prepareAmazon reports an exploit attempt against a honeypot on 17 October, four days before disclosure, from an actor whose source of exploit information is unknown. [fact timeline →](../../facts/ahead-of-attackers/index.html) | OpenAI | disputed | **A2** Reported●●○○○○ opinion disputed | 1/2 | [OpenAI on X](../../sources/x-openai-php2shell/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 14:04 UTC | OpenAI posts: models 'helped researchers ... discover critical security flaws in PHP ... used to run an estimated 70% of websites'. An X Community Note later disputes OpenAI's role. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| almost 70% | websites | reported |

## The bytes
capture 20261022T081645Z · HTTP 200 · https://x.com/OpenAI/status/2112907856018309586- `headers.json` 427b75f5bb12cb7b0acee221f2065095d92c82279e0db87f9b80909525886df3 9,023 bytes
- `page.html` 8e6a0183b6982e8530d7b48277e4b0f6f010b22d3348b30328cc4460cc371d90 160,064 bytes
- `provenance.json` 3e52aad242520de5ca4db4103baf86c58e7d477a8f7c04c19b841034f1ca49e3 1,232 bytes
- `rendered.html` 2e31eee6ab72f0703675cd74158267dbe5cfb55bf03b80153deaa1b899be4c10 147,195 bytes
- `screenshot.png` aaf750d50e69e80b34fbdf908a9fdc330ac315b765eacb2e3e8361cb40f2cbb2 570,247 bytes
- `text.txt` 785b7cae55e3748b3d11e002f9b254408a57849c1ef08eb9fcc16a2cd196f189 3,316 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/x-openai-php2shell/index.html
