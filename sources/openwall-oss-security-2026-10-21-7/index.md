# Source: CVE-2026-109619: PHP 8.2–8.5 RCE via stale global state

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

oss-security list (Jakub Zelenka, PHP security team): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# CVE-2026-109619: PHP 8.2–8.5 RCE via stale global state

**oss-security list (Jakub Zelenka, PHP security team)** · [https://www.openwall.com/lists/oss-security/2026/10/21/7](https://www.openwall.com/lists/oss-security/2026/10/21/7) · published 2026-10-21T14:44:06Z · added by `collector-primary` · slug `openwall-oss-security-2026-10-21-7`

Date header Wed, 21 Oct 2026 16:44:06 +0200. Replies at 21/16, 21/17, 21/23, 22/2 are in openwall-oss-security-109619-thread.

## What it says, as the collector read it

#### oss-security 2026/10/21/7: notes

- From Jakub Zelenka. Date 21 Oct 2026 16:44:06 +0200 = 14:44:06Z. (A reply at 21/16 quotes it as sent "10:11 AM" -0500 = 15:11Z. The quoted time does not match the Date header; it may be the reply client's own receive or display time.)

- Verbatim: "CVE: CVE-2026-109619 / Severity: Critical (CVSS v4.0: 9.2)", same affected ranges.

- "Unauthenticated RCE has been demonstrated against Apache mod_php and PHP-FPM. Exploitability depends on the affected state, configuration, and application behavior."

- "Updating is the only reliable mitigation; there is no complete generic configuration workaround."

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do not make an installation safe [fact timeline →](../../facts/only-update/index.html) | php.net; PHP security team | confirmed | **A6** Established●●●●●● | 3/3 | [php.net](../../sources/php-net-advisory/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-21-7/index.html) [PHP](../../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 14:41:54 UTC | Jakub Zelenka announces CVE-2026-109618 on oss-security; CVE-2026-109619 at 14:44:06Z. | stated |

## The bytes
capture 20261022T081407Z · HTTP 200 · https://www.openwall.com/lists/oss-security/2026/10/21/7- `headers.json` ffb76440772a63ed2186c00ea575b6e673ca3c7222ae89205c2bbb9de07e38ae 239 bytes
- `page.html` 81caae4759a5e9cd8e501221e12f31928874e9d16d7f7e8523e8cb1d36aa69fd 6,323 bytes
- `provenance.json` deeabe8cb21005c2d60c6ffcca6537969877e4411a8d1bbc88503109265756ce 1,028 bytes
- `rendered.html` b797761c288a2b59dad8b9bf3c0f4810af1b669a685b93013a7d6edc0e688638 6,579 bytes
- `screenshot.png` d6c5ab360073ebc5769973dc76493c74acf62cdc6e099f668ebffae91de551fa 154,322 bytes
- `text.txt` ceef70b4943f78182c26af1c04cdac8a7986a9c2c5f5cbb5385a73efdd112384 1,934 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/openwall-oss-security-2026-10-21-7/index.html
