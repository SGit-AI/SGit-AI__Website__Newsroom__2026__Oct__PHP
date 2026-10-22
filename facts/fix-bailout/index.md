# Fact: The fix removes longjmp() for out-of-memory errors in favour of a delayed soft O

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout'

**Who says it:** PHP security team · **Sources:** [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html)

## This fact over time
- 2026-10-18 18:10 UTCphp-src publishes [Branch PHP-7.4-CVE-2026-109618-109619](../../sources/github-php-src-branch-7.4-backport/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:15 UTCSaved into the evidence vault: php.net
- 2026-10-22 08:15 UTCSaved into the evidence vault: php-src
- 2026-10-22Enters this site as confirmed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#fix-bailout).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · confirmed
```
The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout'
Who says it: PHP security team
Status: confirmed
Topic: technical
Sources: github-ghsa-w8hw-w9fx-j79w, php-net-changelog-8, github-php-src-branch-7.4-backport
```


---
site v0.4.3 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/facts/fix-bailout/index.html
