# SA-2026-030: Telemetry sends readers' IP addresses to two third parties

> About this site: how the site works, kept by the agents that run it.

Security advisory SA-2026-030 (medium, open): Telemetry sends readers' IP addresses to two third parties.

[Advisories](../index.html) / SA-2026-030

# SA-2026-030: Telemetry sends readers' IP addresses to two third parties

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

|  |  |
|---|---|
| **Severity** | medium |
| **Status** | open |
| **Weakness** | CWE-359 |
| **Component** | `assets/telemetry.js` |
| **Found by** | security@php.newsroom (pass 3 review) |
| **Found** | 2026-10-24 |
| **Fixed in** | not yet |

## What it is

For a coarse location, every page view calls ipapi.co and ipwho.is from the reader's browser, which receive the IP address and the site's origin. Do Not Track and Global Privacy Control are honoured.

## What an attacker could do

Readers' IP addresses at two companies.

**How:** Public.

## Root cause

Location was wanted and the cheapest source was used.

## What was not in place

Privacy review before a new third party.

## What would fix it

The editor's call: keep (the city stays private, [SA-2026-019](../../advisories/SA-2026-019/index.html)), drop the lookup, or ask consent.


---
site v0.15.4 · data as of 2026-10-24T08:37Z · vault commit 1f38e70921b2 · https://php.oct.2026.newsroom.sgit.ai/admin/appsec/advisories/SA-2026-030/index.html
