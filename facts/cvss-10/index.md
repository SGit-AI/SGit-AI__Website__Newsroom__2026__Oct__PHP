# Fact: The flaws are CVSS 10.0

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The flaws are CVSS 10.0 Who says it, its status (contradicted), its sources, and its timeline from publication to this site.

Fact · technical · contradicted

# The flaws are CVSS 10.0

**Who says it:** social posts on 20 October, relayed by a vendor and a news site · **Sources:** [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html)

The PHP Foundation: 'a wrong CVSS score of 10.0 (the actual score is 9.2)'. Daubois traces it to a social post relayed by Phoenix Security and to watchTowr via Cyber Daily.

## Fact-check

refuted contradicted · Record · verdict: **refuted**

The CVE records (the authoritative record for the score) give 9.2 under CVSS 4.0 for both flaws, and the PHP Foundation names 10.0 as a wrong score from the leak. The statement is refuted; the site's status 'contradicted' matches.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [php-foundation-blog-security-release](../../sources/php-foundation-blog-security-release/index.html) | carries | *They came with a wrong release time and a wrong CVSS score of 10.0 (the actual score is 9.2).* | a1be057adc1c5bfa |
| [daubois-blog-php2shell-rumors](../../sources/daubois-blog-php2shell-rumors/index.html) | carries | *Florian Roth’s post, as Phoenix Security relayed it, said CVSS 10.0, and Cyber Daily reported watchTowr saying the same, while PHP’s own notice says 9.2.* | 5ef17f9886aa93f7 |
| [cve-cve-2026-109618](../../sources/cve-cve-2026-109618/index.html) | carries | *9.2 CRITICAL 4.0* | f8705d8e0aa2a248 |
| [cve-cve-2026-109619](../../sources/cve-cve-2026-109619/index.html) | carries | *9.2 CRITICAL 4.0* | 3162135e82a9edd4 |
| [thehackernews-php2shell-unpatched-alert](../../sources/thehackernews-php2shell-unpatched-alert/index.html) | carries | *The CVSS 10.0 figure is the leak's. PHP's rating is 9.2 on version 4.0 of the scale.* | 33ba8292e26406d7 |

Open tickets: [Contradiction-7](../../factcheck/index.html#Contradiction-7), [Finding-65](../../factcheck/index.html#Finding-65).

Graded in Run-1, resting on captures up to 2026-10-22 08:12 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21PHP Foundation publishes [Today's PHP Security Release, and How We're Strengthening PHP Security](../../sources/php-foundation-blog-security-release/index.html)
- 2026-10-21Daubois publishes [What the PHP2Shell rumors got wrong, from inside the PHP security team](../../sources/daubois-blog-php2shell-rumors/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP Foundation
- 2026-10-22 08:12 UTCSaved into the evidence vault: Daubois, then 1 more capture
- 2026-10-22Enters this site as contradicted in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#cvss-10).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · contradicted
```
The flaws are CVSS 10.0
Who says it: social posts on 20 October, relayed by a vendor and a news site
Status: contradicted
Topic: technical
Sources: php-foundation-blog-security-release, daubois-blog-php2shell-rumors
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/cvss-10/index.html
