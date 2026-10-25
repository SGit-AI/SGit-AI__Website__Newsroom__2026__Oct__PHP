# Source: Critical security issue affecting PHP

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

UK National Cyber Security Centre (NCSC): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Critical security issue affecting PHP

**UK National Cyber Security Centre (NCSC)** · [https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php) · published 2026-10-21 · added by `collector-gov` · slug `ncsc-news-php`

NCSC Alert. Page: PUBLISHED 21 October 2026; JSON-LD dateModified 2026-10-22; HTTP last-modified Thu, 22 Oct 2026 07:30:02 GMT. Names CVE-2026-109618 and CVE-2026-109619. Advice: update; else PHP Foundation temporary mitigations; 'If you are unable to apply the temporary mitigations, or applying them would take too long, you should consider taking the system offline until it can be fully mitigated.' Wording differs from BBC's quote.

## What it says, as the collector read it

#### NCSC (UK) alert: Critical security issue affecting PHP

- URL: https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php (NEWS TYPE: Alert)

- Stated: "PUBLISHED 21 October 2026". JSON-LD `datePublished` 2026-10-21, `dateModified` 2026-10-22. HTTP `last-modified: Thu, 22 Oct 2026 07:30:02 GMT`. The NCSC all-feed RSS lists it as `Wed, 21 Oct 2026 12:00:00 +0000`, but every item in that feed is 12:00, so the time is a placeholder and only the date counts.

- Captured 2026-10-22T08:09Z (capture 20261022T080903Z).

- CVEs named: CVE-2026-109618 and CVE-2026-109619. Links to GHSA-6wmf-4rv5-p3rp and GHSA-w8hw-w9fx-j79w (php/php-src), and to NCSC-NL's php2shell repo (https://github.com/NCSC-NL/php2shell).

#### Exact advice (priority actions, verbatim)

1. "Identify systems running PHP across your infrastructure, prioritising internet-facing systems. As all versions may be affected, do not limit discovery to outdated PHP versions..."

2. "Update to the latest version of PHP and continue to monitor for future updates."

3. "If you are unable to update to a version with the security update applied, the PHP Foundation have provided temporary mitigations."

4. "If you are unable to apply the temporary mitigations, or applying them would take too long, you should consider taking the system offline until it can be fully mitigated."

5. "If you are unable to update or disable the system immediately then you should assess the system for any evidence of compromise ... and look for backdoors installed by an attacker."

6. Monitor third-party vendors that bundle PHP; points to the NCSC-NL inventory.

#### Oddities

- The BBC live page quotes the NCSC as saying "Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated." That sentence is NOT on the page as captured at 08:09Z. The page carries the offline advice as step 4 (quoted above). The page was modified on 22 Oct (last-modified 07:30:02 GMT), so the BBC may have quoted an earlier version, or a different NCSC note. Open question: find an earlier copy (Wayback?).

- "Organisations using any version of PHP are affected".

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. [fact timeline →](../../facts/offline-ncsc/index.html) | UK NCSC, as quoted by the BBC | disputed | **A2** Reported●●○○○○ disputed | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [CCCS](../../sources/cccs-al26-026/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |
| 2026-10-22 07:30:02 UTC | The UK NCSC page is modified (HTTP last-modified). | stated |

### Agency rows from this source
- [NCSC](../../agencies/index.html): offline after mitigations

## The bytes
capture 20261022T080903Z · HTTP 200 · https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php- `headers.json` 642ad2462903a32f7050dae5e198654e710dadc0a6225333d96370031c7ede4c 852 bytes
- `page.html` 2d8e9e72ec5efa695b2d587a4af1bcb75662ead0add90b964cf767e8023ff4f8 225,168 bytes
- `provenance.json` fe3daad10ed2709f256ce5547b2a21d8b35120fe041248d698a63d75652a19fb 1,025 bytes
- `rendered.html` 0b839c8974dc2310cc6f85d334620ae5b5cd944842d6de180bf76938f5b6dcf5 761,056 bytes
- `screenshot.png` 260b9c91a3bf1a838fd1a81633415032eacd24ccaf249c11227903c6038b4544 542,775 bytes
- `text.txt` a18ceeb011a3fe6f0311d92399618b5231abb0f57f3b94ffd7371cab6eccc339 5,135 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/ncsc-news-php/index.html
