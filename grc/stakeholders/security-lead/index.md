# Security lead and AppSec: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for Security lead and AppSec: 6 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / [Organisations running PHP](../../../grc/stakeholders/operators/index.html) / [Inside any one organisation](../../../grc/stakeholders/org-roles/index.html) / Security lead and AppSec

# Security lead and AppSec: its risk register

Triage, detection, compensating controls and the call on whether an incident is declared.

**Kind** role · **Assigned here** 6 · **In its register** 6 · [the briefing for a security lead](../../../briefings/security/index.html)

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) | **20** critical | Disclosure process | **bearer** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIS2 Art.12](../../../grc/frameworks/nis2/index.html#c-art-12), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict) |
| [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) | **20** critical | Security | **treater** | [CISA KEV and BOD 22-01 KEV-entry](../../../grc/frameworks/kev/index.html#c-kev-entry), [CISA KEV and BOD 22-01 BOD22-01](../../../grc/frameworks/kev/index.html#c-bod22-01), [NIST CSF 2.0 DE.CM-01](../../../grc/frameworks/nistcsf/index.html#c-de-cm-01), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4) +3 |
| [R05 A web application firewall taken for a patch](../../../grc/risks/r05/index.html) | **16** high | Security | **owner** | [PCI DSS 6.4.2](../../../grc/frameworks/pcidss/index.html#c-6-4-2), [CIS Controls 13.10](../../../grc/frameworks/cis/index.html#c-13-10), [NIST SP 800-53 SC-7](../../../grc/frameworks/nist80053/index.html#c-sc-7), [ISO/IEC 27001 A.8.20](../../../grc/frameworks/iso27001/index.html#c-a-8-20) +1 |
| [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) | **15** high | Security | **owner** | [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [ISO/IEC 27001 A.5.7](../../../grc/frameworks/iso27001/index.html#c-a-5-7), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4), [PCI DSS 12.10.1](../../../grc/frameworks/pcidss/index.html#c-12-10-1) |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) | **12** high | Security | **owner** | [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [ISO/IEC 27001 6.1.2](../../../grc/frameworks/iso27001/index.html#c-6-1-2) |
| [R03-4 Detections built on a proof of concept with the wrong mechanism](../../../grc/risks/r03-4/index.html) | **12** high | Security | **owner** | [NIST SP 800-53 RA-5](../../../grc/frameworks/nist80053/index.html#c-ra-5), [SOC 2 CC7.1](../../../grc/frameworks/soc2/index.html#c-cc7-1), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 [R02](../../../grc/risks/r02/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 | 16 [R05](../../../grc/risks/r05/index.html) | 20 [R03](../../../grc/risks/r03/index.html) |
| 3 Possible | 3 | 6 | 9 | 12 [R01-2](../../../grc/risks/r01-2/index.html) [R03-4](../../../grc/risks/r03-4/index.html) | 15 [R03-1](../../../grc/risks/r03-1/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Who it shares risks with

[Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) (3), [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (2), [Organisations running PHP](../../../grc/stakeholders/operators/index.html) (2), [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) (1), [The finders](../../../grc/stakeholders/finders/index.html) (1), [Distributors and packagers](../../../grc/stakeholders/distributors/index.html) (1), [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) (1), [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html) (1), [Online shops and payments](../../../grc/stakeholders/commerce/index.html) (1)

## The standards its register touches

[NIST CSF 2.0](../../frameworks/nistcsf/index.html) (4), [ISO/IEC 27001](../../frameworks/iso27001/index.html) (4), [NIST SP 800-53](../../frameworks/nist80053/index.html) (3), [CISA KEV and BOD 22-01](../../frameworks/kev/index.html) (2), [PCI DSS](../../frameworks/pcidss/index.html) (2), [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) (1), [NIS2](../../frameworks/nis2/index.html) (1), [FIRST TLP 2.0](../../frameworks/tlp/index.html) (1), [MITRE ATT&CK](../../frameworks/attack/index.html) (1), [SOC 2](../../frameworks/soc2/index.html) (1), [CIS Controls](../../frameworks/cis/index.html) (1), [Cyber Essentials](../../frameworks/cyberessentials/index.html) (1)


---
site v0.15.2 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/security-lead/index.html
