# Source: Security advisory: Critical remote code execution vulnerabilities, update now

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

PHP Group (php.net): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Security advisory: Critical remote code execution vulnerabilities, update now

**PHP Group (php.net)** · [https://www.php.net/archive/2026.php#2026-10-21-5](https://www.php.net/archive/2026.php#2026-10-21-5) · published 2026-10-21 · added by `collector-primary` · slug `php-net-advisory`

Official php.net advisory (archive anchor 2026-10-21-5) plus the 8.2.35/8.3.36/8.4.27/8.5.12 release posts and the 20 Oct pre-announcement on the same page. Feed  timestamps (00:05-00:35Z on 21 Oct; 20:32Z on 20 Oct) do not match the Foundation's stated times (release 14:00Z, pre-announcement 19:30Z). raw/ holds feed.atom and a curl copy.

## What it says, as the collector read it

#### php.net security advisory: notes

- URL: https://www.php.net/archive/2026.php#2026-10-21-5 (news archive; the same page holds the four release posts and the 20 Oct pre-announcement)

- Captured 2026-10-22T08:09Z (capture.mjs); raw/feed.atom and raw/archive-2026.curl.html fetched with curl ~08:07-08:12Z.

- Publisher: the PHP Group / php.net. Date on the page: "21 Oct 2026".

#### Key wording (verbatim)

- "PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately."

- "Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs."

- "RCE via OOM corruption, CVE-2026-109618 (GHSA-w8hw-w9fx-j79w)"

- "RCE via stale global state, CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp)"

- "PHP 8.1 and older no longer receive updates from the PHP project." Minimal source backports were published as branches PHP-7.4/8.0/8.1-CVE-2026-109618-109619 on php/php-src.

- remirepo: "The repo will not have updates today."

- Mitigations: memory_limit=-1, low post_max_size (8M / 32M), session.upload_progress.enabled=0, on 8.5 fatal_error_backtraces=0. "only an update is a complete solution".

- Pre-announcement (anchor 2026-10-20-1, "Upcoming Critical PHP Security Release"): "It is scheduled for Wednesday, 21 October 2026 at 14:00 UTC." "It addresses two critical vulnerabilities, both rated CVSS v4.0 9.2."

#### Oddities

- Atom feed timestamps: advisory 2026-10-21T00:35:26+00:00; 8.2.35 00:05:37; 8.3.36 00:14:54; 8.4.27 00:20:54; 8.5.12 00:24:52; pre-announcement 2026-10-20T20:32:00+00:00. The Foundation blog says the pre-announcement went out at 19:30 UTC and the release at 14:00 UTC on 21 Oct, and GHSAs show 13:34Z. The php.net timestamps are the entry-creation times written by the authoring script, not verified publish times; do not use them as publication times without checking the php/web-php commit history.

- php.net's own date is 21 Oct; the BBC frames disclosure as 22 Oct (UK morning coverage). The original target date was 22 Oct 14:00 UTC (per Foundation blog).

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 [fact timeline →](../../facts/two-cves-9.2/index.html) | PHP Group (CNA), GitHub advisories, php.net | confirmed | **A6** Established●●●●●● | 5/5 | [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs [fact timeline →](../../facts/rce-modphp/index.html) | PHP security team (GHSA, oss-security), php.net | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe [fact timeline →](../../facts/only-update/index.html) | php.net; PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [php.net](../../sources/php-net-advisory/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| The flaws were disclosed on 22 October 2026Primary sources put the release at 21 October: GHSAs 13:34Z, tags 13:35Z, CVE records 13:48Z and 13:54Z, GitHub release 14:06Z. [fact timeline →](../../facts/disclosure-22oct/index.html) | BBC framing (UK morning coverage) | contradicted | refuted measures differently | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The pre-announcement was published at 19:30 UTC on 20 OctoberThe php.net feed says 20:32 UTC; oss-security relayed it at 20:22:51 UTC, so it was public by then. [fact timeline →](../../facts/preannounce-time/index.html) | PHP Foundation | disputed | **A2** Reported●●○○○○ disputed | 3/3 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [php.net](../../sources/php-net-advisory/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-20 19:30 UTC | php.net publishes the pre-announcement: release moved to 21 October 14:00 UTC, two critical vulnerabilities, CVSS v4.0 9.2, 'we reserve the right to release earlier'. | disputed |
| 2026-10-21 14:00 UTC | The planned release time. php.net's advisory 'Critical remote code execution vulnerabilities, update now' and the four release posts go up. | stated |

## The bytes
capture 20261022T080901Z · HTTP 200 · https://www.php.net/archive/2026.php#2026-10-21-5- `headers.json` 42812c4d4f151d93b62d63d08b84b83e50a94a9e2ab79427924d5b5df582cc72 899 bytes
- `page.html` 3b02b9e9f8ebedb87cbe39a2852c8cc3205067f59572000c730844fbc4a03555 99,388 bytes
- `provenance.json` b1c9672106ace3646ee3912d7e4e87d94dc91cc5b60b9acc1066295675ce5014 948 bytes
- `rendered.html` a8cbeb0c17b3646681217db64cce0e0beb6dc71765bd1bad550f8e20170ef7d0 238,404 bytes
- `screenshot.png` 4727eaed5a4a5a90eb95aed5c3c0093702f427e1aae4bc63ed9ccfea2ca92da4 3,983,360 bytes
- `text.txt` df0b1bba3deae2823b3f7c6200d5a4fafa1625c51cde86e50f650e0b0726b31e 35,947 bytes
raw, 2 files with SHA256SUMS- `archive-2026.curl.html` 3b02b9e9f8ebedb87cbe39a2852c8cc3205067f59572000c730844fbc4a03555
- `feed.atom` 79c12996a433f66b2e2422e32d1dd5d4251c7c24531f75c3a0611f58dc1894a8

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/php-net-advisory/index.html
