# What sixteen agencies actually advise

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The NSA, CISA, the UK NCSC, CERT-EU, ENISA, CERT-FR, Canada, Australia, New Zealand, the Netherlands, Italy, Switzerland, Latvia, Japan, Spain and Portugal on php2shell: who says take it offline, who says isolate, who says patch and nothing more, and who has seen exploitation.

# The agencies, side by side

In plain English What sixteen government cyber agencies told organisations to do. All say update; they disagree on whether to take systems offline.

In one line

All 16 say install the fix. They split on what to do with a system you cannot patch today: the US says take it offline, the UK makes that the fourth step, Europe says isolate, and Australia, Japan and the Netherlands say nothing about it.

## The spectrum
every agency, by what it says to do with a system you cannot patch6 No offline adviceEU ENISA CSIRTs NetworkAU ASD's ACSCNZ NCSCNL NCSC-NLIT ACN / CSIRT ItaliaJP JPCERT/CC2 Consider it, or after other stepsUK NCSCCH BACS1 Restrict accessLV CERT.LV3 Isolate from the internetEU CERT-EUFR CERT-FRCA CCCS2 Take it offlineUS NSA CybersecurityUS CISA
Not readable from this capture environment: CCN-CERT, CNCS.

## Agency by agency
each in its own words, with its saved sources
### NSA Cybersecurity
US
Take offline
If an immediate update is not feasible, it is recommend[ed] that organizations take the system offline until it can be fully mitigated.
NSA Cyber on XNSANSA Cyber on X
### CISA
US
Take offline
Organizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be patched or updated.
CISACISACISA
### NCSC
UK
After mitigations
If you are unable to apply the temporary mitigations, or applying them would take too long, you should consider taking the system offline until it can be fully mitigated.
NCSC UK
### CERT-EU
EU institutions
Isolate
Where that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified.
CERT-EU
### ENISA CSIRTs Network
EU
No offline advice

An index of about 30 national advisories, work in progress: a truncated CVE in the heading and a Dutch 'en'.

ENISA CNW
### CERT-FR (ANSSI)
FR
Isolate first
Le CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue...
CERT-FR
### CCCS
CA
Isolate
Where immediate remediation is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix can be applied.
CCCSCCCS
### ASD's ACSC
AU
No offline advice

No take-offline or isolation advice. The BBC's 'Australian counterparts' framing is not supported by the page. Parts of the body are still pre-patch text.

ACSCACSC
### NCSC
NZ
No offline advice

The only agency to say active exploitation is reported. It does not say whose reports. Time converted from NZDT by this site.

NCSC New ZealandNCSC New Zealand
### NCSC-NL
NL
No offline advice

Runs the public php2shell GitHub repository with the software inventory the UK NCSC cites, cPanel detection and mitigation scripts, and an SPDX/VEX source list.

NCSC-NLNCSC-NLNCSC-NL
### ACN / CSIRT Italia
IT
No offline advice

Update only. Lists the four fixed branches and no end-of-life branches.

ACN / CSIRT Italia
### BACS (NCSC)
CH
Consider
Check, particularly for critical applications, whether a temporary disconnection from the internet or taking the system offline is necessary.
BACSSwiss BACS
### CERT.LV
LV
Restrict from abroad
Systems that cannot be updated must have internet access restricted, with no public availability until the risk is removed.
CERT.LV
### JPCERT/CC
JP
No offline advice

Translations are this site's.

JPCERT/CCJPCERT/CC
### CCN-CERT
ES
Could not be read

The title ('actualización inmediata') points to immediate-update advice. The block is recorded in the vault.

CCN-CERT
### CNCS
PT
Could not be read

The block is recorded in the vault.

CNCS

## The evidence table

16 national and supranational bodies, each read from its own page. The question that divides them is not whether to patch (all say patch) but what to do with a system that cannot be patched now. Of 16: 6 say *none*, 2 say *yes*, 2 say *isolate*, 2 say *unknown*, 1 say *after mitigations*, 1 say *isolate first*, 1 say *consider*, 1 say *restrict from abroad*. Two could not be read because their sites block automated browsers; the block is recorded.

The BBC's morning framing, *the UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline*, holds for the NSA and CISA, is a simplification of the NCSC's fourth of six steps, and is not supported by the Australian page at all. The sentence the BBC quotes from the NCSC is not on the NCSC page as captured; its opening matches the Canadian text.

