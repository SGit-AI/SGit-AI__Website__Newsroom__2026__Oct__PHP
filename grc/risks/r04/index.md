# R04: Services lost to precautionary shutdowns

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because agencies advised taking systems offline where an update was not possible, governments, councils and companies switched off services people rely on, resulting in an outage caused by the defence rather than by an attack.

[Risks](../index.html) / R04

# R04: Services lost to precautionary shutdowns

Because agencies advised taking systems offline where an update was not possible, governments, councils and companies switched off services people rely on, resulting in an outage caused by the defence rather than by an attack.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r04) · [What the graph is missing](../../gaps/index.html)

**Rating** **20** critical · **Likelihood** 5 Happening · **Impact** 4 Major · **Kind** Operational · **Acceptance** not recorded

**Basis.** It happened: the Netherlands, Finland, Latvia, UK councils and the Wikimedia Foundation took services offline.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Governments and public services](../../../grc/stakeholders/public-sector/index.html) | **owner** | Took the decisions. | 3 risks |
| [People who need a service that went offline](../../../grc/stakeholders/service-users/index.html) | **bearer** | Lost the services. | 2 risks |
| [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) | **source** | Their advice drove the decisions. | 11 risks |
| [Board and executives](../../../grc/stakeholders/board/index.html) | **owner** | The offline call is a board-level call. | 5 risks |
| [Communications team](../../../grc/stakeholders/comms/index.html) | **treater** | Explains the outage. | 2 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R04-1 National government services offline](../../../grc/risks/r04-1/index.html) | **20** critical | Operational | [National governments](../../../grc/stakeholders/national-gov/index.html) owner, [People who need a service that went offline](../../../grc/stakeholders/service-users/index.html) bearer, [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) informer | [NIS2 Art.21(2)(c)](../../../grc/frameworks/nis2/index.html#c-art-21-2-c), [ISO/IEC 27001 A.5.29](../../../grc/frameworks/iso27001/index.html#c-a-5-29), [NIST CSF 2.0 RC.RP-01](../../../grc/frameworks/nistcsf/index.html#c-rc-rp-01) |
| [R04-2 Councils and police offline without saying why](../../../grc/risks/r04-2/index.html) | **15** high | Reputational | [Local councils](../../../grc/stakeholders/councils/index.html) owner, [Communications team](../../../grc/stakeholders/comms/index.html) treater, [UK NCSC](../../../grc/stakeholders/uk-ncsc/index.html) informer | [Cyber Essentials SUM](../../../grc/frameworks/cyberessentials/index.html#c-sum), [NIST CSF 2.0 RS.CO-03](../../../grc/frameworks/nistcsf/index.html#c-rs-co-03), [ISO/IEC 27001 A.5.24](../../../grc/frameworks/iso27001/index.html#c-a-5-24) |
| [R04-3 The agencies' advice disagrees](../../../grc/risks/r04-3/index.html) | **12** high | Governance | [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) source, [Board and executives](../../../grc/stakeholders/board/index.html) owner, [The press](../../../grc/stakeholders/media/index.html) informer | [ISO/IEC 27001 A.5.5](../../../grc/frameworks/iso27001/index.html#c-a-5-5), [NIST CSF 2.0 GV.RR-01](../../../grc/frameworks/nistcsf/index.html#c-gv-rr-01), [NIS2 Art.20](../../../grc/frameworks/nis2/index.html#c-art-20) |

## What it arises from
- **PHP versions the project no longer fixes.** 8.1 and older get no upstream fix; reaching them needs a distribution backport, paid support or an upgrade.
- **Not knowing where PHP runs.** PHP is embedded in appliances, images and products whose owners do not list it; 418 inventory rows were still under investigation.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [If an immediate update is not feasible, take the system offline until it can be fully mitigated](../../../facts/offline-nsa/index.html) | confirmed | **A6** Established●●●●●● | [NSA Cyber on X](../../../sources/nsa-x-2112903220209098897/index.html) [NSA](../../../sources/nsa-press-php-4630238/index.html) |
| [Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline](../../../facts/offline-cisa/index.html) | confirmed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) |
| [The Dutch government took NCSC.nl offline as a precaution, with no active misuse seen yet; Dutch press reported DigiD, MijnOverheid and Overheid.nl offline too](../../../facts/nl-offline/index.html) | reported | **A4** Corroborated●●●●○○ | [Rijksoverheid / NCSC-NL](../../../sources/rijksoverheid-ncsc-php-news/index.html) [TPO.nl](../../../sources/tpo-nl-digid-offline/index.html) |
| [Finland's state IT provider Valtori restricted public traffic to government web services from 12:45 local time on 21 October as a precaution](../../../facts/fi-offline/index.html) | reported | **A2** Reported●●○○○○ | [Yle](../../../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../../../sources/helsinkitimes-finland-shutdown/index.html) |
| [Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTC](../../../facts/latvia-offline/index.html) | confirmed | **A6** Established●●●●●● | [CERT.LV](../../../sources/certlv-php-preventive/index.html) |
| [Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the BBC were affected or taken offline](../../../facts/affected-sites/index.html) | reported | **A2** Reported●●○○○○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| [The Wikimedia Foundation took down a number of systems 'as a precautionary measure until they can be safely patched'](../../../facts/wikimedia-precaution/index.html) | reported | **A4** Corroborated●●●●○○ | [CNN](../../../sources/cnn-php2shell-websites-shut/index.html) [The Cyber Express](../../../sources/cyberexpress-php2shell-gov-sites/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Serve from cache while the origin is patched | partial | [Impact: taken offline versus compromised](../../../impact/index.html) |
| A continuity plan that names which services may go dark | missing | [Impact: taken offline versus compromised](../../../impact/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.29](../../frameworks/iso27001/index.html#c-a-5-29) | Information security during disruption | Management-system standards |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.30](../../frameworks/iso27001/index.html#c-a-5-30) | ICT readiness for business continuity | Management-system standards |
| [NIS2](../../frameworks/nis2/index.html) | [Art.21(2)(c)](../../frameworks/nis2/index.html#c-art-21-2-c) | Business continuity, backup management, disaster recovery and crisis management | Law and regulation |
| [DORA](../../frameworks/dora/index.html) | [Art.11](../../frameworks/dora/index.html#c-art-11) | Response and recovery, including ICT business continuity | Law and regulation |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [CP-2](../../frameworks/nist80053/index.html#c-cp-2) | Contingency plan | Frameworks and control catalogues |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [RC.RP-01](../../frameworks/nistcsf/index.html#c-rc-rp-01) | The recovery portion of the incident response plan is executed | Frameworks and control catalogues |

## The stories that tell it
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html)

On this site: [Impact: taken offline versus compromised](../../../impact/index.html) · [What sixteen agencies actually advise](../../../agencies/index.html)


---
site v0.18.0 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r04/index.html
