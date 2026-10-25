# R05: A web application firewall taken for a patch

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because edge rules went live hours before disclosure and covered most traffic, an operator may treat the filter as the fix, resulting in an unpatched engine behind a filter that mutated payloads and unrouted traffic get past.

[Risks](../index.html) / R05

# R05: A web application firewall taken for a patch

Because edge rules went live hours before disclosure and covered most traffic, an operator may treat the filter as the fix, resulting in an unpatched engine behind a filter that mutated payloads and unrouted traffic get past.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r05) · [What the graph is missing](../../gaps/index.html)

**Rating** **16** high · **Likelihood** 4 Likely · **Impact** 4 Major · **Kind** Security · **Acceptance** not recorded

**Basis.** Every vendor said a rule is a stopgap; the claim that a WAF protects is disputed.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html) | **informer** | Said so themselves. | 2 risks |
| [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) | **owner** | Decides whether the filter buys time or replaces the update. | 6 risks |
| [Online shops and payments](../../../grc/stakeholders/commerce/index.html) | **bearer** | PCI DSS 6.4.2 makes the filter a requirement, which can read as enough. | 2 risks |

## What it arises from
- **A filter in front of an unpatched engine.** Rules match the payload shapes seen so far; attackers mutate payloads, and only traffic routed through the filter is covered.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [A web application firewall may provide some protection until systems are patched](../../../facts/waf/index.html) | disputed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) [BACS](../../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../../sources/cloudflare-blog-php2shell-waf/index.html) |
| [Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 October](../../../facts/waf-nine-hours/index.html) | confirmed | **A2** Reported●●○○○○ | [Cloudflare](../../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../../sources/fortinet-fortiweb-php2shell/index.html) |
| [Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe](../../../facts/only-update/index.html) | confirmed | **A6** Established●●●●●● | [php.net](../../../sources/php-net-advisory/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Filter and patch, never filter instead of patch | in place | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html#answer) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [PCI DSS](../../frameworks/pcidss/index.html) | [6.4.2](../../frameworks/pcidss/index.html#c-6-4-2) | An automated technical solution that detects and prevents web attacks protects public-facing web applications | Management-system standards |
| [CIS Controls](../../frameworks/cis/index.html) | [13.10](../../frameworks/cis/index.html#c-13-10) | Perform application layer filtering | Frameworks and control catalogues |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [SC-7](../../frameworks/nist80053/index.html#c-sc-7) | Boundary protection | Frameworks and control catalogues |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.20](../../frameworks/iso27001/index.html#c-a-8-20) | Network security | Management-system standards |
| [Cyber Essentials](../../frameworks/cyberessentials/index.html) | [FW](../../frameworks/cyberessentials/index.html#c-fw) | Firewalls: boundary protection for internet-facing services | Frameworks and control catalogues |

## The stories that tell it
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html)

On this site: [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r05/index.html
