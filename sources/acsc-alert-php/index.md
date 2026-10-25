# Source: Critical vulnerabilities in PHP

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

ASD's ACSC (Australia): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# Critical vulnerabilities in PHP

**ASD's ACSC (Australia)** · [https://www.cyber.gov.au/alert/critical-vulnerabilities-in-php](https://www.cyber.gov.au/alert/critical-vulnerabilities-in-php) · published 2026-10-21 (Published); Last reviewed 2026-10-22 · added by `collector-gov` · slug `acsc-alert-php`

Alert Status: Critical. Published 21 Oct 2026, last reviewed 22 Oct 2026. 'Recent update': identify PHP, review php.net, apply updates and mitigations, monitor. NO offline advice. 'not aware of successful active exploitation within Australia'. Says full details were announced 'Thursday 22 October 2026 at 0100 AEDT' (=21 Oct 14:00Z). The body text is stale (pre-patch).

## What it says, as the collector read it

#### ASD's ACSC alert: Critical vulnerabilities in PHP

- Site title "CGA". Plain curl to cyber.gov.au timed out from this egress, but Playwright got 200.

- "Alert Status: Critical". "Published 21 Oct 2026". "Last reviewed 22 Oct 2026". Captured 2026-10-22T08:16:58Z.

- Recent update (verbatim): "Patches have been released ... ASD's ACSC recommends organisations: - Identify PHP within their environments - Review the latest PHP guidance at https://www.php.net/index.php - Apply available security updates and other appropriate mitigations - Monitor PHP applications and related systems for suspicious activity."

- The older body text is still pre-patch: "Prepare to update and apply security patches as they become available." It also says "full details publicly announced on Thursday 22 October 2026 at 0100 AEDT" (= 2026-10-21T14:00Z). The summary line still reads "is set for public disclosure on 22 October 2026."

- "ASD’s ACSC is not aware of successful active exploitation within Australia".

- **No take-offline or isolation advice.** This contradicts the BBC framing that the Australian counterpart issued advice like the NCSC/NSA. The ACSC advice is patch, mitigate and monitor.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | **A1** Weak signal●○○○○○ | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |

## Events that cite it

No timeline event cites this source yet.

### Agency rows from this source
- [ASD's ACSC](../../agencies/index.html): offline none

### Exploitation signals from this source
- [2026-10-22](../../exploitation/index.html): 'not aware of successful active exploitation within Australia'.

## The bytes
capture 20261022T081658Z · HTTP 200 · https://www.cyber.gov.au/alert/critical-vulnerabilities-in-php- `headers.json` 3f7c0fe9c702d22193630225a56b0991c08fc52fb05ef53f26ea0f611b798b4e 1,985 bytes
- `page.html` 650742fe93abb6dec911f58d21b7cd6d8d82c2d4a7b89eb9745e9a9857bc0c72 1,541,271 bytes
- `provenance.json` 37ce725a8459c6db87ef8d7e3abd3cf92d350bab9e4228852c7d07dd08d65a6f 985 bytes
- `rendered.html` 731eef8ce851ccf1650bc66cf3bb8658569c3de13b3a8084c14761658743e931 1,557,700 bytes
- `screenshot.png` 39318847477c383a130dbafc83210dc27ed7ccae88107979ed124e372d67da9d 345,966 bytes
- `text.txt` 9370af142ded6de9a44fed4330585d677fde367d90d33ce355e9ebe6a75f7d56 6,299 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/acsc-alert-php/index.html
