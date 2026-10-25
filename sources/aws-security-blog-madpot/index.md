# Source: Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Amazon (CJ Moses, AWS Security Blog): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · vendor · primary · captured

# Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

**Amazon (CJ Moses, AWS Security Blog)** · [https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/) · published 2026-10-21 · added by `claude-story-site` · slug `aws-security-blog-madpot`

Primary account of the 17 October honeypot attempt and the 02:00 UTC proof-of-concept attempts; 'PHP2Shell is now being broadly exploited in the wild'.

## What it says, as the collector read it

#### Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog

Captured by claude-story-site. Status: captured. Primary account of the 17 October honeypot attempt and the 02:00 UTC proof-of-concept attempts; 'PHP2Shell is now being broadly exploited in the wild'.

- By CJ Moses, 21 Oct 2026. Verbatim: 'identified a PHP2Shell exploitation attempt dating to Oct. 17, 2026, in MadPot telemetry, four days before public disclosure'; 'originated from an IP address associated with a commercial anonymization network'; 'it remains unclear how the actor acquired exploit information prior to disclosure'.

- 'multiple proof of concept exploits for the vulnerability, with the earliest around 2026-10-21 0200 UTC'; attempts 02:00 to 08:00 UTC from additional anonymised infrastructure, 'multiple actors'; 'it's unclear if any of these attempts would have succeeded in real-world systems'.

- After release: 'PHP2Shell is now being broadly exploited in the wild.' No counts.

- Advice: investigate from 17 October; detections that do not rely on a CVE signature; consider blocking multipart uploads where you cannot patch.

