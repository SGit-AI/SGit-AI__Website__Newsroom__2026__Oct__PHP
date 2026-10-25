# Source: Today's PHP Security Release, and How We're Strengthening PHP Security

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The PHP Foundation: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Today's PHP Security Release, and How We're Strengthening PHP Security

**The PHP Foundation** · [https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) · published 2026-10-21 · added by `collector-primary` · slug `php-foundation-blog-security-release`

Foundation's account of discovery, 2024 audit origin, leak timeline (20 Oct 15:00Z), Calif video, Chainguard embargo break (21 Oct 07:41Z). Page embeds an r/PHP comment thread (third-party, not Foundation).

## What it says, as the collector read it

#### PHP Foundation blog: notes

- URL: https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/

- "Published on Oct 21, 2026", by "The PHP Foundation". Captured 2026-10-22T08:09Z.

- The rendered page also embeds an r/PHP thread (third-party comments, e.g. a claim that the first in-the-wild exploit was at 08:36 UTC citing ellio.tech). That is not Foundation content.

#### Key wording (verbatim)

- "CVE-2026-109618 / GHSA-w8hw-w9fx-j79w: RCE via OOM corruption ... On Apache with mod_php, an unauthenticated request can trigger this before any application code runs, and full remote code execution was demonstrated with default settings. Remote code execution was also confirmed on PHP-FPM through application-level code paths."

- "CVE-2026-109619 / GHSA-6wmf-4rv5-p3rp: RCE via stale global state ... A use-after-free and worker crash were confirmed, and the reporter demonstrated remote code execution against a real-world application running on Apache with mod_php."

- 2024 audit: Sovereign Tech Agency funding, via OSTIF, carried out by Quarkslab; a Foundation-contracted core developer "found the first signs of the OOM problem behind CVE-2026-109618". "the delay was a structural failure".

- "security firm Calif began an audit of PHP on July 30th, 2026. On August 11th researcher Ryan A at Calif reported an unconditional remote code execution ... OpenAI independently reported the same root cause on the same day, followed by further attack vectors from OpenAI on September 18th and from Wiz on August 24th."

- Also mentions scanning with "Anthropic's Claude Mythos" via Alpha-Omega, and "OpenAI's Daybreak Red" for validation; Trail of Bits also auditing.

- "On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked." Pre-announcement "published it at 19:30 UTC". Release moved "from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC."

- "As a result of the leak and pre-announcement around 20:00 UTC, Calif ... mistakenly published a video."

- "Mitigation advice we started providing to a few critical infrastructure providers around Oct 20th 23:00 UTC, may have leaked as well." "did not identify any functional exploits at the time of release/public disclosure."

- "On October 21st at 07:41 UTC, more than six hours before the coordinated release, Chainguard unilaterally broke the embargo and published built images containing the fix."

- Thanks: "Calif, especially Ryan A, Wiz, OpenAI Codex Security, especially Amy Burnett, OSTIF, and Quarkslab".

#### Contradictions

- BBC: Calif found it in August, OpenAI and Wiz "shortly after". Foundation: OpenAI reported the same root cause the same day (11 Aug); Wiz 24 Aug.

- Pre-announcement 19:30 UTC here vs php.net feed timestamp 20:32 UTC.

