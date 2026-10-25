# Source: GitHub - Lexsah/php2shell-detection: Detection and mitigation rules for CVE-2026-109618 / CVE-2026-109619 (php2shell). Blue-team only. · GitHub

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Lexsah, GitHub: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · code · secondary · captured

# GitHub - Lexsah/php2shell-detection: Detection and mitigation rules for CVE-2026-109618 / CVE-2026-109619 (php2shell). Blue-team only. · GitHub

**Lexsah, GitHub** · [https://github.com/Lexsah/php2shell-detection](https://github.com/Lexsah/php2shell-detection) · published 2026-10-21 · added by `claude-story-site` · slug `github-lexsah-php2shell-detection`

Blue-team rules (YARA, Sigma, Suricata SIDs 910961801-803, ModSecurity, Falco, auditd) and the server-level session.upload_progress.enabled=Off mitigation.

## What it says, as the collector read it

#### GitHub - Lexsah/php2shell-detection: Detection and mitigation rules for CVE-2026-109618 / CVE-2026-109619 (php2shell). Blue-team only. · GitHub

Captured by claude-story-site. Status: captured. Blue-team rules (YARA, Sigma, Suricata SIDs 910961801-803, ModSecurity, Falco, auditd) and the server-level session.upload_progress.enabled=Off mitigation.

- 'It is a PHP_INI_PERDIR setting: ini_set() / auto_prepend_file cannot change it, and the upload-progress handler runs while the request body is parsed, i.e. before any of your PHP code executes.'

- 'User-Agent strings are trivially changed. Treat UA rules as a high-confidence/low-coverage signal and the body + process rules as the durable ones.'

## Claims that cite it

No claim cites this source yet.

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T112009Z · HTTP 200 · https://github.com/Lexsah/php2shell-detection- `headers.json` 25e99ec6775270a84bcecf5a232634c2e640ef9246b469967311c1240df22dd7 5,436 bytes
- `page.html` 6151205973ed45a3e00af67742bf708f8d42f4caf1171c1b5671e024b730bdbb 288,052 bytes
- `provenance.json` 2560ba2b32e6f1ea7e5feb0e81a7b6db2855392524862a91661362e6410175ca 1,077 bytes
- `rendered.html` 14e642e4e762e427c9bd8be65bfd45e0d8e2a3289c65ab7c197e197cc9077a66 301,999 bytes
- `screenshot.png` c5300a3f00d8c04d057f920a6e8ceb48282544a99c967bd855027483a7a4ffc9 779,281 bytes
- `text.txt` 10b6edf13054c98d5da298e7bdc04a654d2e0a7fa7fa820047a7996a4887c25e 7,136 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-lexsah-php2shell-detection/index.html
