# R08: Frontier AI finds critical flaws faster than maintainers can fix them

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because four parties, several using frontier models, found the same engine flaws within weeks, and the same capability is open to attackers, the next critical bug in widely used C code may be found by someone who will not report it, resulting in flaws exploited before any embargo exists.

[Risks](../index.html) / R08

# R08: Frontier AI finds critical flaws faster than maintainers can fix them

Because four parties, several using frontier models, found the same engine flaws within weeks, and the same capability is open to attackers, the next critical bug in widely used C code may be found by someone who will not report it, resulting in flaws exploited before any embargo exists.

**Rating** **20** critical · **Likelihood** 4 Likely · **Impact** 5 Severe · **Kind** Strategic · **Acceptance** not recorded

**Basis.** AI-assisted discovery reported by the finders and by Chainguard; 'ahead of attackers' is disputed.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [OpenAI (Patch the Planet)](../../../grc/stakeholders/openai/index.html) | **owner** | A provider of a general-purpose model with systemic risk, under the EU AI Act. | 1 risk |
| [The finders](../../../grc/stakeholders/finders/index.html) | **treater** | Report what they find. | 7 risks |
| [The PHP project](../../../grc/stakeholders/php-project/index.html) | **bearer** | Receives the reports. | 11 risks |
| [Everyone with PHP in the path](../../../grc/stakeholders/world/index.html) | **bearer** | Every user of open-source C. | 34 risks |
| [CISO](../../../grc/stakeholders/ciso/index.html) | **bearer** | The next flaw may arrive with no embargo and no advisory: plans that assume a warning stop working. | 2 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R08-1 A known bug left unexploited, then unfixed, for two years](../../../grc/risks/r08-1/index.html) | **16** high | Strategic | [The PHP project](../../../grc/stakeholders/php-project/index.html) owner, [Quarkslab and OSTIF](../../../grc/stakeholders/quarkslab/index.html) informer, [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) treater | [NIST SSDF PW.7](../../../grc/frameworks/ssdf/index.html#c-pw-7), [NIST SSDF RV.2](../../../grc/frameworks/ssdf/index.html#c-rv-2), [Cyber Resilience Act Art.24](../../../grc/frameworks/cra/index.html#c-art-24), [ISO/IEC 27001 A.8.25](../../../grc/frameworks/iso27001/index.html#c-a-8-25) |
| [R08-2 Several finders, one small team](../../../grc/risks/r08-2/index.html) | **12** high | Operational | [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) bearer, [The finders](../../../grc/stakeholders/finders/index.html) source, [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) owner | [ISO/IEC 29147 and 30111 29147:receipt](../../../grc/frameworks/iso29147/index.html#c-29147-receipt), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08), [NIST SSDF RV.1](../../../grc/frameworks/ssdf/index.html#c-rv-1) |

## What it arises from
- **Frontier models that find memory-safety bugs in widely used C.** The capability that found these flaws ahead of most attackers is available to attackers too, and finds more than maintainers can fix in a week.
- **A small, thinly funded maintainer team at the base of the web.** An audit found the bug in 2024; the fix took until 2026. Four reports in a month land on the same handful of people.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiative](../../../facts/ai-found/index.html) | reported | **A3** Echoed●●●○○○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [OpenAI on X](../../../sources/x-openai-php2shell/index.html) [Calif](../../../sources/calif-php2shell/index.html) [Wiz](../../../sources/wiz-blog-php2shell/index.html) |
| [Frontier AI found the flaw ahead of attackers, giving defenders time to prepare](../../../facts/ahead-of-attackers/index.html) | disputed | **A2** Reported●●○○○○ | [OpenAI on X](../../../sources/x-openai-php2shell/index.html) [THN](../../../sources/thehackernews-php2shell-4days/index.html) |
| [Chainguard's team found the same bugs independently with an AI harness and a frontier model after a researcher warned them on the Friday before](../../../facts/lorenc-ai-found/index.html) | reported | **A2** Reported●●○○○○ | [The Register](../../../sources/theregister-php-blames-chainguard/index.html) |
| [Criminals are using AI to 'vibe code' an attack method](../../../facts/vibe-code/index.html) | unverified | **A1** Weak signal●○○○○○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| [OpenAI independently reported the same root cause on 11 August, with further vectors on 18 September](../../../facts/openai-same-day/index.html) | reported | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| [Wiz Research independently discovered the first flaw on 19 August and reported on 24 August](../../../facts/wiz-independent/index.html) | reported | **A2** Reported●●○○○○ | [Wiz](../../../sources/wiz-blog-php2shell/index.html) [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Coordinated reporting by the model providers (Patch the Planet) | partial | [Who found php2shell, and what the AI did](../../../discovery/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [EU AI Act](../../frameworks/euaiact/index.html) | [Art.55](../../frameworks/euaiact/index.html#c-art-55) | Providers of general-purpose models with systemic risk: evaluate, mitigate systemic risks, report serious incidents, protect cybersecurity | Law and regulation |
| [NIST AI RMF](../../frameworks/nistairmf/index.html) | [GOVERN-6.1](../../frameworks/nistairmf/index.html#c-govern-6-1) | Policies address AI risks from third-party entities | Frameworks and control catalogues |
| [NIST AI RMF](../../frameworks/nistairmf/index.html) | [MEASURE-2.7](../../frameworks/nistairmf/index.html#c-measure-2-7) | AI system security and resilience are evaluated and documented | Frameworks and control catalogues |
| [ISO/IEC 42001](../../frameworks/iso42001/index.html) | [6.1.2](../../frameworks/iso42001/index.html#c-6-1-2) | AI risk assessment | Management-system standards |

## The stories that tell it
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html)

On this site: [Who found php2shell, and what the AI did](../../../discovery/index.html) · [In context: php2shell against Kaminsky, Heartbleed, Shellshock, Log4Shell and the last PHP RCE](../../../context/index.html)


---
site v0.9.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r08/index.html
