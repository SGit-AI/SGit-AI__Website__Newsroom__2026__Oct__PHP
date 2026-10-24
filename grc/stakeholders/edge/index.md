# Edge, WAF and detection vendors: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for Edge, WAF and detection vendors: 8 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / Edge, WAF and detection vendors

# Edge, WAF and detection vendors: its risk register

Cloudflare, Akamai, Fastly, Imperva and others who shipped filters before disclosure, and the threat-intelligence firms who reported what they saw.

**Kind** group · **Assigned here** 2 · **In its register** 8 · in the story as [Cloudflare](../../../actors/index.html#cloudflare), [Akamai](../../../actors/index.html#akamai), [Fastly](../../../actors/index.html#fastly), [Imperva Threat Research](../../../actors/index.html#imperva)

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../../grc/risks/r02-1/index.html) | **20** critical | Disclosure process | **treater** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08) |
| [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) | **20** critical | Security | *through* [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) (informer) | [CISA KEV and BOD 22-01 KEV-entry](../../../grc/frameworks/kev/index.html#c-kev-entry), [CISA KEV and BOD 22-01 BOD22-01](../../../grc/frameworks/kev/index.html#c-bod22-01), [NIST CSF 2.0 DE.CM-01](../../../grc/frameworks/nistcsf/index.html#c-de-cm-01), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4) +3 |
| [R03-2 Mass scanning and mutated payloads after the leak](../../../grc/risks/r03-2/index.html) | **20** critical | Security | *through* [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html) (treater) | [MITRE ATT&CK T1595.002](../../../grc/frameworks/attack/index.html#c-t1595-002), [NIST CSF 2.0 DE.CM-01](../../../grc/frameworks/nistcsf/index.html#c-de-cm-01), [CIS Controls 13.10](../../../grc/frameworks/cis/index.html#c-13-10) |
| [R05 A web application firewall taken for a patch](../../../grc/risks/r05/index.html) | **16** high | Security | *through* [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html) (informer) | [PCI DSS 6.4.2](../../../grc/frameworks/pcidss/index.html#c-6-4-2), [CIS Controls 13.10](../../../grc/frameworks/cis/index.html#c-13-10), [NIST SP 800-53 SC-7](../../../grc/frameworks/nist80053/index.html#c-sc-7), [ISO/IEC 27001 A.8.20](../../../grc/frameworks/iso27001/index.html#c-a-8-20) +1 |
| [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) | **15** high | Security | **treater** | [ISO/IEC 27001 A.8.8](../../../grc/frameworks/iso27001/index.html#c-a-8-8), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [NIST SP 800-53 SI-2](../../../grc/frameworks/nist80053/index.html#c-si-2), [CIS Controls 7.7](../../../grc/frameworks/cis/index.html#c-7-7) +3 |
| [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) | **15** high | Security | *through* [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) (informer) | [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [ISO/IEC 27001 A.5.7](../../../grc/frameworks/iso27001/index.html#c-a-5-7), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4), [PCI DSS 12.10.1](../../../grc/frameworks/pcidss/index.html#c-12-10-1) |
| [R03-3 Exploited in the wild without anyone being able to show it](../../../grc/risks/r03-3/index.html) | **12** high | Governance | *through* [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) (informer) | [CISA KEV and BOD 22-01 KEV-entry](../../../grc/frameworks/kev/index.html#c-kev-entry), [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [NIST CSF 2.0 GV.RR-01](../../../grc/frameworks/nistcsf/index.html#c-gv-rr-01) |
| [R03-4 Detections built on a proof of concept with the wrong mechanism](../../../grc/risks/r03-4/index.html) | **12** high | Security | *through* [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) (treater) | [NIST SP 800-53 RA-5](../../../grc/frameworks/nist80053/index.html#c-ra-5), [SOC 2 CC7.1](../../../grc/frameworks/soc2/index.html#c-cc7-1), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 [R02-1](../../../grc/risks/r02-1/index.html) [R03-2](../../../grc/risks/r03-2/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 | 16 [R05](../../../grc/risks/r05/index.html) | 20 [R03](../../../grc/risks/r03/index.html) |
| 3 Possible | 3 | 6 | 9 | 12 [R03-3](../../../grc/risks/r03-3/index.html) [R03-4](../../../grc/risks/r03-4/index.html) | 15 [R01](../../../grc/risks/r01/index.html) [R03-1](../../../grc/risks/r03-1/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Its parts
- [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html): 2 risks
- [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html): 4 risks

## Who it shares risks with

[Organisations running PHP](../../../grc/stakeholders/operators/index.html) (1), [People who use PHP services](../../../grc/stakeholders/people/index.html) (1), [The PHP project](../../../grc/stakeholders/php-project/index.html) (1), [Hosting and cloud providers](../../../grc/stakeholders/hosting/index.html) (1), [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) (1), [Calif](../../../grc/stakeholders/calif/index.html) (1), [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (1)

## The standards its register touches

[NIST CSF 2.0](../../frameworks/nistcsf/index.html) (5), [ISO/IEC 27001](../../frameworks/iso27001/index.html) (4), [NIST SP 800-53](../../frameworks/nist80053/index.html) (4), [CIS Controls](../../frameworks/cis/index.html) (2), [MITRE ATT&CK](../../frameworks/attack/index.html) (2), [CISA KEV and BOD 22-01](../../frameworks/kev/index.html) (2), [PCI DSS](../../frameworks/pcidss/index.html) (2), [OWASP Top 10s](../../frameworks/owasp/index.html) (1), [NIS2](../../frameworks/nis2/index.html) (1), [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) (1), [SOC 2](../../frameworks/soc2/index.html) (1), [Cyber Essentials](../../frameworks/cyberessentials/index.html) (1)


---
site v0.15.18 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/edge/index.html
