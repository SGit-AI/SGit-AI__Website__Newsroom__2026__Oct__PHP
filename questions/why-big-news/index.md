# Why is this such big news?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Four things at once: the flaws are in PHP itself, which runs a large share of the web; they were found with AI help; the coordinated disclosure leaked a day early, so the fix shipped under pressure; and the NSA, CISA and NCSC told organisations that could not patch to take systems offline, which is why government, council and police sites went dark.

Question · kept by the librarian · `librarian@php.newsroom`

# Why is this such big news?

How it was asked: 'Article about this in The Times as well, so it's big news.'

## The short answer

Four things at once: the flaws are in PHP itself, which runs a large share of the web; they were found with AI help; the coordinated disclosure leaked a day early, so the fix shipped under pressure; and the NSA, CISA and NCSC told organisations that could not patch to take systems offline, which is why government, council and police sites went dark.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/why-big-news/index.html`

## The answer, with its sources

**Where the flaw is.** In the PHP engine, so it affects any PHP site regardless of the application on top, rated 9.2 out of 10. [CVE record](../../sources/cve-cve-2026-109618/index.html) [php.net](../../sources/php-net-advisory/index.html)

**How it was found.** Calif, OpenAI and Wiz each found it with frontier AI models in August; the same root cause had been seen in a 2024 audit and left unfixed. [Calif](../../sources/calif-php2shell/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html)

**How disclosure broke.** The CVE IDs leaked on 20 October with a wrong 10.0 score, a demonstration video was published and deleted, and the release was brought forward a day. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html)

**What the agencies said.** The NSA's post was viewed 10.1 million times at capture; councils, the Met Police, the OBR and government sites in the Netherlands, Finland, France and Latvia went offline as a precaution. [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [LBC](../../sources/lbc-uk-websites-offline/index.html) [Rijksoverheid / NCSC-NL](../../sources/rijksoverheid-ncsc-php-news/index.html) [CERT.LV](../../sources/certlv-php-preventive/index.html)

## The pages that carry it
- [PHP in October 2026: two critical security flaws, tracked as evidence](../../index.html)
- [Who found php2shell, and what the AI did](../../discovery/index.html)
- [How the coordinated disclosure broke](../../leak/index.html)
- [The timeline, 2024 to the latest capture](../../timeline/index.html)
- [In context: php2shell against Kaminsky, Heartbleed, Shellshock, Log4Shell and the last PHP RCE](../../context/index.html)

Next question: [We are on PHP 7.4, 8.0 or 8.1. Is there a patch?](../old-php/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.21.6 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/questions/why-big-news/index.html
