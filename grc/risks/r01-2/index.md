# R01-2: PHP-FPM deployments wrongly treated as safe or as certainly vulnerable

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because code execution on PHP-FPM is disputed between the sources, an operator may deprioritise FPM servers or exhaust itself on them, resulting in either exposure left open or effort misplaced.

[Risks](../index.html) / [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) / R01-2

# R01-2: PHP-FPM deployments wrongly treated as safe or as certainly vulnerable

Because code execution on PHP-FPM is disputed between the sources, an operator may deprioritise FPM servers or exhaust itself on them, resulting in either exposure left open or effort misplaced.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r01-2) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** Security · **Acceptance** not recorded

**Basis.** The claim is disputed; the update is the same either way, so the risk is in the prioritisation.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) | **owner** | Makes the prioritisation call. | 6 risks |
| [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) | **treater** | Most managed platforms run FPM. | 2 risks |
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **informer** | Only the advisories can settle what was shown on FPM. | 7 risks |

## What it arises from
- **Request globals that survive a failed request.** State from a request that failed is still there when the next one starts.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Remote code execution is confirmed on PHP-FPM](../../../facts/rce-fpm/index.html) | disputed | **A6** Established●●●●●● | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-6/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Treat FPM as affected and update it on the same schedule | in place | [Affected systems: versions, deployments, applications, inventory](../../../affected/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-01](../../frameworks/nistcsf/index.html#c-id-ra-01) | Vulnerabilities in assets are identified, validated and recorded | Frameworks and control catalogues |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [6.1.2](../../frameworks/iso27001/index.html#c-6-1-2) | Information security risk assessment: identify risks and their owners | Management-system standards |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Remote code execution on internet-facing PHP servers)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Remote code execution on internet-facing PHP servers)

On this site: [Affected systems: versions, deployments, applications, inventory](../../../affected/index.html) · [Fact-check: how sure can you be of each claim](../../../factcheck/index.html)


---
site v0.17.1 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01-2/index.html
