# In context: php2shell against Kaminsky, Heartbleed, Shellshock, Log4Shell and the last PHP RCE

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Ten landmark vulnerabilities with their CVE records and KEV rows, the KEV catalog counted, and what the comparison says about severity, exposure, urgency and the discovery pipeline.

# In context: php2shell against the flaws that came before

In plain English How php2shell compares with famous past flaws such as Heartbleed and Log4Shell, using the official record of which ones were exploited.

The editor has worked in security long enough to remember Kaminsky's DNS flaw and Heartbleed, and asked whether this one is as big as the morning's coverage made it. The honest way to answer is a table: ten landmark flaws, each with its CVE record fetched into the vault and its row in CISA's Known Exploited Vulnerabilities catalog, captured on 22 October. The catalog is the one public, dated, machine-readable record of 'this was exploited', and php2shell is not in it yet.

Comparators chosen by the editor's memory and the KEV catalog, not by any ranking. Dates are from the CVE records fetched by this site into the vault and from the CISA KEV catalog captured on 22 October; the 'exploited by ransomware' column is CISA's field.

| CVE | Where it was | Published | Added to KEV | Ransomware use | What happened | Why it is here | Record |
|---|---|---|---|---|---|---|---|
| **CVE-2008-1447** DNS cache poisoning (Kaminsky) | the DNS protocol as implemented in BIND and others | 2008-07-08 | not in KEV | … | Coordinated multi-vendor patch day on 8 July 2008; details withheld for 30 days and leaked after 13; the patch was source-port randomisation, not a code fix. | Predates KEV (2021). The disclosure model it set, a synchronised patch day with an embargo, is the one php2shell tried and lost two days of. | [CVE record](../sources/cve-cve-2008-1447/index.html) |
| **CVE-2012-1823** PHP-CGI query string (php-cgi) | PHP, sapi/cgi | 2012-05-11 | 2022-03-25 | Unknown | Disclosed by accident at a CTF; exploited within days; still in KEV a decade later. | The first time a PHP core bug put every php-cgi site at risk. Only php-cgi, not mod_php or FPM. | [CVE record](../sources/cve-cve-2012-1823/index.html) |
| **CVE-2014-0160** Heartbleed | OpenSSL TLS heartbeat | 2014-04-07 | 2022-05-04 | Unknown | Memory disclosure, not code execution; named, branded and logoed; patched in days by big sites, over years by the long tail. | The reference point for 'everyone is affected'. Added to KEV eight years after disclosure. | [CVE record](../sources/cve-cve-2014-0160/index.html) |
| **CVE-2014-6271** Shellshock | GNU Bash | 2014-09-24 | 2022-01-28 | Unknown | RCE through environment variables; mass scanning within hours; the first fix was incomplete and followed by more CVEs. | The precedent for 'the first patch was not the last'. | [CVE record](../sources/cve-cve-2014-6271/index.html) |
| **CVE-2017-5638** Apache Struts (Equifax) | Struts Jakarta multipart parser | 2017-03-11 | 2021-11-03 | Known | Exploited within a day; the Equifax breach followed two months later from an unpatched system. | Also a multipart parser. The lesson was about patch latency, not about the bug. | [CVE record](../sources/cve-cve-2017-5638/index.html) |
| **CVE-2019-11043** PHP-FPM buffer underflow | PHP-FPM with specific nginx configs | 2019-10-28 | 2022-03-25 | Known | Public PoC on disclosure; exploitable only with a particular nginx fastcgi_split_path_info pattern. | A PHP core RCE whose real exposure was a fraction of the headline because it needed a specific configuration. | [CVE record](../sources/cve-cve-2019-11043/index.html) |
| **CVE-2021-44228** Log4Shell | Apache Log4j 2 | 2021-12-10 | 2021-12-10 | Known | In KEV the day it was published; exploited at scale within hours; CISA emergency directive; months of follow-up CVEs. | The closest precedent in shape: a flaw in a runtime library below the application, trivially triggered, reachable through any input path. Same-day KEV listing is the marker php2shell has not yet earned. | [CVE record](../sources/cve-cve-2021-44228/index.html) |
| **CVE-2022-22965** Spring4Shell | Spring Framework on JDK 9+ | 2022-04-01 | 2022-04-04 | Unknown | Leaked before the patch; named after Log4Shell; real exposure needed a specific deployment shape (WAR on Tomcat). | The precedent for a leak forcing the release, and for a '-Shell' name outrunning the actual exposure. | [CVE record](../sources/cve-cve-2022-22965/index.html) |
| **CVE-2023-34362** MOVEit Transfer | Progress MOVEit | 2023-06-02 | 2023-06-02 | Known | Exploited before disclosure by one group (Cl0p); thousands of organisations' data taken; same-day KEV. | The precedent for exploitation preceding disclosure, which Amazon's 17 October honeypot hit suggests here. | [CVE record](../sources/cve-cve-2023-34362/index.html) |
| **CVE-2024-4577** PHP-CGI argument injection (Windows) | PHP on Windows in CGI mode | 2024-06-09 | 2024-06-12 | Known | Exploits in the wild one day after disclosure (Akamai); KEV three days after; ransomware use recorded. | The most recent PHP core RCE before this one: in KEV within three days. php2shell, broader in scope, is not in KEV after one day. | [CVE record](../sources/cve-cve-2024-4577/index.html) |
| **CVE-2026-109618 and CVE-2026-109619** php2shell | PHP engine (Zend allocator, request lifecycle) | 2026-10-21 | not in KEV as of 2026-10-22T08:15Z | … | Leaked two days early; patched a day early; five agencies say take systems offline or isolate; governments and councils pulled sites; millions of attempts seen at one CDN; no named organisation saying it was compromised through php2shell in any captured source as of 20:50 UTC on 22 October. | The row this site exists for. What it shares with Log4Shell is shape; what it has not yet shown is Log4Shell's exploitation. | [CISA](../sources/cisa-kev-json/index.html) |

