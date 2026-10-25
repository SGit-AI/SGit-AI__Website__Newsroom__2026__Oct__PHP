# GRC: the risks of php2shell, who carries them, and the standards that govern them

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

34 risks in a fractal register assigned to 53 stakeholders, each joined to the weakness, vulnerability, fix, code, stories and roles behind it, and mapped to 95 controls in 20 frameworks including GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO 27001 and NIST CSF.

[GRC](../grc/index.html) · [Risks](../grc/risks/index.html) · [Stakeholders](../grc/stakeholders/index.html) · [Frameworks](../grc/frameworks/index.html) · [The graph](../grc/graph/index.html) · [Explore](../grc/explore/index.html) · [Gaps](../grc/gaps/index.html) · [Changes](../grc/changes/index.html) · [From the network](../grc/network/index.html)

# GRC: the risks of php2shell, who carries them, and the standards that govern them

A register of every risk in this story, broken down until each piece has someone who can act on it, and assigned to every stakeholder who carries part of it. The registers are fractal: the PHP project, a hosting provider, a council, a board and a developer each have one, and each is the same register read at a different scale. Every risk is backed by claims already on this site, and joined, edge by edge, to the weakness behind it, the vulnerability, the part of the fix that addresses it, the code that changed, the stories that tell it, the roles that act on it, and the controls in GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO 27001, NIST and the rest.

34risks10at the top53stakeholders10roles14weaknesses20frameworks95controls mapped1357edges

## Where the risks sit

Likelihood up, impact across; the number in each cell is the score, likelihood times impact. Click an id for the risk.

| Likelihood / impact | 1 Minor | 2 Moderate | 3 Significant | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| 5 Happening | 5 | 10 | 15 [R04-2](../grc/risks/r04-2/index.html) | 20 [R02](../grc/risks/r02/index.html) [R02-1](../grc/risks/r02-1/index.html) [R03-2](../grc/risks/r03-2/index.html) [R04](../grc/risks/r04/index.html) [R04-1](../grc/risks/r04-1/index.html) | 25 |
| 4 Likely | 4 | 8 | 12 [R04-3](../grc/risks/r04-3/index.html) [R07](../grc/risks/r07/index.html) [R08-2](../grc/risks/r08-2/index.html) [R10-3](../grc/risks/r10-3/index.html) | 16 [R01-6](../grc/risks/r01-6/index.html) [R02-3](../grc/risks/r02-3/index.html) [R05](../grc/risks/r05/index.html) [R08-1](../grc/risks/r08-1/index.html) [R09](../grc/risks/r09/index.html) | 20 [R01-3](../grc/risks/r01-3/index.html) [R03](../grc/risks/r03/index.html) [R08](../grc/risks/r08/index.html) |
| 3 Possible | 3 | 6 | 9 [R02-2](../grc/risks/r02-2/index.html) | 12 [R01-2](../grc/risks/r01-2/index.html) [R03-3](../grc/risks/r03-3/index.html) [R03-4](../grc/risks/r03-4/index.html) [R06-2](../grc/risks/r06-2/index.html) [R06-3](../grc/risks/r06-3/index.html) [R10](../grc/risks/r10/index.html) [R10-1](../grc/risks/r10-1/index.html) | 15 [R01](../grc/risks/r01/index.html) [R01-1](../grc/risks/r01-1/index.html) [R01-4](../grc/risks/r01-4/index.html) [R01-5](../grc/risks/r01-5/index.html) [R03-1](../grc/risks/r03-1/index.html) [R06](../grc/risks/r06/index.html) [R06-1](../grc/risks/r06-1/index.html) |
| 2 Unlikely | 2 | 4 | 6 | 8 | 10 [R10-2](../grc/risks/r10-2/index.html) |
| 1 Rare | 1 | 2 | 3 | 4 | 5 |

## The ten risks at the top