- A reader comment complains AWS managed distributions lacked packages for 10 hours (unverified).

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| An exploit attempt hit an Amazon honeypot on 17 October from an anonymisation network; proof-of-concept attempts began about 02:00 UTC on 21 October from multiple actors; after release 'PHP2Shell is now being broadly exploited in the wild'Primary party. Amazon adds: 'it's unclear if any of these attempts would have succeeded in real-world systems'. Attempts against honeypots, not compromises of victims. [fact timeline →](../../facts/amazon-honeypot/index.html) | Amazon (CJ Moses, AWS Security Blog) | reported | **A2** Reported●●○○○○ superseded | 1/2 | [Amazon](../../sources/aws-security-blog-madpot/index.html) [THN](../../sources/thehackernews-php2shell-4days/index.html) |
| Amazon and Cloudflare saw sites being probed for the flawBoth companies have since said so themselves. [fact timeline →](../../facts/probing/index.html) | Alan Woodward, via the BBC; confirmed by both companies' own posts | confirmed | **A5** Confirmed●●●●●○ | 2/3 | [BBC News](../../sources/bbc-live-ckgel5xp2xv9t/index.html) [Cloudflare](../../sources/cloudflare-blog-php2shell-waf/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) |
| As of 09:35 UTC on 25 October, no named organisation has said it was compromised through php2shell. Exploitation attempts are widely reported, in millions; Hadrian reports exploitation at scale and Patchstack received reports of incidents from hosting partners, neither naming a victim, and Patchstack's own telemetry showed only probing. Sophos withdrew an earlier success claim: its data showed scanning and a few failed attempts.A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change. Changed from "confirmed" on 22 October at the editor's request. Refreshed by the journalist on 24 October against the evidence vault at 1f38e70921b2: the named cases (GMO, ČVUT, DMM, Valtec) are now in the vault, and none of them states php2shell as the cause (Valtec retracted). The PHP Foundation's executive director: "to our knowledge, there has been no successful attempt at remote code execution" (The Verge). Luxembourg: no institution has announced an intrusion (Paperjam). Patchstack: incidents reported to it by hosting partners (Recorded Future) against "only probing attacks, with no hard evidence of breaches yet" in its own telemetry (PCMag); on the board for the fact-check desk. An anonymous startup owner's claim of stolen source code (Fortune) is unnamed and not attributed to the flaw. Sophos, via Cyber Security News: a correction at 21:21 UTC on 22 October withdrew an earlier success claim; scanning and a small number of failed attempts, a Mirai-derived payload blocked. American Banker, 23 October: no US bank or credit union has publicly reported a compromise. Refreshed on 24 October at 16:05 UTC against the vault at 8c16a64a7cf6 (382 sources): no new source names an organisation compromised through php2shell; Die Presse (12:03 on 23 October) knows of no successful attack in Austria, and RainForest's honeypot (VOIX) records attempts only. Refreshed again on 25 October at 09:35 UTC (10:35 BST) against the vault at 87795d121200 (418 sources): still no new source names an organisation compromised through php2shell; Turkey's Presidency Cybersecurity Directorate says the e-Devlet portal had no problem. [fact timeline →](../../facts/no-confirmed-compromise/index.html) | this site, from every captured source in the evidence vault (418 sources, head 87795d121200), as of its latest capture at 09:35 UTC on 25 October | reported | **A4** Corroborated●●●●○○ | 6/23 | [CISA](../../sources/cisa-kev-json/index.html) [CISA](../../sources/cisa-alert-php-20261021/index.html) [Huntress](../../sources/huntress-php2shell-rapid-response/index.html) [Amazon](../../sources/aws-security-blog-madpot/index.html) [SecurityWeek](../../sources/securityweek-first-attempts-sensors/index.html) [SecurityWeek](../../sources/securityweek-exploitation-days-before/index.html) [Recorded Future](../../sources/recordedfuture-php2shell/index.html) [Imperva Threat Research](../../sources/imperva-blog-php2shell/index.html) [Weird Gloop](../../sources/weirdgloop-blog-php2shell/index.html) [Paperjam](../../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) [PCMag](../../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [IT Social](../../sources/itsocial-cybersecurite-cybersecurite-articles-php/index.html) [Lupa.cz](../../sources/lupa-cvut-cyber-attack/index.html) [Yahoo! News Japan](../../sources/yahoo-jp-gmo-fx-login-leak/index.html) [産経ニュース](../../sources/sankei-dmm-service-halt/index.html) [INTERNET Watch](../../sources/impress-watch-valtec/index.html) [The Verge](../../sources/the-verge-php2shell-websites-down/index.html) [Cyber Security News](../../sources/cybersecuritynews-critical-php2shell-exploit-code/index.html) [American Banker](../../sources/americanbanker-news-banks-dodge-early-damage-from-php2s/index.html) [The Next Web](../../sources/the-next-web-php2shell-no-confirmed-breaches/index.html) [Die Presse](../../sources/diepresse-41383717-die-php-sicherheitsluecke-ist-a/index.html) [voix](../../sources/voix-business-cards-rainforest-ip-activity-an/index.html) [Haber.com](../../sources/haber-teknoloji-siber-guvenlik-baskanligi-ndan/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 | The Dutch NCSC takes its own website offline as a precaution; DigiD, MijnOverheid and Overheid.nl follow. Weird Gloop turns off its wiki web servers for 13 hours. Amazon, Imperva, Fastly, Akamai and Huntress publish. | stated |

### Exploitation signals from this source
- [2026-10-17](../../exploitation/index.html): One exploit attempt against a MadPot honeypot from a commercial anonymisation network, four days before disclosure; 'it remains unclear how the actor acquired e

## The bytes
capture 20261022T111755Z · HTTP 200 · https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/- `headers.json` cd2b6b91c536e98366aa450fc499555f4c46f1fc50e52b619d41fdd8156f7621 961 bytes
- `page.html` 94afa0f2233266fa0310186f90425778563bae6747ca3cf284d7d176d5339c8b 1,407,726 bytes
- `provenance.json` 0d0fa2b45ba63031f0e80fc3fdf09aaa336dc7d1bb31664221072c5be8924343 1,223 bytes
- `rendered.html` 5e11969294ad2dba28416a6f535b5e0674e071861c00efcd5c7b6dbecd42ee92 1,473,573 bytes
- `screenshot.png` 838da55574a9351f12a7a7ef936be739360c2221877d6e744c1ec445ad70a84a 688,402 bytes
- `text.txt` 94315ded6e1175f290a4a7cac71ba39dcf18ada7232367f66c34e1decfb08c7d 8,561 bytes
capture 20261023T160435Z · HTTP 200 · https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/- `headers.json` e0ce26cc23e02ee712c46b0459d730662b9f6c4eb58a7fa0d6e89aa359d4b13c 1,032 bytes
- `page.html` 97b8d87ec2bdc87224e2b4fda3e8e9a8e88cbff80a3f648357313cd537435b1a 1,407,737 bytes
- `provenance.json` e0642397fc34af1b1f8f3fe7b3c5bd2cb39ab9f1163b292c8f1312d7db92abf5 1,920 bytes
- `rendered.html` cdeee247d98d602a20e40fbea16608d42d2d3169c6c20fd0084f69ddbfe64565 1,465,446 bytes
- `screenshot.jpg` cec27caf9be0f02f4189524eff01ba6bbbd4258ca6554bc7eb5ef6b49a0cae60 379,262 bytes
- `text.txt` 4108b2850c48a8f2141f05996ef7e7ed115a0a0f80ce697b3d237b8d13e7c764 7,474 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/aws-security-blog-madpot/index.html
