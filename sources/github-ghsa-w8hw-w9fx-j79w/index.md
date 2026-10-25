# Source: RCE via OOM corruption (CVE-2026-109618)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

PHP (php/php-src GitHub security advisory, published by bukka): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# RCE via OOM corruption (CVE-2026-109618)

**PHP (php/php-src GitHub security advisory, published by bukka)** · [https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) · published 2026-10-21T13:34:25Z · added by `collector-primary` · slug `github-ghsa-w8hw-w9fx-j79w`

CVSS v4 9.2 CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N. Affected

## What it says, as the collector read it

#### GHSA-w8hw-w9fx-j79w (CVE-2026-109618): notes

- URL: https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w. Title "RCE via OOM corruption". "Critical bukka published". Page time element: 2026-10-21T13:34:25Z. Captured 2026-10-22T08:09Z.

- GitHub REST API (repos/php/php-src/security-advisories/..., /advisories/...) was refused for this session (repository not attached), so no JSON was saved.

#### Key facts (verbatim)

- Affected versions: "

#### Contradiction

- The Foundation blog says RCE "was also confirmed on PHP-FPM through application-level code paths"; this GHSA says "no complete FPM exploit has been demonstrated for this SAPI". (Possibly the blog conflates with the 109619 session path validated on FPM.)

- The reporter handle "tomash-areion" is not named in the Foundation's thanks list.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 [fact timeline →](../../facts/two-cves-9.2/index.html) | PHP Group (CNA), GitHub advisories, php.net | confirmed | **A6** Established●●●●●● | 5/5 | [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs [fact timeline →](../../facts/rce-modphp/index.html) | PHP security team (GHSA, oss-security), php.net | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. [fact timeline →](../../facts/rce-fpm/index.html) | PHP Foundation blog; GHSA-6wmf for the session path | disputed | **A6** Established●●●●●● | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) |
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' [fact timeline →](../../facts/fix-bailout/index.html) | PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) |
| OpenAI independently reported the same root cause on 11 August, with further vectors on 18 SeptemberThe GitHub advisories credit amyb-oai among four reporters. OpenAI's own post credits Calif's discovery 'using GPT-5.6 Sol' and Wiz; an X Community Note disputes OpenAI's role. [fact timeline →](../../facts/openai-same-day/index.html) | PHP Foundation | reported | **A2** Reported●●○○○○ disputed | 2/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areiontomash-areion is not named in the PHP Foundation's thanks and appears nowhere else on this beat. [fact timeline →](../../facts/four-reporters/index.html) | GitHub security advisories | confirmed | **A6** Established●●●●●● | 2/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed requestThe fix replaces bailout with a delayed error and an UnwindExit at a safe point, adds a hard limit that _exits, and resets the globals. See the code page. [fact timeline →](../../facts/fix-engine/index.html) | php/php-src fix commit; the GitHub advisories | confirmed | **A6** Established●●●●●● | 3/3 | [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 13:34:13 UTC | GHSA-6wmf-4rv5-p3rp (CVE-2026-109619) and, twelve seconds later, GHSA-w8hw-w9fx-j79w (CVE-2026-109618) are published by bukka. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 9.2 | CVSS v4.0, each CVE | confirmed |

## The bytes
capture 20261022T080901Z · HTTP 200 · https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w- `headers.json` a5b68bac81984833a0df448856c563c0abaaf285f4eac25b6fc9a01c0b4d705f 5,447 bytes
- `page.html` f429f17d81fee9dced4234a3f88772e1a7fdb87170b5bf5e3c6a016758b2a14e 212,571 bytes
- `provenance.json` bb24fb081f4677b9fb91aac8bf728da3b708aec4d694572ccf432df9c0e5162b 1,035 bytes
- `rendered.html` 79647ef8c491692c787e535f84364db88577ccdd26a84a066643ac2d8f0a1110 214,403 bytes
- `screenshot.png` 4e10459ced9f68c1f9fb25ce9f8c603fad05b9e1981b2b9de3c10c16ade86d77 535,897 bytes
- `text.txt` 84ab95d3b1d538ba0ff48d9f7371e482501999c23847fbecb67de6840324bfc4 6,692 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-ghsa-w8hw-w9fx-j79w/index.html
