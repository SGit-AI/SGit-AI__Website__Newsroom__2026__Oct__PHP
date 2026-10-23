# R10-2: A vault key or token published

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because every file in the repository is public within minutes of a push to dev, a vault key, access token or passphrase written into the tree would be published, resulting in the evidence or readers' data opened to anyone.

[Risks](../index.html) / [R10 This newsroom's own agents are steered, leak or mislead](../../../grc/risks/r10/index.html) / R10-2

# R10-2: A vault key or token published

Because every file in the repository is public within minutes of a push to dev, a vault key, access token or passphrase written into the tree would be published, resulting in the evidence or readers' data opened to anyone.

**Rating** **10** medium · **Likelihood** 2 Unlikely · **Impact** 5 Severe · **Kind** AI and agents · **Acceptance** not recorded

**Basis.** Credential shapes and vault files refused by the gate and the release tripwire.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The newsroom's agents](../../../grc/stakeholders/newsroom-agents/index.html) | **treater** | Clone outside the repository; never print a secret. | 4 risks |
| [The editor](../../../grc/stakeholders/newsroom-editor/index.html) | **owner** | Holds the root key; rotates on exposure. | 4 risks |
| [This site's readers](../../../grc/stakeholders/readers/index.html) | **bearer** | Their subscriptions and telemetry are in vaults. | 3 risks |

## What it arises from
- **Agents that read the open web and can publish.** Nine capabilities in the newsroom's agent grant have no boundary in the way (admin/security/abp/DELTA.md); the gate that guards publishing lives in the repository the agents can edit.

## The evidence

No claim on this site carries this risk: it rests on how this newsroom works, set out on the pages linked below.

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Credential-shape and vault-file checks in the gate and on the staged diff | in place | [The vaults behind this site](../../../vaults/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [LLM02:2025](../../frameworks/owasp/index.html#c-llm02-2025) | Sensitive information disclosure | Practice and technique |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.32](../../frameworks/gdpr/index.html#c-art-32) | Security of processing, including a process for regularly testing and evaluating it | Law and regulation |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.14](../../frameworks/iso27001/index.html#c-a-5-14) | Information transfer, including under agreed classification | Management-system standards |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [The vaults behind this site](../../../vaults/index.html)


---
site v0.10.12 · data as of 2026-10-23T01:20Z · vault commit f3c5db0d9873 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r10-2/index.html
