# Frameworks: php2shell risks mapped to GDPR, NIS2, CRA, DORA, the EU AI Act, ISO 27001 and NIST

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

20 frameworks and 120 controls, and which php2shell risks map to each.

[GRC](../../grc/index.html) · [Risks](../../grc/risks/index.html) · [Stakeholders](../../grc/stakeholders/index.html) · [Frameworks](../../grc/frameworks/index.html) · [The graph](../../grc/graph/index.html) · [From the network](../../grc/network/index.html)

# Frameworks: the law, the standards and the controls each risk maps to

20 frameworks, 120 clauses and controls, 95 of them mapped to at least one risk. A mapping says which control a holder of the risk will be asked about, by an auditor, a regulator or a board; it does not say the control is in place. Control titles are this desk's short paraphrase; each framework links to its official text.

## Law and regulation

Binding on the organisations in scope: a gap here is a legal exposure, not a choice.

| Framework | Version | Controls used | Risks | Why it is here |
|---|---|---|---|---|
| [GDPR](gdpr/index.html)General Data Protection Regulation, Regulation (EU) 2016/679 | 2016, in force 25 May 2018 | 6 of 6 | 3 | A PHP application that executes an attacker's code exposes the personal data it holds; whoever controls that data answers for its security and for notifying a breach. |
| [NIS2](nis2/index.html)Directive (EU) 2022/2555 on a high common level of cybersecurity across the Union | 2022, transposition deadline 17 October 2024 | 6 of 8 | 8 | Essential and important entities (energy, health, digital infrastructure, public administration and more) must manage vulnerabilities, handle incidents and report significant ones; management bodies answer for it personally. |
| [Cyber Resilience Act](cra/index.html)Regulation (EU) 2024/2847 on horizontal cybersecurity requirements for products with digital elements | 2024; reporting obligations apply from 11 September 2026 | 4 of 4 | 6 | php2shell is among the first critical flaws in a ubiquitous open-source component since the Act's reporting duty began: a manufacturer whose product ships PHP must handle the flaw and report an actively exploited one; the PHP project is the kind of open-source steward the Act treats lightly. |
| [DORA](dora/index.html)Digital Operational Resilience Act, Regulation (EU) 2022/2554 | 2022, applies from 17 January 2025 | 5 of 6 | 5 | Banks, insurers and other financial entities running PHP, or relying on an ICT provider that does, must identify, protect, detect, respond and report under one regime, and manage the provider as a third-party risk. |
| [EU AI Act](euaiact/index.html)Artificial Intelligence Act, Regulation (EU) 2024/1689 | 2024; general-purpose model obligations apply from 2 August 2025 | 3 of 4 | 4 | Frontier models found these flaws, and the same capability in other hands finds the next ones: the Act asks providers of general-purpose models with systemic risk to assess and mitigate exactly that. This newsroom's own agents are AI systems working under a mandate. |

## Management-system standards

Certifiable standards an organisation chooses and is audited against.

| Framework | Version | Controls used | Risks | Why it is here |
|---|---|---|---|---|
| [ISO/IEC 27001](iso27001/index.html)ISO/IEC 27001:2022 Information security management systems, with the Annex A controls of ISO/IEC 27002:2022 | 2022 | 14 of 21 | 17 | The management system most organisations in this story are certified to: risk assessment and treatment in clauses 6 and 8, and the controls an auditor will ask about after php2shell. |
| [ISO/IEC 42001](iso42001/index.html)ISO/IEC 42001:2023 Artificial intelligence management system | 2023 | 2 of 3 | 2 | For the organisations that run AI to find flaws or to write and check news, as this site does: the AI risk assessment and its treatment. |
| [PCI DSS](pcidss/index.html)Payment Card Industry Data Security Standard v4.0.1 | 4.0.1 | 4 of 4 | 5 | Online shops were among the sites taken offline; most run PHP (Magento, WooCommerce) and take cards. |

## Frameworks and control catalogues

Voluntary catalogues of outcomes and controls; the vocabulary auditors and boards use.

| Framework | Version | Controls used | Risks | Why it is here |
|---|---|---|---|---|
| [NIST CSF 2.0](nistcsf/index.html)NIST Cybersecurity Framework 2.0 (CSWP 29) | 2.0, February 2024 | 12 of 13 | 19 | The outcome language boards and regulators on both sides of the Atlantic now use; GOVERN makes supply chain and risk ownership a first-class function. |
| [NIST SP 800-53](nist80053/index.html)NIST SP 800-53 Rev. 5 Security and Privacy Controls for Information Systems and Organizations | Rev. 5 | 8 of 12 | 9 | The control catalogue behind US federal systems, which CISA and the NSA told to update or go offline. |
| [NIST SSDF](ssdf/index.html)NIST SP 800-218 Secure Software Development Framework 1.1 | 1.1, February 2022 | 5 of 5 | 3 | What a software producer, the PHP project included, is expected to do when a vulnerability is reported: confirm it, fix it, and find the class of bug behind it. |
| [NIST AI RMF](nistairmf/index.html)NIST AI Risk Management Framework 1.0 (AI 100-1) | 1.0, January 2023 | 3 of 4 | 3 | For AI used to find flaws and AI used to report on them: who governs it, what it can reach, and how to switch it off. |
| [CIS Controls](cis/index.html)CIS Critical Security Controls v8.1 | 8.1 | 5 of 7 | 7 | The prioritised list smaller organisations, councils and schools among them, actually work from. |
| [SOC 2](soc2/index.html)AICPA Trust Services Criteria (2017, revised points of focus 2022) | TSC 2017, revised 2022 | 2 of 5 | 2 | The report SaaS and hosting providers hand their customers; the criteria they will be asked about in the next audit window. |
| [Cyber Essentials](cyberessentials/index.html)UK Cyber Essentials: Requirements for IT infrastructure | v3.2 (Willow), 2025 | 2 of 2 | 4 | The baseline UK councils and public-sector suppliers certify against; several of the councils in this story went offline. |

