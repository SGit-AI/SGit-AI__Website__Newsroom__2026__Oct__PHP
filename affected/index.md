# Affected systems: versions, deployments, applications, inventory

Which PHP versions and SAPIs php2shell affects, which applications had RCE demonstrated, and the NCSC-NL inventory of 674 products counted by status.

# Affected systems

Three layers: the PHP versions, the ways PHP is attached to a web server, and the software that runs on top. The first two come from the PHP project. The third comes from NCSC-NL's public inventory, which this site counts rather than quotes: 674 products at commit `cca173c64ec5`, of which 206 are marked vulnerable to CVE-2026-109618, 46 fixed, 418 under investigation and 3 not vulnerable.

## Versions

| Branch | Affected | Fixed | In the CVE record |
|---|---|---|---|
| 8.5 | = 5.4' (Wiz); 'toutes versions 5.x, 6.x, 7.x' (CERT-FR) | no release, no backport | **no** |

The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected. The php.net advisory, the backport branches and a Greenbone reply on oss-security say otherwise. [CVE record](../sources/cve-cve-2026-109618/index.html) [php.net](../sources/php-net-advisory/index.html) [php-src](../sources/github-php-src-branch-7.4-backport/index.html) [NCSC-NL](../sources/ncsc-nl-advisories/index.html) [Wiz on X](../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../sources/certfr-2026-ale-014/index.html) [oss-security](../sources/openwall-oss-security-109619-thread/index.html)

## Deployments

| SAPI | Risk | What the primary sources say | Sources |
|---|---|---|---|
| Apache mod_php | highest | Unauthenticated RCE demonstrated over HTTP with default input and memory limits, before any application code runs. | [php.net](../sources/php-net-advisory/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../sources/openwall-oss-security-2026-10-21-6/index.html) |
| PHP-FPM | susceptible | For CVE-2026-109618 the GitHub advisory says no complete FPM exploit has been demonstrated; the PHP Foundation blog says RCE was confirmed on FPM through application-level paths. For CVE-2026-109619 the session path was validated against FPM. | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) [oss-security](../sources/openwall-oss-security-2026-10-21-7/index.html) |
| php-cgi | at risk | Listed by php.net among installations serving web requests. | [php.net](../sources/php-net-advisory/index.html) |
| FrankenPHP | likely susceptible | 'likely susceptible' per the GitHub advisory. | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| LiteSpeed (LSAPI) | likely, unvalidated | 'application-specific exploits being likely but unvalidated'. | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) |
| CLI, cron, queue workers | not web-serving | The advisory scopes the risk to installations serving web requests. A CLI process that parses untrusted input is not covered either way by the primary sources. | [php.net](../sources/php-net-advisory/index.html) |

## Applications

Calif reports confirmed pre-authentication RCE against WordPress 7.1.2, Drupal 11.4.3, Joomla 6.1.4, MediaWiki, Roundcube, Magento, phpMyAdmin, Nextcloud, Laravel, Symfony and WHMCS; Wiz confirmed Drupal (20 August) and WordPress (21 August). The flaw is below the application, so any PHP web application on an affected runtime is in scope. [Calif](../sources/calif-php2shell/index.html) [Wiz](../sources/wiz-blog-php2shell/index.html)

## The NCSC-NL inventory, counted

| Status | CVE-2026-109618 | CVE-2026-109619 |
|---|---|---|
| Vulnerable | 206 | 206 |
| Fix | 46 | 46 |
| Investigation | 418 | 418 |
| Not vuln | 3 | 3 |
| none | 1 | 1 |

NCSC-NL generates the list from an SPDX 3 inventory with VEX statements and says an entry is an investigation lead until a vendor or upstream backs it. 46 products carry a fix for both CVEs; 206 are marked vulnerable to at least one. The suppliers with the most entries:

| Supplier | Entries |
|---|---|
| The PHP Group | 86 |
| Nette community | 15 |
| Synology | 11 |
| Canonical / Ubuntu package maintainers | 9 |
| Sean Morris / php-wasm project | 7 |
| Icinga GmbH | 6 |
| Symfony | 6 |
| Microsoft Azure Storage | 5 |
| Plesk | 5 |
| SURF | 5 |
| TuxCare / CloudLinux | 5 |
| WordPress Playground contributors | 5 |
| Docker Official Images / docker-library PHP maintainers | 4 |
| Google | 4 |
| Laravel | 4 |

[The full inventory, all 674 rows →](software.html) The parsed file is in the vault as `software-list-cca173c64ec5.json`; the repository bundle and tree at the same commit are there too. [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell/index.html)


---
site v0.2.6 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/affected/index.html
