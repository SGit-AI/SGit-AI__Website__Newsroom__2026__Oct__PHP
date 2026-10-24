// php.oct.2026.newsroom.sgit.ai: /team/schedule/, the schedule vault read live in the browser. Kept by
// conductor@php.newsroom; the brief is admin/content/briefs/2026-10-23__brief__the-schedule-vault.md.
//
// The vault (data/schedule-vault.json) is public: this page opens it read-only with its published read key, with the
// vault library the rest of the site uses (assets/vendor/sg-vault, assets/vault/newsroom-vault.js), reads index.json
// and draws it: every schedule, every task (due, overdue, repeating, done), every run, and a run's log when it is
// opened. Everything read is text from the vault, shown as text.
const html = document.documentElement
const ROOT = new URL(html.getAttribute('data-root') || '../../', location.href).href
const LIB = ['sg-send/sg-send-crypto.js', 'sg-send/sg-send.js', 'sg-vault/sg-vault-crypto.js', 'sg-vault/sg-vault-object-store.js', 'sg-vault/sg-vault-ref-manager.js',
  'sg-vault/sg-vault-commit.js', 'sg-vault/sg-vault.js', 'sg-vault/sg-vault--file-ops.js', 'sg-vault/sg-vault--folder-ops.js', 'sg-vault/sg-vault--sync.js',
  'sg-vault/sg-vault--history.js', 'sg-vault/sg-vault--branches.js'].map(f => `${ROOT}assets/vendor/sg-vault/v0.2.3/${f}`).concat([`${ROOT}assets/vendor/sg-vault/local/sg-vault--create-with-id.js`])
const out = document.getElementById('schedule-app')
const cfg = JSON.parse(document.getElementById('schedule-config').textContent)
let NV = null, V = null, IDX = null, agent = '', since = null

function h(tag, attrs, ...kids) {
  const e = document.createElement(tag)
  for (const [k, v] of Object.entries(attrs || {})) { if (v == null) continue; if (k.startsWith('on')) e.addEventListener(k.slice(2), v); else if (k === 'class') e.className = v; else e.setAttribute(k, v) }
  for (const k of kids.flat()) if (k != null && k !== false) e.append(k)
  return e
}
const when = t => t ? t.replace('T', ' ').replace(/:\d\dZ?$/, '').replace(/Z$/, '') + ' UTC' : ''
const ago = t => { if (!t) return ''; const m = Math.round((Date.now() - Date.parse(t)) / 6e4); return m < 0 ? `in ${-m < 120 ? -m + ' min' : Math.round(-m / 60) + ' h'}` : m < 120 ? `${m} min ago` : m < 2880 ? `${Math.round(m / 60)} h ago` : `${Math.round(m / 1440)} days ago` }
const pill = (txt, cls) => h('span', { class: 'st st-' + cls }, txt)
const STATE = { active: 'confirmed', paused: 'contradicted', 'setting up': 'disputed' }
const OUT = { ok: 'confirmed', idle: 'reported', failed: 'contradicted', partial: 'disputed', running: 'disputed', unknown: 'reported' }

async function load() {
  for (const src of LIB) await new Promise((ok, no) => { const s = document.createElement('script'); s.src = src; s.onload = ok; s.onerror = () => no(new Error('could not load ' + src)); document.head.append(s) })
  NV = await import(ROOT + 'assets/vault/newsroom-vault.js')
  V = await NV.openReadOnly(NV.client({ endpoint: cfg.endpoint }), cfg.vault_id, cfg.read_key)
  IDX = await NV.readJson(V, '/index.json')
  since = new Date()
}

function taskState(t) {
  const now = new Date().toISOString()
  if (t.state === 'done') return pill('done', 'confirmed')
  if (t.state === 'failed') return pill('failed', 'contradicted')
  if (t.repeat_until && t.repeat_until < now) return pill('ended', 'reported')
  if (t.due_by && t.due_by < now) return pill('overdue', 'contradicted')
  if (t.not_before && t.not_before > now) return pill('not yet', 'reported')
  return pill(t.repeat_until ? 'repeating' : 'queued', 'disputed')
}

async function showLog(r, cell) {
  cell.replaceChildren(h('span', { class: 'small' }, 'Reading the run…'))
  try {
    const full = await NV.readJson(V, '/' + IDX.run_files[r.run])
    cell.replaceChildren(h('pre', { class: 'msg' }, full.log || '(no log recorded for this run)'))
  } catch (e) { cell.replaceChildren(h('span', { class: 'sub-err' }, 'Could not read it: ' + e.message)) }
}

