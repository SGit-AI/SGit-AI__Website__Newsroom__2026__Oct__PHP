# NIST SP 800-53: the php2shell risks it governs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each NIST SP 800-53 clause or control the GRC desk cites, the php2shell risks mapped to it and who owns them.

[Frameworks](../index.html) / NIST SP 800-53

# NIST SP 800-53: the php2shell risks it governs

The control catalogue behind US federal systems, which CISA and the NSA told to update or go offline.

**Full name** NIST SP 800-53 Rev. 5 Security and Privacy Controls for Information Systems and Organizations · **Publisher** US National Institute of Standards and Technology · **Version** Rev. 5 · [the official text](https://doi.org/10.6028/NIST.SP.800-53r5)

## Clauses and controls

| Control | What it asks (paraphrased) | Risks mapped | Owned or regulated by |
|---|---|---|---|
| **RA-3** | Risk assessment | *no risk mapped* |  |
| **RA-5** | Vulnerability monitoring and scanning | [R03-4 Detections built on a proof of concept with the wrong mechanism](../../../grc/risks/r03-4/index.html) **12** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **SI-2** | Flaw remediation | [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html) |
| **SI-4** | System monitoring | [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) **20** critical [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) **15** high | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html), [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **SA-22** | Unsupported system components | [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../../grc/risks/r01-3/index.html) **20** critical | [Organisations running PHP](../../../grc/stakeholders/operators/index.html), [CTO](../../../grc/stakeholders/cto/index.html) |
| **CM-8** | System component inventory | [R09 Not knowing where PHP runs](../../../grc/risks/r09/index.html) **16** high | [CTO](../../../grc/stakeholders/cto/index.html) |
| **SC-7** | Boundary protection | [R05 A web application firewall taken for a patch](../../../grc/risks/r05/index.html) **16** high | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) |
| **CP-2** | Contingency plan | [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) **20** critical | [Governments and public services](../../../grc/stakeholders/public-sector/index.html), [Board and executives](../../../grc/stakeholders/board/index.html) |
| **IR-4** | Incident handling | *no risk mapped* |  |
| **IR-6** | Incident reporting | [R06-2 Essential and financial entities miss their reporting clocks](../../../grc/risks/r06-2/index.html) **12** high | [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html), [Banks, insurers and financial entities](../../../grc/stakeholders/finance/index.html), [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) |
| **SR-3** | Supply chain controls and processes | *no risk mapped* |  |
| **PM-15** | Security and privacy groups and associations | *no risk mapped* |  |


---
site v0.10.17 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/nist80053/index.html
