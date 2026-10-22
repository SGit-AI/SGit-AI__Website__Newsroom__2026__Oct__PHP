/* The briefing deck (storyboard@php.newsroom): Present shows one slide at a time, full screen, moved with the arrow
   keys, space, PageUp/PageDown, a click or a swipe; Esc leaves. Print lays one slide per page. Nothing is stored. */
(function () {
  'use strict';
  var deck = document.querySelector('.dk-deck');
  if (!deck) return;
  var slides = [].slice.call(deck.querySelectorAll('.dk-slide')), i = 0, on = false, x0 = null;
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
  document.querySelector('.dk-present').addEventListener('click', start);
  var pr = document.querySelector('.dk-print');
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
