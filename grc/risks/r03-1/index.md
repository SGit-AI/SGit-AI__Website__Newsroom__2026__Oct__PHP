# R03-1: Attempts before disclosure

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because an exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network, someone may have had the flaw before the leak, resulting in compromises that pre-date every advisory and every log review window.

[Risks](../index.html) / [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) / R03-1

# R03-1: Attempts before disclosure

Because an exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network, someone may have had the flaw before the leak, resulting in compromises that pre-date every advisory and every log review window.

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** One attempt reported by Amazon; Imperva saw nothing matching before disclosure.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) | **informer** | The honeypot evidence and its absence elsewhere. | 4 risks |
| [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) | **owner** | Decides how far back to look in the logs. | 6 risks |

## What it arises from
- **Exploitation that cannot yet be seen.** Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'](../../../facts/amazon-honeypot/index.html) | reported | **A2** Reported●●○○○○ | [Amazon](../../../sources/aws-security-blog-madpot/index.html) [THN](../../../sources/thehackernews-php2shell-4days/index.html) |
| [No traffic matching the php2shell exploit patterns was seen during Imperva's pre-disclosure monitoring](../../../facts/imperva-none/index.html) | reported | **A2** Reported●●○○○○ | [Imperva Threat Research](../../../sources/imperva-blog-php2shell/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Hunt back to 17 October, not to the release | partial | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html#host) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-02](../../frameworks/nistcsf/index.html#c-id-ra-02) | Threat intelligence is received from information sharing forums and sources | Frameworks and control catalogues |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.7](../../frameworks/iso27001/index.html#c-a-5-7) | Threat intelligence | Management-system standards |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [SI-4](../../frameworks/nist80053/index.html#c-si-4) | System monitoring | Frameworks and control catalogues |
| [PCI DSS](../../frameworks/pcidss/index.html) | [12.10.1](../../frameworks/pcidss/index.html#c-12-10-1) | An incident response plan exists and is ready to be activated | Management-system standards |

## The stories that tell it
- [Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit](../../../articles/exposed-is-not-exploited/index.html)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Exploitation outpaces patching)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Exploitation outpaces patching)

On this site: [Exploitation signals, in order](../../../exploitation/index.html)


---
site v0.10.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r03-1/index.html
