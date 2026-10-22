# We are behind Cloudflare (or another firewall). Are we safe?

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Safer, not safe. Cloudflare's rules were live about nine hours before disclosure, on every plan including Free, and Akamai, Fastly, Imperva and Fortinet followed. Every one of them calls it a stopgap and says patch anyway: attackers mutate payloads, and the rules only see traffic that goes through the firewall.

Question · kept by the librarian · `librarian@php.newsroom`

# We are behind Cloudflare (or another firewall). Are we safe?

How it was asked: Asked by site owners who saw that Cloudflare had rules live before disclosure.

## The short answer

Safer, not safe. Cloudflare's rules were live about nine hours before disclosure, on every plan including Free, and Akamai, Fastly, Imperva and Fortinet followed. Every one of them calls it a stopgap and says patch anyway: attackers mutate payloads, and the rules only see traffic that goes through the firewall.

To paste back where it was asked: the paragraph above and `https://php.oct.2026.newsroom.sgit.ai/questions/waf-enough/index.html`

## The answer, with its sources

**Rules exist.** Cloudflare at 03:02 UTC on 21 October for all plans; Akamai, Fastly and Imperva the same day; Fortinet signatures by 22 October, shipped in alert-only mode by default. [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html)

**Their own caveats.** Cloudflare's CTO: a stopgap only. Swiss BACS: not sufficient on its own. Tenable: Cloudflare's rules cover only traffic routed through Cloudflare, so a direct hit on the origin server is not covered. [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [BACS](../../sources/ch-bacs-warnung-php/index.html) [Tenable](../../sources/tenable-php2shell-faq/index.html)

## The pages that carry it
- [Detection and defence: what blocks php2shell and what shows it](../../defence/index.html)
- [Every claim, with its status and sources](../../claims/index.html#waf)

Next question: [Do our developers need to change our code?](../change-code/index.html) · [every question](../index.html). Nothing here is advice for your environment; the [php.net advisory](https://www.php.net/archive/2026.php#2026-10-21-5) and your national agency are the authorities.


---
site v0.4.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/questions/waf-enough/index.html
