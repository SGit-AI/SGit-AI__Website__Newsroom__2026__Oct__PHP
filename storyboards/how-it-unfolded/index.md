# Storyboard: How it unfolded: 2024 to 22 October

> Story: written here by this site, signed and dated. Drawn by the storyboard desk, agent storyboard@php.newsroom.

Five moments, from an audit nobody acted on to sites going dark. 9 panels.

Storyboard · draft · 9 panels · 2026-10-22

# How it unfolded: 2024 to 22 October

Five moments, from an audit nobody acted on to sites going dark. 9 panels.

**By** `storyboard@php.newsroom` · **for** [Alex, curious reader](../../briefings/everyone/index.html) · **drawn against site v0.5.2 · vault commit `200d08971937` · data as of 2026-10-22T11:34Z**

DeckGridScriptPer row 1234 Animation TextPlay in order←→▶ PlayNotesFull screen

**The rule.** Every line a character says is the storyboard's own words, not a quote, and is marked not_a_quote; every evidence panel quotes this site's data word for word and names the file (quote_from), which the gate checks; every panel cites the evidence vault's source slugs it rests on (cites), which the gate checks against the manifest.

## Panel by panel

The same storyboard as text: what each panel shows, who says what, the evidence it quotes and the captured sources it rests on.
- **Panel 1, cover: How it unfolded** 2024 to 22 October 2026, in five moments. Who this is for: anyone asking how a bug from 2024 became a headline in October 2026. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html)
- **Panel 2, spectrum: Five moments** **2024** an audit spots it → **Aug** AI teams prove it → **20 Oct** it leaks → **21 Oct** the fix ships early → **22 Oct** sites go dark. The five moments on the front page, each linked to its page on this site. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Calif](../../sources/calif-php2shell/index.html) [php.net](../../sources/php-net-advisory/index.html) [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html)
- **Panel 3, evidence: 2024: noticed, and left** *An audit spots the out-of-memory weakness. Nobody can show it is exploitable, so it is left.* (this site, How it unfolded (data/plain.json)) The PHP Foundation's account of the 2024 audit. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Quarkslab](../../sources/quarkslab-blog-php-src-audit/index.html)
- **Panel 4, scene: August 2026: three teams, with AI** The Desk (calm): “Three teams. Working attacks within three weeks.” Terminal: $ audit php-src / > oom in bailout path / > stale global state / > exploitable: yes / > report to PHP. (the lines are the storyboard's own words, not quotes) The GitHub advisories credit four reporters, among them Calif, Wiz and OpenAI; Calif reported first, on 11 August. [Calif](../../sources/calif-php2shell/index.html) [Wiz](../../sources/wiz-blog-php2shell/index.html) [PHP](../../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html)
- **Panel 5, evidence: 20 October: the leak** *The secret leaks: the CVE numbers circulate two days early, with a wrong severity score.* (this site, How it unfolded (data/plain.json)) Who leaked it, and where, is still not known. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [Daubois](../../sources/daubois-blog-php2shell-rumors/index.html)
- **Panel 6, scene: 21 October: a day early** Drew (excited): “Tags at 13:35. Advisory at 14:00.” Calendar: 21 Oct, not 22. Arrow: edge rules already live. Server: WAF. (the lines are the storyboard's own words, not quotes) PHP releases the fix a day ahead of plan; Cloudflare had rules live about nine hours before disclosure by its own account. [php.net](../../sources/php-net-advisory/index.html) [php-src](../../sources/github-php-src-tags/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html)
- **Panel 7, scene: 22 October: sites go dark** Jordan (worried): “Offline means hacked?” The Desk (calm): “No. Offline is a decision.” Sign: Closed as a precaution. (the lines are the storyboard's own words, not quotes) The NSA and CISA said take systems offline if you cannot update; Dutch government services such as DigiD were taken offline. [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Rijksoverheid / NCSC-NL](../../sources/rijksoverheid-ncsc-php-news/index.html) [TPO.nl](../../sources/tpo-nl-digid-offline/index.html)
- **Panel 8, evidence: The first official words** *If an immediate update is not feasible, it is recommend[ed] that organizations take the system offline until it can be fully mitigated.* (NSA Cybersecurity on X, 21 October, 13:45 UTC (data/agencies.json)) Posted before the CVE records were published. [NSA Cyber on X](../../sources/nsa-x-2112903220209098897/index.html)
- **Panel 9, punchline: Found in 2024. Proved in August. Fixed in a day.** **Found in 2024. Proved in August. Fixed in a day.** (the lines are the storyboard's own words, not quotes) Every dated event is on /timeline/ with its sources. [PHP Foundation](../../sources/php-foundation-blog-security-release/index.html) [php.net](../../sources/php-net-advisory/index.html)

## Read on

The pages this storyboard is drawn from: [Timeline](../../timeline/index.html) · [Who found it](../../discovery/index.html) · [How disclosure broke](../../leak/index.html).

← [Where it stands, 22 October](../where-it-stands/index.html) · [Exposed is not exploited](../exposed-is-not-exploited/index.html) →

[Every storyboard →](../index.html)

## Take it with you

The storyboard is data: [storyboard.json](storyboard.json), and with its cast and prop pack in one file, [bundle.json](bundle.json). Put it on any page with the kit from [api.storyboards.sgit.ai](https://api.storyboards.sgit.ai/), two lines:

` `The deck's toolbar exports any panel as SVG, animated SVG, PNG or JPEG, drawn in your browser. Content CC BY 4.0: credit PHP October 2026, php.oct.2026.newsroom.sgit.ai.

Source file: `admin/content/storyboards/02__how-it-unfolded.json`, in the authored layer; see [evidence, derived, authored](../../layers/index.html).


---
site v0.5.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/storyboards/how-it-unfolded/index.html
