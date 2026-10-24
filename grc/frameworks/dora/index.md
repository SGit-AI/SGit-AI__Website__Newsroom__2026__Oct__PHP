# DORA: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each DORA clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / DORA

# DORA: the php2shell risks it governs

Banks, insurers and other financial entities running PHP, or relying on an ICT provider that does, must identify, protect, detect, respond and report under one regime, and manage the provider as a third-party risk.

**Full name** Digital Operational Resilience Act, Regulation (EU) 2022/2554 · **Publisher** European Union · **Version** 2022, applies from 17 January 2025 · [the official text](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **Art.8** | Identification of ICT assets, their dependencies and the risks to them | [R09 Not knowing where PHP runs](../../../grc/risks/r09/index.html) **16** high | [CTO](../../../grc/stakeholders/cto/index.html) |
| **Art.9** | Protection and prevention, including patches and updates | *no risk mapped* |  |
| **Art.10** | Detection of anomalous activities | [R06-2 Essential and financial entities miss their reporting clocks](../../../grc/risks/r06-2/index.html) **12** high | [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html), [Banks, insurers and financial entities](../../../grc/stakeholders/finance/index.html), [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) |
| **Art.11** | Response and recovery, including ICT business continuity | [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) **20** critical | [Governments and public services](../../../grc/stakeholders/public-sector/index.html), [Board and executives](../../../grc/stakeholders/board/index.html) |
| **Art.19** | Reporting major ICT-related incidents | [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) **15** high [R06-2 Essential and financial entities miss their reporting clocks](../../../grc/risks/r06-2/index.html) **12** high | [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html), [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [Data protection officer](../../../grc/stakeholders/dpo/index.html), [Board and executives](../../../grc/stakeholders/board/index.html), [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) |
| **Art.28** | Managing ICT third-party risk | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |


---
site v0.15.5 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/dora/index.html
