# R04-1: National government services offline

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the Dutch, Finnish and Latvian governments restricted or switched off their own web services as a precaution, citizens lost access to identity, tax and emergency information, resulting in harm to people who needed them that day.

[Risks](../index.html) / [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) / R04-1

# R04-1: National government services offline

Because the Dutch, Finnish and Latvian governments restricted or switched off their own web services as a precaution, citizens lost access to identity, tax and emergency information, resulting in harm to people who needed them that day.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r04-1) · [What the graph is missing](../../gaps/index.html)

**Rating** **20** critical · **Likelihood** 5 Happening · **Impact** 4 Major · **Kind** Operational · **Acceptance** not recorded

**Basis.** Confirmed in the Netherlands and Latvia; reported in Finland.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [National governments](../../../grc/stakeholders/national-gov/index.html) | **owner** | Made the call. | 1 risk |
| [People who need a service that went offline](../../../grc/stakeholders/service-users/index.html) | **bearer** | Lost DigiD, MijnOverheid, 112.lv. | 2 risks |
| [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) | **informer** | NCSC-NL and CERT.LV advised and acted. | 5 risks |

## What it arises from
- **Not knowing where PHP runs.** PHP is embedded in appliances, images and products whose owners do not list it; 418 inventory rows were still under investigation.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [The Dutch government took NCSC.nl offline as a precaution, with no active misuse seen yet; Dutch press reported DigiD, MijnOverheid and Overheid.nl offline too](../../../facts/nl-offline/index.html) | reported | **A4** Corroborated●●●●○○ | [Rijksoverheid / NCSC-NL](../../../sources/rijksoverheid-ncsc-php-news/index.html) [TPO.nl](../../../sources/tpo-nl-digid-offline/index.html) |
| [Finland's state IT provider Valtori restricted public traffic to government web services from 12:45 local time on 21 October as a precaution](../../../facts/fi-offline/index.html) | reported | **A2** Reported●●○○○○ | [Yle](../../../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../../../sources/helsinkitimes-finland-shutdown/index.html) |
| [Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTC](../../../facts/latvia-offline/index.html) | confirmed | **A6** Established●●●●●● | [CERT.LV](../../../sources/certlv-php-preventive/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Restrict access by geography instead of switching off | partial | [Impact: taken offline versus compromised](../../../impact/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIS2](../../frameworks/nis2/index.html) | [Art.21(2)(c)](../../frameworks/nis2/index.html#c-art-21-2-c) | Business continuity, backup management, disaster recovery and crisis management | Law and regulation |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.29](../../frameworks/iso27001/index.html#c-a-5-29) | Information security during disruption | Management-system standards |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [RC.RP-01](../../frameworks/nistcsf/index.html#c-rc-rp-01) | The recovery portion of the incident response plan is executed | Frameworks and control catalogues |

## The stories that tell it
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Services lost to precautionary shutdowns)

On this site: [Impact: taken offline versus compromised](../../../impact/index.html)


---
site v0.14.10 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r04-1/index.html
