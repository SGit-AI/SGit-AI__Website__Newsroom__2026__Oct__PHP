# R01-5: Popular applications compromised before authentication

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because pre-authentication code execution was reported against WordPress, Drupal, Joomla, MediaWiki, Magento, Nextcloud and other applications, their users are exposed whatever the application's own security, resulting in the largest share of affected sites.

[Risks](../index.html) / [R01 Remote code execution on internet-facing PHP servers](../../../grc/risks/r01/index.html) / R01-5

# R01-5: Popular applications compromised before authentication

Because pre-authentication code execution was reported against WordPress, Drupal, Joomla, MediaWiki, Magento, Nextcloud and other applications, their users are exposed whatever the application's own security, resulting in the largest share of affected sites.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r01-5) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Security · **Acceptance** not recorded

**Basis.** Reported by the finders; the applications inherit the flaw from the engine.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Open-source PHP applications](../../../grc/stakeholders/oss-apps/index.html) | **informer** | Can only tell their users to update PHP; their advisories reach the people who must act. | 1 risk |
| [Website owner](../../../grc/stakeholders/site-owner/index.html) | **owner** | Runs the application. | 2 risks |
| [Online shops and payments](../../../grc/stakeholders/commerce/index.html) | **bearer** | Magento and WooCommerce shops take cards. | 2 risks |

## What it arises from
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.
- **Request globals that survive a failed request.** State from a request that failed is still there when the next one starts.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS](../../../facts/wordpress-drupal/index.html) | reported | **A2** Reported●●○○○○ | [Calif](../../../sources/calif-php2shell/index.html) [Wiz](../../../sources/wiz-blog-php2shell/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Update PHP under the application | in place | [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [OWASP Top 10s](../../frameworks/owasp/index.html) | [A06:2021](../../frameworks/owasp/index.html#c-a06-2021) | Vulnerable and outdated components | Practice and technique |
| [PCI DSS](../../frameworks/pcidss/index.html) | [6.3.1](../../frameworks/pcidss/index.html#c-6-3-1) | Security vulnerabilities are identified, risk-ranked and managed | Management-system standards |
| [CIS Controls](../../frameworks/cis/index.html) | [16.4](../../frameworks/cis/index.html#c-16-4) | Establish and manage an inventory of third-party software components | Frameworks and control catalogues |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html) (through Remote code execution on internet-facing PHP servers)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Remote code execution on internet-facing PHP servers)

On this site: [Affected systems: versions, deployments, applications, inventory](../../../affected/index.html)


---
site v0.15.9 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r01-5/index.html
