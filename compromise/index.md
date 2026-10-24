# No named organisation has said it was compromised through php2shell: the evidence

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The evidence behind one statement, as of 2026-10-23 16:04 UTC: attempts, vendor reports, statements that no success is known, named organisations, allegations and official lists, each with its source.

# No named organisation has said it was compromised through php2shell.

This page holds the evidence behind one statement, as of **2026-10-23 16:04 UTC**: every statement found about attacks on, or compromises of, real systems through php2shell, sorted by what kind of evidence it is, with the words of the party that made it and where its capture is held. It makes no assessment of risk. The statement's status is **reported**: A time-bounded absence, not a confirmed fact. It is true only as of the last check, and one statement from one organisation would end it. It is [claim no-confirmed-compromise](../claims/index.html#no-confirmed-compromise).

## What was searched

Where the statement was checked. A statement that something does not exist is only as good as the search behind it.
295The evidence vault: sourceshead 1845598d9a38; the site is built from all of it913The source watch: pages watched597 publishers, head 20afaa62129d (the old watch, oq9gflln; the watch continues in pack vault 7r83qic5)339Read in their own language: non-English pages28 languages; 568 new items with verbatim quotes; as counted on 22 October3,444Discovery feeds: news items scannedGoogle News and Bing News, 85 editions, from 1,621 publishers; as counted on 22 October295Named sites probed: sitesevery site somebody named as taken offline, probed every 30 minutes; as counted on 22 October

## From attempts to a named compromise

Not to scale. Each layer is a different kind of statement, and a statement in one layer does not move a case into the next: an attempt is not a compromise, and a vendor's report without a victim is not a victim's statement. The bottom layer is the statement this page is about.

## The evidence, by kind

36 statements on this page, by what kind of evidence they are. A count of statements, not of events: one party can report millions of attempts in one statement.

Each dot is one statement on this page, placed at the time the source gives (noon where it gives only a date). Hover a dot for who said it.

## Attempts seen (9)

This kind of statement can show that someone tried. It cannot show that anyone succeeded.

| When | Who | What they said | Where it is held |
|---|---|---|---|
| 2026-10-17 | **Amazon (AWS Threat Intelligence)** | An exploit attempt against a MadPot honeypot four days before disclosure; "it's unclear if any of these attempts would have succeeded in real-world systems." | [Amazon](../sources/aws-security-blog-madpot/index.html) |
| 2026-10-21 | **Cloudflare** | "We observed attack traffic targeting our customers" and attackers "mutating the attack payload to try to bypass our protections". | [Cloudflare](../sources/cloudflare-blog-php2shell-waf/index.html) |
| 2026-10-21 | **watchTowr (via SecurityWeek)** | First in-the-wild attempts hit its sensors; "Whilst nobody has been successful to date, we don't expect that will last long." | [SecurityWeek](../sources/securityweek-first-attempts-sensors/index.html) |
| 2026-10-21 08:36 UTC | **ELLIO (via The Hacker News)** | First sensor hit, about 55 minutes after Chainguard's images. | [THN](../sources/thehackernews-php2shell-4days/index.html) |
| 2026-10-21 20:00 UTC | **CERT.LV (Latvia)** | Automated exploitation attempts seen in Latvia; no successful attacks reported. | [CERT.LV](../sources/certlv-php-preventive/index.html) |
| 2026-10-22 | **Cloudflare's CEO, Matthew Prince** | "thousands in the 45 minutes post announcement, hundreds of thousands within 2 hours, and millions now." | [Matthew Prince, Cloudflare CEO on…](../sources/x-eastdakota-php2shell-stats/index.html) |
| 2026-10-22 | **VulnCheck (via SecurityWeek)** | "At least one Chinese IP address unsuccessfully attempted to exploit PHP2Shell to deploy a webshell." | [SecurityWeek](../sources/securityweek-exploitation-days-before/index.html) |
| 2026-10-22 | **QNAP PSIRT** | Observed scanning activity and attack attempts using the PHP2Shell flaws. | [QNAP](../sources/qnap-statement-php2shell/index.html) source watch: `raw/tw/security-vendor/qnap/statement-php2shell/20261022T191720Z/` |
| 2026-10-22 | **A Tencent News analyst, with ThreatBook sensors (China)** | Captured scanning requests with the User-Agent php2shell-scan/1.0; no evidence of successful code execution. | source watch: `translations/hk/news/news-qq/rain-a-20261021a0eq4p00.json` |