## Practice and technique

How the work is done and how attackers behave: disclosure, patching, testing, techniques.

| Framework | Version | Controls used | Risks | Why it is here |
|---|---|---|---|---|
| [ISO/IEC 29147 and 30111](iso29147/index.html)ISO/IEC 29147:2018 Vulnerability disclosure and ISO/IEC 30111:2019 Vulnerability handling processes | 2018 and 2019 | 3 of 4 | 6 | The standards for exactly what broke on 20 and 21 October: receiving reports from several finders, keeping an embargo, coordinating a release and publishing the advisory. |
| [CISA KEV and BOD 22-01](kev/index.html)CISA Known Exploited Vulnerabilities catalog and Binding Operational Directive 22-01 | BOD 22-01, November 2021 | 2 of 2 | 2 | The public test of 'exploited': a CVE enters the catalogue on evidence of exploitation in the wild, and US federal agencies must then remediate by a due date. php2shell is not in it as of the vault's last capture. |
| [FIRST TLP 2.0](tlp/index.html)FIRST Traffic Light Protocol 2.0 | 2.0, August 2022 | 1 of 2 | 2 | The labels for sharing under embargo: the mitigation advice given early to critical-infrastructure providers, and its possible leak, is a TLP question. |
| [MITRE ATT&CK](attack/index.html)MITRE ATT&CK Enterprise | Enterprise v17 | 2 of 2 | 3 | How the threat is described in detection terms: scanning for the flaw first, then exploiting a public-facing application. |
| [OWASP Top 10s](owasp/index.html)OWASP Top 10 (2021 and 2025) and OWASP Top 10 for LLM Applications (2025) | 2021, 2025 | 6 of 6 | 9 | A06 is php2shell for everyone downstream of PHP; the LLM list is the risk register for this newsroom's own agents, which read the open web and hold publishing rights. |

## Risks against frameworks

How many of each framework's controls each risk maps to.

