# Source: PHP 8 ChangeLog

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

PHP Group (php.net): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# PHP 8 ChangeLog

**PHP Group (php.net)** · [https://www.php.net/ChangeLog-8.php](https://www.php.net/ChangeLog-8.php) · published not stated · added by `collector-primary` · slug `php-net-changelog-8`

8.5.12, 8.4.27, 8.3.36, 8.2.35 entries dated '22 Oct 2026' (the original target date), although they were released 21 Oct. Core entry: 'Fixed GHSA-w8hw-w9fx-j79w, GHSA-6wmf-4rv5-p3rp (Avoid state corruption via bailout).' 8.5.12 and 8.4.27 also carry unrelated bug fixes.

## What it says, as the collector read it

#### php.net PHP 8 ChangeLog: notes

- Captured 08:15Z (and curl copy in raw/).

- Each of "Version 8.5.12", "Version 8.4.27", "Version 8.3.36" and "Version 8.2.35" is dated "22 Oct 2026". The release actually shipped on 21 Oct (php.net news, GitHub release at 14:06Z). The ChangeLog keeps the originally planned date, and nobody has corrected it.

- Security line (verbatim, identical in all four): "Fixed GHSA-w8hw-w9fx-j79w, GHSA-6wmf-4rv5-p3rp (Avoid state corruption via bailout)." CVE IDs are not printed on these lines, unlike earlier entries (e.g. 8.3.35 lists CVE-2026-91768).

- 8.3.36 and 8.2.35 contain only the security fix. 8.5.12 and 8.4.27 bundle normal bug fixes (GH-23644, GH-21999, GH-23980, a dl() use-after-free, etc.).

- The fix is "bailout": PHP's zend_bailout (longjmp) mechanism, consistent with the GHSA's description of removing longjmp() for OOM.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' [fact timeline →](../../facts/fix-bailout/index.html) | PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) |
| The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leakThe php.net ChangeLog still dates all four releases 22 October. Wiz's X thread still says 22 October. [fact timeline →](../../facts/release-moved/index.html) | PHP Foundation; php.net pre-announcement; Wiz thread ('Apply the Oct 22 security release') | confirmed | **A4** Corroborated●●●●○○ measures differently status overstated | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [php.net](../../sources/php-net-changelog-8/index.html) |

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T081558Z · HTTP 200 · https://www.php.net/ChangeLog-8.php- `headers.json` 7e0f775cb09c408472e389bec122b0fc703a450df430b26aca98e4539caf6f4f 892 bytes
- `page.html` 8d771e4a97a9457c8ff4dfff88d79661cf8b5d520666b8799a944f033e620e68 752,126 bytes
- `provenance.json` 08d9493b6d1480061ad20e23c5ea875c121bb9741f79ccf69dd923284133f1c9 919 bytes
- `rendered.html` 03ecb3465829e89ba578ae7bc7f36881fbbd37d9bc77ae5bb3c74bdd15e2d36a 751,162 bytes
- `screenshot.png` 0954e33d2a52ac1470b5c204eaaeea8d8fe811854486542ece88541cf7dbc526 15,023,593 bytes
- `text.txt` e39f8d2cb60ee8a58c5400536714b0688b198b31bc07685fd7cdada8f2f0dd70 417,190 bytes
raw, 1 files with SHA256SUMS- `ChangeLog-8.curl.html` 8d771e4a97a9457c8ff4dfff88d79661cf8b5d520666b8799a944f033e620e68

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/php-net-changelog-8/index.html