## Exploitation reported, no victim named (4)

This kind of statement can show that a party says exploitation happened. It cannot show who was hit, or whether it was confirmed by the victim.

| When | Who | What they said | Where it is held |
|---|---|---|---|
| 2026-10-21 | **Hadrian (via SecurityWeek)** | "We are now seeing php2shell exploited in the wild at scale." No victim named. | [SecurityWeek](../sources/securityweek-first-attempts-sensors/index.html) |
| 2026-10-21 | **Amazon (AWS Threat Intelligence)** | "PHP2Shell is now being broadly exploited in the wild." Against its sensors; no victim named. | [Amazon](../sources/aws-security-blog-madpot/index.html) |
| 2026-10-21 07:34 UTC | **Patchstack (via Recorded Future)** | "Received reports of multiple active exploitation incidents from hosting partners." No victim named. | [Recorded Future](../sources/recordedfuture-php2shell/index.html) |
| 2026-10-21 20:15 UTC | **NCSC New Zealand** | "The NCSC is aware of reports of active exploitation." Whose reports is not said. | [NCSC New Zealand](../sources/ncsc-nz-alert-php/index.html) |

## No successful exploitation known (12)

This kind of statement can show what a party with visibility has not seen. It cannot show that nothing happened outside its view.

| When | Who | What they said | Where it is held |
|---|---|---|---|
| 2026-10-21 | **CISA** | "CISA has not observed exploitation of these vulnerabilities as of the time of publication." | [CISA](../sources/cisa-alert-php-20261021/index.html) |
| 2026-10-21 | **The PHP Foundation** | The security team "did not identify any functional exploits at the time of release/public disclosure." | [PHP Foundation](../sources/php-foundation-blog-security-release/index.html) |
| 2026-10-21 | **Australia's ACSC (via Information Age)** | In its critical alert, ASD's ACSC said it was "not aware of active exploitation related to these vulnerabilities". | [Information Age](../sources/ia-acs-article-2026-govt-sites-go-down-after-ai-finds-critical-php/index.html) |
| 2026-10-21 | **Patchstack (via PCMag)** | "Shortly after PHP's update, our telemetry shows only probing attacks, with no hard evidence of breaches yet." Recorded Future reports the same company receiving reports of exploitation incidents from hosting partners that morning; the two accounts are not reconciled. | [PCMag](../sources/pcmag-news-hackers-already-trying-to-exploit-serious-php-flaw/index.html) [Recorded Future](../sources/recordedfuture-php2shell/index.html) |
| 2026-10-21 20:30 UTC | **Huntress** | "As of October 21 at 4:30pm ET, Huntress has not observed in-the-wild exploitation on partner systems." | [Huntress](../sources/huntress-php2shell-rapid-response/index.html) |
| 2026-10-22 | **The PHP Foundation's executive director (to The Verge and WIRED)** | "To our knowledge, there has been no successful attempt at remote code execution." | [The Verge](../sources/the-verge-php2shell-websites-down/index.html) source watch: `raw/us/tech-press/the-verge/php2shell-websites-down/` |
| 2026-10-22 | **Germany's BSI, the Dutch NCSC, Japan's Chief Cabinet Secretary (via The Next Web, Politico)** | Germany has seen attacks but no successful use; the Netherlands has no indication of active misuse; Japan says no attacks exploiting the flaws have been confirmed. | source watch: `raw/nl/tech-press/the-next-web/php2shell-no-confirmed-breaches/` |
| 2026-10-22 | **Switzerland's BACS** | Knows of no attacks in Switzerland attributable to the flaws (via SRF, read in German). | source watch: `translations/ch/news/srf/news-schweiz-cyber-schwachstelle-bei-php-erste-schadensbilan.json` |
| 2026-10-22 | **Belgium's CCB** | Has recorded no attacks on Belgian websites (via RTVE, read in Spanish; and Clickx, in French). | [RTVE.es](../sources/rtve-noticias-20261022-fallos-criticos-php2shell-vulnerabili/index.html) source watch: `translations/es/news/rtve/noticias-20261022-fallos-criticos-php2shell-vulnerabilidades.json` |
| 2026-10-22 | **Austria's Interior Ministry** | No concrete reports of successful attacks so far (via Salzburg24, read in German). | [salzburg24](../sources/salzburg24-news-oesterreich-massive-sache-folgen-der-php-sic/index.html) source watch: `translations/at/news/salzburg24/news-oesterreich-massive-sache-folgen-der-php-sicherheitslue.json` |
| 2026-10-22 | **Cloudflare (to USA Today)** | Its observations "describe attack attempts; they do not, by themselves, establish successful compromises." | [USA Today](../sources/usa-today-php2shell-live/index.html) source watch: `raw/us/news/usa-today/php2shell-live/` |
| 2026-10-23 | **Luxembourg (via Paperjam)** | No Luxembourg financial institution, public service or operator had announced it had actually been infiltrated through php2shell; the state announced no confirmed compromise, and the authorities asked operators to search back for traces of compromise and to keep the evidence. | [Paperjam](../sources/paperjam-article-php2shell-des-milliers-de-sites/index.html) |

