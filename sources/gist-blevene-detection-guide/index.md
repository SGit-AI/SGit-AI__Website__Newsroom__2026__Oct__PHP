# Source: PHP2Shell: Detection Opportunities · GitHub

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

Blevene (GitHub gist): what it says, the claims and events that cite it, and the hashes of every captured file.

Source · code · secondary · captured

# PHP2Shell: Detection Opportunities · GitHub

**Blevene (GitHub gist)** · [https://gist.github.com/Blevene/472692937d05145d29d17dc3c6edc2a0](https://gist.github.com/Blevene/472692937d05145d29d17dc3c6edc2a0) · published 2026-10-21 · added by `claude-story-site` · slug `gist-blevene-detection-guide`

The most detailed detection guide found: verified ModSecurity tripwire on the upload-progress field, Sigma rules for the arm-phase fatal ('in Unknown on line 0'), FPM segfault correlation, Falco worker-exec rules, and the arm/fire success receipt in the access log.

## What it says, as the collector read it

#### PHP2Shell: Detection Opportunities · GitHub

Captured by claude-story-site. Status: captured. The most detailed detection guide found: verified ModSecurity tripwire on the upload-progress field, Sigma rules for the arm-phase fatal ('in Unknown on line 0'), FPM segfault correlation, Falco worker-exec rules, and the arm/fire success receipt in the access log.

- 'ModSecurity leaves REQUEST_BODY empty for multipart requests, so that rule never fires. Use the field-name rule.'

- 'a genuine memory-limit fatal cites the script ... in Unknown on line 0 means the bailout happened outside any script — the multipart parse.'

- 'reliable exploitation needs several attempts per target ... a burst of fatal-then-fire pairs is a tuned attacker. The SUCCESS receipt is visible in the ACCESS LOG: an arm-fatal burst followed by a fire that returns 2xx'.

- Reproduction ran on PHP 8.4.4's CLI server; nginx/FPM/Apache behaviour mapped, not observed.

## Claims that cite it

No claim cites this source yet.

## Events that cite it

No timeline event cites this source yet.

## The bytes
capture 20261022T112029Z · HTTP 200 · https://gist.github.com/Blevene/472692937d05145d29d17dc3c6edc2a0- `headers.json` e515879745065efa3f6d82ddfddf934b4dd0528d08c9cd4686517a7909ad53a9 5,398 bytes
- `page.html` 638f078193990b68d231d7f9d70c8090f0fa5ea1c6f17144ce040e86005b0e0e 172,916 bytes
- `provenance.json` b55dcda494ff7fa675bdade5d18cd9c720a7f4c91f3c8902067bb528fe41a621 1,010 bytes
- `rendered.html` e632d2722b6bc2f11dae20c788c7c087967ff8b1617f9e49874b67f34f3ccbc7 171,073 bytes
- `screenshot.png` 40cb4bc63512079ac9f9922051f970143f708fe8f10a7839fdf8f3a8cebe109d 2,916,589 bytes
- `text.txt` e87c134fef2ac6dadce17cc4b2ede04888da65e4c1939814c3e2acc5683ddb81 28,797 bytes

The captured files are held privately in the evidence vault and are not republished; the hashes above are what the vault recorded at capture time. [Every source →](../index.html)


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/sources/gist-blevene-detection-guide/index.html
