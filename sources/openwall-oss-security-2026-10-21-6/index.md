# Source: CVE-2026-109618: PHP 8.2–8.5 RCE via OOM corruption

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

oss-security list (Jakub Zelenka, PHP security team): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# CVE-2026-109618: PHP 8.2–8.5 RCE via OOM corruption

**oss-security list (Jakub Zelenka, PHP security team)** · [https://www.openwall.com/lists/oss-security/2026/10/21/6](https://www.openwall.com/lists/oss-security/2026/10/21/6) · published 2026-10-21T14:41:54Z · added by `collector-primary` · slug `openwall-oss-security-2026-10-21-6`

Date header Wed, 21 Oct 2026 16:41:54 +0200. Official PHP security team announcement.

## What it says, as the collector read it

#### oss-security 2026/10/21/6: notes

- From Jakub Zelenka (PHP security team; GitHub handle bukka, who published both GHSAs). Date 21 Oct 2026 16:41:54 +0200 = 14:41:54Z.

- Verbatim: "CVE: CVE-2026-109618 / Severity: Critical (CVSS v4.0: 9.2)". "Affected versions are PHP 8.2 before 8.2.35, PHP 8.3 before 8.3.36, PHP 8.4 before 8.4.27, and PHP 8.5 before 8.5.12."

- "Unauthenticated RCE has been demonstrated over HTTP against Apache mod_php, before application code executes. Source analysis also indicates FPM susceptibility, although a complete FPM exploit has not been demonstrated."

- "Updating is the only complete mitigation."

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs [fact timeline →](../../facts/rce-modphp/index.html) | PHP security team (GHSA, oss-security), php.net | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. [fact timeline →](../../facts/rce-fpm/index.html) | PHP Foundation blog; GHSA-6wmf for the session path | disputed | **A6** Established●●●●●● | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 14:41:54 UTC | Jakub Zelenka announces CVE-2026-109618 on oss-security; CVE-2026-109619 at 14:44:06Z. | stated |

## The bytes
capture 20261022T081408Z · HTTP 200 · https://www.openwall.com/lists/oss-security/2026/10/21/6- `headers.json` 716db9e977d3bc55b5045e260d9914e03196ed370f73c86c22880782e6a6a114 239 bytes
- `page.html` d43a7569e9b4ff185814a61ed2a17e0b058d4554558a9fee8e3a7a29810169c5 6,170 bytes
- `provenance.json` 9ab3756501428b0a77ed30c1d7ef15298f6a8edb131b1dc1436043a045609b4b 1,024 bytes
- `rendered.html` 0686ceff1b17dfaad334b167b4f0fbb9dc9cbcdc897203d210b9a1d7a9630269 6,426 bytes
- `screenshot.png` 6604c447fd5c7db94e64b0c9eeb75cd7301d461bd4f903890db31f9971d20236 146,765 bytes
- `text.txt` 2f2d3ff13f3a32b7b624d0c1f0e16f1d9172beabd52d42d7c20e504cb4cf8e4f 1,805 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/openwall-oss-security-2026-10-21-6/index.html
