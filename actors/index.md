# Who says what: every party and its claims

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

27 parties in the php2shell story, each with the claims this site attributes to it and the sources behind them.

# Who says what

In plain English Every organisation and person quoted, and what each one says.

27 parties whose words this site quotes: maintainers, researchers, agencies, vendors, operators and reporters. Each has a page with the claims it makes, the sources those claims come from, and its own small graph. The count is of claims this site attributes to the party; a party with many claims and few primary sources is one whose word is being taken.

| Party | Role in the story | Claims | Sources |
|---|---|---|---|
| [The PHP Group / php.net](php-group/index.html) | maintainer, CVE numbering authority | 5 | [php.net](../sources/php-net-advisory/index.html) [php.net](../sources/php-net-changelog-8/index.html) [php-src](../sources/github-php-src-tags/index.html) |
| [The PHP Foundation](php-foundation/index.html) | funds core developers; published the account of discovery and the leak | 0 | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| [Jakub Zelenka (bukka), PHP security team](zelenka/index.html) | published both GitHub advisories and the oss-security announcements | 4 | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [oss-security](../sources/openwall-oss-security-2026-10-21-6/index.html) |
| [Alexandre Daubois, PHP security team (personal blog)](daubois/index.html) | inside account of the rumours and the leak | 4 | [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) |
| [Calif (Ryan Austin, @lcfr_hax; Michal Zalewski)](calif/index.html) | first reporter; published the write-up with demo videos | 5 | [Calif](../sources/calif-php2shell/index.html) [Ryan Austin, Calif on X](../sources/x-lcfr-hax-hash-tweet/index.html) |
| [OpenAI (Patch the Planet, Codex Security, Amy Burnett)](openai/index.html) | reported the same root cause on 11 August; ran the coordination coalition | 3 | [OpenAI on X](../sources/x-openai-php2shell/index.html) [OpenAI](../sources/patchtheplanet-org/index.html) [OpenAI forum](../sources/openai-community-php-flaws/index.html) |
| [Wiz Research](wiz/index.html) | independent discovery 19 August; the '70% of the Internet' headline | 0 | [Wiz](../sources/wiz-blog-php2shell/index.html) [Wiz on X](../sources/x-wiz-io-php2shell/index.html) |
| [Quarkslab, OSTIF](quarkslab/index.html) | 2024 audit that first surfaced the OOM issue | 1 | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Calif](../sources/calif-php2shell/index.html) |
| [Cloudflare](cloudflare/index.html) | WAF rules live 9 hours early; saw attack traffic | 3 | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) |
| [Amazon (CJ Moses)](amazon/index.html) | honeypot evidence of a pre-disclosure attempt | 1 | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| [Chainguard](chainguard/index.html) | published patched images before the embargo lifted, per the Foundation | 1 | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) [Techzine](../sources/techzine-php-chainguard/index.html) |
| [watchTowr](watchtowr/index.html) | confirmed the CVE numbers in public on 20 October, per Daubois | 2 | [Daubois](../sources/daubois-blog-php2shell-rumors/index.html) [CERT-EU](../sources/certeu-sa-2026-018/index.html) |
| [National agencies (NSA, CISA, NCSC UK, CERT-EU, CERT-FR, CCCS, ACSC, NCSC NZ, NCSC-NL, ACN, BACS, CERT.LV, JPCERT)](agencies/index.html) | advisories; see the agency table | 11 | [NSA](../sources/nsa-press-php-4630238/index.html) [CISA](../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../sources/ncsc-news-php/index.html) |
| [BBC News (live page; Kieran Kelly, Imogen James)](bbc/index.html) | the coverage most readers saw on the morning of 22 October | 0 | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| [Alan Woodward, Surrey Centre for Cyber Security](woodward/index.html) | commentator quoted by the BBC: 30 million websites; probing seen by Amazon and Cloudflare | 2 | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| [The Hacker News (Ravie Lakshmanan)](thn/index.html) | carried Amazon's honeypot account and VulnCheck's host count | 1 | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| [Dan Lorenc, Chainguard](chainguard-lorenc/index.html) | shipped patched images early; says exploits were in the wild and denies leaking | 2 | [The Register](../sources/theregister-php-blames-chainguard/index.html) [Feross Aboukhadijeh on X on X](../sources/x-feross-chainguard/index.html) |
| [Matthew Prince, Cloudflare CEO](prince/index.html) | the attempt counts | 1 | [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) |
| [Imperva Threat Research](imperva/index.html) | had the details under embargo; saw nothing before disclosure | 1 | [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |
| [Fastly](fastly/index.html) | the most candid vendor on exploitability and on what a WAF cannot do | 2 | [Fastly](../sources/fastly-blog-php2shell/index.html) |
| [Akamai](akamai/index.html) | rule 3000991; the 2024 precedent | 1 | [Akamai Security Research](../sources/akamai-blog-php-core-rce/index.html) [Akamai Security Research](../sources/akamai-blog-cve-2024-4577-one-day/index.html) |
| [Huntress](huntress/index.html) | no exploitation seen on partner systems | 2 | [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| [Weird Gloop (cookmeplox)](weirdgloop/index.html) | the one operator with a measured outage | 1 | [Weird Gloop](../sources/weirdgloop-blog-php2shell/index.html) |
| [The Dutch government and NCSC-NL](rijksoverheid/index.html) | took its own site offline | 3 | [Rijksoverheid / NCSC-NL](../sources/rijksoverheid-ncsc-php-news/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell/index.html) |
| [Valtori and NCSC-FI](valtori/index.html) | Finland's precautionary shutdown | 1 | [Yle](../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../sources/helsinkitimes-finland-shutdown/index.html) |
| [Community detection authors (darkfibr, rjmendez, Lexsah, Blevene)](detectors/index.html) | the rules, and the correction of the leaked PoC's mechanism | 1 | [darkfibr, GitHub](../sources/github-darkfibr-php2shell-detect/index.html) [rjmendez, GitHub](../sources/github-rjmendez-phpup-2026/index.html) [Lexsah, GitHub](../sources/github-lexsah-php2shell-detection/index.html) [Blevene](../sources/gist-blevene-detection-guide/index.html) |
| [Arnaud Le Blanc and the PHP fix authors](leblanc/index.html) | wrote the fix | 0 | [php/php-src, read from a clone](../sources/github-php-src-fix-commit-3584a98bd/index.html) |


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/actors/index.html
