# R03-2: Mass scanning and mutated payloads after the leak

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because tens of thousands of attempts followed the announcement and attackers mutated payloads, every internet-facing PHP server was tested within hours, resulting in exposure measured in hours, not weeks.

[Risks](../index.html) / [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) / R03-2

# R03-2: Mass scanning and mutated payloads after the leak

Because tens of thousands of attempts followed the announcement and attackers mutated payloads, every internet-facing PHP server was tested within hours, resulting in exposure measured in hours, not weeks.

**Rating** **20** critical · **Likelihood** 5 Happening · **Impact** 4 Major · **Kind** Security · **Acceptance** not recorded

**Basis.** Reported by Cloudflare's CEO and confirmed as probing by Amazon and Cloudflare.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html) | **treater** | Absorb the scanning. | 2 risks |
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **owner** | Every server was tested; only its operator can patch it. | 26 risks |

## What it arises from
- **A filter in front of an unpatched engine.** Rules match the payload shapes seen so far; attackers mutate payloads, and only traffic routed through the filter is covered.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Exploit attempts across Cloudflare's network: thousands in the ten hours before announcement, tens of thousands within 45 minutes after, hundreds of thousands within two hours, millions by 22 October 01:25 UTC](../../../facts/cf-millions/index.html) | reported | **A2** Reported●●○○○○ | [Matthew Prince, Cloudflare CEO on…](../../../sources/x-eastdakota-php2shell-stats/index.html) |
| [Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloads](../../../facts/cloudflare-traffic/index.html) | reported | **A2** Reported●●○○○○ | [Cloudflare](../../../sources/cloudflare-blog-php2shell-waf/index.html) |
| [Amazon and Cloudflare saw sites being probed for the flaw](../../../facts/probing/index.html) | confirmed | **A5** Confirmed●●●●●○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../../sources/aws-security-blog-madpot/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Edge rules from every major vendor | partial | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html#edge) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [MITRE ATT&CK](../../frameworks/attack/index.html) | [T1595.002](../../frameworks/attack/index.html#c-t1595-002) | Active scanning: vulnerability scanning | Practice and technique |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [DE.CM-01](../../frameworks/nistcsf/index.html#c-de-cm-01) | Networks and network services are monitored to find potentially adverse events | Frameworks and control catalogues |
| [CIS Controls](../../frameworks/cis/index.html) | [13.10](../../frameworks/cis/index.html#c-13-10) | Perform application layer filtering | Frameworks and control catalogues |

## The stories that tell it
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Exploitation outpaces patching)
- [Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit](../../../articles/exposed-is-not-exploited/index.html) (through Exploitation outpaces patching)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Exploitation outpaces patching)

On this site: [Exploitation signals, in order](../../../exploitation/index.html) · [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html)


---
site v0.8.3 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r03-2/index.html
