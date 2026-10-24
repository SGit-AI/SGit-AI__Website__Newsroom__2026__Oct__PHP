# Explore the risk graph: start from one thing and follow it

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Start from a CVE, a risk, a stakeholder, a file, a test or a control and see only what touches it, grouped by verb, one step at a time; or climb from code to the risks, controls and stakeholders above it. Every edge says how it is known.

[GRC](../../grc/index.html) · [Risks](../../grc/risks/index.html) · [Stakeholders](../../grc/stakeholders/index.html) · [Frameworks](../../grc/frameworks/index.html) · [The graph](../../grc/graph/index.html) · [Explore](../../grc/explore/index.html) · [Gaps](../../grc/gaps/index.html) · [From the network](../../grc/network/index.html)

# Explore the risk graph: start from one thing and follow it

The whole graph is 713 nodes and 1418 edges, too much to read at once. Start from one thing you care about (a CVE, a risk, the people who run PHP, a file of the fix, a test, a control) and see only what touches it, grouped by how; open any of those to go one step further, with the way back always shown. Or start from code or a test and climb: the fixes it realises, the flaws they fix, the risks above them, and the controls, stakeholders and stories of each risk.

The explorer needs JavaScript; it reads [data/grc-graph.json](../../data/grc-graph.json) in your browser and sends nothing anywhere.

## How to read it

- **Every edge is a verb**, read from the node you are on: a risk *arises from* a weakness, a test *tests* a fix, a file *realises* a fix.

- **Every edge says how it is known.** Read from a capture, read from the fix commit, inferred by an agent, or confirmed by a person. Inferred edges are dashed; one switch hides them, and the view shows what is left. Each link names what supports it.

- **The address is the view.** Copy it to send someone exactly what you are looking at: the start, everything you opened, and whether inferred edges are hidden.

In the graph: 270 test, 95 control, 71 source, 62 claim, 43 stakeholder, 41 treatment, 34 risk, 26 page, 16 code, 14 weakness, 10 role, 9 briefing, 8 member, 7 remediation, 5 story, 2 vulnerability. The tests are the 270 test files of the fix commit, from its file list in the evidence vault ([data/grc-tests.json](../../data/grc-tests.json)).


---
site v0.11.4 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/grc/explore/index.html
