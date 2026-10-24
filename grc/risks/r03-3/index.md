# R03-3: Exploited in the wild without anyone being able to show it

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because one firm lists the flaws as exploited in the wild, CISA has not observed exploitation and no organisation has confirmed a compromise, the signal that would move boards and regulators is missing, resulting in decisions made on the absence of evidence.

[Risks](../index.html) / [R03 Exploitation outpaces patching](../../../grc/risks/r03/index.html) / R03-3

# R03-3: Exploited in the wild without anyone being able to show it

Because one firm lists the flaws as exploited in the wild, CISA has not observed exploitation and no organisation has confirmed a compromise, the signal that would move boards and regulators is missing, resulting in decisions made on the absence of evidence.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r03-3) · [What the graph is missing](../../gaps/index.html)

**Rating** **12** high · **Likelihood** 3 Possible · **Impact** 4 Major · **Kind** Governance · **Acceptance** not recorded

**Basis.** watchTowr's listing is unverified; KEV and Huntress show nothing; the precedent says exploitation follows.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [Threat intelligence and detection](../../../grc/stakeholders/threat-intel/index.html) | **informer** | Their reports disagree. | 4 risks |
| [US: CISA and the NSA](../../../grc/stakeholders/us-agencies/index.html) | **regulator** | KEV is the public test. | 2 risks |
| [Board and executives](../../../grc/stakeholders/board/index.html) | **owner** | Decides on what the evidence does and does not show. | 5 risks |

## What it arises from
- **Exploitation that cannot yet be seen.** Honeypots and edge networks see attempts; nobody has shown a compromise, and KEV waits for one. Absence of evidence is read as safety.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild](../../../facts/watchtowr-itw/index.html) | unverified | **A4** Corroborated●●●●○○ | [watchTowr](../../../sources/watchtowr-php2shell/index.html) [watchTowr](../../../sources/watchtowr-php2shell-faq/index.html) |
| [CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalog](../../../facts/cisa-none/index.html) | confirmed | **A6** Established●●●●●● | [CISA](../../../sources/cisa-alert-php-20261021/index.html) [CISA](../../../sources/cisa-kev-json/index.html) [CVE record](../../../sources/cve-cve-2026-109618/index.html) |
| [No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no public exploit code known to Huntress](../../../facts/huntress-none/index.html) | reported | **A2** Reported●●○○○○ | [Huntress](../../../sources/huntress-php2shell-rapid-response/index.html) |
| [As of 08:37 UTC on 24 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.](../../../facts/no-confirmed-compromise/index.html) | reported | **A4** Corroborated●●●●○○ | [CISA](../../../sources/cisa-kev-json/index.html) [CISA](../../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../../sources/impress-watch-valtec/index.html) [The Verge](../../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) |
| [Reports of active exploitation exist](../../../facts/nz-active/index.html) | reported | **A2** Reported●●○○○○ | [NCSC New Zealand](../../../sources/ncsc-nz-alert-php/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Rate on exposure and precedent, not only on confirmed exploitation | partial | [The second stories: exposed, attempted, exploited, and what was within reach](../../../signals/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [CISA KEV and BOD 22-01](../../frameworks/kev/index.html) | [KEV-entry](../../frameworks/kev/index.html#c-kev-entry) | A CVE enters the catalogue on reliable evidence of active exploitation | Practice and technique |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-02](../../frameworks/nistcsf/index.html#c-id-ra-02) | Threat intelligence is received from information sharing forums and sources | Frameworks and control catalogues |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [GV.RR-01](../../frameworks/nistcsf/index.html#c-gv-rr-01) | Leadership is responsible and accountable for cybersecurity risk | Frameworks and control catalogues |

## The stories that tell it
- [Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit](../../../articles/exposed-is-not-exploited/index.html)
- [Patch at the speed of Metasploit: where php2shell sits on the weaponisation ladder, and the attacks that come second and third](../../../articles/patch-at-the-speed-of-metasploit/index.html) (through Exploitation outpaces patching)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html) (through Exploitation outpaces patching)

On this site: [No named organisation has said it was compromised through php2shell: the evidence](../../../compromise/index.html) · [The second stories: exposed, attempted, exploited, and what was within reach](../../../signals/index.html) · [Exploitation signals, in order](../../../exploitation/index.html)


---
site v0.15.9 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r03-3/index.html
