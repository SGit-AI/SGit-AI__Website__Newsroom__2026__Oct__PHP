# NIST CSF 2.0: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each NIST CSF 2.0 clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / NIST CSF 2.0

# NIST CSF 2.0: the php2shell risks it governs

The outcome language boards and regulators on both sides of the Atlantic now use; GOVERN makes supply chain and risk ownership a first-class function.

**Full name** NIST Cybersecurity Framework 2.0 (CSWP 29) · **Publisher** US National Institute of Standards and Technology · **Version** 2.0, February 2024 · [the official text](https://doi.org/10.6028/NIST.CSWP.29)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **GV.RM-01** | Risk management objectives are established and agreed by stakeholders | [R07 Decisions made on numbers that measure something else](../../../grc/risks/r07/index.html) **12** high | [Board and executives](../../../grc/stakeholders/board/index.html) |
| **GV.RR-01** | Leadership is responsible and accountable for cybersecurity risk | [R03-3 Exploited in the wild without anyone being able to show it](../../../grc/risks/r03-3/index.html) **12** high [R04-3 The agencies' advice disagrees](../../../grc/risks/r04-3/index.html) **12** high | [Board and executives](../../../grc/stakeholders/board/index.html), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) |
| **GV.SC-05** | Supply chain requirements are established and integrated into contracts | [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) **16** high | [Distributors and packagers](../../../grc/stakeholders/distributors/index.html), [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) |
| **GV.SC-07** | Supplier risks are understood, recorded, prioritised, assessed, responded to and monitored | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) **16** high | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **ID.AM-02** | Inventories of software, services and systems are maintained | [R09 Not knowing where PHP runs](../../../grc/risks/r09/index.html) **16** high | [CTO](../../../grc/stakeholders/cto/index.html) |
| **ID.RA-01** | Vulnerabilities in assets are identified, validated and recorded | [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) **15** high [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) **12** high [R03-4 Detections built on a proof of concept with the wrong mechanism](../../../grc/risks/r03-4/index.html) **12** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html), [Organisations running PHP](../../../grc/stakeholders/operators/index.html) |
| **ID.RA-02** | Threat intelligence is received from information sharing forums and sources | [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) **15** high [R03-3 Exploited in the wild without anyone being able to show it](../../../grc/risks/r03-3/index.html) **12** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html), [Board and executives](../../../grc/stakeholders/board/index.html) |
| **ID.RA-08** | Processes for receiving, analysing and responding to vulnerability disclosures are established | [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) **20** critical [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../../grc/risks/r02-1/index.html) **20** critical [R08-2 Several finders, one small team](../../../grc/risks/r08-2/index.html) **12** high | [The PHP security team](../../../grc/stakeholders/php-security-team/index.html), [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) |
| **PR.PS-02** | Software is maintained, replaced and removed commensurate with risk | [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../../grc/risks/r01-3/index.html) **20** critical | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **DE.CM-01** | Networks and network services are monitored to find potentially adverse events | [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) **20** critical [R03-2 Mass scanning and mutated payloads after the leak](../../../grc/risks/r03-2/index.html) **20** critical | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) |
| **RS.MA-01** | The incident response plan is executed with relevant third parties once an incident is declared | *no risk mapped* |  |
| **RS.CO-03** | Information is shared with designated internal and external stakeholders | [R04-2 Councils and police offline without saying why](../../../grc/risks/r04-2/index.html) **15** high | [Local councils](../../../grc/stakeholders/councils/index.html) |
| **RC.RP-01** | The recovery portion of the incident response plan is executed | [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) **20** critical [R04-1 National government services offline](../../../grc/risks/r04-1/index.html) **20** critical | [Governments and public services](../../../grc/stakeholders/public-sector/index.html), [Board and executives](../../../grc/stakeholders/board/index.html), [National governments](../../../grc/stakeholders/national-gov/index.html) |


---
site v0.22.15 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/nistcsf/index.html
