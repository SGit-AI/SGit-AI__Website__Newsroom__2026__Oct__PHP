# The second stories: exposed, attempted, exploited, and what was within reach

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

php2shell as signals: the ladder from websites that use PHP to the sites that were exploited and held something worth reaching, the four kinds of signal and what each shows now, and the time each barrier became available.

# The second stories: exposed, attempted, exploited, and what was within reach

The second stories of php2shell, as signals. The first story counts attacks. The second asks who was exposed and was not hit, who was hit and what that says about them, and what was within reach behind the server. This page is the site's analysis, built from captured sources: each layer, signal and barrier cites the evidence it rests on, and says plainly where there is none.

## From exposed to what matters

Each layer is a smaller population than the one above, until the evidence runs out. The two bars are counts of the same thing, hosts, on one linear scale: 1.57 million of 2.6 million were unpatched on the first day; a dashed box is a layer nobody has measured; a single line is zero. The units change down the ladder, from a share of websites to hosts to attempts, and the ladder says so rather than drawing them as one funnel.

| Layer | How many |  | Signal | Status | Sources |
|---|---|---|---|---|---|
| **Websites that use PHP**of websites whose server-side language a survey can identify | **about 69 to 70%** |  | [exposure](#f-exposure) | reported | [Feross Aboukhadijeh on X on X](../sources/x-feross-chainguard/index.html) [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [OpenAI on X](../sources/x-openai-php2shell/index.html) |
| **Internet-facing hosts that expose PHP**hosts, one scanner's count (VulnCheck) | **2,608,039** |  | [exposure](#f-exposure) | reported | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| **Still unpatched on 21 October**hosts, Censys's count on the day of the release | **1.57 million** |  | [Patching](#f-patching) | reported | [SecurityWeek](../sources/securityweek-exploitation-days-before/index.html) |
| **On a deployment where code execution has been shown**mod_php with default settings is demonstrated; PHP-FPM is disputed; nobody has counted either | **not measured** |  | [Internal vulnerability](#f-internal) | disputed | [PHP](../sources/github-ghsa-w8hw-w9fx-j79w/index.html) [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| **Not behind an edge that blocks the request**Cloudflare, Akamai, Fastly and Imperva had rules live on 21 October; how many exposed hosts sit behind one is not published | **not measured** |  | [Network protection](#f-network) | reported | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [Akamai Security Research](../sources/akamai-blog-php-core-rce/index.html) [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |
| **Attempted**requests at one CDN by 01:25 UTC on 22 October; attempts, not sites | **millions of attempts** |  | [Exploitation](#f-exploitation) | reported | [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) |
| **Exploited**named organisations confirming a compromise, in every captured source | **0 confirmed** |  | [Exploitation](#f-exploitation) | confirmed | [CISA](../sources/cisa-kev-json/index.html) [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| **Exploited, and holding something worth reaching**the number that matters: a compromised worker with credentials, data or a path inward | **not measured** |  | [Internal vulnerability](#f-internal) | unverified | [Weird Gloop](../sources/weirdgloop-blog-php2shell/index.html) |

## The four kinds of signal

The editor's four families: what each would show, what it shows now, and what would change it.

### Exploitation signals

*Who is trying, at what scale, and does anything land?*

**Now.** Attempts at scale from the parties positioned to see them; one honeypot hit four days before release; no confirmed compromise; not in CISA's Known Exploited Vulnerabilities catalog. [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) [Amazon](../sources/aws-security-blog-madpot/index.html) [CISA](../sources/cisa-kev-json/index.html)

**What would change it.** The KEV listing; a named victim; a gap between the date a site was compromised and the date it says so.

[Where this site tracks it →](../exploitation/index.html)

### Patching signals

*How fast does the fix reach the servers, and who is left behind?*

**Now.** Releases for 8.2 to 8.5 within the hour, distributions recorded fixed in the NCSC-NL inventory from 15:30 UTC on 21 October, and a long tail: 440 of 724 inventory rows still under investigation at 15:28 UTC on 22 October, about 25 hours after release, and 1.57 million unpatched hosts on the first day. [SecurityWeek](../sources/securityweek-exploitation-days-before/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html)

**What would change it.** Censys or VulnCheck recounting unpatched hosts; the inventory's investigation rows resolving; the end-of-life tail.

[Where this site tracks it →](../patching/inventory/index.html)

### Network protection signals

*What stood in front of the server, and did it hold?*

**Now.** Edge rules live from 03:02 UTC on 21 October at Cloudflare and the same day at Akamai, Fastly and Imperva; Cloudflare saw attackers mutating payloads to get past them; Fortinet's signatures ship in alert-only mode. Some of the devices in front of servers run PHP themselves: Palo Alto lists every PAN-OS and Panorama version as affected, and the inventory has Check Point's firewall web interfaces and NetScaler ADC as vulnerable. [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [Fortinet Community](../sources/fortinet-fortiweb-php2shell/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html)

**What would change it.** A vendor reporting a bypass of its rule; a security appliance compromised through its own PHP.

[Where this site tracks it →](../defence/index.html)

### Internal vulnerability signals

*Once code runs as the web worker, what can it reach?*

**Now.** No captured source describes what was behind a compromised server, because no compromise is confirmed. What exists are the signals defenders were told to look for: a PHP worker spawning a shell or downloading tools, new outbound connections from workers, and the warning that a clean log proves little. [CISA](../sources/cisa-alert-php-20261021/index.html) [Blevene](../sources/gist-blevene-detection-guide/index.html) [JPCERT/CC](../sources/jpcert-at260033/index.html)

**What would change it.** The first incident report that says what the attacker reached: credentials on the host, the database, the internal network, a cloud role.

[Where this site tracks it →](../flaws/index.html#blast)

## Every barrier has a time

The barriers between this bug and a breach, with the moment each became available. A dot is a stated time; a band is a day with no time given. Read across: a compromise after the dot says something about the organisation, not only about PHP.

| Barrier | Available | 21 Oct 00:00 → 22 Oct 16:00 UTC | A compromise after it says the organisation had | Sources |
|---|---|---|---|---|
| **Edge rules at the big WAF providers** | 21 October 2026, 03:02 UTC | Cloudflare, about nine hours before disclosure by its own account; Akamai, Fastly and Imperva the same day | No edge protection, or rules not switched on | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) [Akamai Security Research](../sources/akamai-blog-php-core-rce/index.html) [Fastly](../sources/fastly-blog-php2shell/index.html) [Imperva Threat Research](../sources/imperva-blog-php2shell/index.html) |
| **The first official advice to be ready to take systems offline** | 21 October 2026, 13:45 UTC | the NSA on X, before the CVE records were published | No way to pull a system quickly, or nobody with the authority to decide | [NSA Cyber on X](../sources/nsa-x-2112903220209098897/index.html) |
| **Fixed PHP releases for every supported branch** | 21 October 2026, 14:00 UTC | tags at 13:35 UTC; the advisory at 14:00 | No patch pipeline: the organisation could not rebuild and redeploy PHP in time, or did not know where it ran | [php-src](../sources/github-php-src-tags/index.html) [php.net](../sources/php-net-advisory/index.html) |
| **Configuration mitigations for those who could not patch** | 21 October 2026, 14:00 UTC | in the same advisory | No configuration management: settings could not be pushed to every server | [php.net](../sources/php-net-advisory/index.html) [PHP](../sources/github-ghsa-6wmf-4rv5-p3rp/index.html) |
| **Fixed packages from the operating systems** | 21 October 2026, 15:30 UTC | the first one recorded in the NCSC-NL inventory (Red Hat); Ubuntu, Debian and the Docker image by 16:03 | Routine updates not applied, or the server on a distribution nobody maintains | [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html) |
| **Host and log signals to look for** | 21 October 2026 | CISA's alert, dated 21 October with no time; community Sigma, Suricata and Falco rules followed | No monitoring that would see a worker spawn a shell or call out | [CISA](../sources/cisa-alert-php-20261021/index.html) [Blevene](../sources/gist-blevene-detection-guide/index.html) |
| **Defence in depth behind the worker** | *not a release* | not a release: either it was built before 21 October or it was not there | Credentials the worker can use, a database it can read, an internal network it can call: the reach that turns code execution into a breach | [CISA](../sources/cisa-alert-php-20261021/index.html) [Blevene](../sources/gist-blevene-detection-guide/index.html) |

## The reading
- A site that was exposed and not exploited is evidence too. Attempts ran in the millions and confirmed compromises stayed at zero; the difference is the population this page is about, and nobody has counted it.
- Code execution as the web worker is reach, not yet a breach. Whether it becomes one depends on what that worker can open: the newsroom's question about any secret, 'can the attacker reach the system it opens?', asked of a whole server.
- Every barrier has a time. A compromise after a barrier was available says something about the organisation, not only about the bug: after 03:02 UTC on 21 October, that there was no edge protection in front; after 14:00, that there was no pipeline to patch; and at any time, if the attacker reached anything that mattered, that there was nothing behind the worker.

This page is the site's analysis, marked as research because every row rests on captured sources; the argument it supports is made in Exposed is not exploited: the sites php2shell did not hit, and what a hit will admit.


---
site v0.8.2 · data as of 2026-10-22T11:34Z · vault commit 200d08971937 · https://php.oct.2026.newsroom.sgit.ai/signals/index.html
