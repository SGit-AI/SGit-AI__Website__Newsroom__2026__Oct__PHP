# Fact: No named organisation has confirmed a compromise through php2shell

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

No named organisation has confirmed a compromise through php2shell Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · impact · confirmed

# No named organisation has confirmed a compromise through php2shell

**Who says it:** this site, from every captured source · **Sources:** [CISA](../../sources/cisa-kev-json/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html)

A negative finding as of the latest capture. Amazon says 'broadly exploited' against sensors; Weird Gloop expects old forums to have been hit; CISA has not listed either CVE.

## Fact-check

**A4** Corroborated●●●●○○ status overstated · State · verdict: **holds** · the status word overstates the evidence

A search of every vault capture (manifest and unexported) finds no named organisation confirming a php2shell compromise, and several independent parties say none known (Huntress, Imperva, CERT.LV, the German digital ministry via Reuters, the Australian industry minister). A universal negative from a finite, time-bound capture set cannot exceed A4, and it is volatile; "confirmed" without an as-of in the claim text is overstated.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [cisa-kev-json](../../sources/cisa-kev-json/index.html) | partial | *nothing that carries it* | ef8fffede5c47200 |
| [huntress-php2shell-rapid-response](../../sources/huntress-php2shell-rapid-response/index.html) | carries | *As of October 21 at 4:30pm ET, Huntress has not observed in-the-wild exploitation on partner systems.* | a83d744768109a61 |
| [huntress-php2shell-rapid-response](../../sources/huntress-php2shell-rapid-response/index.html) | carries | *No indicators of compromise have been confirmed yet.* | a83d744768109a61 |
| [imperva-blog-php2shell](../../sources/imperva-blog-php2shell/index.html) | partial | *During this pre-disclosure monitoring period, Imperva observed no traffic matching the monitored PHP2Shell exploit patterns.* | 3da873bdb21219a6 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | partial | *Technical analysis is ongoing, and it’s unclear if any of these attempts would have succeeded in real-world systems.* | 94315ded6e1175f2 |
| [aws-security-blog-madpot](../../sources/aws-security-blog-madpot/index.html) | partial | *PHP2Shell is now being broadly exploited in the wild.* | 94315ded6e1175f2 |
| [weirdgloop-blog-php2shell](../../sources/weirdgloop-blog-php2shell/index.html) | partial | *it’s extremely likely that a bunch of old PHP fansites and forums have had their databases compromised* | 6bd492a6220e8eea |
| [certlv-php-preventive](../../sources/certlv-php-preventive/index.html) | carries | *taču līdz šim nav ziņu par sekmīgiem uzbrukumiem.* | e37a6582c4e6c685 |
| [insurancebusiness-uk-councils-met](../../sources/insurancebusiness-uk-councils-met/index.html) | carries | *No successful break-ins had been confirmed as of Wednesday afternoon.* | 89357150e0bc8363 |
| [reuters-factbox-websites-offline](../../sources/reuters-factbox-websites-offline/index.html) | carries | *The temporary deactivation was purely preventive and no security incidents were known to have occurred, the spokesperson said.* | d562e28995b00a19 |
| abc-au-politics-live (in the vault, not yet on this site) | carries | *Industry and Innovation Minister Tim Ayres says there has been no breach of Australian government websites* | a86331d9b7a21f78 |

Open tickets: [Contradiction-2](../../factcheck/index.html#Contradiction-2), [Evidence-1](../../factcheck/index.html#Evidence-1), [Evidence-10](../../factcheck/index.html#Evidence-10), [Evidence-3](../../factcheck/index.html#Evidence-3), [Finding-26](../../factcheck/index.html#Finding-26), [Finding-85](../../factcheck/index.html#Finding-85).

Graded in Run-1, resting on captures up to 2026-10-22 11:28 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Huntress publishes [Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress](../../sources/huntress-php2shell-rapid-response/index.html)
- 2026-10-21Imperva Threat Research publishes [PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva](../../sources/imperva-blog-php2shell/index.html)
- 2026-10-21Amazon publishes [Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Securi](../../sources/aws-security-blog-madpot/index.html)
- 2026-10-21Weird Gloop publishes [Recent wiki downtime (PHP2Shell mitigation) | Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html)
- 2026-10-21 14:04 UTCCISA publishes [CISA Known Exploited Vulnerabilities catalog (JSON feed)](../../sources/cisa-kev-json/index.html)
- 2026-10-22 11:17 UTCSaved into the evidence vault: Amazon
- 2026-10-22 11:18 UTCSaved into the evidence vault: Imperva Threat Research
- 2026-10-22 11:18 UTCSaved into the evidence vault: Weird Gloop
- 2026-10-22 11:28 UTCSaved into the evidence vault: Huntress
- 2026-10-22Enters this site as confirmed in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
AAlexCurious readerTTaylorProject or programme managerJJordanBoard member or executiveRRobinCISOQQuinnCFORRileyCommunications team
And on [every claim](../../claims/index.html#no-confirmed-compromise).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · confirmed
```
No named organisation has confirmed a compromise through php2shell
Who says it: this site, from every captured source
Status: confirmed
Topic: impact
Sources: cisa-kev-json, huntress-php2shell-rapid-response, imperva-blog-php2shell, aws-security-blog-madpot, weirdgloop-blog-php2shell
```


---
site v0.5.8 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/facts/no-confirmed-compromise/index.html