## The catalog itself, counted

Catalog version 2026.10.21: 1,754 entries, 361 with known ransomware use, 13 with PHP in the vendor, product or name, of which three are PHP core: CVE-2012-1823 (added 2022-03-25); CVE-2019-11043 (added 2022-03-25, ransomware known); CVE-2024-4577 (added 2024-06-12, ransomware known). Counted from the captured file. [CISA](../sources/cisa-kev-json/index.html)

| Year | CVEs added to KEV |
|---|---|
| 2021 | 311 |
| 2022 | 555 |
| 2023 | 187 |
| 2024 | 186 |
| 2025 | 245 |
| 2026 | 270 |

| 2026 | Added |
|---|---|
| 2026-01 | 17 |
| 2026-02 | 28 |
| 2026-03 | 26 |
| 2026-04 | 31 |
| 2026-05 | 21 |
| 2026-06 | 23 |
| 2026-07 | 26 |
| 2026-08 | 31 |
| 2026-09 | 43 |
| 2026-10 | 24 |

## What the comparison says

The site's reading of the table above. Positions, with the evidence attached.
- Severity is not exposure. php2shell's 9.2 is a property of the bug; Heartbleed's 'everyone' and Log4Shell's 'everywhere' were properties of deployment. The comparators show both kinds of big: a bug in a runtime that everything sits on (Log4Shell, Shellshock, php2shell) and a bug whose real exposure was a narrow configuration (CVE-2019-11043, Spring4Shell, CVE-2024-4577 on Windows CGI). Which kind php2shell is depends on how many of the 1.57 million unpatched hosts Censys counted are mod_php on x86_64 with the default settings, a number nobody has published.
- Urgency before disclosure was institutional, not public. The PHP project had the fix on 18 October and sat on it for a coordinated release; Cloudflare had rules live nine hours early; Amazon had honeypot hits four days early; agencies published within the hour. That is the Kaminsky model working as designed, right up to the point it leaked. The public alarm came with the agencies' offline advice on the morning of 22 October, which is why the editor's question, 'why was the alarm only raised when it went public', has a factual answer: because the embargo held for everyone who was inside it.
- The KEV test. CISA lists a CVE when it has reliable evidence of exploitation in the wild. Log4Shell and MOVEit were listed the day they were published; CVE-2024-4577 in three days. php2shell was not listed after one day, with Amazon saying it is 'broadly exploited' against honeypots and NCSC NZ 'aware of reports'. Either the evidence has not reached CISA's bar, or attempts against sensors are not the same as exploitation of victims. This site will record the day it is added, if it is.
- What is new is not the bug class but the discovery pipeline. The OOM-bailout pattern was seen in 2024 and shelved because nobody could prove exploitation. Three teams with model assistance proved it inside three weeks of each other. The historical comparison that matters is therefore not Heartbleed but the gap between 'theoretically exploitable' and 'proven', which used to be months of expert work and may now be days.

The signals that would move php2shell into the catalog are on [the exploitation page](../exploitation/index.html); what was taken offline, and by whom, is on [impact](../impact/index.html).


---
site v0.11.2 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/context/index.html
