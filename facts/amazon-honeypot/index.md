# Fact: An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation ne

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild' Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · exploitation · reported

# An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'

**Who says it:** Amazon (CJ Moses, AWS Security Blog) · **Sources:** [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html)

Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims.

## Fact-check

**A2** Reported●●○○○○ superseded · Attribution · verdict: **holds in part**

The quoted words were Amazon's in its post as captured at 11:17 UTC on 22 October. Amazon revised the sentence at 21:25 UTC that day, without a note, to 'now seeing broad exploitation attempts in the wild'; the vault's 23 October capture carries the new wording. The claim gives the first wording as Amazon's without its date. The rest (17 October honeypot hit, PoC attempts from 02:00 UTC on 21 October) holds as Amazon wrote it; one party, A2.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *Amazon Threat Intelligence identified a PHP2Shell exploitation attempt dating to Oct. 17, 2026, in MadPot telemetry, four days before public disclosure* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *The exploit attempt originated from an IP address associated with a commercial anonymization network.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *multiple proof of concept exploits for the vulnerability, with the earliest around 2026-10-21 0200 UTC.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *The actual payloads and choices in anonymization infrastructure varied, suggesting these were multiple actors.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | carries | *PHP2Shell is now being broadly exploited in the wild.* | 94315ded6e1175f2 |
| [thehackernews-php2shell-4days](../../sources/thehackernews-php2shell-4days/index.html) | carries | *as the flaws come under broad exploitation in the wild following the release of the patches.* | c1cb63141287484c |
| [securityweek-exploitation-days-before](../../sources/securityweek-exploitation-days-before/index.html) | partial | *The exploits being sprayed indiscriminately either don’t work at all, test for timing-based differences, or crash the target,* | ac663f2d9dbd0197 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | partial | *PHP2Shell is now seeing broad exploitation attempts in the wild.* | 4108b2850c48a8f2 |

Open tickets: [Contradiction-2](../../factcheck/index.html#Contradiction-2), [Evidence-12](../../factcheck/index.html#Evidence-12), [Finding-122](../../factcheck/index.html#Finding-122), [Finding-126](../../factcheck/index.html#Finding-126), [Finding-14](../../factcheck/index.html#Finding-14), [Finding-60](../../factcheck/index.html#Finding-60).

Graded in Run-5, resting on captures up to 2026-10-23 16:04 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Amazon publishes [Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Securi](../../sources/aws-security-blog-madpot/index.html)
- 2026-10-22THN publishes [Someone Tried to Exploit PHP2Shell 4 Days Before the Vulnerabilities Were Publicly Disclosed](../../sources/thehackernews-php2shell-4days/index.html)
- 2026-10-22 08:13 UTCSaved into the evidence vault: THN, then 1 more capture
- 2026-10-22 11:17 UTCSaved into the evidence vault: Amazon, then 1 more capture
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
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/amazon-honeypot/index.html
