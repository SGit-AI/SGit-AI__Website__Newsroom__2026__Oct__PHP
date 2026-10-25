# Fact: The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after di

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one day Who says it, its status (reported), its sources, and its timeline from publication to this site.

Fact · exploitation · reported

# The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one day

**Who says it:** CISA KEV catalog; Akamai (2024) · **Sources:** [CISA](../../sources/cisa-kev-json/index.html) [CVE record](../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../sources/akamai-blog-cve-2024-4577-one-day/index.html)

The KEV dates are counted from the captured catalog; 'exploited in the wild one day after disclosure' rests on Akamai alone.

## Fact-check

**A2** Reported●●○○○○ · Record · verdict: **holds in part**

'Reported' now fits, and the note says the one-day exploitation rests on Akamai alone. The claim text still calls CVE-2024-4577 'the last PHP core RCE', which the CVE record does not carry (a PHP-CGI argument injection on Windows); and 'not in KEV after one day' should name the catalog version checked. Finding-20 partly fixed; Finding-21 open.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [cisa-kev-json](../../sources/cisa-kev-json/index.html) | carries | *nothing that carries it* | ef8fffede5c47200 |
| [cve-cve-2024-4577](../../sources/cve-cve-2024-4577/index.html) | carries | *nothing that carries it* | e8cc1b1dcd1a3333 |
| [akamai-blog-cve-2024-4577-one-day](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) | carries | *As early as one day after disclosure, the SIRT observed numerous exploit attempts to abuse this vulnerability* | f7a58be0ecaaa8db |
| [akamai-blog-cve-2024-4577-one-day](../../sources/akamai-blog-cve-2024-4577-one-day/index.html) | partial | *we observed exploit attempts targeting this PHP flaw on our honeypot network within 24 hours of its disclosure.* | f7a58be0ecaaa8db |

Open tickets: [Evidence-1](../../factcheck/index.html#Evidence-1), [Finding-20](../../factcheck/index.html#Finding-20), [Finding-21](../../factcheck/index.html#Finding-21), [Finding-76](../../factcheck/index.html#Finding-76).

Graded in Run-3, resting on captures up to 2026-10-22 11:25 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2024Akamai Security Research publishes [CVE-2024-4577 Exploits in the Wild One Day After Disclosure](../../sources/akamai-blog-cve-2024-4577-one-day/index.html)
- 2024-06-09 19:42 UTCCVE record publishes [CVE-2024-4577 (PHP-CGI argument injection)](../../sources/cve-cve-2024-4577/index.html)
- 2026-10-21 14:04 UTCCISA publishes [CISA Known Exploited Vulnerabilities catalog (JSON feed)](../../sources/cisa-kev-json/index.html)
- 2026-10-22 11:25 UTCSaved into the evidence vault: Akamai Security Research
- 2026-10-22Enters this site as confirmed in v0.2.0 (reconstructed from git)
- 2026-10-24Status changes from confirmed to reported in v0.12.1

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
AAlexCurious readerCCaseyWebsite ownerJJordanBoard member or executiveSSamSecurity leadBBlakeAnalyst or policy advisorRRobinCISOQQuinnCFOMMorganData protection officerJJamieHead of AppSec
And on [every claim](../../claims/index.html#kev-precedent).

## Every version of this fact
v1 · site v0.2.0 · 22 October 2026 · confirmed
```
The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one day
Who says it: CISA KEV catalog; Akamai (2024)
Status: confirmed
Topic: exploitation
Sources: cisa-kev-json, cve-cve-2024-4577, akamai-blog-cve-2024-4577-one-day
```
v2 · site v0.12.1 · 24 October 2026 · reportedThe last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one dayWho says it: CISA KEV catalog; Akamai (2024)Status: confirmedreportedTopic: exploitationSources: cisa-kev-json, cve-cve-2024-4577, akamai-blog-cve-2024-4577-one-day


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/kev-precedent/index.html
