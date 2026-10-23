# Cyber Resilience Act: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each Cyber Resilience Act clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / Cyber Resilience Act

# Cyber Resilience Act: the php2shell risks it governs

php2shell is among the first critical flaws in a ubiquitous open-source component since the Act's reporting duty began: a manufacturer whose product ships PHP must handle the flaw and report an actively exploited one; the PHP project is the kind of open-source steward the Act treats lightly.

**Full name** Regulation (EU) 2024/2847 on horizontal cybersecurity requirements for products with digital elements · **Publisher** European Union · **Version** 2024; reporting obligations apply from 11 September 2026 · [the official text](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **Art.13** | Obligations of manufacturers, including due diligence on integrated third-party and open-source components | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) **16** high [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../../grc/risks/r06-3/index.html) **12** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html), [Distributors and packagers](../../../grc/stakeholders/distributors/index.html), [The PHP security team](../../../grc/stakeholders/php-security-team/index.html), [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) |
| **Art.14** | Reporting an actively exploited vulnerability: early warning within 24 hours to the CSIRT and ENISA | [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) **15** high [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../../grc/risks/r06-3/index.html) **12** high | [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html), [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [Data protection officer](../../../grc/stakeholders/dpo/index.html), [Board and executives](../../../grc/stakeholders/board/index.html), [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html) |
| **Art.24** | Obligations of open-source software stewards | [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../../grc/risks/r06-3/index.html) **12** high [R08-1 A known bug left unexploited, then unfixed, for two years](../../../grc/risks/r08-1/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html), [The PHP project](../../../grc/stakeholders/php-project/index.html) |
| **AnnexI.II** | Vulnerability handling requirements: identify components, remedy without delay, publish fixed vulnerabilities, coordinated disclosure | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../../grc/risks/r06-3/index.html) **12** high [R09 Not knowing where PHP runs](../../../grc/risks/r09/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html), [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) |


---
site v0.9.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/cra/index.html
