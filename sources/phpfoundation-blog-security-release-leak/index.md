# Source: Today's PHP Security Release, and How We're Strengthening PHP Security

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The PHP Foundation: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Today's PHP Security Release, and How We're Strengthening PHP Security

**The PHP Foundation** · [https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) · published 2026-10-21 · added by `collector-researchers` · slug `phpfoundation-blog-security-release-leak`

Dated Oct 21, 2026. Primary account of the leak: CVE IDs circulating Oct 20 ~15:00 UTC; Calif 'mistakenly published a video' ~20:00 UTC; mitigation advice may have leaked; Chainguard broke embargo Oct 21 07:41 UTC. Captured text also contains reader comments below the post (lines ~90 onward) — those are third-party, unverified.

## What it says, as the collector read it

#### PHP Foundation blog, 21 Oct 2026: the leak and the discovery timeline (collector-researchers)

Captured for the researchers/leak beat; the advisory collectors may hold their own copy.

#### Discovery (verbatim)

- 2024: "While fixing one of the issues Quarkslab reported, a PHP core developer contracted by the PHP Foundation found the first signs of the OOM problem behind CVE-2026-109618. In 2024, a potential exploit for the OOM problem was theorized, but no concrete vectors were found".

- "The PHP Foundation got the PHP project into the Patch the Planet program, as part of which security firm Calif began an audit of PHP on July 30th, 2026. On August 11th researcher Ryan A at Calif reported an unconditional remote code execution with the same root cause as the OOM problem we had found in 2024. OpenAI independently reported the same root cause on the same day, followed by further attack vectors from OpenAI on September 18th and from Wiz on August 24th. More recently, Trail of Bits has also been auditing PHP."

- Tools: "Earlier this year, we worked with Alpha-Omega to scan PHP with Anthropic's Claude Mythos ... OpenAI's Daybreak Red for validating reports and exploits".

- Thanks "OpenAI Codex Security, especially Amy Burnett".

#### Leak (verbatim, section "Leak and disrupted disclosure")

- "The coordinated disclosure of these vulnerabilities worked well until 2 days ahead of the targeted release date."

- "On Tuesday, October 20th, at around 15:00 UTC, the two CVE IDs began circulating on online forums and social media. They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2). No technical details leaked." Pre-announcement moved to 19:30 UTC; release moved from Oct 22 14:00 UTC to Oct 21 14:00 UTC.

- "As a result of the leak and pre-announcement around 20:00 UTC, Calif, one of the security firms that had reported the issues, mistakenly published a video. It showed their proof of concept working against a number of targets and revealed a few additional, though limited, details about the vulnerabilities. Copies of the deleted video started circulating on social media soon after. The video contributed to accelerated development of various PoCs".

- "Mitigation advice we started providing to a few critical infrastructure providers around Oct 20th 23:00 UTC, may have leaked as well."

- "did not identify any functional exploits at the time of release/public disclosure."

- "On October 21st at 07:41 UTC ... Chainguard unilaterally broke the embargo and published built images containing the fix."

#### Odd / follow up

- Does not say WHO first leaked the CVE IDs, nor where. Daubois (same team) points to an anonymous Hacker News post.

- Text capture includes reader comments under the post (third-party; e.g. a commenter claims "sansec.io leaked one of the attack vectors ... in their page's metadata"; another notes ELLIO's first in-the-wild hit 55 min after Chainguard). Unverified.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social media with a wrong release time and a wrong CVSS score; no technical details leakedPrimary party. The Foundation does not say who or where. [fact timeline →](../../facts/leak-cve-ids/index.html) | PHP Foundation | reported | **A4** Corroborated●●●●○○ disputed | 2/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../sources/phpfoundation-blog-security-release-leak/index.html) |
| Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'Calif's own page does not mention a leak or a deleted video; it embeds two demo videos. Whether one of them is the deleted video is unknown. [fact timeline →](../../facts/leak-video/index.html) | PHP Foundation | reported | **A3** Echoed●●●○○○ | 3/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../sources/phpfoundation-blog-security-release-leak/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Calif](../../sources/calif-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-20 20:00 UTC | Calif 'mistakenly published a video' showing its proof of concept against several targets; copies circulate after it is deleted. | stated |
| 2026-10-21 08:36 UTC | ELLIO records its first sensor hit. | stated |

### Exploitation signals from this source
- [2026-10-21 08:36 UTC](../../exploitation/index.html): First sensor hit, about 55 minutes after Chainguard's images.

## The bytes
capture 20261022T081244Z · HTTP 200 · https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/- `headers.json` 3b9ca485b393afa38381b67bb251208dca58e32f815fd1aed95ba69e1d88dda3 856 bytes
- `page.html` 6b8915a800a5311c06544c4c47fe0e6b69586e9d75aeab49d2922a6a71446223 40,324 bytes
- `provenance.json` 777ac74e8e4915a67c651d019c1cdcf9a099773e9963221b097b676fa5054bde 1,222 bytes
- `rendered.html` 074da5662f04df8f88a2efc163726c553f5bb43c8095278a089daa0faf364955 126,414 bytes
- `screenshot.png` 09956999247e6e42a5635bb2b1234a2f8a11f0c66c26b88fafc020c31f3b6cd6 2,630,327 bytes
- `text.txt` b9f29cfdc1c0cd65dd505738d06d5f7d590d5d3da95801309990871870d2e0dd 31,883 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/phpfoundation-blog-security-release-leak/index.html
