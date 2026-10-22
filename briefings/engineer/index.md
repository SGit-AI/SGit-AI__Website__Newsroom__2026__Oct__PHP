# Briefing for a php or platform engineer: Which versions, which SAPIs, which settings, which commands?

The php2shell story for a php or platform engineer: what to decide, the claims it rests on with their status and sources, and what is still open.

Briefing · PHP or platform engineer · from the same 49 claims, selected and ordered for one reader

# Which versions, which SAPIs, which settings, which commands?

Versions, SAPIs, settings and what each does. The claims are the primary records' own words where they exist.

## What to decide or do
- Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker; rebuild images.
- memory_limit=-1 via php_admin_value; post_max_size 8M or 32M; cgroup limits not RLIMIT; session.upload_progress.enabled=0 in php.ini or the pool, never ini_set; fatal_error_backtraces=0 on 8.5; pm.max_requests=1.
- The CVE record calls 7.4 to 8.1 unaffected by omission; the backport branches say otherwise. Do not trust a scanner on this.
- The 8.5.12 fix may have a follow-up; watch php.net and oss-security.
- Verify the running version with phpinfo or php -v inside the container, after the restart.

## The facts this rests on
- confirmed two or more primary sources agree, or the fact was counted from a captured file
- reported one party says so, and it has not been contradicted
- disputed the sources disagree, and both readings are shown
- contradicted a primary source says otherwise
- unverified even the reporting outlet could not check it

| Claim | Who says it | Status | Sources |
|---|---|---|---|
| Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 | PHP Group (CNA), GitHub advisories, php.net | confirmed | [CVE record](../../sources/index.html#cve-cve-2026-109618) [CVE record](../../sources/index.html#cve-cve-2026-109619) [PHP](../../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [PHP](../../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) [php.net](../../sources/index.html#php-net-advisory) |
| Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs | PHP security team (GHSA, oss-security), php.net | confirmed | [PHP](../../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [oss-security](../../sources/index.html#openwall-oss-security-2026-10-21-6) [php.net](../../sources/index.html#php-net-advisory) |
| The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point and a hard OOM via _exit(); the changelog line is 'Avoid state corruption via bailout' | PHP security team | confirmed | [PHP](../../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [php.net](../../sources/index.html#php-net-changelog-8) [php-src](../../sources/index.html#github-php-src-branch-7.4-backport) |
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe | php.net; PHP security team | confirmed | [php.net](../../sources/index.html#php-net-advisory) [oss-security](../../sources/index.html#openwall-oss-security-2026-10-21-7) [PHP](../../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) |
| Pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCSTwo researcher parties, no third-party reproduction in the vault. The demo videos were not downloaded. | Calif; Wiz for WordPress and Drupal | reported | [Calif](../../sources/index.html#calif-php2shell) [Wiz](../../sources/index.html#wiz-blog-php2shell) |
| Remote code execution is confirmed on PHP-FPMGHSA-w8hw (CVE-2026-109618): 'no complete FPM exploit has been demonstrated for this SAPI'. The Foundation blog: RCE 'was also confirmed on PHP-FPM through application-level code paths'. GHSA-6wmf (CVE-2026-109619): session lifecycle RCE 'validated against mod_php and FPM'. The accounts may refer to different CVEs. | PHP Foundation blog; GHSA-6wmf for the session path | disputed | [PHP Foundation](../../sources/index.html#php-foundation-blog-security-release) [PHP](../../sources/index.html#github-ghsa-6wmf-4rv5-p3rp) [PHP](../../sources/index.html#github-ghsa-w8hw-w9fx-j79w) [oss-security](../../sources/index.html#openwall-oss-security-2026-10-21-6) |
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | [NCSC-NL](../../sources/index.html#ncsc-nl-advisories) [Wiz on X](../../sources/index.html#x-wiz-io-php2shell) [CERT-FR](../../sources/index.html#certfr-2026-ale-014) [oss-security](../../sources/index.html#openwall-oss-security-109619-thread) |
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. | CISA | disputed | [CISA](../../sources/index.html#cisa-alert-php-20261021) [BACS](../../sources/index.html#ch-bacs-warnung-php) [Cloudflare](../../sources/index.html#cloudflare-blog-php2shell-waf) |
| The flaws are CVSS 10.0The PHP Foundation: 'a wrong CVSS score of 10.0 (the actual score is 9.2)'. Daubois traces it to a social post relayed by Phoenix Security and to watchTowr via Cyber Daily. | social posts on 20 October, relayed by a vendor and a news site | contradicted | [PHP Foundation](../../sources/index.html#php-foundation-blog-security-release) [Daubois](../../sources/index.html#daubois-blog-php2shell-rumors) |
| The 8.5.12 fix may be incomplete, or there is a third, different bugPer a Matrix channel, Canonical asked PHP and 'was told that it's unrelated and not a real issue'. Second-hand. Nothing from PHP on the list at capture. | Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez | unverified | [oss-security](../../sources/index.html#openwall-oss-security-109619-thread) |

## What is still open
- Who first leaked the CVE IDs on 20 October, and where. The PHP Foundation does not say; a PHP security team member points to an anonymous Hacker News post. No copy of that post is in the vault.
- Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.
- Whether any site was actually compromised before it was patched or taken offline. Every claim of exploitation so far is of attempts, probes or honeypot hits.
- Which sites were really taken offline, and why. The BBC's list (parts of Wikipedia, Edinburgh council, French government services, the University of Geneva, the BBC itself) has not been captured from any of those organisations. Latvia's geo-blocking is the one documented case, from the agency itself.
- Whether the 8.5.12 fix is complete. A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated. Nothing from PHP on the list yet.

The full set of claims is on [every claim](../../claims/index.html); the ordered steps for a vulnerable system are on [if you run PHP](../../playbook/index.html). Other briefings: [Board member or executive](../board/index.html) · [Security lead](../security/index.html) · [Journalist](../journalist/index.html) · [Security researcher](../researcher/index.html) · [Analyst or advisor](../analyst/index.html).


---
site v0.1.0 · data as of 2026-10-22T08:48Z · vault commit 379e3d7f172a · https://php.oct-2026.story.sgit.ai/briefings/engineer/index.html
