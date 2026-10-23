# The risk register: every php2shell risk, as a tree

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

All 34 risks in the fractal register, with their rating, kind, owner and the number of stakeholders and controls each touches.

[GRC](../../grc/index.html) · [Risks](../../grc/risks/index.html) · [Stakeholders](../../grc/stakeholders/index.html) · [Frameworks](../../grc/frameworks/index.html) · [The graph](../../grc/graph/index.html) · [From the network](../../grc/network/index.html)

# The risk register: every risk, as a tree

34 risks, 10 at the top and 24 beneath them. A risk beneath another is a part of it narrow enough to own. Sorted as the tree; each row links to the risk's page with its full path.

| Risk | Rating | Kind | Owned by | Stakeholders | Controls |
|---|---|---|---|---|---|
| [R01 Remote code execution on internet-facing PHP servers](../../grc/risks/r01/index.html) | **15** high | Security | [Organisations running PHP](../../grc/stakeholders/operators/index.html) | 6 | 7 |
| [R01-1 Default Apache mod_php installations exploited before application code runs](../../grc/risks/r01-1/index.html) | **15** high | Security | [Shared and self-service hosting](../../grc/stakeholders/shared-hosts/index.html) | 3 | 4 |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../grc/risks/r01-2/index.html) | **12** high | Security | [Security lead and AppSec](../../grc/stakeholders/security-lead/index.html) | 3 | 2 |
| [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../grc/risks/r01-3/index.html) | **20** critical | Security | [Organisations running PHP](../../grc/stakeholders/operators/index.html), [CTO](../../grc/stakeholders/cto/index.html) | 5 | 5 |
| [R01-4 The fix is incomplete, or a third flaw follows](../../grc/risks/r01-4/index.html) | **15** high | Security | [The fix authors](../../grc/stakeholders/php-fix-authors/index.html) | 5 | 4 |
| [R01-5 Popular applications compromised before authentication](../../grc/risks/r01-5/index.html) | **15** high | Security | [Website owner](../../grc/stakeholders/site-owner/index.html) | 3 | 3 |
| [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../grc/risks/r01-6/index.html) | **16** high | Supply chain | [Suppliers in the NCSC-NL inventory](../../grc/stakeholders/inventory-suppliers/index.html), [CTO](../../grc/stakeholders/cto/index.html) | 4 | 8 |
| [R02 The coordinated disclosure broke before the fix was ready](../../grc/risks/r02/index.html) | **20** critical | Disclosure process | [The PHP security team](../../grc/stakeholders/php-security-team/index.html) | 5 | 4 |
| [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../grc/risks/r02-1/index.html) | **20** critical | Disclosure process | [The PHP security team](../../grc/stakeholders/php-security-team/index.html) | 3 | 2 |
| [R02-2 Early mitigation advice to a few providers leaked](../../grc/risks/r02-2/index.html) | **9** medium | Disclosure process | [The PHP security team](../../grc/stakeholders/php-security-team/index.html) | 3 | 3 |
| [R02-3 Patched builds published before the embargo lifted](../../grc/risks/r02-3/index.html) | **16** high | Supply chain | [Distributors and packagers](../../grc/stakeholders/distributors/index.html) | 3 | 4 |
| [R03 Exploitation outpaces patching](../../grc/risks/r03/index.html) | **20** critical | Security | [Organisations running PHP](../../grc/stakeholders/operators/index.html) | 4 | 7 |
| [R03-1 Attempts before disclosure](../../grc/risks/r03-1/index.html) | **15** high | Security | [Security lead and AppSec](../../grc/stakeholders/security-lead/index.html) | 2 | 4 |
| [R03-2 Mass scanning and mutated payloads after the leak](../../grc/risks/r03-2/index.html) | **20** critical | Security | [Organisations running PHP](../../grc/stakeholders/operators/index.html) | 2 | 3 |
| [R03-3 Exploited in the wild without anyone being able to show it](../../grc/risks/r03-3/index.html) | **12** high | Governance | [Board and executives](../../grc/stakeholders/board/index.html) | 3 | 3 |
| [R03-4 Detections built on a proof of concept with the wrong mechanism](../../grc/risks/r03-4/index.html) | **12** high | Security | [Security lead and AppSec](../../grc/stakeholders/security-lead/index.html) | 2 | 3 |
| [R04 Services lost to precautionary shutdowns](../../grc/risks/r04/index.html) | **20** critical | Operational | [Governments and public services](../../grc/stakeholders/public-sector/index.html), [Board and executives](../../grc/stakeholders/board/index.html) | 5 | 6 |
| [R04-1 National government services offline](../../grc/risks/r04-1/index.html) | **20** critical | Operational | [National governments](../../grc/stakeholders/national-gov/index.html) | 3 | 3 |
| [R04-2 Councils and police offline without saying why](../../grc/risks/r04-2/index.html) | **15** high | Reputational | [Local councils](../../grc/stakeholders/councils/index.html) | 3 | 3 |
| [R04-3 The agencies' advice disagrees](../../grc/risks/r04-3/index.html) | **12** high | Governance | [Board and executives](../../grc/stakeholders/board/index.html) | 3 | 3 |
| [R05 A web application firewall taken for a patch](../../grc/risks/r05/index.html) | **16** high | Security | [Security lead and AppSec](../../grc/stakeholders/security-lead/index.html) | 3 | 5 |
| [R06 A compromise becomes a reportable breach](../../grc/risks/r06/index.html) | **15** high | Compliance | [Organisations running PHP](../../grc/stakeholders/operators/index.html), [Data protection officer](../../grc/stakeholders/dpo/index.html), [Board and executives](../../grc/stakeholders/board/index.html) | 5 | 6 |
| [R06-1 Personal data taken from a compromised PHP application](../../grc/risks/r06-1/index.html) | **15** high | Compliance | [Data protection officer](../../grc/stakeholders/dpo/index.html) | 3 | 6 |
| [R06-2 Essential and financial entities miss their reporting clocks](../../grc/risks/r06-2/index.html) | **12** high | Compliance | [Critical infrastructure providers](../../grc/stakeholders/critical-infra/index.html), [Banks, insurers and financial entities](../../grc/stakeholders/finance/index.html) | 4 | 5 |
| [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../grc/risks/r06-3/index.html) | **12** high | Compliance | [Suppliers in the NCSC-NL inventory](../../grc/stakeholders/inventory-suppliers/index.html) | 4 | 4 |
| [R07 Decisions made on numbers that measure something else](../../grc/risks/r07/index.html) | **12** high | Governance | [Board and executives](../../grc/stakeholders/board/index.html) | 4 | 3 |
| [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../grc/risks/r08/index.html) | **20** critical | Strategic | [OpenAI (Patch the Planet)](../../grc/stakeholders/openai/index.html) | 5 | 4 |
| [R08-1 A known bug left unexploited, then unfixed, for two years](../../grc/risks/r08-1/index.html) | **16** high | Strategic | [The PHP project](../../grc/stakeholders/php-project/index.html) | 3 | 4 |
| [R08-2 Several finders, one small team](../../grc/risks/r08-2/index.html) | **12** high | Operational | [The PHP Foundation](../../grc/stakeholders/php-foundation/index.html) | 3 | 3 |
| [R09 Not knowing where PHP runs](../../grc/risks/r09/index.html) | **16** high | Operational | [CTO](../../grc/stakeholders/cto/index.html) | 3 | 6 |
| [R10 This newsroom's own agents are steered, leak or mislead](../../grc/risks/r10/index.html) | **12** high | AI and agents | [The editor](../../grc/stakeholders/newsroom-editor/index.html) | 3 | 4 |
| [R10-1 Prompt injection through captured material](../../grc/risks/r10-1/index.html) | **12** high | AI and agents | [The editor](../../grc/stakeholders/newsroom-editor/index.html) | 2 | 3 |
| [R10-2 A vault key or token published](../../grc/risks/r10-2/index.html) | **10** medium | AI and agents | [The editor](../../grc/stakeholders/newsroom-editor/index.html) | 3 | 3 |
| [R10-3 A status word stronger than its evidence](../../grc/risks/r10-3/index.html) | **12** high | AI and agents | [The editor](../../grc/stakeholders/newsroom-editor/index.html) | 3 | 2 |

## By kind

| Kind | Risks | Highest |
|---|---|---|
| Security | 11 | [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../grc/risks/r01-3/index.html) **20** critical |
| Supply chain | 2 | [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../grc/risks/r01-6/index.html) **16** high |
| Disclosure process | 3 | [R02 The coordinated disclosure broke before the fix was ready](../../grc/risks/r02/index.html) **20** critical |
| Operational | 4 | [R04 Services lost to precautionary shutdowns](../../grc/risks/r04/index.html) **20** critical |
| Compliance | 4 | [R06 A compromise becomes a reportable breach](../../grc/risks/r06/index.html) **15** high |
| Governance | 3 | [R03-3 Exploited in the wild without anyone being able to show it](../../grc/risks/r03-3/index.html) **12** high |
| Reputational | 1 | [R04-2 Councils and police offline without saying why](../../grc/risks/r04-2/index.html) **15** high |
| Strategic | 2 | [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../grc/risks/r08/index.html) **20** critical |
| AI and agents | 4 | [R10 This newsroom's own agents are steered, leak or mislead](../../grc/risks/r10/index.html) **12** high |

## Acceptance

No risk on this register is **accepted**. An acceptance is an act by the holder of a risk, for a stated interval, and nobody can accept on anyone else's behalf; this desk records risks and their holders, it does not accept for them. Until a holder accepts, funds or fixes, each risk stands as it is rated here.


---
site v0.8.4 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/risks/index.html
