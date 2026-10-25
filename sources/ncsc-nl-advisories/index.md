# Source: NCSC NL | Security Advisories (PHP banner: Ernstige kwetsbaarheden in PHP: bereid je voor op patchen)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

NCSC-NL: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# NCSC NL | Security Advisories (PHP banner: Ernstige kwetsbaarheden in PHP: bereid je voor op patchen)

**NCSC-NL** · [https://advisories.ncsc.nl/advisories](https://advisories.ncsc.nl/advisories) · published not stated · added by `collector-gov` · slug `ncsc-nl-advisories`

Final URL advisories.ncsc.nl/. A banner is still the pre-patch text: 'bereid je voor op patchen', patch expected '21 oktober 16:00 Nederlandse tijd'; 'Er is een publieke Proof of Concept (PoC)- code beschikbaar, maar het NCSC heeft nog geen actief misbruik gesignaleerd.' Affects 'alle versies vanaf versie 5'.

## What it says, as the collector read it

#### NCSC-NL advisories portal (PHP banner)

Captured 08:16Z. The PHP banner is still the pre-patch version: "Ernstige kwetsbaarheden in PHP: bereid je voor op patchen" (serious PHP flaws: prepare to patch). It advises preparing for "een komende patch op 21 oktober 16:00 Nederlandse tijd" (=14:00Z) and says "Dit tijdstip kan eventueel worden vervroegd" (that time may be brought forward). It says a public PoC exists but NCSC-NL has seen no active abuse ("nog geen actief misbruik gesignaleerd"). It names WordPress, Joomla, Drupal, Zabbix and Roundcube as PHP-based. ENISA CNW quotes this text. No offline advice was seen in the captured part. We did not identify the individual NCSC-2026-xxxx advisory URL.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. [fact timeline →](../../facts/versions-old/index.html) | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | **A3** Echoed●●●○○○ disputed | 3/4 | [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |

## Events that cite it

No timeline event cites this source yet.

### Agency rows from this source
- [NCSC-NL](../../agencies/index.html): offline none

## The bytes
capture 20261022T081605Z · HTTP 200 · https://advisories.ncsc.nl/- `headers.json` 3e389f62cb8a1de496ebc873bbcfb98ccf729f22e1ec56c94d0893bba1bef324 884 bytes
- `page.html` c0c4e5aa82e2eaec26497f7eb201c72888ecdcb1361964f73aab7b5dcc046c5f 240 bytes
- `provenance.json` cd3655ebd5a05e5e7a94cfc0438e17c9f78418f1c570bf5097613f30ba7612ca 980 bytes
- `rendered.html` f008b1f5da4c00459105f979db89eebc16702be90d3a6de1656acfab41951cc6 69,813 bytes
- `screenshot.png` 9bd5b7a047aff8b7f81e8c61b6f1ccc1475f7be1ad89a7d9d32a6f2aee84abbe 611,099 bytes
- `text.txt` b7e4ac6caf7d177d8b7e55fa8c587da75a1e78fafc951012d2d2595a6dfa5e8b 8,130 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/ncsc-nl-advisories/index.html
