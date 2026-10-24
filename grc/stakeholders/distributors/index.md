# Distributors and packagers: its php2shell risk register

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The fractal risk register for Distributors and packagers: 3 risks assigned to it or arriving through its parts, the part it plays in each and who it shares them with.

[Stakeholders](../index.html) / [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) / Distributors and packagers

# Distributors and packagers: its risk register

Everyone between the PHP source and a running server: Linux distributions, container image builders, hosting panels. A fix reaches most servers through them, not from php.net.

**Kind** group · **Assigned here** 2 · **In its register** 3 · in the story as [Chainguard](../../../actors/index.html#chainguard), [Dan Lorenc, Chainguard](../../../actors/index.html#chainguard-lorenc)

## The register

Assigned here, or arriving through a part of this stakeholder. The part played is the one recorded for whoever holds the assignment.

| Risk | Rating | Kind | Part played | Controls |
|---|---|---|---|---|
| [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../../grc/risks/r01-3/index.html) | **20** critical | Security | *through* [Hosting panels and paid long-term support](../../../grc/stakeholders/panels/index.html) (treater), [Linux distributions and image builders](../../../grc/stakeholders/distros/index.html) (treater) | [NIST SP 800-53 SA-22](../../../grc/frameworks/nist80053/index.html#c-sa-22), [CIS Controls 2.2](../../../grc/frameworks/cis/index.html#c-2-2), [NIST CSF 2.0 PR.PS-02](../../../grc/frameworks/nistcsf/index.html#c-pr-ps-02), [Cyber Essentials SUM](../../../grc/frameworks/cyberessentials/index.html#c-sum) +1 |
| [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) | **20** critical | Disclosure process | **source** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIS2 Art.12](../../../grc/frameworks/nis2/index.html#c-art-12), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict) |
| [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) | **16** high | Supply chain | **owner** | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [NIST CSF 2.0 GV.SC-05](../../../grc/frameworks/nistcsf/index.html#c-gv-sc-05), [OWASP Top 10s A03:2025](../../../grc/frameworks/owasp/index.html#c-a03-2025) |

## Where its risks sit

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 | 20 [R02](../../../grc/risks/r02/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 | 16 [R02-3](../../../grc/risks/r02-3/index.html) | 20 [R01-3](../../../grc/risks/r01-3/index.html) |
| 3 Possible | 3 | 6 | 9 | 12 | 15 |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## Its parts
- [Chainguard](../../../grc/stakeholders/chainguard/index.html): 1 risks
- [Linux distributions and image builders](../../../grc/stakeholders/distros/index.html): 1 risks
- [Hosting panels and paid long-term support](../../../grc/stakeholders/panels/index.html): 1 risks

## Who it shares risks with

[The PHP security team](../../../grc/stakeholders/php-security-team/index.html) (2), [The finders](../../../grc/stakeholders/finders/index.html) (1), [Organisations running PHP](../../../grc/stakeholders/operators/index.html) (1), [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) (1), [Chainguard](../../../grc/stakeholders/chainguard/index.html) (1)

## The standards its register touches

[NIST CSF 2.0](../../frameworks/nistcsf/index.html) (3), [NIST SP 800-53](../../frameworks/nist80053/index.html) (1), [CIS Controls](../../frameworks/cis/index.html) (1), [Cyber Essentials](../../frameworks/cyberessentials/index.html) (1), [PCI DSS](../../frameworks/pcidss/index.html) (1), [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) (1), [NIS2](../../frameworks/nis2/index.html) (1), [FIRST TLP 2.0](../../frameworks/tlp/index.html) (1), [Cyber Resilience Act](../../frameworks/cra/index.html) (1), [OWASP Top 10s](../../frameworks/owasp/index.html) (1)


---
site v0.15.12 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/stakeholders/distributors/index.html
