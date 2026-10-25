# R06-2: Essential and financial entities miss their reporting clocks

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because NIS2 asks for an early warning within 24 hours and DORA for major-incident reports on its own schedule, an entity that cannot tell a precautionary outage from an incident may report late or not at all, resulting in a regulatory finding on top of the incident.

[Risks](../index.html) / [R06 A compromise becomes a reportable breach](../../../grc/risks/r06/index.html) / R06-2

# R06-2: Essential and financial entities miss their reporting clocks

Because NIS2 asks for an early warning within 24 hours and DORA for major-incident reports on its own schedule, an entity that cannot tell a precautionary outage from an incident may report late or not at all, resulting in a regulatory finding on top of the incident.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r06-2) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** Compliance · **Acceptance** not recorded

**Basis.** Precautionary shutdowns may themselves meet the significance tests; the evidence does not say how entities classified them.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) | **owner** | Essential entities under NIS2. | 2 risks |
| [Banks, insurers and financial entities](../../../grc/stakeholders/finance/index.html) | **owner** | Under DORA. | 1 risk |
| [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) | **regulator** | Receive the reports. | 5 risks |
| [CISO](../../../grc/stakeholders/ciso/index.html) | **treater** | Classifies the event. | 2 risks |

## What it arises from
- **Exploitation that cannot yet be seen.** Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.](../../../facts/no-confirmed-compromise/index.html) | reported | **A4** Corroborated●●●●○○ | [CISA](../../../sources/cisa-kev-json/index.html) [CISA](../../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../../sources/impress-watch-valtec/index.html) [The Verge](../../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |
| [The Dutch government took NCSC.nl offline as a precaution, with no active misuse seen yet; Dutch press reported DigiD, MijnOverheid and Overheid.nl offline too](../../../facts/nl-offline/index.html) | reported | **A4** Corroborated●●●●○○ | [Rijksoverheid / NCSC-NL](../../../sources/rijksoverheid-ncsc-php-news/index.html) [TPO.nl](../../../sources/tpo-nl-digid-offline/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Classify a precautionary shutdown against the reporting thresholds on the day | missing | [Impact: taken offline versus compromised](../../../impact/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [NIS2](../../frameworks/nis2/index.html) | [Art.23](../../frameworks/nis2/index.html#c-art-23) | Reporting significant incidents: early warning in 24 hours, notification in 72 hours, final report in a month | Law and regulation |
| [NIS2](../../frameworks/nis2/index.html) | [Art.20](../../frameworks/nis2/index.html#c-art-20) | Governance: management bodies approve and oversee the risk-management measures and can be held liable | Law and regulation |
| [DORA](../../frameworks/dora/index.html) | [Art.19](../../frameworks/dora/index.html#c-art-19) | Reporting major ICT-related incidents | Law and regulation |
| [DORA](../../frameworks/dora/index.html) | [Art.10](../../frameworks/dora/index.html#c-art-10) | Detection of anomalous activities | Law and regulation |
| [NIST SP 800-53](../../frameworks/nist80053/index.html) | [IR-6](../../frameworks/nist80053/index.html#c-ir-6) | Incident reporting | Frameworks and control catalogues |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [Impact: taken offline versus compromised](../../../impact/index.html) · [What sixteen agencies actually advise](../../../agencies/index.html)


---
site v0.22.14 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r06-2/index.html
