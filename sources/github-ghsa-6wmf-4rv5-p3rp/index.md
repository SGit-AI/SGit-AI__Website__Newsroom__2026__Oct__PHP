# Source: RCE via stale global state (CVE-2026-109619)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

PHP (php/php-src GitHub security advisory, published by bukka): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# RCE via stale global state (CVE-2026-109619)

**PHP (php/php-src GitHub security advisory, published by bukka)** · [https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) · published 2026-10-21T13:34:13Z · added by `collector-primary` · slug `github-ghsa-6wmf-4rv5-p3rp`

CVSS v4 9.2, same vector as 109618. Use-after-free of worker global state across requests. Confirmed RCE mod_php (PHP 8.5 fatal_error_backtraces path) and session upload progress path on mod_php and FPM. GitHub API blocked; timestamp from page.

## What it says, as the collector read it

#### GHSA-6wmf-4rv5-p3rp (CVE-2026-109619): notes

- URL: https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp. Title "RCE via stale global state". Published by bukka; page time element 2026-10-21T13:34:13Z. Captured 2026-10-22T08:09Z. GitHub API blocked for this session.

#### Key facts (verbatim)

- Affected "

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 [fact timeline →](../../facts/two-cves-9.2/index.html) | PHP Group (CNA), GitHub advisories, php.net | confirmed | **A6** Established●●●●●● | 5/5 | [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. [fact timeline →](../../facts/rce-fpm/index.html) | PHP Foundation blog; GHSA-6wmf for the session path | disputed | **A6** Established●●●●●● | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) |
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe [fact timeline →](../../facts/only-update/index.html) | php.net; PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [php.net](../../sources/php-net-advisory/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areiontomash-areion is not named in the PHP Foundation's thanks and appears nowhere else on this beat. [fact timeline →](../../facts/four-reporters/index.html) | GitHub security advisories | confirmed | **A6** Established●●●●●● | 2/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed requestThe fix replaces bailout with a delayed error and an UnwindExit at a safe point, adds a hard limit that _exits, and resets the globals. See the code page. [fact timeline →](../../facts/fix-engine/index.html) | php/php-src fix commit; the GitHub advisories | confirmed | **A6** Established●●●●●● | 3/3 | [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 13:34:13 UTC | GHSA-6wmf-4rv5-p3rp (CVE-2026-109619) and, twelve seconds later, GHSA-w8hw-w9fx-j79w (CVE-2026-109618) are published by bukka. | stated |

## The bytes
capture 20261022T080901Z · HTTP 200 · https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp- `headers.json` 9474439a8ed75c50ba02584a2c67a564bf208b0caa8b2aefe0d7d2704e46c263 5,440 bytes
- `page.html` 93ff984c03081442f47f1c338683875fabf1741564d711e2a3862d71cef29fdd 221,023 bytes
- `provenance.json` ab199ddc3636b44804bf4b7da3949fe9d22f000959f8fc04c7f00eb3e416a0bb 1,039 bytes
- `rendered.html` 89eb250785b0066130856745323cc48cd37a515b3264c10da91dfee64deb45cb 222,855 bytes
- `screenshot.png` bb279a6b633c6e9d1de5a4778673aa4b3ed7dc5e1a1d9f08a3ba27c30f99820a 1,024,722 bytes
- `text.txt` 99d85c973c41c0242c944f052d5f13beee1b0e381b83f8f89416c986099db4fc 13,502 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-ghsa-6wmf-4rv5-p3rp/index.html
