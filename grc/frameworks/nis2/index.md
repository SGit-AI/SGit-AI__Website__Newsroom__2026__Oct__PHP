# NIS2: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each NIS2 clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / NIS2

# NIS2: the php2shell risks it governs

Essential and important entities (energy, health, digital infrastructure, public administration and more) must manage vulnerabilities, handle incidents and report significant ones; management bodies answer for it personally.

**Full name** Directive (EU) 2022/2555 on a high common level of cybersecurity across the Union · **Publisher** European Union · **Version** 2022, transposition deadline 17 October 2024 · [the official text](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **Art.12** | Coordinated vulnerability disclosure and the European vulnerability database | [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) **20** critical | [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) |
| **Art.20** | Governance: management bodies approve and oversee the risk-management measures and can be held liable | [R04-3 The agencies' advice disagrees](../../../grc/risks/r04-3/index.html) **12** high [R06-2 Essential and financial entities miss their reporting clocks](../../../grc/risks/r06-2/index.html) **12** high | [Board and executives](../../../grc/stakeholders/board/index.html), [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html), [Banks, insurers and financial entities](../../../grc/stakeholders/finance/index.html), [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) |
| **Art.21(2)(a)** | Policies on risk analysis and information system security | *no risk mapped* |  |
| **Art.21(2)(b)** | Incident handling | *no risk mapped* |  |
| **Art.21(2)(c)** | Business continuity, backup management, disaster recovery and crisis management | [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) **20** critical [R04-1 National government services offline](../../../grc/risks/r04-1/index.html) **20** critical | [Governments and public services](../../../grc/stakeholders/public-sector/index.html), [Board and executives](../../../grc/stakeholders/board/index.html), [National governments](../../../grc/stakeholders/national-gov/index.html) |
| **Art.21(2)(d)** | Supply chain security, including the security of each direct supplier | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **Art.21(2)(e)** | Security in acquisition, development and maintenance, including vulnerability handling and disclosure | [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html) |
| **Art.23** | Reporting significant incidents: early warning in 24 hours, notification in 72 hours, final report in a month | [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) **15** high [R06-2 Essential and financial entities miss their reporting clocks](../../../grc/risks/r06-2/index.html) **12** high | [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html), [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [Data protection officer](../../../grc/stakeholders/dpo/index.html), [Board and executives](../../../grc/stakeholders/board/index.html), [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) |


---
site v0.22.9 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/nis2/index.html
