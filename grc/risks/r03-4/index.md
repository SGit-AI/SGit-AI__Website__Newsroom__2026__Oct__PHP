# R03-4: Detections built on a proof of concept with the wrong mechanism

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because none of the public proof-of-concept exploits reviewed had the correct mechanism, rules and scans built from them may pass a vulnerable server or miss a real attack, resulting in false assurance.

[Risks](../index.html) / [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) / R03-4

# R03-4: Detections built on a proof of concept with the wrong mechanism

Because none of the public proof-of-concept exploits reviewed had the correct mechanism, rules and scans built from them may pass a vulnerable server or miss a real attack, resulting in false assurance.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r03-4) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** Security · **Acceptance** not recorded

**Basis.** Reported by VulnCheck and Huntress; community authors corrected the leaked PoC's preconditions.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) | **treater** | Write and correct the detection rules. | 4 risks |
| [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) | **owner** | Relies on the rules and decides whether to trust a scan. | 6 risks |

## What it arises from
- **Exploitation that cannot yet be seen.** Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.
- **A filter in front of an unpatched engine.** Rules match the payload shapes seen so far; attackers mutate payloads, and only traffic routed through the filter is covered.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200](../../../facts/pocs-wrong/index.html) | reported | **A1** Weak signal●○○○○○ | [rjmendez, GitHub](../../../sources/github-rjmendez-phpup-2026/index.html) [Huntress](../../../sources/huntress-php2shell-rapid-response/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Check versions, not scanner verdicts | in place | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html#hard) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [RA-5](../../frameworks/nist80053/index.html#c-ra-5) | Vulnerability monitoring and scanning | Frameworks and control catalogues |
| [SOC 2](../../frameworks/soc2/index.html) | [CC7.1](../../frameworks/soc2/index.html#c-cc7-1) | Detection and monitoring procedures identify new vulnerabilities and configuration changes | Frameworks and control catalogues |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-01](../../frameworks/nistcsf/index.html#c-id-ra-01) | Vulnerabilities in assets are identified, validated and recorded | Frameworks and control catalogues |

## The stories that tell it
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html)
- [Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit](../../../articles/exposed-is-not-exploited/index.html) (through Exploitation outpaces patching)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Exploitation outpaces patching)

On this site: [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html)


---
site v0.15.14 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r03-4/index.html
