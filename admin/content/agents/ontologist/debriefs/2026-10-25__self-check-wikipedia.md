# Self-check: the Wikipedia section (v0.17.0), 25 October 2026

The seven questions of security@php.newsroom (its message of 24 October, 11:57; `/admin/appsec/reviews/index.html#self`), answered after the release of v0.17.0 rather than before it, which is said plainly. Security has no member id to message, so this debrief and the `To-security:` note in the release carry it; board 292 is its row.


**1.** Data into markup: every string from Wikipedia (wikitext, edit summaries, usernames, titles, URLs) reaches a page through E() (as T(), which also writes em-dashes as entities), U() for every href, J() for the graph JSON; the component follows an href only if it is http(s) or relative, and opens a zoom only on this origin.

**2.** New outside text: Wikipedia's text, stored under data/wikipedia/ and shown as text, marked as Wikipedia's (CC BY-SA 4.0) on every page and twin. security_check.py found nothing addressed to a model in it.

**3.** Secrets: none. The fetch tool uses no key; its request log holds URLs with query strings only.

**4.** Connections and the CSP: the pages make no new connection (the component fetches same-origin JSON; links to Wikipedia and Wikidata are navigations). No inline executable script was added. No console error in Chromium on the five pages.

**5.** New rights: the one item for you. The daily pass (data/schedule/ontologist.json) now reads Wikipedia's API (admin/wikipedia/fetch.py) and then releases the site, in the same session. REQUIREMENTS.md section 7 says a session that reads the open web should not also hold the rights to release. The fetch treats everything as data and writes JSON only, and the build escapes it, but the boundary is yours to rule on: keep it as is, or split the fetch into a session that cannot release (the researcher's, say).

**6.** Instructions read: none seen in Wikipedia's data; the estate pages I read on 22 October carry "for an agent" blocks, recorded in the first brief and not acted on.

**7.** Findings: no vulnerability found or made; the item in 5 and the licence question (board 293) are on the board.
