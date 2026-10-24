# Threat intelligence and detection: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for Threat intelligence and detection: 4 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) / Threat intelligence and detection

# Threat intelligence and detection: its risk register

Amazon's honeypots, Huntress, watchTowr and the community authors of detection rules: the eyes that say whether exploitation is happening.

**Kind** group · **Assigned here** 4 · **In its register** 4 · in the story as [Amazon](../../../actors/index.html#amazon), [Huntress](../../../actors/index.html#huntress), [watchTowr](../../../actors/index.html#watchtowr), [Community detection authors](../../../actors/index.html#detectors)

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) | **20** critical | Security | **informer** | [CISA KEV and BOD 22-01 KEV-entry](../../../grc/frameworks/kev/index.html#c-kev-entry), [CISA KEV and BOD 22-01 BOD22-01](../../../grc/frameworks/kev/index.html#c-bod22-01), [NIST CSF 2.0 DE.CM-01](../../../grc/frameworks/nistcsf/index.html#c-de-cm-01), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4) +3 |
| [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) | **15** high | Security | **informer** | [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [ISO/IEC 27001 A.5.7](../../../grc/frameworks/iso27001/index.html#c-a-5-7), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4), [PCI DSS 12.10.1](../../../grc/frameworks/pcidss/index.html#c-12-10-1) |
| [R03-3 Exploited in the wild without anyone being able to show it](../../../grc/risks/r03-3/index.html) | **12** high | Governance | **informer** | [CISA KEV and BOD 22-01 KEV-entry](../../../grc/frameworks/kev/index.html#c-kev-entry), [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [NIST CSF 2.0 GV.RR-01](../../../grc/frameworks/nistcsf/index.html#c-gv-rr-01) |
| [R03-4 Detections built on a proof of concept with the wrong mechanism](../../../grc/risks/r03-4/index.html) | **12** high | Security | **treater** | [NIST SP 800-53 RA-5](../../../grc/frameworks/nist80053/index.html#c-ra-5), [SOC 2 CC7.1](../../../grc/frameworks/soc2/index.html#c-cc7-1), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 | 25 |
| 4 Likely | 4 | 8 | 12 | 16 | 20 [R03](../../../grc/risks/r03/index.html) |
| 3 Possible | 3 | 6 | 9 | 12 [R03-3](../../../grc/risks/r03-3/index.html) [R03-4](../../../grc/risks/r03-4/index.html) | 15 [R03-1](../../../grc/risks/r03-1/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Who it shares risks with

[Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) (3), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) (2), [Organisations running PHP](../../../grc/stakeholders/operators/index.html) (1), [Board and executives](../../../grc/stakeholders/board/index.html) (1)

## The standards its register touches

[NIST CSF 2.0](../../frameworks/nistcsf/index.html) (4), [CISA KEV and BOD 22-01](../../frameworks/kev/index.html) (2), [NIST SP 800-53](../../frameworks/nist80053/index.html) (2), [ISO/IEC 27001](../../frameworks/iso27001/index.html) (2), [MITRE ATT&CK](../../frameworks/attack/index.html) (1), [PCI DSS](../../frameworks/pcidss/index.html) (1), [SOC 2](../../frameworks/soc2/index.html) (1)


---
site v0.17.0 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/threat-intel/index.html