## Named organisations (7)

This kind of statement can show what the organisation itself said. It cannot show a cause the organisation did not state.

| When | Who | What they said | Reading | Where it is held |
|---|---|---|---|---|
| 2026-10-21 | **DMM (Japan)** | Halted services to respond to "a vulnerability in external software"; no data leaked; would not say whether it was PHP. | Precaution; cause not stated | [産経ニュース](../sources/sankei-dmm-service-halt/index.html) source watch: `raw/jp/news/sankei/dmm-service-halt/20261022T191536Z/` |
| 2026-10-22 | **GMO Internet Group (Japan)** | Malicious programs were found on 20 October on servers of its FX trading VPS service; 26,739 servers possibly affected; account logins may have been taken; fraudulent operations reported. The cause is not stated. | A confirmed break-in, cause not stated | [Yahoo! News Japan](../sources/yahoo-jp-gmo-fx-login-leak/index.html) source watch: `raw/jp/news/yahoo-news-jp/gmo-fx-login-leak/20261022T191523Z/` |
| 2026-10-22 | **Czech Technical University (ČVUT)** | Facing "a cyber attack on its IT infrastructure… part of worldwide attempts to hit PHP sites"; "the active attack was stopped"; some systems taken offline. | An attack reported and stopped; success not stated | [Lupa.cz](../sources/lupa-cvut-cyber-attack/index.html) source watch: `raw/cz/tech-press/lupa/cvut-cyber-attack/20261022T191510Z/` |
| 2026-10-22 | **Valtec (Japan)** | First blamed a "cyberattack targeting the PHP vulnerability", then corrected: the attackers used a flaw in its own service. | Attribution to php2shell retracted | [INTERNET Watch](../sources/impress-watch-valtec/index.html) source watch: `raw/jp/tech-press/impress-watch/valtec-php-attack/20261022T191433Z/` |
| 2026-10-22 | **Germany's Interior Ministry (to Bild)** | Its site "was not hacked", only taken down "for a repair". | Precaution, stated not compromised | source watch: `translations/de/news/bild/leben-wissen-digital-php-sicherheitsluecken-behoerden-nehmen.json` |
| 2026-10-22 | **Anexia (Austria)** | Confirmed attack attempts on websites it operates; bank data not affected (via ORF). | Attempts, stated not compromised | [ORF](../sources/orf-stories-3445806/index.html) source watch: `translations/at/news/orf/stories-3445806.json` |
| 2026-10-22 | **Ahold Delhaize** | No reason to believe its recent cyberattack is linked to the PHP flaws (via Accountant.nl). | A separate incident, link denied | source watch: `translations/nl/news/accountant/nieuws-2026-10-europese-cybersecuritydienst-waarschuwt-voor.json` |

