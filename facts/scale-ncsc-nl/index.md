# Fact: 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under inves

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · scale · confirmed

# 674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable

**Who says it:** NCSC-NL, counted by this site from the file at commit cca173c64ec5 · **Sources:** [NCSC-NL](../../sources/ncsc-nl-php2shell-software-list/index.html)

Counted, not quoted. NCSC-NL calls unbacked entries 'investigation leads'.

## Fact-check

**A1** Weak signal●○○○○○ contradicted status overstated · Count · verdict: **holds in part** · the status word overstates the evidence

The inventory files at commit cca173c64ec5 are in the vault (tree and git bundle), and counting them gives 675 rows: 206 Vulnerable, 46 Fix, 418 Investigation, 4 Not vuln and 1 row with no status. The 206/46/418 figures hold; the total 674 and '3 not vulnerable' are contradicted by the file itself, because the vault's parsed JSON dropped the iBabs row. 'Confirmed' overstates a count the file contradicts.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [ncsc-nl-php2shell-software-list](../../sources/ncsc-nl-php2shell-software-list/index.html) | absent | *List of software with PHP dependency potentially affected by php2shell CVEs* | 83f3aa60070e20b8 |
| [ncsc-nl-php2shell](../../sources/ncsc-nl-php2shell/index.html) | partial | *"count": 674,* | f0a17e96a336a878 |
| [ncsc-nl-php2shell](../../sources/ncsc-nl-php2shell/index.html) | carries | *\|iBabs\|iBabs bestuursportaal\|\|Not vuln\|Not vuln\|PHP is not being used in iBabs.* | f25e5ef68d476c05 |
| [ncsc-nl-php2shell](../../sources/ncsc-nl-php2shell/index.html) | carries | *Product entries should still be treated as investigation leads until they are backed by an upstream or vendor source* | f651662623352976 |
| [ncsc-nl-php2shell](../../sources/ncsc-nl-php2shell/index.html) | carries | *nothing that carries it* | 4a72bcc9bbc58e88 |

Open tickets: [Finding-105](../../factcheck/index.html#Finding-105), [Finding-120](../../factcheck/index.html#Finding-120), [Finding-35](../../factcheck/index.html#Finding-35), [Finding-36](../../factcheck/index.html#Finding-36), [Finding-37](../../factcheck/index.html#Finding-37).

Graded in Run-1, resting on captures up to 2026-10-22 08:48 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-22 08:48 UTCSaved into the evidence vault: NCSC-NL
- 2026-10-22Enters this site as confirmed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
AAlexCurious readerJJordanBoard member or executiveSSamSecurity leadRRowanJournalistBBlakeAnalyst or policy advisorRRobinCISOQQuinnCFORRileyCommunications team
And on [every claim](../../claims/index.html#scale-ncsc-nl).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · confirmed
```
674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable
Who says it: NCSC-NL, counted by this site from the file at commit cca173c64ec5
Status: confirmed
Topic: scale
Sources: ncsc-nl-php2shell-software-list
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/scale-ncsc-nl/index.html
