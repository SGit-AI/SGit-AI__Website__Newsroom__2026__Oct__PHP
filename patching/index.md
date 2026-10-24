# Patching: which versions get a fix, and from whom

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Which PHP versions the PHP project fixed, which it left to others, which nobody upstream fixed, and how the fix reaches a server: patched for you, rebuild yourself, a system update, extended support, a hosting panel, or still waiting.

# Patching: which versions get a fix, and from whom

Who can get a fix for php2shell, for which version of PHP, and from whom. Upstream is the PHP project; downstream is everyone who ships PHP to someone else: operating systems, hosting panels, cloud platforms, container images, paid support. The downstream rows are the NCSC-NL inventory's own rows at commit cca173c64ec5 (22 October, 08:40 UTC), each named exactly so the gate can check it is there and has the status quoted. The inventory changes by the hour; these are the statuses at that commit.

**46** fixed · **206** still affected · **418** under investigation · **3** not affected, of 674 products in [the NCSC-NL inventory](../affected/software.html) at commit `cca173c64ec5` [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html)

## The version ladder

Each PHP branch, what the PHP project itself shipped for it, and some of the companies that shipped a fix for it anyway, or had not yet.

| PHP branch | Upstream | What the PHP project shipped | In the CVE record | Downstream, at the inventory commit | Sources |
|---|---|---|---|---|---|
| **8.5, 8.4, 8.3, 8.2** | supported | Releases 8.5.12, 8.4.27, 8.3.36 and 8.2.35, with signed tags and Windows binaries; the full engine change | yes | fixed The PHP Group / PHP Windows maintainers: Official PHP Windows binary ZIP distribution 8.5.12, 8.4.27, 8.3.36, 8.2.35fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13fixed Debian PHP Maintainers: Debian trixie PHP 8.4 FPM package 8.4.27-1~deb13u1fixed Red Hat: Red Hat Enterprise Linux 9 php:8.2 module 8.2.35-1.module+el9.8.0+25111+a1450321fixed Docker Official Images maintainers: Docker Official Image: phpstill affected Plesk: Plesk for Windows All shipped PHP versions | [php.net](../sources/php-net-advisory/index.html) [php-src](../sources/github-php-src-tags/index.html) [CVE record](../sources/cve-cve-2026-109618/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html) |
| **8.1** | end of life | A minimal source backport on a branch; no release, no binaries | no | fixed Canonical / Ubuntu package maintainers: Ubuntu Jammy php8.1-fpm binary package 8.1.2-1ubuntu2.28fixed Heroku / Salesforce: Heroku PHP buildpack and application runtime Heroku PHP 8.2.35 / 8.3.36 / 8.4.27 / 8.5.12; rebuilt 8.1.34fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27still affected Plesk: Plesk Obsidian hosted-site PHP | [php.net](../sources/php-net-advisory/index.html) [CISA](../sources/cisa-alert-php-20261021/index.html) |
| **8.0** | end of life | A minimal source backport on a branch; no release, no binaries | no | fixed CloudLinux / TuxCare: CloudLinux Alt-PHP 8.0 package for Alpine Linux 3.23fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27 | [php.net](../sources/php-net-advisory/index.html) |
| **7.4** | end of life | A 17-file commit labelled 'Minimal mitigation for EOL version', on a branch; no release, no binaries | no | fixed Canonical / Ubuntu package maintainers: Ubuntu Focal php7.4-fpm binary package 7.4.3-4ubuntu2.29+esm5fixed CloudLinux / TuxCare: CloudLinux Alt-PHP 7.4 fixed package setfixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27 | [php-src](../sources/github-php-src-branch-7.4-backport/index.html) [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) |
| **7.3 down to 5.x** | end of life | Nothing: no backport, no branch | no | fixed Canonical / Ubuntu package maintainers: Ubuntu Bionic php7.2-fpm binary package 7.2.24-0ubuntu0.18.04.17+esm14fixed Canonical / Ubuntu package maintainers: Ubuntu Xenial php7.0-fpm binary package 7.0.33-0ubuntu0.16.04.16+esm22fixed Canonical / Ubuntu package maintainers: Ubuntu Trusty php5-fpm binary package 5.5.9+dfsg-1ubuntu4.29+esm18 | [NCSC-NL](../sources/ncsc-nl-advisories/index.html) [Wiz on X](../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../sources/certfr-2026-ale-014/index.html) |

## Why not every version
- The bug is in the engine, below any application code, so the fix has to be compiled into PHP itself; there is nothing a site's own code can change. [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html)
- The full fix is a refactor of how the engine handles memory errors, 389 files across the engine and its extensions. For the end-of-life 7.4 branch the project wrote a different, smaller change instead of carrying the refactor back. [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) [php-src](../sources/github-php-src-branch-7.4-backport/index.html)
- For end-of-life branches the project published source, not releases: someone else has to build, test and ship it. The CVE records do not list those branches at all. [php.net](../sources/php-net-advisory/index.html) [CVE record](../sources/cve-cve-2026-109618/index.html)
- Below 7.4 the project published nothing. Fixes for 7.2, 7.0 and 5.5 exist because Canonical maintains those versions for Ubuntu Pro, its commercial extended-support programme. [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html)
- CISA's advice for anyone still on 8.1 or older is to take the system offline until it is upgraded. [CISA](../sources/cisa-alert-php-20261021/index.html)

## How a fix reaches a server

The same fix arrives in very different ways depending on who a site gets its PHP from. Read from [the NCSC-NL inventory](../affected/software.html), row by row.

### Patched for you

The platform runs PHP and updates it; the customer does nothing.
- fixed Google Cloud: Google App Engine Standard PHP runtime PHP 8.2+ supported runtimes

### Fixed, but you must rebuild and redeploy

