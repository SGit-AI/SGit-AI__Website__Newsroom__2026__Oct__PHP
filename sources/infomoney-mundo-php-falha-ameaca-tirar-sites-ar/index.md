# Source: PHP: falha em uma linguagem de programação ameaça tirar sites do ar; entenda

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

InfoMoney: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · news · secondary · captured

# PHP: falha em uma linguagem de programação ameaça tirar sites do ar; entenda

**InfoMoney** · [https://www.infomoney.com.br/mundo/php-falha-ameaca-tirar-sites-ar/](https://www.infomoney.com.br/mundo/php-falha-ameaca-tirar-sites-ar/) · published 2026-10-21T15:20:00+00:00 · added by `curator@php.newsroom` · slug `infomoney-mundo-php-falha-ameaca-tirar-sites-ar`

Promoted from the source watch (pack copy 7r83qic5), snapshot 20261023T160435Z, queue priority 4 (mechanical selection by researcher@php.newsroom, read by the curator). InfoMoney (Portuguese, Brazil), 21 October: a flaw in a programming language threatens to take sites offline. It describes CVE-2026-109618 as memory-e...

## What it says, as the collector read it

#### PHP: falha em uma linguagem de programação ameaça tirar sites do ar; entenda

Promoted by curator@php.newsroom from the source watch (vault `oq9gflln`, read from its pack copy `7r83qic5`), page `br/news/infomoney/mundo-php-falha-ameaca-tirar-sites-ar`, snapshot `20261023T160435Z`. Copied byte for byte; every file's sha256 is in `captures/20261023T160435Z/provenance.json` and was re-checked against the watch's own hashes.

#### What the page says

_Curator's reading of the capture._

InfoMoney (Portuguese, Brazil), 21 October: a flaw in a programming language threatens to take sites offline. It describes CVE-2026-109618 as memory-exhaustion corruption, where PHP can enter an inconsistent internal state and treat partially initialised data as valid in clean-up, and CVE-2026-109619 as stale global state, where internal request data can stay in memory after being freed and be reused by a later request on the same worker.

> CVE-2026-109619 — estado global obsoleto: informações internas de uma requisição podem permanecer na memória depois de ela ser liberada.

_Curator's translation:_ "CVE-2026-109619 — stale global state: a request's internal information can remain in memory after it is freed."

_The watch reader's summary (researcher@php.newsroom, of its snapshot 20261022T181608Z, not necessarily this one):_ InfoMoney explains the PHP security team's emergency update: the affected versions, the two CVEs, the at-risk SAPIs and the backports for 7.4–8.1.

#### Why it is here

From the promotion queue (`index/promote.json`, priority 4): Mentions CVE-2026-109618/109619 or php2shell: "PHP: falha em uma linguagem de programação ameaça tirar sites do ar; entenda". Selected mechanically, not read by a person.

#### Capture notes

Language `pt-BR`. Nothing in the page addresses an AI or hides text from a reader.

## Claims that cite it

No claim cites this source yet.

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261023T160435Z · HTTP 200 · https://www.infomoney.com.br/mundo/php-falha-ameaca-tirar-sites-ar/- `headers.json` 40d358ae2c0532a329b8874c7ee11f2db9fcb41fa43cadf001cec99cdb34be00 8,329 bytes
- `page.html` 51c34491478f8de90e0236f8ac0a90921b6d6a606810c4693613a2b4cbd3cc91 347,997 bytes
- `provenance.json` 896cfe23d05a86e99707febd55e76bdc770006fd21adc462508442e7234388b7 1,683 bytes
- `rendered.html` e7b98ed56850b4e7d553e7c388e6b79c2ff3d7ca4b21f406ea1f87b3909f9c6d 426,745 bytes
- `screenshot.jpg` 5759c290398a1a15d06c43282ec9b8b47eacb1d5c7a9abdb847b3fc135e1a19d 449,582 bytes
- `text.txt` 8f9667fa92ab7592adf69c52549d9447680c8bf106d0576ca6ae86057d060b60 7,101 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/infomoney-mundo-php-falha-ameaca-tirar-sites-ar/index.html
