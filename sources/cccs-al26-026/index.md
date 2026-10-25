# Source: AL26-026 - Critical vulnerabilities impacting PHP - CVE-2026-109618 and CVE-2026-109619

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Canadian Centre for Cyber Security (CCCS): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# AL26-026 - Critical vulnerabilities impacting PHP - CVE-2026-109618 and CVE-2026-109619

**Canadian Centre for Cyber Security (CCCS)** · [https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619](https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619) · published 2026-10-21 · added by `collector-gov` · slug `cccs-al26-026`

Date: October 21, 2026; Date modified 2026-10-21. 'Where immediate remediation is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix can be applied.' PoC available; no active exploitation identified. Also AV26-1070 (PHP security advisory), same date.

## What it says, as the collector read it

#### CCCS AL26-026

- "Date: October 21, 2026"; "Date modified: 2026-10-21". Captured 2026-10-22T08:17:00Z. The alerts listing (`cccs-alerts`) also shows AV26-1070 "PHP security advisory", 2026-10-21. (The listing table labels AL26-026 as "AV26-026", a typo on the page.)

- Verbatim: "Organizations should identify affected systems and apply the appropriate updates immediately." / "Update affected PHP installations immediately to a fixed, supported release." / "Where immediate remediation is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix can be applied."

- Note: the CCCS sentence "Where immediate remediation is not feasible, organisations should consider ..." matches the opening of the sentence the BBC attributes to the UK NCSC. The wording is shared across Five Eyes and CERT-EU text (CERT-EU: "Where that is not feasible, organisations should consider isolating...").

- Exploitation: "a Proof of Concept (PoC) is available, with no active exploitation being identified at this time, but that can change quickly."

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| 'Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'That sentence is not on the NCSC page as captured at 08:09Z on 22 October. The page's offline advice is step 4 of 6 and is worded differently. The page was modified at 07:30Z that morning. The sentence's opening matches the Canadian CCCS text. [fact timeline →](../../facts/offline-ncsc/index.html) | UK NCSC, as quoted by the BBC | disputed | **A2** Reported●●○○○○ disputed | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html) [CCCS](../../sources/cccs-al26-026/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

### Agency rows from this source
- [CCCS](../../agencies/index.html): offline isolate

### Exploitation signals from this source
- [2026-10-21](../../exploitation/index.html): 'a Proof of Concept (PoC) is available, with no active exploitation being identified at this time, but that can change quickly.'

## The bytes
capture 20261022T081700Z · HTTP 200 · https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619- `headers.json` 0db6dd151e1887553a32a56de4d1f6a133645e87d6dbee931f362e8a21a370f3 583 bytes
- `page.html` 171c897e4a6fde98e73f9d1e221188dae6d0c04b49e8b6a242fba591739a11c9 39,250 bytes
- `provenance.json` 9759aec757d5df865a795a86bf304ffdcc697988c45f47adcc0159a6771a4fa1 1,195 bytes
- `rendered.html` d6536d39602e9709a1afb05fb61fad1b88b57a5d1b839a7f5de58c7f3588300c 149,258 bytes
- `screenshot.png` 9df75da37b7ed8ceb13b241f71f041d29c9f33055750a65070c6c785bbe9cdd2 538,343 bytes
- `text.txt` 9e7f44cc73e21ad54d1caf36c5273a289839c76ff1e1ac35bf377e4645ad91a2 5,403 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/cccs-al26-026/index.html
