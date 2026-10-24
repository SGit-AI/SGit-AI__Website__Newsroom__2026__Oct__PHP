# The PHP security team: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for The PHP security team: 7 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / [The PHP project](../../../grc/stakeholders/php-project/index.html) / The PHP security team

# The PHP security team: its risk register

Received the reports, ran the embargo, published the advisories and the oss-security announcements.

**Kind** team · **Assigned here** 7 · **In its register** 7 · in the story as [Jakub Zelenka](../../../actors/index.html#zelenka), [Alexandre Daubois, PHP security team](../../../actors/index.html#daubois)

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) | **20** critical | Disclosure process | **owner** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIS2 Art.12](../../../grc/frameworks/nis2/index.html#c-art-12), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict) |
| [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../../grc/risks/r02-1/index.html) | **20** critical | Disclosure process | **owner** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08) |
| [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) | **16** high | Supply chain | **regulator** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [NIST CSF 2.0 GV.SC-05](../../../grc/frameworks/nistcsf/index.html#c-gv-sc-05), [OWASP Top 10s A03:2025](../../../grc/frameworks/owasp/index.html#c-a03-2025) |
| [R01-4 The fix is incomplete, or a third flaw follows](../../../grc/risks/r01-4/index.html) | **15** high | Security | **treater** | [NIST SSDF RV.3](../../../grc/frameworks/ssdf/index.html#c-rv-3), [NIST SSDF PW.8](../../../grc/frameworks/ssdf/index.html#c-pw-8), [ISO/IEC 27001 A.8.29](../../../grc/frameworks/iso27001/index.html#c-a-8-29), [ISO/IEC 29147 and 30111 30111:handling](../../../grc/frameworks/iso29147/index.html#c-30111-handling) |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) | **12** high | Security | **informer** | [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [ISO/IEC 27001 6.1.2](../../../grc/frameworks/iso27001/index.html#c-6-1-2) |
| [R08-2 Several finders, one small team](../../../grc/risks/r08-2/index.html) | **12** high | Operational | **bearer** | [ISO/IEC 29147 and 30111 29147:receipt](../../../grc/frameworks/iso29147/index.html#c-29147-receipt), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [NIST SSDF RV.1](../../../grc/frameworks/ssdf/index.html#c-rv-1) |
| [R02-2 Early mitigation advice to a few providers leaked](../../../grc/risks/r02-2/index.html) | **9** medium | Disclosure process | **owner** | [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict), [ISO/IEC 27001 A.5.14](../../../grc/frameworks/iso27001/index.html#c-a-5-14), [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 [R02](../../../grc/risks/r02/index.html) [R02-1](../../../grc/risks/r02-1/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 [R08-2](../../../grc/risks/r08-2/index.html) | 16 [R02-3](../../../grc/risks/r02-3/index.html) | 20 |
| 3 Possible | 3 | 6 | 9 [R02-2](../../../grc/risks/r02-2/index.html) | 12 [R01-2](../../../grc/risks/r01-2/index.html) | 15 [R01-4](../../../grc/risks/r01-4/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Who it shares risks with

[Organisations running PHP](../../../grc/stakeholders/operators/index.html) (3), [The finders](../../../grc/stakeholders/finders/index.html) (3), [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) (2), [Distributors and packagers](../../../grc/stakeholders/distributors/index.html) (2), [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) (1), [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html) (1), [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) (1), [Calif](../../../grc/stakeholders/calif/index.html) (1), [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) (1), [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) (1), [Chainguard](../../../grc/stakeholders/chainguard/index.html) (1), [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) (1)

## The standards its register touches

[NIST CSF 2.0](../../frameworks/nistcsf/index.html) (3), [ISO/IEC 27001](../../frameworks/iso27001/index.html) (3), [NIST SSDF](../../frameworks/ssdf/index.html) (3), [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) (3), [NIS2](../../frameworks/nis2/index.html) (1), [FIRST TLP 2.0](../../frameworks/tlp/index.html) (1), [Cyber Resilience Act](../../frameworks/cra/index.html) (1), [OWASP Top 10s](../../frameworks/owasp/index.html) (1)


---
site v0.15.19 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/php-security-team/index.html
