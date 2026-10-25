# Briefing for a developer: Is my code the problem, what do I change, and how do I check the box I deployed to?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The php2shell story for a developer: a thirty-second answer, what to decide, a reading path, the claims it rests on with their status and sources, and what is still open.

Briefing for Lee, developer · ******Some technical · from the same 70 claims, selected and ordered for one reader

# Is my code the problem, what do I change, and how do I check the box I deployed to?

L
The answer in thirty seconds

Your code is not the problem and cannot be the fix: the flaw is in the engine beneath it. ini_set, .user.ini and auto_prepend_file all run too late. Check the running version where the code runs, after the restart, and tell the platform owner today if your target is 8.1 or older.

[Read the site as Lee →](../../flaws/index.html)

Your code is not the problem and cannot be the fix. The flaw is in the C engine that runs it. What you can do is check the box you deploy to and avoid making the engine's job harder.

## What to decide or do
- Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.
- Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35. If your target is 8.1 or older there is no release; tell whoever owns the platform today.
- Nothing in userland blocks the demonstrated paths: ini_set() runs too late, .user.ini runs too late, auto_prepend_file runs too late. The settings have to be in php.ini, the pool or the server config.
- Fix attacker-reachable fatal errors and timeouts in your own code anyway: the advisory lists them as one of the paths for the stale-state bug.
- After the patch, out-of-memory behaves differently: a delayed fatal at the next safe point instead of an abort, and a hard limit that ends the process. Code that caught the old behaviour in tests will see a change.

## Your reading path
- [Your briefing](../../briefings/developer/index.html) 4 min
- [The two flaws](../../flaws/index.html) 4 min
- [The code](../../code/index.html) 7 min
- [If you run PHP](../../playbook/index.html) 3 min

About 18 minutes in all. Choose *read as Lee* and the bar under the menu keeps your place on every page.

### What this briefing covers
- is my code the problem
- what I can and cannot do in userland
- how to check the box I deploy to

### What you can skip
- the agency comparison
- the money

## Words you will meet

