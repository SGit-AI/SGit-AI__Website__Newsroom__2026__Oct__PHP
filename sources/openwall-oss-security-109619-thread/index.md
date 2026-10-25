# Source: Re: CVE-2026-109619 thread (21/16, 21/17, 21/23, 22/2)

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

oss-security list (replies: Aaron Rainbolt, Yves-Alexis Perez/Debian, Christian Fischer/Greenbone): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · forum · secondary · captured

# Re: CVE-2026-109619 thread (21/16, 21/17, 21/23, 22/2)

**oss-security list (replies: Aaron Rainbolt, Yves-Alexis Perez/Debian, Christian Fischer/Greenbone)** · [https://www.openwall.com/lists/oss-security/2026/10/21/16](https://www.openwall.com/lists/oss-security/2026/10/21/16) · published 2026-10-21T15:24:37Z · added by `collector-primary` · slug `openwall-oss-security-109619-thread`

raw/ curl copies of four replies. Fediverse report (fedi.katze.sh/@elise) that the 8.5.12 fix may be incomplete or a different new bug; Canonical reportedly told by PHP 'unrelated and not a real issue' (second-hand, via Matrix). Greenbone notes 7.4-8.1 are implicitly affected.

## What it says, as the collector read it

#### oss-security replies to the CVE-2026-109619 announcement: notes

- Captured with curl only (raw/), ~08:14Z on 22 Oct. These are third-party replies, not PHP statements.

- 21/16, Aaron Rainbolt, 21 Oct 10:24:37 -0500 (15:24Z): "While not yet fully confirmed, the Fediverse is reporting that the fix to at least PHP 8.5.12 may be incomplete: https://fedi.katze.sh/@elise/117479383739450605"

- 21/17, Yves-Alexis Perez (Debian), 17:41:56 +0200 (15:41Z): @elise also said it seems to be a *different* vulnerability: "there's no way this is the same vuln, this is another one." (https://fedi.katze.sh/@elise/117478655339557825)

- 21/23, Rainbolt, 12:29:01 -0500 (17:29Z): per #security:ubuntu.com Matrix, Canonical asked PHP and "was told that it's 'unrelated and not a real issue'". Second-hand and unconfirmed on-list.

- 22/2, Christian Fischer (Greenbone), 22 Oct 08:45:47 +0200 (06:45Z): the subject "PHP 8.2-8.5" could imply that older versions are unaffected, but the php.net backports to 7.4/8.0/8.1 imply that "at least versions down to 7.4 are affected as well".

- OPEN: is there a third PHP bug, or an incomplete fix in 8.5.12? Not confirmed by PHP on-list as of capture. The fedi.katze.sh posts should be captured by the social collector.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| The 8.5.12 fix may be incomplete, or there is a third, different bugPer a Matrix channel, Canonical asked PHP and 'was told that it's unrelated and not a real issue'. Second-hand. Nothing from PHP on the list at capture. [fact timeline →](../../facts/fix-incomplete/index.html) | Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez | unverified | **A1** Weak signal●○○○○○ opinion disputed | 0/1 | [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| All PHP versions from 5 onwards are affected by at least one of the flawsThe CVE records list only 8.2 to 8.5 with defaultStatus 'unaffected'. php.net published source backports for 7.4, 8.0 and 8.1, which implies they are affected. A scanner that trusts the CVE record will miss 7.4 to 8.1. [fact timeline →](../../facts/versions-old/index.html) | NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) | disputed | **A3** Echoed●●●○○○ disputed | 3/4 | [NCSC-NL](../../sources/ncsc-nl-advisories/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html) [CERT-FR](../../sources/certfr-2026-ale-014/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expectedA position, from a vendor; consistent with the Fediverse report of a third bug. [fact timeline →](../../facts/more-paths/index.html) | Fastly | reported | **A2** Reported●●○○○○ opinion | 1/2 | [Fastly](../../sources/fastly-blog-php2shell/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 15:24:37 UTC | Aaron Rainbolt relays to oss-security a Fediverse report that the 8.5.12 fix may be incomplete; a Debian maintainer adds that the poster called it a different bug. | stated |
| 2026-10-21 17:29 UTC | Per a Matrix channel, Canonical asked PHP about the Fediverse report and was told it is 'unrelated and not a real issue'. | stated |
| 2026-10-22 06:45:47 UTC | Greenbone on oss-security: the backports imply versions down to 7.4 are affected, whatever the subject line says. | stated |

## The bytes

No browser capture; see raw.
raw, 4 files with SHA256SUMS- `oss-security-2026-10-21-16.html` 6a76141ae5a06584e8c6f6e61f4c455ce078152d6c56ce05206ee1c9ef7acccf
- `oss-security-2026-10-21-17.html` 059317aa4a1f458e19196e6add44a6b3106632b82c82f104a5b83d0df6fbe09f
- `oss-security-2026-10-21-23.html` 39555f34a419becc6a47480eabb369e05f4bac6ce06e9e3843e4dfcb5c99801b
- `oss-security-2026-10-22-2.html` bbc0f0fc06953b13308925334e39e7808796e46ea9505630917762502996bea2

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/openwall-oss-security-109619-thread/index.html
