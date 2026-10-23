# Fact: An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation ne

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild' Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · exploitation · reported

# An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'

**Who says it:** Amazon (CJ Moses, AWS Security Blog) · **Sources:** [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html)

Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims.

## Fact-check

**A2** Reported●●○○○○ disputed · Attribution · verdict: **holds**

Amazon's own post (now cited first) carries all three parts and the quoted sentence character for character; The Hacker News is an echo of the same Amazon post, not independent, so the level stays A2. Amazon's 'broadly exploited in the wild' is disputed by CISA's dated negative and by Austin and Huntress, partly because they measure different things (attempts versus successful compromise) at different times.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *Amazon Threat Intelligence identified a PHP2Shell exploitation attempt dating to Oct. 17, 2026, in MadPot telemetry, four days before public disclosure* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *The exploit attempt originated from an IP address associated with a commercial anonymization network.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *multiple proof of concept exploits for the vulnerability, with the earliest around 2026-10-21 0200 UTC.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *The actual payloads and choices in anonymization infrastructure varied, suggesting these were multiple actors.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *PHP2Shell is now being broadly exploited in the wild.* | 94315ded6e1175f2 |
| [thehackernews-php2shell-4days](../../sources/thehackernews-php2shell-4days/index.html) | carries | *as the flaws come under broad exploitation in the wild following the release of the patches.* | c1cb63141287484c |
| [securityweek-exploitation-days-before](../../sources/securityweek-exploitation-days-before/index.html) | partial | *The exploits being sprayed indiscriminately either don’t work at all, test for timing-based differences, or crash the target,* | ac663f2d9dbd0197 |

Open tickets: [Contradiction-2](../../factcheck/index.html#Contradiction-2), [Finding-122](../../factcheck/index.html#Finding-122), [Finding-14](../../factcheck/index.html#Finding-14), [Finding-60](../../factcheck/index.html#Finding-60).

Graded in Run-1, resting on captures up to 2026-10-22 11:17 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Amazon publishes [Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Securi](../../sources/aws-security-blog-madpot/index.html)
- 2026-10-22THN publishes [Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed](../../sources/thehackernews-php2shell-4days/index.html)
- 2026-10-22 08:13 UTCSaved into the evidence vault: THN
- 2026-10-22 11:17 UTCSaved into the evidence vault: Amazon
- 2026-10-22Enters this site as reported in v0.1.0 (reconstructed from git)
- 2026-10-22Reworded or re-sourced in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
AAlexCurious readerCCaseyWebsite ownerJJordanBoard member or executiveSSamSecurity leadBBlakeAnalyst or policy advisorRRobinCISOQQuinnCFOMMorganData protection officerJJamieHead of AppSec
And on [every claim](../../claims/index.html#amazon-honeypot).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · reported
```
An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network, and proof-of-concept attempts started about 02:00 UTC on 21 October
Who says it: CJ Moses, Amazon, via The Hacker News
Status: reported
Topic: exploitation
Sources: thehackernews-php2shell-4days
```
v2 · site v0.2.0 · 22 October 2026 · reportedAn exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network, andnetwork; proof-of-concept attempts startedbegan about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'Who says it: CJAmazon (CJ Moses, Amazon,AWS viaSecurity The Hacker NewsBlog)Status: reportedTopic: exploitationSources: aws-security-blog-madpot, thehackernews-php2shell-4days


---
site v0.10.8 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/facts/amazon-honeypot/index.html
