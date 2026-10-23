# R02-2: Early mitigation advice to a few providers leaked

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because mitigation advice was given to a few critical-infrastructure providers from about 23:00 UTC on 20 October without, as far as the record shows, a sharing label that held, it may have leaked, resulting in a signal to attackers and an uneven head start among defenders.

[Risks](../index.html) / [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) / R02-2

# R02-2: Early mitigation advice to a few providers leaked

Because mitigation advice was given to a few critical-infrastructure providers from about 23:00 UTC on 20 October without, as far as the record shows, a sharing label that held, it may have leaked, resulting in a signal to attackers and an uneven head start among defenders.

**Rating** **9** medium · **Likelihood** 3 Possible · **Impact** 3 Significant · **Kind** Disclosure process · **Acceptance** not recorded

**Basis.** Reported by the Foundation as possible, not shown.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) | **source** | Received the advice. | 2 risks |
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **owner** | Chose who to tell and on what terms. | 7 risks |
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **bearer** | Most received nothing early. | 26 risks |

## What it arises from
- **One embargo shared by many parties.** Four independent finders, a coalition, early advice to critical infrastructure and image builders: every party is a place the secret can leave by.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Mitigation advice given to a few critical-infrastructure providers from about 23:00 UTC on 20 October may have leaked](../../../facts/leak-mitigations/index.html) | reported | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Share early advice under TLP:AMBER+STRICT and record who received it | missing | [How the coordinated disclosure broke](../../../leak/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [FIRST TLP 2.0](../../frameworks/tlp/index.html) | [TLP:AMBER+STRICT](../../frameworks/tlp/index.html#c-tlp-amber-strict) | Limited disclosure: recipients share only within their organisation | Practice and technique |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.14](../../frameworks/iso27001/index.html#c-a-5-14) | Information transfer, including under agreed classification | Management-system standards |
| [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) | [29147:coordination](../../frameworks/iso29147/index.html#c-29147-coordination) | Coordinating disclosure with other vendors and parties under embargo | Practice and technique |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through The coordinated disclosure broke before the fix was ready)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through The coordinated disclosure broke before the fix was ready)

On this site: [How the coordinated disclosure broke](../../../leak/index.html)


---
site v0.9.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r02-2/index.html
