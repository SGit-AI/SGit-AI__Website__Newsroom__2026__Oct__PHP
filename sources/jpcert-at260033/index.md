# Source: PHPにおける複数の脆弱性（CVE-2026-109618、CVE-2026-109619）に関する注意喚起 (JPCERT-AT-2026-0033)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

JPCERT/CC (Japan): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# PHPにおける複数の脆弱性（CVE-2026-109618、CVE-2026-109619）に関する注意喚起 (JPCERT-AT-2026-0033)

**JPCERT/CC (Japan)** · [https://www.jpcert.or.jp/at/2026/at260033.html](https://www.jpcert.or.jp/at/2026/at260033.html) · published 2026-10-22 · added by `collector-gov` · slug `jpcert-at260033`

JPCERT-AT-2026-0033, published 2026-10-22, updated 2026-10-22 (wording fix in section V). Advice: apply fixed versions promptly 'after sufficient testing' and investigate for compromise. No offline advice. Says PHP is widely used in Japan. JVN entry also listed 2026-10-22 14:20 JST.

## What it says, as the collector read it

#### JPCERT/CC alert JPCERT-AT-2026-0033

- "2026-10-22（公開）"; "2026-10-22（更新）". Revision log: "2026-10-22 「V. 侵害調査」の一部の表現を修正" (a wording fix in the compromise-investigation section). Captured 2026-10-22T08:17:00Z. The JPCERT home page (`jpcert-home`) also lists a JVN entry at "2026-10-22 14:20" JST (=05:20Z).

- Advice (JA, verbatim): "速やかに対策の適用および侵害有無の調査を実施してください" (apply countermeasures promptly and investigate whether you have been compromised). Also: "十分なテストを実施の上、速やかに修正済みバージョンを適用してください" (after sufficient testing, apply the fixed version promptly). Upgrade from 8.1 and older is recommended.

- No offline advice. JPCERT also warns that there are several exploit paths, so one detection rule may miss attacks, and a lack of traces does not prove no compromise.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasibleAustralia's ACSC gives no offline advice. CERT-EU says isolate. The Netherlands, Italy, Japan and New Zealand give no offline advice. [fact timeline →](../../facts/offline-allies/index.html) | BBC | contradicted | **A1** Weak signal●○○○○○ | 4/6 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [ACSC](../../sources/acsc-alert-php/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [NCSC-NL](../../sources/ncsc-nl-php2shell/index.html) [ACN / CSIRT Italia](../../sources/acn-it-php2shell/index.html) [JPCERT/CC](../../sources/jpcert-at260033/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-22 05:20 UTC | JVN publishes its note (14:20 JST); JPCERT/CC alert JPCERT-AT-2026-0033 is dated 22 October. | stated |

### Agency rows from this source
- [JPCERT/CC](../../agencies/index.html): offline none

## The bytes
capture 20261022T081700Z · HTTP 200 · https://www.jpcert.or.jp/at/2026/at260033.html- `headers.json` cbc1e287bde3882e41d91bfa7315dcbaccf9a996c0a383acc62f9095fbe921eb 605 bytes
- `page.html` 85db7a09e865158643525fef5aa5cfc69513aaf896fcb2da4562189d43decf44 31,008 bytes
- `provenance.json` 4ba4d01fa5ebe5235184ed530cedbac6cd8985446a10845775da38efa45aa5b9 1,013 bytes
- `rendered.html` c4ba52d8393f4189aade005389d1b8c2923eeb29f0d917a7221b5330cff3bf91 30,690 bytes
- `screenshot.png` 99789e60674ab7b0d3f01afbc2012337348a1434417d4820d6c89133f2d6ff64 722,717 bytes
- `text.txt` 1fea87241b307f92c5ddc2b16356954d947ec3e0f5ad55158315dc08d98127f5 8,327 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/jpcert-at260033/index.html
