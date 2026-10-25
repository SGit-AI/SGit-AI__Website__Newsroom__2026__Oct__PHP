# Who found php2shell, and what the AI did

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Calif, OpenAI and Wiz each claim the discovery of php2shell; their own timelines side by side, the 2024 audit that saw it first, the credits on the advisories, and what the sources do and do not say about the models.

# Who found it, and how

In plain English Who found the flaws (three research teams, all using AI help) and what the AI actually did, as far as anyone has said.

Three research parties say they found php2shell, and all three say AI helped. Their own timelines, placed side by side, do not conflict on dates: Calif first (1 to 11 August), OpenAI the same day as Calif's report, Wiz independently eight days later. They conflict on framing: Wiz's *Wiz Research uncovers*, OpenAI's *frontier AI was able to find this vulnerability ahead of attackers*, and a Community Note on OpenAI's post pointing at Calif's August hash.

### Calif
- 2026-07-30 audit begins under Patch the Planet
- 2026-08-01 multiple paths to RCE found
- 2026-08-05 hash commitment posted on X
- 2026-08-11 first bug reported to PHP
- 2026-08-14 RCE PoC shared; confirmed 08-15
- 2026-08-21 second bug reported

[Calif](../sources/calif-php2shell/index.html) [Ryan Austin, Calif on X](../sources/x-lcfr-hax-hash-tweet/index.html)

### OpenAI
- 2026-08-11 same root cause reported, same day as Calif (per the Foundation)
- 2026-09-18 further attack vectors
- coalition of maintainers, researchers and providers over two months
- credit: amyb-oai on both advisories

[PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [OpenAI on X](../sources/x-openai-php2shell/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html)

### Wiz
- 2026-08-19 first vulnerability found (Wiz Atlas, Gemini 4 Argon, GPT-5.6 Sol)
- 2026-08-20 RCE confirmed on Drupal
- 2026-08-21 RCE confirmed on WordPress
- 2026-08-24 reported to PHP
- 2026-09-21 PHP acknowledges
- credit: sagitzadik-wiz

[Wiz](../sources/wiz-blog-php2shell/index.html)

### Before them
- 2024 Quarkslab audit (OSTIF, Sovereign Tech Agency) surfaces the OOM issue
- 2024 a Foundation-contracted developer finds first signs; exploit theorised, no vector
- credit: tomash-areion on both advisories, named nowhere else

[PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Calif](../sources/calif-php2shell/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

## What the AI did

The honest answer from the captured sources is: not enough is said. Calif says *No special harness, or access to models that weren't generally available to everyone were used in the initial bug discovery* and that the researcher *asked my LLM companion for help*; it names no model. Wiz names three tools and quotes Google DeepMind's head of Gemini security: *a single researcher completed in a week what previously would have taken a world-class team months of work.* OpenAI's blog, which reportedly names GPT-5.6 Sol, is behind a bot challenge from this capture environment. The PHP Foundation adds that the project was separately scanned with Anthropic's Claude Mythos through Alpha-Omega and that OpenAI's Daybreak Red validated reports and exploits.

What is established is the shape: a bug class seen in 2024 and left because nobody could prove exploitation, then three groups with model assistance finding working exploits within three weeks of each other in August 2026. The BBC's quote, *a complex chain of steps, at the edge of what human researchers could practically achieve*, is not on any captured researcher page.

[Calif](../sources/calif-php2shell/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html) [OpenAI](../sources/openai-blog-coordinated-disclosure/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html)

## The claims on discovery

| Claim | Who says it | Status | [Fact-check](../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. [fact timeline →](../facts/ai-found/index.html) | BBC; OpenAI; Calif; Wiz | reported | **A3** Echoed●●●○○○ opinion measures differently | 3/4 | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) [OpenAI on X](../sources/x-openai-php2shell/index.html) [Calif](../sources/calif-php2shell/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html) |
| Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 AugustThe hash tweet is dated 5 August 2026 on X; its pre-image has not been published, so what it commits to cannot be checked. [fact timeline →](../facts/who-first/index.html) | Calif; PHP Foundation (report date) | confirmed | **A3** Echoed●●●○○○ opinion measures differently status overstated | 3/3 | [Calif](../sources/calif-php2shell/index.html) [Ryan Austin, Calif on X](../sources/x-lcfr-hax-hash-tweet/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| OpenAI independently reported the same root cause on 11 August, with further vectors on 18 SeptemberThe GitHub advisories credit amyb-oai among four reporters. OpenAI's own post credits Calif's discovery 'using GPT-5.6 Sol' and Wiz; an X Community Note disputes OpenAI's role. [fact timeline →](../facts/openai-same-day/index.html) | PHP Foundation | reported | **A2** Reported●●○○○○ disputed | 2/2 | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| Wiz Research independently discovered the first flaw on 19 August and reported on 24 AugustWiz's X post says 'Wiz Research uncovers' with no credit to Calif or OpenAI; the blog thanks both. [fact timeline →](../facts/wiz-independent/index.html) | Wiz; PHP Foundation (24 August) | reported | **A2** Reported●●○○○○ | 2/2 | [Wiz](../sources/wiz-blog-php2shell/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areiontomash-areion is not named in the PHP Foundation's thanks and appears nowhere else on this beat. [fact timeline →](../facts/four-reporters/index.html) | GitHub security advisories | confirmed | **A6** Established●●●●●● | 2/3 | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixedTwo parties agree. The Foundation calls the delay 'a structural failure'. Cloudflare lists Quarkslab among the 2026 disclosers; nobody else does. [fact timeline →](../facts/quarkslab-2024/index.html) | PHP Foundation; Calif | confirmed | **A2** Reported●●○○○○ disputed status overstated | 2/2 | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Calif](../sources/calif-php2shell/index.html) |
| Frontier AI found the flaw ahead of attackers, giving defenders time to prepareAmazon reports an exploit attempt against a honeypot on 17 October, four days before disclosure, from an actor whose source of exploit information is unknown. [fact timeline →](../facts/ahead-of-attackers/index.html) | OpenAI | disputed | **A2** Reported●●○○○○ opinion disputed | 1/2 | [OpenAI on X](../sources/x-openai-php2shell/index.html) [THN](../sources/thehackernews-php2shell-4days/index.html) |
| The most severe flaws ever detected by AIWiz's own wording is 'among the most severe vulnerabilities discovered in PHP, and arguably in software history'. OpenAI: 'one of the most impactful vulnerabilities in recent memory'. [fact timeline →](../facts/most-severe/index.html) | BBC attributing Wiz | reported | **A2** Reported●●○○○○ opinion measures differently | 1/2 | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html) |
| Quarkslab's published audit summary lists 27 findings, two redacted because their fixes were complex and in progress; it does not describe an out-of-memory findingThe Foundation says the OOM signs were found while fixing one of the audit's findings, not in the audit report itself. [fact timeline →](../facts/quarkslab-redacted/index.html) | Quarkslab's blog; a Substack analysis | reported | **A6** Established●●●●●● | 1/2 | [Quarkslab](../sources/quarkslab-blog-php-src-audit/index.html) [David Lopez-Kurtz](../sources/substack-lopezkurtz-patch-is-the-exploit/index.html) |
| Chainguard's team found the same bugs independently with an AI harness and a frontier model after a researcher warned them on the Friday beforeUnverified by anyone else. [fact timeline →](../facts/lorenc-ai-found/index.html) | Dan Lorenc, via The Register | reported | **A2** Reported●●○○○○ | 0/1 | [The Register](../sources/theregister-php-blames-chainguard/index.html) |


---
site v0.20.3 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/discovery/index.html
