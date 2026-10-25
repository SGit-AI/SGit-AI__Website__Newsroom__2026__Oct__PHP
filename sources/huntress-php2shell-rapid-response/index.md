# Source: Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Huntress: what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress

**Huntress** · [https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities](https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities) · published 2026-10-21 · added by `claude-story-site` · slug `huntress-php2shell-rapid-response`

As of 16:30 ET (20:30 UTC) 21 Oct: no exploitation observed on partner systems; no PoC built or reproduced; not aware of public exploit code.

## What it says, as the collector read it

#### Rapid Response: php2shell, Leaked Critical PHP Vulnerabilities (CVE-2026-109618 & CVE-2026-109619) | Huntress

Captured by claude-story-site. Status: captured. As of 16:30 ET (20:30 UTC) 21 Oct: no exploitation observed on partner systems; no PoC built or reproduced; not aware of public exploit code.

- Primary negative finding from a managed-detection vendor.

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| No exploitation observed on Huntress partner systems as of 20:30 UTC on 21 October; no public exploit code known to Huntress [fact timeline →](../../facts/huntress-none/index.html) | Huntress | reported | **A2** Reported●●○○○○ disputed | 1/1 | [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |
| None of the public proof-of-concept exploits reviewed by VulnCheck has the correct mechanism; a lab reproduction of the leaked PoC's precondition produced a clean 200The Hacker News says the same of the public code. Fastly: working RCE needs knowledge of the running binary's layout on x86_64. [fact timeline →](../../facts/pocs-wrong/index.html) | rjmendez (detection author) citing VulnCheck; Huntress | reported | **A1** Weak signal●○○○○○ status overstated | 1/2 | [rjmendez, GitHub](../../sources/github-rjmendez-phpup-2026/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |
| 2026-10-21 20:30 UTC | Huntress: no exploitation observed on partner systems (16:30 ET). | stated |

### Exploitation signals from this source
- [2026-10-21 20:30 UTC](../../exploitation/index.html): No exploitation observed on partner systems; no public exploit code known.

## The bytes
capture 20261022T112853Z · HTTP 200 · https://www.huntress.com/blog/php2shell-leaked-critical-php-vulnerabilities- `headers.json` 39dd8f8ed13d1e993a95f88bddf69702d0cd23e3aef38da50d65068f495d1cff 7,379 bytes
- `page.html` 39d79180c85ccbc63f3acbf3bb0f076d56933f94e5fa8a5be8dafc3ca3160c7a 913,455 bytes
- `provenance.json` 23031a4937921ef79d80fb4b2546b9d7054028e640b9babec2c44d9f66dee0a2 1,102 bytes
- `rendered.html` 41e5af59038a7155953c6809d743ca579e2eeb7cdc503f13f6e3550ea920d970 1,115,188 bytes
- `screenshot.png` a4d89c5787921c4fe23ea13f25dc2d0104756a669450c44aad83ad220d9bc3a7 1,862,920 bytes
- `text.txt` a83d744768109a61f623c0d4de5df589cde5c1e0da114b25d62a7321f159455c 17,843 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/huntress-php2shell-rapid-response/index.html
