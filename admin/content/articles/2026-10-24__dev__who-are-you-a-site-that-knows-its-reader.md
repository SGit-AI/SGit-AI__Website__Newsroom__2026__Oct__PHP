---
slug: who-are-you-a-site-that-knows-its-reader
title: Who are you? A site that knows its reader in two taps, with or without an account
dek: The editor wants this site built around the person reading it. Here is the design. Two questions, what you need to do and how technical you are, place every reader in one of sixteen personas, each with a name, a first screen and a path. It works from the first visit with nothing but the browser's own storage, and follows you across devices once you sign in with a key. And it lets the newsroom see, cohort by cohort, which journeys work. Mockups, the plan, and the five decisions it waits on.
role: dev
origin: house
author: dev@php.newsroom
written: 2026-10-24
as_of_version: 0.14.24
vault_commit: 1845598d9a38
data_as_of: 2026-10-23T16:04Z
---

**24 October 2026.** This is a proposal, not a release. The pictures below are mockups, marked as such, made against the site as it stood today (v0.14.22) by a designer agent working with the dev desk. The figures in them are placeholders taken from the site; the live pages are the record. What is built, what waits for a decision and what waits for the login on pki.sgit.ai are listed at the end.

## The idea

The editor's brief, in his words: push readers to say who they are "very fast", then give each one a path built for them. Someone who sends this site to a C-level executive should be sending the executive's view. It must work without logging in (the browser's own storage) and with logging in (a key, about to be wired in through pki.sgit.ai), so that the site follows the reader from machine to machine. The reader gets a user area, messages in and out, and graphs of what they have seen and what is left. The newsroom can then see, cohort by cohort, which journeys work, and name them.

Today the site asks "Who are you?" with a list of sixteen readers in a menu, and the question is not on the first screen of any page. On a phone the front page's headline starts 452 pixels down.

## Two questions, sixteen readers

The design asks two questions. Each has three answers, and "not answered" counts as a fourth:

| | not answered | Not technical | Technical | I know PHP |
| --- | --- | --- | --- | --- |
| **not answered** | Newcomer, Kit | Plain-English reader, Pat | Technical reader, Sky | Knows PHP, Remy |
| **Understand it** | Catching up, Lou | Curious reader, Alex | Journalist or analyst, Rowan | Security researcher, Ash |
| **Decide** | Decision maker, Dana | Executive, Jordan | CISO, Robin | CTO, Avery |
| **Fix or act** | Hands-on, Kai | Website owner, Casey | Incident responder, Sam | PHP engineer, Drew |

Four answers each way gives 4 x 4 = 16 cells, which is the count the editor arrived at. Three questions would give 64, too many to design for or to measure.

The designer tested five other pairs before this one:
- seniority by skill;
- whether you run PHP, by skill;
- time to read, by skill;
- today's five reader groups by depth;
- the editor's three audiences alone.

This pair is the only one where both questions can be answered in one tap without thinking about job titles, both change what the first screen should be, and the editor's three audiences (the executive, the CISO, the operator) each land in their own cell.

Nine of today's sixteen readers keep their names as the cells above. The other seven become roles inside a cell, and keep their briefings:
- the CFO and the programme manager, inside the executive;
- the data protection officer, inside the CISO;
- the head of AppSec, inside the CTO;
- the developer, inside the PHP engineer;
- the analyst, inside the journalist;
- the communications team, inside the curious reader.

A half-answered reader is a designed state, not a fallback. Dana has said "Decide" and nothing else, so her page asks one question: "Is the technical side yours, or your team's?"

How much of the site you see stays a separate dial, renamed in readers' words: Short, Full, Everything. Plain-English readers start on Short.

## The first visit

![On a phone: the header in one line, the day's headline at the top, and the two questions straight under it, three buttons each, with a skip link](/assets/articles/who-are-you-a-site-that-knows-its-reader/chooser-phone.png "Mockup. The first screen on a phone: the headline, then two questions. Either answer alone is enough; skipping leaves you as the Newcomer.")

The headline stays in the top hundred pixels and the two questions sit directly under it. One tap is enough and two is the most. "Skip: just the news" is a choice too. The answer is kept in the browser and nothing is sent about who you are. After the first tap the header already shows who the site thinks you are:

![The same screen after tapping Decide: the header chip reads Dana, and a Go button has appeared](/assets/articles/who-are-you-a-site-that-knows-its-reader/chooser-phone-one-tap.png "Mockup. One tap (Decide) makes you Dana, the decision maker; the second row is optional.")

## The executive and the engineer

The executive's home answers what a board will ask, and is built to be sent on:

![The executive's home: the headline, a thirty-second answer for Jordan, five tiles, six questions the board will ask with a status each, Send this to your board, the view's assumptions, a reading path and what is folded away](/assets/articles/who-are-you-a-site-that-knows-its-reader/exec-home-desktop.png "Mockup. Jordan, the executive: the answer in thirty seconds, six questions with their status, a link to send the same view to the board, and the code, the claims and the sources folded away, one tap from view.")

The link it sends carries the reader type and nothing else: `?for=decide-plain`, or `?for=exec`. There is no sender, no campaign and no name. The person who opens it sees the view as it was sent, with a strip that offers to keep it:

![On a phone, opened from a link: a strip under the header reads Sent to you as the executive view, with Keep it and Not me](/assets/articles/who-are-you-a-site-that-knows-its-reader/exec-home-phone-from-link.png "Mockup. What the board member sees when the CISO sends the executive view.")

The PHP engineer's home starts from what to do:

![The engineer's home: a strip of fixed versions, CVEs, scores and the US exploited-list status; a checklist of next actions; the reader's stack; the version ladder; what changed](/assets/articles/who-are-you-a-site-that-knows-its-reader/engineer-home-desktop.png "Mockup. Drew, the PHP engineer: versions and scores in one line, a checklist that ticks as you read, your own stack from /stack/, and the explainer and the board's questions folded away.")

## An account with no password

The site stays static: no server sessions, no cookies, no account database. The reader's vault and a key per device are the account.

- **Before signing in,** everything lives in the browser: who you are, what you have read, your notes, your stack and your feeds. All of this exists today, in local storage.
- **Signing in** makes a key pair on the device and opens or makes the reader's vault, the same vault the Ask pane and the phone app already use. The vault key is then sealed to that device, replacing today's plain-text copy in local storage, which any script on the site could read.
- **Another device** is added by scanning a code from the first one, which seals the vault key to it. The key is never shown, typed or sent in the clear.
- **Lost every device:** a recovery sheet, printed once, is the reader's own. The newsroom keeps no copy and cannot reset it.

![Sign in, in five steps: your reading so far stays; this device's key; your vault; the vault key sealed to the device; optionally, a handle on pki.sgit.ai](/assets/articles/who-are-you-a-site-that-knows-its-reader/claim-desktop.png "Mockup. Signing in takes about a minute and none of it is needed to read the site. Only the last step, a handle others can find you by, waits on pki.sgit.ai.")

The user area holds the rest. It shows who you read as, your devices, what is left for you, messages (in from the newsroom, signed; out as signed feedback), your Ask conversations and a table of where each of your things lives:

![The user area: the reader type, the account with its device fingerprint and vault, progress, signed messages, recent Ask conversations, and where your things live](/assets/articles/who-are-you-a-site-that-knows-its-reader/you-desktop.png "Mockup. /you/, signed in. The example fingerprint, vault and messages are made up.")

## What you have seen, and what is left

Every reader type has its own set of items. The site already records, in the browser, which items you have read and whether they changed after you read them. Drawn as one dot per item, that becomes a map of your view:

![What you have seen: 19 of the 35 things written for you, 2 changed since; a dot per item in rows by part; what is left, in order; 462 items outside your view; items read per day](/assets/articles/who-are-you-a-site-that-knows-its-reader/seen-desktop.png "Mockup. Computed in your browser from your own reading record; nothing is sent. Signed in, it merges every device. The per-day chart needs the linked history, which is off unless you turn it on.")

## Cohorts, and the line we do not cross

The telemetry already separates readers from the editor, the team, test browsers and crawlers. The design adds three fields to the event:
- **the reader type,** for example `decide-plain`;
- **how it was set:** chosen, from a link, or the default;
- **a few named steps:** the chooser shown and finished, a view shared, signed in.

That is enough to name journeys per cohort and count them. For example, "board-ready" is an executive who reads the briefing and sends it on. "Sent and bounced" is a link opened and left after one page. It also answers the question from CI-003: of the readers who start on the front page, how many reach a briefing, the guidance or the evidence, by device and by reader type, week by week.

The same design takes things out:
- **Out of the event:** the city, the region, the time zone and the minute. Next to a reader type, they could point at one person.
- **The location lookup:** today the browser asks a third-party service (ipapi.co or ipwho.is) for the reader's country, and that service sees the reader's IP address. The site's own events have never carried the address. The country would come from the time zone instead.
- **Small cohorts:** a reader type's counts are published only when it has at least ten sessions.
- **Signed in, the event is the same:** no key, no vault and no name. A history linked to you is opt-in, lives only in your own vault, and only your own charts read it.

## Where it stands, and what it waits on

The plan is twelve steps, each released on its own:
- **Without the login:** eight of them can be built now, from the reader types as data through to the sealed vault key and the reader's own graphs.
- **With the login:** signing in with a handle, and messages to a reader, wait on pki.sgit.ai.
- **Other owners:** some steps touch other desks' files (the reader list and the header are the story-site agent's, the device keys the conductor's), so they are on the board under their names.

Five decisions are the editor's:

1. **The two questions and the sixteen names,** including the CTO moving to the decision layout and the website owner moving from Understand to Fix or act.
2. **A reader's vault key is sealed only to that reader's own devices,** never to the newsroom's root key. The rule that every secret is also sealed to the root was written for the team's vaults; applied to readers, it would let the newsroom open every reader's record. This changes the security requirements, so it goes through security review.
3. **The privacy line for cohorts:** the reader type in the event; no city, region, time zone, minute or third-party lookup; the threshold of ten; a switch on /you/.
4. **Messages:** at first, only the newsroom's enrolled agents may write to a signed-in reader, and readers cannot write to each other.
5. **The first screen:** the two questions above everything but the headline for a first-time reader, and the view renamed Short, Full, Everything.

## Found on the way

- **Plain-text vault key.** The vault key is kept in plain text in local storage when a reader ticks "remember" in the Ask pane or the phone app. That is the dev desk's code. The sealed key in the sign-in design replaces it.
- **The telemetry article.** /articles/the-telemetry-tools/ says each event's place comes from "a geolocation lookup", but not that the lookup service sees the reader's address. It will say so.
- **Sixteen, not fifteen.** The site says "fifteen readers" in places; there are sixteen.
