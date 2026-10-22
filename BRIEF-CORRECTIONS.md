# Corrections to the brief, and to the site

Newest first. A correction names the date, what was wrong, what was found, and what was done instead. The mistake stays visible where it was made.

## 2026-10-22, v0.1.0: the brief's domain name

The memo proposes a name of the shape `php.story.newsroom.sgit.ai`; the repository's README already names `php.oct-2026.story.sgit.ai`. The site is built for the README's name, with a `CNAME` file, because that is the one with a repository behind it. If the editor prefers the memo's shape, the `CNAME` file is the one line to change.

## 2026-10-22, v0.1.0: "both ChatGPT and Claude"

The first memo asks for both models to be used to connect the data. This first release was built in one Claude session reading the vault that several Claude agents filled; no second model has read the vault yet. Recorded as not done rather than described as done.

## 2026-10-22, v0.1.0: the semantic fractal graph

The second memo asks for the whole semantic fractal graph. What exists is one graph (claims, events, sources and citation edges) in `data/graph.json`, drawn on one page. It is not fractal: no node opens into a graph of its own. That is the next layer, not this one.
