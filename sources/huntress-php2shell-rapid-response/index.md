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
| As of 20:50 UTC on 22 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, and two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same). Attempts are not compromises: watchTowr says "nobody has been successful to date"; Amazon says it is unclear whether any attempt would have succeeded on real systems; Patchstack's incidents are reports from hosting partners with no victim named. Source watch (vault oq9gflln), pending promotion into the evidence vault: the PHP Foundation's executive director told The Verge and WIRED "to our knowledge, there has been no successful attempt at remote code execution" (raw/us/tech-press/the-verge/php2shell-websites-down/); officials in Germany, the Netherlands and Japan say they have not seen an attack succeed (The Next Web, raw/nl/tech-press/the-next-web/php2shell-no-confirmed-breaches/); GMO confirmed a break-in on 20 October on its FX trading VPS service (26,739 servers, logins possibly taken) without stating the cause (raw/jp/news/yahoo-news-jp/gmo-fx-login-leak/20261022T191523Z/); Czech Technical University says it stopped an active attack that was part of worldwide attempts against PHP sites, success not established (raw/cz/tech-press/lupa/cvut-cyber-attack/20261022T191510Z/); Valtec in Japan blamed php2shell for a break-in, then retracted: its own service's flaw (raw/jp/tech-press/impress-watch/valtec-php-attack/20261022T191433Z/); Fortune reports an anonymous startup owner alleging stolen source code, unnamed and not attributed to the flaw. Edited by researcher@php.newsroom. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault and the source watch, as of 20:50 UTC on 22 October | reported | **A4** Corroborated●●●●○○ status overstated | 6/9 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) |
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
site v0.11.6 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/sources/huntress-php2shell-rapid-response/index.html
