# Source: Upcoming Critical PHP Security Release

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

oss-security list (Alan Coopersmith, Oracle): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Upcoming Critical PHP Security Release

**oss-security list (Alan Coopersmith, Oracle)** · [https://www.openwall.com/lists/oss-security/2026/10/20/34](https://www.openwall.com/lists/oss-security/2026/10/20/34) · published 2026-10-20T20:22:51Z · added by `collector-primary` · slug `openwall-oss-security-2026-10-20-34`

Date header Tue, 20 Oct 2026 13:22:51 -0700 (= 20:22:51Z). Quotes the php.net pre-announcement verbatim: scheduled 21 Oct 14:00 UTC, two vulns CVSS v4.0 9.2.

## What it says, as the collector read it

#### oss-security 2026/10/20/34: notes

- Posted by Alan Coopersmith (Oracle). Date: Tue, 20 Oct 2026 13:22:51 -0700 = 20:22:51Z.

- Relays the php.net pre-announcement verbatim: "It is scheduled for Wednesday, 21 October 2026 at 14:00 UTC." "It addresses two critical vulnerabilities, both rated CVSS v4.0 9.2." "We reserve the right to release earlier should details of either vulnerability become public, or should evidence of active exploitation appear in the wild."

- Timing evidence: the php.net pre-announcement was public by 20:22Z on 20 Oct. That fits the Foundation's "19:30 UTC" and contradicts php.net's own feed timestamp of 20:32:00+00:00.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leakThe php.net ChangeLog still dates all four releases 22 October. Wiz's X thread still says 22 October. [fact timeline →](../../facts/release-moved/index.html) | PHP Foundation; php.net pre-announcement; Wiz thread ('Apply the Oct 22 security release') | confirmed | **A4** Corroborated●●●●○○ measures differently status overstated | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [php.net](../../sources/php-net-changelog-8/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The pre-announcement was published at 19:30 UTC on 20 OctoberThe php.net feed says 20:32 UTC; oss-security relayed it at 20:22:51 UTC, so it was public by then. [fact timeline →](../../facts/preannounce-time/index.html) | PHP Foundation | disputed | **A2** Reported●●○○○○ disputed | 3/3 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [php.net](../../sources/php-net-advisory/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-20 19:30 UTC | php.net publishes the pre-announcement: release moved to 21 October 14:00 UTC, two critical vulnerabilities, CVSS v4.0 9.2, 'we reserve the right to release earlier'. | disputed |
| 2026-10-20 20:22:51 UTC | Alan Coopersmith relays the php.net pre-announcement to oss-security. | stated |
| 2026-10-21 14:00 UTC | The planned release time. php.net's advisory 'Critical remote code execution vulnerabilities, update now' and the four release posts go up. | stated |

## The bytes
capture 20261022T081408Z · HTTP 200 · https://www.openwall.com/lists/oss-security/2026/10/20/34- `headers.json` 716db9e977d3bc55b5045e260d9914e03196ed370f73c86c22880782e6a6a114 239 bytes
- `page.html` 46a94f610255e2ee75ab240c658666ef2589e34e4dd4fcb93b5c5e45fc9917d4 5,800 bytes
- `provenance.json` 04ff8e63e2b72caeb3d48ed4a44ecc28434a0414db9f8d59022e7b75af8ccb40 1,012 bytes
- `rendered.html` 5c80dc74b7328496b9f3ee62eef06aa707db7327bd0bcdd7ab9aa4f0c5a5a5d8 6,056 bytes
- `screenshot.png` c03f4fc0fefe0485485685cdf28d3e439a4b167b3022a946ee928be55cd4ee0d 120,872 bytes
- `text.txt` 57b273733e7d5fe658deca4275db17ad5fd01aeb06d84d973d55551983dfa392 1,415 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/openwall-oss-security-2026-10-20-34/index.html
