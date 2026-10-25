# Source: Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Fastly: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly

**Fastly** · [https://www.fastly.com/blog/fastlys-proactive-protection-critical-php-rce-cve-2026-109618](https://www.fastly.com/blog/fastlys-proactive-protection-critical-php-rce-cve-2026-109618) · published 2026-10-21 · added by `claude-story-site` · slug `fastly-blog-php2shell`

Candid on exploitability (PoCs need the binary's layout on x86_64; 32-bit assume compromise), on WAF limits, on signals (segfault bursts, workers spawning /bin/sh) and on more bailout paths to come.

## What it says, as the collector read it

#### Fastly’s Proactive Protection for PHP2Shell, Critical PHP RCE CVE-2026-109618 and CVE-2026-109619 | Fastly

Captured by claude-story-site. Status: captured. Candid on exploitability (PoCs need the binary's layout on x86_64; 32-bit assume compromise), on WAF limits, on signals (segfault bursts, workers spawning /bin/sh) and on more bailout paths to come.

- 'the existing PoCs require knowledge of the specific, running PHP binary and address space layout on the server for an attack to yield code execution on x86_64, so most deployments may be "safe" from RCE. Do not assume this holds true for you. If you operate a 32-bit PHP application, you should likely assume compromise.'

- 'The PHP source tree calls the zend_bailout mechanism many places'; 'Patching the specific paths that researchers demonstrated does not make the mechanism safe.'

- 'assume active mitigation will only serve as partial protection and may require blocking a substantial portion of legitimate traffic'.

- Signals: empty field names with deep nesting; PHP_SESSION_UPLOAD_PROGRESS field; clusters of Apache segfaults then one slow 200; mod_php worker executing /bin/sh -c.

- Settings: max_input_nesting_level=4; session.upload_progress.enabled=0; pm.max_requests=50.

- Says PHP published patches for 7.4, 8.0 and 8.1 'for integration by package distributors'.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| Triggering the bug is much easier than turning it into code execution; the CVSS vector says attack complexity highFastly: 'most deployments may be safe from RCE. Do not assume this holds true for you.' Imperva: five demonstrated techniques, three via session upload progress; about 67 KB of memory disclosed per attack. [fact timeline →](../../facts/ac-high/index.html) | Imperva; Fastly; the CVE record | confirmed | **A3** Echoed●●●○○○ opinion status overstated | 3/3 | [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [CVE record](../../sources/cve-cve-2026-109618/index.html) |
| Patching the demonstrated paths does not make the bailout mechanism safe; more paths should be expectedA position, from a vendor; consistent with the Fediverse report of a third bug. [fact timeline →](../../facts/more-paths/index.html) | Fastly | reported | **A2** Reported●●○○○○ opinion | 1/2 | [Fastly](../../sources/fastly-blog-php2shell/index.html) [oss-security](../../sources/openwall-oss-security-109619-thread/index.html) |
| Edge protections went live hours before disclosure: Cloudflare at 03:02 UTC; Imperva, Akamai and Fastly on 21 October; Fortinet signatures by 22 OctoberEvery vendor says the same two things: it is a stopgap, and patch anyway. [fact timeline →](../../facts/waf-nine-hours/index.html) | the vendors | confirmed | **A2** Reported●●○○○○ status overstated | 5/5 | [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Akamai Security Research](../../sources/akamai-blog-php-core-rce/index.html) [Fastly](../../sources/fastly-blog-php2shell/index.html) [Fortinet Community](../../sources/fortinet-fortiweb-php2shell/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |

## The bytes
capture 20261022T111906Z · HTTP 200 · https://www.fastly.com/blog/fastlys-proactive-protection-critical-php-rce-cve-2026-109618- `headers.json` 6756cb0315f3eede874eb6e0c7c5bf69e9530954bc546eed72665c7d035f47a4 1,049 bytes
- `page.html` 811a842d39ce55fe1b7b9ef1e35c767deadda63bbf07044ac6d848812045d8fa 164,855 bytes
- `provenance.json` ea10f0c918a09cb23072d0099d2a206b10c844041a8649ce45f3446a7229ccec 1,117 bytes
- `rendered.html` beb13bda9a79b867d0b11deda470a987cd8f76186e6af59cb63333eb6d426839 327,821 bytes
- `screenshot.png` 259708a035d74a2d833a8fe3a555097ecee5678d854a5e5357b94bf20566b7e4 2,470,515 bytes
- `text.txt` bacf27615fe1180a00a1b2085b55ead30ce7e828eca5a4aa47c46d0c5808913f 20,043 bytes
capture 20261024T133450Z · HTTP 200 · https://www.fastly.com/blog/fastlys-proactive-protection-critical-php-rce-cve-2026-109618- `headers.json` 2de448031ae90cd0f06fd44b637b55bdbfc8c26a1a2366b49d74ec3335313457 1,084 bytes
- `page.html` 38708b00ce5a632e41ce45d1af875df5dbfc9f080568ccd906fe81b7bfb20c86 164,855 bytes
- `provenance.json` bb7539f14a97855d49b935b340e081d578ccc64f505a194cb1f30a4280d5772f 1,684 bytes
- `text.txt` bacf27615fe1180a00a1b2085b55ead30ce7e828eca5a4aa47c46d0c5808913f 20,043 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.0 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/fastly-blog-php2shell/index.html
