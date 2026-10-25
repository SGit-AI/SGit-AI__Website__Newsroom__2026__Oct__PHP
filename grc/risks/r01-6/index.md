# R01-6: Products that embed PHP stay vulnerable while their suppliers investigate

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because PHP is embedded in products whose suppliers must each ship their own fix, and most of the 674 products in the NCSC-NL inventory were vulnerable or under investigation, customers of those products cannot patch on their own, resulting in exposure that lasts as long as the slowest supplier.

[Risks](../index.html) / [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) / R01-6

# R01-6: Products that embed PHP stay vulnerable while their suppliers investigate

Because PHP is embedded in products whose suppliers must each ship their own fix, and most of the 674 products in the NCSC-NL inventory were vulnerable or under investigation, customers of those products cannot patch on their own, resulting in exposure that lasts as long as the slowest supplier.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r01-6) · [What the graph is missing](../../gaps/index.html)

**Rating** **16** high · **Likelihood** 4 Likely · **Impact** 4 Major · **Kind** Supply chain · **Acceptance** not recorded

**Basis.** Counted from the inventory: 206 vulnerable and 418 under investigation against 46 fixed at the vault's capture.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html) | **owner** | Each ships the fix for its product. | 3 risks |
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **bearer** | Depend on the supplier's release. | 26 risks |
| [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) | **informer** | NCSC-NL keeps the inventory. | 5 risks |
| [CTO](../../../grc/stakeholders/cto/index.html) | **owner** | Owns the supplier relationship and the inventory of what runs where. | 3 risks |

## What it arises from
- **Not knowing where PHP runs.** PHP is embedded in appliances, images and products whose owners do not list it; 418 inventory rows were still under investigation.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable](../../../facts/scale-ncsc-nl/index.html) | confirmed | **A1** Weak signal●○○○○○ | [NCSC-NL](../../../sources/ncsc-nl-php2shell-software-list/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| The NCSC-NL inventory, tracked hour by hour | partial | [The inventory, hour by hour: fixed, vulnerable, still under investigation](../../../patching/inventory/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.13](../../frameworks/cra/index.html#c-art-13) | Obligations of manufacturers, including due diligence on integrated third-party and open-source components | Law and regulation |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [AnnexI.II](../../frameworks/cra/index.html#c-annexi-ii) | Vulnerability handling requirements: identify components, remedy without delay, publish fixed vulnerabilities, coordinated disclosure | Law and regulation |
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [A03:2025](../../frameworks/owasp/index.html#c-a03-2025) | Software supply chain failures | Practice and technique |
| [NIS2](../../frameworks/nis2/index.html) | [Art.21(2)(d)](../../frameworks/nis2/index.html#c-art-21-2-d) | Supply chain security, including the security of each direct supplier | Law and regulation |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.21](../../frameworks/iso27001/index.html#c-a-5-21) | Managing information security in the ICT supply chain | Management-system standards |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [GV.SC-07](../../frameworks/nistcsf/index.html#c-gv-sc-07) | Supplier risks are understood, recorded, prioritised, assessed, responded to and monitored | Frameworks and control catalogues |
| [DORA](../../frameworks/dora/index.html) | [Art.28](../../frameworks/dora/index.html#c-art-28) | Managing ICT third-party risk | Law and regulation |
| [SOC 2](../../frameworks/soc2/index.html) | [CC9.2](../../frameworks/soc2/index.html#c-cc9-2) | Risks from vendors and business partners are assessed and managed | Frameworks and control catalogues |

## The stories that tell it
- [Why can't every version of PHP just be patched?](../../../articles/why-not-patch-every-version/index.html)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Remote code execution on internet-facing PHP servers)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Remote code execution on internet-facing PHP servers)

On this site: [The NCSC-NL inventory: 674 products](../../../affected/software.html) · [The inventory, hour by hour: fixed, vulnerable, still under investigation](../../../patching/inventory/index.html)


---
site v0.22.9 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01-6/index.html