function draw() {
  const agents = [...new Set([...IDX.schedules.map(s => s.agent), ...IDX.tasks.map(t => t.agent), ...IDX.runs.map(r => r.agent)])].sort()
  const pick = h('select', { onchange: e => { agent = e.target.value; draw() } }, h('option', { value: '' }, 'every agent'), ...agents.map(a => { const o = h('option', { value: a }, a); if (a === agent) o.selected = true; return o }))
  const mine = x => !agent || x.agent === agent
  const now = new Date().toISOString()
  const S = IDX.schedules.filter(mine), T = IDX.tasks.filter(mine), R = IDX.runs.filter(mine)
  const lastRun = a => IDX.runs.find(r => r.agent === a)
  const dueNow = T.filter(t => t.state === 'queued' && (!t.not_before || t.not_before <= now) && !(t.repeat_until && t.repeat_until < now))
  const overdue = T.filter(t => t.state === 'queued' && t.due_by && t.due_by < now)
  const sched = h('table', { class: 'board' }, h('thead', null, h('tr', null, ...['Agent', 'State', 'Wakes', 'How often', 'Model', 'Last run', 'Tasks due', 'Policy'].map(x => h('th', null, x)))),
    h('tbody', null, S.map(s => { const lr = lastRun(s.agent), n = dueNow.filter(t => t.agent === s.agent).length
      return h('tr', null, h('td', null, h('b', null, s.agent), h('div', { class: 'note' }, s.what)), h('td', null, pill(s.status, STATE[s.status] || 'reported'), s.note ? h('div', { class: 'note' }, s.note) : null),
        h('td', null, s.wakes), h('td', null, s.cadence), h('td', null, s.model || ''), h('td', null, lr ? [pill(lr.outcome, OUT[lr.outcome] || 'reported'), h('div', { class: 'note' }, ago(lr.started))] : 'none yet'),
        h('td', null, n ? String(n) : h('span', { class: 'small' }, n === 0 && s.status === 'active' ? 'none: it will idle' : '0')), h('td', { class: 'note' }, s.abp)) })))
  const tasks = h('table', { class: 'board' }, h('thead', null, h('tr', null, ...['Task', 'Agent', 'State', 'Due', 'Repeats until', 'Runs', 'Brief'].map(x => h('th', null, x)))),
    h('tbody', null, T.sort((a, b) => (a.state > b.state) - (a.state < b.state) || (a.due_by || '9').localeCompare(b.due_by || '9')).map(t => h('tr', null,
      h('td', null, h('code', null, t.id), h('div', null, t.title)), h('td', null, t.agent), h('td', null, taskState(t)), h('td', null, t.due_by ? [when(t.due_by), h('div', { class: 'note' }, ago(t.due_by))] : 'any time'),
      h('td', null, t.repeat_until ? when(t.repeat_until) : ''), h('td', null, String((t.runs || []).length), t.last_run ? h('div', { class: 'note' }, 'last ' + ago(t.last_run)) : null),
      h('td', { class: 'note' }, t.brief, h('div', { class: 'small' }, 'To run it now, tell a Claude session: ', h('code', null, `Run ${t.agent} task ${t.id} from the schedule vault (${cfg.vault_id}).`)))))))
  const runs = h('table', { class: 'board' }, h('thead', null, h('tr', null, ...['Started', 'Agent', 'Outcome', 'Took', 'Tasks', 'Summary', 'Log'].map(x => h('th', null, x)))),
    h('tbody', null, R.slice(0, 200).map(r => { const cell = h('td'); const took = r.finished && r.started ? Math.round((Date.parse(r.finished) - Date.parse(r.started)) / 6e4) + ' min' : ''
      cell.append(h('button', { type: 'button', class: 'rs-b', onclick: () => showLog(r, cell) }, 'Open'))
      return h('tr', null, h('td', null, when(r.started), h('div', { class: 'note' }, ago(r.started))), h('td', null, r.agent), h('td', null, pill(r.outcome, OUT[r.outcome] || 'reported')), h('td', null, took),
        h('td', null, (r.tasks || []).join(', ')), h('td', { class: 'note' }, r.summary || '', /^https?:\/\//.test(r.article || '') ? h('div', null, h('a', { href: r.article, rel: 'noopener' }, 'the article')) : null), cell) })))
  out.replaceChildren(
    h('p', { class: 'kv' }, h('b', null, 'Read live from the vault '), h('code', null, cfg.vault_id), ` at ${since.toISOString().slice(11, 16)} UTC (index built ${when(IDX.built)}). `,
      h('button', { type: 'button', class: 'rs-b', onclick: () => { out.replaceChildren(h('p', null, 'Reading the vault…')); load().then(draw).catch(fail) } }, 'Read again'), ' · Show ', pick),
    h('div', { class: 'stats' }, ...[[S.filter(s => s.status === 'active').length, 'schedules active'], [S.filter(s => s.status !== 'active').length, 'paused or setting up'], [dueNow.length, 'tasks due now'], [overdue.length, 'overdue'],
      [R.filter(r => r.started && Date.now() - Date.parse(r.started) < 864e5).length, 'runs in the last day']].map(([n, l]) => h('div', { class: 'stat' }, h('b', null, String(n)), h('span', null, l)))),
    h('h2', null, 'Schedules'), h('div', { class: 'tw' }, sched),
    h('h2', null, 'Tasks'), h('p', { class: 'small' }, 'No task due, no work: an agent woken with nothing queued records an idle run and stops. A repeating task runs on every wake until its date.'), h('div', { class: 'tw' }, tasks),
    h('h2', null, 'Runs'), h('p', { class: 'small' }, 'Newest first; open a run to read its log, fetched from the vault.'), h('div', { class: 'tw' }, runs))
}
function fail(e) { out.replaceChildren(h('p', { class: 'sub-err' }, 'The vault could not be read: ' + e.message + '. It also opens in the vault browser: '), h('a', { href: cfg.open_url, rel: 'noopener', target: '_blank' }, 'open the vault')) }
load().then(draw).catch(fail)
