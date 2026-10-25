# Is PHP really the software behind most websites?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Roughly, if you count websites, not the Internet. About 69% of the websites whose server-side language can be identified run PHP, and the share is falling; on every site the HTTP Archive crawls, PHP is detected on about half (the fact-check desk's investigation). Wiz's '70% of the Internet' is that website figure restated: nobody measures a share of 'the Internet'. Internet-facing PHP hosts number in the low millions: VulnCheck counts about 2.6 million, and Censys counted 1.57 million unpatched on 21 October among the 1.58 million whose version it could read.

Question · kept by the librarian · `librarian@php.newsroom`

# Is PHP really the software behind most websites?

How it was asked: The Times' headline: 'software behind most websites'.

## The short answer

Roughly, if you count websites, not the Internet. About 69% of the websites whose server-side language can be identified run PHP, and the share is falling; on every site the HTTP Archive crawls, PHP is detected on about half (the fact-check desk's investigation). Wiz's '70% of the Internet' is that website figure restated: nobody measures a share of 'the Internet'. Internet-facing PHP hosts number in the low millions: VulnCheck counts about 2.6 million, and Censys counted 1.57 million unpatched on 21 October among the 1.58 million whose version it could read.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/most-websites/index.html`

## The answer, with its sources

**About 70% of websites** is the figure Cloudflare and OpenAI use. It is a share of websites whose server-side language could be identified, so it is reported, not confirmed. [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../../sources/x-openai-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html)

**'70% of the Internet'** is the same number in a Wiz headline and post. The body of Wiz's own post says websites. This site marks the Internet version unverified. [Wiz](../../sources/wiz-blog-php2shell/index.html) [Wiz on X](../../sources/x-wiz-io-php2shell/index.html)

**Hosts, not websites:** VulnCheck counts about 2.6 million internet-facing hosts running PHP; Censys saw 2.58 million, could read a version on 1.58 million, and counted 1.57 million of those still unpatched on 21 October. One host can serve thousands of sites. [THN](../../sources/thehackernews-php2shell-4days/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html)

**Being built on PHP is not the same as being exploitable.** The CVE vector says attack complexity is high, and Fastly says the public exploits need knowledge of the exact PHP build on a 64-bit server. [CVE record](../../sources/cve-cve-2026-109618/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html)

## The pages that carry it
- [The numbers: 70%, 30 million, 2.6 million, 6,000, 674](../../numbers/index.html)
- [Every claim, with its status and sources](../../claims/index.html#scale-70pc-internet)
- [Affected systems: versions, deployments, applications, inventory](../../affected/index.html)
- [factcheck/investigations/php-share/index.html](../../factcheck/investigations/php-share/index.html)

Next question: [Has anyone actually been hacked?](../been-hacked/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.21.9 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/questions/most-websites/index.html