| Risk | [GDPR](gdpr/index.html) | [NIS2](nis2/index.html) | [Cyber](cra/index.html) | [DORA](dora/index.html) | [EU](euaiact/index.html) | [ISO/IEC](iso27001/index.html) | [ISO/IEC](iso42001/index.html) | [ISO/IEC](iso29147/index.html) | [NIST](nistcsf/index.html) | [NIST](nist80053/index.html) | [NIST](ssdf/index.html) | [NIST](nistairmf/index.html) | [CIS](cis/index.html) | [PCI](pcidss/index.html) | [SOC](soc2/index.html) | [Cyber](cyberessentials/index.html) | [CISA](kev/index.html) | [FIRST](tlp/index.html) | [MITRE](attack/index.html) | [OWASP](owasp/index.html) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [R01 Remote code execution on internet-facing PHP servers](../../grc/risks/r01/index.html) |  | 1 |  |  |  | 1 |  |  | 1 | 1 |  |  | 1 |  |  |  |  |  | 1 | 1 |
| [R01-1 Default Apache mod_php installations exploited before application code runs](../../grc/risks/r01-1/index.html) |  |  |  |  |  | 1 |  |  |  |  |  |  | 1 | 1 |  | 1 |  |  |  |  |
| [R01-2 PHP-FPM deployments wrongly treated as safe or as certainly vulnerable](../../grc/risks/r01-2/index.html) |  |  |  |  |  | 1 |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |
| [R01-3 Versions the PHP project no longer fixes stay vulnerable](../../grc/risks/r01-3/index.html) |  |  |  |  |  |  |  |  | 1 | 1 |  |  | 1 | 1 |  | 1 |  |  |  |  |
| [R01-4 The fix is incomplete, or a third flaw follows](../../grc/risks/r01-4/index.html) |  |  |  |  |  | 1 |  | 1 |  |  | 2 |  |  |  |  |  |  |  |  |  |
| [R01-5 Popular applications compromised before authentication](../../grc/risks/r01-5/index.html) |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  |  |  |  |  | 1 |
| [R01-6 Products that embed PHP stay vulnerable while their suppliers investigate](../../grc/risks/r01-6/index.html) |  | 1 | 2 | 1 |  | 1 |  |  | 1 |  |  |  |  |  | 1 |  |  |  |  | 1 |
| [R02 The coordinated disclosure broke before the fix was ready](../../grc/risks/r02/index.html) |  | 1 |  |  |  |  |  | 1 | 1 |  |  |  |  |  |  |  |  | 1 |  |  |
| [R02-1 The CVE IDs and the proof-of-concept video circulated before release](../../grc/risks/r02-1/index.html) |  |  |  |  |  |  |  | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| [R02-2 Early mitigation advice to a few providers leaked](../../grc/risks/r02-2/index.html) |  |  |  |  |  | 1 |  | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |
| [R02-3 Patched builds published before the embargo lifted](../../grc/risks/r02-3/index.html) |  |  | 1 |  |  |  |  | 1 | 1 |  |  |  |  |  |  |  |  |  |  | 1 |
| [R03 Exploitation outpaces patching](../../grc/risks/r03/index.html) |  |  |  |  |  | 2 |  |  | 1 | 1 |  |  |  |  |  |  | 2 |  | 1 |  |
| [R03-1 Attempts before disclosure](../../grc/risks/r03-1/index.html) |  |  |  |  |  | 1 |  |  | 1 | 1 |  |  |  | 1 |  |  |  |  |  |  |
| [R03-2 Mass scanning and mutated payloads after the leak](../../grc/risks/r03-2/index.html) |  |  |  |  |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  | 1 |  |
| [R03-3 Exploited in the wild without anyone being able to show it](../../grc/risks/r03-3/index.html) |  |  |  |  |  |  |  |  | 2 |  |  |  |  |  |  |  | 1 |  |  |  |
| [R03-4 Detections built on a proof of concept with the wrong mechanism](../../grc/risks/r03-4/index.html) |  |  |  |  |  |  |  |  | 1 | 1 |  |  |  |  | 1 |  |  |  |  |  |
| [R04 Services lost to precautionary shutdowns](../../grc/risks/r04/index.html) |  | 1 |  | 1 |  | 2 |  |  | 1 | 1 |  |  |  |  |  |  |  |  |  |  |
| [R04-1 National government services offline](../../grc/risks/r04-1/index.html) |  | 1 |  |  |  | 1 |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |
| [R04-2 Councils and police offline without saying why](../../grc/risks/r04-2/index.html) |  |  |  |  |  | 1 |  |  | 1 |  |  |  |  |  |  | 1 |  |  |  |  |
| [R04-3 The agencies' advice disagrees](../../grc/risks/r04-3/index.html) |  | 1 |  |  |  | 1 |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |
| [R05 A web application firewall taken for a patch](../../grc/risks/r05/index.html) |  |  |  |  |  | 1 |  |  |  | 1 |  |  | 1 | 1 |  | 1 |  |  |  |  |
| [R06 A compromise becomes a reportable breach](../../grc/risks/r06/index.html) | 3 | 1 | 1 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [R06-1 Personal data taken from a compromised PHP application](../../grc/risks/r06-1/index.html) | 6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [R06-2 Essential and financial entities miss their reporting clocks](../../grc/risks/r06-2/index.html) |  | 2 |  | 2 |  |  |  |  |  | 1 |  |  |  |  |  |  |  |  |  |  |
| [R06-3 Manufacturers under the Cyber Resilience Act owe a 24-hour report](../../grc/risks/r06-3/index.html) |  |  | 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| [R07 Decisions made on numbers that measure something else](../../grc/risks/r07/index.html) |  |  |  |  |  | 1 |  |  | 1 |  |  |  |  |  |  |  |  |  |  | 1 |
| [R08 Frontier AI finds critical flaws faster than maintainers can fix them](../../grc/risks/r08/index.html) |  |  |  |  | 1 |  | 1 |  |  |  |  | 2 |  |  |  |  |  |  |  |  |
| [R08-1 A known bug left unexploited, then unfixed, for two years](../../grc/risks/r08-1/index.html) |  |  | 1 |  |  | 1 |  |  |  |  | 2 |  |  |  |  |  |  |  |  |  |
| [R08-2 Several finders, one small team](../../grc/risks/r08-2/index.html) |  |  |  |  |  |  |  | 1 | 1 |  | 1 |  |  |  |  |  |  |  |  |  |
| [R09 Not knowing where PHP runs](../../grc/risks/r09/index.html) |  |  | 1 | 1 |  | 1 |  |  | 1 | 1 |  |  | 1 |  |  |  |  |  |  |  |
| [R10 This newsroom's own agents are steered, leak or mislead](../../grc/risks/r10/index.html) |  |  |  |  | 1 |  | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  | 1 |
| [R10-1 Prompt injection through captured material](../../grc/risks/r10-1/index.html) |  |  |  |  | 1 |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  | 1 |
| [R10-2 A vault key or token published](../../grc/risks/r10-2/index.html) | 1 |  |  |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 |
| [R10-3 A status word stronger than its evidence](../../grc/risks/r10-3/index.html) |  |  |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 |


---
site v0.9.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/grc/frameworks/index.html
