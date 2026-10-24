# Hosting and cloud providers: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for Hosting and cloud providers: 4 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / Hosting and cloud providers

# Hosting and cloud providers: its risk register

Shared hosts, managed PHP platforms and clouds: they patch for millions of customers at once, or leave the customer to do it.

**Kind** group · **Assigned here** 1 · **In its register** 4

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) | **15** high | Security | **treater** | [ISO/IEC 27001 A.8.8](../../../grc/frameworks/iso27001/index.html#c-a-8-8), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [NIST SP 800-53 SI-2](../../../grc/frameworks/nist80053/index.html#c-si-2), [CIS Controls 7.7](../../../grc/frameworks/cis/index.html#c-7-7) +3 |
| [R01-1 Default Apache mod_php installations exploited before application code runs](../../../grc/risks/r01-1/index.html) | **15** high | Security | *through* [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html) (owner) | [ISO/IEC 27001 A.8.8](../../../grc/frameworks/iso27001/index.html#c-a-8-8), [CIS Controls 7.4](../../../grc/frameworks/cis/index.html#c-7-4), [Cyber Essentials SUM](../../../grc/frameworks/cyberessentials/index.html#c-sum), [PCI DSS 6.3.3](../../../grc/frameworks/pcidss/index.html#c-6-3-3) |
| [R06-1 Personal data taken from a compromised PHP application](../../../grc/risks/r06-1/index.html) | **15** high | Compliance | *through* [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) (treater) | [GDPR Art.5(1)(f)](../../../grc/frameworks/gdpr/index.html#c-art-5-1-f), [GDPR Art.24](../../../grc/frameworks/gdpr/index.html#c-art-24), [GDPR Art.28](../../../grc/frameworks/gdpr/index.html#c-art-28), [GDPR Art.32](../../../grc/frameworks/gdpr/index.html#c-art-32) +2 |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) | **12** high | Security | *through* [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) (treater) | [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [ISO/IEC 27001 6.1.2](../../../grc/frameworks/iso27001/index.html#c-6-1-2) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 | 25 |
| 4 Likely | 4 | 8 | 12 | 16 | 20 |
| 3 Possible | 3 | 6 | 9 | 12 [R01-2](../../../grc/risks/r01-2/index.html) | 15 [R01](../../../grc/risks/r01/index.html) [R01-1](../../../grc/risks/r01-1/index.html) [R06-1](../../../grc/risks/r06-1/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Its parts
- [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html): 2 risks
- [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html): 1 risks

## Who it shares risks with

[Organisations running PHP](../../../grc/stakeholders/operators/index.html) (1), [People who use PHP services](../../../grc/stakeholders/people/index.html) (1), [The PHP project](../../../grc/stakeholders/php-project/index.html) (1), [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) (1), [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) (1)

## The standards its register touches

[GDPR](../../frameworks/gdpr/index.html) (6), [ISO/IEC 27001](../../frameworks/iso27001/index.html) (2), [CIS Controls](../../frameworks/cis/index.html) (2), [NIST CSF 2.0](../../frameworks/nistcsf/index.html) (1), [NIST SP 800-53](../../frameworks/nist80053/index.html) (1), [MITRE ATT&CK](../../frameworks/attack/index.html) (1), [OWASP Top 10s](../../frameworks/owasp/index.html) (1), [NIS2](../../frameworks/nis2/index.html) (1), [Cyber Essentials](../../frameworks/cyberessentials/index.html) (1), [PCI DSS](../../frameworks/pcidss/index.html) (1)


---
site v0.14.11 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/hosting/index.html
