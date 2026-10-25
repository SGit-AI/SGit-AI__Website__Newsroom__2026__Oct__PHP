# R02-1: The CVE IDs and the proof-of-concept video circulated before release

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the CVE IDs circulated from an anonymous post and a proof-of-concept video was published by mistake, attackers knew the target and saw it work before any fix existed, resulting in scanning that began ahead of the release.

[Risks](../index.html) / [R02 The coordinated disclosure broke before the fix was ready](../../../grc/risks/r02/index.html) / R02-1

# R02-1: The CVE IDs and the proof-of-concept video circulated before release

Because the CVE IDs circulated from an anonymous post and a proof-of-concept video was published by mistake, attackers knew the target and saw it work before any fix existed, resulting in scanning that began ahead of the release.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r02-1) · [What the graph is missing](../../gaps/index.html)

**Rating** **20** critical · **Likelihood** 5 Happening · **Impact** 4 Major · **Kind** Disclosure process · **Acceptance** not recorded

**Basis.** Reported by the PHP Foundation and the security team's own account.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Calif](../../../grc/stakeholders/calif/index.html) | **source** | Published the video, according to the Foundation. | 1 risk |
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **owner** | Decides how the embargo responds. | 7 risks |
| [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) | **treater** | Shipped rules within hours of the leak. | 8 risks |

## What it arises from
- **One embargo shared by many parties.** Four independent finders, a coalition, early advice to critical infrastructure and image builders: every party is a place the secret can leave by.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social media with a wrong release time and a wrong CVSS score; no technical details leaked](../../../facts/leak-cve-ids/index.html) | reported | **A4** Corroborated●●●●○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../../sources/phpfoundation-blog-security-release-leak/index.html) |
| [The leak started with an anonymous Hacker News post citing a reliable source, which came down after screenshots spread; a screenshot of the 'PHP2Shell tool' credited to Calif.io and a short exploitation video also went up and came down](../../../facts/leak-hn/index.html) | reported | **A4** Corroborated●●●●○○ | [Daubois](../../../sources/daubois-blog-php2shell-rumors/index.html) |
| [watchTowr confirmed in public that the bugs were real and posted both CVE numbers before the release](../../../facts/leak-watchtowr/index.html) | reported | **A4** Corroborated●●●●○○ | [Daubois](../../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-EU](../../../sources/certeu-sa-2026-018/index.html) |
| [Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'](../../../facts/leak-video/index.html) | reported | **A3** Echoed●●●○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../../sources/phpfoundation-blog-security-release-leak/index.html) [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Calif](../../../sources/calif-php2shell/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Edge rules live before disclosure | partial | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html#edge) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) | [29147:coordination](../../frameworks/iso29147/index.html#c-29147-coordination) | Coordinating disclosure with other vendors and parties under embargo | Practice and technique |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-08](../../frameworks/nistcsf/index.html#c-id-ra-08) | Processes for receiving, analysing and responding to vulnerability disclosures are established | Frameworks and control catalogues |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through The coordinated disclosure broke before the fix was ready)

On this site: [How the coordinated disclosure broke](../../../leak/index.html)


---
site v0.18.6 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r02-1/index.html
