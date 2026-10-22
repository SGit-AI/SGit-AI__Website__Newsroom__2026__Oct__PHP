# Who found php2shell, and what the AI did

Calif, OpenAI and Wiz each claim the discovery of php2shell; their own timelines side by side, the 2024 audit that saw it first, the credits on the advisories, and what the sources do and do not say about the models.

# Who found it, and how

Three research parties say they found php2shell, and all three say AI helped. Their own timelines, placed side by side, do not conflict on dates: Calif first (1 to 11 August), OpenAI the same day as Calif's report, Wiz independently eight days later. They conflict on framing: Wiz's *Wiz Research uncovers*, OpenAI's *frontier AI was able to find this vulnerability ahead of attackers*, and a Community Note on OpenAI's post pointing at Calif's August hash.

### Calif
- 2026-07-30 audit begins under Patch the Planet
- 2026-08-01 multiple paths to RCE found
- 2026-08-05 hash commitment posted on X
- 2026-08-11 first bug reported to PHP
- 2026-08-14 RCE PoC shared; confirmed 08-15
- 2026-08-21 second bug reported

[Calif](../sources/index.html#calif-php2shell) [Ryan Austin , Calif on X](../sources/index.html#x-lcfr-hax-hash-tweet)

### OpenAI
- 2026-08-11 same root cause reported, same day as Calif (per the Foundation)
- 2026-09-18 further attack vectors
- coalition of maintainers, researchers and providers over two months
- credit: amyb-oai on both advisories

[PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [OpenAI on X](../sources/index.html#x-openai-php2shell) [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w)

### Wiz
- 2026-08-19 first vulnerability found (Wiz Atlas, Gemini 4 Argon, GPT-5.6 Sol)
- 2026-08-20 RCE confirmed on Drupal
- 2026-08-21 RCE confirmed on WordPress
- 2026-08-24 reported to PHP
- 2026-09-21 PHP acknowledges
- credit: sagitzadik-wiz

[Wiz](../sources/index.html#wiz-blog-php2shell)

### Before them
- 2024 Quarkslab audit (OSTIF, Sovereign Tech Agency) surfaces the OOM issue
- 2024 a Foundation-contracted developer finds first signs; exploit theorised, no vector
- credit: tomash-areion on both advisories, named nowhere else

[PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [Calif](../sources/index.html#calif-php2shell) [PHP](../sources/index.html#github-ghsa-6wmf-4rv5-p3rp)

## What the AI did

The honest answer from the captured sources is: not enough is said. Calif says *No special harness, or access to models that weren't generally available to everyone were used in the initial bug discovery* and that the researcher *asked my LLM companion for help*; it names no model. Wiz names three tools and quotes Google DeepMind's head of Gemini security: *a single researcher completed in a week what previously would have taken a world-class team months of work.* OpenAI's blog, which reportedly names GPT-5.6 Sol, is behind a bot challenge from this capture environment. The PHP Foundation adds that the project was separately scanned with Anthropic's Claude Mythos through Alpha-Omega and that OpenAI's Daybreak Red validated reports and exploits.

What is established is the shape: a bug class seen in 2024 and left because nobody could prove exploitation, then three groups with model assistance finding working exploits within three weeks of each other in August 2026. The BBC's quote, *a complex chain of steps, at the edge of what human researchers could practically achieve*, is not on any captured researcher page.

[Calif](../sources/index.html#calif-php2shell) [Wiz](../sources/index.html#wiz-blog-php2shell) [OpenAI](../sources/index.html#openai-blog-coordinated-disclosure) [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t)

## The claims on discovery

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. | BBC; OpenAI; Calif; Wiz | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [OpenAI on X](../sources/index.html#x-openai-php2shell) [Calif](../sources/index.html#calif-php2shell) [Wiz](../sources/index.html#wiz-blog-php2shell) |
| Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 AugustThe hash tweet is dated 5 August 2026 on X; its pre-image has not been published, so what it commits to cannot be checked. | Calif; PHP Foundation (report date) | confirmed | [Calif](../sources/index.html#calif-php2shell) [Ryan Austin , Calif on X](../sources/index.html#x-lcfr-hax-hash-tweet) [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) |
| OpenAI independently reported the same root cause on 11 August, with further vectors on 18 SeptemberThe GitHub advisories credit amyb-oai among four reporters. OpenAI's own post credits Calif's discovery 'using GPT-5.6 Sol' and Wiz; an X Community Note disputes OpenAI's role. | PHP Foundation | reported | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) |
| Wiz Research independently discovered the first flaw on 19 August and reported on 24 AugustWiz's X post says 'Wiz Research uncovers' with no credit to Calif or OpenAI; the blog thanks both. | Wiz; PHP Foundation (24 August) | reported | [Wiz](../sources/index.html#wiz-blog-php2shell) [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) |
| The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areiontomash-areion is not named in the PHP Foundation's thanks and appears nowhere else on this beat. | GitHub security advisories | confirmed | [PHP](../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [PHP](../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) [Daubois](../sources/index.html#daubois-blog-php2shell-rumors) |
| The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixedTwo parties agree. The Foundation calls the delay 'a structural failure'. Cloudflare lists Quarkslab among the 2026 disclosers; nobody else does. | PHP Foundation; Calif | confirmed | [PHP Foundation](../sources/index.html#php-foundation-blog-security-release) [Calif](../sources/index.html#calif-php2shell) |
| Frontier AI found the flaw ahead of attackers, giving defenders time to prepareAmazon reports an exploit attempt against a honeypot on 17 October, four days before disclosure, from an actor whose source of exploit information is unknown. | OpenAI | disputed | [OpenAI on X](../sources/index.html#x-openai-php2shell) [THN](../sources/index.html#thehackernews-php2shell-4days) |
| The most severe flaws ever detected by AIWiz's own wording is 'among the most severe vulnerabilities discovered in PHP, and arguably in software history'. OpenAI: 'one of the most impactful vulnerabilities in recent memory'. | BBC attributing Wiz | reported | [BBC News](../sources/index.html#bbc-live-ckgel5xp2xv9t) [Wiz](../sources/index.html#wiz-blog-php2shell) |


---
site v0.1.0 · data as of 2026-10-22T08:48Z · vault commit 379e3d7f172a · https://php.oct-2026.story.sgit.ai/discovery/index.html
