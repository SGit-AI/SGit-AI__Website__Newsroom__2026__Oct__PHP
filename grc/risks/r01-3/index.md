# R01-3: Versions the PHP project no longer fixes stay vulnerable

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because PHP 8.1 and older receive no upstream fix and the flaws may reach back to PHP 5, installations on retired versions depend on a distribution backport, paid support or an upgrade, resulting in a long tail that stays exposed for months.

[Risks](../index.html) / [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) / R01-3

# R01-3: Versions the PHP project no longer fixes stay vulnerable

Because PHP 8.1 and older receive no upstream fix and the flaws may reach back to PHP 5, installations on retired versions depend on a distribution backport, paid support or an upgrade, resulting in a long tail that stays exposed for months.

**Rating** **20** critical · **Likelihood** 4 Likely · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** Retired versions are common on shared hosting and appliances; upstream will not fix them; CISA singles out 8.1 and older.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **owner** | Chose or inherited the version. | 26 risks |
| [Hosting panels and paid long-term support](../../../grc/stakeholders/panels/index.html) | **treater** | Paid long-term support and panel vendors are the only fix route for many. | 1 risk |
| [Linux distributions and image builders](../../../grc/stakeholders/distros/index.html) | **treater** | Backport to the versions their releases ship. | 1 risk |
| [CTO](../../../grc/stakeholders/cto/index.html) | **owner** | Owns the upgrade budget and the decision to retire. | 3 risks |
| [CFO](../../../grc/stakeholders/cfo/index.html) | **bearer** | Pays for extended support or the upgrade. | 1 risk |

## What it arises from
- **PHP versions the project no longer fixes.** 8.1 and older get no upstream fix; reaching them needs a distribution backport, paid support or an upgrade.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [All PHP versions from 5 onwards are affected by at least one of the flaws](../../../facts/versions-old/index.html) | disputed | **A3** Echoed●●●○○○ | [NCSC-NL](../../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../../sources/certfr-2026-ale-014/index.html) [oss-security](../../../sources/openwall-oss-security-109619-thread/index.html) |
| [Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offline](../../../facts/offline-cisa/index.html) | confirmed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Distribution backports and paid support for retired versions | partial | [Patching: which versions get a fix, and from whom](../../../patching/index.html#models) |
| Upgrade to a supported branch | in place | [Patching: which versions get a fix, and from whom](../../../patching/index.html#why) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [SA-22](../../frameworks/nist80053/index.html#c-sa-22) | Unsupported system components | Frameworks and control catalogues |
| [CIS Controls](../../frameworks/cis/index.html) | [2.2](../../frameworks/cis/index.html#c-2-2) | Ensure authorised software is currently supported | Frameworks and control catalogues |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [PR.PS-02](../../frameworks/nistcsf/index.html#c-pr-ps-02) | Software is maintained, replaced and removed commensurate with risk | Frameworks and control catalogues |
| [Cyber Essentials](../../frameworks/cyberessentials/index.html) | [SUM](../../frameworks/cyberessentials/index.html#c-sum) | Security update management: high and critical updates within 14 days of release; unsupported software removed | Frameworks and control catalogues |
| [PCI DSS](../../frameworks/pcidss/index.html) | [6.3.3](../../frameworks/pcidss/index.html#c-6-3-3) | Critical security patches are installed within one month of release | Management-system standards |

## The stories that tell it
- [Why can't every version of PHP just be patched?](../../../articles/why-not-patch-every-version/index.html)
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Remote code execution on internet-facing PHP servers)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Remote code execution on internet-facing PHP servers)

On this site: [Patching: which versions get a fix, and from whom](../../../patching/index.html) · [The inventory, hour by hour: fixed, vulnerable, still under investigation](../../../patching/inventory/index.html)


---
site v0.8.3 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01-3/index.html
