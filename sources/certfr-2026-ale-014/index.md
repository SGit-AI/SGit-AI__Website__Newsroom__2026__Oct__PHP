# Source: [Màj] Multiples vulnérabilités dans PHP (CERTFR-2026-ALE-014)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

CERT-FR (ANSSI): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · advisory · primary · captured

# [Màj] Multiples vulnérabilités dans PHP (CERTFR-2026-ALE-014)

**CERT-FR (ANSSI)** · [https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/) · published 2026-10-21 · added by `collector-gov` · slug `certfr-2026-ale-014`

First and last version 21 Oct 2026. 'Le CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue...'. Affected: all 5.x, 6.x, 7.x, 8.0, 8.1, and 8.2-8.5 below the fixed versions. Workarounds: session.upload_progress off; block multipart Content-Type at WAF.

## What it says, as the collector read it

#### CERT-FR alert CERTFR-2026-ALE-014: [Màj] Multiples vulnérabilités dans PHP

- New domain: cert.cyber.gouv.fr (the old www.cert.ssi.gouv.fr redirects with a 302).

- "Date de la première version 21 octobre 2026"; "Date de la dernière version 21 octobre 2026". Two versions: the initial one, then "Mises à jour des risques, des systèmes affectés et ajout des correctifs de sécurité".

- Captured 2026-10-22T08:13:53Z.

- Key lines (verbatim, French):

- "L'éditeur annonce la disponibilité des correctifs de sécurité pour le 21 octobre 2026 à 16h00 heure de Paris (14h00 UTC)." (This is PHP's pre-announced time; CERT-EU says the fixes came out at 13:30 UTC.)

- Advice: "Le CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue et avec les derniers correctifs de sécurité dès publication du correctif éditeur." In English: CERT-FR recommends isolating affected equipment, then migrating to a maintained, patched version once the vendor fix is out.

- Workarounds "non qualifiés par le CERT-FR": session.upload_progress.enabled = Off (plus php_admin_flag for FPM); "bloquer toutes requêtes HTTP dont l'en-tête contient un Content-Type positionné à la valeur multipart", or failing that, monitor such requests; can be done at a WAF.

- Affected: "PHP toutes versions 5.x, 6.x, 7.x, 8.0.x, 8.1.x" plus 8.2 to 8.5 below the fixed versions.

- Also references CERTFR-2026-AVI-1359 and the reflex sheet CERTFR-2025-RFX-002 (edge-device compromise containment).

- Of all the agencies, CERT-FR's advice is the closest to "isolate first": isolate, THEN migrate.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. [fact timeline →](../../facts/versions-old/index.html) | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | **A3** Echoed●●●○○○ disputed | 3/4 | [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| The fixes were released at 14:00 UTC on 21 OctoberCERT-EU says 13:30 UTC; the tags and advisories are stamped 13:34 to 13:35 UTC; the GitHub release 14:06 UTC; the php.net feed entries carry 00:05 to 00:35 UTC, which are authoring times, not publication times. [fact timeline →](../../facts/release-time/index.html) | php.net pre-announcement; Daubois; CERT-FR (16:00 Paris) | disputed | **A2** Reported●●○○○○ disputed | 7/8 | [oss-security](../../sources/openwall-oss-security-2026-10-20-34/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [CERT-EU](../../sources/certeu-sa-2026-018/index.html) [php-src](../../sources/github-php-src-tags/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [php-src](../../sources/github-php-src-tag-php-8.5.12/index.html) [php.net](../../sources/php-net-advisory/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | CISA alert 'Critical Vulnerabilities in PHP Require Immediate Patching': take systems offline if you cannot update. NSA press release 'PHP2Shell'. UK NCSC alert. CCCS AL26-026. CERT-FR ALE-014. ACN AL07/261021. Cloudflare, Wiz, Calif, the PHP Foundation and Daubois publish their accounts. | stated |

### Agency rows from this source
- [CERT-FR (ANSSI)](../../agencies/index.html): offline isolate first

## The bytes
capture 20261022T081353Z · HTTP 200 · https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/- `headers.json` 96a5cd42d4ca38099fc910e8c06f10cfd15f15e6ca7bebdb699b3b7245d08d58 1,075 bytes
- `page.html` 91f474e2f0f414b2d8575b91cecd59d880e62f0179033baae665177100fc094a 26,782 bytes
- `provenance.json` 53ea7bfd63a634427908cc6846e7e974b45c9cdc7028b88d7e87d148408ecd59 989 bytes
- `rendered.html` f71933fcd112f86a98d8838cc53fa38dabffe5f27a6c4dc7bfc62f9ef6e9aa7c 27,674 bytes
- `screenshot.png` e6ccac8825818ecc2cfd2223035c6c335a3de1c38fad734d7dd292215618cef7 502,064 bytes
- `text.txt` f9e9557ab49ddb9598b22d6774d5466de0429deba8720e6e3fba62d778b5d0f3 5,127 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/certfr-2026-ale-014/index.html
