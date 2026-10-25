# R04-2: Councils and police offline without saying why

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because UK councils and the Met Police went offline calling it maintenance or a precaution and did not confirm the link, residents could not tell an outage from an attack, resulting in lost trust and calls the council could not answer.

[Risks](../index.html) / [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) / R04-2

# R04-2: Councils and police offline without saying why

Because UK councils and the Met Police went offline calling it maintenance or a precaution and did not confirm the link, residents could not tell an outage from an attack, resulting in lost trust and calls the council could not answer.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r04-2) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 5 Happening · **Impact** 3 Significant · **Kind** Reputational · **Acceptance** not recorded

**Basis.** Reported by the press; Oxford's statement quoted.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Local councils](../../../grc/stakeholders/councils/index.html) | **owner** | Took the sites down and chose the words. | 1 risk |
| [Communications team](../../../grc/stakeholders/comms/index.html) | **treater** | Says what is known. | 2 risks |
| [UK NCSC](../../../grc/stakeholders/uk-ncsc/index.html) | **informer** | Its advice was the reason. | 1 risk |

## What it arises from
- **PHP versions the project no longer fixes.** 8.1 and older get no upstream fix; reaching them needs a distribution backport, paid support or an upgrade.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Edinburgh council's site went offline late on 21 October; the council called it 'essential maintenance' and did not confirm a link](../../../facts/edinburgh/index.html) | reported | **A3** Echoed●●●○○○ | [The Scotsman](../../../sources/scotsman-edinburgh-council-offline/index.html) |
| [Oxford City Council: 'a precaution because of a worldwide issue with the underlying technology and is not a cyber incident'](../../../facts/oxford/index.html) | reported | **A2** Reported●●○○○○ | [Oxford Chronicle](../../../sources/oxfordchronicle-councils-offline/index.html) |
| [Edinburgh and Oxford councils, the Met Police and the Office for Budget Responsibility were unavailable; Bristol, Lambeth and Barnet council sites showed errors](../../../facts/uk-list/index.html) | reported | **A3** Echoed●●●○○○ | [LBC](../../../sources/lbc-uk-websites-offline/index.html) [Insurance Business](../../../sources/insurancebusiness-uk-councils-met/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| A holding statement prepared before the outage | missing | [Briefing for a media and communications team: What can we say that is true, what should we not say, and what will we be asked?](../../../briefings/comms/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [Cyber Essentials](../../frameworks/cyberessentials/index.html) | [SUM](../../frameworks/cyberessentials/index.html#c-sum) | Security update management: high and critical updates within 14 days of release; unsupported software removed | Frameworks and control catalogues |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [RS.CO-03](../../frameworks/nistcsf/index.html#c-rs-co-03) | Information is shared with designated internal and external stakeholders | Frameworks and control catalogues |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.24](../../frameworks/iso27001/index.html#c-a-5-24) | Incident management planning and preparation | Management-system standards |

## The stories that tell it
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Services lost to precautionary shutdowns)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Services lost to precautionary shutdowns)

On this site: [Impact: taken offline versus compromised](../../../impact/index.html) · [Briefing for a media and communications team: What can we say that is true, what should we not say, and what will we be asked?](../../../briefings/comms/index.html)


---
site v0.20.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r04-2/index.html