Each breaks down into the narrower risks it is made of; the full register is on the risks page.

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R02 The coordinated disclosure broke before the fix was ready](../grc/risks/r02/index.html) | **20** critical | Disclosure process | [The PHP security team](../grc/stakeholders/php-security-team/index.html) owner, [The finders](../grc/stakeholders/finders/index.html) source, [Distributors and packagers](../grc/stakeholders/distributors/index.html) source, [Organisations running PHP](../grc/stakeholders/operators/index.html) bearer, [Security lead and AppSec](../grc/stakeholders/security-lead/index.html) bearer | [ISO/IEC 29147 and 30111 29147:coordination](../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIS2 Art.12](../grc/frameworks/nis2/index.html#c-art-12), [NIST CSF 2.0 ID.RA-08](../grc/frameworks/nistcsf/index.html#c-id-ra-08), [FIRST TLP 2.0 TLP:AMBER+STRICT](../grc/frameworks/tlp/index.html#c-tlp-amber-strict) |
| [R03 Exploitation outpaces patching](../grc/risks/r03/index.html) | **20** critical | Security | [Organisations running PHP](../grc/stakeholders/operators/index.html) owner, [Threat intelligence and detection](../grc/stakeholders/threat-intel/index.html) informer, [US: CISA and the NSA](../grc/stakeholders/us-agencies/index.html) regulator, [Security lead and AppSec](../grc/stakeholders/security-lead/index.html) treater | [CISA KEV and BOD 22-01 KEV-entry](../grc/frameworks/kev/index.html#c-kev-entry), [CISA KEV and BOD 22-01 BOD22-01](../grc/frameworks/kev/index.html#c-bod22-01), [NIST CSF 2.0 DE.CM-01](../grc/frameworks/nistcsf/index.html#c-de-cm-01), [NIST SP 800-53 SI-4](../grc/frameworks/nist80053/index.html#c-si-4) +3 |
| [R04 Services lost to precautionary shutdowns](../grc/risks/r04/index.html) | **20** critical | Operational | [Governments and public services](../grc/stakeholders/public-sector/index.html) owner, [People who need a service that went offline](../grc/stakeholders/service-users/index.html) bearer, [Agencies and CERTs](../grc/stakeholders/agencies/index.html) source, [Board and executives](../grc/stakeholders/board/index.html) owner, [Communications team](../grc/stakeholders/comms/index.html) treater | [ISO/IEC 27001 A.5.29](../grc/frameworks/iso27001/index.html#c-a-5-29), [ISO/IEC 27001 A.5.30](../grc/frameworks/iso27001/index.html#c-a-5-30), [NIS2 Art.21(2)(c)](../grc/frameworks/nis2/index.html#c-art-21-2-c), [DORA Art.11](../grc/frameworks/dora/index.html#c-art-11) +2 |
| [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../grc/risks/r08/index.html) | **20** critical | Strategic | [OpenAI (Patch the Planet)](../grc/stakeholders/openai/index.html) owner, [The finders](../grc/stakeholders/finders/index.html) treater, [The PHP project](../grc/stakeholders/php-project/index.html) bearer, [Everyone with PHP in the path](../grc/stakeholders/world/index.html) bearer, [CISO](../grc/stakeholders/ciso/index.html) bearer | [EU AI Act Art.55](../grc/frameworks/euaiact/index.html#c-art-55), [NIST AI RMF GOVERN-6.1](../grc/frameworks/nistairmf/index.html#c-govern-6-1), [NIST AI RMF MEASURE-2.7](../grc/frameworks/nistairmf/index.html#c-measure-2-7), [ISO/IEC 42001 6.1.2](../grc/frameworks/iso42001/index.html#c-6-1-2) |
| [R05 A web application firewall taken for a patch](../grc/risks/r05/index.html) | **16** high | Security | [WAF vendors](../grc/stakeholders/waf-vendors/index.html) informer, [Security lead and AppSec](../grc/stakeholders/security-lead/index.html) owner, [Online shops and payments](../grc/stakeholders/commerce/index.html) bearer | [PCI DSS 6.4.2](../grc/frameworks/pcidss/index.html#c-6-4-2), [CIS Controls 13.10](../grc/frameworks/cis/index.html#c-13-10), [NIST SP 800-53 SC-7](../grc/frameworks/nist80053/index.html#c-sc-7), [ISO/IEC 27001 A.8.20](../grc/frameworks/iso27001/index.html#c-a-8-20) +1 |
| [R09 Not knowing where PHP runs](../grc/risks/r09/index.html) | **16** high | Operational | [CTO](../grc/stakeholders/cto/index.html) owner, [Platform engineers and developers](../grc/stakeholders/engineers/index.html) treater, [Suppliers in the NCSC-NL inventory](../grc/stakeholders/inventory-suppliers/index.html) informer | [NIST CSF 2.0 ID.AM-02](../grc/frameworks/nistcsf/index.html#c-id-am-02), [NIST SP 800-53 CM-8](../grc/frameworks/nist80053/index.html#c-cm-8), [CIS Controls 16.4](../grc/frameworks/cis/index.html#c-16-4), [DORA Art.8](../grc/frameworks/dora/index.html#c-art-8) +2 |
| [R01 Remote code execution on internet-facing PHP servers](../grc/risks/r01/index.html) | **15** high | Security | [Organisations running PHP](../grc/stakeholders/operators/index.html) owner, [People who use PHP services](../grc/stakeholders/people/index.html) bearer, [The PHP project](../grc/stakeholders/php-project/index.html) treater, [Hosting and cloud providers](../grc/stakeholders/hosting/index.html) treater, [Edge, WAF and detection vendors](../grc/stakeholders/edge/index.html) treater, [Agencies and CERTs](../grc/stakeholders/agencies/index.html) informer | [ISO/IEC 27001 A.8.8](../grc/frameworks/iso27001/index.html#c-a-8-8), [NIST CSF 2.0 ID.RA-01](../grc/frameworks/nistcsf/index.html#c-id-ra-01), [NIST SP 800-53 SI-2](../grc/frameworks/nist80053/index.html#c-si-2), [CIS Controls 7.7](../grc/frameworks/cis/index.html#c-7-7) +3 |
| [R06 A compromise becomes a reportable breach](../grc/risks/r06/index.html) | **15** high | Compliance | [Organisations running PHP](../grc/stakeholders/operators/index.html) owner, [Data protection officer](../grc/stakeholders/dpo/index.html) owner, [People whose data is held in PHP applications](../grc/stakeholders/data-subjects/index.html) bearer, [EU and member-state CERTs](../grc/stakeholders/eu-agencies/index.html) regulator, [Board and executives](../grc/stakeholders/board/index.html) owner | [GDPR Art.32](../grc/frameworks/gdpr/index.html#c-art-32), [GDPR Art.33](../grc/frameworks/gdpr/index.html#c-art-33), [GDPR Art.34](../grc/frameworks/gdpr/index.html#c-art-34), [NIS2 Art.23](../grc/frameworks/nis2/index.html#c-art-23) +2 |
| [R07 Decisions made on numbers that measure something else](../grc/risks/r07/index.html) | **12** high | Governance | [The press](../grc/stakeholders/media/index.html) source, [Wiz Research](../grc/stakeholders/wiz/index.html) source, [Board and executives](../grc/stakeholders/board/index.html) owner, [This newsroom](../grc/stakeholders/newsroom/index.html) treater | [NIST CSF 2.0 GV.RM-01](../grc/frameworks/nistcsf/index.html#c-gv-rm-01), [ISO/IEC 27001 6.1.2](../grc/frameworks/iso27001/index.html#c-6-1-2), [OWASP Top 10s LLM09:2025](../grc/frameworks/owasp/index.html#c-llm09-2025) |
| [R10 This newsroom's own agents are steered, leak or mislead](../grc/risks/r10/index.html) | **12** high | AI and agents | [The editor](../grc/stakeholders/newsroom-editor/index.html) owner, [The newsroom's agents](../grc/stakeholders/newsroom-agents/index.html) treater, [This site's readers](../grc/stakeholders/readers/index.html) bearer | [EU AI Act Art.50](../grc/frameworks/euaiact/index.html#c-art-50), [NIST AI RMF MANAGE-2.4](../grc/frameworks/nistairmf/index.html#c-manage-2-4), [ISO/IEC 42001 6.1.3](../grc/frameworks/iso42001/index.html#c-6-1-3), [OWASP Top 10s LLM06:2025](../grc/frameworks/owasp/index.html#c-llm06-2025) |

## From a risk to the code, the story and the role

The editor's test for this section: a path in the graph from every risk to the vulnerabilities, the code, the stories and the roles. The build walks it for every risk and the table below is the count; the gaps are listed by name, not hidden. A risk with no vulnerability is not a gap in itself: some risks here arise from how disclosure, regulation or this newsroom works, and their weaknesses point at the code in this repository that guards them instead.

| Every risk reaches | Risks that do | Risks that do not yet |
|---|---|---|
| a vulnerability | 30 of 34 | [R10 This newsroom's own agents are steered, leak or mislead](../grc/risks/r10/index.html), [R10-1 Prompt injection through captured material](../grc/risks/r10-1/index.html), [R10-2 A vault key or token published](../grc/risks/r10-2/index.html), [R10-3 A status word stronger than its evidence](../grc/risks/r10-3/index.html) |
| code | 34 of 34 | none |
| a story | 26 of 34 | [R06 A compromise becomes a reportable breach](../grc/risks/r06/index.html), [R06-1 Personal data taken from a compromised PHP application](../grc/risks/r06-1/index.html), [R06-2 Essential and financial entities miss their reporting clocks](../grc/risks/r06-2/index.html), [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../grc/risks/r06-3/index.html), [R10 This newsroom's own agents are steered, leak or mislead](../grc/risks/r10/index.html), [R10-1 Prompt injection through captured material](../grc/risks/r10-1/index.html), [R10-2 A vault key or token published](../grc/risks/r10-2/index.html), [R10-3 A status word stronger than its evidence](../grc/risks/r10-3/index.html) |
| a role inside an organisation | 34 of 34 | none |
| a member of this team | 34 of 34 | none |

## How the registers work
- **A stakeholder is a node in a tree.** A sector holds organisations, an organisation holds roles. The same register is read at every level: a stakeholder's register is what is assigned to it plus everything that arrives through the parts below it.
- **A risk is a node in a tree.** A broad risk holds the narrower risks it is made of, until each can be owned.
- **One risk, many stakeholders.** Each assignment says the part played: owner, bearer, treater, source, informer or regulator. Two stakeholders that share a risk are connected; the stakeholders page shows by how much.
- **Every edge is a verb with a named inverse**, following the [sgit graph grammar](https://graphs.sgit.ai/v1/grammar/edge-set.html): a risk *arises from* a weakness, which *gives rise to* it; a risk is *owned by* a stakeholder, who *owns* it.
- **A rating is a judgement.** Likelihood and impact on a scale of 1 to 5, each with its basis in a sentence, as at the vault's last capture.

No risk on this register is **accepted**. An acceptance is an act by the holder of a risk, for a stated interval, and nobody can accept on anyone else's behalf; this desk records risks and their holders, it does not accept for them. Until a holder accepts, funds or fixes, each risk stands as it is rated here.

|  | Likelihood | Impact |
|---|---|---|
| 1 | **Rare**: Not seen and needs conditions nobody has shown | **Minor**: An inconvenience, absorbed without a decision |
| 2 | **Unlikely**: Possible; no sign of it in the evidence yet | **Moderate**: Costs time or money; one team's problem |
| 3 | **Possible**: Reported or attempted; not confirmed at scale | **Significant**: A service degraded or an obligation triggered; a director decides |
| 4 | **Likely**: Under way somewhere, by confirmed evidence, or the precedent says it will be within weeks | **Major**: A service down, a regulator involved, data at risk; the board decides |
| 5 | **Happening**: Confirmed and under way now | **Severe**: Code execution or data loss at scale, or harm to people relying on the service |

| Part | Means | Edge |
|---|---|---|
| **Owner** | Accountable for treating the risk: decides, funds, signs off | `owned_by` / `owns` |
| **Bearer** | Suffers the consequence if it happens, whether or not it can act | `borne_by` / `bears` |
| **Treater** | Does the work that reduces it: patches, filters, detects, ships | `treated_by` / `treats` |
| **Source** | Its actions or omissions create or raise the risk, without intent | `raised_by` / `raises` |
| **Informer** | Its information changes how others see and rate the risk | `informed_by` / `informs` |
| **Regulator** | Sets or enforces the obligation the risk triggers | `regulated_by` / `regulates` |

## The data

Authored: [data/grc.json](../data/grc.json) (53 stakeholders, 14 weaknesses, 34 risks) and [data/grc-frameworks.json](../data/grc-frameworks.json) (20 frameworks, 120 controls). Generated on every build: [data/grc-graph.json](../data/grc-graph.json), 727 nodes and 1357 edges. The build refuses a risk that points at a claim, source, story, page, member, code node or control that does not exist, and a risk with no owner. Kept by [the GRC desk](../team/grc/index.html).


---
site v0.21.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/index.html
