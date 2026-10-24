# The inventory, hour by hour: fixed, vulnerable, still under investigation

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The NCSC-NL php2shell inventory across 50 commits: how 751 products moved between fixed, vulnerable and under investigation after the release, what kind of products they are, and when each supplier was first recorded fixed.

# The inventory, hour by hour: fixed, vulnerable, still under investigation

The Dutch NCSC keeps a public list of software that ships or depends on PHP, with a status for each product. This site captured it once, at 08:40 UTC on 22 October. Its git history shows the rest: 50 versions from 21 October 2026, 11:20 UTC to 23 October 2026, 12:50 UTC, each read from the commit that made it. At the last one, 109 of 751 rows were fixed, 222 vulnerable and 389 still under investigation, about 47 hours after the release.

- Fixed
- Not affected
- Vulnerable
- Under investigation

Rows by status at every commit of the inventory that changed it. Hover a column for the commit and its counts; the table below has the same numbers. Read from a clone of [https://github.com/NCSC-NL/php2shell](https://github.com/NCSC-NL/php2shell) at `2fdc314ded28`.

The same numbers as a table
| When (UTC) | Commit | Rows | Fixed | Not affected | Vulnerable | Under investigation |
|---|---|---|---|---|---|---|
| 21 October 2026, 11:20 UTC | `1781b17f0eb7` | 620 | 0 | 0 | 0 | 620 |
| 21 October 2026, 11:41 UTC | `fa324ebe5b53` | 620 | 0 | 0 | 0 | 620 |
| 21 October 2026, 12:01 UTC | `1e690ffff384` | 622 | 0 | 0 | 2 | 620 |
| 21 October 2026, 12:13 UTC | `2a5edbab577f` | 622 | 0 | 0 | 3 | 619 |
| 21 October 2026, 12:24 UTC | `8a41720a54f8` | 622 | 0 | 0 | 5 | 617 |
| 21 October 2026, 12:38 UTC | `b01efe4f6f38` | 629 | 0 | 0 | 5 | 624 |
| 21 October 2026, 12:41 UTC | `60da4d290315` | 629 | 0 | 0 | 5 | 624 |
| 21 October 2026, 12:57 UTC | `cb58112f6e3e` | 629 | 0 | 0 | 5 | 624 |
| 21 October 2026, 13:05 UTC | `23dbf42b2bba` | 629 | 0 | 0 | 6 | 623 |
| 21 October 2026, 13:38 UTC | `cb3182746ed2` | 630 | 0 | 1 | 6 | 623 |
| 21 October 2026, 14:10 UTC | `2383e9b98b2c` | 630 | 0 | 1 | 8 | 621 |
| 21 October 2026, 14:11 UTC | `fec0407ebe49` | 630 | 0 | 1 | 8 | 621 |
| 21 October 2026, 14:33 UTC | `360888300228` | 632 | 0 | 1 | 8 | 623 |
| 21 October 2026, 15:30 UTC | `b4da5417672d` | 633 | 1 | 1 | 8 | 623 |
| 21 October 2026, 16:03 UTC | `bec5b547bd27` | 633 | 8 | 1 | 9 | 615 |
| 21 October 2026, 16:06 UTC | `a490b0be270f` | 636 | 11 | 1 | 9 | 615 |
| 21 October 2026, 17:03 UTC | `eea1372e344d` | 636 | 19 | 1 | 12 | 604 |
| 21 October 2026, 17:46 UTC | `1b3c6dd3e26d` | 648 | 30 | 1 | 13 | 604 |
| 21 October 2026, 18:01 UTC | `b4ee11d57841` | 648 | 45 | 4 | 20 | 579 |
| 21 October 2026, 20:40 UTC | `3b6535ac4863` | 650 | 45 | 4 | 31 | 569 |
| 21 October 2026, 21:14 UTC | `0a01a4a3a786` | 650 | 45 | 4 | 206 | 394 |
| 21 October 2026, 21:22 UTC | `fb312f372f05` | 664 | 45 | 4 | 206 | 408 |
| 21 October 2026, 21:40 UTC | `682c88a2d1b9` | 672 | 45 | 4 | 206 | 416 |
| 22 October 2026, 08:22 UTC | `17188006c9a8` | 673 | 45 | 4 | 206 | 417 |
| 22 October 2026, 08:27 UTC | `86b418d24f3b` | 674 | 46 | 4 | 206 | 417 |
| 22 October 2026, 08:40 UTC | `cca173c64ec5` | 675 | 46 | 4 | 206 | 418 |
| 22 October 2026, 09:25 UTC | `f944d1d6e558` | 675 | 61 | 4 | 206 | 403 |
| 22 October 2026, 12:30 UTC | `047f49681080` | 675 | 61 | 4 | 207 | 402 |
| 22 October 2026, 12:57 UTC | `145eb125f6c9` | 675 | 61 | 4 | 207 | 402 |
| 22 October 2026, 13:08 UTC | `aa2d52c4f8dd` | 676 | 61 | 4 | 208 | 402 |
| 22 October 2026, 13:17 UTC | `5ecd81b9b29b` | 707 | 61 | 6 | 208 | 431 |
| 22 October 2026, 13:17 UTC | `741faabd9c2a` | 707 | 61 | 6 | 208 | 431 |
| 22 October 2026, 13:30 UTC | `014f80c544ae` | 713 | 61 | 6 | 216 | 429 |
| 22 October 2026, 13:57 UTC | `033ba861d336` | 713 | 61 | 6 | 216 | 429 |
| 22 October 2026, 14:13 UTC | `758f08e8eb19` | 715 | 61 | 6 | 216 | 431 |
| 22 October 2026, 14:41 UTC | `51b0962ecd42` | 715 | 61 | 6 | 216 | 431 |
| 22 October 2026, 15:04 UTC | `6e65576e2003` | 715 | 61 | 6 | 216 | 431 |
| 22 October 2026, 15:28 UTC | `94b4b16db9e5` | 724 | 61 | 6 | 216 | 440 |
| 22 October 2026, 22:27 UTC | `7c1b84f732ce` | 724 | 61 | 6 | 216 | 440 |
| 22 October 2026, 22:48 UTC | `302d139b8b75` | 725 | 62 | 6 | 216 | 440 |
| 22 October 2026, 22:50 UTC | `b5b6f85fafb4` | 725 | 62 | 6 | 216 | 440 |
| 22 October 2026, 23:54 UTC | `ecad8f7dbcc8` | 725 | 62 | 6 | 216 | 440 |
| 23 October 2026, 08:50 UTC | `b6458a205421` | 726 | 63 | 6 | 216 | 440 |
| 23 October 2026, 09:34 UTC | `c3ecfc62d0aa` | 726 | 84 | 30 | 226 | 385 |
| 23 October 2026, 09:44 UTC | `bc4c0dddb9f7` | 728 | 86 | 30 | 226 | 385 |
| 23 October 2026, 10:43 UTC | `f6f57510376f` | 728 | 86 | 30 | 226 | 385 |
| 23 October 2026, 11:13 UTC | `5669ab341570` | 732 | 86 | 30 | 228 | 387 |
| 23 October 2026, 11:33 UTC | `44ee95fe19ad` | 746 | 108 | 30 | 220 | 387 |
| 23 October 2026, 11:48 UTC | `b216139f5b83` | 749 | 108 | 30 | 221 | 389 |
| 23 October 2026, 12:50 UTC | `2fdc314ded28` | 751 | 109 | 30 | 222 | 389 |

## How to read it

- **Vulnerable mostly means inherited.** 184 of the 222 vulnerable rows are applications the inventory marks *affected when deployed on an affected web-serving PHP runtime*. Their fix is patching PHP underneath them, not a release from their maker, so they stay vulnerable in the list whatever the server does. That is why only 10 row moved from vulnerable to fixed.

- **Fixes came from the people who ship PHP.** Operating systems, container images, platforms and hosting panels: the 109 fixed rows are almost all runtimes, recorded from 15:30 UTC on 21 October.

- **The investigation pile grew while it shrank.** 217 rows were resolved to vulnerable and 64 to fixed, and 82 new rows arrived under investigation.

- **The boxes in front run PHP too.** Vulnerable: **Check Point firewall web interfaces** (Check Point), **Cisco Expressway Select Series** (Cisco), **Cisco Expressway Series** (Cisco), **Cisco Ultra-Reliable Wireless Backhaul (URWB)** (Cisco), **Citrix NetScaler ADC and Citrix NetScaler Gateway** (Citrix / NetScaler), **BIG-IP APM PHP page templates** (F5), **BIG-IP TMOS platform PHP** (F5), **PAN-OS** (Palo Alto Networks), **Panorama** (Palo Alto Networks), **MyUTM portal** (Sophos). Under investigation: Cisco (10), Fortinet (5), Juniper Networks (1).

## Every change of status

| From | To | Rows |
|---|---|---|
| under investigation | vulnerable | 217 |
| added to the list | under investigation | 82 |
| under investigation | fixed | 64 |
| added to the list | fixed | 36 |
| under investigation | not affected | 27 |
| added to the list | vulnerable | 18 |
| vulnerable | fixed | 10 |
| added to the list | not affected | 3 |
| fixed | none | 1 |

Between consecutive commits, per row. A row added already fixed counts as added.

## What kind of rows they are

| What kind of row | Rows | Fixed | Not affected | Vulnerable | Under investigation |
|---|---|---|---|---|---|
| Affected because it runs on affected PHP | 184 |  |  | 184 |  |
| From a security or network vendor (matched on the supplier) | 52 |  | 26 | 10 | 16 |
| Named in a vendor advisory | 45 | 25 | 3 | 13 | 4 |
| A fixed build or release | 105 | 84 |  | 13 | 7 |
| Ships or hosts PHP itself | 73 |  |  |  | 73 |
| Runs on PHP; whether it is exposed is not yet assessed | 171 |  |  |  | 171 |
| Development, CI or admin tooling | 44 |  |  |  | 44 |
| A library: only the caller's PHP matters | 26 |  |  |  | 26 |
| Another engine, the browser, or history | 37 |  |  |  | 37 |
| Only a requirement or an SBOM says it uses PHP | 10 |  |  |  | 10 |
| No rule matched | 4 |  | 1 | 2 | 1 |

Read from each row's own *CVE assessment* line by 11 rules, applied in order; the rules are in `admin/build/inventory_history.py` and in [the data](../../data/inventory-history.json). The words matched are the inventory's; the grouping is this site's.

## When each supplier was first recorded fixed

| Recorded fixed (UTC) | Hours after release | Supplier | First product |
|---|---|---|---|
| 21 October 2026, 15:30 UTC | 1.5 | Red Hat | Red Hat Enterprise Linux 9 php:8.2 module |
| 21 October 2026, 16:03 UTC | 2.0 | Canonical / Ubuntu package maintainers | Ubuntu Noble php8.3-fpm binary package |
| 21 October 2026, 16:03 UTC | 2.0 | Debian PHP Maintainers | Debian trixie PHP 8.4 FPM package |
| 21 October 2026, 16:03 UTC | 2.0 | Docker Official Images / docker-library PHP maintainers | Docker Official PHP Apache/mod_php image variant |
| 21 October 2026, 16:03 UTC | 2.0 | Docker Official Images maintainers | Docker Official Image: php |
| 21 October 2026, 17:03 UTC | 3.0 | Arch Linux package maintainers | Arch Linux Extra PHP package |
| 21 October 2026, 17:03 UTC | 3.0 | Google Cloud | Google App Engine Standard PHP runtime |
| 21 October 2026, 17:03 UTC | 3.0 | The PHP Group | PHP LiteSpeed SAPI |
| 21 October 2026, 17:03 UTC | 3.0 | The PHP Group / Apache operators | Apache PHP module (mod_php) |
| 21 October 2026, 17:03 UTC | 3.0 | The PHP Group / PHP Windows maintainers | Official PHP Windows binary ZIP distribution |
| 21 October 2026, 17:46 UTC | 3.8 | CloudLinux / TuxCare | CloudLinux Alt-PHP 7.4 fixed package set |
| 21 October 2026, 17:46 UTC | 3.8 | TuxCare / CloudLinux | TuxCare ELS PHP package for CentOS 8.4 |
| 21 October 2026, 18:01 UTC | 4.0 | BookStack project | BookStack |
| 21 October 2026, 18:01 UTC | 4.0 | Bref project | Bref PHP Lambda runtime layers |
| 21 October 2026, 18:01 UTC | 4.0 | Gentoo PHP maintainers | Gentoo dev-lang/php runtime package family |
| 21 October 2026, 18:01 UTC | 4.0 | Heroku / Salesforce | Heroku PHP buildpack and application runtime |
| 21 October 2026, 18:01 UTC | 4.0 | Hestia Control Panel project | HestiaCP hosted-site PHP-FPM / MultiPHP option |
| 21 October 2026, 18:01 UTC | 4.0 | JBMC Software / DirectAdmin | DirectAdmin CustomBuild hosted PHP |
| 21 October 2026, 18:01 UTC | 4.0 | Kevin Papst / Kimai project | Kimai |
| 21 October 2026, 18:01 UTC | 4.0 | Passbolt SA | Passbolt API server |
| 21 October 2026, 18:01 UTC | 4.0 | Shivam Mathur / setup-php project | setup-php GitHub Action external PHP provisioning |
| 21 October 2026, 18:01 UTC | 4.0 | WebPros / cPanel | cPanel EasyApache 4 / MultiPHP |
| 21 October 2026, 18:01 UTC | 4.0 | aaPanel | aaPanel PHP Project hosting and CLI selection |
| 22 October 2026, 08:27 UTC | 18.4 | Checkmk GmbH | Checkmk Appliance |

The time the inventory recorded the fix, not the time the supplier shipped it.

## Where this comes from

a git clone; every count is from software/software_list_*.md at the commit named. Commits are content-addressed: anyone with a clone can check every number here against the commit named. The self-check: at cca173c64ec5 this parser agrees with data/software.json on all 674 rows the vault exported, status for status; it also finds 1 row the vault missed: iBabs / iBabs bestuursportaal (Not vuln). That one row is a correction to this site's earlier counts, on [corrections](../../corrections/index.html). The vault holds the inventory at one commit; the history is not yet captured into it (board).

The patching ladder, version by version, is on [Patching](../index.html); the signals this belongs to are on [The second stories](../../signals/index.html).


---
site v0.15.15 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/patching/inventory/index.html
