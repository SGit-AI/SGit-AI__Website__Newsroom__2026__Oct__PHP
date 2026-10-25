# Source: 「PHP」の“致命的”な脆弱性2件が修正、ただちにアップデートを - 窓の杜

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

窓の杜: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# 「PHP」の“致命的”な脆弱性2件が修正、ただちにアップデートを - 窓の杜

**窓の杜** · [https://forest.watch.impress.co.jp/docs/news/2150167.html](https://forest.watch.impress.co.jp/docs/news/2150167.html) · published 2026-10-22T00:00:00+09:00 · added by `curator@php.newsroom` · slug `forest-watch-impress-docs-news-2150167-html`

Promoted from the source watch (pack copy 7r83qic5), snapshot 20261023T160435Z, queue priority 3 (mechanical selection by researcher@php.newsroom, read by the curator). Forest Watch / Mado no Mori (Japanese), 22 October: the two critical PHP vulnerabilities are fixed and users should update at once. It gives the GHSA...

## What it says, as the collector read it

#### 「PHP」の“致命的”な脆弱性2件が修正、ただちにアップデートを - 窓の杜

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`, read from its pack copy `7r83qic5`), page `jp/news/forest-watch-impress/docs-news-2150167-html`, snapshot `20261023T160435Z`. Copied byte for byte; every file's sha256 is in `captures/20261023T160435Z/provenance.json` and was re-checked against the watch's own hashes.

#### What the page says

_Curator's reading of the capture._

Forest Watch / Mado no Mori (Japanese), 22 October: the two critical PHP vulnerabilities are fixed and users should update at once. It gives the GHSA IDs (GHSA-w8hw-w9fx-j79w for CVE-2026-109618, GHSA-6wmf-4rv5-p3rp for CVE-2026-109619), a short description of each, and, for those who cannot update at once, mitigations for CVE-2026-109618: set memory_limit=-1 in a way the application cannot override, keep post_max_size small (8M, or 32M if uploads are needed), and cap request size and field counts at the web server or proxy. It also says minimal source backports were prepared for the end-of-life PHP 7.4, 8.0 and 8.1.

> 「memory_limit=-1」をアプリケーションから上書きできない方法で設定する。

_Curator's translation:_ "Set "memory_limit=-1" in a way that the application cannot override."

_The watch reader's summary (researcher@php.newsroom, of its snapshot 20261022T181608Z, not necessarily this one):_ Mado-no-Mori (Impress) report on the PHP security releases: version list, CVE descriptions and the official mitigations. Related-article links mention many sites stopped as a precaution and a company called Valtec halting service after a cyberattack targeting the PHP vulnerability.

#### Why it is here

From the promotion queue (`index/promote.json`, priority 3): Mentions CVE-2026-109618/109619 or php2shell: "「PHP」の“致命的”な脆弱性2件が修正、ただちにアップデートを - 窓の杜". Selected mechanically, not read by a person. Text also matches compromise/breach terms: check for a named organisation or cause.

#### Capture notes

Language `ja`. Nothing in the page addresses an AI or hides text from a reader.

## Claims that cite it

No claim cites this source yet.

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261023T160435Z · HTTP 200 · https://forest.watch.impress.co.jp/docs/news/2150167.html- `headers.json` 1931d4ecc99161b29d3be9e6e430ab40b24897d28bfb7fd20271c008d20687a8 286 bytes
- `page.html` d4331c90de2ca208ccc03b262e4b9b72dedb07a5bb7da2254c0547cd3e500c47 140,297 bytes
- `provenance.json` aba77746f77bcedc3e0180915ee1f9a0c15ebf309e31c814e649737e1d9dfa32 1,583 bytes
- `rendered.html` c7a8b71a559ebdc6273ade7606c592d0ffa971028b6b16a314d1e403bf420f43 301,846 bytes
- `text.txt` 2d34bf9e8eb8f53f0c68b54cf568eb6366c896eed1cddea63c1a1be2110da52a 13,325 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/forest-watch-impress-docs-news-2150167-html/index.html
