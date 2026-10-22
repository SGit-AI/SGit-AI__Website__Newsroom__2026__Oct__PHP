/* The briefing deck (storyboard@php.newsroom). Draws the silent storyboard panels and the faces with the vendored
   storyboard kit, then sets window.__deckReady (admin/build/deck_pdf.js waits for it before printing). Present shows one
   slide at a time, full screen, moved with the arrow keys, space, PageUp/PageDown, a click or a swipe; Esc leaves.
   Nothing is stored. */
(function () {
  'use strict';
  var deck = document.querySelector('.dk-deck');
  if (!deck) return;
  var data = JSON.parse((document.querySelector('script.bd-data') || {}).textContent || '{}');
  function draw() {
    var K = window.StoryboardKit, cast = data.cast;
    if (!K || !cast) return;
    var who = function (id) { return cast.characters.filter(function (c) { return c.id === id; })[0]; };
    [].forEach.call(document.querySelectorAll('svg[data-strip]'), function (svg) {
      var b = data.boards[svg.getAttribute('data-strip')], i = +svg.getAttribute('data-panel');
      var sc = JSON.parse(JSON.stringify(b.scenes[i]));
      // silent: the lines and the caption are printed under the panel, readable at strip size
      (sc.cast || []).forEach(function (c) { delete c.says; delete c.thinks; });
      delete sc.caption;
      if (sc.kind === 'punchline') { sc.kind = 'scene'; delete sc.punchline; }
      K.drawScene(svg, sc, cast, { seed: 11 + i });
    });
    [].forEach.call(document.querySelectorAll('svg.bd-face[data-who]'), function (svg, i) {
      K.figure(svg, who(svg.getAttribute('data-who')), 'stand', 'happy', 'face', 3 + i);
    });
  }
  var fonts = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
  fonts.then(function () { try { draw(); } finally { window.__deckReady = true; } });

  var slides = [].slice.call(deck.querySelectorAll('.bd-slide')), i = 0, on = false, x0 = null;
  function show(n) {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach(function (s, k) { s.classList.toggle('dk-cur', k === i); });
    if (history.replaceState) history.replaceState(null, '', '#slide-' + (i + 1));
  }
  function start() {
    var m = /^#slide-(\d+)$/.exec(location.hash); on = true;
    deck.classList.add('dk-on'); document.documentElement.classList.add('dk-lock');
    show(m ? +m[1] - 1 : 0);
    if (deck.requestFullscreen) deck.requestFullscreen().catch(function () {});
  }
  function stop() {
    on = false; deck.classList.remove('dk-on'); document.documentElement.classList.remove('dk-lock');
    if (document.fullscreenElement && document.exitFullscreen) document.exitFullscreen().catch(function () {});
    slides[i].scrollIntoView({ block: 'start' });
  }
  var pb = document.querySelector('.dk-present'), pr = document.querySelector('.dk-print');
  if (pb) pb.addEventListener('click', start);
  if (pr) pr.addEventListener('click', function () { window.print(); });
  document.addEventListener('fullscreenchange', function () { if (on && !document.fullscreenElement) stop(); });
  document.addEventListener('keydown', function (e) {
    if (!on) return;
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].indexOf(e.key) >= 0) { e.preventDefault(); show(i + 1); }
    else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].indexOf(e.key) >= 0) { e.preventDefault(); show(i - 1); }
    else if (e.key === 'Home') show(0); else if (e.key === 'End') show(slides.length - 1);
    else if (e.key === 'Escape') stop();
  });
  deck.addEventListener('click', function (e) { if (on && !e.target.closest('a,summary')) show(i + (e.clientX < window.innerWidth / 3 ? -1 : 1)); });
  deck.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  deck.addEventListener('touchend', function (e) { if (on && x0 !== null) { var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1)); } x0 = null; });
})();
