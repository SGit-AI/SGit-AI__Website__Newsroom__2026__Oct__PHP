#!/usr/bin/env node
// The briefing deck as PowerPoint: reads admin/content/decks/<date>__briefing.json, the same file build.py draws as
// HTML slides, and writes storyboards/<slug>/<slug>.pptx with its sidecar <slug>.pptx.json (the source's sha256, which
// the gate compares with the deck, so a stale PowerPoint cannot ship). Native shapes and charts, speaker notes with
// every slide's sources. Not part of build.py (which is standard library only): run it after changing a deck.
// Usage: NODE_PATH=<dir holding pptxgenjs> node admin/build/deck_pptx.js [deck.json ...]
const fs = require('fs'), path = require('path'), crypto = require('crypto');
let PptxGenJS;
try { PptxGenJS = require('pptxgenjs'); } catch (e) { console.error('needs pptxgenjs: npm install pptxgenjs@3.12.0 in a scratch folder, then NODE_PATH=<it>/node_modules'); process.exit(2); }
const ROOT = path.resolve(__dirname, '..', '..');
const SITE = 'https://php.oct.2026.newsroom.sgit.ai';
const C = { ink: '16202C', head: '0B3B3A', accent: '0F766E', dim: '475569', tile: 'F1F5F9', mint: 'EEF6F5', dark: '0B3B3A', light: 'F1F5F4', pale: 'CDE7E3', warn: '9A3412' };
const STATUS = { confirmed: ['15803D', 'DCFCE7'], reported: ['1D4ED8', 'DBEAFE'], disputed: ['B45309', 'FEF3C7'], contradicted: ['B91C1C', 'FEE2E2'], unverified: ['475569', 'E5E7EB'] };
const FONT = 'Calibri', HEAD = 'Calibri';
const W = 13.333, H = 7.5, M = 0.6;
const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const nice = (d) => `${+d.slice(8)} ${MONTHS[+d.slice(5, 7) - 1]} ${d.slice(0, 4)}`;

function pill(slide, st, x, y) {
  if (!st || !STATUS[st]) return;
  slide.addText(st.toUpperCase(), { x, y, w: 1.35, h: 0.28, fontFace: FONT, fontSize: 10, bold: true, color: STATUS[st][0], fill: { color: STATUS[st][1] },
    shape: 'roundRect', rectRadius: 0.06, align: 'center', valign: 'middle', margin: 0, isTextBox: true, charSpacing: 1 });
}

