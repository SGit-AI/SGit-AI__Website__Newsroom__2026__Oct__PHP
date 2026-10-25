# Source: Synology製品における「PHP2Shell」脆弱性の影響について | 株式会社アスク

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

株式会社アスク: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# Synology製品における「PHP2Shell」脆弱性の影響について | 株式会社アスク

**株式会社アスク** · [https://www.ask-corp.jp/news/2026/10/synology-php2shell-vulnerabilities.html](https://www.ask-corp.jp/news/2026/10/synology-php2shell-vulnerabilities.html) · published 2026-10-23T12:14:16+09:00 · added by `curator@php.newsroom` · slug `ask-corp-news-2026-10-synology-php2shell-vulnerab`

Promoted from the source watch (pack copy 7r83qic5), snapshot 20261023T160435Z, queue priority 4 (mechanical selection by researcher@php.newsroom, read by the curator). ASK Corporation (Japanese distributor of Synology), 23 October: Synology's PSIRT investigated and found the impact is limited to systems running certa...

## What it says, as the collector read it

#### Synology製品における「PHP2Shell」脆弱性の影響について | 株式会社アスク

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`, read from its pack copy `7r83qic5`), page `jp/news/ask-corp/news-2026-10-synology-php2shell-vulnerabilities-html`, snapshot `20261023T160435Z`. Copied byte for byte; every file's sha256 is in `captures/20261023T160435Z/provenance.json` and was re-checked against the watch's own hashes.

#### What the page says

_Curator's reading of the capture._

ASK Corporation (Japanese distributor of Synology), 23 October: Synology's PSIRT investigated and found the impact is limited to systems running certain PHP-dependent packages: Calendar, IDrive (third party), Joomla, KodExplorer, MailStation, MediaWiki, phpMyAdmin, vtigerCRM, Web Station and WordPress; Synology Drive is not affected. Security updates for PHP were released for DSM 7.4, 7.3 and the end-of-life 7.2; updating through Package Center restarts the package and clears the flaw (MailStation needs a manual update).

> これによる影響は一部のPHP依存パッケージ（アプリ）を実行しているシステムに限定されている

_Curator's translation:_ "the impact is limited to systems running some PHP-dependent packages (apps)"

#### Why it is here

From the promotion queue (`index/promote.json`, priority 4): Mentions CVE-2026-109618/109619 or php2shell: "Synology製品における「PHP2Shell」脆弱性の影響について | 株式会社アスク". Selected mechanically, not read by a person.

#### Capture notes

Language `ja`. Nothing in the page addresses an AI or hides text from a reader.

## Claims that cite it

No claim cites this source yet.

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261023T160435Z · HTTP 200 · https://www.ask-corp.jp/news/2026/10/synology-php2shell-vulnerabilities.html- `headers.json` f7efa40eced7de094e1454d75d903089f8edc6283538b1bb1bb167a7e7e9f96d 513 bytes
- `page.html` 36e585132825e6f74d0c7dc8949cc4939fcaa561e6040f042c7284224c180609 32,059 bytes
- `provenance.json` 1fb451ccb51d0aab506320c5326cf44cf08b624947042521b72fde2e91aaa87e 1,745 bytes
- `rendered.html` 1c8e49b4f6e8a2fc19fac8fb79c8da79cbf34c504a78cb01c6afb81a7b9a50af 36,453 bytes
- `screenshot.jpg` 06a6815944d0dfb8ab21e9f3785a6c539ffaebb2a1d99b6d7cd2ed9fe3ede788 290,684 bytes
- `text.txt` 6522b5d445b74558fd46281774222b2a0bc0cba617fbd4017dce5a6556577011 6,428 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/ask-corp-news-2026-10-synology-php2shell-vulnerab/index.html
