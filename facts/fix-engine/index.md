# Fact: Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based ba

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed request Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed request

**Who says it:** php/php-src fix commit; the GitHub advisories · **Sources:** [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)

The fix replaces bailout with a delayed error and an UnwindExit at a safe point, adds a hard limit that _exits, and resets the globals. See the code page.

## Fact-check

**A6** Established●●●●●● · Record · verdict: **holds**

The fix commit itself (read from a clone, raw patch hashed in the vault) says 'Replace bailout on OOM with UnwindExit' and 'Properly reset various globals that may be accessed during startup', and removes zend_bailout() from the allocator; the two advisories describe the same two mechanisms. The authoritative record carries it.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [github-php-src-fix-commit-3584a98bd](../../sources/github-php-src-fix-commit-3584a98bd/index.html) | carries | *- Replace bailout on OOM with UnwindExit - Properly reset various globals that may be accessed during startup* | 26bed812bcc7c89e |
| [github-ghsa-w8hw-w9fx-j79w](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) | carries | *PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request.* | 84ab95d3b1d538ba |
| [github-ghsa-6wmf-4rv5-p3rp](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) | carries | *global state, such as error, session, object and extension state that is retained by a worker but points to memory owned by one request.* | 99d85c973c41c024 |

Open tickets: [Finding-71](../../factcheck/index.html#Finding-71).

Graded in Run-1, resting on captures up to 2026-10-22 08:15 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-18 15:26 UTCphp/php-src, read from a clone publishes [Commit 3584a98bd: Avoid state corruption via bailout (the php2shell fix) and the PHP-7.4 backport 712e60f9e](../../sources/github-php-src-fix-commit-3584a98bd/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via OOM corruption (CVE-2026-109618)](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- 2026-10-21 13:34 UTCPHP publishes [RCE via stale global state (CVE-2026-109619)](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html)
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22 08:09 UTCSaved into the evidence vault: PHP
- 2026-10-22Enters this site as confirmed in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#fix-engine).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · confirmed
```
Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed request
Who says it: php/php-src fix commit; the GitHub advisories
Status: confirmed
Topic: technical
Sources: github-php-src-fix-commit-3584a98bd, github-ghsa-w8hw-w9fx-j79w, github-ghsa-6wmf-4rv5-p3rp
```


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/fix-engine/index.html
