# OWASP Top 10s: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each OWASP Top 10s clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / OWASP Top 10s

# OWASP Top 10s: the php2shell risks it governs

A06 is php2shell for everyone downstream of PHP; the LLM list is the risk register for this newsroom's own agents, which read the open web and hold publishing rights.

**Full name** OWASP Top 10 (2021 and 2025) and OWASP Top 10 for LLM Applications (2025) · **Publisher** OWASP Foundation · **Version** 2021, 2025 · [the official text](https://owasp.org/www-project-top-ten/)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **A06:2021** | Vulnerable and outdated components | [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) **15** high [R01-5 Popular applications compromised before authentication](../../../grc/risks/r01-5/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [Website owner](../../../grc/stakeholders/site-owner/index.html) |
| **A03:2025** | Software supply chain failures | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html), [Distributors and packagers](../../../grc/stakeholders/distributors/index.html), [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) |
| **LLM01:2025** | Prompt injection | [R10-1 Prompt injection through captured material](../../../grc/risks/r10-1/index.html) **12** high | [The editor](../../../grc/stakeholders/newsroom-editor/index.html) |
| **LLM02:2025** | Sensitive information disclosure | [R10-2 A vault key or token published](../../../grc/risks/r10-2/index.html) **10** medium | [The editor](../../../grc/stakeholders/newsroom-editor/index.html) |
| **LLM06:2025** | Excessive agency | [R10 This newsroom's own agents are steered, leak or mislead](../../../grc/risks/r10/index.html) **12** high | [The editor](../../../grc/stakeholders/newsroom-editor/index.html) |
| **LLM09:2025** | Misinformation | [R07 Decisions made on numbers that measure something else](../../../grc/risks/r07/index.html) **12** high [R10-3 A status word stronger than its evidence](../../../grc/risks/r10-3/index.html) **12** high | [Board and executives](../../../grc/stakeholders/board/index.html), [The editor](../../../grc/stakeholders/newsroom-editor/index.html) |


---
site v0.21.6 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/owasp/index.html
