# R08-2: Several finders, one small team

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because Calif, OpenAI, Wiz and a fourth reporter reached the same small security team within weeks, each report costs the same few people triage time, resulting in a coordination load that grows with every AI-assisted finder.

[Risks](../index.html) / [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../../grc/risks/r08/index.html) / R08-2

# R08-2: Several finders, one small team

Because Calif, OpenAI, Wiz and a fourth reporter reached the same small security team within weeks, each report costs the same few people triage time, resulting in a coordination load that grows with every AI-assisted finder.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r08-2) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 4 Likely · **Impact** 3 Significant · **Kind** Operational · **Acceptance** not recorded

**Basis.** Four credited reporters; dates confirmed.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **bearer** | Triage for every report. | 7 risks |
| [The finders](../../../grc/stakeholders/finders/index.html) | **source** | Each report is load. | 7 risks |
| [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) | **owner** | Decides how the team is resourced. | 3 risks |

## What it arises from
- **A small, thinly funded maintainer team at the base of the web.** An audit found the bug in 2024; the fix took until 2026. Four reports in a month land on the same handful of people.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tomash-areion](../../../facts/four-reporters/index.html) | confirmed | **A6** Established●●●●●● | [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [Daubois](../../../sources/daubois-blog-php2shell-rumors/index.html) |
| [Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 August](../../../facts/who-first/index.html) | confirmed | **A3** Echoed●●●○○○ | [Calif](../../../sources/calif-php2shell/index.html) [Ryan Austin, Calif on X](../../../sources/x-lcfr-hax-hash-tweet/index.html) [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) |
| [OpenAI independently reported the same root cause on 11 August, with further vectors on 18 September](../../../facts/openai-same-day/index.html) | reported | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| [Wiz Research independently discovered the first flaw on 19 August and reported on 24 August](../../../facts/wiz-independent/index.html) | reported | **A2** Reported●●○○○○ | [Wiz](../../../sources/wiz-blog-php2shell/index.html) [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| A coalition that pooled reports for one fix | partial | [Who found php2shell, and what the AI did](../../../discovery/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) | [29147:receipt](../../frameworks/iso29147/index.html#c-29147-receipt) | Receiving vulnerability reports and acknowledging the finder | Practice and technique |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-08](../../frameworks/nistcsf/index.html#c-id-ra-08) | Processes for receiving, analysing and responding to vulnerability disclosures are established | Frameworks and control catalogues |
| [NIST SSDF](../../frameworks/ssdf/index.html) | [RV.1](../../frameworks/ssdf/index.html#c-rv-1) | Identify and confirm vulnerabilities on an ongoing basis | Frameworks and control catalogues |

## The stories that tell it
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Frontier AI finds critical flaws faster than maintainers can fix them)

On this site: [Who found php2shell, and what the AI did](../../../discovery/index.html)


---
site v0.22.8 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r08-2/index.html
