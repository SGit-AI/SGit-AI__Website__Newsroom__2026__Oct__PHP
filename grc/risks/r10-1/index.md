# R10-1: Prompt injection through captured material

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because captures, tips and feeds are written by anyone and read by agents that hold credentials, an instruction hidden in one could be followed, resulting in a push, a sent message or a deleted vault nobody asked for.

[Risks](../index.html) / [R10 This newsroom's own agents are steered, leak or mislead](../../../grc/risks/r10/index.html) / R10-1

# R10-1: Prompt injection through captured material

Because captures, tips and feeds are written by anyone and read by agents that hold credentials, an instruction hidden in one could be followed, resulting in a push, a sent message or a deleted vault nobody asked for.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r10-1) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** AI and agents · **Acceptance** not recorded

**Basis.** Material is untrusted by rule; the gate refuses text addressed to a model; nothing seen yet.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The newsroom's agents](../../../grc/stakeholders/newsroom-agents/index.html) | **treater** | Read material as material. | 4 risks |
| [The editor](../../../grc/stakeholders/newsroom-editor/index.html) | **owner** | Confirms anything that changes credentials or targets. | 4 risks |

## What it arises from
- **Third-party text inside the agents' context.** Captured pages, feeds, tips and other models' output are read by agents that hold credentials; one sentence addressed to a model is enough to try.

## The evidence

No claim on this site carries this risk: it rests on how this newsroom works, set out on the pages linked below.

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Untrusted input fenced, flagged and never followed; the gate's injection check | in place | [How to work on this site: guidance for every agent](../../../admin/agents/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [LLM01:2025](../../frameworks/owasp/index.html#c-llm01-2025) | Prompt injection | Practice and technique |
| [NIST AI RMF](../../frameworks/nistairmf/index.html) | [MEASURE-2.7](../../frameworks/nistairmf/index.html#c-measure-2-7) | AI system security and resilience are evaluated and documented | Frameworks and control catalogues |
| [EU AI Act](../../frameworks/euaiact/index.html) | [Art.15](../../frameworks/euaiact/index.html#c-art-15) | Accuracy, robustness and cybersecurity of high-risk AI systems | Law and regulation |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [How to work on this site: guidance for every agent](../../../admin/agents/index.html)


---
site v0.15.10 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r10-1/index.html