[Patch](../../glossary/index.html#patch)[Out of memory (OOM)](../../glossary/index.html#oom)[Primary source](../../glossary/index.html#primary)[PHP](../../glossary/index.html#php)[CVSS](../../glossary/index.html#cvss)[Vulnerability](../../glossary/index.html#vulnerability)[GitHub advisory (GHSA)](../../glossary/index.html#ghsa)[Remote code execution (RCE)](../../glossary/index.html#rce)[mod_php](../../glossary/index.html#mod-php)[longjmp](../../glossary/index.html#longjmp)[CVE](../../glossary/index.html#cve)[Exploit, exploitation](../../glossary/index.html#exploit)[Proof of concept (PoC)](../../glossary/index.html#poc)[PHP-FPM](../../glossary/index.html#fpm)

Each is underlined where it first appears; hover or tap for a one-line definition, or open [the glossary](../../glossary/index.html).

## The facts this rests on
- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it
- p/n primary sources among the n cited; a blocked capture is counted and marked

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 [fact timeline →](../../facts/two-cves-9.2/index.html) | PHP Group (CNA), GitHub advisories, php.net | confirmed | **A6** Established●●●●●● | 5/5 | [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs [fact timeline →](../../facts/rce-modphp/index.html) | PHP security team (GHSA, oss-security), php.net | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) [php.net](../../sources/php-net-advisory/index.html) |
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' [fact timeline →](../../facts/fix-bailout/index.html) | PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php.net](../../sources/php-net-changelog-8/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html) |
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe [fact timeline →](../../facts/only-update/index.html) | php.net; PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [php.net](../../sources/php-net-advisory/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity highFastly: 'most deployments may be safe from RCE. Do not assume this holds true for you.' Imperva: five demonstrated techniques, three via session upload progress; about 67 KB of memory disclosed per attack. [fact timeline →](../../facts/ac-high/index.html) | Imperva; Fastly; the CVE record | confirmed | **A3** Echoed●●●○○○ opinion status overstated | 3/3 | [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and request globals that survive a failed requestThe fix replaces bailout with a delayed error and an UnwindExit at a safe point, adds a hard limit that _exits, and resets the globals. See the code page. [fact timeline →](../../facts/fix-engine/index.html) | php/php-src fix commit; the GitHub advisories | confirmed | **A6** Established●●●●●● | 3/3 | [php/php-src, read from a clone](../../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCSTwo researcher parties, no third-party reproduction in the vault. The demo videos were not downloaded. [fact timeline →](../../facts/wordpress-drupal/index.html) | Calif; Wiz for WordPress and Drupal | reported | **A2** Reported●●○○○○ | 2/2 | [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) |
| None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200The Hacker News says the same of the public code. Fastly: working RCE needs knowledge of the running binary's layout on x86_64. [fact timeline →](../../facts/pocs-wrong/index.html) | rjmendez (detection author) citing VulnCheck; Huntress | reported | **A1** Weak signal●○○○○○ status overstated | 1/2 | [rjmendez, GitHub](../../sources/github-rjmendez-phpup-2026/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |
| Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expectedA position, from a vendor; consistent with the Fediverse report of a third bug. [fact timeline →](../../facts/more-paths/index.html) | Fastly | reported | **A2** Reported●●○○○○ opinion | 1/2 | [Fastly](../../sources/fastly-blog-php2shell/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. [fact timeline →](../../facts/rce-fpm/index.html) | PHP Foundation blog; GHSA-6wmf for the session path | disputed | **A6** Established●●●●●● | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-6/index.html) |
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. [fact timeline →](../../facts/versions-old/index.html) | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | **A3** Echoed●●●○○○ disputed | 3/4 | [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. [fact timeline →](../../facts/waf/index.html) | CISA | disputed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |
| The flaws are CVSS 10.0The PHP Foundation: 'a wrong CVSS score of 10.0 (the actual score is 9.2)'. Daubois traces it to a social post relayed by Phoenix Security and to watchTowr via Cyber Daily. [fact timeline →](../../facts/cvss-10/index.html) | social posts on 20 October, relayed by a vendor and a news site | contradicted | refuted contradicted | 1/2 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) |
| The 8.5.12 fix may be incomplete, or there is a third, different bugPer a Matrix channel, Canonical asked PHP and 'was told that it's unrelated and not a real issue'. Second-hand. Nothing from PHP on the list at capture. [fact timeline →](../../facts/fix-incomplete/index.html) | Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez | unverified | **A1** Weak signal●○○○○○ opinion disputed | 0/1 | [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |

## What is still open
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post, and Notebookcheck and Nguoi Quan Sat repeat that account. No copy of the post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits, and the named cases do not state php2shell as the cause. Authorities in Singapore and Luxembourg now ask operators to look for traces; the answer will come from those searches, if it comes.
- Which sites were really taken offline, and why. The list now draws on more captured reports (Germany's hospitals and hosts, Morocco, Romania, Japan), but most are press accounts; few come from the organisations themselves (the Dutch government, Latvia's agency, Weird Gloop, the Charité's spokesman as quoted). A community tracker counts 51 listed and 50 back.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. On 23 October PHP published an informational advisory for a separate flaw, CVE-2026-115560, in the session upload progress feature, reported by Cloudflare, SOCRadar and The Hacker News: it affects fully patched releases including 8.5.12, needs a rare session setting, will be fixed in the next regular release, and has session.upload_progress.enabled=0 as the mitigation; SOCRadar reports no exploitation and no severity score. PHP's advisory is not in the evidence vault, and whether this is the bug the Fediverse report described is not stated.

The full set of claims is on [every claim](../../claims/index.html); the ordered steps for a vulnerable system are on [if you run PHP](../../playbook/index.html). Other readers: [Curious reader](../everyone/index.html) · [Website owner](../site-owner/index.html) · [Project or programme manager](../pm/index.html) · [Board member or executive](../board/index.html) · [Security lead](../security/index.html) · [PHP or platform engineer](../engineer/index.html) · [Journalist](../journalist/index.html) · [Security researcher](../researcher/index.html) · [Analyst or policy advisor](../analyst/index.html) · [CISO](../ciso/index.html) · [CTO](../cto/index.html) · [CFO](../cfo/index.html) · [Data protection officer](../dpo/index.html) · [Head of AppSec](../appsec/index.html) · [Communications team](../comms/index.html).


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/briefings/developer/index.html
