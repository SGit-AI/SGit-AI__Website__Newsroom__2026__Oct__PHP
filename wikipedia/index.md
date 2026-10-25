# Wikipedia, as a graph

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Each Wikipedia article this site watches, read as a fractal semantic graph: statements classed as facts, attributions and quotes, references joined to the captures this site holds, and every edit as what it changed.

# Wikipedia, as a graph

Wikipedia is one of the largest bodies of checked fact there is, and one of the hardest to use as one: an article is long, its edits are diffs of markup, its references are a list at the bottom, and nothing tells a reader what they have already seen. This section reads each article this site watches as a fractal semantic graph: one statement per sentence, each classed by its wording (a fact stated, a view attributed, a quote), each joined to the references it cites, and those to the captures this site holds of the same pages, which is where the article's facts and this site's claims meet. Every revision is kept, so an edit reads as what it changed. Kept by the ontologist; fetched by `admin/wikipedia/fetch.py` on the daily pass.

| Article | Statements | Cited | References captured here | Shared with our claims | Revisions | Editors | Reverts | Latest revision |
|---|---|---|---|---|---|---|---|---|
| [PHP2Shell](php2shell/index.html) | 40 | 37 (92%) | 17 of 44 | 13 | 370 | 178 | 41 | 2026-10-25 11:39:32 UTC |

## How it is made
- **Fetch.** Every revision of the article, with its wikitext, time, editor and edit summary; the Wikidata item; the articles that link in. Anonymous editors are recorded as anonymous, never by address.
- **Parse.** A parser (`admin/build/wikitext.py`, no model) lifts the references out, turns the markup into text, and splits it into sentences. One sentence is one statement; its id is a hash of its words, so the same sentence keeps its id across revisions and an edit is a set difference.
- **Class.** By wording only: a *record* (a number, a date, an identifier), a plain *stated* fact, an *attributed* statement (a named party said, reported or estimated it), a *quote*, or *hedged* wording. The class says how the article speaks, not whether it is right.
- **Join.** A reference is matched to this site's sources by its address and to a party by its host. A statement there and a claim here that cite the same captured page meet at that page.
- **Keep.** The data is `data/wikipedia/`; the graph of each article is in the ontology's `wikipedia` scope ([data/ontology.json](../data/ontology.json)), with its own kinds and verbs, joined to the story graph by `captured_as`.

## Wikidata and DBpedia

Wikidata is the structured sister of Wikipedia: one item per thing, with typed claims, edited in the open with the same history as an article. DBpedia is the older extraction of the same facts from Wikipedia's infoboxes, built from periodic dumps. This site reads both for the articles it watches, keeps the item's own history (on each article's [evolution page](php2shell/evolution/index.html#item)), and looks the parties of its own graph up on Wikidata so that a party here can carry the item that is already there, rather than a new identifier: 95 parties looked up, 25 items confirmed by hand, 2 proposed and waiting. The lookups are in [wikidata-links.json](../data/wikidata-links.json); the build shows only confirmed items.

| Article | Wikidata item | Claims | Item history | DBpedia |
|---|---|---|---|---|
| [PHP2Shell](php2shell/index.html) | [Q141801185](https://www.wikidata.org/wiki/Q141801185) | 15 claims | 112 revisions, last 2026-10-24 18:38:02 UTC | HTTP 404, not yet extracted |

Learned from them so far: an item is created by whichever language edition gets there first (this one from the Finnish Wikipedia, two hours after the English article); its claims are typed and sourced one by one, which is the shape this site's own attribution rows take; and an identifier that exists already is the one to use.

## For Wikipedia's editors

This site does not edit Wikipedia and does not ask to be cited by it. What it offers the article's editors, and the rules it holds itself to, are on [one page](for-editors/index.html); its reading of the article as a reviewer would read it, finding by finding against the captures, is on each article's [review page](php2shell/review/index.html).

## What this is for

Three things. A reader who wants the facts of a story, each with its evidence and without the markup, the edit wars and the list at the bottom. A newsroom that can see what Wikipedia says, what it rests on, and what changed since it last looked, in one view. And, in time, a measure: a source's trust shown by how often its statements are corrected, against other publications', rather than assumed.

The text of each article is Wikipedia's, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), by its contributors, with the revision id as the attribution; the pages and data of this section that carry it are under the same licence.


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/wikipedia/index.html
