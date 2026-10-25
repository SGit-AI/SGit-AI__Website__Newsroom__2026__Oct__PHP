# Source: Security Advisory 2026-018: Critical Vulnerabilities in PHP

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

CERT-EU: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Security Advisory 2026-018: Critical Vulnerabilities in PHP

**CERT-EU** · [https://cert.europa.eu/publications/security-advisories/2026-018/](https://cert.europa.eu/publications/security-advisories/2026-018/) · published 2026-10-21 15:20:18 (as stated; timezone not given) · added by `collector-gov` · slug `certeu-sa-2026-018`

v1.0 and v1.1 both 21/10/2026. States the PHP fixes were released '21 October 2026 at 13:30 UTC'. CVSS 9.2 each. Advice: 'patch affected assets immediately. Where that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified.' Notes PoCs are circulating.

## What it says, as the collector read it

#### CERT-EU Security Advisory 2026-018: Critical Vulnerabilities in PHP

- Stated "Release Date: 21-10-2026 15:20:18" (no timezone; CERT-EU is in Brussels, so probably CEST = 13:20Z, but that is not stated). History: v1.0 "Initial publication" and v1.1 "Updates with additional information", both 21/10/2026.

- Captured 2026-10-22T08:13:29Z.

- Key claims (verbatim):

- "On 20 October 2026, the PHP project announced an upcoming security release addressing two critical vulnerabilities in PHP"

- "The PHP team released the fixes today, 21 October 2026 at 13:30 UTC, in PHP versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35"

- "Technical details are now being discussed publicly, and initial proofs of concept (PoCs) have begun to circulate. This raises the likelihood that attackers are already exploiting the vulnerabilities."

- CVE-2026-109618 (GHSA-w8hw-w9fx-j79w), CVSS 9.2, OOM memory corruption; CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp), CVSS 9.2, stale global state.

- "The PHP team considers mod_php the highest-risk setup."

- Exact advice: "CERT-EU advises organisations to patch affected assets immediately. Where that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified." Repeated under Recommendations as "isolating internet-facing resources from public networks".

- Temporary mitigations: memory_limit=-1 set via php_admin_value; low post_max_size; proxy-level request limits; cgroup memory limit (not RLIMIT_AS); session.upload_progress.enabled=0 and restart workers; on 8.5 fatal_error_backtraces=0.

- Notes "rpms.remirepo.net ... will not have updates on release day".

- Its references include a Mastodon post by @GossiTheDog (cyberplace.social/@GossiTheDog/117474220875882526) and an X post by watchTowr (x.com/watchtowrcyber/status/2112611507749982605) as "public reports". Those are for the social/researcher collectors.

- Differs from CERT-FR on the release time: CERT-FR quotes PHP's pre-announcement of 16:00 Paris (14:00 UTC); CERT-EU says released 13:30 UTC.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| watchTowr confirmed in public that the bugs were real and posted both CVE numbers before the release [fact timeline →](../../facts/leak-watchtowr/index.html) | Daubois; CERT-EU lists a watchTowr X post among public reports | reported | **A4** Corroborated●●●●○○ | 1/2 | [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | **A1** Weak signal●○○○○○ | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 13:30 UTC | CERT-EU's stated release time for the PHP fixes. | stated |
| 2026-10-21 15:20 UTC | CERT-EU Security Advisory 2026-018 (stated 15:20:18, timezone not given). | inferred |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 9.2 | CVSS v4.0, each CVE | confirmed |

### Agency rows from this source
- [CERT-EU](../../agencies/index.html): offline isolate

## The bytes
capture 20261022T081329Z · HTTP 200 · https://cert.europa.eu/publications/security-advisories/2026-018/- `headers.json` 035d980d7924b86c61cd912c5ae8e55b5adbdf20e9f99f9c780d7b37e830e596 1,370 bytes
- `page.html` 1cc49d8c9b94ac2e09eb5f4e2bcb732a0d1fd4f630eaedad06da28a295978e53 24,504 bytes
- `provenance.json` d5c1ea12a493fd9c195d90ee56eba85c93cd77d6131bce3ac08929d72f275820 999 bytes
- `rendered.html` abb92e1078d68ea54089f704855e78b2a71cee27a6244c2d3f26cd1b8c90b759 23,744 bytes
- `screenshot.png` 894baac8f7c1a2e25439f481a468e1c086cf4c783d11e7f020bb354120ef6c99 624,274 bytes
- `text.txt` c65c95cf165d9ed7ec5d362642e92dd918c77fdfca1d4f88b303db6a3ab24ae3 7,105 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/certeu-sa-2026-018/index.html
