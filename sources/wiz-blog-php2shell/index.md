# Source: PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Wiz (Wiz Research): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · researcher · primary · captured

# PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet

**Wiz (Wiz Research)** · [https://www.wiz.io/blog/php2shell-php-rce](https://www.wiz.io/blog/php2shell-php-rce) · published 2026-10-21 · added by `collector-researchers` · slug `wiz-blog-php2shell`

Wiz Research post dated October 21, 2026. Source of '70% of the Internet' headline; body basis is 'powers 70% of all websites'. Disclosure timeline: discovered Aug 19, reported Aug 24, PHP ack Sep 21. Credits Gemini 4 Argon, GPT-5.6 Sol, Wiz Atlas.

## What it says, as the collector read it

#### Wiz Research blog: "PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet"

- URL https://www.wiz.io/blog/php2shell-php-rce ; dated "October 21, 2026". Captured 2026-10-22T08:10:47Z, HTTP 200.

- 70% basis: body says PHP "powers 70% of all websites in the world" — a share-of-websites figure (no source cited for it on the page) that the headline turns into "70% of the Internet". Conclusion: "With 70% of the Internet affected, the impact of PHP2Shell cannot be overstated."

- Severity claim: "These findings rank among the most severe vulnerabilities discovered in PHP, and arguably in software history."

- AI: "We used Wiz Atlas, Gemini 4 Argon and GPT-5.6 Sol throughout this research. Notably, Gemini 4 Argon made an invaluable contribution to finding the vulnerability..." Quote from Raluca Ada Popa, Head of Gemini Security, Google DeepMind. "a single researcher completed in a week what previously would have taken a world-class team months of work."

- Credits: "Wiz Research would like to thank the PHP team, Calif and OpenAI for their work on discovery, coordination and patch verification."

- Partners named: "Google Cloud, Cloudflare, AWS, Microsoft, Automattic, Fastly, Akamai, Imperva, Vercel and many others".

#### Wiz's timeline (verbatim)

- "August 19, 2026: Wiz Research discovers the first PHP vulnerability using Wiz Atlas, Gemini 4 Argon, and GPT-5.6 Sol."

- "August 20, 2026: Unauthenticated RCE is confirmed against Drupal."

- "August 21, 2026: Unauthenticated RCE is confirmed against WordPress."

- "August 24, 2026: Wiz Research reports the vulnerabilities to the PHP security team."

- "September 21, 2026: PHP acknowledges the reports and begins developing a coordinated fix."

- "October 21, 2026: Patched PHP releases become available." / "Public disclosure."

#### Notes

- No mention of the leak, the Calif video or Chainguard.

- "September 21 ... begins developing a coordinated fix" conflicts with the PHP Foundation's account that fixing was "the top priority" "from August 11th onward" (Daubois: fix PR opened 2026-09-25).

- The BBC's "most severe ever found by AI" wording is not on this page as such; closest is "arguably in software history".

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCSTwo researcher parties, no third-party reproduction in the vault. The demo videos were not downloaded. [fact timeline →](../../facts/wordpress-drupal/index.html) | Calif; Wiz for WordPress and Drupal | reported | **A2** Reported●●○○○○ | 2/2 | [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. [fact timeline →](../../facts/scale-70pc-internet/index.html) | Wiz (headline, X post); the BBC, which reports it as Wiz's 'roughly 70%' | unverified | **A1** Weak signal●○○○○○ measures differently | 2/3 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| PHP is used by almost 70% of websites whose server-side language is knownNone of the three cites the survey it comes from. A share of websites using PHP is an upper bound on exposure, not a count of vulnerable systems. [fact timeline →](../../facts/scale-70pc-websites/index.html) | Cloudflare; OpenAI ('an estimated 70%'); Wiz body text | reported | **A2** Reported●●○○○○ measures differently | 3/3 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. [fact timeline →](../../facts/ai-found/index.html) | BBC; OpenAI; Calif; Wiz | reported | **A3** Echoed●●●○○○ opinion measures differently | 3/4 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Wiz Research independently discovered the first flaw on 19 August and reported on 24 AugustWiz's X post says 'Wiz Research uncovers' with no credit to Calif or OpenAI; the blog thanks both. [fact timeline →](../../facts/wiz-independent/index.html) | Wiz; PHP Foundation (24 August) | reported | **A2** Reported●●○○○○ | 2/2 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) |
| The most severe flaws ever detected by AIWiz's own wording is 'among the most severe vulnerabilities discovered in PHP, and arguably in software history'. OpenAI: 'one of the most impactful vulnerabilities in recent memory'. [fact timeline →](../../facts/most-severe/index.html) | BBC attributing Wiz | reported | **A2** Reported●●○○○○ opinion measures differently | 1/2 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-08-19 | Wiz Research discovers the first vulnerability using Wiz Atlas, Gemini 4 Argon and GPT-5.6 Sol; confirms RCE against Drupal on 20 August and WordPress on 21 August. | stated |
| 2026-08-24 | Wiz reports to the PHP security team. | stated |
| 2026-09-21 | PHP acknowledges Wiz's reports 'and begins developing a coordinated fix'. | stated |
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 70% | the Internet | unverified |

## The bytes
capture 20261022T081047Z · HTTP 200 · https://www.wiz.io/blog/php2shell-php-rce- `headers.json` f3a7f515bda9ae91541c7792cad2fbb4d5864a7962be4f5db93bccbe8caa2d03 5,075 bytes
- `page.html` 32408c9f60071e7bdcf0e702160f6c398d6967cb89fbc81b5f0e0029e34af07b 438,665 bytes
- `provenance.json` 4e362d46ccd571e124b20fb3518c8d00076dc508a0146ee5338a7dce931d1fa1 1,002 bytes
- `rendered.html` 6db43e32910bdf4bc2b82a93afa5097900aa4a205b5cdde32d1a2510beff4c68 580,534 bytes
- `screenshot.png` 4ba83874c540e1f7faf4c817b6b8c3ae1ef61eacda5851a112d6601e47d6d91f 2,753,995 bytes
- `text.txt` e3568b6f88c93f6bb08eebe3c8811f9fd283212f7331b287d5170b91d6bad1ea 19,147 bytes
capture 20261023T160435Z · HTTP 200 · https://www.wiz.io/blog/php2shell-php-rce- `headers.json` 9a16e711afa57b40119200d4edbace18a1e933561b09e239752b3796525ce1a9 5,133 bytes
- `page.html` 76dcb531033b21e366d4f5a6f70f4985f27945ecd9d4483e54929e184f778d47 439,659 bytes
- `provenance.json` e1c70991a21d294d5f694fae2f0a1cccb9fc5d6e7905faacc0d639652e991c31 1,537 bytes
- `text.txt` 4c6c2b8a41be8de0fd90fcc8232995625833e085788e2f99ce8ef9789b09635d 19,135 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/wiz-blog-php2shell/index.html
