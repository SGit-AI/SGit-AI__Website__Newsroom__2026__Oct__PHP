# Fact: The fixes were released at 14:00 UTC on 21 October

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fixes were released at 14:00 UTC on 21 October Who says it, its status (disputed), its sources, and its timeline from publication to this site.

Fact · timing · disputed

# The fixes were released at 14:00 UTC on 21 October

**Who says it:** php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) · **Sources:** [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html)

CERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times.

## Fact-check

**A2** Reported●●○○○○ disputed · Event · verdict: **holds in part**

21 October is carried by every primary record. 14:00 UTC was the scheduled time (php.net pre-announcement, oss-security relay, CERT-FR, ACSC 0100 AEDT); only Daubois states it after the event ('Published: 2026-10-21, 14:00 UTC'). The artifacts are stamped earlier and later: GHSA 13:34Z, tags 13:35:38 UTC, CVE records 13:48Z and 13:54Z, GitHub release 14:06:46Z; CERT-EU says 13:30 UTC. 'Disputed' fits.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [openwall-oss-security-2026-10-20-34](../../sources/openwall-oss-security-2026-10-20-34/index.html) | partial | *> It is scheduled for Wednesday, 21 October 2026 at 14:00 UTC.* | 57b273733e7d5fe6 |
| [daubois-blog-php2shell-rumors](../../sources/daubois-blog-php2shell-rumors/index.html) | carries | *Published: 2026-10-21, 14:00 UTC* | 5ef17f9886aa93f7 |
| [certfr-2026-ale-014](../../sources/certfr-2026-ale-014/index.html) | partial | *L'éditeur annonce la disponibilité des correctifs de sécurité pour le 21 octobre 2026 à 16h00 heure de Paris (14h00 UTC).* | f9e9557ab49ddb95 |
| [certeu-sa-2026-018](../../sources/certeu-sa-2026-018/index.html) | partial | *The PHP team released the fixes today, 21 October 2026 at 13:30 UTC, in PHP versions 8.5.12, 8.4.27, 8.3.36 and 8.2.35* | c65c95cf165d9ed7 |
| [github-php-src-tags](../../sources/github-php-src-tags/index.html) | partial | *datetime="2026-10-21 13:35:38 UTC"* | ca0a96e8466a3479 |
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | partial | *datetime="2026-10-21T13:34:25Z"* | 79647ef8c491692c |
| [github-php-src-tag-php-8.5.12](../../sources/github-php-src-tag-php-8.5.12/index.html) | partial | *datetime="2026-10-21T14:06:46Z"* | 330630ed887249f6 |
| [php-net-advisory](../../sources/php-net-advisory/index.html) | partial | *It is scheduled for Wednesday, 21 October 2026 at 14:00 UTC.* | df0b1bba3deae282 |
| [php-foundation-blog-security-release](../../sources/php-foundation-blog-security-release/index.html) | partial | *It also moved the release from October 22nd, 14:00 UTC, to October 21st, 14:00 UTC.* | a1be057adc1c5bfa |

Open tickets: [Contradiction-10](../../factcheck/index.html#Contradiction-10), [Finding-39](../../factcheck/index.html#Finding-39), [Finding-99](../../factcheck/index.html#Finding-99).

Graded in Run-1, resting on captures up to 2026-10-22 08:15 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-20 20:22 UTCoss-security publishes [Upcoming Critical PHP Security Release](../../sources/openwall-oss-security-2026-10-20-34/index.html)
- 2026-10-21Daubois publishes [What the PHP2Shell rumors got wrong, from inside the PHP security team](../../sources/daubois-blog-php2shell-rumors/index.html)
- 2026-10-21CERT-FR publishes [[Màj] Multiples vulnérabilités dans PHP (CERTFR-2026-ALE-014)](../../sources/certfr-2026-ale-014/index.html)
- 2026-10-21php.net publishes [Security advisory: Critical remote code execution vulnerabilities, update now](../../sources/php-net-advisory/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- 2026-10-21 14:06 UTCphp-src publishes [Release PHP 8.5.12](../../sources/github-php-src-tag-php-8.5.12/index.html)
- 2026-10-21 15:20 UTCCERT-EU publishes [Security Advisory 2026-018: Critical Vulnerabilities in PHP](../../sources/certeu-sa-2026-018/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:09 UTCSaved into the evidence vault: php.net
- 2026-10-22 08:12 UTCSaved into the evidence vault: Daubois, then 1 more capture
- 2026-10-22 08:13 UTCSaved into the evidence vault: CERT-FR
- 2026-10-22 08:13 UTCSaved into the evidence vault: CERT-EU
- 2026-10-22 08:14 UTCSaved into the evidence vault: oss-security
- 2026-10-22 08:15 UTCSaved into the evidence vault: php-src
- 2026-10-22 08:15 UTCSaved into the evidence vault: php-src
- 2026-10-22Enters this site as disputed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
TTaylorProject or programme managerRRowanJournalistBBlakeAnalyst or policy advisorAAveryCTO
And on [every claim](../../claims/index.html#release-time).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · disputed
```
The fixes were released at 14:00 UTC on 21 October
Who says it: php.net pre-announcement; Daubois; CERT-FR (16:00 Paris)
Status: disputed
Topic: timing
Sources: openwall-oss-security-2026-10-20-34, daubois-blog-php2shell-rumors, certfr-2026-ale-014, certeu-sa-2026-018, github-php-src-tags, github-ghsa-w8hw-w9fx-j79w, github-php-src-tag-php-8.5.12, php-net-advisory
```


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/release-time/index.html
