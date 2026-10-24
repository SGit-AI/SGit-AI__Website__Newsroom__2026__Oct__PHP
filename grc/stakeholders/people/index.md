# People who use PHP services: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for People who use PHP services: 5 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / People who use PHP services

# People who use PHP services: its risk register

Citizens, customers and readers: they cannot patch anything, and they bear the outage and the breach.

**Kind** group · **Assigned here** 1 · **In its register** 5

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) | **20** critical | Operational | *through* [People who need a service that went offline](../../../grc/stakeholders/service-users/index.html) (bearer) | [ISO/IEC 27001 A.5.29](../../../grc/frameworks/iso27001/index.html#c-a-5-29), [ISO/IEC 27001 A.5.30](../../../grc/frameworks/iso27001/index.html#c-a-5-30), [NIS2 Art.21(2)(c)](../../../grc/frameworks/nis2/index.html#c-art-21-2-c), [DORA Art.11](../../../grc/frameworks/dora/index.html#c-art-11) +2 |
| [R04-1 National government services offline](../../../grc/risks/r04-1/index.html) | **20** critical | Operational | *through* [People who need a service that went offline](../../../grc/stakeholders/service-users/index.html) (bearer) | [NIS2 Art.21(2)(c)](../../../grc/frameworks/nis2/index.html#c-art-21-2-c), [ISO/IEC 27001 A.5.29](../../../grc/frameworks/iso27001/index.html#c-a-5-29), [NIST CSF 2.0 RC.RP-01](../../../grc/frameworks/nistcsf/index.html#c-rc-rp-01) |
| [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) | **15** high | Security | **bearer** | [ISO/IEC 27001 A.8.8](../../../grc/frameworks/iso27001/index.html#c-a-8-8), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [NIST SP 800-53 SI-2](../../../grc/frameworks/nist80053/index.html#c-si-2), [CIS Controls 7.7](../../../grc/frameworks/cis/index.html#c-7-7) +3 |
| [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) | **15** high | Compliance | *through* [People whose data is held in PHP applications](../../../grc/stakeholders/data-subjects/index.html) (bearer) | [GDPR Art.32](../../../grc/frameworks/gdpr/index.html#c-art-32), [GDPR Art.33](../../../grc/frameworks/gdpr/index.html#c-art-33), [GDPR Art.34](../../../grc/frameworks/gdpr/index.html#c-art-34), [NIS2 Art.23](../../../grc/frameworks/nis2/index.html#c-art-23) +2 |
| [R06-1 Personal data taken from a compromised PHP application](../../../grc/risks/r06-1/index.html) | **15** high | Compliance | *through* [People whose data is held in PHP applications](../../../grc/stakeholders/data-subjects/index.html) (bearer) | [GDPR Art.5(1)(f)](../../../grc/frameworks/gdpr/index.html#c-art-5-1-f), [GDPR Art.24](../../../grc/frameworks/gdpr/index.html#c-art-24), [GDPR Art.28](../../../grc/frameworks/gdpr/index.html#c-art-28), [GDPR Art.32](../../../grc/frameworks/gdpr/index.html#c-art-32) +2 |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 [R04](../../../grc/risks/r04/index.html) [R04-1](../../../grc/risks/r04-1/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 | 16 | 20 |
| 3 Possible | 3 | 6 | 9 | 12 | 15 [R01](../../../grc/risks/r01/index.html) [R06](../../../grc/risks/r06/index.html) [R06-1](../../../grc/risks/r06-1/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Its parts
- [People whose data is held in PHP applications](../../../grc/stakeholders/data-subjects/index.html): 2 risks
- [People who need a service that went offline](../../../grc/stakeholders/service-users/index.html): 2 risks

## Who it shares risks with

[Organisations running PHP](../../../grc/stakeholders/operators/index.html) (1), [The PHP project](../../../grc/stakeholders/php-project/index.html) (1), [Hosting and cloud providers](../../../grc/stakeholders/hosting/index.html) (1), [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) (1), [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) (1)

## The standards its register touches

[GDPR](../../frameworks/gdpr/index.html) (6), [ISO/IEC 27001](../../frameworks/iso27001/index.html) (3), [NIS2](../../frameworks/nis2/index.html) (3), [NIST CSF 2.0](../../frameworks/nistcsf/index.html) (2), [NIST SP 800-53](../../frameworks/nist80053/index.html) (2), [DORA](../../frameworks/dora/index.html) (2), [CIS Controls](../../frameworks/cis/index.html) (1), [MITRE ATT&CK](../../frameworks/attack/index.html) (1), [OWASP Top 10s](../../frameworks/owasp/index.html) (1), [Cyber Resilience Act](../../frameworks/cra/index.html) (1)


---
site v0.14.1 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/people/index.html
