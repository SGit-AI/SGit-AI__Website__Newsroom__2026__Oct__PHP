# R06-1: Personal data taken from a compromised PHP application

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because PHP applications hold accounts, orders and records, code execution on one gives the attacker its database, resulting in a personal data breach the controller must assess within 72 hours.

[Risks](../index.html) / [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) / R06-1

# R06-1: Personal data taken from a compromised PHP application

Because PHP applications hold accounts, orders and records, code execution on one gives the attacker its database, resulting in a personal data breach the controller must assess within 72 hours.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r06-1) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Compliance · **Acceptance** not recorded

**Basis.** Follows from code execution; no named organisation has reported a breach through php2shell.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Data protection officer](../../../grc/stakeholders/dpo/index.html) | **owner** | Runs the breach assessment. | 2 risks |
| [People whose data is held in PHP applications](../../../grc/stakeholders/data-subjects/index.html) | **bearer** | Their data. | 2 risks |
| [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) | **treater** | Processors under Article 28 for their customers. | 2 risks |

## What it arises from
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs](../../../facts/rce-modphp/index.html) | confirmed | **A6** Established●●●●●● | [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../../sources/php-net-advisory/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Security of processing kept current, tested and evaluated | partial | [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [GDPR](../../frameworks/gdpr/index.html) | [Art.5(1)(f)](../../frameworks/gdpr/index.html#c-art-5-1-f) | Integrity and confidentiality: personal data processed with appropriate security | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.24](../../frameworks/gdpr/index.html#c-art-24) | Responsibility of the controller: measures appropriate to the risk | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.28](../../frameworks/gdpr/index.html#c-art-28) | Processors: the controller uses only processors that give sufficient guarantees | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.32](../../frameworks/gdpr/index.html#c-art-32) | Security of processing, including a process for regularly testing and evaluating it | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.33](../../frameworks/gdpr/index.html#c-art-33) | Notifying a personal data breach to the supervisory authority within 72 hours | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.34](../../frameworks/gdpr/index.html#c-art-34) | Communicating a high-risk personal data breach to the people affected | Law and regulation |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [Briefing for a data protection officer: Was personal data exposed, does this start a GDPR breach assessment or a 72-hour notification, and what do I document?](../../../briefings/dpo/index.html) · [Impact: taken offline versus compromised](../../../impact/index.html)


---
site v0.14.27 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r06-1/index.html
