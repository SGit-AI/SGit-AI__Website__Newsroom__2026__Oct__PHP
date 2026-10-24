# R01-1: Default Apache mod_php installations exploited before application code runs

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the flaw is reached over HTTP before any application code runs, every mod_php site is exposed whatever application it serves, resulting in compromise without any application weakness.

[Risks](../index.html) / [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) / R01-1

# R01-1: Default Apache mod_php installations exploited before application code runs

Because the flaw is reached over HTTP before any application code runs, every mod_php site is exposed whatever application it serves, resulting in compromise without any application weakness.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r01-1) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** Confirmed mechanism on the most common shared-hosting setup; no confirmed compromise yet.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Shared and self-service hosting](../../../grc/stakeholders/shared-hosts/index.html) | **owner** | mod_php is the shared-hosting default; the host controls the runtime. | 1 risk |
| [Website owner](../../../grc/stakeholders/site-owner/index.html) | **bearer** | Has a site on the host and no control of its PHP. | 2 risks |
| [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) | **treater** | Find and upgrade every mod_php runtime they run. | 4 risks |

## What it arises from
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs](../../../facts/rce-modphp/index.html) | confirmed | **A6** Established●●●●●● | [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../../sources/php-net-advisory/index.html) |
| [Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed request](../../../facts/fix-engine/index.html) | confirmed | **A6** Established●●●●●● | [php/php-src, read from a clone](../../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Update PHP; the configuration measures reduce exposure and do not make an installation safe | in place | [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 27001](../../frameworks/iso27001/index.html) | [A.8.8](../../frameworks/iso27001/index.html#c-a-8-8) | Management of technical vulnerabilities | Management-system standards |
| [CIS Controls](../../frameworks/cis/index.html) | [7.4](../../frameworks/cis/index.html#c-7-4) | Perform automated application patch management | Frameworks and control catalogues |
| [Cyber Essentials](../../frameworks/cyberessentials/index.html) | [SUM](../../frameworks/cyberessentials/index.html#c-sum) | Security update management: high and critical updates within 14 days of release; unsupported software removed | Frameworks and control catalogues |
| [PCI DSS](../../frameworks/pcidss/index.html) | [6.3.3](../../frameworks/pcidss/index.html#c-6-3-3) | Critical security patches are installed within one month of release | Management-system standards |

## The stories that tell it
- [Why can't every version of PHP just be patched?](../../../articles/why-not-patch-every-version/index.html)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Remote code execution on internet-facing PHP servers)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Remote code execution on internet-facing PHP servers)

On this site: [Affected systems: versions, deployments, applications, inventory](../../../affected/index.html) · [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html)


---
site v0.11.3 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01-1/index.html
