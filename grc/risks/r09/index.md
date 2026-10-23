# R09: Not knowing where PHP runs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because PHP sits in appliances, images, plugins and forgotten sites, an organisation cannot patch what it has not listed, resulting in an update programme that reports done while vulnerable runtimes remain.

[Risks](../index.html) / R09

# R09: Not knowing where PHP runs

Because PHP sits in appliances, images, plugins and forgotten sites, an organisation cannot patch what it has not listed, resulting in an update programme that reports done while vulnerable runtimes remain.

**Rating** **16** high · **Likelihood** 4 Likely · **Impact** 4 Major · **Kind** Operational · **Acceptance** not recorded

**Basis.** 418 inventory rows under investigation; the precedent of every component flaw since Log4Shell.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [CTO](../../../grc/stakeholders/cto/index.html) | **owner** | Owns the inventory. | 3 risks |
| [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) | **treater** | Build it and keep it. | 4 risks |
| [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html) | **informer** | Say which products embed PHP. | 3 risks |

## What it arises from
- **Not knowing where PHP runs.** PHP is embedded in appliances, images and products whose owners do not list it; 418 inventory rows were still under investigation.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable](../../../facts/scale-ncsc-nl/index.html) | confirmed | **A1** Weak signal●○○○○○ | [NCSC-NL](../../../sources/ncsc-nl-php2shell-software-list/index.html) |
| [PHP is exposed on about 2.6 million internet-facing hosts, of which Censys counted 1.57 million unpatched on 21 October](../../../facts/scale-2.6m-hosts/index.html) | reported | **A2** Reported●●○○○○ | [THN](../../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../../sources/securityweek-exploitation-days-before/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| A software inventory with component versions (SBOM) | partial | [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.AM-02](../../frameworks/nistcsf/index.html#c-id-am-02) | Inventories of software, services and systems are maintained | Frameworks and control catalogues |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [CM-8](../../frameworks/nist80053/index.html#c-cm-8) | System component inventory | Frameworks and control catalogues |
| [CIS Controls](../../frameworks/cis/index.html) | [16.4](../../frameworks/cis/index.html#c-16-4) | Establish and manage an inventory of third-party software components | Frameworks and control catalogues |
| [DORA](../../frameworks/dora/index.html) | [Art.8](../../frameworks/dora/index.html#c-art-8) | Identification of ICT assets, their dependencies and the risks to them | Law and regulation |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.9](../../frameworks/iso27001/index.html#c-a-8-9) | Configuration management | Management-system standards |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [AnnexI.II](../../frameworks/cra/index.html#c-annexi-ii) | Vulnerability handling requirements: identify components, remedy without delay, publish fixed vulnerabilities, coordinated disclosure | Law and regulation |

## The stories that tell it
- [Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit](../../../articles/exposed-is-not-exploited/index.html)

On this site: [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) · [The NCSC-NL inventory: 674 products](../../../affected/software.html)


---
site v0.9.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r09/index.html
