# The story as a graph: who states what, who relays it, and what it rests on

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

1482 nodes and 1857 typed edges: every claim, number, event, signal, advice, party, source and capture on the PHP flaws story, walkable, with the independent origins of each claim.

# The story as a graph

In plain English Who said each thing first, who passed it on, and which saved pages it rests on. Click anything to walk from it to what it is connected to.

1482 nodes and 1857 edges in 15 verbs: 479 captures, 418 sources, 363 parties, 70 claims, 68 events, 20 exploitation signals, 17 numbers, 16 advice, 12 tensions, 8 topics, 8 phases, 3 CVEs. Each is drawn from the same rows as the pages, so the picture cannot disagree with the text. Start anywhere, follow a link, and the graph re-centres on it; a node with a thick ring opens a graph of its own.

The interactive graph needs JavaScript. Every node is also on a page: [the claims](../claims/index.html), [the sources](../sources/index.html), [the parties](../graph/parties/index.html), [the timeline](../timeline/index.html), [the tensions](../factcheck/index.html); the whole graph is [data/graph.json](../data/graph.json).

## Read it as sentences

Every edge is a verb, and read from the other end it has a different name: Wiz *states* a claim, the claim is *stated by* Wiz. There is no edge that only says two things are related. The verbs, with how many edges use each:

| Verb | Inverse | Reads | Edges | Where it comes from |
|---|---|---|---|---|
| `cites` | `cited_by` | A cites B | 377 | inherited from altitudes.json edge_registry |
| `states` | `stated_by` | A states B | 146 | proposed here |
| `relays` | `relayed_by` | A relays B | 46 | proposed here |
| `counts` | `counted_by` | A counts B | 6 | proposed here |
| `published_by` | `publishes` | A is published by B | 418 | inherited from governance-beat-ontology |
| `syndicates` | `syndicated_in` | A syndicates B | 9 | proposed here |
| `captured_in` | `captures` | A is captured in B | 479 | inherited from portugal-ontology |
| `appears_in` | `carries` | A appears in B | 138 | inherited from altitudes.json (Concept to Unit) |
| `flags` | `flagged_by` | A flags B | 25 | inherited from altitudes.json edge_registry |
| `advises` | `advised_by` | A advises B | 16 | proposed here |
| `classified_as` | `classifies` | A is classified as B | 138 | proposed here |
| `names` | `named_in` | A names B | 14 | proposed here |
| `part_of` | `has_part` | A is part of B | 13 | inherited from governance-beat-ontology |
| `member_of` | `has_member` | A is a member of B | 29 | proposed here |
| `works_for` | `employs` | A works for B | 3 | proposed here |

## How many voices, not how many pages

A claim is as strong as the number of **independent** parties that state it, not the number of pages that carry it. A person is counted with the organisation they speak for, and an outlet that passes a statement on is a *relay*, not a second origin. The fact-check desk grades the same claims by reading their captures ([the spectrum of evidence](../factcheck/index.html)); this is the reading the graph gives from its edges alone.

### Echoes: one origin, many relays (4)
- ['Where immediate remediation is not feasible, organisations should consider taking the system offline until it can be fully mitigated'](../facts/offline-ncsc/index.html) (3 relays)
- [watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild](../facts/watchtowr-itw/index.html) (3 relays)
- [The Dutch government took NCSC.nl offline as a precaution, with no active misuse seen yet; Dutch press reported DigiD, MijnOverheid and Overheid.nl offline too](../facts/nl-offline/index.html) (3 relays)
- [The Wikimedia Foundation took down a number of systems 'as a precautionary measure until they can be safely patched'](../facts/wikimedia-precaution/index.html) (4 relays)

### Unnamed origins (3)

Stated only by sources a page does not name: a gap in the evidence, not a party.
- [The flaws are CVSS 10.0](../facts/cvss-10/index.html) (0 relays)
- [The 8.5.12 fix may be incomplete, or there is a third, different bug](../facts/fix-incomplete/index.html) (1 relays)
- [Criminals are using AI to 'vibe code' an attack method](../facts/vibe-code/index.html) (1 relays)

