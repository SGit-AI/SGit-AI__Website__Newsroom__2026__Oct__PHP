# Impact: taken offline versus compromised

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Two ledgers for php2shell: every system reported taken offline with who said so, and every claim of compromise with its basis. As of the latest capture, no named organisation has confirmed a compromise.

# Impact: what was taken offline, and what was compromised

In plain English Two lists: who took websites offline (many, as a precaution), and who was actually broken into (nobody confirmed).

Two ledgers, because they measure different things. Taking a system offline is a decision an operator makes and can confirm, and the first table is full. Being compromised is a fact only evidence establishes, and the second table has, as of the latest capture, no confirmed entry. That gap is the most important finding on this site: the reported cost of php2shell so far is the cost of precaution.

Two ledgers. The first is systems taken offline, which is a decision an operator makes and can confirm; the second is systems compromised, which only evidence can establish. The columns say whether the entry comes from the organisation itself or from the press, because the difference is the whole point.

## Taken offline

| Who | What happened | When | Who says so | Status | Sources |
|---|---|---|---|---|---|
| **NCSC.nl (the Dutch national cyber security centre's own site)** NL | Taken offline 'uit voorzorg' (as a precaution); DigiD, MijnOverheid and Overheid.nl also offline; no signs of active exploitation of those services at the time | 2026-10-21 | the Dutch government (Rijksoverheid news) | confirmed | [Rijksoverheid / NCSC-NL](../sources/rijksoverheid-ncsc-php-news/index.html) [Dutch IT Leaders](../sources/dutchitleaders-websites-offline/index.html) [TPO.nl](../sources/tpo-nl-digid-offline/index.html) |
| **Finland's government public web services (Valtori)** FI | Incoming public traffic restricted from 12:45 local (09:45 UTC); described as preventive, not a response to a breach; internal networks unaffected | 2026-10-21 09:45 UTC | Yle and Helsinki Times quoting Valtori and the National Cyber Security Centre Finland | reported | [Yle](../sources/yle-finland-government-sites-shut/index.html) [Helsinki Times](../sources/helsinkitimes-finland-shutdown/index.html) |
| **Latvia: several state digital resources, lsm.lv, 112.lv** LV | Access restricted from abroad; state website platform patched by 20:00 UTC; lsm.lv and 112.lv restored; restrictions on others possibly until 26 October | 2026-10-21 15:25 UTC | CERT.LV itself | confirmed | [CERT.LV](../sources/certlv-php-preventive/index.html) |
| **Wikimedia Foundation: 'a number of other systems'** US | 'taken down a number of other systems as a precautionary measure until they can be safely patched'; parts of Wikipedia affected | 2026-10-21 | the Foundation, as quoted by CNN and The Cyber Express; the BBC | reported | [CNN](../sources/cnn-php2shell-websites-shut/index.html) [The Cyber Express](../sources/cyberexpress-php2shell-gov-sites/index.html) [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| **Weird Gloop (RuneScape and other game wikis, about 500 million page views a month)** UK | Web servers off for 13 hours, 'the longest outage we've ever had'; about 94% of page views still served from cache | 2026-10-21 | Weird Gloop itself | confirmed | [Weird Gloop](../sources/weirdgloop-blog-php2shell/index.html) |
| **City of Edinburgh Council** UK | Website offline from late Wednesday afternoon; the council says 'essential maintenance' and is 'waiting on an update from our provider'; it has not confirmed a link | 2026-10-21 | The Scotsman quoting a council spokesperson | reported | [The Scotsman](../sources/scotsman-edinburgh-council-offline/index.html) |
| **Oxford City Council and Oxfordshire County Council** UK | Sites removed from service; the city council's post: 'a precaution because of a worldwide issue with the underlying technology and is not a cyber incident' | 2026-10-21 | Oxford Chronicle quoting the councils' social posts | reported | [Oxford Chronicle](../sources/oxfordchronicle-councils-offline/index.html) |
| **Metropolitan Police, Office for Budget Responsibility; errors on Bristol, Lambeth and Barnet council sites** UK | Reported unavailable; a minister said there was no breach of Budget security | 2026-10-21 | LBC, Insurance Business, East Anglian Daily Times | reported | [LBC](../sources/lbc-uk-websites-offline/index.html) [Insurance Business](../sources/insurancebusiness-uk-councils-met/index.html) [East Anglian Daily Times](../sources/eadt-minister-budget-no-breach/index.html) |
| **French government services; the University of Geneva; the BBC; online shops** FR, CH, UK | Listed by the BBC as affected or taken offline | 2026-10-22 | BBC News | reported | [BBC News](../sources/bbc-live-ckgel5xp2xv9t/index.html) |
| **Government sites in the Netherlands, France, Germany and Belgium** EU | Listed by Reuters' factbox as having taken sites offline | 2026-10-21 | Reuters, via Global Banking and Finance | reported | [Reuters factbox, via Global…](../sources/reuters-factbox-websites-offline/index.html) |

## Compromised

| Claim | Basis | Status | Sources |
|---|---|---|---|
| Amazon: 'PHP2Shell is now being broadly exploited in the wild' | MadPot honeypot telemetry: an attempt on 17 October, proof-of-concept attempts from 02:00 UTC on 21 October, use against sensors 'almost immediately' after release. 'It's unclear if any of these attempts would have succeeded in real-world systems.' | reported (primary party); attempts against sensors, not victims | [Amazon](../sources/aws-security-blog-madpot/index.html) |
| Cloudflare: thousands of attempts in the ten hours before announcement, tens of thousands within 45 minutes after, hundreds of thousands within two hours, 'millions now' | Matthew Prince on X, 22 October 01:25 UTC; attempts seen at the edge, not compromises; no blocked count published | reported (primary party) | [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) |
| Imperva: no traffic matching the exploit patterns during pre-disclosure monitoring | Imperva had the details under embargo and monitored customer traffic before the announcement | reported (primary party); a negative finding | [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |
| Huntress: no exploitation observed on partner systems as of 20:30 UTC on 21 October; no public exploit code known | Huntress's own rapid-response post | reported (primary party); a negative finding | [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| watchTowr: active exploitation attempts seen; the flaws 'exploited in the wild' | watchTowr's pages, which block automated capture (HTTP 403); known through search summaries only | unverified the source could not be read | [watchTowr](../sources/watchtowr-php2shell/index.html) [watchTowr](../sources/watchtowr-php2shell-faq/index.html) |
| Chainguard's honeypots trapped IPs from China and Russia; 'several other security vendors' reported exploits in the wild | Dan Lorenc, as reported by The Register; vendors not named, no evidence published | reported, second-hand | [The Register](../sources/theregister-php-blames-chainguard/index.html) |
| NCSC New Zealand: 'aware of reports of active exploitation' | Unattributed | reported | [NCSC New Zealand](../sources/ncsc-nz-alert-php/index.html) |
| Weird Gloop: 'extremely likely that a bunch of old PHP fansites and forums have had their databases compromised' | The author's expectation; no case named | unverified an expectation, not a finding | [Weird Gloop](../sources/weirdgloop-blog-php2shell/index.html) |
| A named organisation confirms it was compromised through php2shell | No captured source carries one | none found | [CISA](../sources/cisa-kev-json/index.html) [Huntress](../sources/huntress-php2shell-rapid-response/index.html) [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |

## What the two ledgers say together

- **Precaution was the dominant response**, and it was institutional: national CERTs, state IT providers and councils pulled sites on advice, often before the patch existed, and said so. The one operator who measured it served 94% of its traffic from cache for 13 hours.

- **Attempts are not compromises.** Cloudflare's millions and Amazon's honeypot hits are requests matching a shape at the edge or against a sensor. Nobody has published a count of successful exploitations, and the parties best placed to see one (CISA, Huntress, Imperva) report none.

- **Absence of evidence is weak here.** The detection authors are explicit that default web logs cannot show the attack shape and that no standard log carries the worker id the cross-request bug needs. A quiet log is not a clean host.

- **The question that would settle it** is one that no captured source answers: of the 1.57 million unpatched hosts Censys counted, how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell. That number is what 'blast radius' means at internet scale, and it does not exist yet.

What a compromise of one system would reach is on [the blast-radius section](../flaws/index.html#blast); how to tell is on [detection and defence](../defence/index.html).


---
site v0.5.7 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/impact/index.html
