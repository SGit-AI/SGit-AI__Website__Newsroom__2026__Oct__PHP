# R02: The coordinated disclosure broke before the fix was ready

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Because the secret was held by four finders, a coalition, critical-infrastructure providers and image builders at once, it leaked a day early, resulting in a release moved forward by 24 hours and defenders starting the race with attackers already told where to look.

[Risks](../index.html) / R02

# R02: The coordinated disclosure broke before the fix was ready

Because the secret was held by four finders, a coalition, critical-infrastructure providers and image builders at once, it leaked a day early, resulting in a release moved forward by 24 hours and defenders starting the race with attackers already told where to look.

[Explore the graph from this risk](../../explore/index.html#focus=risk:r02) · [What the graph is missing](../../gaps/index.html)

**Rating** **20** critical · **Likelihood** 5 Happening · **Impact** 4 Major · **Kind** Disclosure process · **Acceptance** not recorded

**Basis.** It happened: the release moved from 22 to 21 October because of the leak.

## The path

The risk sits in the middle. To its left, the stories that tell it, the roles and team members that act on it, and every stakeholder that carries part of it. To its right, what it arises from, the vulnerability behind that, the part of the fix that addresses it and the code the fix changed. Every line is an edge in the graph; every node is a link; hover for the full name. Vulnerabilities, stories and team members include those of the risk this one is part of; roles include those of the risks above and beneath it.

## Who carries it

One risk, assigned to every stakeholder that carries part of it, with the part each plays.

| Stakeholder | Part | Why | Its register |
|---|---|---|---|
| [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) | **owner** | Ran the embargo and moved the release. | 7 risks |
| [The finders](../../../grc/stakeholders/finders/index.html) | **source** | Four parties held the details; one published a video by mistake. | 7 risks |
| [Distributors and packagers](../../../grc/stakeholders/distributors/index.html) | **source** | Built and, in one disputed case, published fixed images early. | 3 risks |
| [Organisations running PHP](../../../grc/stakeholders/operators/index.html) | **bearer** | Lost a day of preparation. | 26 risks |
| [Security lead and AppSec](../../../grc/stakeholders/security-lead/index.html) | **bearer** | Starts the patch plan a day early, on leaked details. | 6 risks |

## The risks this one is made of

| Risk | Rating | Kind | Assigned to | Controls |
|---|---|---|---|---|
| [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../../grc/risks/r02-1/index.html) | **20** critical | Disclosure process | [Calif](../../../grc/stakeholders/calif/index.html) source, [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) owner, [Edge, WAF and detection vendors](../../../grc/stakeholders/edge/index.html) treater | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [NIST CSF 2.0 ID.RA-08](../../../grc/frameworks/nistcsf/index.html#c-id-ra-08) |
| [R02-3 Patched builds published before the embargo lifted](../../../grc/risks/r02-3/index.html) | **16** high | Supply chain | [Chainguard](../../../grc/stakeholders/chainguard/index.html) source, [Distributors and packagers](../../../grc/stakeholders/distributors/index.html) owner, [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) regulator | [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination), [Cyber Resilience Act Art.13](../../../grc/frameworks/cra/index.html#c-art-13), [NIST CSF 2.0 GV.SC-05](../../../grc/frameworks/nistcsf/index.html#c-gv-sc-05), [OWASP Top 10s A03:2025](../../../grc/frameworks/owasp/index.html#c-a03-2025) |
| [R02-2 Early mitigation advice to a few providers leaked](../../../grc/risks/r02-2/index.html) | **9** medium | Disclosure process | [Critical infrastructure providers](../../../grc/stakeholders/critical-infra/index.html) source, [The PHP security team](../../../grc/stakeholders/php-security-team/index.html) owner, [Organisations running PHP](../../../grc/stakeholders/operators/index.html) bearer | [FIRST TLP 2.0 TLP:AMBER+STRICT](../../../grc/frameworks/tlp/index.html#c-tlp-amber-strict), [ISO/IEC 27001 A.5.14](../../../grc/frameworks/iso27001/index.html#c-a-5-14), [ISO/IEC 29147 and 30111 29147:coordination](../../../grc/frameworks/iso29147/index.html#c-29147-coordination) |

## What it arises from
- **One embargo shared by many parties.** Four independent finders, a coalition, early advice to critical infrastructure and image builders: every party is a place the secret can leave by.

## The evidence

| Claim | Status | Fact-check | Sources |
|---|---|---|---|
| [The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leak](../../../facts/release-moved/index.html) | confirmed | **A4** Corroborated●●●●○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../../sources/openwall-oss-security-2026-10-20-34/index.html) [Wiz on X](../../../sources/x-wiz-io-php2shell/index.html) [php.net](../../../sources/php-net-changelog-8/index.html) |
| [On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social media with a wrong release time and a wrong CVSS score; no technical details leaked](../../../facts/leak-cve-ids/index.html) | reported | **A4** Corroborated●●●●○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../../sources/phpfoundation-blog-security-release-leak/index.html) |
| [Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a number of targets; copies circulated and 'contributed to accelerated development of various PoCs'](../../../facts/leak-video/index.html) | reported | **A3** Echoed●●●○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [PHP Foundation](../../../sources/phpfoundation-blog-security-release-leak/index.html) [BBC News](../../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Calif](../../../sources/calif-php2shell/index.html) |
| [Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built images containing the fix](../../../facts/chainguard/index.html) | disputed | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) [The Register](../../../sources/theregister-php-blames-chainguard/index.html) [Feross Aboukhadijeh on X on X](../../../sources/x-feross-chainguard/index.html) |
| [Mitigation advice given to a few critical-infrastructure providers from about 23:00 UTC on 20 October may have leaked](../../../facts/leak-mitigations/index.html) | reported | **A2** Reported●●○○○○ | [PHP Foundation](../../../sources/php-foundation-blog-security-release/index.html) |

## Treatments

| Treatment | Status | Where |
|---|---|---|
| Move the release forward once the leak was confirmed | in place | [How the coordinated disclosure broke](../../../leak/index.html) |

## The standards that govern it

| Framework | Control | What it asks | Family |
|---|---|---|---|
| [ISO/IEC 29147 and 30111](../../frameworks/iso29147/index.html) | [29147:coordination](../../frameworks/iso29147/index.html#c-29147-coordination) | Coordinating disclosure with other vendors and parties under embargo | Practice and technique |
| [NIS2](../../frameworks/nis2/index.html) | [Art.12](../../frameworks/nis2/index.html#c-art-12) | Coordinated vulnerability disclosure and the European vulnerability database | Law and regulation |
| [NIST CSF 2.0](../../frameworks/nistcsf/index.html) | [ID.RA-08](../../frameworks/nistcsf/index.html#c-id-ra-08) | Processes for receiving, analysing and responding to vulnerability disclosures are established | Frameworks and control catalogues |
| [FIRST TLP 2.0](../../frameworks/tlp/index.html) | [TLP:AMBER+STRICT](../../frameworks/tlp/index.html#c-tlp-amber-strict) | Limited disclosure: recipients share only within their organisation | Practice and technique |

## The stories that tell it
- [Where php2shell stands: many sites dark, millions of attempts, no confirmed breach](../../../articles/where-php2shell-stands/index.html)
- [php2shell in perspective: an old embargo model, a Log4Shell shape, and the shrinking gap between theory and proof](../../../articles/php2shell-in-perspective/index.html)

On this site: [How the coordinated disclosure broke](../../../leak/index.html) · [The timeline, 2024 to the latest capture](../../../timeline/index.html)


---
site v0.22.13 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/r02/index.html
