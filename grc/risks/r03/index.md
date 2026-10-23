# R03: Exploitation outpaces patching

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because probing began before disclosure and the last PHP core flaw was exploited in the wild a day after its release, attackers may reach unpatched servers faster than operators can update them, resulting in compromises in the window between release and patch.

[Risks](../index.html) / R03

# R03: Exploitation outpaces patching

Because probing began before disclosure and the last PHP core flaw was exploited in the wild a day after its release, attackers may reach unpatched servers faster than operators can update them, resulting in compromises in the window between release and patch.

**Rating** **20** critical · **Likelihood** 4 Likely · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** Probing confirmed; the 2024 precedent was exploited within a day; KEV has not listed php2shell.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **owner** | Their patch time is the window. | 26 risks |
| [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) | **informer** | Sees attempts first. | 4 risks |
| [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) | **regulator** | A KEV listing starts the federal clock. | 2 risks |
| [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) | **treater** | Watches for the shift from probing to compromise. | 6 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R03-2 Mass scanning and mutated payloads after the leak](../../../grc/risks/r03-2/index.html) | **20** critical | Security | [WAF vendors](../../../grc/stakeholders/waf-vendors/index.html) treater, [Organisations running PHP](../../../grc/stakeholders/operators/index.html) owner | [MITRE ATT&CK T1595.002](../../../grc/frameworks/attack/index.html#c-t1595-002), [NIST CSF 2.0 DE.CM-01](../../../grc/frameworks/nistcsf/index.html#c-de-cm-01), [CIS Controls 13.10](../../../grc/frameworks/cis/index.html#c-13-10) |
| [R03-1 Attempts before disclosure](../../../grc/risks/r03-1/index.html) | **15** high | Security | [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) informer, [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) owner | [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [ISO/IEC 27001 A.5.7](../../../grc/frameworks/iso27001/index.html#c-a-5-7), [NIST SP 800-53 SI-4](../../../grc/frameworks/nist80053/index.html#c-si-4), [PCI DSS 12.10.1](../../../grc/frameworks/pcidss/index.html#c-12-10-1) |
| [R03-3 Exploited in the wild without anyone being able to show it](../../../grc/risks/r03-3/index.html) | **12** high | Governance | [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) informer, [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) regulator, [Board and executives](../../../grc/stakeholders/board/index.html) owner | [CISA KEV and BOD 22-01 KEV-entry](../../../grc/frameworks/kev/index.html#c-kev-entry), [NIST CSF 2.0 ID.RA-02](../../../grc/frameworks/nistcsf/index.html#c-id-ra-02), [NIST CSF 2.0 GV.RR-01](../../../grc/frameworks/nistcsf/index.html#c-gv-rr-01) |
| [R03-4 Detections built on a proof of concept with the wrong mechanism](../../../grc/risks/r03-4/index.html) | **12** high | Security | [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) treater, [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) owner | [NIST SP 800-53 RA-5](../../../grc/frameworks/nist80053/index.html#c-ra-5), [SOC 2 CC7.1](../../../grc/frameworks/soc2/index.html#c-cc7-1), [NIST CSF 2.0 ID.RA-01](../../../grc/frameworks/nistcsf/index.html#c-id-ra-01) |

## What it arises from
- **Exploitation that cannot yet be seen.** Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Amazon and Cloudflare saw sites being probed for the flaw](../../../facts/probing/index.html) | confirmed | **A5** Confirmed●●●●●○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../../sources/aws-security-blog-madpot/index.html) |
| [An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'](../../../facts/amazon-honeypot/index.html) | reported | **A2** Reported●●○○○○ | [Amazon](../../../sources/aws-security-blog-madpot/index.html) [THN](../../../sources/thehackernews-php2shell-4days/index.html) |
| [The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days after; php2shell is not in KEV after one day](../../../facts/kev-precedent/index.html) | confirmed | **A2** Reported●●○○○○ | [CISA](../../../sources/cisa-kev-json/index.html) [CVE record](../../../sources/cve-cve-2024-4577/index.html) [Akamai Security Research](../../../sources/akamai-blog-cve-2024-4577-one-day/index.html) |
| [CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalog](../../../facts/cisa-none/index.html) | confirmed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) [CISA](../../../sources/cisa-kev-json/index.html) [CVE record](../../../sources/cve-cve-2026-109618/index.html) |
| [Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloads](../../../facts/cloudflare-traffic/index.html) | reported | **A2** Reported●●○○○○ | [Cloudflare](../../../sources/cloudflare-blog-php2shell-waf/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Patch within days, not the 14-day Cyber Essentials window | partial | [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) |
| Watch the signals ladder for the move from exposed to exploited | in place | [The second stories: exposed, attempted, exploited, and what was within reach](../../../signals/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [CISA KEV and BOD 22-01](../../frameworks/kev/index.html) | [KEV-entry](../../frameworks/kev/index.html#c-kev-entry) | A CVE enters the catalogue on reliable evidence of active exploitation | Practice and technique |
| [CISA KEV and BOD 22-01](../../frameworks/kev/index.html) | [BOD22-01](../../frameworks/kev/index.html#c-bod22-01) | Federal agencies remediate catalogued vulnerabilities by the due date set | Practice and technique |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [DE.CM-01](../../frameworks/nistcsf/index.html#c-de-cm-01) | Networks and network services are monitored to find potentially adverse events | Frameworks and control catalogues |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [SI-4](../../frameworks/nist80053/index.html#c-si-4) | System monitoring | Frameworks and control catalogues |
| [MITRE ATT&CK](../../frameworks/attack/index.html) | [T1595.002](../../frameworks/attack/index.html#c-t1595-002) | Active scanning: vulnerability scanning | Practice and technique |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.16](../../frameworks/iso27001/index.html#c-a-8-16) | Monitoring activities | Management-system standards |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.7](../../frameworks/iso27001/index.html#c-a-5-7) | Threat intelligence | Management-system standards |

## The stories that tell it
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html)
- [Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit](../../../articles/exposed-is-not-exploited/index.html)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html)

On this site: [Exploitation signals, in order](../../../exploitation/index.html) · [The second stories: exposed, attempted, exploited, and what was within reach](../../../signals/index.html)


---
site v0.10.12 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r03/index.html