The platform or image publisher has a fixed runtime, and nothing already running changes until its owner rebuilds. 'Existing deployments are not automatically patched' is Google's phrase for App Engine Flexible.
- fixed Heroku / Salesforce: Heroku PHP buildpack and application runtime Heroku PHP 8.2.35 / 8.3.36 / 8.4.27 / 8.5.12; rebuilt 8.1.34
- fixed Docker Official Images maintainers: Docker Official Image: php
- fixed Bref project: Bref PHP Lambda runtime layers Bref 3: php-85:21, php-84:24, php-83:24, php-82:26; Bref 2 l
- still affected Google Cloud: Google App Engine Flexible PHP runtime App Engine Flexible PHP runtimes not redeployed onto patched
- still affected Google Cloud; customer image publisher: Google Cloud Run customer PHP container option Cloud Run customer containers with unpatched PHP on their re

### A package update from your operating system

The distribution backports the fix into the PHP version it shipped, and an ordinary system update installs it.
- fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13
- fixed Debian PHP Maintainers: Debian trixie PHP 8.4 FPM package 8.4.27-1~deb13u1
- fixed Arch Linux package maintainers: Arch Linux Extra PHP package 8.5.12-1
- fixed Red Hat: Red Hat Enterprise Linux 9 php:8.2 module 8.2.35-1.module+el9.8.0+25111+a1450321

### Extended support for versions upstream has abandoned

A commercial supplier backports the fix to an end-of-life version for customers of its extended-support programme: Canonical under Ubuntu Pro and Ubuntu Pro Legacy Support for PHP 5.5, 7.0, 7.2 and 7.4; CloudLinux and TuxCare for 7.4 and 8.0.
- fixed Canonical / Ubuntu package maintainers: Ubuntu Trusty php5-fpm binary package 5.5.9+dfsg-1ubuntu4.29+esm18
- fixed Canonical / Ubuntu package maintainers: Ubuntu Xenial php7.0-fpm binary package 7.0.33-0ubuntu0.16.04.16+esm22
- fixed Canonical / Ubuntu package maintainers: Ubuntu Bionic php7.2-fpm binary package 7.2.24-0ubuntu0.18.04.17+esm14
- fixed Canonical / Ubuntu package maintainers: Ubuntu Focal php7.4-fpm binary package 7.4.3-4ubuntu2.29+esm5
- fixed CloudLinux / TuxCare: CloudLinux Alt-PHP 7.4 fixed package set

### Through your hosting control panel

Shared hosting runs the PHP its panel ships, often several versions side by side; the site owner can only pick among them. Here the panels part ways: cPanel backported to 7.4, 8.0 and 8.1; Plesk's end-of-life Linux builds and all its Windows builds were still affected.
- fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27
- still affected Plesk: Plesk Obsidian hosted-site PHP
- still affected Plesk: Plesk for Windows All shipped PHP versions
- fixed Hestia Control Panel project: HestiaCP hosted-site PHP-FPM / MultiPHP option HestiaCP hosted-site PHP using patched distribution/Sury pac

### Still waiting on the supplier

The product embeds its own PHP and its supplier had not shipped a fix at that commit. Most of the inventory is here or further back: 418 of 674 rows were still under investigation.
- still affected Plesk: Plesk sw-engine internal PHP management runtime
- still affected Hestia Control Panel project: HestiaCP hestia-php internal runtime Unpatched HestiaCP bundled hestia-php runtime; fix still bei
- still affected CloudLinux: CloudLinux legacy ea-PHP extended-support packages

## What the fix changes

The reason an operator hesitates: the fix is not invisible.
- **Memory errors behave differently.** Before the fix, a request that ran out of memory jumped straight out (a C longjmp). After it, the error is queued and the request unwinds at the next safe point, so code that relied on the old fatal error at the exact allocation sees it slightly later. [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html)
- **Two new settings.** memory_hard_limit_percent sets a ceiling above memory_limit, where the worker now ends with _exit(); max_multipart_body_parts caps the parts in a form upload. Both have defaults, and a site with very large forms or memory-hungry requests may meet them. [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html)
- **The change is wide.** 389 files, 113 of them outside the tests, across the engine and the bundled extensions (standard, mbstring, gd, date, soap, zlib, session): every place that used to abort on a failed allocation was rewritten. The PHP Foundation says the fix required a major change to the engine and took two months. [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html)
- **The end-of-life mitigation trades availability for safety.** The 7.4 backport makes every memory error end the worker process at once and switches off the session upload-progress callback. A worker that exits on every out-of-memory error cannot be exploited this way, and restarts more often. [php-src](../sources/github-php-src-branch-7.4-backport/index.html)
- **Scanners can call old versions safe.** The CVE records list only 8.2 to 8.5 and default to 'unaffected', so a scanner that reads them will report 7.4 to 8.1 as not affected. The php.net advisory, the backport branches and a Greenbone reply on oss-security say they are. [CVE record](../sources/cve-cve-2026-109618/index.html) [php.net](../sources/php-net-advisory/index.html) [oss-security](../sources/openwall-oss-security-109619-thread/index.html)

## Not known yet
- How many live sites run each PHP version. No captured source counts it; W3Techs publishes version shares and is board item 033's first capture.
- What the new settings break in practice. No captured source reports a regression yet; the Fediverse report of an incomplete fix is about security, not compatibility.
- What extended support costs. The inventory shows who sells it, not the price.

The story behind this page is [Why can't every version of PHP just be patched?](../articles/why-not-patch-every-version/index.html), with the editor's argument on who should own patching. The data is [data/patching.json](../data/patching.json); the gate checks that every downstream row names a product in the inventory with the status shown.


---
site v0.14.14 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/patching/index.html
