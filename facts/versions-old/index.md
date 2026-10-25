# Fact: All PHP versions from 5 onwards are affected by at least one of the flaws

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

All PHP versions from 5 onwards are affected by at least one of the flaws Who says it, its status (disputed), its sources, and its timeline from publication to this site.

Fact · technical · disputed

# All PHP versions from 5 onwards are affected by at least one of the flaws

**Who says it:** NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) · **Sources:** [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html)

The CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1.

## Fact-check

**A3** Echoed●●●○○○ disputed · State · verdict: **holds in part**

Wiz (a finder) says '>= 5.4'; PHP's own source backports for 7.4, 8.0 and 8.1 imply those are affected; only NCSC-NL and CERT-FR say all of 5.x, and both pre-release texts look like echoes of the leak (CERT-FR lists a 6.x that never shipped). The CVE records list only 8.2 to 8.5 with default unaffected. So 7.4+ is well supported, 5.4+ rests on Wiz, and 5.0 to 5.3 is not shown; disputed caps display at A2.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [ncsc-nl-advisories](../../sources/ncsc-nl-advisories/index.html) | carries | *Alle versies vanaf versie 5 zijn in ieder geval kwetsbaar.* | b7e4ac6caf7d177d |
| [x-wiz-io-php2shell](../../sources/x-wiz-io-php2shell/index.html) | partial | *All php versions >= 5.4 are affected by at least 1 of these vulnerabilities.* | 6c17977662815b0c |
| [certfr-2026-ale-014](../../sources/certfr-2026-ale-014/index.html) | carries | *PHP toutes versions 5.x PHP toutes versions 6.x PHP toutes versions 7.x* | f9e9557ab49ddb95 |
| [openwall-oss-security-109619-thread](../../sources/openwall-oss-security-109619-thread/index.html) | partial | *which implies that at least versions down to 7.4 are affected as well* | bbc0f0fc06953b13 |
| [cve-cve-2026-109618](../../sources/cve-cve-2026-109618/index.html) | absent | *Default Status: unaffected* | f8705d8e0aa2a248 |
| [php-net-advisory](../../sources/php-net-advisory/index.html) | partial | *the PHP security team provided minimal source-backports for PHP 7.4, PHP 8.0, and PHP 8.1* | df0b1bba3deae282 |
| [daubois-blog-php2shell-rumors](../../sources/daubois-blog-php2shell-rumors/index.html) | partial | *the same jump sits in the PHP-5.3 allocator. I have not seen an exploit shown on those old versions either.* | 5ef17f9886aa93f7 |
| [thehackernews-php2shell-unpatched-alert](../../sources/thehackernews-php2shell-unpatched-alert/index.html) | partial | *a post on HN said two PHP remote code execution flaws, rated CVSS 10.0 and affecting versions from PHP 5 onward* | 33ba8292e26406d7 |

Open tickets: [Contradiction-3](../../factcheck/index.html#Contradiction-3), [Evidence-16](../../factcheck/index.html#Evidence-16), [Evidence-9](../../factcheck/index.html#Evidence-9), [Finding-107](../../factcheck/index.html#Finding-107), [Finding-50](../../factcheck/index.html#Finding-50).

Graded in Run-1, resting on captures up to 2026-10-22 08:16 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21CERT-FR publishes [[Màj] Multiples vulnérabilités dans PHP (CERTFR-2026-ALE-014)](../../sources/certfr-2026-ale-014/index.html)
- 2026-10-21 13:32 UTCWiz on X publishes [Wiz on X: BREAKING ... #PHP2SHELL ... impacting 70% of the Internet](../../sources/x-wiz-io-php2shell/index.html)
- 2026-10-21 15:24 UTCoss-security publishes [Re: CVE-2026-109619 thread (21/16, 21/17, 21/23, 22/2)](../../sources/openwall-oss-security-109619-thread/index.html)
- 2026-10-22 08:13 UTCSaved into the evidence vault: CERT-FR
- 2026-10-22 08:16 UTCSaved into the evidence vault: NCSC-NL
- 2026-10-22 08:16 UTCSaved into the evidence vault: Wiz on X
- 2026-10-22Enters this site as disputed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#versions-old).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · disputed
```
All PHP versions from 5 onwards are affected by at least one of the flaws
Who says it: NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1)
Status: disputed
Topic: technical
Sources: ncsc-nl-advisories, x-wiz-io-php2shell, certfr-2026-ale-014, openwall-oss-security-109619-thread
```


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/versions-old/index.html