- The note's order of OpenAI 18 Sep then Wiz 24 Aug is as written (non-chronological).

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The flaws are CVSS 10.0The PHP Foundation: 'a wrong CVSS score of 10.0 (the actual score is 9.2)'. Daubois traces it to a social post relayed by Phoenix Security and to watchTowr via Cyber Daily. [fact timeline →](../../facts/cvss-10/index.html) | social posts on 20 October, relayed by a vendor and a news site | contradicted | refuted contradicted | 1/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. [fact timeline →](../../facts/rce-fpm/index.html) | PHP Foundation blog; GHSA-6wmf for the session path | disputed | **A6** Established●●●●●● | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) |
| Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 AugustThe hash tweet is dated 5 August 2026 on X; its pre-image has not been published, so what it commits to cannot be checked. [fact timeline →](../../facts/who-first/index.html) | Calif; PHP Foundation (report date) | confirmed | **A3** Echoed●●●○○○ opinion measures differently status overstated | 3/3 | [Calif](../../sources/calif-php2shell/index.html) [Ryan Austin, Calif on X](../../sources/x-lcfr-hax-hash-tweet/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) |
| OpenAI independently reported the same root cause on 11 August, with further vectors on 18 SeptemberThe GitHub advisories credit amyb-oai among four reporters. OpenAI's own post credits Calif's discovery 'using GPT-5.6 Sol' and Wiz; an X Community Note disputes OpenAI's role. [fact timeline →](../../facts/openai-same-day/index.html) | PHP Foundation | reported | **A2** Reported●●○○○○ disputed | 2/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| Wiz Research independently discovered the first flaw on 19 August and reported on 24 AugustWiz's X post says 'Wiz Research uncovers' with no credit to Calif or OpenAI; the blog thanks both. [fact timeline →](../../facts/wiz-independent/index.html) | Wiz; PHP Foundation (24 August) | reported | **A2** Reported●●○○○○ | 2/2 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) |
| The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixedTwo parties agree. The Foundation calls the delay 'a structural failure'. Cloudflare lists Quarkslab among the 2026 disclosers; nobody else does. [fact timeline →](../../facts/quarkslab-2024/index.html) | PHP Foundation; Calif | confirmed | **A2** Reported●●○○○○ disputed status overstated | 2/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Calif](../../sources/calif-php2shell/index.html) |
| On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social media with a wrong release time and a wrong CVSS score; no technical details leakedPrimary party. The Foundation does not say who or where. [fact timeline →](../../facts/leak-cve-ids/index.html) | PHP Foundation | reported | **A4** Corroborated●●●●○○ disputed | 2/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../sources/phpfoundation-blog-security-release-leak/index.html) |
| Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'Calif's own page does not mention a leak or a deleted video; it embeds two demo videos. Whether one of them is the deleted video is unknown. [fact timeline →](../../facts/leak-video/index.html) | PHP Foundation | reported | **A3** Echoed●●●○○○ | 3/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../sources/phpfoundation-blog-security-release-leak/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Calif](../../sources/calif-php2shell/index.html) |
| Mitigation advice given to a few critical-infrastructure providers from about 23:00 UTC on 20 October may have leaked [fact timeline →](../../facts/leak-mitigations/index.html) | PHP Foundation | reported | **A2** Reported●●○○○○ | 1/1 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) |
| Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built images containing the fixDan Lorenc (via The Register): 'I made the call to get these out early when exploits hit in the wild'; several unnamed vendors had reported exploits; Chainguard's honeypots trapped IPs; a researcher warned the company on the Friday and its team then found the bugs independently with an AI harness. No evidence published. The PHP security team found no functional exploit by release time. [fact timeline →](../../facts/chainguard/index.html) | PHP Foundation; Chainguard's CEO accepts the time and denies leaking | disputed | **A2** Reported●●○○○○ opinion disputed | 1/3 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [The Register](../../sources/theregister-php-blames-chainguard/index.html) [Feross Aboukhadijeh on X on X](../../sources/x-feross-chainguard/index.html) |
| The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leakThe php.net ChangeLog still dates all four releases 22 October. Wiz's X thread still says 22 October. [fact timeline →](../../facts/release-moved/index.html) | PHP Foundation; php.net pre-announcement; Wiz thread ('Apply the Oct 22 security release') | confirmed | **A4** Corroborated●●●●○○ measures differently status overstated | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [php.net](../../sources/php-net-changelog-8/index.html) |
| The pre-announcement was published at 19:30 UTC on 20 OctoberThe php.net feed says 20:32 UTC; oss-security relayed it at 20:22:51 UTC, so it was public by then. [fact timeline →](../../facts/preannounce-time/index.html) | PHP Foundation | disputed | **A2** Reported●●○○○○ disputed | 3/3 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [php.net](../../sources/php-net-advisory/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2024 | Quarkslab audits PHP (funded through OSTIF and the Sovereign Tech Agency). While fixing one of its findings a PHP core developer finds the first signs of the out-of-memory problem behind CVE-2026-109618; an exploit is theorised but no vector found, so it is not fixed. | stated |
| 2026-07-30 | Calif begins an audit of PHP under Patch the Planet; Volker Dusch accepts the invitation. | stated |
| 2026-08-11 | Calif reports the first bug to PHP and coordinated disclosure begins. OpenAI independently reports the same root cause the same day. | stated |
| 2026-08-24 | Wiz reports to the PHP security team. | stated |
| 2026-09-18 | Further attack vectors reported by OpenAI. | stated |
| 2026-10-20 15:00 UTC | The two CVE IDs begin circulating on forums and social media with a wrong release time and a wrong CVSS of 10.0. Per Daubois: an anonymous Hacker News post, then screenshots, a 'PHP2Shell tool' screenshot credited to Calif.io, a short exploitation video, and watchTowr posting both CVE numbers. | stated |
| 2026-10-20 19:30 UTC | php.net publishes the pre-announcement: release moved to 21 October 14:00 UTC, two critical vulnerabilities, CVSS v4.0 9.2, 'we reserve the right to release earlier'. | disputed |
| 2026-10-20 20:00 UTC | Calif 'mistakenly published a video' showing its proof of concept against several targets; copies circulate after it is deleted. | stated |
| 2026-10-20 23:00 UTC | The PHP project starts giving mitigation advice to a few critical-infrastructure providers; it 'may have leaked as well'. | stated |
| 2026-10-21 07:41 UTC | Chainguard publishes built images containing the fix, 'more than six hours before the coordinated release'. | stated |
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| more than 6 hours | before the coordinated release, Chainguard published built images with the fix | reported |

### Exploitation signals from this source
- [2026-10-21](../../exploitation/index.html): 'did not identify any functional exploits at the time of release/public disclosure.'

## The bytes
capture 20261022T080901Z · HTTP 200 · https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/- `headers.json` c18914982a4c07d0a15b76e052d18c5f77f345016e356ea5cb65e766f0096b0f 857 bytes
- `page.html` 6b8915a800a5311c06544c4c47fe0e6b69586e9d75aeab49d2922a6a71446223 40,324 bytes
- `provenance.json` 2acdcc9ae9ee9e14a8960ed26727dee21b5561915fc6632378e78c9ae27a3f1b 1,218 bytes
- `rendered.html` 874a78d766936a3c9d375512a1882ac83f25921f0a1050ed8169c5f37ea72cf2 126,413 bytes
- `screenshot.png` f6eb5d0b42048f1570880df5c5e38adea3d5ee8635a98b8fef51f6234e5d2089 2,631,098 bytes
- `text.txt` a1be057adc1c5bfabad6a59007bd08960168346230f03967fba68f2402ab3f04 31,882 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/php-foundation-blog-security-release/index.html
