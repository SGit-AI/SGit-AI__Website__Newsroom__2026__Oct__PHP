# Source: What the PHP2Shell rumors got wrong, from inside the PHP security team

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Alexandre Daubois (PHP security team / PHP Foundation): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · researcher · secondary · captured

# What the PHP2Shell rumors got wrong, from inside the PHP security team

**Alexandre Daubois (PHP security team / PHP Foundation)** · [https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/](https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/) · published 2026-10-21 · added by `collector-researchers` · slug `daubois-blog-php2shell-rumors`

Personal blog of a PHP Foundation contractor on the PHP security team, dated 21 OCT 2026. Describes anonymous HN post Oct 20, leaked 'PHP2Shell tool' screenshot credited to Calif.IO, the short exploitation video, and watchTowr confirming the CVEs publicly. Gives GHSA advisory opened 2026-08-27 credited to lcfr-hax, sagitzadik-wiz, amyb-oai and tomash-areion.

## What it says, as the collector read it

#### Alexandre Daubois: "What the PHP2Shell rumors got wrong, from inside the PHP security team"

- URL https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/ ; "BLOG · 21 OCT 2026", "REV 2026.10.21". Author joined the PHP Foundation in July 2026 to help the security team (per the Foundation's post). Personal blog, not an official statement.

- How the leak happened (verbatim): "An anonymous Hacker News post citing a reliable source went up on October 20 and came down, but screenshots of it had already reached X and Mastodon. A screenshot of the PHP2Shell tool, credited to Calif.IO, leaked alongside the advisory, and a short exploitation video went up and came down the same way. Then watchTowr, writing that 'we were all supposed to wait until Thursday at 11am ET', confirmed in public that the bugs were real and posted both CVE numbers."

- Says the CVSS 10.0 traces to "Florian Roth's post, as Phoenix Security relayed it" and to watchTowr via Cyber Daily.

- Facts box: "Advisory opened: 2026-08-27, credited to lcfr-hax, sagitzadik-wiz, amyb-oai and tomash-areion"; "Fix PR opened: 2026-09-25, final commit 01a40e89fbfc authored 2026-10-18"; "Leak and advance notice: 2026-10-20"; "Published: 2026-10-21, 14:00 UTC".

- Contradiction: the PHP Foundation says "No technical details leaked" with the CVE IDs, yet Daubois describes a leaked tool screenshot and advisory. Also "tomash-areion" is a fourth credited reporter not named elsewhere on this beat.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The flaws are CVSS 10.0The PHP Foundation: 'a wrong CVSS score of 10.0 (the actual score is 9.2)'. Daubois traces it to a social post relayed by Phoenix Security and to watchTowr via Cyber Daily. [fact timeline →](../../facts/cvss-10/index.html) | social posts on 20 October, relayed by a vendor and a news site | contradicted | refuted contradicted | 1/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areiontomash-areion is not named in the PHP Foundation's thanks and appears nowhere else on this beat. [fact timeline →](../../facts/four-reporters/index.html) | GitHub security advisories | confirmed | **A6** Established●●●●●● | 2/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| The leak started with an anonymous Hacker News post citing a reliable source, which came down after screenshots spread; a screenshot of the 'PHP2Shell tool' credited to Calif.io and a short exploitation video also went up and came downContradicts the Foundation's 'no technical details leaked' and The Hacker News's 'a proof-of-concept exploit leaked'. No copy of the post, screenshot or video is in the vault. [fact timeline →](../../facts/leak-hn/index.html) | Alexandre Daubois (PHP security team, personal blog) | reported | **A4** Corroborated●●●●○○ disputed | 0/1 | [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| watchTowr confirmed in public that the bugs were real and posted both CVE numbers before the release [fact timeline →](../../facts/leak-watchtowr/index.html) | Daubois; CERT-EU lists a watchTowr X post among public reports | reported | **A4** Corroborated●●●●○○ | 1/2 | [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-08-27 | The GitHub security advisory is opened, credited to lcfr-hax, sagitzadik-wiz, amyb-oai and tomash-areion. | stated |
| 2026-09-25 | The fix pull request is opened. | stated |
| 2026-10-18 | The final fix commit is authored; the 7.4 backport branch's commit is dated 18:10:24Z. | stated |
| 2026-10-20 15:00 UTC | The two CVE IDs begin circulating on forums and social media with a wrong release time and a wrong CVSS of 10.0. Per Daubois: an anonymous Hacker News post, then screenshots, a 'PHP2Shell tool' screenshot credited to Calif.io, a short exploitation video, and watchTowr posting both CVE numbers. | stated |
| 2026-10-21 14:00 UTC | The planned release time. php.net's advisory 'Critical remote code execution vulnerabilities, update now' and the four release posts go up. | stated |
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

## The bytes
capture 20261022T081256Z · HTTP 200 · https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/- `headers.json` 7f4da02c6bd4388f7475aed4c30ba66fbfd5e93f9e9b69537b21005081745afa 1,049 bytes
- `page.html` 8f85e508b569e07d58f4ab54611fc7bb886c13f58b8c0448198f44899bf54d10 22,135 bytes
- `provenance.json` c86d302cfb9e3442fe758ce082c1015c8500db089f7e8350402efbd4b259241d 1,046 bytes
- `rendered.html` 8bc8f77f0b030a431c17cfb6048a516fae5d743bcf9af1d571e1a377dbe77fbd 21,926 bytes
- `screenshot.png` c86032b5d2ce179ae664684fe600ba45c0b3ff7003c835716b5cce042a13e514 817,325 bytes
- `text.txt` 5ef17f9886aa93f7f15ab1f6657ef6991a8ec008e5e309bdde5b5e51d961c4d8 8,821 bytes
capture 20261023T160435Z · HTTP 200 · https://daubois.dev/blog/cve-2026-109618-php2shell-rumors/- `headers.json` 623adbf1988184eb649cce8858aced007c5165ba6b98c43fcac0f6f8a553ecf2 1,113 bytes
- `page.html` cc22de0d3ddaa04114949ea038bb07fa1d246179a302856380c2588aaec8db33 22,135 bytes
- `provenance.json` 407a98c95ce52c1483f3569b75eb4c2e34948836cc0da42e26d58572bf9d913d 1,776 bytes
- `rendered.html` d1b60675fb382f85b3e100bba166f6ddcd6f6227bb577920e6ace8e38e0c86d4 21,926 bytes
- `screenshot.jpg` b6d33a9fcad21d4a5e0492ffaff604c34cb5abed436db0c682cea86e24546adb 585,832 bytes
- `text.txt` 530fd6cb980feec08028f50c58a1631f903305d34a3319fe86c46f0f1d71588a 8,821 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/daubois-blog-php2shell-rumors/index.html