| Agency | Published | Offline? | Exploitation | Note | Sources |
|---|---|---|---|---|---|
| **NSA Cybersecurity** US | 2026-10-21T13:45:58Z (X post); press release dated 21 Oct | yesIf an immediate update is not feasible, it is recommend[ed] that organizations take the system offline until it can be fully mitigated. | not stated | The X post says 'be prepared for an update', so it reads as written before or with the patch. The press release names no CVE IDs and calls the pair 'PHP2Shell'. | [NSA Cyber on X](../sources/nsa-x-2112903220209098897/index.html) [NSA](../sources/nsa-press-php-4630238/index.html) [NSA Cyber on X](../sources/nsa-x-2113068811058622971/index.html) |
| **CISA** US | 2026-10-21 | yesOrganizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be patched or updated. | none observed at publication; neither CVE in KEV as of catalog 2026.10.21 | 'A web application firewall may provide some protection until systems are updated or patched.' The most absolute offline advice, and it covers end-of-life versions explicitly. | [CISA](../sources/cisa-alert-php-20261021/index.html) [CISA](../sources/cisa-kev-json/index.html) [CISA](../sources/cisa-home/index.html) |
| **NCSC** UK | 2026-10-21 (page modified 2026-10-22T07:30:02Z) | after mitigationsIf you are unable to apply the temporary mitigations, or applying them would take too long, you should consider taking the system offline until it can be fully mitigated. | not stated | Offline is the fourth of six priority actions, after inventory, update and the PHP Foundation's temporary mitigations. The sentence the BBC quotes ('Where immediate remediation is not feasible...') is not on the page as captured; the page changed on 22 October. | [NCSC UK](../sources/ncsc-news-php/index.html) |
| **CERT-EU** EU institutions | 2026-10-21 15:20:18 (timezone not stated) | isolateWhere that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified. | PoCs circulating; 'raises the likelihood that attackers are already exploiting' | States the fixes were released at 13:30 UTC. Lists the PHP temporary mitigations in full. | [CERT-EU](../sources/certeu-sa-2026-018/index.html) |
| **ENISA CSIRTs Network** EU | 2026-10-21 | noneThe Mitigation field still holds template placeholder text. | not stated | An index of about 30 national advisories, work in progress: a truncated CVE in the heading and a Dutch 'en'. | [ENISA CNW](../sources/enisa-cnw-2026-04-php/index.html) |
| **CERT-FR (ANSSI)** FR | 2026-10-21 | isolate firstLe CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue... | not stated | The closest to 'isolate first, then patch'. Lists all 5.x, 6.x, 7.x, 8.0 and 8.1 as affected. Workarounds: session.upload_progress off; block multipart Content-Type at a WAF. | [CERT-FR](../sources/certfr-2026-ale-014/index.html) |
| **CCCS** CA | 2026-10-21 | isolateWhere immediate remediation is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix can be applied. | PoC available, no active exploitation identified | The opening of this sentence is the one the BBC attributes to the UK NCSC. The wording is shared across Five Eyes and CERT-EU text. | [CCCS](../sources/cccs-al26-026/index.html) [CCCS](../sources/cccs-alerts/index.html) |
| **ASD's ACSC** AU | 2026-10-21, reviewed 2026-10-22 | noneIdentify PHP, review php.net, apply updates and mitigations, monitor. | not aware of successful active exploitation within Australia | No take-offline or isolation advice. The BBC's 'Australian counterparts' framing is not supported by the page. Parts of the body are still pre-patch text. | [ACSC](../sources/acsc-alert-php/index.html) [ACSC](../sources/acsc-home/index.html) |
| **NCSC** NZ | 2026-10-21T20:15Z (09:15 NZDT, 22 Oct); updated 21:20Z | noneUpdate to PHP 8.5.12, 8.4.27, 8.3.36 or 8.2.35; apply the remediation as soon as possible; investigate unauthorised access or compromise. | 'The NCSC is aware of reports of active exploitation.' | The only agency to say active exploitation is reported. It does not say whose reports. Time converted from NZDT by this site. | [NCSC New Zealand](../sources/ncsc-nz-alert-php/index.html) [NCSC New Zealand](../sources/ncsc-nz-alerts/index.html) |
| **NCSC-NL** NL | 2026-10-21T15:25Z (README last significant change) | noneIf immediate patching is not possible, follow PHP's temporary mitigations... PHP states that these measures are not complete fixes. | public PoC exists; no active abuse seen (portal banner) | Runs the public php2shell GitHub repository with the software inventory the UK NCSC cites, cPanel detection and mitigation scripts, and an SPDX/VEX source list. | [NCSC-NL](../sources/ncsc-nl-php2shell/index.html) [NCSC-NL](../sources/ncsc-nl-advisories/index.html) [NCSC-NL](../sources/ncsc-nl-php2shell-software-list/index.html) |
| **ACN / CSIRT Italia** IT | 2026-10-21 | noneSi raccomanda di aggiornare i prodotti vulnerabili. | not stated | Update only. Lists the four fixed branches and no end-of-life branches. | [ACN / CSIRT Italia](../sources/acn-it-php2shell/index.html) |
| **BACS (NCSC)** CH | 2026-10-21 (home-page teaser dated 20 Oct) | considerCheck, particularly for critical applications, whether a temporary disconnection from the internet or taking the system offline is necessary. | not stated | 'Even a web application firewall alone is not sufficient', which contrasts with CISA. Says containers may need to be rebuilt. | [BACS](../sources/ch-bacs-warnung-php/index.html) [Swiss BACS](../sources/ch-ncsc-home/index.html) |
| **CERT.LV** LV | 2026-10-21T15:25Z; updated 20:00Z (converted from EEST) | restrict from abroadSystems that cannot be updated must have internet access restricted, with no public availability until the risk is removed. | automated exploitation attempts seen, none successful | Latvia geo-blocked several state digital resources from abroad, possibly until 26 October. The unified state website platform was patched by 20:00Z; lsm.lv and 112.lv restored. Translations are this site's. | [CERT.LV](../sources/certlv-php-preventive/index.html) |
| **JPCERT/CC** JP | 2026-10-22 | noneAfter sufficient testing, apply the fixed version promptly; investigate whether you have been compromised. | not stated; warns that one detection rule may miss attacks | Translations are this site's. | [JPCERT/CC](../sources/jpcert-at260033/index.html) [JPCERT/CC](../sources/jpcert-home/index.html) |
| **CCN-CERT** ES | unknown | unknownNot read: HTTP 403 bot challenge to every fetch. | unknown | The title ('actualización inmediata') points to immediate-update advice. The block is recorded in the vault. | [CCN-CERT](../sources/ccn-cert-al-11-26/index.html) |
| **CNCS** PT | unknown | unknownNot read: HTTP 513 browser-verification challenge. | unknown | The block is recorded in the vault. | [CNCS](../sources/cncs-pt-alerta-136114/index.html) |

Each agency's full text is in its capture; the sentences here are the ones the collectors copied verbatim into their notes. Translations from French, Italian, Latvian and Japanese are this site's and are marked as such in the notes.


---
site v0.21.2 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/agencies/index.html
