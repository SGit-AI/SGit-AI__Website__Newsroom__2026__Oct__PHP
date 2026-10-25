# Fact: Triggering the bug is much easier than turning it into code execution; the CVSS 

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity high Who says it, its status (confirmed), its sources, and its timeline from publication to this site.

Fact · technical · confirmed

# Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity high

**Who says it:** Imperva; Fastly; the CVE record · **Sources:** [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html)

Fastly: 'most deployments may be safe from RCE. Do not assume this holds true for you.' Imperva: five demonstrated techniques, three via session upload progress; about 67 KB of memory disclosed per attack.

## Fact-check

**A3** Echoed●●●○○○ opinion status overstated · Opinion · verdict: **holds** · the status word overstates the evidence

The CVSS half is a record (AC:H in the CVE record, A6). The 'much easier' half is Imperva's characterisation, supported by Fastly (single-request trigger; RCE needs binary layout knowledge) and the advisory's reliability caveats; as a reading it caps at A3, so 'confirmed' overstates the claim as a whole.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [imperva-blog-php2shell](../../sources/imperva-blog-php2shell/index.html) | carries | *It’s worth noting that the attack complexity in both vulnerabilities is high* | 3da873bdb21219a6 |
| [imperva-blog-php2shell](../../sources/imperva-blog-php2shell/index.html) | carries | *Triggering the bug is much easier than turning it into code execution.* | 3da873bdb21219a6 |
| [fastly-blog-php2shell](../../sources/fastly-blog-php2shell/index.html) | partial | *most deployments may be “safe” from RCE. Do not assume this holds true for you.* | bacf27615fe1180a |
| [cve-cve-2026-109618](../../sources/cve-cve-2026-109618/index.html) | carries | *CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N* | f8705d8e0aa2a248 |

Open tickets: [Finding-53](../../factcheck/index.html#Finding-53), [Finding-56](../../factcheck/index.html#Finding-56).

Graded in Run-1, resting on captures up to 2026-10-22 11:19 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21Imperva Threat Research publishes [PHP2Shell: When PHP Runs Out of Memory at the Wrong Moment | Imperva](../../sources/imperva-blog-php2shell/index.html)
- 2026-10-21Fastly publishes [Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly](../../sources/fastly-blog-php2shell/index.html)
- 2026-10-21 13:48 UTCCVE record publishes [CVE-2026-109618: RCE via OOM corruption](../../sources/cve-cve-2026-109618/index.html)
- 2026-10-22 08:12 UTCSaved into the evidence vault: CVE record
- 2026-10-22 11:18 UTCSaved into the evidence vault: Imperva Threat Research, then 1 more capture
- 2026-10-22 11:19 UTCSaved into the evidence vault: Fastly, then 1 more capture
- 2026-10-22Enters this site as confirmed in v0.2.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#ac-high).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · confirmed
```
Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity high
Who says it: Imperva; Fastly; the CVE record
Status: confirmed
Topic: technical
Sources: imperva-blog-php2shell, fastly-blog-php2shell, cve-cve-2026-109618
```


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/ac-high/index.html
