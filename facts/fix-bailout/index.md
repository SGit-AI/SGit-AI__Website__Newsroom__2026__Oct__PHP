# Fact: The fix removes longjmp() for out-of-memory errors in favour of a delayed soft O

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout'

**Who says it:** PHP security team · **Sources:** [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html)

## Fact-check

**A6** Established●●●●●● · Record · verdict: **holds**

GHSA-w8hw's Mitigation section states the mechanism in nearly these words, the php.net ChangeLog carries the exact line for all four releases, and the 7.4 branch commit carries the same title. Primary records carry all of it.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | carries | *It is replaced with a delayed, graceful soft OOM triggered at the next VM safe point, and an immediate hard OOM using _exit()* | 84ab95d3b1d538ba |
| [php-net-changelog-8](../../sources/php-net-changelog-8/index.html) | carries | *Fixed GHSA-w8hw-w9fx-j79w, GHSA-6wmf-4rv5-p3rp (Avoid state corruption via bailout).* | e39f8d2cb60ee8a5 |
| [github-php-src-branch-7.4-backport](../../sources/github-php-src-branch-7.4-backport/index.html) | carries | *Avoid state corruption via bailout* | bd71e98ee89b7c6c |

Open tickets: [Finding-70](../../factcheck/index.html#Finding-70).

Graded in Run-1, resting on captures up to 2026-10-22 08:15 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

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
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
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
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/fix-bailout/index.html
