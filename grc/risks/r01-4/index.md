# R01-4: The fix is incomplete, or a third flaw follows

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the bailout mechanism is a class of bug and the 8.5.12 fix may be incomplete, a patched server may still be reachable by another path, resulting in a second emergency on systems already declared done.

[Risks](../index.html) / [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) / R01-4

# R01-4: The fix is incomplete, or a third flaw follows

Because the bailout mechanism is a class of bug and the 8.5.12 fix may be incomplete, a patched server may still be reachable by another path, resulting in a second emergency on systems already declared done.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r01-4) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** Reported by Fastly and in the oss-security thread; unverified as to a specific third bug.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The fix authors](../../../grc/stakeholders/php-fix-authors/index.html) | **owner** | Own the design of the fix and its completeness. | 1 risk |
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **treater** | Receives and coordinates the next report. | 7 risks |
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **bearer** | Will patch again. | 26 risks |
| [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) | **bearer** | Rebuild and redeploy a second time, on systems already signed off. | 4 risks |
| [The finders](../../../grc/stakeholders/finders/index.html) | **informer** | Already looking at the same code with the same tools. | 7 risks |

## What it arises from
- **Bailout as a class of bug.** Patching the demonstrated paths does not make the mechanism safe: other paths to the same bailout should be expected.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [The 8.5.12 fix may be incomplete, or there is a third, different bug](../../../facts/fix-incomplete/index.html) | unverified | **A1** Weak signal●○○○○○ | [oss-security](../../../sources/openwall-oss-security-109619-thread/index.html) |
| [Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expected](../../../facts/more-paths/index.html) | reported | **A2** Reported●●○○○○ | [Fastly](../../../sources/fastly-blog-php2shell/index.html) [oss-security](../../../sources/openwall-oss-security-109619-thread/index.html) |
| [The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout'](../../../facts/fix-bailout/index.html) | confirmed | **A6** Established●●●●●● | [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../../sources/php-net-changelog-8/index.html) [php-src](../../../sources/github-php-src-branch-7.4-backport/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| The fix replaces the longjmp bailout with a delayed soft limit and a clean hard exit | partial | [The fix, mapped to the code](../../../review/index.html#remediation) |
| Keep detection and filters after patching | partial | [Detection and defence: what blocks php2shell and what shows it](../../../defence/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST SSDF](../../frameworks/ssdf/index.html) | [RV.3](../../frameworks/ssdf/index.html#c-rv-3) | Analyse vulnerabilities to identify their root causes | Frameworks and control catalogues |
| [NIST SSDF](../../frameworks/ssdf/index.html) | [PW.8](../../frameworks/ssdf/index.html#c-pw-8) | Test executable code to find vulnerabilities | Frameworks and control catalogues |
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.29](../../frameworks/iso27001/index.html#c-a-8-29) | Security testing in development and acceptance | Management-system standards |
| [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) | [30111:handling](../../frameworks/iso29147/index.html#c-30111-handling) | Investigating, remediating and releasing the fix, and learning from it | Practice and technique |

## The stories that tell it
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Remote code execution on internet-facing PHP servers)

On this site: [The fix, mapped to the code](../../../review/index.html) · [The code: where php2shell lives and what the fix does](../../../code/index.html)


---
site v0.14.15 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01-4/index.html