function build(file) {
  const raw = fs.readFileSync(file), deck = JSON.parse(raw);
  const pres = new PptxGenJS();
  pres.layout = 'LAYOUT_WIDE';
  pres.title = `${deck.title}, ${nice(deck.date)}`; pres.author = 'storyboard@php.newsroom'; pres.company = 'PHP October 2026, SGit Newsroom';
  pres.subject = deck.subtitle;
  pres.theme = { headFontFace: HEAD, bodyFontFace: FONT };
  const foot = `PHP October 2026 · briefing of ${nice(deck.date)} · evidence as of ${deck.data_as_of}`;
  pres.defineSlideMaster({ title: 'DARK', background: { color: C.dark },
    objects: [{ text: { text: foot, options: { x: M, y: H - 0.5, w: 9, h: 0.3, fontFace: FONT, fontSize: 10, color: '7FB8B0', margin: 0 } } }],
    slideNumber: { x: W - M - 0.8, y: H - 0.5, w: 0.8, h: 0.3, fontFace: FONT, fontSize: 10, color: '7FB8B0', align: 'right' } });
  pres.defineSlideMaster({ title: 'CONTENT', background: { color: 'FFFFFF' },
    objects: [{ placeholder: { options: { name: 'title', type: 'title', x: M, y: 0.4, w: W - 2 * M, h: 0.9, fontFace: HEAD, fontSize: 36, bold: true, color: C.head, margin: 0, valign: 'top', align: 'left' }, text: '' } },
              { text: { text: foot, options: { x: M, y: H - 0.5, w: 9, h: 0.3, fontFace: FONT, fontSize: 10, color: '64748B', margin: 0 } } }],
    slideNumber: { x: W - M - 0.8, y: H - 0.5, w: 0.8, h: 0.3, fontFace: FONT, fontSize: 10, color: '64748B', align: 'right' } });

  deck.slides.forEach((sl, n) => {
    const dark = sl.kind === 'title' || sl.kind === 'closing';
    const s = pres.addSlide({ masterName: dark ? 'DARK' : 'CONTENT' });
    const notes = [sl.note || '', '', 'Sources (captured into the evidence vault; each has its page):', ...(sl.cites || []).map(c => `${SITE}/sources/${c}/index.html`)];
    s.addNotes(notes.join('\n'));
    let y = 1.35;
    if (dark) {
      s.addText('PHP OCTOBER 2026 · BRIEFING', { x: M + 0.2, y: 1.2, w: 10, h: 0.4, fontFace: FONT, fontSize: 14, color: '7DD3C8', charSpacing: 3, margin: 0, isTextBox: true });
      s.addText(sl.title, { x: M + 0.2, y: 1.7, w: W - 2 * M, h: 1.3, fontFace: HEAD, fontSize: 54, bold: true, color: 'FFFFFF', margin: 0, isTextBox: true });
      s.addText(sl.lead || '', { x: M + 0.2, y: 3.05, w: 10, h: 1.1, fontFace: FONT, fontSize: 22, color: C.pale, margin: 0, valign: 'top', isTextBox: true });
      if (sl.points) s.addText(sl.points.map((p, i) => ({ text: p.text, options: { bullet: true, breakLine: i < sl.points.length - 1 } })),
        { x: M + 0.2, y: 4.2, w: W - 2 * M - 0.4, h: 1.5, fontFace: FONT, fontSize: 18, color: C.light, paraSpaceAfter: 6, margin: 0, valign: 'top', isTextBox: true });
      s.addText(sl.dateline || '', { x: M + 0.2, y: sl.points ? 5.8 : 4.4, w: W - 2 * M - 0.4, h: 0.7, fontFace: FONT, fontSize: 15, color: 'A7D4CD', margin: 0, valign: 'top', isTextBox: true });
      return;
    }
    s.addText(sl.title, { placeholder: 'title', align: 'left' });
    if (sl.lead) { s.addText(sl.lead, { x: M, y: 1.25, w: W - 2 * M, h: 0.5, fontFace: FONT, fontSize: 18, color: '334155', margin: 0, isTextBox: true }); y = 1.9; }
    const bullets = (pts, x, yy, w, h, size) => s.addText(pts.map((p, i) => ({ text: (p.status ? `[${p.status}] ` : '') + (p.head ? p.head + ': ' : '') + p.text, options: { bullet: true, breakLine: i < pts.length - 1 } })),
      { x, y: yy, w, h, fontFace: FONT, fontSize: size || 16, color: C.ink, paraSpaceAfter: 8, margin: 0, valign: 'top', isTextBox: true });
    if (sl.kind === 'bottomline') {
      const cw = (W - 2 * M - 0.6) / 3;
      sl.points.forEach((p, i) => {
        const x = M + i * (cw + 0.3);
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.5, w: cw, h: 4.9, fill: { color: C.mint }, line: { color: C.mint }, rectRadius: 0.12, objectName: `card-${i + 1}` });
        s.addText(String(i + 1), { x: x + 0.35, y: 1.75, w: 1, h: 0.9, fontFace: HEAD, fontSize: 54, bold: true, color: C.accent, margin: 0, isTextBox: true });
        s.addText(p.head, { x: x + 0.35, y: 2.75, w: cw - 0.7, h: 0.9, fontFace: HEAD, fontSize: 24, bold: true, color: C.head, margin: 0, valign: 'top', isTextBox: true });
        s.addText(p.text, { x: x + 0.35, y: 3.7, w: cw - 0.7, h: 2.0, fontFace: FONT, fontSize: 17, color: C.ink, margin: 0, valign: 'top', isTextBox: true });
        pill(s, p.status, x + 0.35, 5.85);
      });
    }
    if (sl.stats) {
      const tw = (W - 2 * M - 0.9) / 4;
      sl.stats.forEach((t, i) => {
        const x = M + i * (tw + 0.3);
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: tw, h: 2.25, fill: { color: C.tile }, line: { color: C.tile }, rectRadius: 0.1, objectName: `stat-${i + 1}` });
        s.addText(t.value, { x: x + 0.25, y: y + 0.15, w: tw - 0.5, h: 0.85, fontFace: HEAD, fontSize: t.value.length > 4 ? 36 : 48, bold: true, color: C.accent, margin: 0, isTextBox: true });
        s.addText(t.label, { x: x + 0.25, y: y + 1.0, w: tw - 0.5, h: 0.4, fontFace: FONT, fontSize: 15, bold: true, color: C.ink, margin: 0, isTextBox: true });
        s.addText(t.sub || '', { x: x + 0.25, y: y + 1.38, w: tw - 0.5, h: 0.32, fontFace: FONT, fontSize: 11, color: C.dim, margin: 0, isTextBox: true });
        pill(s, t.status, x + 0.25, y + 1.8);
      });
      if (sl.points) bullets(sl.points, M, y + 2.6, W - 2 * M, 2.4, 16);
    }
    if (sl.kind === 'timeline') {
      const cw = (W - 2 * M - 1.2) / 5;
      sl.moments.forEach((m, i) => {
        const x = M + i * (cw + 0.3);
        s.addShape(pres.shapes.RECTANGLE, { x, y: 1.6, w: cw, h: 0.08, fill: { color: C.accent }, line: { color: C.accent }, objectName: `tick-${i + 1}` });
        s.addText(m.when, { x, y: 1.8, w: cw, h: 0.6, fontFace: HEAD, fontSize: 26, bold: true, color: C.head, margin: 0, isTextBox: true });
        s.addText(m.what, { x, y: 2.45, w: cw, h: 3.2, fontFace: FONT, fontSize: 16, color: C.ink, margin: 0, valign: 'top', isTextBox: true });
      });
    }
    if (sl.kind === 'bars') {
      const rows = sl.bars.rows;
      s.addChart(pres.charts.BAR, [{ name: sl.bars.title, labels: rows.map(r => r.label), values: rows.map(r => r.value) }], {
        x: M, y, w: 6.4, h: 4.4, barDir: 'bar', chartColors: rows.map(r => r.colour), showTitle: true, title: sl.bars.title, titleFontSize: 14, titleColor: C.head, titleFontFace: '+mn-lt',
        showValue: true, dataLabelPosition: 'outEnd', dataLabelFontSize: 12, dataLabelFontFace: '+mn-lt', dataLabelColor: C.ink, catAxisOrientation: 'maxMin',
        catAxisLabelColor: '334155', catAxisLabelFontSize: 13, catAxisLabelFontFace: '+mn-lt', valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, showLegend: false, barGapWidthPct: 40 });
      s.addText(`From ${sl.bars.from.file}`, { x: M, y: y + 4.45, w: 6.4, h: 0.3, fontFace: FONT, fontSize: 10, color: '64748B', margin: 0, isTextBox: true });
      if (sl.points) bullets(sl.points, M + 6.9, y + 0.2, W - 2 * M - 6.9, 4.2, 16);
    }
    if (sl.kind === 'ladder') {
      sl.steps.forEach((st, i) => {
        const yy = 1.5 + i * 0.78, w = W - 2 * M - i * 0.55, hot = st.status === 'confirmed';
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y: yy, w, h: 0.64, fill: { color: hot ? 'DCFCE7' : C.tile }, line: { color: hot ? 'DCFCE7' : C.tile }, rectRadius: 0.08, objectName: `rung-${i + 1}` });
        s.addText(st.value, { x: M + 0.25, y: yy, w: 2.2, h: 0.64, fontFace: HEAD, fontSize: 26, bold: true, color: C.accent, margin: 0, valign: 'middle', isTextBox: true });
        s.addText(st.label, { x: M + 2.5, y: yy, w: w - 4.3, h: 0.64, fontFace: FONT, fontSize: 17, color: C.ink, margin: 0, valign: 'middle', isTextBox: true });
        pill(s, st.status, M + w - 1.6, yy + 0.18);
      });
    }
    if (sl.kind === 'columns') {
      const cw = (W - 2 * M - 0.6) / 3;
      sl.cols.forEach((c, i) => {
        const x = M + i * (cw + 0.3);
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.5, w: cw, h: 4.3, fill: { color: C.tile }, line: { color: C.tile }, rectRadius: 0.1, objectName: `column-${i + 1}` });
        s.addText(c.head, { x: x + 0.3, y: 1.7, w: cw - 0.6, h: 0.5, fontFace: HEAD, fontSize: 20, bold: true, color: C.head, margin: 0, isTextBox: true });
        pill(s, c.status, x + 0.3, 2.25);
        s.addText(c.points.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j < c.points.length - 1 } })),
          { x: x + 0.3, y: 2.7, w: cw - 0.6, h: 3.0, fontFace: FONT, fontSize: 16, color: C.ink, paraSpaceAfter: 8, margin: 0, valign: 'top', isTextBox: true });
      });
      if (sl.later) s.addText(sl.later, { x: M, y: 6.0, w: W - 2 * M, h: 0.35, fontFace: FONT, fontSize: 12, color: C.warn, margin: 0, isTextBox: true });
    }
    if (sl.kind === 'list') bullets(sl.points, M, 1.5, W - 2 * M, 4.8, 18);
  });
  const out = path.join(ROOT, 'storyboards', deck.slug, deck.slug + '.pptx');
  fs.mkdirSync(path.dirname(out), { recursive: true });
  return pres.writeFile({ fileName: out }).then(() => {
    fs.writeFileSync(out + '.json', JSON.stringify({ what: 'The PowerPoint beside it was made by admin/build/deck_pptx.js from the deck source named here; the gate refuses it if the source has changed since.',
      source: path.relative(ROOT, file), source_sha256: crypto.createHash('sha256').update(raw).digest('hex'), slides: deck.slides.length, made_with: 'pptxgenjs ' + (PptxGenJS.version || '') }, null, 1) + '\n');
    console.log(`wrote ${path.relative(ROOT, out)} (${deck.slides.length} slides)`);
  });
}

const files = process.argv.slice(2);
const dir = path.join(ROOT, 'admin', 'content', 'decks');
(files.length ? files : fs.readdirSync(dir).filter(f => f.endsWith('.json')).map(f => path.join(dir, f))).reduce((p, f) => p.then(() => build(f)), Promise.resolve());
