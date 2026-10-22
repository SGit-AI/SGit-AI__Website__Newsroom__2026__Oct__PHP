// php.oct.2026.newsroom.sgit.ai: the Feedback tab of the pane on the right (assets/ask/ask.js draws the pane and calls
// draw() here). Kept by conductor@php.newsroom; the brief is admin/content/briefs/2026-10-22__brief__feedback-keys-and-review.md.
//
// A note on this page: what kind (wrong, unclear, missing, an idea, good), the words, and a screenshot if wanted (a file,
// or this screen captured with the browser's own permission prompt, scaled down here). It is signed with this device's
// key (assets/feedback/identity.js), encrypted to the collaborators key and posted to the collaborators lane. Without a
// key the tab says how to get one: an invitation from the editor. Nothing is kept in this browser but the key.
import { getIdentity, sign, sendToLane, siteData } from './identity.js'

const KINDS = [['wrong', 'Something is wrong'], ['unclear', 'Unclear'], ['missing', 'Missing'], ['idea', 'An idea'], ['good', 'This is good']]
const MAX_W = 1600
let shot = null      // { data: 'data:image/jpeg;base64,…', w, h } while the form is open

async function scaled(source, w, h) {
  const k = Math.min(1, MAX_W / w), c = document.createElement('canvas')
  c.width = Math.round(w * k); c.height = Math.round(h * k)
  c.getContext('2d').drawImage(source, 0, 0, c.width, c.height)
  for (const q of [0.75, 0.6, 0.45]) { const d = c.toDataURL('image/jpeg', q); if (d.length < 2_400_000) return { data: d, w: c.width, h: c.height } }
  throw new Error('the screenshot is too large even scaled down')
}
async function fromFile(file) {
  const bmp = await createImageBitmap(file)
  try { return await scaled(bmp, bmp.width, bmp.height) } finally { bmp.close && bmp.close() }
}
async function fromScreen() {
  const stream = await navigator.mediaDevices.getDisplayMedia({ video: { displaySurface: 'browser' }, audio: false, preferCurrentTab: true })
  try {
    const v = document.createElement('video'); v.srcObject = stream; v.muted = true; await v.play()
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))
    return await scaled(v, v.videoWidth, v.videoHeight)
  } finally { stream.getTracks().forEach(t => t.stop()) }
}

export async function draw(body, { h, root }) {
  const me = await getIdentity()
  const path = document.documentElement.getAttribute('data-path') || location.pathname
  const ver = document.documentElement.getAttribute('data-ver') || ''
  const quote = String(window.getSelection ? window.getSelection() : '').trim().slice(0, 500)   // taken now: pressing a button clears it
  if (!me) {
    body.append(h('p', null, h('b', null, 'Feedback needs a key. '), 'Contributors sign what they send, so the team knows who it came from. To get a key, ask Dinis for an invitation, by email or on WhatsApp: it is a link or QR code that makes a key on this device in one tap.'),
      h('p', null, h('a', { href: root + 'collaborators/index.html#join' }, 'Ask to join'), ' · ', h('a', { href: root + 'collaborators/index.html#feedback' }, 'or send unsigned feedback with the form')))
    return
  }
  const out = h('p', { role: 'status', 'aria-live': 'polite' })
  const say = (t, ok) => { out.textContent = t; out.className = ok ? 'sub-ok' : 'sub-err' }
  const kind = h('select', { name: 'kind' }, ...KINDS.map(([k, t]) => h('option', { value: k }, t)))
  const text = h('textarea', { name: 'text', rows: '5', maxlength: '4000', placeholder: 'What did you see, and what did you expect?' })
  const preview = h('div', { class: 'fb-shot' })
  const showShot = () => { preview.textContent = ''; if (shot) preview.append(h('img', { src: shot.data, alt: 'The screenshot to send', style: 'max-width:100%;border:1px solid var(--line);border-radius:6px' }), h('button', { type: 'button', class: 'rs-b', onclick: () => { shot = null; showShot() } }, 'Remove the screenshot')) }
  const file = h('input', { type: 'file', accept: 'image/*', onchange: async () => { try { if (file.files[0]) { shot = await fromFile(file.files[0]); showShot() } } catch (e) { say('That image could not be read: ' + e.message, false) } } })
  const cap = navigator.mediaDevices && navigator.mediaDevices.getDisplayMedia
    ? h('button', { type: 'button', class: 'rs-b', onclick: async () => { try { shot = await fromScreen(); showShot() } catch (e) { say('No screenshot taken (' + e.message + ')', false) } } }, 'Capture this screen') : null
  const form = h('form', { class: 'ask-key', onsubmit: async e => {
    e.preventDefault()
    if (!text.value.trim() && !shot) return say('Write something, or add a screenshot.', false)
    try {
      say('Signing and sending…', true)
      const { lane } = await siteData(root)
      const msg = await sign(me, { v: 1, kind: 'feedback', page: path, site: ver, about: kind.value, text: text.value.trim().slice(0, 4000),
        quote, at: new Date().toISOString(),
        screenshot: shot ? shot.data : '', bundle: me.bundle })
      await sendToLane(lane, msg)
      text.value = ''; shot = null; showShot(); file.value = ''
      say('Sent, signed with ' + me.bundle.signing_fingerprint + '. Thank you: the conductor reads it at the next run.', true)
    } catch (e2) { say('It could not be sent: ' + e2.message, false) }
  } },
    h('p', { class: 'small' }, 'On ', h('code', null, path), ' (v' + ver + ').', quote ? h('span', null, ' Quoting: \u201c', quote.slice(0, 140), '\u201d') : ' Select text on the page before opening Feedback to quote it.'),
    h('label', null, 'What kind ', kind), text,
    h('p', null, h('label', null, 'Screenshot (optional) ', file), ' ', cap), preview,
    h('button', { type: 'submit', class: 'rs-b' }, 'Sign and send'), out)
  body.append(form, h('p', { class: 'small' }, 'Signed with this device’s key ', h('code', null, me.bundle.signing_fingerprint), ', encrypted in this browser to the team’s key and sent to a private vault. The site never shows it.'))
  showShot()
}
