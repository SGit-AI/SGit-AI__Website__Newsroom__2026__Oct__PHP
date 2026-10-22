# Brief: how many sites went offline, and where

Status: proposed by desk@php.newsroom (the narrator) on 22 October 2026, for the editor's go. Asked by the editor: "a very tight grip and understanding on how many websites have now been taken offline", and a pattern he suspects: "a lot of impact on non-English countries because they tend to run on [old] infrastructure ... a lot of PHP".

## Where we are

- The offline ledger in `data/impact.json` has 10 rows. They count different things: one row is a whole government's public web services (Finland, Valtori), another is one council's site (Edinburgh). Ten rows are not ten of anything, so the site cannot give a count today.
- Three rows rest on the organisation's own word (NCSC.nl, CERT.LV, Weird Gloop); the rest are the press. The fact-check desk grades the Netherlands row overstated: the government's notice names only NCSC.nl; DigiD, MijnOverheid and Overheid.nl come from the press.
- The ledger's latest capture is about 11:30 UTC on 22 October. The two sources closest to a count are not captured yet: the PHPocalypse Tracker's `sites.csv` and the BBC live page as it stands ("32 UK services, 90%"), board 089.

## The editor's hypothesis, and what tests it

**Hypothesis:** non-English-speaking countries are hit harder because they run more old PHP.

**What the data can say today: nothing either way.**

1. **Our collection leans English.** The source watch is 214 of 333 pages in English (64%), and discovery across languages is blocked (board 077). The UK holds 4 of the 10 offline rows because we read the UK press.
2. **A rival explanation fits the big takedowns.** The national-scale ones (the Netherlands, Finland, Latvia) were precautionary decisions by national centres or state IT agencies, and Latvia patched one "state website platform". Centralised government hosting and a cautious CERT can switch a whole government off at once. Italy's ACN advised update only, with no offline advice. The offline map may be a map of posture, not of old PHP.
3. **There is no denominator.** "More old PHP" needs, per country: PHP's share of sites and the share on unsupported versions (8.1 and older). The only national count we hold is CERT.LV's "about 6,000 potentially affected" in Latvia.

What would support the hypothesis: in the same country-domain samples, a higher share of unsupported PHP outside the English-speaking web, and offline or compromise rows that follow it rather than following CERT advice. What would refute it: offline rows that track CERT posture and centralised hosting, with version shares that do not differ.

## The work

| Board | Owner | Work |
| --- | --- | --- |
| 089 (exists, first) | collector-researchers | Capture the PHPocalypse Tracker's `sites.csv` and the BBC live page today. |
| 091 | researcher@php.newsroom | Discovery in the other languages straight from the source: national CERTs and public broadcasters of DE, FR, ES, IT, PL, PT, BR and JP, not through Google News (board 077). |
| 092 | collector-gov | The posture map: every EU and EEA national CERT's advice on php2shell coded as offline, isolate or update only, with the capture. |
| 093 | collector-researchers | The denominator: W3Techs PHP share and PHP version shares by country domain (extends 033 and 043), and any per-country host count from Censys, Shodan or VulnCheck. |
| 094 | claude-story-site | The offline ledger reshaped: one row per organisation, a unit (site, platform, whole government), a count of domains where known, the source's language, and who said it; then a count with its basis on the front page. |
| 095 | factcheck | Grade the reshaped ledger as rows land, the Netherlands row first, and the count's basis. |
| 096 | journalist | The piece on where the web went dark and why, once 092 and 093 are in, not before. |

## What this cannot do

It cannot count sites that went offline quietly: an outage nobody announced leaves no source. The count will be a floor, and the page says so.
