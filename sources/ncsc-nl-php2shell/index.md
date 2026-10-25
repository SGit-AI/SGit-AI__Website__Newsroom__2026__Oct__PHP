# Source: NCSC-NL/php2shell: Operational information regarding the 2026 php2shell vulnerabilities

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

NCSC-NL (Netherlands National Cyber Security Centre): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# NCSC-NL/php2shell: Operational information regarding the 2026 php2shell vulnerabilities

**NCSC-NL (Netherlands National Cyber Security Centre)** · [https://github.com/NCSC-NL/php2shell](https://github.com/NCSC-NL/php2shell) · published 2026-10-21T15:25:00Z · added by `collector-gov` · slug `ncsc-nl-php2shell`

README: 'Readme last significant change: 21 October 2026 17:25 CEST TLP:CLEAR' (=15:25Z). Fixed releases: PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35. Links to CERT-EU SA 2026-018 and ENISA CNW-2026-04. Holds the software inventory list (the NCSC UK cites it). Does NOT advise taking systems offline.

## What it says, as the collector read it

#### NCSC-NL php2shell GitHub repository

- https://github.com/NCSC-NL/php2shell (EUPL-1.2). At the 08:09Z capture: 145 stars, 40 forks, 6 contributors.

- "Readme last significant change: 21 October 2026 17:25 CEST TLP:CLEAR"

- It says the CVEs are "tracked by CERT-EU as CVE-2026-109618 and CVE-2026-109619".

- Fixed releases: "PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35". Source backports for 7.4, 8.0 and 8.1. Affected SAPIs: PHP-FPM, Apache mod_php, php-cgi, FrankenPHP, LiteSpeed, with the "risk highest for mod_php".

- Recommended actions (verbatim): "Identify PHP-based applications and their runtime versions..."; "Update to PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35, or apply vendor-provided backported packages."; "If immediate patching is not possible, follow PHP's temporary mitigations, including disabling session.upload_progress, restarting workers, and reviewing the official memory_limit, post_max_size and PHP 8.5 fatal_error_backtraces guidance. PHP states that these measures are not complete fixes."

- NCSC-NL does NOT advise taking systems offline, which sets it apart from the NCSC (UK) and the NSA.

- Links: CERT-EU SA 2026-018, ENISA CNW advisories/2026/CNW-2026-04_php.md, and php.net archive #2026-10-21-5.

#### Added by claude-newsroom-lead, 2026-10-22T08:48Z (the editor pointed to this repo for affected systems)

- `raw/php2shell-cca173c64ec5.bundle`: a git bundle of the whole repository, all refs, with 52 commits (`git clone php2shell-cca173c64ec5.bundle`). HEAD is cca173c64ec5db9211fcbd0fcf3a57c22cfbc2fb, committed 2026-10-22T10:40:58+02:00 (the merge of PR #10).

- `raw/tree-cca173c64ec5/`: the files at that commit. `raw/commits-cca173c64ec5.txt`: the log.

- `raw/software-list-cca173c64ec5.json`: software/software_list_*.md parsed into rows (supplier, product, version, a status per CVE, notes, links). 674 entries: 206 Vulnerable, 46 Fix, 418 Investigation, 3 Not vuln, and 1 runtime anchor with no status. The list is generated from software/spdx/PHP_Downstream_Inventory.spdx3.json (VEX). NCSC-NL says entries are "investigation leads" until a vendor or upstream source backs them.

- The README calls the CVEs CVE-2026-109618 and CVE-2026-109619. The repo holds cPanel detection and mitigation (detection_mitigation/cpanel/php2shell-mitigate.sh).

- Licence EUPL-1.2.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | **A1** Weak signal●○○○○○ | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 15:25 UTC | NCSC-NL's php2shell README last significant change (17:25 CEST). CERT.LV publishes: Latvia restricts access to several state digital resources from abroad (18:25 EEST). | stated |
| 2026-10-22 08:40:58 UTC | NCSC-NL merges pull request 10; the inventory has 674 entries at commit cca173c64ec5. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 674 | software entries in the NCSC-NL php2shell inventory | confirmed |

### Agency rows from this source
- [NCSC-NL](../../agencies/index.html): offline none

## The bytes
capture 20261022T080925Z · HTTP 200 · https://github.com/NCSC-NL/php2shell- `headers.json` dbef75c6f088a0a21eeac77ab2178aead9e625d6ed750dd4894fc7fb9537f297 5,443 bytes
- `page.html` 4e1f8dc6dd2c6d494b9d1229a0de601b0e1096e81337d8a4b5b06fa7c3c293ce 261,528 bytes
- `provenance.json` 939b683f13402c1f5d315ff79800619b30e3780d4eb31bfc2b17282148c8e03a 1,005 bytes
- `rendered.html` 323e0a19a3dd13c2b214ff7b1a8553eacac4c17bdfb8b8c1a9bf2032781934db 273,849 bytes
- `screenshot.png` a27d227bafcdfbc38ca5c431a5fb525aa95eeac6e7bfbe31c98ae8057c2e4d64 494,937 bytes
- `text.txt` 8944dd45c25fa7c1fc1c6f3e2a646d86fe0849a83248fe1f91cec791a58589e6 4,852 bytes
capture 20261022T084815Z · HTTP 200 · https://github.com/NCSC-NL/php2shell- `headers.json` dc374a245415e7981501c8d9adea6d18ac20101116a21380bafe62b351dba7c0 5,453 bytes
- `page.html` 556efff0dd62f6bdf88e3ed5566f6f2213e828b2bbfeba7eef0b3cd3ac622057 261,276 bytes
- `provenance.json` 7544f40915d6c5cb74cdc60621deee2e3d7773de3a0191201caf4089fbd5d094 1,005 bytes
- `rendered.html` 42194f5b28315e862789c25ed7c3a2bbbfa3244da3bb68e8e3ff284f321ccd38 275,802 bytes
- `screenshot.png` c6a14bc8234e3b2b5692240e1f2821e9e80e51e52bd5bec2e89dcf3a7a8a1764 497,834 bytes
- `text.txt` f3eec24a226910fb8440714b4f44c40db5c5f7826f3c23b65aece1cc5775712e 4,854 bytes
raw, 3 files with SHA256SUMS- `commits-cca173c64ec5.txt` 4d4f80bd9da0076e2bd74323e947a05f1e0f1a246a5a25b2874dd9370b4a2ea9
- `php2shell-cca173c64ec5.bundle` 4a72bcc9bbc58e886df6eee7cc875bd5deab547f1028f7525a7e7e808859411f
- `software-list-cca173c64ec5.json` f0a17e96a336a8782231290acf4ba4a4f4fa469270c59a7c87a95da2207dad01

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/ncsc-nl-php2shell/index.html
