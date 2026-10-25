# The PHP project: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for The PHP project: 11 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / The PHP project

# The PHP project: its risk register

The people who write, fix and release PHP: the PHP Group, the PHP Foundation, the security team and the fix authors.

**Kind** group · **Assigned here** 3 · **In its register** 11 · in the story as [The PHP Group / php.net](../../../actors/index.html#php-group), [The PHP Foundation](../../../actors/index.html#php-foundation)

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) | **20** critical | Disclosure process | *through* [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (owner) | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIS2 Art.12](../../../grc/frameworks/nis2/index.html#c-art-12), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict) |
| [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../../grc/risks/r02-1/index.html) | **20** critical | Disclosure process | *through* [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (owner) | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08) |
| [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../../grc/risks/r08/index.html) | **20** critical | Strategic | **bearer** | [EU AI Act Art.55](../../../grc/frameworks/euaiact/index.html#c-art-55), [NIST AI RMF GOVERN-6.1](../../../grc/frameworks/nistairmf/index.html#c-govern-6-1), [NIST AI RMF MEASURE-2.7](../../../grc/frameworks/nistairmf/index.html#c-measure-2-7), [ISO/IEC 42001 6.1.2](../../../grc/frameworks/iso42001/index.html#c-6-1-2) |
| [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) | **16** high | Supply chain | *through* [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (regulator) | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [NIST CSF 2.0 GV.SC-05](../../../grc/frameworks/nistcsf/index.html#c-gv-sc-05), [OWASP Top 10s A03:2025](../../../grc/frameworks/owasp/index.html#c-a03-2025) |
| [R08-1 A known bug left unexploited, then unfixed, for two years](../../../grc/risks/r08-1/index.html) | **16** high | Strategic | **owner** | [NIST SSDF PW.7](../../../grc/frameworks/ssdf/index.html#c-pw-7), [NIST SSDF RV.2](../../../grc/frameworks/ssdf/index.html#c-rv-2), [Cyber Resilience Act Art.24](../../../grc/frameworks/cra/index.html#c-art-24), [ISO/IEC 27001 A.8.25](../../../grc/frameworks/iso27001/index.html#c-a-8-25) |
| [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) | **15** high | Security | **treater** | [ISO/IEC 27001 A.8.8](../../../grc/frameworks/iso27001/index.html#c-a-8-8), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [NIST SP 800-53 SI-2](../../../grc/frameworks/nist80053/index.html#c-si-2), [CIS Controls 7.7](../../../grc/frameworks/cis/index.html#c-7-7) +3 |
| [R01-4 The fix is incomplete, or a third flaw follows](../../../grc/risks/r01-4/index.html) | **15** high | Security | *through* [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html) (owner), [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (treater) | [NIST SSDF RV.3](../../../grc/frameworks/ssdf/index.html#c-rv-3), [NIST SSDF PW.8](../../../grc/frameworks/ssdf/index.html#c-pw-8), [ISO/IEC 27001 A.8.29](../../../grc/frameworks/iso27001/index.html#c-a-8-29), [ISO/IEC 29147 and 30111 30111:handling](../../../grc/frameworks/iso29147/index.html#c-30111-handling) |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) | **12** high | Security | *through* [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (informer) | [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [ISO/IEC 27001 6.1.2](../../../grc/frameworks/iso27001/index.html#c-6-1-2) |
| [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../../grc/risks/r06-3/index.html) | **12** high | Compliance | *through* [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) (informer) | [Cyber Resilience Act Art.14](../../../grc/frameworks/cra/index.html#c-art-14), [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [Cyber Resilience Act Art.24](../../../grc/frameworks/cra/index.html#c-art-24), [Cyber Resilience Act AnnexI.II](../../../grc/frameworks/cra/index.html#c-annexi-ii) |
| [R08-2 Several finders, one small team](../../../grc/risks/r08-2/index.html) | **12** high | Operational | *through* [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (bearer), [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) (owner) | [ISO/IEC 29147 and 30111 29147:receipt](../../../grc/frameworks/iso29147/index.html#c-29147-receipt), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [NIST SSDF RV.1](../../../grc/frameworks/ssdf/index.html#c-rv-1) |
| [R02-2 Early mitigation advice to a few providers leaked](../../../grc/risks/r02-2/index.html) | **9** medium | Disclosure process | *through* [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (owner) | [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict), [ISO/IEC 27001 A.5.14](../../../grc/frameworks/iso27001/index.html#c-a-5-14), [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 [R02](../../../grc/risks/r02/index.html) [R02-1](../../../grc/risks/r02-1/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 [R08-2](../../../grc/risks/r08-2/index.html) | 16 [R02-3](../../../grc/risks/r02-3/index.html) [R08-1](../../../grc/risks/r08-1/index.html) | 20 [R08](../../../grc/risks/r08/index.html) |
| 3 Possible | 3 | 6 | 9 [R02-2](../../../grc/risks/r02-2/index.html) | 12 [R01-2](../../../grc/risks/r01-2/index.html) [R06-3](../../../grc/risks/r06-3/index.html) | 15 [R01](../../../grc/risks/r01/index.html) [R01-4](../../../grc/risks/r01-4/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Its parts
- [The PHP security team](../../../grc/stakeholders/php-security-team/index.html): 7 risks
- [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html): 1 risks
- [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html): 3 risks

## Who it shares risks with

[Organisations running PHP](../../../grc/stakeholders/operators/index.html) (1), [People who use PHP services](../../../grc/stakeholders/people/index.html) (1), [Hosting and cloud providers](../../../grc/stakeholders/hosting/index.html) (1), [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) (1), [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) (1), [OpenAI (Patch the Planet)](../../../grc/stakeholders/openai/index.html) (1), [The finders](../../../grc/stakeholders/finders/index.html) (1), [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) (1), [CISO](../../../grc/stakeholders/ciso/index.html) (1), [Quarkslab and OSTIF](../../../grc/stakeholders/quarkslab/index.html) (1), [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) (1)

## The standards its register touches

[ISO/IEC 27001](../../frameworks/iso27001/index.html) (5), [NIST SSDF](../../frameworks/ssdf/index.html) (5), [Cyber Resilience Act](../../frameworks/cra/index.html) (4), [NIST CSF 2.0](../../frameworks/nistcsf/index.html) (3), [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) (3), [OWASP Top 10s](../../frameworks/owasp/index.html) (2), [NIS2](../../frameworks/nis2/index.html) (2), [NIST AI RMF](../../frameworks/nistairmf/index.html) (2), [NIST SP 800-53](../../frameworks/nist80053/index.html) (1), [CIS Controls](../../frameworks/cis/index.html) (1), [MITRE ATT&CK](../../frameworks/attack/index.html) (1), [FIRST TLP 2.0](../../frameworks/tlp/index.html) (1), [EU AI Act](../../frameworks/euaiact/index.html) (1), [ISO/IEC 42001](../../frameworks/iso42001/index.html) (1)


---
site v0.21.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/php-project/index.html
