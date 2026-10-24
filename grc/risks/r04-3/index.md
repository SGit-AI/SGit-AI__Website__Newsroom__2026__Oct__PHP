# R04-3: The agencies' advice disagrees

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the agencies worded their offline advice differently, from 'take offline' to 'consider taking offline', and reports of allied agreement were contradicted, boards in different countries made opposite calls on the same facts, resulting in outages some did not need and exposure others did not s

[Risks](../index.html) / [R04 Services lost to precautionary shutdowns](../../../grc/risks/r04/index.html) / R04-3

# R04-3: The agencies' advice disagrees

Because the agencies worded their offline advice differently, from 'take offline' to 'consider taking offline', and reports of allied agreement were contradicted, boards in different countries made opposite calls on the same facts, resulting in outages some did not need and exposure others did not see.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r04-3) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 4 Likely · **Impact** 3 Significant · **Kind** Governance · **Acceptance** not recorded

**Basis.** The allies' joint advice is contradicted by the captures; the wording differs per agency.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Agencies and CERTs](../../../grc/stakeholders/agencies/index.html) | **source** | Wrote the advice. | 11 risks |
| [Board and executives](../../../grc/stakeholders/board/index.html) | **owner** | Reads it and decides. | 5 risks |
| [The press](../../../grc/stakeholders/media/index.html) | **informer** | Summarised it as one voice. | 6 risks |

## What it arises from
- **Numbers and ratings repeated without their source.** 70% of the Internet, CVSS 10, 30 million sites: figures that measure different things, carried from post to post until they read as fact.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| ['Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'](../../../facts/offline-ncsc/index.html) | disputed | **A2** Reported●●○○○○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [NCSC UK](../../../sources/ncsc-news-php/index.html) [CCCS](../../../sources/cccs-al26-026/index.html) |
| [The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasible](../../../facts/offline-allies/index.html) | contradicted | **A1** Weak signal●○○○○○ | [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../../sources/acsc-alert-php/index.html) [CERT-EU](../../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../../sources/jpcert-at260033/index.html) |
| [If an immediate update is not feasible, take the system offline until it can be fully mitigated](../../../facts/offline-nsa/index.html) | confirmed | **A6** Established●●●●●● | [NSA Cyber on X](../../../sources/nsa-x-2112903220209098897/index.html) [NSA](../../../sources/nsa-press-php-4630238/index.html) |
| [Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline](../../../facts/offline-cisa/index.html) | confirmed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| The agencies table, advice side by side | in place | [What sixteen agencies actually advise](../../../agencies/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.5.5](../../frameworks/iso27001/index.html#c-a-5-5) | Contact with authorities | Management-system standards |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [GV.RR-01](../../frameworks/nistcsf/index.html#c-gv-rr-01) | Leadership is responsible and accountable for cybersecurity risk | Frameworks and control catalogues |
| [NIS2](../../frameworks/nis2/index.html) | [Art.20](../../frameworks/nis2/index.html#c-art-20) | Governance: management bodies approve and oversee the risk-management measures and can be held liable | Law and regulation |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Services lost to precautionary shutdowns)

On this site: [What sixteen agencies actually advise](../../../agencies/index.html)


---
site v0.15.13 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r04-3/index.html
