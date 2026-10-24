# R06-3: Manufacturers under the Cyber Resilience Act owe a 24-hour report

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the Act's reporting duty has applied since 11 September 2026, a manufacturer whose product embeds PHP must report an actively exploited vulnerability within 24 hours, and whether php2shell is 'actively exploited' is exactly what the evidence cannot yet settle, resulting in manufacturers deci

[Risks](../index.html) / [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) / R06-3

# R06-3: Manufacturers under the Cyber Resilience Act owe a 24-hour report

Because the Act's reporting duty has applied since 11 September 2026, a manufacturer whose product embeds PHP must report an actively exploited vulnerability within 24 hours, and whether php2shell is 'actively exploited' is exactly what the evidence cannot yet settle, resulting in manufacturers deciding alone when the clock starts.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r06-3) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** Compliance · **Acceptance** not recorded

**Basis.** The legal test turns on exploitation, which is disputed; the inventory shows hundreds of products.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html) | **owner** | Manufacturers under the Act. | 3 risks |
| [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) | **informer** | An open-source steward, with lighter duties under Article 24. | 3 risks |
| [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) | **regulator** | The CSIRTs and ENISA receive the reports. | 5 risks |
| [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) | **treater** | Build the fixed product and the component inventory that shows it. | 4 risks |

## What it arises from
- **Not knowing where PHP runs.** PHP is embedded in appliances, images and products whose owners do not list it; 418 inventory rows were still under investigation.
- **Exploitation that cannot yet be seen.** Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable](../../../facts/scale-ncsc-nl/index.html) | confirmed | **A1** Weak signal●○○○○○ | [NCSC-NL](../../../sources/ncsc-nl-php2shell-software-list/index.html) |
| [watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild](../../../facts/watchtowr-itw/index.html) | unverified | **A4** Corroborated●●●●○○ | [watchTowr](../../../sources/watchtowr-php2shell/index.html) [watchTowr](../../../sources/watchtowr-php2shell-faq/index.html) |
| [CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalog](../../../facts/cisa-none/index.html) | confirmed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) [CISA](../../../sources/cisa-kev-json/index.html) [CVE record](../../../sources/cve-cve-2026-109618/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| A documented decision on whether and when the exploitation test is met | missing | [The NCSC-NL inventory: 674 products](../../../affected/software.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.14](../../frameworks/cra/index.html#c-art-14) | Reporting an actively exploited vulnerability: early warning within 24 hours to the CSIRT and ENISA | Law and regulation |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.13](../../frameworks/cra/index.html#c-art-13) | Obligations of manufacturers, including due diligence on integrated third-party and open-source components | Law and regulation |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.24](../../frameworks/cra/index.html#c-art-24) | Obligations of open-source software stewards | Law and regulation |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [AnnexI.II](../../frameworks/cra/index.html#c-annexi-ii) | Vulnerability handling requirements: identify components, remedy without delay, publish fixed vulnerabilities, coordinated disclosure | Law and regulation |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [The NCSC-NL inventory: 674 products](../../../affected/software.html) · [Exploitation signals, in order](../../../exploitation/index.html)


---
site v0.14.10 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r06-3/index.html