## Unnamed allegations (1)

This kind of statement can show that a claim was made. It cannot show who, or that php2shell was the way in.

| When | Who | What they said | Where it is held |
|---|---|---|---|
| 2026-10-21 | **An anonymous startup owner (via Fortune)** | Alleges hackers stole source code, exposed cookie data and leaked legal documents. Unnamed; not attributed to php2shell; not verified. | [Fortune](../sources/fortune-ai-tools-php-vulnerability/index.html) source watch: `raw/us/news/fortune/ai-tools-php-vulnerability/` |

## Official exploited signals (3)

This kind of statement can show what the official lists record. It cannot show anything they have not yet recorded.

| When | Who | What they said | Where it is held |
|---|---|---|---|
| 2026-10-21 14:34 UTC | **CISA's assessment on the CVE records (SSVC)** | Exploitation: none. Automatable: no. Technical impact: total. | [CVE record](../sources/cve-cve-2026-109618/index.html) [CVE record](../sources/cve-cve-2026-109619/index.html) |
| 2026-10-22 17:51 UTC | **EPSS (FIRST)** | 0.053 and 0.058: the modelled probability of exploitation activity in the next 30 days. | source watch: `series/epss/` |
| 2026-10-23 08:03 UTC | **CISA Known Exploited Vulnerabilities catalog** | Version 2026.10.21, 1,754 entries; neither CVE listed. The source watch re-read it at 08:03 UTC on 23 October, unchanged since its capture at 18:16 UTC on 22 October. | [CISA](../sources/cisa-kev-json/index.html) source watch: `series/kev-listed/` |

## What would change the statement
- A named organisation saying it was compromised through php2shell, in its own notice, filing or statement.
- GMO, ČVUT or DMM stating a cause.
- A KEV listing for either CVE, with CISA's evidence.
- A regulator's breach notice (for example under GDPR or Australia's Notifiable Data Breaches scheme) naming the flaw.
- A security vendor naming a victim, with the victim's consent.

The source watch checks the official lists and the named organisations' pages every 30 minutes; this page is rebuilt from data/compromise.json when the evidence changes.

## The disagreements, recorded

Where sources disagree, the disagreement is a record of its own in the source watch's contradiction ledger, with both statements and their captures: `contradictions/is-it-exploited.json`, `contradictions/compromise-gmo-fx-vps.json`, `contradictions/compromise-cvut.json`, `contradictions/compromise-valtec.json`, `contradictions/compromise-dmm.json`, `contradictions/exploitation-germany-netherlands.json`.

## How this page is made

Every row is in [data/compromise.json](../data/compromise.json). Rows with sources cite captures in the evidence vault, which the build checks. Rows marked *source watch* cite a dated snapshot folder in the source-watch vault ([oq9gflln](../vaults/source-watch/index.html)), read with its published key; they move into the evidence vault as the evidence curator promotes them. Statements read in another language carry the reader’s English translation beside the verbatim original in the watch’s `translations/` files. The charts are drawn from the same rows when the site is built.


---
site v0.14.14 · data as of 2026-10-23T16:04Z · vault commit 1845598d9a38 · https://php.oct.2026.newsroom.sgit.ai/compromise/index.html
