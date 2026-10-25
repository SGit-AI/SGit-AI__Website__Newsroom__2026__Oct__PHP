# Fact: watchTowr sees active exploitation attempts and lists the flaws as exploited in 

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild Who says it, its status (unverified), its sources, and its timeline from publication to this site.

Fact · exploitation · unverified

# watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild

**Who says it:** watchTowr · **Sources:** [watchTowr](../../sources/watchtowr-php2shell/index.html) [watchTowr](../../sources/watchtowr-php2shell-faq/index.html)

watchtowr.com returns HTTP 403 to this site's capture tool; known only from search summaries.

## Fact-check

**A6** Established●●●●●● · Attribution · verdict: **holds** · the status word understates the evidence

watchTowr's own pages are now captured (23 October): its intel page lists both CVEs as 'EXPLOITED IN THE WILD: Yes', and its FAQ says it 'has observed exploitation in the wild through its Attacker Eye honeypot network'. The claim is an attribution, and watchTowr's own page is the primary record of what watchTowr says: A6, and the site's 'unverified' understates it. What watchTowr measures is honeypot traffic, the same kind of evidence as Amazon's (K-002); its own words elsewhere say none of the sprayed exploits succeeded (Finding on the missing qualifier stays open).

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [watchtowr-php2shell](../../sources/watchtowr-php2shell/index.html) | blocked | *Access to watchtowr.com was denied* | 1837b6e2c766cabd |
| [watchtowr-php2shell-faq](../../sources/watchtowr-php2shell-faq/index.html) | blocked | *Access to watchtowr.com was denied* | 1837b6e2c766cabd |
| [securityweek-first-attempts-sensors](../../sources/securityweek-first-attempts-sensors/index.html) | carries | *it has seen the first in-the-wild exploitation attempts hitting its sensors around the same time the patches landed, but has not observed successful attempts.* | b63772dddccf9cee |
| [securityweek-exploitation-days-before](../../sources/securityweek-exploitation-days-before/index.html) | carries | *WatchTowr Intel is seeing broad exploitation attempts and sloppy proof-of-concept exploit code tweeted and thrown onto GitHub.* | ac663f2d9dbd0197 |
| [darkreading-php2shell-red-alert](../../sources/darkreading-php2shell-red-alert/index.html) | carries | *WatchTowr reported it has observed exploitation attempts of both flaws in the wild.* | 6db30e279f5f3877 |
| [therecord-php-warnings](../../sources/therecord-php-warnings/index.html) | carries | *the cybersecurity company is also observing in-the-wild exploitation of the vulnerabilities* | 39efe473da414c01 |
| [tenable-php2shell-faq](../../sources/tenable-php2shell-faq/index.html) | carries | *watchTowr says it has reproduced both vulnerabilities and is observing exploitation attempts against both.* | 10d98694b9c0243e |
| [equixly-php2shell-what-we-know](../../sources/equixly-php2shell-what-we-know/index.html) | absent | *watchTowr lists no reported exploitation, and neither CVE appears in CISA’s Known Exploited Vulnerabilities catalog.* | 34bf72d02f14deb9 |
| [securityweek-mass-exploitation-looms](../../sources/securityweek-mass-exploitation-looms/index.html) | absent | *WatchTowr and Huntress say they have not seen either of the vulnerabilities being exploited in the wild.* | 693aa4300139d2af |
| [watchtowr-php2shell](../../sources/watchtowr-php2shell/index.html) | carries | *EXPLOITED IN THE WILD: Yes , reported by watchTowr* | e09524178ed5f328 |
| [watchtowr-php2shell-faq](../../sources/watchtowr-php2shell-faq/index.html) | carries | *watchTowr has observed exploitation in the wild through its Attacker Eye honeypot network.* | 3c561d0c08e9343f |

Open tickets: [Contradiction-2](../../factcheck/index.html#Contradiction-2), [Finding-111](../../factcheck/index.html#Finding-111), [Finding-127](../../factcheck/index.html#Finding-127), [Finding-18](../../factcheck/index.html#Finding-18), [Finding-19](../../factcheck/index.html#Finding-19).

Graded in Run-6, resting on captures up to 2026-10-23 23:25 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-22 11:18 UTCSaved into the evidence vault: watchTowr, then 1 more capture
- 2026-10-22 11:18 UTCSaved into the evidence vault: watchTowr, then 1 more capture
- 2026-10-22Enters this site as unverified in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
AAlexCurious readerCCaseyWebsite ownerJJordanBoard member or executiveSSamSecurity leadBBlakeAnalyst or policy advisorRRobinCISOQQuinnCFOMMorganData protection officerJJamieHead of AppSec
And on [every claim](../../claims/index.html#watchtowr-itw).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · unverified
```
watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild
Who says it: watchTowr
Status: unverified
Topic: exploitation
Sources: watchtowr-php2shell, watchtowr-php2shell-faq
```


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/watchtowr-itw/index.html
