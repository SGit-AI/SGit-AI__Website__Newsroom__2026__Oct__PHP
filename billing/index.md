# The billing model: what runs and what is designed

How this site is paid for: the reading meter that runs (pence per page, kept in your browser, never blocking), the provenance pricing that is designed (per claim, with a share for the fact creator), and a counted model of what the story cost to assemble.

# The billing model

Two layers, and the page is careful to say which is which. **What runs** is a reading meter: a few pence a page from credit kept in your browser, charged by how far down the page you read, never blocking, with the option to decline and say why. **What is designed** is paying for provenance rather than pages: a price per verified claim, a share for whoever created the fact, and a snapshot of the vault for a reader who wants the bytes. The first is the same component the newsroom runs; the second is argued here and built nowhere.

## What runs: the reading meter

Every page carries ``, SG Meter v1.3.1, vendored under `assets/components/` and loaded from this site only. You start with £5.00 of credit in this browser; the balance is in the top bar and goes below zero without anything being blocked. A page costs its price times the share of it you scrolled through, rounded to 5% and never less than a tenth, once per page per session. At the foot of each page you can rate how useful it was, which sets the price from free to double, or decline to pay with a reason. Nothing leaves the browser: no account, no cookie, no server of ours, no analytics listening to the meter's events. [Your reading account](../account/index.html) shows the history and exports it as JSON.

| Kind | Price, read to the end | Pages | Why |
|---|---|---|---|
| story | 2p | the front page, the flaws, the timeline, the leak, the discovery, the exploitation signals, the playbook | Pages assembled from the vault by agents; the reader pays for the assembly. |
| analysis | 3p | the numbers, the claims, the agencies, the affected systems | Pages where the site did work a reader cannot do by reading one source: counting, comparing, converting times. |
| briefing | 5p | the six briefings | The most compressed form of the work: one page for one reader's decision. |
| evidence | 1p | the sources page, the graph | Reference pages. Cheap, because the value is in checking, not reading. |
| free | 0p | the method, the team, the billing model, corrections, the release history, admin | The site's own account of itself is free; charging for it would be charging to be checked. |

Top-ups are £5.00 of credit on a payment page. No payment link is configured for this site yet, so [the top-up page](../account/top-up.html) runs the meter's simulated cart and says so. When a link is added, the credit is added on the return page without verifying the payment, because a static site has nowhere to receive a webhook; the meter's security model is explicit that this is an honesty box, not a paywall.

## What is designed: paying for provenance
- **A price per verified claim.** Each claim on this site carries a status and the sources that give it that status. The unit a reader or an agent would pay for is not the page but the claim with its evidence chain: 'is this use of it sound', in the newsroom's phrase, not 'is this true'. Proposed price: 1p per claim read, 5p per claim with its captures opened, 20p per claim re-verified on request.
- **The fact creator's share.** The newsroom's economics page argues a 60/25/10/5 split between the creator of the fact, the checker, the publisher and the rails. On this site the creators are the agencies, the researchers and the reporters whose pages are captured; the checker is the collector agent and the verifier; the publisher is this site. The split is argued, not implemented: nothing here pays anyone.
- **Reading the vault itself.** A reader who wants the bytes rather than this site's reading of them would be sold a read-only snapshot of the evidence vault for a fixed sum, opened in the browser with a read key. The captures are third-party pages and are not for republication, so this stays a proposal until the rights question has an answer.
- **An agent's subscription.** An agent that briefs an executive every morning would pay per briefing regenerated, metered by the same component, with the balance kept in the agent's own vault rather than a browser. The meter already fires an event per charge; nothing listens to it here.

None of this is live. The newsroom's pages on [paying the fact creator](https://newsroom.sgit.ai/economics/index.html) and [provenance as the product](https://newsroom.sgit.ai/provenance/index.html) carry the argument; this site is the first with a claim table granular enough to price.

## What this story cost to assemble, as a model

A model of what this story cost to assemble, in units counted from the vault and the repository. The unit prices are assumptions, labelled as such; the counts are not.

| Unit | Count | Assumed price | £ | Why that unit |
|---|---|---|---|---|
| sources captured | 144 | 5p | 7.20 | one headless-browser capture with six files and their hashes |
| captures (dated page states) | 137 | 5p | 6.85 | the same page captured again is a new unit, because the series is the record |
| source notes written | 143 | 20p | 28.60 | an agent reading a page and writing what it says, who says it and what is odd |
| claims traced | 70 | 10p | 7.00 | one claim, its status and its sources |
| timeline events dated | 68 | 5p | 3.40 | one event, its time, its source and whether the time was stated or converted |
| pages built | 63 | 0p | 0.00 | the build is deterministic and costs nothing to run again |

Total at those assumptions: **£53.05**. The counts are from the data files named; the prices are the site's assumptions and a reader is invited to substitute their own. What the model leaves out is the editor's time and the model inference behind each agent run, neither of which is counted anywhere yet; the honest column on this is *not measured*.

## The prices, as data

{ "storageKey": "php-story.meter.v1", "start": 500, "symbol": "\u00a3", "prices": { "story": 2, "briefing": 5, "analysis": 3, "evidence": 1, "page": 1, "free": 0 }, "topup": { "amount": 500, "link": "" } }This block is `data/billing.json`, which is also what every page's meter config is generated from, so the table above and the meter cannot disagree.


---
site v0.2.8 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/billing/index.html
