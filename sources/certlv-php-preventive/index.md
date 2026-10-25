# Source: Saistībā ar globāli atklātām PHP ievainojamībām Latvijā ievieš preventīvus pasākumus

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

CERT.LV (Latvia): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · government · primary · captured

# Saistībā ar globāli atklātām PHP ievainojamībām Latvijā ievieš preventīvus pasākumus

**CERT.LV (Latvia)** · [https://cert.lv/lv/2026/10/saistiba-ar-globali-atklatam-php-ievainojamibam-latvija-ievies-preventivus-pasakumus](https://cert.lv/lv/2026/10/saistiba-ar-globali-atklatam-php-ievainojamibam-latvija-ievies-preventivus-pasakumus) · published 2026-10-21T18:25 local (EEST, =15:25Z); updated 2026-10-21T23:00 local (=20:00Z) · added by `collector-gov` · slug `certlv-php-preventive`

Latvia restricted access from abroad to several state digital resources (geo-blocking, possibly until Mon 26 Oct). Update 23:00: the TVP unified website platform is patched and reachable from Latvia; latvija.gov.lv is restricted only from abroad; lsm.lv and 112.lv restored. About 6000 potentially affected resources in Latvia, a few hundred of them public sector. Automated exploitation attempts seen, none successful so far.

## What it says, as the collector read it

#### CERT.LV: Latvia introduces preventive measures over the PHP vulnerabilities

- Page date 2026-10-21. "[Informācija publicēta 21.10.2026, plkst. 18:25]" = published 18:25 local (EEST, UTC+3), so 15:25Z. "[Informācija papildināta: 21.10.2026, plkst. 23:00]" = updated 23:00 local, so 20:00Z. The UTC conversion is ours.

- Captured 2026-10-22T08:13:54Z. The text is Latvian; the translations below are ours, so check them before publishing.

- Original post (18:25): to protect state information systems, "pieņemts lēmums uz laiku ierobežot piekļuvi vairākiem valsts digitālajiem resursiem no ārvalstīm". A decision was made to temporarily restrict access to several state digital resources FROM ABROAD. Applied selectively. "Piekļuves ierobežojumi varētu būt spēkā līdz pirmdienai, 26. oktobrim". The restrictions may last until Monday 26 October. Residents in Latvia should not be affected. No known compromise in Latvia.

- Advice: update to 8.5.12/8.4.27/8.3.36/8.2.35. "Sistēmām, kuras nav iespējams atjaunināt uz drošu PHP versiju, ir jāierobežo piekļuve no interneta, nepieļaujot to publisku pieejamību līdz drošības risku novēršanai." Systems that cannot be updated MUST have internet access restricted, with no public availability until the risk is removed.

- Update (23:00): the unified website platform (TVP) for state and municipal sites is patched and reachable again from Latvia. Latvija.gov.lv is reachable from Latvia and restricted only from abroad. lsm.lv (public broadcaster) and 112.lv have been restored. Other state resources keep their foreign-access restrictions. "Kopumā Latvijā identificēti aptuveni 6000 potenciāli ietekmētu resursu, no kuriem tikai daži simti ir valsts sektorā." Around 6,000 potentially affected resources in Latvia, a few hundred of them in the state sector. "Latvijā jau ir konstatēti automatizēti mēģinājumi izmantot PHP ievainojamības, taču līdz šim nav ziņu par sekmīgiem uzbrukumiem." Automated exploitation attempts have been seen in Latvia; no successful attacks reported so far.

- This is a concrete case of government services being taken off the public internet: geo-blocked, not fully down. lsm.lv and 112.lv were evidently restricted too (they were "restored").

## Claims that cite it

| Claim | Who says it | Status | [Fact-check](../../factcheck/index.html) | Primary | Sources |
|---|---|---|---|---|---|
| About 6,000 potentially affected resources in Latvia, a few hundred in the public sectorPrimary source, one country, says 'potentially'. [fact timeline →](../../facts/scale-latvia/index.html) | CERT.LV | reported | **A2** Reported●●○○○○ | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Automated exploitation attempts were seen in Latvia; none succeededPrimary source. [fact timeline →](../../facts/latvia-attempts/index.html) | CERT.LV | reported | **A2** Reported●●○○○○ | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |
| Latvia restricted access from abroad to several state digital resources, possibly until 26 October; lsm.lv and 112.lv were restored by 20:00 UTCThe one documented case of government services being pulled from the public internet, from the agency itself. [fact timeline →](../../facts/latvia-offline/index.html) | CERT.LV | confirmed | **A6** Established●●●●●● | 1/1 | [CERT.LV](../../sources/certlv-php-preventive/index.html) |

## Events that cite it

| When | Event | Time is |
|---|---|---|
| 2026-10-21 15:25 UTC | NCSC-NL's php2shell README last significant change (17:25 CEST). CERT.LV publishes: Latvia restricts access to several state digital resources from abroad (18:25 EEST). | stated |
| 2026-10-21 20:00 UTC | CERT.LV update: the unified state website platform is patched; lsm.lv and 112.lv restored; about 6,000 potentially affected resources in Latvia; automated attempts seen, none successful. | stated |

### Numbers from this source

| Figure | Of | Status |
|---|---|---|
| about 6,000 | potentially affected resources in Latvia, a few hundred in the public sector | reported |

### Agency rows from this source
- [CERT.LV](../../agencies/index.html): offline restrict from abroad

### Exploitation signals from this source
- [2026-10-21 20:00 UTC](../../exploitation/index.html): Automated exploitation attempts seen in Latvia; no reports of successful attacks.

## The bytes
capture 20261022T081354Z · HTTP 200 · https://cert.lv/lv/2026/10/saistiba-ar-globali-atklatam-php-ievainojamibam-latvija-ievies-preventivus-pasakumus- `headers.json` b75279eb611beef16c83a6ab4d307db8ec59d18614d4d21ea1c78320a4346166 737 bytes
- `page.html` de622b5e59bf43071dcb45655edbd42b337e97f28b3e41e801ebaacc64a33581 35,634 bytes
- `provenance.json` e046187fdaa6dc172317abf6fa62152e1b5594b3c2d59c75c1de1baafa4667ba 1,158 bytes
- `rendered.html` 4f3a30ed3f755cd5965265ba1cc6f1cce9e514537463c1f9d2b87fdfceaaf514 35,482 bytes
- `screenshot.png` 504fd0c9b36378f8039c94b1157842426c17d95ab822429554c1bfc0cdbfb4d2 750,435 bytes
- `text.txt` e37a6582c4e6c685ad840001892ea94cd8e91ec107708ce4e7b7110899c2d05e 6,579 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/certlv-php-preventive/index.html
