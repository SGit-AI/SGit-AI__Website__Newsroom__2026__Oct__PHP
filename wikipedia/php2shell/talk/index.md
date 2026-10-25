# What Wikipedia&#39;s editors discuss about the PHP2Shell article

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The talk page of the article as threads: 8 discussions and 23 posts, including the edit requests outside parties made with a disclosed conflict of interest.

[Wikipedia, as a graph](../../index.html) / [PHP2Shell](../index.html) / The talk page

# What Wikipedia's editors discuss about the PHP2Shell article

The article's [talk page](https://en.wikipedia.org/wiki/Talk%3APHP2Shell), as threads: 8 discussions, 23 signed posts, 40 revisions of the page since 2026-10-21 11:22:20 UTC. This is where corrections are argued, where outside parties ask for changes without editing the article (1 thread use the edit-request process, with a disclosed conflict of interest), and where readers say what the article does not yet explain. Every post links to its author's public Wikipedia page; a temporary account is Wikipedia's own pseudonym for a logged-out editor.

## The Man on the Clapham Omnibus (3 posts, 2026-10-21 20:59 UTC)
- **[Ericoides](https://en.wikipedia.org/wiki/User:Ericoides)** 2026-10-21 20:59 UTC Could there be a section explaining how this affects your average Joe who doesn't have a clue what most/all of the article means, e.g. are their home systems vulnerable?
- **[Kevstuff](https://en.wikipedia.org/wiki/User:Kevstuff)** 2026-10-21 21:11 UTC From what I know, would making the layout similar to Log4Shell be helpful? I don't know where to start though.
- **[Ericoides](https://en.wikipedia.org/wiki/User:Ericoides)** 2026-10-22 04:21 UTC Yes, that looks suitable.

## External link suggestion (conflict of interest disclosed) (2 posts, 2026-10-21 21:54 UTC) request edit
- **[Simgen321](https://en.wikipedia.org/wiki/User:Simgen321)** 2026-10-21 21:54 UTC request edit answered Disclosure: I built the tools below, so I am not adding anything to the article myself and will leave the decision to other editors. Readers of this article will mostly want to know whether their own site or server is affected. Two free resources may be useful in an "External links" section, if editors think they meet WP:EL: An open-source (MIT) script that lists every PHP installation on a server and flags PHP-FPM processes still running a replaced binary after the update: https://github.com/KyleClouthier/php2shell-check A browser check that reads a site's public signals (headers, CMS fingerprints) and explains what to ask the host if the version is hidden: https://simgen.dev/php-patch-check . This one is on my own business site, which also offers paid help, so editors may prefer the GitHub link alone. Happy for either or neither to be used. Thanks for maintaining the article.
- **[guninvalid](https://en.wikipedia.org/wiki/User:guninvalid)** 2026-10-22 05:02 UTC Do you have any reliable sources talking about this?

## Suggested source for detection and response (COI disclosure) (7 posts, 2026-10-21 23:16 UTC)
- **[guninvalid](https://en.wikipedia.org/wiki/User:guninvalid)** 2026-10-22 17:48 UTC
- **[~2026-56359-71](https://en.wikipedia.org/wiki/User:~2026-56359-71) (temporary account)** 2026-10-21 23:16 UTC I'm the author of the post below, so I'm disclosing a conflict of interest and not adding it myself. I briefly added it earlier on the wrong sentence and have removed it. The article doesn't yet cover how organizations can check whether they were compromised before patching. My post covers this (preserving logs, reviewing activity from 20 October onward, signs of web shells, and rotating secrets because one bug can leak server memory). Editors may find it useful for a "Detection and response" section, or may prefer a vendor source such as Huntress or watchTowr for the same points.  ~2026-56359-71 ( ~2026-56359-71 (
- **[AceZ1q](https://en.wikipedia.org/wiki/User:AceZ1q)** 2026-10-21 23:46 UTC Proposed addition to Impact: “Security researchers advised organizations to preserve logs, review activity from 20 October onward, and rotate credentials, since one of the flaws could leak server memory without code execution.”
- **[AceZ1q](https://en.wikipedia.org/wiki/User:AceZ1q)** 2026-10-21 23:46 UTC would you mind taking a look when you have a moment?
- **[Fubar Obfusco](https://en.wikipedia.org/wiki/User:Fubar_Obfusco)** 2026-10-22 01:08 UTC That article appears to have been written by an LLM, not a human author. See WP:RSPLLM.
- **[AceZ1q](https://en.wikipedia.org/wiki/User:AceZ1q)** 2026-10-22 02:54 UTC Thanks for taking a look. Understood, I'll withdraw the request.
- ***unsigned***

## Clarification on affected versions: Is PHP 5.3 affected or excluded? (1 post, 2026-10-22 01:53 UTC)
- **[~2026-56289-78](https://en.wikipedia.org/wiki/User:~2026-56289-78) (temporary account)** 2026-10-22 01:53 UTC Hello, The article currently lists the affected versions as "PHP versions 5.4–8.5" and states that versions "as early as 5.4" are affected. Could someone clarify whether PHP 5.3 (or earlier) is affected by CVE-2026-109618 and CVE-2026-109619, or if it is technically exempt? From what I understand from the technical advisories, the primary attack vectors—such as the RFC 1867 session upload-progress unserializer UAF—rely on features and Zend MM structures introduced in PHP 5.4. Does this mean PHP 5.3 and earlier completely lack the vulnerable attack surface for this specific exploit chain? If reliable sources confirm that PHP 5.3 is safe from this vulnerability, it might be helpful to add a brief clarification in the article for readers managing legacy systems. Thanks! ~2026-56289-78 (

## Is the attack still ongoing? (5 posts, 2026-10-23 09:32 UTC)
- **[guninvalid](https://en.wikipedia.org/wiki/User:guninvalid)** 2026-10-23 09:55 UTC
- **[SoyUnEditorRandom](https://en.wikipedia.org/wiki/User:SoyUnEditorRandom)** 2026-10-23 09:32 UTC Does this security issue—which has now persisted for 48 hours—still exist? As of October 23, sites such as pageviews.wmcloud.org and xtools.wmcloud.org are still failing to load. The problem has been ongoing since October 21, when it reached its peak. I am not sure if the inability to load these pages is directly due to this specific issue.
- **[Strongshorts](https://en.wikipedia.org/wiki/User:Strongshorts)** 2026-10-23 09:33 UTC Wikimedia Toolforge is still down. Please be patient
- **[SoyUnEditorRandom](https://en.wikipedia.org/wiki/User:SoyUnEditorRandom)** 2026-10-23 09:34 UTC Okay. Thank you.
- ***unsigned***

## AI (1 post, 2026-10-23 20:13 UTC)
- **[Joe vom Titan](https://en.wikipedia.org/wiki/User:Joe_vom_Titan)** 2026-10-23 20:13 UTC Many news sources emphasize that the vulnerabilities were discovered by AI. Shouldn't the lead mention this?

## Black October (3 posts, 2026-10-23 21:13 UTC)
- **[Carolineovo](https://en.wikipedia.org/wiki/User:Carolineovo)** 2026-10-23 21:13 UTC The event is now frequently being referred to as AI's "Black October" in the media. Should this be reflected either in the article or as a disambiguation?
- **[Vitorperrut555](https://en.wikipedia.org/wiki/User:Vitorperrut555)** 2026-10-24 01:15 UTC Only if it were widely covered by the media. [[User:Vitorperrut555|VitorFriboquen :] ]]
- **[guninvalid](https://en.wikipedia.org/wiki/User:guninvalid)** 2026-10-24 01:36 UTC It does seem to have at least 3 sources talking about it in depth. That being said, Black October seems to be referring to potential security incidents alongside both PHP2Shell and the Indian security key breach. For now I'll start a stub as Black October security incidents, but without prejudice for if someone else feels it should be merged into another article.

## Diagram explaining the attack (1 post, 2026-10-24 01:22 UTC)
- **[cmglee](https://en.wikipedia.org/wiki/User:cmglee)** 2026-10-24 01:22 UTC Would https://www.akamai.com/blog/security-research/understanding-php2shell-everything-you-need-to-know and https://outcomeschool.com/blog/php2shell be considered reputable sources if I wish to draw a diagram explaining how PHP2Shell works, in a similar style to this explanation for Heartbleed?

The posts are their authors', CC BY-SA 4.0, shown as text.


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/wikipedia/php2shell/talk/index.html
