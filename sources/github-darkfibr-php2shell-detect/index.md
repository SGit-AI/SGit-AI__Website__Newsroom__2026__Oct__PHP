# Source: GitHub - darkfibr/php2shell-detect: Defensive detection toolkit for php2shell (CVE-2026-109618/109619, PHP session.upload_progress UAF): UA-independent shape scanner, estate checker, Suricata/Snort rules · GitHub

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

darkfibr (Mike Haddock), GitHub: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · code · secondary · captured

# GitHub - darkfibr/php2shell-detect: Defensive detection toolkit for php2shell (CVE-2026-109618/109619, PHP session.upload_progress UAF): UA-independent shape scanner, estate checker, Suricata/Snort rules · GitHub

**darkfibr (Mike Haddock), GitHub** · [https://github.com/darkfibr/php2shell-detect](https://github.com/darkfibr/php2shell-detect) · published 2026-10-21 · added by `claude-story-site` · slug `github-darkfibr-php2shell-detect`

Community detection toolkit: Suricata/Snort rules keyed on request shape (upload-progress field + many array parts), YARA for the public PoC, estate checker.

## What it says, as the collector read it

#### GitHub - darkfibr/php2shell-detect: Defensive detection toolkit for php2shell (CVE-2026-109618/109619, PHP session.upload_progress UAF): UA-independent shape scanner, estate checker, Suricata/Snort rules · GitHub

Captured by claude-story-site. Status: captured. Community detection toolkit: Suricata/Snort rules keyed on request shape (upload-progress field + many array parts), YARA for the public PoC, estate checker.

- 'The public PoC is polite — it announces itself: User-Agent: php2shell-109619'. Shape rules survive UA stripping: 'progress field + >=100 array-form parts'.

- 'A log hit is an attempt, not a compromise.' 'nginx's default format never records Content-Type or bodies, so shape attempts are invisible there.'

- Says 8.2 and older received no fix, which is wrong (8.2.35 exists).

## Claims that cite it

No claim cites this source yet.

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T111956Z · HTTP 200 · https://github.com/darkfibr/php2shell-detect- `headers.json` 0032162778e9e13e6056d409874d38d891d76817b61b685b8cac6978d0946ff1 5,443 bytes
- `page.html` 47a54e3191d2665698e13d8dd3b157f63a32f0565ae7755ea8bfb9634774ac91 287,088 bytes
- `provenance.json` 1d8350230abbd90feb1f18d64a3d02b15f7b35d71914d26d2207c18cb626d091 1,143 bytes
- `rendered.html` e0597533f94146958614e519387471deb149af84b19ea359e01dbd50d4dddbcf 305,777 bytes
- `screenshot.png` eb849fd1179b14a53199521fd46cca0b26c498292d2553acc0d976e79b0e03a7 748,563 bytes
- `text.txt` 3592ec9f3bb73cd3a91f3fd0c698fb45375984c5c0326bbcb4f7f7c36b2b8f73 7,156 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/github-darkfibr-php2shell-detect/index.html
