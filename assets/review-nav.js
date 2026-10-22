// php.oct.2026.newsroom.sgit.ai /review/ui/: a small navigator over data/review.json.
// Three layers (the flaws, what the fix does, the code), a force-laid SVG graph with no library,
// a breadcrumb, and a panel for the node in focus. Click a node or a list item to move.
(async function () {
  const root = document.documentElement.getAttribute('data-root') || '../../'
  let G
  try { G = await (await fetch(root + 'data/review.json', { cache: 'no-store' })).json() } catch (e) { document.getElementById('rv').textContent = 'Could not load the review graph.'; return }
  const byId = new Map(G.nodes.map(n => [n.id, n]))
  const nbr = new Map(G.nodes.map(n => [n.id, []]))
  for (const e of G.edges) { nbr.get(e.from)?.push({ id: e.to, rel: e.rel, dir: 'out' }); nbr.get(e.to)?.push({ id: e.from, rel: e.rel, dir: 'in' }) }
  const layerName = Object.fromEntries(G.layers.map(l => [l.id, l.name]))
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]))
  let focus = location.hash.slice(1) || 'fix-commit'
  if (!byId.has(focus)) focus = 'fix-commit'

  function rank(rel) { return ({ fixes: 0, addresses: 0, introduces: 1, 'realised in': 1, contains: 3, touches: 3 })[rel] ?? 2 }
  function layout(center) {
    // the focus plus its neighbours, placed by a tiny force simulation
    const order = nbr.get(center).slice().sort((a, b) => rank(a.rel) - rank(b.rel))
    const ids = [center, ...order.slice(0, 16).map(x => x.id)]
    const set = [...new Set(ids)]
    const P = new Map(), W = 640, H = 420
    set.forEach((id, i) => { const a = (i / set.length) * Math.PI * 2; P.set(id, { x: W / 2 + Math.cos(a) * 150, y: H / 2 + Math.sin(a) * 120 }) })
    P.set(center, { x: W / 2, y: H / 2 })
    const links = []
    for (const n of nbr.get(center)) if (P.has(n.id)) links.push([center, n.id])
    for (let t = 0; t < 180; t++) {
      const k = 1 - t / 180
      for (const a of set) for (const b of set) if (a < b) {
        const pa = P.get(a), pb = P.get(b), dx = pa.x - pb.x, dy = pa.y - pb.y, d = Math.hypot(dx, dy) || 1, f = (2400 / (d * d)) * k
        pa.x += dx / d * f; pa.y += dy / d * f; pb.x -= dx / d * f; pb.y -= dy / d * f
      }
      for (const [a, b] of links) {
        const pa = P.get(a), pb = P.get(b), dx = pb.x - pa.x, dy = pb.y - pa.y, d = Math.hypot(dx, dy) || 1, f = (d - 140) * 0.05 * k
        if (a !== center) { pa.x += dx / d * f; pa.y += dy / d * f }
        pb.x -= dx / d * f; pb.y -= dy / d * f
      }
      for (const id of set) { const p = P.get(id); p.x = Math.max(70, Math.min(W - 70, p.x)); p.y = Math.max(30, Math.min(H - 30, p.y)) }
      P.set(center, { x: W / 2, y: H / 2 })
    }
    return { P, links, W, H }
  }

  function render() {
    const n = byId.get(focus), { P, links, W, H } = layout(focus)
    const edge = (a, b) => `<path class="e" d="M${P.get(a).x},${P.get(a).y} C${(P.get(a).x + P.get(b).x) / 2},${P.get(a).y} ${(P.get(a).x + P.get(b).x) / 2},${P.get(b).y} ${P.get(b).x},${P.get(b).y}"/>`
    const dot = id => { const p = P.get(id), m = byId.get(id); return `<g class="nd l-${esc(m.layer)}${id === focus ? ' here' : ''}" tabindex="0" role="button" data-id="${esc(id)}"><circle cx="${p.x}" cy="${p.y}" r="${id === focus ? 9 : 6}"/><text x="${p.x}" y="${p.y - 12}" text-anchor="middle">${esc((m.name || id).slice(0, 30))}</text></g>` }
    const svg = `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="${esc(n.name)} and its neighbours">${links.map(l => edge(l[0], l[1])).join('')}${[...new Set([focus, ...nbr.get(focus).map(x => x.id)])].map(dot).join('')}</svg>`
    const rel = nbr.get(focus).map(x => `<li><span class="rl">${esc(x.dir === 'out' ? x.rel : '&larr; ' + x.rel)}</span> <a href="#${esc(x.id)}" data-id="${esc(x.id)}">${esc(byId.get(x.id).name)}</a> <span class="ly">${esc(layerName[byId.get(x.id).layer])}</span></li>`).join('')
    const extra = []
    if (n.func) extra.push(`<p><b>Functions.</b> <code>${esc(n.func)}</code></p>`)
    if (n.file) extra.push(`<p><b>In.</b> <code>${esc(n.file)}</code></p>`)
    if (n.ini) extra.push(`<p><b>New setting.</b> <code>${esc(n.ini)}</code></p>`)
    if (n.functions && n.functions.length) extra.push(`<p><b>Functions the fix changed.</b> ${n.functions.map(f => `<code>${esc(f)}</code>`).join(' ')}</p>`)
    if (n.url && /^https:\/\//.test(n.url)) extra.push(`<p><a href="${esc(n.url)}" rel="noopener nofollow">Open in php-src &#8599;</a></p>`)
    if (n.source) extra.push(`<p><a href="${root}sources/${esc(n.source)}/index.html">The source &rarr;</a></p>`)
    document.getElementById('rv').innerHTML =
      `<p class="crumb">${G.layers.map(l => `<span class="ly l-${l.id}${l.id === n.layer ? ' on' : ''}">${esc(l.name)}</span>`).join(' &rsaquo; ')}</p>
       <figure class="rgraph">${svg}</figure>
       <article class="rnode"><p class="kicker">${esc(layerName[n.layer])}</p><h2>${esc(n.name)}</h2><p>${esc(n.text)}</p>${extra.join('')}
       <h3>Connected</h3><ul class="rel">${rel}</ul></article>`
    document.querySelectorAll('[data-id]').forEach(el => el.addEventListener('click', ev => { ev.preventDefault(); focus = el.getAttribute('data-id'); location.hash = focus; render() }))
    document.querySelectorAll('.nd').forEach(el => el.addEventListener('keydown', ev => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); focus = el.getAttribute('data-id'); location.hash = focus; render() } }))
  }
  window.addEventListener('hashchange', () => { const h = location.hash.slice(1); if (byId.has(h) && h !== focus) { focus = h; render() } })
  render()
})()
