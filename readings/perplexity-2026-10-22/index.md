# Perplexity's notes on php2shell, in full

> Research, external: material from outside, published as received and credited; not written here.

PHP2Shell: intelligence notes from this chat: the notes Perplexity compiled on 2026-10-22, published in full and credited, with the comparison against the evidence vault one page up.

Second reading · by Perplexity · compiled 2026-10-22

**This page is Perplexity's text, not this site's.** A research chat run by the editor in Perplexity on 22 October 2026, compiled by Perplexity into notes and given to this site by the editor. Perplexity read the web through search excerpts; it did not read the evidence vault. It is published in full and unedited, credited to Perplexity, from `admin/content/external/2026-10-22__perplexity__php2shell-intelligence-notes.md`. Its links go to the open web; none of its sources is cited by this site until a collector has captured it. Where it agrees or disagrees with the evidence vault is on [second readings](../index.html#perplexity-2026-10-22).

## PHP2Shell — intelligence notes from this chat

Compiled: 22 October 2026

### Scope and confidence

This document consolidates the reporting and research gathered during this chat. It is not an independently validated vulnerability advisory. No exploit testing, source-code review, or deployment exposure measurement was performed. Some technical details in earlier chat answers were more specific than the retrieved excerpts supported; those details are explicitly marked below rather than treated as confirmed.

### Executive summary

- The reported vulnerability family is named **PHP2Shell**, also styled `php2shell`.

- Reports identify two PHP core vulnerabilities: `CVE-2026-109618` and `CVE-2026-109619`.

- The central reporting problem is the conversion of PHP usage share into a claimed vulnerability exposure rate: “roughly 70% of the internet affected” is not an established measurement of vulnerable websites.

- The W3Techs excerpt retrieved in this chat says PHP is used by 69.3% of websites **whose server-side programming language it knows**. That qualification matters.

- Searches did not establish an earlier use of the name for a different vulnerability or tool. Absence of search results is not proof of first use.

### 1. The original claim

The user supplied a screenshot of BBC reporting stating that governments and companies, including Amazon, were responding to critical PHP flaws. The screenshot attributes the estimate that “roughly 70%” of the internet was affected to Wiz and explicitly says the BBC could not independently verify the figure.

The screenshot also reports precautionary service shutdowns, AI-assisted discovery involving Wiz and OpenAI technology, and UK government efforts to identify exposure. These are claims in the supplied article, not independently verified operational findings from this chat.

BBC article located during research:

https://www.bbc.com/news/articles/cmly0lg3w5x2o

### 2. Why the 70% claim is misleading

#### The actual denominator

The W3Techs search excerpt read:

PHP is used by 69.3% of all the websites whose server-side programming language we know.

Source:

https://w3techs.com/technologies/details/pl-php

Overview:

https://w3techs.com/technologies/overview/programming_language

This does not mean 69.3% of all websites, internet traffic, servers, applications, or internet infrastructure. It is a technology-usage estimate within the subset of websites for which the server-side language is identified.

#### Usage is not exposure

Three propositions need to remain distinct:

1. A website uses PHP.

2. Its deployed PHP version contains a particular flaw.

3. Its actual deployment is reachable and exploitable through that flaw.

A language usage statistic alone does not establish the population satisfying the latter two conditions. This chat did not retrieve an internet-wide measurement demonstrating that 70% of websites were exposed.

Wiz itself uses the headline “PHP2Shell: AI uncovers critical RCE vulnerabilities affecting 70% of the Internet,” so the broad wording is not solely a journalistic paraphrase.

Source:

https://www.wiz.io/blog/php2shell-php-rce

#### More defensible wording

Critical flaws affect widely deployed versions of PHP, a language used by roughly 70% of websites whose server-side technology can be identified. The proportion of websites currently exposed has not been established by the evidence gathered here.

### 3. Name and identifiers

| Field | Collected information |
|---|---|
| Collective name | PHP2Shell / php2shell |
| Identifiers | CVE-2026-109618 and CVE-2026-109619 |
| Reported component | PHP core/runtime |
| Reported impact | Remote code execution, including unauthenticated attack scenarios |
| Important distinction | A pair of vulnerabilities, not one CVE |

Multiple retrieved excerpts independently associate the name with both CVEs:

- BleepingComputer: https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/

- Cloudflare: https://blog.cloudflare.com/php-vulnerabilities-waf-protection/

- Huntress: https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities

- Elastic: https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection

### 4. Technical details and verification limits

An earlier answer described the two issues as follows:

| Identifier | Description given earlier | Verification status in this session |
|---|---|---|
| CVE-2026-109618 | Out-of-memory handling leaves request data partially initialized; cleanup processes invalid data, leading to memory corruption and possible RCE. | The exact per-CVE mechanism was not established by the visible retrieved excerpts. Treat as unverified pending a primary advisory or patch review. |
| CVE-2026-109619 | Request-specific state outlives its backing memory; a later request handled by the same worker can cause use-after-free, disclosure or RCE. | The exact per-CVE mechanism was not established by the visible retrieved excerpts. Treat as unverified pending a primary advisory or patch review. |

A retrieved researcher-post excerpt described the pair more broadly as memory-corruption issues in PHP internal error handling, including out-of-memory and fatal errors:

https://x.com/sagitz_/status/2112901395229597922

Earlier chat prose also discussed affected releases going back to PHP 5.4, demonstrations against WordPress, Drupal and Joomla, simple-application exposure, and exploit dependence on version, configuration and memory layout. The page retrieval available in this session was truncated; those specifics should not be treated as fully validated technical findings from this evidence set.

### 5. Reported patched versions

The following fixed releases were stated in the chat and also appeared together in a retrieved search excerpt:

- PHP 8.2.35

- PHP 8.3.36

- PHP 8.4.27

- PHP 8.5.12

Source excerpt:

https://blog.authon.dev/php2shell-cve-2026-109618-patch-check-php-version

BleepingComputer separately reported emergency patches for the two CVEs, without the complete release list in the excerpt retrieved here:

https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/

Verification limitation: the session did not retrieve an official PHP release advisory confirming this release matrix. Use it as a collected lead, not the sole basis for patch decisions.

### 6. Was the name used before?

Searches for earlier uses of the exact string did not establish a previous vulnerability or tool using this name. Search results were dominated by the October 2026 disclosure.

One FAQ says the label began as the name of the researchers’ combined exploit script and became the vulnerability-family name:

https://php2shell.uk/faq

A separate report says researchers started calling the pair php2shell and distinguishes that label from PHP’s own naming:

https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html?hl=en

Conclusion: no earlier use was verified. This is not a claim that the researchers were the first people ever to use the string.

### 7. Exploitation timeline collected

| Date | Reported event | Evidence limitation |
|---|---|---|
| 20 October 2026 | Details reportedly leaked before the patch. | Supported by retrieved reporting excerpts; no primary incident timeline reviewed. |
| 21 October 2026 | Emergency patches and reports of initial exploitation attempts. | Attempts are not proof of successful compromise or pre-disclosure exploitation. |

Sources:

- https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities

- https://www.securityweek.com/php2shell-patches-land-as-first-exploitation-attempts-hit-sensors/

- https://blog.authon.dev/php2shell-cve-2026-109618-patch-check-php-version

The collected evidence does not establish exploitation before disclosure. Lack of such evidence is not proof that no earlier exploitation occurred.

### 8. Outstanding questions

The following were not resolved by this chat:

- Official per-CVE root causes and affected-version boundaries.

- Official fixed-release matrix and support/backport coverage.

- Exact deployment prerequisites for each exploit path.

- Measured global exposure, rather than PHP market share.

- Confirmed successful exploitation and earliest reliable exploitation date.

- Definitive provenance of the PHP2Shell name.

### Bottom line

The evidence collected supports a widely reported, potentially serious PHP core vulnerability family named PHP2Shell. It does not justify interpreting a PHP technology-usage percentage as a measured percentage of vulnerable websites or of “the internet.”


---
site v0.10.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/readings/perplexity-2026-10-22/index.html
