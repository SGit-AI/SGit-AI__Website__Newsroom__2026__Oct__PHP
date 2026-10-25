# CIS Controls: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each CIS Controls clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / CIS Controls

# CIS Controls: the php2shell risks it governs

The prioritised list smaller organisations, councils and schools among them, actually work from.

**Full name** CIS Critical Security Controls v8.1 · **Publisher** Center for Internet Security · **Version** 8.1 · [the official text](https://www.cisecurity.org/controls/v8-1)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **2.2** | Ensure authorised software is currently supported | [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../../grc/risks/r01-3/index.html) **20** critical | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **7.1** | Establish and maintain a vulnerability management process | *no risk mapped* |  |
| **7.4** | Perform automated application patch management | [R01-1 Default Apache mod_php installations exploited before application code runs](../../../grc/risks/r01-1/index.html) **15** high | [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html) |
| **7.7** | Remediate detected vulnerabilities | [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html) |
| **13.10** | Perform application layer filtering | [R03-2 Mass scanning and mutated payloads after the leak](../../../grc/risks/r03-2/index.html) **20** critical [R05 A web application firewall taken for a patch](../../../grc/risks/r05/index.html) **16** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **16.4** | Establish and manage an inventory of third-party software components | [R01-5 Popular applications compromised before authentication](../../../grc/risks/r01-5/index.html) **15** high [R09 Not knowing where PHP runs](../../../grc/risks/r09/index.html) **16** high | [Website owner](../../../grc/stakeholders/site-owner/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **17.4** | Establish and maintain an incident response process | *no risk mapped* |  |


---
site v0.19.0 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/cis/index.html
