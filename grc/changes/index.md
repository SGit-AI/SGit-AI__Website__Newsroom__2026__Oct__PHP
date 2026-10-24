# What changed in the risk graph, release by release

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The php2shell risk graph compared between any two releases: nodes and edges added and removed, bases changed, gaps opened and closed; computed from git at every release.

[GRC](../../grc/index.html) · [Risks](../../grc/risks/index.html) · [Stakeholders](../../grc/stakeholders/index.html) · [Frameworks](../../grc/frameworks/index.html) · [The graph](../../grc/graph/index.html) · [Explore](../../grc/explore/index.html) · [Gaps](../../grc/gaps/index.html) · [Changes](../../grc/changes/index.html) · [From the network](../../grc/network/index.html)

# What changed in the risk graph, release by release

The graph is rebuilt at every release. This page compares two releases of it: the nodes and edges added and removed, the edges whose basis changed (from inferred to confirmed, say), and the gaps that opened or closed. 98 releases carry a graph; 6 of them changed it. Pick any two below; the default is the latest change.

## v0.15.18 → v0.15.19

| Measure | v0.15.18 | v0.15.19 | Change |
|---|---|---|---|
| Nodes | 724 | 726 | +2 |
| Edges | 1,354 | 1,356 | +2 |
| Edges known as source | 252 | 254 | +2 |
| Edges known as code | 287 | 287 | same |
| Edges known as inferred | 815 | 815 | same |
| Gap: Controls joined to no code or test that implements them | 95 | 95 | same |
| Gap: Code with no owner one step away | 16 | 16 | same |
| Gap: Code no test reaches | 9 | 9 | same |
| Gap: Risks no story tells | 14 | 14 | same |
| Gap: Risks with no treatment | 0 | 0 | same |
| Gap: Risks with no owner | 0 | 0 | same |
| Gap: Vulnerabilities no test reaches | 0 | 0 | same |
| Gap: Edges inferred by an agent, not yet checked | 815 | 815 | same |

### Nodes added: 2

2 source
- [Die Presse](../../grc/explore/index.html#focus=source:diepresse-41383717-die-php-sicherheitsluecke-ist-a) source
- [voix](../../grc/explore/index.html#focus=source:voix-business-cards-rainforest-ip-activity-an) source

### Edges added: 2

2 *cites*
- As of 16:05 UTC on 24 October, no named organisation has sai *cites* Die Presse source
- As of 16:05 UTC on 24 October, no named organisation has sai *cites* voix source

## Every release that changed the graph

| Release | Against | Nodes | Edges | Bases | Gaps | Nodes / edges after |
|---|---|---|---|---|---|---|
| [v0.15.19](#from=0.15.18&to=0.15.19) 2026-10-24 | v0.15.18 | +2 −0 | +2 −0 | 0 | +0 −0 | 726 / 1,356 |
| [v0.14.30](#from=0.14.29&to=0.14.30) 2026-10-24 | v0.14.29 | +3 −0 | +3 −0 | 0 | +0 −0 | 724 / 1,354 |
| [v0.13.0](#from=0.12.1&to=0.13.0) 2026-10-24 | v0.12.1 | +1 −1 | +1 −1 | 0 | +0 −0 | 721 / 1,351 |
| [v0.12.1](#from=0.12.0&to=0.12.1) 2026-10-24 | v0.12.0 | +8 −0 | +8 −0 | 0 | +0 −0 | 721 / 1,351 |
| [v0.10.13](#from=0.10.12&to=0.10.13) 2026-10-23 | v0.10.12 | +271 −0 | +504 −0 | 839 | +0 −9 | 713 / 1,343 |
| [v0.6.0](#from=&to=0.6.0) 2026-10-22 | the first graph | +442 −0 | +839 −0 | 0 | +143 −0 | 442 / 839 |

How it is made: every release commits the graph the build wrote ([data/grc-graph.json](../../data/grc-graph.json)). `admin/build/grc_history.py` compares each release's graph with the one before and keeps what changed in [data/grc-history.json](../../data/grc-history.json), written once per release, at its own build. The gaps are counted with today's rules ([data/grc-gaps.json](../../data/grc-gaps.json)) over each release's graph, so every pair is measured the same way. An edge is the same edge when its start, verb and end are the same. Graphs before v0.10.13 recorded no basis on an edge. Comparing two releases that are not next to each other replays the changes between them in your browser.


---
site v0.16.1 · data as of 2026-10-24T16:05Z · vault commit 8c16a64a7cf6 · https://php.oct.2026.newsroom.sgit.ai/grc/changes/index.html
