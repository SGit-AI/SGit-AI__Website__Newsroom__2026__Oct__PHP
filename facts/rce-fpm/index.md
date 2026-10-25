# Fact: Remote code execution is confirmed on PHP-FPM

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Remote code execution is confirmed on PHP-FPM Who says it, its status (disputed), its sources, and its timeline from publication to this site.

Fact · technical · disputed

# Remote code execution is confirmed on PHP-FPM

**Who says it:** PHP Foundation blog; GHSA-6wmf for the session path · **Sources:** [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html)

GHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs.

## Fact-check

**A6** Established●●●●●● · State · verdict: **holds** · the status word understates the evidence

As worded, the claim is carried by the PHP security team's own advisory for CVE-2026-109619 (GHSA-6wmf) and its oss-security post, which say RCE was demonstrated on a normal dynamic FPM pool, given a suitable application operation. What is disputed is which flaw does it: the Foundation's blog puts FPM under CVE-2026-109618, whose own advisory says no complete FPM exploit was shown (K-008). That does not touch this claim, so the site's 'disputed' understates it.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [github-ghsa-6wmf-4rv5-p3rp](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) | carries | *The fatal backtrace path has confirmed RCE against mod_php. Session lifecycle RCE was validated against mod_php and FPM.* | 99d85c973c41c024 |
| [openwall-oss-security-2026-10-21-7](../../sources/openwall-oss-security-2026-10-21-7/index.html) | carries | *Unauthenticated RCE has been demonstrated against Apache mod_php and PHP-FPM. Exploitability depends on the affected state, configuration, and application behavior.* | ceef70b4943f7818 |
| [php-foundation-blog-security-release](../../sources/php-foundation-blog-security-release/index.html) | carries | *Remote code execution was also confirmed on PHP-FPM through application-level code paths.* | a1be057adc1c5bfa |
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | partial | *Source analysis therefore supports FPM as a susceptible, though no complete FPM exploit has been demonstrated for this SAPI.* | 84ab95d3b1d538ba |
| [openwall-oss-security-2026-10-21-6](../../sources/openwall-oss-security-2026-10-21-6/index.html) | partial | *Source analysis also indicates FPM susceptibility, although a complete FPM exploit has not been demonstrated.* | 2f2d3ff13f3a32b7 |

Open tickets: [Contradiction-8](../../factcheck/index.html#Contradiction-8), [Finding-48](../../factcheck/index.html#Finding-48), [Finding-49](../../factcheck/index.html#Finding-49), [Finding-96](../../factcheck/index.html#Finding-96).

Graded in Run-1, resting on captures up to 2026-10-22 08:14 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21PHP Foundation publishes [Today's PHP Security Release, and How We're Strengthening PHP Security](../../sources/php-foundation-blog-security-release/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via stale global state (CVE-2026-109619)](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- 2026-10-21 14:41 UTCoss-security publishes [CVE-2026-109618: PHP 8.2–8.5 RCE via OOM corruption](../../sources/openwall-oss-security-2026-10-21-6/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP Foundation
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:14 UTCSaved into the evidence vault: oss-security
- 2026-10-22Enters this site as disputed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#rce-fpm).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · disputed
```
Remote code execution is confirmed on PHP-FPM
Who says it: PHP Foundation blog; GHSA-6wmf for the session path
Status: disputed
Topic: technical
Sources: php-foundation-blog-security-release, github-ghsa-6wmf-4rv5-p3rp, github-ghsa-w8hw-w9fx-j79w, openwall-oss-security-2026-10-21-6
```


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/rce-fpm/index.html
