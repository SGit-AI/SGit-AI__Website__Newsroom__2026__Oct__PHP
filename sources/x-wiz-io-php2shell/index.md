# Source: Wiz on X: BREAKING ... #PHP2SHELL ... impacting 70% of the Internet

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Wiz (@wiz_io): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · social · primary · captured

# Wiz on X: BREAKING ... #PHP2SHELL ... impacting 70% of the Internet

**Wiz (@wiz_io)** · [https://x.com/wiz_io/status/2112899813264277528](https://x.com/wiz_io/status/2112899813264277528) · published 2026-10-21T13:32Z · added by `collector-researchers` · slug `x-wiz-io-php2shell`

Shown '13:32 · 21 Oct 2026' (UTC in capture browser) — 28 min before the 14:00 UTC release. Thread says 'Apply the Oct 22 security release immediately' — stale date from the original schedule.

## What it says, as the collector read it

#### Wiz on X: "#PHP2SHELL ... impacting 70% of the Internet"

- Verbatim: "🚨 BREAKING: @wiz_io Research uncovers #PHP2SHELL, a decade-old PHP Core vulnerability reaching CVSS 9.2 severity impacting 70% of the Internet." Shown 13:32 · 21 Oct 2026 (UTC), i.e. before the 14:00 UTC release.

- "Wiz Research uncovers" framing: no credit to Calif or OpenAI in the lead post (the blog thanks them).

- Thread: "All php versions >= 5.4 are affected by at least 1 of these vulnerabilities." "Confirmed pre-auth RCE on representative targets: WordPress, Drupal, and Joomla". "Patch: Apply the Oct 22 security release immediately" — wrong date (the release moved to Oct 21), so the thread was probably drafted before the leak moved the date.

- 70% here is "of the Internet"; Wiz's blog body and Cloudflare/OpenAI say "of websites".

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. [fact timeline →](../../facts/versions-old/index.html) | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | **A3** Echoed●●●○○○ disputed | 3/4 | [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| 70% of the Internet is affectedThe BBC was 'unable to independently verify that figure'. Wiz's body text says 70% of websites and cites no measurement. [fact timeline →](../../facts/scale-70pc-internet/index.html) | Wiz (headline, X post); the BBC, which reports it as Wiz's 'roughly 70%' | unverified | **A1** Weak signal●○○○○○ measures differently | 2/3 | [Wiz](../../sources/wiz-blog-php2shell/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leakThe php.net ChangeLog still dates all four releases 22 October. Wiz's X thread still says 22 October. [fact timeline →](../../facts/release-moved/index.html) | PHP Foundation; php.net pre-announcement; Wiz thread ('Apply the Oct 22 security release') | confirmed | **A4** Corroborated●●●●○○ measures differently status overstated | 4/4 | [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [php.net](../../sources/php-net-changelog-8/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 13:32 UTC | Wiz posts 'BREAKING ... #PHP2SHELL ... impacting 70% of the Internet', 28 minutes before the planned release; the thread still says 'Apply the Oct 22 security release'. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| 70% | the Internet | unverified |

## The bytes
capture 20261022T081624Z · HTTP 200 · https://x.com/wiz_io/status/2112899813264277528- `headers.json` f9a8ec8c80b7e7b13a6e772a718ece30ec0796dffd3481acc57a310616eca249 9,022 bytes
- `page.html` 6adc23abb012a9e89f22453d2d8d4f0eff574edc67373bc94eef59cfc12ebe85 183,867 bytes
- `provenance.json` 5df6949985ad1cf4a150d5b9a7e52f1355bac3b127484b31c70c8052986b1556 1,086 bytes
- `rendered.html` 9c5f87ac8afbe6aad1205a23ecbe79d83dc801c77f4d0ffb750ffb5b53625888 193,354 bytes
- `screenshot.png` d2187dc09d49ec23ea5593aa7ffef5df60cd2385f290922ec6d77b6861fc7abb 578,314 bytes
- `text.txt` 6c17977662815b0cb25a32e0987d1b1f95942156825b0cc616dc43a3f7f46809 2,222 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/x-wiz-io-php2shell/index.html
