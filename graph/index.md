# The story as a graph: claims, events and the sources they cite

209 nodes and 281 citation edges from the php2shell claims and timeline to the captured sources, drawn from the same rows as the text, with the JSON to download.

# The story as a graph

209 nodes and 281 edges: 70 claims, 68 events and the 71 sources they cite. There is no second graph behind this one: the page, the briefings and the timeline are all drawn from the same rows, so the picture cannot disagree with the text. The JSON is [data/graph.json](../data/graph.json); this page shows the claims-to-sources slice.

Every line is one citation. Colour is the claim's status: green confirmed, grey reported, amber disputed or contradicted, red unverified. A source with a filled dot is primary.

## How to read it

- A claim with many lines to primary sources is well-founded; a claim with one line to a news page is one party's word relayed once.

- The BBC live page sits near the top of the right column because the early claims all came through it; the work of the last day was to draw second lines from those claims to the pages the BBC was reporting on.

- A source with no line is captured but not yet cited: a home page kept for context, a block recorded for the record, or a page whose claims nobody has traced yet. The sources page lists them all.

- Events cite sources the same way; they are in the JSON and on the timeline, and are left off the drawing to keep it legible.


---
site v0.2.1 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/graph/index.html
