// php.oct-2026.story.sgit.ai: the menu toggle on narrow screens, and a note in the bar when this page is older
// than the release the site now serves (one same-origin read of /VERSION; nothing is sent anywhere else).
(function () {
  var v = document.querySelector('nav.site .ver'), root = document.documentElement.getAttribute('data-root') || '';
  if (v && window.fetch) fetch(root + 'VERSION?t=' + Date.now(), { cache: 'no-store' }).then(function (r) { return r.ok ? r.text() : ''; }).then(function (t) {
    var live = (t || '').trim(), mine = v.textContent.replace(/^v/, '');
    if (!/^\d+\.\d+\.\d+$/.test(live)) return;
    var a1 = live.split('.').map(Number), b1 = mine.split('.').map(Number), d = 0;
    for (var i = 0; i < 3 && !d; i++) d = a1[i] - (b1[i] || 0);
    if (d <= 0) return;
    var a = document.createElement('a'); a.className = 'ver newer'; a.href = root + 'status/index.html';
    a.title = 'This page is v' + mine + '; the site now serves v' + live + '. Reload for the new release; the pipeline page shows what changed and what is deploying.';
    a.textContent = 'v' + live + ' is live: reload'; v.insertAdjacentElement('afterend', a);
  }).catch(function () {});
})();
(function () {
  var b = document.querySelector('.nav-toggle'), n = document.getElementById('nav-items');
  if (!b || !n) return;
  b.addEventListener('click', function () {
    var open = n.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.querySelectorAll('.ni > .nl').forEach(function (a) {
    a.addEventListener('click', function (ev) {
      if (window.matchMedia('(max-width: 900px)').matches) { ev.preventDefault(); a.parentNode.classList.toggle('open'); }
    });
  });
})();