### Every claim

| Claim | Status | Independent origins | Relays | Captures that carry it | Open tension |
|---|---|---|---|---|---|
| [Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 ](../facts/waf-nine-hours/index.html) | confirmed | 5 | 0 | 1 |  |
| [Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity ](../facts/ac-high/index.html) | confirmed | 3 | 0 | 2 |  |
| [The flaws were found by researchers using frontier AI under OpenAI's Patch the Planet initiative](../facts/ai-found/index.html) | reported | 3 | 0 | 1 |  |
| [None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproducti](../facts/pocs-wrong/index.html) | reported | 3 | 0 | 1 |  |
| [The release moved forward from 22 October 14:00 UTC to 21 October 14:00 UTC because of the leak](../facts/release-moved/index.html) | confirmed | 3 | 0 | 1 | K-010 |
| [PHP is used by almost 70% of websites whose server-side language is known](../facts/scale-70pc-websites/index.html) | reported | 3 | 0 | 3 |  |
| [All PHP versions from 5 onwards are affected by at least one of the flaws](../facts/versions-old/index.html) | disputed | 3 | 0 | 2 |  |
| [Amazon and Cloudflare saw sites being probed for the flaw](../facts/probing/index.html) | confirmed | 3 | 1 | 3 |  |
| [Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built images containing the](../facts/chainguard/index.html) | disputed | 2 | 0 | 1 |  |
| [The last PHP core RCE, CVE-2024-4577, was exploited in the wild one day after disclosure and in KEV three days](../facts/kev-precedent/index.html) | reported | 2 | 0 | 1 |  |
| [watchTowr confirmed in public that the bugs were real and posted both CVE numbers before the release](../facts/leak-watchtowr/index.html) | reported | 2 | 0 | 2 |  |
| [The out-of-memory issue was found in a 2024 audit by Quarkslab (funded through OSTIF and the Sovereign Tech Ag](../facts/quarkslab-2024/index.html) | confirmed | 2 | 0 | 2 |  |
| [Quarkslab's published audit summary lists 27 findings, two redacted because their fixes were complex and in pr](../facts/quarkslab-redacted/index.html) | reported | 2 | 0 | 3 |  |
| [Remote code execution is confirmed on PHP-FPM](../facts/rce-fpm/index.html) | disputed | 2 | 0 | 3 | K-008 |
| [The fixes were released at 14:00 UTC on 21 October](../facts/release-time/index.html) | disputed | 2 | 0 | 1 | K-010 |
| [Calif found the flaws first: discovery 1 August, hash commitment 5 August, report to PHP 11 August](../facts/who-first/index.html) | confirmed | 2 | 0 | 2 |  |
| [Wiz Research independently discovered the first flaw on 19 August and reported on 24 August](../facts/wiz-independent/index.html) | reported | 2 | 0 | 0 |  |
| [In researchers' own tests, pre-authentication RCE was confirmed against WordPress, Drupal, Joomla, MediaWiki, ](../facts/wordpress-drupal/index.html) | reported | 2 | 0 | 1 |  |
| [Edinburgh and Oxford councils, the Met Police and the Office for Budget Responsibility were unavailable; Brist](../facts/uk-list/index.html) | reported | 2 | 1 | 3 | K-005 |
| [VulnCheck counts about 2.6 million internet-facing hosts exposing PHP; Censys, of the 2.58 million hosts it sa](../facts/scale-2.6m-hosts/index.html) | reported | 2 | 3 | 3 |  |
| [Frontier AI found the flaw ahead of attackers, giving defenders time to prepare](../facts/ahead-of-attackers/index.html) | disputed | 1 | 0 | 1 |  |
| [Exploit attempts across Cloudflare's network: thousands in the ten hours before announcement, tens of thousand](../facts/cf-millions/index.html) | reported | 1 | 0 | 1 |  |
| [CISA has not observed exploitation; neither CVE is in the Known Exploited Vulnerabilities catalog](../facts/cisa-none/index.html) | confirmed | 1 | 0 | 1 |  |
| [The flaws were disclosed on 22 October 2026](../facts/disclosure-22oct/index.html) | contradicted | 1 | 0 | 4 |  |
| [The fix was authored on 18 October at 15:26 UTC and entered the public branches at 14:06 UTC on 21 October, wi](../facts/fix-authored/index.html) | confirmed | 1 | 0 | 0 |  |
| [The fix removes longjmp() for out-of-memory errors in favour of a delayed soft OOM at the next VM safe point a](../facts/fix-bailout/index.html) | confirmed | 1 | 0 | 3 |  |
| [Both bugs are in the C engine, not in PHP code: the allocator's longjmp-based bailout on out-of-memory, and re](../facts/fix-engine/index.html) | confirmed | 1 | 0 | 2 |  |
| [The GitHub advisories credit four reporters: lcfr-hax (Calif), sagitzadik-wiz (Wiz), amyb-oai (OpenAI) and tom](../facts/four-reporters/index.html) | confirmed | 1 | 0 | 3 |  |
| [The risks require immediate patching across United States Government departments and agencies](../facts/gov-patch-required/index.html) | reported | 1 | 0 | 1 |  |
| [No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no public exploit code kno](../facts/huntress-none/index.html) | reported | 1 | 0 | 1 |  |
| [No traffic matching the php2shell exploit patterns was seen during Imperva's pre-disclosure monitoring](../facts/imperva-none/index.html) | reported | 1 | 0 | 1 |  |
| [Automated exploitation attempts were seen in Latvia; none succeeded](../facts/latvia-attempts/index.html) | reported | 1 | 0 | 0 |  |
| [Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and](../facts/latvia-offline/index.html) | confirmed | 1 | 0 | 1 |  |
| [On 20 October at about 15:00 UTC the two CVE IDs began circulating on forums and social media with a wrong rel](../facts/leak-cve-ids/index.html) | reported | 1 | 0 | 2 |  |
| [The leak started with an anonymous Hacker News post citing a reliable source, which came down after screenshot](../facts/leak-hn/index.html) | reported | 1 | 0 | 1 |  |
| [Mitigation advice given to a few critical-infrastructure providers from about 23:00 UTC on 20 October may have](../facts/leak-mitigations/index.html) | reported | 1 | 0 | 1 |  |
| [Calif mistakenly published a video around 20:00 UTC on 20 October showing its proof of concept against a numbe](../facts/leak-video/index.html) | reported | 1 | 0 | 2 |  |
| [Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expected](../facts/more-paths/index.html) | reported | 1 | 0 | 1 | K-011 |
| [As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitati](../facts/no-confirmed-compromise/index.html) | reported | 1 | 0 | 11 |  |
| [Reports of active exploitation exist](../facts/nz-active/index.html) | reported | 1 | 0 | 1 |  |
| [The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patc](../facts/offline-allies/index.html) | contradicted | 1 | 0 | 5 |  |
| [Organisations that cannot update immediately, or that run PHP 8.1 or older, should take PHP-based systems offl](../facts/offline-cisa/index.html) | confirmed | 1 | 0 | 1 |  |
| [If an immediate update is not feasible, take the system offline until it can be fully mitigated](../facts/offline-nsa/index.html) | confirmed | 1 | 0 | 2 |  |
| [Updating is the only complete mitigation; the configuration measures reduce exposure to specific paths and do ](../facts/only-update/index.html) | confirmed | 1 | 0 | 4 |  |
| [OpenAI independently reported the same root cause on 11 August, with further vectors on 18 September](../facts/openai-same-day/index.html) | reported | 1 | 0 | 1 |  |
| [The pre-announcement was published at 19:30 UTC on 20 October](../facts/preannounce-time/index.html) | disputed | 1 | 0 | 1 |  |
| [Unauthenticated RCE over HTTP against Apache mod_php with default settings, before any application code runs](../facts/rce-modphp/index.html) | confirmed | 1 | 0 | 2 | K-008 |
| [About 6,000 potentially affected resources in Latvia, a few hundred in the public sector](../facts/scale-latvia/index.html) | reported | 1 | 0 | 1 |  |
| [674 products in the NCSC-NL inventory: 206 vulnerable, 46 fixed, 418 under investigation, 3 not vulnerable](../facts/scale-ncsc-nl/index.html) | confirmed | 1 | 0 | 0 |  |
| [Two critical vulnerabilities, CVE-2026-109618 and CVE-2026-109619, each CVSS v4.0 9.2, fixed in PHP 8.5.12, 8.](../facts/two-cves-9.2/index.html) | confirmed | 1 | 0 | 6 |  |
| [A web application firewall may provide some protection until systems are patched](../facts/waf/index.html) | disputed | 1 | 0 | 1 |  |
| [Weird Gloop turned off its wiki web servers for 13 hours and still served about 94% of page views from cache](../facts/weirdgloop-13h/index.html) | confirmed | 1 | 0 | 1 |  |
| [Parts of Wikipedia, Edinburgh council, French government sites, the University of Geneva, online shops and the](../facts/affected-sites/index.html) | reported | 1 | 1 | 4 |  |
| [An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attemp](../facts/amazon-honeypot/index.html) | reported | 1 | 1 | 2 |  |
| [Cloudflare observed attack traffic targeting its customers after the leak, with attackers mutating payloads](../facts/cloudflare-traffic/index.html) | reported | 1 | 1 | 2 |  |
| [Chainguard's team found the same bugs independently with an AI harness and a frontier model after a researcher](../facts/lorenc-ai-found/index.html) | reported | 1 | 1 | 1 |  |
| [The most severe flaws ever detected by AI](../facts/most-severe/index.html) | reported | 1 | 1 | 2 |  |
| [There is no evidence yet that hackers have exploited the flaw](../facts/no-exploitation/index.html) | reported | 1 | 1 | 1 |  |
| [Something like 30 million websites could be affected](../facts/scale-30m/index.html) | reported | 1 | 1 | 1 |  |
| [70% of the Internet is affected](../facts/scale-70pc-internet/index.html) | unverified | 1 | 1 | 0 |  |
| [Edinburgh council's site went offline late on 21 October; the council called it 'essential maintenance' and di](../facts/edinburgh/index.html) | reported | 1 | 2 | 2 |  |
| [Finland's state IT provider Valtori restricted public traffic to government web services from 12:45 local time](../facts/fi-offline/index.html) | reported | 1 | 2 | 1 |  |
| [Oxford City Council: 'a precaution because of a worldwide issue with the underlying technology and is not a cy](../facts/oxford/index.html) | reported | 1 | 2 | 1 |  |
| [The Dutch government took NCSC.nl offline as a precaution, with no active misuse seen yet; Dutch press reporte](../facts/nl-offline/index.html) | reported | 1 | 3 | 3 |  |
| ['Where immediate remediation is not feasible, organisations should consider taking the system offline until it](../facts/offline-ncsc/index.html) | disputed | 1 | 3 | 3 |  |
| [watchTowr sees active exploitation attempts and lists the flaws as exploited in the wild](../facts/watchtowr-itw/index.html) | unverified | 1 | 3 | 7 |  |
| [The Wikimedia Foundation took down a number of systems 'as a precautionary measure until they can be safely pa](../facts/wikimedia-precaution/index.html) | reported | 1 | 4 | 3 |  |
| [The flaws are CVSS 10.0](../facts/cvss-10/index.html) | contradicted | 0 | 0 | 5 |  |
| [The 8.5.12 fix may be incomplete, or there is a third, different bug](../facts/fix-incomplete/index.html) | unverified | 0 | 1 | 0 | K-011 |
| [Criminals are using AI to 'vibe code' an attack method](../facts/vibe-code/index.html) | unverified | 0 | 1 | 1 |  |

## Zooming in: the fractal layers

- **A CVE opens the code.** The two CVE nodes open the review graph of the fix, which has its own ontology (the flaws, the design of the patch, the files and functions changed) and its own verbs, joined to this one by a named bridge. This is the estate's test of a fractal graph: going down opens a new vocabulary under the same grammar.

- **A source opens its captures**, and each capture lists its files with their SHA-256. A claim *appears in* a capture where the fact-check desk found its words there. This step is addressing rather than a new ontology, and is described as such.

- **A party opens what it said and what it passed on**: the claims and numbers it states, the ones it relays, the sources it publishes, the organisation it is part of. [Every party](parties/index.html).

- **A party steps across into the risk graph.** The risk desk keeps its own graph ([the risk graph](../grc/graph/index.html)), where parties appear as stakeholders, mostly as classes (WAF vendors, local councils, national governments). [data/crosswalk.json](../data/crosswalk.json) declares the bridges: a party *is* a stakeholder, or is *among* a class of them; a CVE is the same anchor in all three graphs. Bridges, not a merge: each graph keeps its words.

- **A tension opens the claims it flags**: the contradiction ledger of the fact-check desk, one node per row, because two claims that disagree are not one edge with the same name both ways.

## The ontology

Kinds of node:

| Kind | Altitude | Nodes | What it is |
|---|---|---|---|
| Claim | story | 70 | One sentence this site carries, with its sources and a status word (data/claims.json). |
| Number | story | 17 | A figure someone published, with what it measures (data/numbers.json). |
| Event | story | 68 | A dated moment on the timeline (data/timeline.json). |
| Exploitation signal | story | 20 | One party's report of exploitation, attempts or none seen (data/exploitation.json). |
| Advice | story | 16 | What one agency told operators to do, chiefly whether to take systems offline (data/agencies.json). |
| Tension | story | 12 | A row of the fact-check desk's contradiction ledger: claims that measure differently, dispute or contradict each other. A node, because the grammar has no self-inverse edge. |
| Topic | story | 8 | A class in the topic taxonomy of claims. |
| Phase | story | 8 | A class in the phase taxonomy of the timeline. |
| Party | world | 363 | A person, organisation, agency, outlet, group, registry, platform or project (data/entities.json); its class is in 'class'. |
| Source | evidence | 418 | A page in the evidence vault's manifest (data/sources.json). |
| Capture | evidence | 479 | One time the vault saved a source: its files and their hashes. The first fractal layer below a source. |
| CVE | anchor | 3 | An anchor node: a CVE identifier, where the story graph joins the code-review graph (data/review.json) and the outside world (cve.org). It has no authority of its own. |

Verbs this graph will not use, and why:
- `related_to`: a generic association edge says nothing; the estate bans it outright
- `mentions`: say what the mention does: cites, names, states or relays
- `associated_with`: generic
- `contradicts`: self-inverse; a contradiction is a node that flags both claims
- `measures_differently`: self-inverse; recorded as a contradiction node with tension 'measures-differently'
- `agrees_with`: self-inverse, and agreement is read from independent states edges, not asserted

The grammar is the estate's, from [graphs.sgit.ai](https://graphs.sgit.ai/v1/grammar/); the files are [data/ontology.json](../data/ontology.json) (kinds, verbs, taxonomies, formulas), [data/entities.json](../data/entities.json) (one node per party, whatever a page calls it) and [data/attribution.json](../data/attribution.json) (who states each row). The graph is [data/graph.json](../data/graph.json). Kept by the ontologist. The component that draws it is documented for every agent on [the graph component](component/index.html) page.


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/graph/index.html
