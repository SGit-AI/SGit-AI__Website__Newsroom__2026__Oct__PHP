# Fact: VulnCheck counts about 2.6 million internet-facing hosts exposing PHP; Censys, o

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

VulnCheck counts about 2.6 million internet-facing hosts exposing PHP; Censys, of the 2.58 million hosts it saw, could read a version on 1.58 million, and 1.57 million of those were unpatched on 21 October Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · scale · reported

# VulnCheck counts about 2.6 million internet-facing hosts exposing PHP; Censys, of the 2.58 million hosts it saw, could read a version on 1.58 million, and 1.57 million of those were unpatched on 21 October

**Who says it:** VulnCheck and Censys, via The Hacker News and SecurityWeek · **Sources:** [THN](../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html)

Censys: 2.58 million hosts seen, 1.58 million reporting a version, 1.57 million not patched; nearly 3 million by 22 October. VirusTotal: 5.1 million IPs running PHP, 1.1 million announcing a version. Unit 42: 22.6 million systems that 'could be vulnerable' (via Insurance Business). Censys's own post was not found.

## Fact-check

**A2** Reported●●○○○○ · Count · verdict: **holds**

Rewritten to keep the counters apart: VulnCheck's 2.6 million hosts, and Censys's 1.57 million unpatched of the 1.58 million whose version it could read, of 2.58 million seen (Finding-34 fixed; K-004 now explained). Both reach the vault only through news outlets (Finding-100), so A2.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [thehackernews-php2shell-4days](../../sources/thehackernews-php2shell-4days/index.html) | carries | *VulnCheck's analysis has identified PHP on 2,608,039 internet-facing hosts, out of which over 700,000 hosts run PHP 3.x through 7.3.* | c1cb63141287484c |
| [securityweek-exploitation-days-before](../../sources/securityweek-exploitation-days-before/index.html) | carries | *roughly 1.58 million were reporting identifiable PHP versions, and approximately 1.57 million were not patched, Censys says.* | ac663f2d9dbd0197 |
| [securityweek-exploitation-days-before](../../sources/securityweek-exploitation-days-before/index.html) | carries | *VulnCheck was seeing more than 2.6 million internet-facing hosts running PHP, nearly all of which were vulnerable.* | ac663f2d9dbd0197 |
| [insurancebusiness-uk-councils-met](../../sources/insurancebusiness-uk-councils-met/index.html) | carries | *Palo Alto Networks’ Unit 42 has counted more than 22.6 million internet-facing systems that could be vulnerable.* | 89357150e0bc8363 |

Open tickets: [Contradiction-4](../../factcheck/index.html#Contradiction-4), [Finding-100](../../factcheck/index.html#Finding-100), [Finding-34](../../factcheck/index.html#Finding-34).

Graded in Run-3, resting on captures up to 2026-10-22 11:23 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-22THN publishes [Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed](../../sources/thehackernews-php2shell-4days/index.html)
- 2026-10-22SecurityWeek publishes [PHP2Shell Exploitation Started Days Before Patches - SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html)
- 2026-10-22 08:13 UTCSaved into the evidence vault: THN, then 1 more capture
- 2026-10-22 11:23 UTCSaved into the evidence vault: SecurityWeek, then 2 more captures
- 2026-10-22Enters this site as reported in v0.1.0 (reconstructed from git)
- 2026-10-22Reworded or re-sourced in v0.2.0 (reconstructed from git)
- 2026-10-24Reworded or re-sourced in v0.12.1

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
AAlexCurious readerJJordanBoard member or executiveSSamSecurity leadRRowanJournalistBBlakeAnalyst or policy advisorRRobinCISOQQuinnCFORRileyCommunications team
And on [every claim](../../claims/index.html#scale-2.6m-hosts).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · reported
```
PHP is exposed on 2,608,039 internet-facing hosts
Who says it: VulnCheck, via The Hacker News
Status: reported
Topic: scale
Sources: thehackernews-php2shell-4days
```
v2 · site v0.2.0 · 22 October 2026 · reportedPHP is exposed on 2,608,039about 2.6 million internet-facing hostshosts, of which Censys counted 1.57 million unpatched on 21 OctoberWho says it: VulnCheck,VulnCheck and Censys, via The Hacker News and SecurityWeekStatus: reportedTopic: scaleSources: thehackernews-php2shell-4daysthehackernews-php2shell-4days, securityweek-exploitation-days-beforev3 · site v0.12.1 · 24 October 2026 · reportedPHPVulnCheck is exposed oncounts about 2.6 million internet-facing hosts,hosts exposing PHP; Censys, of whichthe Censys2.58 countedmillion hosts it saw, could read a version on 1.58 million, and 1.57 million of those were unpatched on 21 OctoberWho says it: VulnCheck and Censys, via The Hacker News and SecurityWeek2 unchanged linesSources: thehackernews-php2shell-4days, securityweek-exploitation-days-before


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/scale-2.6m-hosts/index.html
