# Fact: Unauthenticated RCE over HTTP against Apache mod_php with default settings, befo

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs

**Who says it:** PHP security team (GHSA, oss-security), php.net · **Sources:** [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html)

## Fact-check

**A6** Established●●●●●● · State · verdict: **holds**

GHSA-w8hw (the advisory record for CVE-2026-109618) says complete RCE was validated over HTTP against mod_php with default PHP input and memory limits, entirely before application code; oss-security and php.net repeat it. All parts carried by the primary record.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | carries | *Complete remote code execution was validated over HTTP against mod_php with default PHP input and memory limits and normal prefork configurations with multiple workers.* | 84ab95d3b1d538ba |
| [openwall-oss-security-2026-10-21-6](../../sources/openwall-oss-security-2026-10-21-6/index.html) | carries | *Unauthenticated RCE has been demonstrated over HTTP against Apache mod_php, before application code executes.* | 2f2d3ff13f3a32b7 |
| [php-net-advisory](../../sources/php-net-advisory/index.html) | partial | *We consider the risk highest for mod_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs.* | df0b1bba3deae282 |

Open tickets: [Contradiction-8](../../factcheck/index.html#Contradiction-8), [Finding-97](../../factcheck/index.html#Finding-97).

Graded in Run-1, resting on captures up to 2026-10-22 08:14 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21php.net publishes [Security advisory: Critical remote code execution vulnerabilities, update now](../../sources/php-net-advisory/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- 2026-10-21 14:41 UTCoss-security publishes [CVE-2026-109618: PHP 8.2–8.5 RCE via OOM corruption](../../sources/openwall-oss-security-2026-10-21-6/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:09 UTCSaved into the evidence vault: php.net
- 2026-10-22 08:14 UTCSaved into the evidence vault: oss-security
- 2026-10-22Enters this site as confirmed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#rce-modphp).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · confirmed
```
Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs
Who says it: PHP security team (GHSA, oss-security), php.net
Status: confirmed
Topic: technical
Sources: github-ghsa-w8hw-w9fx-j79w, openwall-oss-security-2026-10-21-6, php-net-advisory
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/rce-modphp/index.html
