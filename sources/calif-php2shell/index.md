# Source: php2shell by Calif Research — A tale of two PHP remote vulnerabilities

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Calif (Calif Research): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · researcher · primary · captured

# php2shell by Calif Research — A tale of two PHP remote vulnerabilities

**Calif (Calif Research)** · [https://calif.io/php2shell/](https://calif.io/php2shell/) · published 2026-10-21 · added by `collector-researchers` · slug `calif-php2shell`

Calif's own write-up by Ryan Austin (@lcfr_hax). Page has no machine timestamp; story panel dated 'Oct 21, 2026'. Embeds two YouTube exploit demo videos (pfWZrdzvooc 'php2shell exploit demonstration', cE4h79AWbT4 'Exploiting Nginx with PHP-FPM'); videos NOT downloaded. Its timeline omits the leaked/deleted video.

## What it says, as the collector read it

#### Calif: "php2shell by Calif Research" — notes (collector-researchers)

- URL: https://calif.io/php2shell/ (linked from the calif.io homepage banner "Calif discovered php2shell"). Captured 2026-10-22T08:10:33Z, HTTP 200.

- Date: no machine-readable publish time; the comic timeline's last panel reads "Oct 21, 2026 and here we are...". Credits: "Research and writeup by Ryan Austin (@lcfr_hax) of Calif ... Poster and comic story by Michal Zalewski (@lcamtuf) of Calif."

- Framing: "two PHP remote vulnerabilities (CVE-2026-109618, CVE-2026-109619) discovered by Calif, OpenAI and Wiz".

#### Calif's timeline (verbatim from "An interesting timeline of events")

- "2026 — August 1 Calif discovered multiple different paths independently leading to RCE that resurfaced the 2024 issues and new trigger points."

- "2026 — August 5 Calif researcher Ryan Austin (@lcfr_hax) tweeted hash of one finding." (links https://x.com/lcfr_hax/status/2085031675382071483)

- "2026 — August 11 Calif reported the first bug to PHP and started coordinated disclosure process."

- "2026 — August 14 Calif shared an RCE PoC with PHP."

- "2026 — August 15 PHP confirmed that the RCE PoC worked as expected."

- "2026 — August 21 Calif reported the second bug to PHP."

- "2026 — October 21 Patched versions released."

- Comic panel 4: "July 30, 2026 Patch the Planet ... OpenAI invited us to join its Patch the Planet initiative ... Stefan connected us with Volker Dusch, who accepted our invitation."

- 2024 panel: "OSTIF and Quarkslab performed an audit of PHP and rediscovered the same OOM issue. However, exploitation was not proven, hence the bug was not fixed."

#### AI angle

- "No special harness, or access to models that weren't generally available to everyone were used in the initial bug discovery." Austin: "I asked my LLM companion for help." Model is NOT named on this page (press says GPT-5.6 Sol).

- "We were not expecting to find anything critical - everyone and every lab had already done extensive AI assisted audits of this target."

#### Exploit demos (not downloaded)

- Page embeds "Here is a demo video of the exploits running:" YouTube iframes: youtube-nocookie.com/embed/pfWZrdzvooc ("php2shell exploit demonstration") and /embed/cE4h79AWbT4 ("Exploiting Nginx with PHP-FPM"). Claims confirmed pre-auth RCE on WordPress 7.1.2, Drupal 11.4.3, Joomla 6.1.4, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony, WHMCS.

- Whether pfWZrdzvooc is the same video the PHP Foundation says Calif "mistakenly published" on Oct 20 is UNKNOWN. The page does not mention the leak or the deleted video at all.

#### Contradictions

- Calif: discovery Aug 1; first report Aug 11. Fortune repeats Aug 1. PHP Foundation: Calif's audit began July 30, report Aug 11 (agrees).

- Calif homepage also links two archive.is snapshots (arHsF, spwCf), probably of WSJ/NYT coverage — not checked.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCSTwo researcher parties, no third-party reproduction in the vault. The demo videos were not downloaded. [fact timeline →](../../facts/wordpress-drupal/index.html) | Calif; Wiz for WordPress and Drupal | reported | **A2** Reported●●○○○○ | 2/2 | [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiativeAll three research parties say AI was used. Calif: 'No special harness, or access to models that weren't generally available to everyone were used'. Calif does not name a model; Wiz names Gemini 4 Argon, GPT-5.6 Sol and Wiz Atlas; OpenAI's blog reportedly names GPT-5.6 Sol but is blocked. [fact timeline →](../../facts/ai-found/index.html) | BBC; OpenAI; Calif; Wiz | reported | **A3** Echoed●●●○○○ opinion measures differently | 3/4 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 AugustThe hash tweet is dated 5 August 2026 on X; its pre-image has not been published, so what it commits to cannot be checked. [fact timeline →](../../facts/who-first/index.html) | Calif; PHP Foundation (report date) | confirmed | **A3** Echoed●●●○○○ opinion measures differently status overstated | 3/3 | [Calif](../../sources/calif-php2shell/index.html) [Ryan Austin, Calif on X](../../sources/x-lcfr-hax-hash-tweet/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) |
| The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixedTwo parties agree. The Foundation calls the delay 'a structural failure'. Cloudflare lists Quarkslab among the 2026 disclosers; nobody else does. [fact timeline →](../../facts/quarkslab-2024/index.html) | PHP Foundation; Calif | confirmed | **A2** Reported●●○○○○ disputed status overstated | 2/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Calif](../../sources/calif-php2shell/index.html) |
| Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'Calif's own page does not mention a leak or a deleted video; it embeds two demo videos. Whether one of them is the deleted video is unknown. [fact timeline →](../../facts/leak-video/index.html) | PHP Foundation | reported | **A3** Echoed●●●○○○ | 3/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../sources/phpfoundation-blog-security-release-leak/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Calif](../../sources/calif-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2024 | Quarkslab audits PHP (funded through OSTIF and the Sovereign Tech Agency). While fixing one of its findings a PHP core developer finds the first signs of the out-of-memory problem behind CVE-2026-109618; an exploit is theorised but no vector found, so it is not fixed. | stated |
| 2026-07-30 | Calif begins an audit of PHP under Patch the Planet; Volker Dusch accepts the invitation. | stated |
| 2026-08-01 | Calif discovers 'multiple different paths independently leading to RCE that resurfaced the 2024 issues and new trigger points'. | stated |
| 2026-08-05 15:54 UTC | Ryan Austin (@lcfr_hax) posts a SHA-256 hash on X as a commitment to one finding. | stated |
| 2026-08-11 | Calif reports the first bug to PHP and coordinated disclosure begins. OpenAI independently reports the same root cause the same day. | stated |
| 2026-08-14 | Calif shares an RCE proof of concept with PHP; PHP confirms it works on 15 August. | stated |
| 2026-08-21 | Calif reports the second bug to PHP. | stated |
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

## The bytes
capture 20261022T081033Z · HTTP 200 · https://calif.io/php2shell/- `headers.json` 1fc0b2864079499b5911e31166e216c1c753a83da9a65d38086609e84372794e 759 bytes
- `page.html` 9f3df4d68b9d185563f9b5eec4b1e910f296389f54e02b4f6a25fef2573662a3 68,302 bytes
- `provenance.json` c800836bfdf2759a20495415eb65bff17d26b8d9127d0695f7be27870b1dc67b 906 bytes
- `rendered.html` 24e345e4514f5240f94df7537536a5ed14ba6e440cffffae74f8c38c7c8e5644 68,280 bytes
- `screenshot.png` 38990c6ce9af5828a86614d9dff808d621097986d5288e8136bda70412b3ac63 20,097,747 bytes
- `text.txt` 23afef81971778f954d3cefb62c4901814afddd6ae0948c941af3edead40ced4 23,876 bytes
capture 20261024T133450Z · HTTP 200 · https://calif.io/php2shell/- `headers.json` 4a8ab067dd4e49688e657fdfd0c51aec0e51a8a6aebf16f0dd8bcf9b6e2d0dc1 738 bytes
- `page.html` 2b77deb5169ba2a3872ea2045454735893bcc915a4f2f4eb2132ec415b62f7cb 69,595 bytes
- `provenance.json` a3e7faae2faf08834fc17c711b74edc2c6b6ef4983321a0e8fdbc7f161e5a095 1,438 bytes
- `text.txt` effb0fa357b68ea97d847a69a42809262dd6c84accfe18cfc4113ec58e5c849b 23,899 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/calif-php2shell/index.html
