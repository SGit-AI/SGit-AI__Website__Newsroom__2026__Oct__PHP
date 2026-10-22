# Who reads this site: anonymous telemetry over an append lane

What every page sends to the telemetry lane, the published write-only credential, the key it is encrypted to, the counts, and what they are worth.

# Who reads this site

Every page sends one anonymous event to a write-only lane on a separate, private vault: which page, the referrer's host, the visitor's country, region and city from a geolocation lookup, language, screen class and time zone, with a random session id that lives in the tab. No IP address, no cookie, no name, no user-agent string. The event is encrypted in your browser to the key below before it leaves; the lane's reply is a blind `{"ok": true}`. Do Not Track and Global Privacy Control switch it off. The brief is on [briefs](../briefs/index.html#2026-10-22__telemetry-over-an-append-lane).

## What this page carries

One anonymous event per page per session: path, referrer host, country, region, city (from a geolocation lookup; the lookup service sees your IP, the event does not carry it), language, screen class, time zone, a random session id, the site version. Encrypted in your browser to the key below and written to a write-only lane. The brief and the counts are in the admin section.

**Lane** vault `84wr8mib` on `https://dev.send.sgraph.ai` · **append token** `43ed24b413cdf8c2405d0b72cddcd36c04fd7ae1ad852b872ed25727b6d61fb3` (write-only; publishable by design) · **encrypted to** `sha256:8b2b26ff9386078f`

-----BEGIN PUBLIC KEY----- MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA2eWJSSnd9+s2VjObHUc6 acOgnVxCaUavKP7eex/kMjUhaSCMHDIr6phTVS/mtjs+5toVNtYPkMS1eHbo1ivu gOiCVn5iJz4r75Lrn9t6Kj7YiBQzNpFngeDAq3RhI9BkfwVtc6Ds/hNIiaHXdZAF p9Fbd3GiH3aY6EK1iHGIRD2QF/eIcI5tEtzEZG8fa+AyyDrK2otOXgI2SlabA+bh sm344AfE+3FIbre/NqP6NLG4a0Odtw5xLfNUiJRP2kuFapj0ryVeRkyom30UNeCQ jS7JHZKkumeqAglLbRDyJ0GSkbbQdzGUSd8B++hHgf+rwPsZG9BxzTNT2jc4LGzM eB8fxr4ujMCCU35ZsOWQBgjXwnzpOnFCxdXsHKIq13Yuxc+2sJiSBmaYZJDVkfxx SzVowtBHS1Ad1qRZC/dojFmvaHqYOEajHsxH/aJokW5LqCLuYBir9vniqS7GkJNO 2HBkozg3m/gjNMB6k+g6hz0brWfZ5/r28bOdRtBoof7AEcXzHYzmCX6AdDQ7ho+A gdLDNaSYLyTH0b2OIwDTaU+/tSdTQ+v8D7b3gXQwn0Fbe0YTbL1ZIxrILxzKuEhX 2WAKYR/IrJeCVhy6yKJtDv9iQ8j98+CFFbTfpiTXJ/DIS99XJgj1m9fO35QUJWFO JM7i64/3L87WlSvDQftSensCAwEAAQ== -----END PUBLIC KEY----- The geolocation lookup goes to `https://ipapi.co/json/` then `https://ipwho.is/`; that service sees your IP address and returns a country, a region and a city; the event keeps the three names and nothing else. The vault server sees that a lane received something, its size and the time, and the requesting IP, as any server does.

## The counts

Report as of **2026-10-22**: **4** events from **1** sessions (1 test or undecryptable rows excluded). Counts over events received in the lane. Every event is an untrusted claim: the token and the public key are published, so rows can be forged or flooded. Visitors with blockers do not appear. No row leaves the vault.

| Country | Events |
|---|---|
| US | 4 |

| Region | Events |
|---|---|
| California | 4 |

| Referrer host | Events |
|---|---|
| (none) | 4 |

| Screen | Events |
|---|---|
| desktop | 4 |

### By page

| Page | Events |
|---|---|
| /index.html | 1 |
| /admin/telemetry/index.html | 1 |
| /admin/vault/index.html | 1 |
| /admin/board/index.html | 1 |

### By day

| Day | Events |
|---|---|
| 2026-10-22 | 4 |

## What the counts are worth

- Every row is an untrusted claim: the token and the public key are on this page, so anyone can add rows or flood the lane (1000 pending per token, then the lane returns 507).

- The counts are a floor: visitors with blockers, Do Not Track or Global Privacy Control do not appear.

- Nobody can be identified from them, by design, and no row leaves the vault; the drainer publishes counts.

Mechanics: `assets/telemetry.js` sends; `admin/build/telemetry_drain.py`, run by whoever holds the telemetry vault key, lists the lane with the enum key, fetches, decrypts with the private key, marks processed and writes `reports/`; `data/telemetry-report.json` is the latest report, copied into this repository at each drain.


---
site v0.2.8 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/admin/telemetry/index.html
