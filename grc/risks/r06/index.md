# R06: A compromise becomes a reportable breach

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because a server running an attacker's code exposes the personal data and the services behind it, a single compromise can trigger breach notification under GDPR, incident reporting under NIS2 and DORA, and, for a manufacturer, reporting under the Cyber Resilience Act, resulting in deadlines measured

[Risks](../index.html) / R06

# R06: A compromise becomes a reportable breach

Because a server running an attacker's code exposes the personal data and the services behind it, a single compromise can trigger breach notification under GDPR, incident reporting under NIS2 and DORA, and, for a manufacturer, reporting under the Cyber Resilience Act, resulting in deadlines measured in hours and fines measured in turnover.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r06) · [What the graph is missing](../../gaps/index.html)

**Rating** **15** high · **Likelihood** 3 Possible · **Impact** 5 Severe · **Kind** Compliance · **Acceptance** not recorded

**Basis.** No named organisation has said it was compromised; two vendors report successful exploitation without naming a victim. If one comes, the clocks are 24 and 72 hours.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **owner** | Controllers and essential entities. | 26 risks |
| [Data protection officer](../../../grc/stakeholders/dpo/index.html) | **owner** | Decides whether the 72-hour clock has started. | 2 risks |
| [People whose data is held in PHP applications](../../../grc/stakeholders/data-subjects/index.html) | **bearer** | Their data. | 2 risks |
| [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) | **regulator** | Receive the reports. | 5 risks |
| [Board and executives](../../../grc/stakeholders/board/index.html) | **owner** | Personally accountable under NIS2. | 5 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R06-1 Personal data taken from a compromised PHP application](../../../grc/risks/r06-1/index.html) | **15** high | Compliance | [Data protection officer](../../../grc/stakeholders/dpo/index.html) owner, [People whose data is held in PHP applications](../../../grc/stakeholders/data-subjects/index.html) bearer, [Managed PHP platforms](../../../grc/stakeholders/managed-hosts/index.html) treater | [GDPR Art.5(1)(f)](../../../grc/frameworks/gdpr/index.html#c-art-5-1-f), [GDPR Art.24](../../../grc/frameworks/gdpr/index.html#c-art-24), [GDPR Art.28](../../../grc/frameworks/gdpr/index.html#c-art-28), [GDPR Art.32](../../../grc/frameworks/gdpr/index.html#c-art-32) +2 |
| [R06-2 Essential and financial entities miss their reporting clocks](../../../grc/risks/r06-2/index.html) | **12** high | Compliance | [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) owner, [Banks, insurers and financial entities](../../../grc/stakeholders/finance/index.html) owner, [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) regulator, [CISO](../../../grc/stakeholders/ciso/index.html) treater | [NIS2 Art.23](../../../grc/frameworks/nis2/index.html#c-art-23), [NIS2 Art.20](../../../grc/frameworks/nis2/index.html#c-art-20), [DORA Art.19](../../../grc/frameworks/dora/index.html#c-art-19), [DORA Art.10](../../../grc/frameworks/dora/index.html#c-art-10) +1 |
| [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../../grc/risks/r06-3/index.html) | **12** high | Compliance | [Suppliers in the NCSC-NL inventory](../../../grc/stakeholders/inventory-suppliers/index.html) owner, [The PHP Foundation](../../../grc/stakeholders/php-foundation/index.html) informer, [EU and member-state CERTs](../../../grc/stakeholders/eu-agencies/index.html) regulator, [Platform engineers and developers](../../../grc/stakeholders/engineers/index.html) treater | [Cyber Resilience Act Art.14](../../../grc/frameworks/cra/index.html#c-art-14), [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [Cyber Resilience Act Art.24](../../../grc/frameworks/cra/index.html#c-art-24), [Cyber Resilience Act AnnexI.II](../../../grc/frameworks/cra/index.html#c-annexi-ii) |

## What it arises from
- **The allocator's longjmp-based bailout on out-of-memory.** An out-of-memory error unwinds by longjmp and can leave request memory in a state that cleanup later reads.
- **Request globals that survive a failed request.** State from a request that failed is still there when the next one starts.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [As of 08:37 UTC on 24 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.](../../../facts/no-confirmed-compromise/index.html) | reported | **A4** Corroborated●●●●○○ | [CISA](../../../sources/cisa-kev-json/index.html) [CISA](../../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../../sources/impress-watch-valtec/index.html) [The Verge](../../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) |
| [Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs](../../../facts/rce-modphp/index.html) | confirmed | **A6** Established●●●●●● | [PHP](../../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../../sources/php-net-advisory/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| A breach-assessment step in the incident plan, started at the first sign of compromise | partial | [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [GDPR](../../frameworks/gdpr/index.html) | [Art.32](../../frameworks/gdpr/index.html#c-art-32) | Security of processing, including a process for regularly testing and evaluating it | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.33](../../frameworks/gdpr/index.html#c-art-33) | Notifying a personal data breach to the supervisory authority within 72 hours | Law and regulation |
| [GDPR](../../frameworks/gdpr/index.html) | [Art.34](../../frameworks/gdpr/index.html#c-art-34) | Communicating a high-risk personal data breach to the people affected | Law and regulation |
| [NIS2](../../frameworks/nis2/index.html) | [Art.23](../../frameworks/nis2/index.html#c-art-23) | Reporting significant incidents: early warning in 24 hours, notification in 72 hours, final report in a month | Law and regulation |
| [DORA](../../frameworks/dora/index.html) | [Art.19](../../frameworks/dora/index.html#c-art-19) | Reporting major ICT-related incidents | Law and regulation |
| [Cyber Resilience Act](../../frameworks/cra/index.html) | [Art.14](../../frameworks/cra/index.html#c-art-14) | Reporting an actively exploited vulnerability: early warning within 24 hours to the CSIRT and ENISA | Law and regulation |

## The stories that tell it
- No story on this site tells this risk yet.

On this site: [No named organisation has said it was compromised through php2shell: the evidence](../../../compromise/index.html) · [Impact: taken offline versus compromised](../../../impact/index.html) · [If you run PHP: the steps, in order, with their sources](../../../playbook/index.html)


---
site v0.15.3 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r06/index.html
