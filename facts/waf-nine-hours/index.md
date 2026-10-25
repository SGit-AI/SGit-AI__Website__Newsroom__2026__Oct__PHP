# Fact: Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imp

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 October Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · advice · confirmed

# Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 October

**Who says it:** the vendors · **Sources:** [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html)

Every vendor says the same two things: it is a stopgap, and patch anyway.

## Fact-check

**A2** Reported●●○○○○ status overstated · Event · verdict: **holds in part** · the status word overstates the evidence

Only Cloudflare gives a pre-disclosure go-live time (03:02 UTC on 21 Oct, its own account). Imperva says it verified protection and monitored before the announcement but gives no time; Akamai and Fastly give only a 21 October post date; Fortinet's article is dated 22 October 07:55, after disclosure, so 'went live hours before disclosure' does not cover it. Each date is the vendor's own word, A2; 'confirmed' overstates.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [cloudflare-blog-php2shell-waf](../../sources/cloudflare-blog-php2shell-waf/index.html) | carries | *Starting on October 21 3:02 am UTC, Cloudflare customers using our free or paid WAF were protected by default against php2shell.* | 302408765abf45e3 |
| [imperva-blog-php2shell](../../sources/imperva-blog-php2shell/index.html) | partial | *enabling Imperva to verify its protection and begin monitoring customer traffic before the announcement.* | 3da873bdb21219a6 |
| [akamai-blog-php-core-rce](../../sources/akamai-blog-php-core-rce/index.html) | partial | *Akamai App & API Protector customers are protected because we have released security updates to address this CVE and monitor for exploitation attempts.* | 2a001600cd450bc5 |
| [fastly-blog-php2shell](../../sources/fastly-blog-php2shell/index.html) | partial | *To mitigate risk for your applications protected by NGWAF, Fastly customers may enable the signal covering both CVE-2026-109618 & CVE-2026-109619.* | bacf27615fe1180a |
| [fortinet-fortiweb-php2shell](../../sources/fortinet-fortiweb-php2shell/index.html) | partial | *10/22/2026 \| 07:55 AM* | 66beb7cb9c50e017 |

Open tickets: [Finding-110](../../factcheck/index.html#Finding-110), [Finding-46](../../factcheck/index.html#Finding-46), [Finding-47](../../factcheck/index.html#Finding-47).

Graded in Run-1, resting on captures up to 2026-10-22 11:25 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Cloudflare publishes [Cloudflare deploys protections against php2shell vulnerability](../../sources/cloudflare-blog-php2shell-waf/index.html)
- 2026-10-21Imperva Threat Research publishes [PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva](../../sources/imperva-blog-php2shell/index.html)
- 2026-10-21Akamai Security Research publishes [Critical Remote Code Execution Vulnerabilities in PHP Core | Akamai](../../sources/akamai-blog-php-core-rce/index.html)
- 2026-10-21Fastly publishes [Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly](../../sources/fastly-blog-php2shell/index.html)
- 2026-10-22 07:55 UTCFortinet Community publishes [How to block PHP2Shell (CVE-2026-109618, CVE-2026-109619) on FortiWeb | Community](../../sources/fortinet-fortiweb-php2shell/index.html)
- 2026-10-22 08:12 UTCSaved into the evidence vault: Cloudflare, then 1 more capture
- 2026-10-22 11:18 UTCSaved into the evidence vault: Imperva Threat Research, then 1 more capture
- 2026-10-22 11:19 UTCSaved into the evidence vault: Fastly, then 1 more capture
- 2026-10-22 11:20 UTCSaved into the evidence vault: Fortinet Community, then 1 more capture
- 2026-10-22 11:25 UTCSaved into the evidence vault: Akamai Security Research
- 2026-10-22Enters this site as confirmed in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerTTaylorProject or programme managerJJordanBoard member or executiveSSamSecurity leadRRowanJournalistRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecRRileyCommunications team
And on [every claim](../../claims/index.html#waf-nine-hours).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · confirmed
```
Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 October
Who says it: the vendors
Status: confirmed
Topic: advice
Sources: cloudflare-blog-php2shell-waf, imperva-blog-php2shell, akamai-blog-php-core-rce, fastly-blog-php2shell, fortinet-fortiweb-php2shell
```


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/waf-nine-hours/index.html
