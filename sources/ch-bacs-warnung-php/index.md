# Source: Critical vulnerabilities in PHP: Install security updates immediately

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Swiss Federal Office for Cyber Security (BACS / NCSC): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Critical vulnerabilities in PHP: Install security updates immediately

**Swiss Federal Office for Cyber Security (BACS / NCSC)** · [https://www.bacs.admin.ch/en/warnung-php-en](https://www.bacs.admin.ch/en/warnung-php-en) · published 2026-10-21 · added by `collector-gov` · slug `ch-bacs-warnung-php`

Published on 21 October 2026 (the home page teaser shows 20 October 2026). 'If an immediate update is not possible': restrict access; 'Check, particularly for critical applications, whether a temporary disconnection from the internet or taking the system offline is necessary.' Says a WAF alone is not sufficient.

## What it says, as the collector read it

#### Swiss BACS (NCSC) warning

- ncsc.admin.ch now redirects to bacs.admin.ch. The page says "Published on 21 October 2026", but the home-page teaser (`ch-ncsc-home`) is dated "20 October 2026", so the page was probably first posted on the 20th (pre-announcement) and rewritten after the patch. Captured 2026-10-22T08:17:00Z.

- Verbatim: "Install updates immediately"; "After the update, restart the affected PHP services ... Containers may need to be rebuilt"; "If an immediate update is not possible: Where possible, restrict access to the affected applications to only those people and systems that actually require it. Check, particularly for critical applications, whether a temporary disconnection from the internet or taking the system offline is necessary."; "Even a web application firewall alone is not sufficient." (This contrasts with CISA: "A web application firewall may provide some protection".)

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| A web application firewall may provide some protection until systems are patchedSwiss BACS: 'Even a web application firewall alone is not sufficient.' Cloudflare says its rules blocked the traffic it saw and that attackers mutated payloads to get past them. [fact timeline →](../../facts/waf/index.html) | CISA | disputed | **A6** Established●●●●●● | 3/3 | [CISA](../../sources/cisa-alert-php-20261021/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-20 | Swiss BACS posts a warning (home-page teaser dated 20 October; the page itself now says 21 October). | inferred |

### Agency rows from this source
- [BACS (NCSC)](../../agencies/index.html): offline consider

## The bytes
capture 20261022T081700Z · HTTP 200 · https://www.bacs.admin.ch/en/warnung-php-en- `headers.json` 603765d5dfe2bc360d0d8becb67c71a6a5810ad02fbe68f5d677488189ac7317 6,406 bytes
- `page.html` bdef753f8a5972cd0d5af92574637f8edd425df0511ef469bf2c11ee39207e0f 160,186 bytes
- `provenance.json` 1574e8470bf5e04e0a830d2ee1ffd4d728872599f3828cba3399f0b095066f39 984 bytes
- `rendered.html` 7400fa0917a78b8192f819815d7bddbc76a93e9ddb57e9ce574cb60b713b4e0b 174,883 bytes
- `screenshot.png` b14b81a2939d7eafc4abdd581e6591629c66d8728ce4402a2c68421d788a9f63 846,454 bytes
- `text.txt` 99886a19aead8abe4faab9f41918c8654a2e070c816f856c0dd3e14a194d6890 4,966 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/ch-bacs-warnung-php/index.html
