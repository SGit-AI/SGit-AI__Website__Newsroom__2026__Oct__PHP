# R02-3: Patched builds published before the embargo lifted

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because built images containing the fix were published at 07:41 UTC on 21 October, before the release, anyone could diff them against the previous images, resulting in the fix itself becoming a map to the flaw.

[Risks](../index.html) / [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) / R02-3

# R02-3: Patched builds published before the embargo lifted

Because built images containing the fix were published at 07:41 UTC on 21 October, before the release, anyone could diff them against the previous images, resulting in the fix itself becoming a map to the flaw.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r02-3) · [What the graph is missing](../../gaps/index.html)

**Rating** **16** high · **Likelihood** 4 Likely · **Impact** 4 Major · **Kind** Supply chain · **Acceptance** not recorded

**Basis.** Disputed: the Foundation says Chainguard broke the embargo; Chainguard denies leaking.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Chainguard](../../../grc/stakeholders/chainguard/index.html) | **source** | Published the images, by the Foundation's account. | 1 risk |
| [Distributors and packagers](../../../grc/stakeholders/distributors/index.html) | **owner** | Every builder in an embargo can do the same. | 3 risks |
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **regulator** | Sets the embargo's terms. | 7 risks |

## What it arises from
- **One embargo shared by many parties.** Four independent finders, a coalition, early advice to critical infrastructure and image builders: every party is a place the secret can leave by.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built images containing the fix](../../../facts/chainguard/index.html) | disputed | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [The Register](../../../sources/theregister-php-blames-chainguard/index.html) [Feross Aboukhadijeh on X on X](../../../sources/x-feross-chainguard/index.html) |
| [Chainguard's team found the same bugs independently with an AI harness and a frontier model after a researcher warned them on the Friday before](../../../facts/lorenc-ai-found/index.html) | reported | **A2** Reported●●○○○○ | [The Register](../../../sources/theregister-php-blames-chainguard/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Embargo terms that cover built artefacts, not only advisories | missing | [How the coordinated disclosure broke](../../../leak/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) | [29147:coordination](../../frameworks/iso29147/index.html#c-29147-coordination) | Coordinating disclosure with other vendors and parties under embargo | Practice and technique |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.13](../../frameworks/cra/index.html#c-art-13) | Obligations of manufacturers, including due diligence on integrated third-party and open-source components | Law and regulation |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [GV.SC-05](../../frameworks/nistcsf/index.html#c-gv-sc-05) | Supply chain requirements are established and integrated into contracts | Frameworks and control catalogues |
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [A03:2025](../../frameworks/owasp/index.html#c-a03-2025) | Software supply chain failures | Practice and technique |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through The coordinated disclosure broke before the fix was ready)

On this site: [How the coordinated disclosure broke](../../../leak/index.html)


---
site v0.18.1 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r02-3/index.html
