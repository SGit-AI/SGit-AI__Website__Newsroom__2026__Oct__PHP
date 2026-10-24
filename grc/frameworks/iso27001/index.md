# ISO/IEC 27001: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each ISO/IEC 27001 clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / ISO/IEC 27001

# ISO/IEC 27001: the php2shell risks it governs

The management system most organisations in this story are certified to: risk assessment and treatment in clauses 6 and 8, and the controls an auditor will ask about after php2shell.

**Full name** ISO/IEC 27001:2022 Information security management systems, with the Annex A controls of ISO/IEC 27002:2022 · **Publisher** ISO and IEC · **Version** 2022 · [the official text](https://www.iso.org/standard/27001)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **6.1.2** | Information security risk assessment: identify risks and their owners | [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) **12** high [R07 Decisions made on numbers that measure something else](../../../grc/risks/r07/index.html) **12** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html), [Board and executives](../../../grc/stakeholders/board/index.html) |
| **6.1.3** | Information security risk treatment, and the statement of applicability | *no risk mapped* |  |
| **A.5.5** | Contact with authorities | [R04-3 The agencies' advice disagrees](../../../grc/risks/r04-3/index.html) **12** high | [Board and executives](../../../grc/stakeholders/board/index.html) |
| **A.5.6** | Contact with special interest groups | *no risk mapped* |  |
| **A.5.7** | Threat intelligence | [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) **20** critical [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html), [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **A.5.14** | Information transfer, including under agreed classification | [R02-2 Early mitigation advice to a few providers leaked](../../../grc/risks/r02-2/index.html) **9** medium [R10-2 A vault key or token published](../../../grc/risks/r10-2/index.html) **10** medium | [The PHP security team](../../../grc/stakeholders/php-security-team/index.html), [The editor](../../../grc/stakeholders/newsroom-editor/index.html) |
| **A.5.19** | Information security in supplier relationships | *no risk mapped* |  |
| **A.5.21** | Managing information security in the ICT supply chain | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **A.5.23** | Information security for use of cloud services | *no risk mapped* |  |
| **A.5.24** | Incident management planning and preparation | [R04-2 Councils and police offline without saying why](../../../grc/risks/r04-2/index.html) **15** high | [Local councils](../../../grc/stakeholders/councils/index.html) |
| **A.5.26** | Response to information security incidents | *no risk mapped* |  |
| **A.5.29** | Information security during disruption | [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) **20** critical [R04-1 National government services offline](../../../grc/risks/r04-1/index.html) **20** critical | [Governments and public services](../../../grc/stakeholders/public-sector/index.html), [Board and executives](../../../grc/stakeholders/board/index.html), [National governments](../../../grc/stakeholders/national-gov/index.html) |
| **A.5.30** | ICT readiness for business continuity | [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) **20** critical | [Governments and public services](../../../grc/stakeholders/public-sector/index.html), [Board and executives](../../../grc/stakeholders/board/index.html) |
| **A.8.8** | Management of technical vulnerabilities | [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) **15** high [R01-1 Default Apache mod_php installations exploited before application code runs](../../../grc/risks/r01-1/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html) |
| **A.8.9** | Configuration management | [R09 Not knowing where PHP runs](../../../grc/risks/r09/index.html) **16** high | [CTO](../../../grc/stakeholders/cto/index.html) |
| **A.8.16** | Monitoring activities | [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) **20** critical | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) |
| **A.8.20** | Network security | [R05 A web application firewall taken for a patch](../../../grc/risks/r05/index.html) **16** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **A.8.25** | Secure development life cycle | [R08-1 A known bug left unexploited, then unfixed, for two years](../../../grc/risks/r08-1/index.html) **16** high | [The PHP project](../../../grc/stakeholders/php-project/index.html) |
| **A.8.28** | Secure coding | *no risk mapped* |  |
| **A.8.29** | Security testing in development and acceptance | [R01-4 The fix is incomplete, or a third flaw follows](../../../grc/risks/r01-4/index.html) **15** high | [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html) |
| **A.8.32** | Change management | *no risk mapped* |  |


---
site v0.15.10 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/iso27001/index.html
