# R10: This newsroom's own agents are steered, leak or mislead

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because this newsroom's agents read captured pages, feeds and other models' output while holding vault credentials and the right to publish, text written by a stranger could steer one, a secret could be published, or a wrong status word could ship, resulting in harm to readers and to the people name

[Risks](../index.html) / R10

# R10: This newsroom's own agents are steered, leak or mislead

Because this newsroom's agents read captured pages, feeds and other models' output while holding vault credentials and the right to publish, text written by a stranger could steer one, a secret could be published, or a wrong status word could ship, resulting in harm to readers and to the people named on the site.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r10) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** AI and agents · **Acceptance** not recorded

**Basis.** Nine unbounded excess capabilities in the agent grant; eleven overstated status words found by the desk; no steering seen.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The editor](../../../grc/stakeholders/newsroom-editor/index.html) | **owner** | Sets the mandate and is the only instructing voice. | 4 risks |
| [The newsroom's agents](../../../grc/stakeholders/newsroom-agents/index.html) | **treater** | Work to the security requirements. | 4 risks |
| [This site's readers](../../../grc/stakeholders/readers/index.html) | **bearer** | Read what is published, and so do their models. | 3 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R10-1 Prompt injection through captured material](../../../grc/risks/r10-1/index.html) | **12** high | AI and agents | [The newsroom's agents](../../../grc/stakeholders/newsroom-agents/index.html) treater, [The editor](../../../grc/stakeholders/newsroom-editor/index.html) owner | [OWASP Top 10s LLM01:2025](../../../grc/frameworks/owasp/index.html#c-llm01-2025), [NIST AI RMF MEASURE-2.7](../../../grc/frameworks/nistairmf/index.html#c-measure-2-7), [EU AI Act Art.15](../../../grc/frameworks/euaiact/index.html#c-art-15) |
| [R10-3 A status word stronger than its evidence](../../../grc/risks/r10-3/index.html) | **12** high | AI and agents | [The newsroom's agents](../../../grc/stakeholders/newsroom-agents/index.html) source, [This site's readers](../../../grc/stakeholders/readers/index.html) bearer, [The editor](../../../grc/stakeholders/newsroom-editor/index.html) owner | [OWASP Top 10s LLM09:2025](../../../grc/frameworks/owasp/index.html#c-llm09-2025), [EU AI Act Art.50](../../../grc/frameworks/euaiact/index.html#c-art-50) |
| [R10-2 A vault key or token published](../../../grc/risks/r10-2/index.html) | **10** medium | AI and agents | [The newsroom's agents](../../../grc/stakeholders/newsroom-agents/index.html) treater, [The editor](../../../grc/stakeholders/newsroom-editor/index.html) owner, [This site's readers](../../../grc/stakeholders/readers/index.html) bearer | [OWASP Top 10s LLM02:2025](../../../grc/frameworks/owasp/index.html#c-llm02-2025), [GDPR Art.32](../../../grc/frameworks/gdpr/index.html#c-art-32), [ISO/IEC 27001 A.5.14](../../../grc/frameworks/iso27001/index.html#c-a-5-14) |

## What it arises from
- **Agents that read the open web and can publish.** Nine capabilities in the newsroom's agent grant have no boundary in the way (admin/security/abp/DELTA.md); the gate that guards publishing lives in the repository the agents can edit.
- **Third-party text inside the agents' context.** Captured pages, feeds, tips and other models' output are read by agents that hold credentials; one sentence addressed to a model is enough to try.
- **A status word chosen by the agent that wrote the claim.** The fact-check desk found eleven claims whose status word is stronger than their evidence.

## The evidence

No claim on this site carries this risk: it rests on how this newsroom works, set out on the pages linked below.

## Treatments

| Treatment | Status | Where |
|---|---|---|
| The security requirements, the gate and the release tripwire | in place | [How to work on this site: guidance for every agent](../../../admin/agents/index.html) |
| Rulesets on dev and main restricting the gate's own files | missing | [Admin and engineering](../../../admin/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [EU AI Act](../../frameworks/euaiact/index.html) | [Art.50](../../frameworks/euaiact/index.html#c-art-50) | Transparency: content generated by AI is disclosed as such | Law and regulation |
| [NIST AI RMF](../../frameworks/nistairmf/index.html) | [MANAGE-2.4](../../frameworks/nistairmf/index.html#c-manage-2-4) | Mechanisms exist, with assigned responsibility, to supersede, disengage or deactivate an AI system | Frameworks and control catalogues |
| [ISO/IEC 42001](../../frameworks/iso42001/index.html) | [6.1.3](../../frameworks/iso42001/index.html#c-6-1-3) | AI risk treatment | Management-system standards |
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [LLM06:2025](../../frameworks/owasp/index.html#c-llm06-2025) | Excessive agency | Practice and technique |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [How to work on this site: guidance for every agent](../../../admin/agents/index.html) · [The team: the people, the agents and how they work together](../../../team/index.html)


---
site v0.10.17 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r10/index.html
