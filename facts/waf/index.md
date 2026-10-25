# Fact: A web application firewall may provide some protection until systems are patched

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

A web application firewall may provide some protection until systems are patched Who says it, its status (disputed), its sources, and its timeline from publication to this site.

Fact · technical · disputed

# A web application firewall may provide some protection until systems are patched

**Who says it:** CISA · **Sources:** [CISA](../../sources/cisa-alert-php-20261021/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html)

Swiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them.

## Fact-check

**A6** Established●●●●●● · Advice · verdict: **holds** · the status word understates the evidence

CISA's alert carries the sentence nearly verbatim, so the advice is established as CISA's. BACS ('alone is not sufficient') and Cloudflare (attackers mutating payloads) qualify it but do not contradict 'some protection'; CERT-FR also recommends WAF-level blocking. 'Disputed' overstates the disagreement.

| Capture checked | Result | What it says | sha256 of the text read |
|---|---|---|---|
| [cisa-alert-php-20261021](../../sources/cisa-alert-php-20261021/index.html) | carries | *A web application firewall may provide some protection until systems are updated or patched.* | 7bf853872a073bde |
| [ch-bacs-warnung-php](../../sources/ch-bacs-warnung-php/index.html) | partial | *They do not provide complete protection and are no substitute for security updates. Even a web application firewall alone is not sufficient.* | 99886a19aead8abe |
| [cloudflare-blog-php2shell-waf](../../sources/cloudflare-blog-php2shell-waf/index.html) | partial | *We observed how attackers were mutating the attack payload to try to bypass our protections* | 302408765abf45e3 |
| [certfr-2026-ale-014](../../sources/certfr-2026-ale-014/index.html) | partial | *Ces mesures peuvent être réalisées au niveau d'un pare-feu applicatif (Web Application Firewall).* | f9e9557ab49ddb95 |

Open tickets: [Finding-109](../../factcheck/index.html#Finding-109), [Finding-51](../../factcheck/index.html#Finding-51).

Graded in Run-1, resting on captures up to 2026-10-22 08:17 UTC. The scale is on [the fact-check page](../../factcheck/index.html#ladder).

## This fact over time
- 2026-10-21CISA publishes [Critical Vulnerabilities in PHP Require Immediate Patching](../../sources/cisa-alert-php-20261021/index.html)
- 2026-10-21BACS publishes [Critical vulnerabilities in PHP: Install security updates immediately](../../sources/ch-bacs-warnung-php/index.html)
- 2026-10-21Cloudflare publishes [Cloudflare deploys protections against php2shell vulnerability](../../sources/cloudflare-blog-php2shell-waf/index.html)
- 2026-10-22 08:12 UTCSaved into the evidence vault: Cloudflare, then 1 more capture
- 2026-10-22 08:13 UTCSaved into the evidence vault: CISA
- 2026-10-22 08:17 UTCSaved into the evidence vault: BACS
- 2026-10-22Enters this site as disputed in v0.1.0 (reconstructed from git)

Published: when the source says it was published. Saved: the first capture into the evidence vault. The rest are this site: the release in which the fact first appeared and every release that changed its wording, sources or status.

## What it rests on

## Where this fact appears

In the briefings for:
CCaseyWebsite ownerSSamSecurity leadDDrewPHP or platform engineerAAshSecurity researcherRRobinCISOAAveryCTOMMorganData protection officerJJamieHead of AppSecLLeeDeveloper
And on [every claim](../../claims/index.html#waf).

## Every version of this fact
v1 · site v0.1.0 · 22 October 2026 · disputed
```
A web application firewall may provide some protection until systems are patched
Who says it: CISA
Status: disputed
Topic: technical
Sources: cisa-alert-php-20261021, ch-bacs-warnung-php, cloudflare-blog-php2shell-waf
```


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/facts/waf/index.html
