# Fact: Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35

**Who says it:** PHP Group (CNA), GitHub advisories, php.net · **Sources:** [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../../sources/php-net-advisory/index.html)

## Fact-check

**A6** Established●●●●●● · Record · verdict: **holds**

Both CVE records (CNA PHP Group) carry CVSS 4.0 9.2 CRITICAL and the four fixed-in versions; the two GHSAs, both oss-security announcements and php.net agree. The authoritative record carries every number, so A6.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [cve-cve-2026-109618](../../sources/cve-cve-2026-109618/index.html) | carries | *9.2 CRITICAL 4.0 CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N* | f8705d8e0aa2a248 |
| [cve-cve-2026-109619](../../sources/cve-cve-2026-109619/index.html) | carries | *affectedfrom 8.5.*before 8.5.12* | 3162135e82a9edd4 |
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | carries | *Patched versions 8.2.35 8.3.36 8.4.27 8.5.12* | 84ab95d3b1d538ba |
| [github-ghsa-6wmf-4rv5-p3rp](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) | carries | *Critical 9.2 / 10 CVSS v4 base metrics* | 99d85c973c41c024 |
| [php-net-advisory](../../sources/php-net-advisory/index.html) | carries | *PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution.* | df0b1bba3deae282 |
| [openwall-oss-security-2026-10-21-6](../../sources/openwall-oss-security-2026-10-21-6/index.html) | carries | *Severity: Critical (CVSS v4.0: 9.2)* | 2f2d3ff13f3a32b7 |

Open tickets: [Contradiction-3](../../factcheck/index.html#Contradiction-3), [Contradiction-7](../../factcheck/index.html#Contradiction-7), [Evidence-10](../../factcheck/index.html#Evidence-10), [Evidence-17](../../factcheck/index.html#Evidence-17), [Evidence-6](../../factcheck/index.html#Evidence-6).

Graded in Run-1, resting on captures up to 2026-10-22 08:14 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21php.net publishes [Security advisory: Critical remote code execution vulnerabilities, update now](../../sources/php-net-advisory/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via stale global state (CVE-2026-109619)](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)
- 2026-10-21 13:48 UTCCVE record publishes [CVE-2026-109618: RCE via OOM corruption](../../sources/cve-cve-2026-109618/index.html)
- 2026-10-21 13:54 UTCCVE record publishes [CVE-2026-109619: RCE via stale global state](../../sources/cve-cve-2026-109619/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:09 UTCSaved into the evidence vault: php.net
- 2026-10-22 08:12 UTCSaved into the evidence vault: CVE record
- 2026-10-22 08:12 UTCSaved into the evidence vault: CVE record
- 2026-10-22Enters this site as confirmed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#two-cves-9.2).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · confirmed
```
Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35
Who says it: PHP Group (CNA), GitHub advisories, php.net
Status: confirmed
Topic: technical
Sources: cve-cve-2026-109618, cve-cve-2026-109619, github-ghsa-w8hw-w9fx-j79w, github-ghsa-6wmf-4rv5-p3rp, php-net-advisory
```


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/two-cves-9.2/index.html
