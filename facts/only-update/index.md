# Fact: Updating is the only complete mitigation; the configuration measures reduce expo

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe

**Who says it:** php.net; PHP security team · **Sources:** [php.net](../../sources/php-net-advisory/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

## Fact-check

**A6** Established●●●●●● · Advice · verdict: **holds**

php.net's advisory carries the claim almost word for word, and both GHSAs and the oss-security post say updating is the only complete/reliable mitigation. The party's own records carry the advice.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [php-net-advisory](../../sources/php-net-advisory/index.html) | carries | *while only an update is a complete solution, the following measures reduce exposure to specific attack paths but do not make an installation safe.* | df0b1bba3deae282 |
| [openwall-oss-security-2026-10-21-7](../../sources/openwall-oss-security-2026-10-21-7/index.html) | carries | *Updating is the only reliable mitigation; there is no complete generic configuration workaround.* | ceef70b4943f7818 |
| [github-ghsa-6wmf-4rv5-p3rp](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) | carries | *Updating to a release containing the complete state reset patch is the only reliable mitigation.* | 99d85c973c41c024 |
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | carries | *Updating to a PHP release containing the patch to this vulnerability is the only complete mitigation.* | 84ab95d3b1d538ba |

Graded in Run-1, resting on captures up to 2026-10-22 08:14 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21php.net publishes [Security advisory: Critical remote code execution vulnerabilities, update now](../../sources/php-net-advisory/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via stale global state (CVE-2026-109619)](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)
- 2026-10-21 14:44 UTCoss-security publishes [CVE-2026-109619: PHP 8.2–8.5 RCE via stale global state](../../sources/openwall-oss-security-2026-10-21-7/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: php.net
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:14 UTCSaved into the evidence vault: oss-security
- 2026-10-22Enters this site as confirmed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#only-update).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · confirmed
```
Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe
Who says it: php.net; PHP security team
Status: confirmed
Topic: technical
Sources: php-net-advisory, openwall-oss-security-2026-10-21-7, github-ghsa-6wmf-4rv5-p3rp
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/only-update/index.html
