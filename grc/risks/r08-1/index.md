# R08-1: A known bug left unexploited, then unfixed, for two years

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because a 2024 audit found the out-of-memory issue but not its exploitation, and two findings were redacted while their fixes were in progress, the bug waited until better tools showed it could be weaponised, resulting in a fix shipped under emergency instead of on the maintainers' schedule.

[Risks](../index.html) / [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../../grc/risks/r08/index.html) / R08-1

# R08-1: A known bug left unexploited, then unfixed, for two years

Because a 2024 audit found the out-of-memory issue but not its exploitation, and two findings were redacted while their fixes were in progress, the bug waited until better tools showed it could be weaponised, resulting in a fix shipped under emergency instead of on the maintainers' schedule.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r08-1) · [What the graph is missing](../../gaps/index.html)

**Rating** **16** high · **Likelihood** 4 Likely · **Impact** 4 Major · **Kind** Strategic · **Acceptance** not recorded

**Basis.** Confirmed audit; redaction reported.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The PHP project](../../../grc/stakeholders/php-project/index.html) | **owner** | Triage of audit findings. | 11 risks |
| [Quarkslab and OSTIF](../../../grc/stakeholders/quarkslab/index.html) | **informer** | The audit. | 1 risk |
| [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) | **treater** | Funds the developers who would fix it. | 3 risks |

## What it arises from
- **A small, thinly funded maintainer team at the base of the web.** An audit found the bug in 2024; the fix took until 2026. Four reports in a month land on the same handful of people.
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Agency) but exploitation was not proven, so it was not fixed](../../../facts/quarkslab-2024/index.html) | confirmed | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [Calif](../../../sources/calif-php2shell/index.html) |
| [Quarkslab's published audit summary lists 27 findings, two redacted because their fixes were complex and in progress; it does not describe an out-of-memory finding](../../../facts/quarkslab-redacted/index.html) | reported | **A6** Established●●●●●● | [Quarkslab](../../../sources/quarkslab-blog-php-src-audit/index.html) [David Lopez-Kurtz](../../../sources/substack-lopezkurtz-patch-is-the-exploit/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Publicly funded audits (OSTIF, Sovereign Tech Agency) | partial | [Who found php2shell, and what the AI did](../../../discovery/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST SSDF](../../frameworks/ssdf/index.html) | [PW.7](../../frameworks/ssdf/index.html#c-pw-7) | Review and analyse human-readable code to find vulnerabilities | Frameworks and control catalogues |
| [NIST SSDF](../../frameworks/ssdf/index.html) | [RV.2](../../frameworks/ssdf/index.html#c-rv-2) | Assess, prioritise and remediate vulnerabilities | Frameworks and control catalogues |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.24](../../frameworks/cra/index.html#c-art-24) | Obligations of open-source software stewards | Law and regulation |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.25](../../frameworks/iso27001/index.html#c-a-8-25) | Secure development life cycle | Management-system standards |

## The stories that tell it
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html)

On this site: [Who found php2shell, and what the AI did](../../../discovery/index.html)


---
site v0.14.9 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r08-1/index.html
