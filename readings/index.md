# Second readings: other models, checked against the vault

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Another model's notes on php2shell, published in full and credited, set beside the evidence vault point by point: where they agree, where the vault resolves or goes further, and the new leads for capture.

# Second readings: other models, checked against the vault

The editor's first memo asked for more than one model to read this story. The vault was read by Claude agents; this page sets readings by other models beside it, point by point. Each other model's text is published in full and credited, and nothing in it is cited on this site until a collector has captured its source.

- agrees the vault holds the same finding, from captured sources
- the vault resolves it the other model left it open or unverified; a primary source in the vault settles it
- the vault goes further the vault holds a more specific or earlier finding on the same point
- a new lead the other model names something the vault does not hold; listed for capture, not cited
- open in both neither reading can settle it

## Perplexity: PHP2Shell: intelligence notes from this chat

A research chat run by the editor in Perplexity on 22 October 2026, compiled by Perplexity into notes and given to this site by the editor. Perplexity read the web through search excerpts; it did not read the evidence vault. [The notes in full →](perplexity-2026-10-22/index.html)

**5** agrees · **2** the vault resolves it · **4** the vault goes further · **1** a new lead · **1** open in both

| Point | What Perplexity found | Against the vault | What the vault holds | Sources |
|---|---|---|---|---|
| **The name and the pair**section 3 | PHP2Shell names two PHP core vulnerabilities, CVE-2026-109618 and CVE-2026-109619: a pair, not one CVE. | agrees | Confirmed from the CVE records, the GitHub advisories and php.net.[two-cves-9.2](../claims/index.html#two-cves-9.2) | [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) [php.net](../sources/php-net-advisory/index.html) |
| **What 70% is a share of**section 2 | W3Techs says PHP is used by 69.3% of all the websites 'whose server-side programming language we know'. Usage is not exposure: a site using PHP, running a flawed version, and being reachable through the flaw are three different populations. | the vault goes further | The vault already carries the qualifier, second-hand: a security founder's post on X, captured on 22 October, says 'PHP runs 69% of websites whose server-side language is known'. The three pages that carry the bare 70% figure do not name the measurement. W3Techs itself is not captured; capturing it would make this first-hand and close the front page's open question.[scale-70pc-websites](../claims/index.html#scale-70pc-websites), [scale-70pc-internet](../claims/index.html#scale-70pc-internet) | [Feross Aboukhadijeh on X on X](../sources/x-feross-chainguard/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html) [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../sources/x-openai-php2shell/index.html) |
| **Who said 70% of the Internet**section 2 | Wiz's own headline says 'affecting 70% of the Internet', so the broad wording is not only a journalist's paraphrase. | agrees | The same: the vault attributes '70% of the Internet' to Wiz's headline and X post, and marks it unverified.[scale-70pc-internet](../claims/index.html#scale-70pc-internet) | [Wiz](../sources/wiz-blog-php2shell/index.html) [Wiz on X](../sources/x-wiz-io-php2shell/index.html) |
| **The BBC and the 70% figure**section 1 | A BBC article attributes 'roughly 70%' to Wiz and says the BBC could not independently verify it. | agrees | The vault's capture of the BBC live page carries the same attribution. The BBC article Perplexity read is a different page and is not in the vault; it is listed below for capture.[scale-70pc-internet](../claims/index.html#scale-70pc-internet) | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| **How each flaw works**section 4 | The per-CVE mechanisms (out-of-memory handling leaving request memory uninitialised; request state outliving its memory into the next request) are marked unverified, pending a primary advisory or a patch review. | the vault resolves it | Both mechanisms are stated in the CVE records and the GitHub advisories, and the fix commit was read from a clone of php-src. Perplexity's earlier descriptions were right; its caution was right too, given what it could read.[fix-engine](../claims/index.html#fix-engine), [fix-bailout](../claims/index.html#fix-bailout) | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) |
| **The fixed versions**section 5 | 8.2.35, 8.3.36, 8.4.27 and 8.5.12, treated as a collected lead because no official PHP advisory was retrieved. | the vault resolves it | Confirmed by php.net's advisory, the CVE records and the signed tags in php-src.[two-cves-9.2](../claims/index.html#two-cves-9.2) | [php.net](../sources/php-net-advisory/index.html) [php-src](../sources/github-php-src-tags/index.html) |
| **Versions back to 5.4**section 4 | Earlier answers said affected releases go back to PHP 5.4; not validated. | the vault goes further | Disputed in the vault: Wiz says 5.4 and later, NCSC-NL from 5, CERT-FR lists 5.x to 8.1, while the CVE records list only 8.2 to 8.5; the project published backports down to 7.4.[versions-old](../claims/index.html#versions-old) | [Wiz on X](../sources/x-wiz-io-php2shell/index.html) [NCSC-NL](../sources/ncsc-nl-advisories/index.html) [CERT-FR](../sources/certfr-2026-ale-014/index.html) [php-src](../sources/github-php-src-branch-7.4-backport/index.html) |
| **Demonstrations against applications**section 4 | Demonstrations against WordPress, Drupal and Joomla; not validated. | the vault goes further | Reported, not confirmed: Calif lists eleven applications and Wiz two, each by its own account; no third party has reproduced them in a captured source.[wordpress-drupal](../claims/index.html#wordpress-drupal) | [Calif](../sources/calif-php2shell/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html) |
| **Where the name came from**section 6 | A FAQ at php2shell.uk says the label began as the name of the researchers' combined exploit script. No earlier use of the name was found, which is not proof of first use. | a new lead | The FAQ is not in the vault. What the vault holds fits it: on 20 October a screenshot of a 'PHP2Shell tool' credited to Calif.io circulated, per a PHP security team member's account, and the NSA calls the pair PHP2Shell.[leak-hn](../claims/index.html#leak-hn) | [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) [NSA](../sources/nsa-press-php-4630238/index.html) |
| **Exploitation before disclosure**section 7 | The collected evidence does not establish exploitation before disclosure; absence of evidence is not proof. | the vault goes further | Amazon reports one exploit attempt against a honeypot on 17 October, four days before disclosure, from an anonymisation network. That is an attempt against a sensor, still not a compromise.[amazon-honeypot](../claims/index.html#amazon-honeypot) | [Amazon](../sources/aws-security-blog-madpot/index.html) [THN](../sources/thehackernews-php2shell-4days/index.html) |
| **Attempts are not compromises**section 7 | Reports of exploitation attempts on 21 October are not proof of successful compromise. | agrees | The same, counted across every captured source: no named organisation has confirmed a compromise.[no-confirmed-compromise](../claims/index.html#no-confirmed-compromise), [cf-millions](../claims/index.html#cf-millions) | [CISA](../sources/cisa-kev-json/index.html) [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| **Measured exposure**section 8 | Outstanding: a measured global exposure, rather than PHP's market share. | open in both | Open here too. The nearest are host counts: VulnCheck's 2.6 million internet-facing hosts and Censys's 1.57 million unpatched on 21 October, which count machines, not sites, and say nothing about configuration.[scale-2.6m-hosts](../claims/index.html#scale-2.6m-hosts) | [THN](../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../sources/securityweek-exploitation-days-before/index.html) |
| **Its own earlier answers**section Scope | The notes say that some technical details in Perplexity's earlier answers in the same chat were more specific than the excerpts it had retrieved could support, and mark them rather than repeat them. | agrees | This is the rule the verifier role exists to enforce here: a statement the captured text does not carry is downgraded, not repeated. A model applying it to itself is worth recording. |  |

### Sources Perplexity named that the vault has not captured

Listed for the collectors, in the order they should be captured. None is cited on this site until it is captured; this list is the whole of what they are used for.

- [W3Techs on PHP: the 69.3% figure and its denominator](https://w3techs.com/technologies/details/pl-php) first: it would close the front page's open question on what 70% measures
- [W3Techs: server-side languages overview](https://w3techs.com/technologies/overview/programming_language) with the above
- [A FAQ on the name's origin](https://php2shell.uk/faq) second: the only account of where the name came from
- [A BBC article, separate from the live page in the vault](https://www.bbc.com/news/articles/cmly0lg3w5x2o) third
- [A Wiz researcher's post on the bug class](https://x.com/sagitz_/status/2112901395229597922) third: social posts get deleted
- [BleepingComputer on the emergency patches](https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/) later
- [Elastic Security Labs on detection](https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection) later: for the detection and defence page
- [A blog post with the fixed-version list](https://blog.authon.dev/php2shell-cve-2026-109618-patch-check-php-version) later: secondary, the vault holds the primary

The comparison rows are [data/readings.json](../data/readings.json), in the derived layer; the other models' text is in the authored layer ([evidence, derived, authored](../layers/index.html)). The gate checks every source and claim a row cites.


---
site v0.15.13 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/readings/index.html
