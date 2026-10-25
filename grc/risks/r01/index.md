# R01: Remote code execution on internet-facing PHP servers

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because two flaws in the PHP engine let an unauthenticated request execute code on a default Apache mod_php setup, an attacker who reaches an unpatched server can take it over, resulting in data theft, defacement or a foothold in the network behind it.

[Risks](../index.html) / R01

# R01: Remote code execution on internet-facing PHP servers

Because two flaws in the PHP engine let an unauthenticated request execute code on a default Apache mod_php setup, an attacker who reaches an unpatched server can take it over, resulting in data theft, defacement or a foothold in the network behind it.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r01) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** Impact: unauthenticated code execution, confirmed on mod_php. Likelihood: probing confirmed, attempts reported, no confirmed compromise; attack complexity high.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **owner** | Only the organisation running the server can update it or take it offline. | 26 risks |
| [People who use PHP services](../../../grc/stakeholders/people/index.html) | **bearer** | Their data and their services are what an attacker reaches. | 5 risks |
| [The PHP project](../../../grc/stakeholders/php-project/index.html) | **treater** | Ships the fix in 8.5.12, 8.4.27, 8.3.36 and 8.2.35. | 11 risks |
| [Hosting and cloud providers](../../../grc/stakeholders/hosting/index.html) | **treater** | Patch the runtime for every customer on a managed platform. | 4 risks |
| [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) | **treater** | Filters and detection between the attacker and the server. | 8 risks |
| [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) | **informer** | Their advisories set how urgently boards act. | 11 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../../grc/risks/r01-3/index.html) | **20** critical | Security | [Organisations running PHP](../../../grc/stakeholders/operators/index.html) owner, [Hosting panels and paid long-term support](../../../grc/stakeholders/panels/index.html) treater, [Linux distributions and image builders](../../../grc/stakeholders/distros/index.html) treater, [CTO](../../../grc/stakeholders/cto/index.html) owner, [CFO](../../../grc/stakeholders/cfo/index.html) bearer | [NIST SP 800-53 SA-22](../../../grc/frameworks/nist80053/index.html#c-sa-22), [CIS Controls 2.2](../../../grc/frameworks/cis/index.html#c-2-2), [NIST CSF 2.0 PR.PS-02](../../../grc/frameworks/nistcsf/index.html#c-pr-ps-02), [Cyber Essentials SUM](../../../grc/frameworks/cyberessentials/index.html#c-sum) +1 |
| [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../../grc/risks/r01-6/index.html) | **16** high | Supply chain | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html) owner, [Organisations running PHP](../../../grc/stakeholders/operators/index.html) bearer, [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) informer, [CTO](../../../grc/stakeholders/cto/index.html) owner | [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [Cyber Resilience Act AnnexI.II](../../../grc/frameworks/cra/index.html#c-annexi-ii), [OWASP Top 10s A03:2025](../../../grc/frameworks/owasp/index.html#c-a03-2025), [NIS2 Art.21(2)(d)](../../../grc/frameworks/nis2/index.html#c-art-21-2-d) +4 |
| [R01-1 Default Apache mod_php installations exploited before application code runs](../../../grc/risks/r01-1/index.html) | **15** high | Security | [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html) owner, [Website owner](../../../grc/stakeholders/site-owner/index.html) bearer, [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) treater | [ISO/IEC 27001 A.8.8](../../../grc/frameworks/iso27001/index.html#c-a-8-8), [CIS Controls 7.4](../../../grc/frameworks/cis/index.html#c-7-4), [Cyber Essentials SUM](../../../grc/frameworks/cyberessentials/index.html#c-sum), [PCI DSS 6.3.3](../../../grc/frameworks/pcidss/index.html#c-6-3-3) |
| [R01-4 The fix is incomplete, or a third flaw follows](../../../grc/risks/r01-4/index.html) | **15** high | Security | [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html) owner, [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) treater, [Organisations running PHP](../../../grc/stakeholders/operators/index.html) bearer, [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) bearer, [The finders](../../../grc/stakeholders/finders/index.html) informer | [NIST SSDF RV.3](../../../grc/frameworks/ssdf/index.html#c-rv-3), [NIST SSDF PW.8](../../../grc/frameworks/ssdf/index.html#c-pw-8), [ISO/IEC 27001 A.8.29](../../../grc/frameworks/iso27001/index.html#c-a-8-29), [ISO/IEC 29147 and 30111 30111:handling](../../../grc/frameworks/iso29147/index.html#c-30111-handling) |
| [R01-5 Popular applications compromised before authentication](../../../grc/risks/r01-5/index.html) | **15** high | Security | [Open-source PHP applications](../../../grc/stakeholders/oss-apps/index.html) informer, [Website owner](../../../grc/stakeholders/site-owner/index.html) owner, [Online shops and payments](../../../grc/stakeholders/commerce/index.html) bearer | [OWASP Top 10s A06:2021](../../../grc/frameworks/owasp/index.html#c-a06-2021), [PCI DSS 6.3.1](../../../grc/frameworks/pcidss/index.html#c-6-3-1), [CIS Controls 16.4](../../../grc/frameworks/cis/index.html#c-16-4) |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../../grc/risks/r01-2/index.html) | **12** high | Security | [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) owner, [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) treater, [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) informer | [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01), [ISO/IEC 27001 6.1.2](../../../grc/frameworks/iso27001/index.html#c-6-1-2) |

## What it arises from
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.
- **Request globals that survive a failed request.** State from a request that failed is still there when the next one starts.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35](../../../facts/two-cves-9.2/index.html) | confirmed | **A6** Established●●●●●● | [CVE record](../../../sources/cve-cve-2026-109618/index.html) [CVE record](../../../sources/cve-cve-2026-109619/index.html) [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../../../sources/php-net-advisory/index.html) |
| [Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs](../../../facts/rce-modphp/index.html) | confirmed | **A6** Established●●●●●● | [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../../sources/php-net-advisory/index.html) |
| [Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed request](../../../facts/fix-engine/index.html) | confirmed | **A6** Established●●●●●● | [php/php-src, read from a clone](../../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| [Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity high](../../../facts/ac-high/index.html) | confirmed | **A3** Echoed●●●○○○ | [Imperva Threat Research](../../../sources/imperva-blog-php2shell/index.html) [Fastly](../../../sources/fastly-blog-php2shell/index.html) [CVE record](../../../sources/cve-cve-2026-109618/index.html) |
| [Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe](../../../facts/only-update/index.html) | confirmed | **A6** Established●●●●●● | [php.net](../../../sources/php-net-advisory/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Update to 8.5.12, 8.4.27, 8.3.36 or 8.2.35 | in place | [Patching: which versions get a fix, and from whom](../../../patching/index.html) |
| Take the system offline where an update is not possible (CISA, NSA) | in place | [Impact: taken offline versus compromised](../../../impact/index.html) |
| Edge filters while the update is rolled out | partial | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html#edge) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.8](../../frameworks/iso27001/index.html#c-a-8-8) | Management of technical vulnerabilities | Management-system standards |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-01](../../frameworks/nistcsf/index.html#c-id-ra-01) | Vulnerabilities in assets are identified, validated and recorded | Frameworks and control catalogues |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [SI-2](../../frameworks/nist80053/index.html#c-si-2) | Flaw remediation | Frameworks and control catalogues |
| [CIS Controls](../../frameworks/cis/index.html) | [7.7](../../frameworks/cis/index.html#c-7-7) | Remediate detected vulnerabilities | Frameworks and control catalogues |
| [MITRE ATT&CK](../../frameworks/attack/index.html) | [T1190](../../frameworks/attack/index.html#c-t1190) | Exploit public-facing application | Practice and technique |
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [A06:2021](../../frameworks/owasp/index.html#c-a06-2021) | Vulnerable and outdated components | Practice and technique |
| [NIS2](../../frameworks/nis2/index.html) | [Art.21(2)(e)](../../frameworks/nis2/index.html#c-art-21-2-e) | Security in acquisition, development and maintenance, including vulnerability handling and disclosure | Law and regulation |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html)

On this site: [The two flaws: CVE-2026-109618 and CVE-2026-109619](../../../flaws/index.html) · [The fix, mapped to the code](../../../review/index.html) · [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html)


---
site v0.22.14 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01/index.html
