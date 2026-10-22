#!/usr/bin/env node
// Prints the briefing deck page to PDF, one 1080 by 1350 page per slide, in headless Chromium, so the PDF is the page.
// Reads the built page from the working tree (run build.py first), waits for the storyboard panels and fonts
// (window.__deckReady), writes storyboards/<slug>/<slug>.pdf and its sidecar <slug>.pdf.json holding the deck source's
// sha256, which the gate compares with the deck so a stale PDF cannot ship. Not part of build.py (standard library only).
// Usage: node admin/build/deck_pdf.js [slug]   (needs Playwright; PLAYWRIGHT_CHROMIUM or the default Chromium)
const fs = require('fs'), path = require('path'), crypto = require('crypto'), http = require('http');
let chromium;
for (const m of ['playwright', '/opt/node-tools/node_modules/playwright']) { try { ({ chromium } = require(m)); break; } catch (e) {} }
if (!chromium) { console.error('needs playwright'); process.exit(2); }
const ROOT = path.resolve(__dirname, '..', '..');
const TYPES = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json', '.woff2': 'font/woff2', '.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml' };
const dir = path.join(ROOT, 'admin', 'content', 'decks');
const want = process.argv[2];

(async () => {
  // a local server for the working tree, and nothing else: the page's telemetry and outside requests are refused
  const srv = http.createServer((q, r) => {
    const f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0]));
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); return r.end(); }
    r.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r);
  }).listen(0);
  const port = srv.address().port;
  const exe = process.env.PLAYWRIGHT_CHROMIUM || (fs.existsSync('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') ? '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' : undefined);
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  for (const fn of fs.readdirSync(dir).filter(f => f.endsWith('.json'))) {
    const raw = fs.readFileSync(path.join(dir, fn)), deck = JSON.parse(raw);
    if (want && deck.slug !== want) continue;
    const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
    await page.route('**/*', (rt) => rt.request().url().startsWith(`http://localhost:${port}/`) ? rt.continue() : rt.abort());
    await page.goto(`http://localhost:${port}/storyboards/${deck.slug}/index.html`, { waitUntil: 'load' });
    await page.waitForFunction(() => window.__deckReady === true, null, { timeout: 30000 });
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(300);
    const out = path.join(ROOT, 'storyboards', deck.slug, deck.slug + '.pdf');
    await page.pdf({ path: out, width: '1080px', height: '1350px', printBackground: true, preferCSSPageSize: true });
    const pages = await page.evaluate(() => document.querySelectorAll('.bd-slide').length), bytes = fs.statSync(out).size;
    fs.writeFileSync(out + '.json', JSON.stringify({ what: 'The PDF beside it was printed from the deck page by admin/build/deck_pdf.js; the gate refuses it if the deck source has changed since.',
      source: path.relative(ROOT, path.join(dir, fn)), source_sha256: crypto.createHash('sha256').update(raw).digest('hex'), pages, bytes, size: '1080x1350' }, null, 1) + '\n');
    console.log(`wrote ${path.relative(ROOT, out)}: ${pages} pages, ${(bytes / 1048576).toFixed(1)} MB`);
    await page.close();
  }
  await browser.close(); srv.close();
})().catch(e => { console.error(e); process.exit(1); });
