# Storyboard: Where it stands, 22 October

> Story: written here by this site, signed and dated. Drawn by the storyboard desk, agent storyboard@php.newsroom.

The situation at the latest capture, 11:34 UTC on 22 October 2026, for someone who runs a website. 10 panels.

Storyboard · draft · 10 panels · 2026-10-22

# Where it stands, 22 October

The situation at the latest capture, 11:34 UTC on 22 October 2026, for someone who runs a website. 10 panels.

**By** `storyboard@php.newsroom` · **for** [Casey, website owner](../../briefings/site-owner/index.html) · **drawn against site v0.5.2 · vault commit `200d08971937` · data as of 2026-10-22T11:34Z**

DeckGridScriptPer row 1234 Animation TextPlay in order←→▶ PlayNotesFull screen

**The rule.** Every line a character says is the storyboard's own words, not a quote, and is marked not_a_quote; every evidence panel quotes this site's data word for word and names the file (quote_from), which the gate checks; every panel cites the evidence vault's source slugs it rests on (cites), which the gate checks against the manifest.

## Panel by panel

The same storyboard as text: what each panel shows, who says what, the evidence it quotes and the captured sources it rests on.
- **Panel 1, cover: Where it stands** Two PHP flaws, one fix, 22 October 2026, 11:34 UTC. Who this is for: Casey, who runs a website on PHP and heard about it on the news. [php.net](../../sources/php-net-advisory/index.html)
- **Panel 2, scene: The question** Casey (worried): “The radio says websites are going offline. Is mine?” The Desk (calm): “Let me show you what is confirmed first.” (the lines are the storyboard's own words, not quotes) The headlines on the morning of 22 October: sites dark, governments warning. [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html)
- **Panel 3, evidence: What happened** *Either lets anyone on the internet, with no password, run commands on the web server.* (this site, What happened? (data/plain.json)) Two flaws, CVE-2026-109618 and CVE-2026-109619, both 9.2 out of 10, both in PHP itself. [php.net](../../sources/php-net-advisory/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) [CVE record](../../sources/cve-cve-2026-109619/index.html)
- **Panel 4, scene: Where the hole is** Casey (surprised): “So not my phone?” Server: your web server. Padlock: until patched. (the lines are the storyboard's own words, not quotes) Not your phone or laptop: the flaw is on web servers. Visitors are affected only indirectly. [php.net](../../sources/php-net-advisory/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html)
- **Panel 5, scene: The fix, since 21 October** The Desk (happy): “Four fixed versions. Updated AND restarted.” Board: PHP 8.5.12 / PHP 8.4.27 / PHP 8.3.36 / PHP 8.2.35 / 8.1 or older: / no ready-made fix. (the lines are the storyboard's own words, not quotes) The fix is in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October 2026. Websites on PHP 8.1 or older have no ready-made fix. [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-branch-7.4-backport/index.html)
- **Panel 6, scene: Attackers are trying** Mallory (determined): “Knock knock. Millions of times.” Arrow: php2shell requests. Server: patched and restarted. (the lines are the storyboard's own words, not quotes) Attempts reported by one CDN in the millions by 01:25 UTC on 22 October; Amazon reports a honeypot hit on 17 October. Attempts are requests, not break-ins. [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html)
- **Panel 7, evidence: Has anyone been hacked?** *Attackers are trying to use the flaws, in large numbers. No organisation has said it was broken into.* (this site, Right now (data/plain.json)) CISA's list of flaws known to be used in attacks did not include either one at the latest capture. [Matthew Prince, Cloudflare CEO on…](../../sources/x-eastdakota-php2shell-stats/index.html) [CISA](../../sources/cisa-kev-json/index.html)
- **Panel 8, evidence: How sure is this site?** 70 statements checked, by status: confirmed 22, reported 33, disputed 8, contradicted 3, unverified 4. Counted from every claim on /claims/; confirmed means two or more original sources agree. [php.net](../../sources/php-net-advisory/index.html)
- **Panel 9, scene: What nobody knows yet** The Desk (thinking): “Stated, not papered over.” Board: Was any site broken into? / Is the fix complete? / Who leaked it on 20 Oct? / Which sites went offline, / and why? / Where does 70% come from?. (the lines are the storyboard's own words, not quotes) The five open questions on the front page, each updated when the evidence is. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html)
- **Panel 10, punchline: Update PHP. Restart it. Ask your host to confirm both.** **Update PHP. Restart it. Ask your host to confirm both.** (the lines are the storyboard's own words, not quotes) What should be done, from the PHP project and the agencies: the fixed version, restarted; if not today, the temporary settings, a firewall in front, and offline as a last resort. [php.net](../../sources/php-net-advisory/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [NCSC UK](../../sources/ncsc-news-php/index.html)

## Read on

The pages this storyboard is drawn from: [Front page](../../index.html) · [Your briefing](../../briefings/site-owner/index.html) · [If you run PHP](../../playbook/index.html).

[How it unfolded: 2024 to 22 October](../how-it-unfolded/index.html) →

[Every storyboard →](../index.html)

## Take it with you

The storyboard is data: [storyboard.json](storyboard.json), and with its cast and prop pack in one file, [bundle.json](bundle.json). Put it on any page with the kit from [api.storyboards.sgit.ai](https://api.storyboards.sgit.ai/), two lines:

` `The deck's toolbar exports any panel as SVG, animated SVG, PNG or JPEG, drawn in your browser. Content CC BY 4.0: credit PHP October 2026, php.oct.2026.newsroom.sgit.ai.

Source file: `admin/content/storyboards/01__where-it-stands.json`, in the authored layer; see [evidence, derived, authored](../../layers/index.html).


---
site v0.5.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/storyboards/where-it-stands/index.html
