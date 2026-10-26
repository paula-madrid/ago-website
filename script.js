(function () {
  var work = document.getElementById('work-view');
  var info = document.getElementById('info-view');
  var lb = document.getElementById('lightbox');
  var lbImg = lb.querySelector('img.lb-img');
  var lbVid = lb.querySelector('.lb-vid');
  var lbCap = lb.querySelector('.lb-caption');
  var current = null; // {slides, title, i}

  /* views: #information shows the studio text, anything else shows the work */
  function route() {
    var h = location.hash.slice(1);
    var isInfo = h === 'information';
    info.hidden = !isInfo;
    work.hidden = isInfo;
    if (isInfo) { window.scrollTo(0, 0); return; }
    var el = h && document.getElementById(h);
    if (el) el.scrollIntoView(); else if (!h) window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', route);
  route();

  /* slideshows */
  function imgs(s) { return s.querySelectorAll('.frame > img, .frame > video'); }
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var EASE = 'transform .55s cubic-bezier(.25,.8,.25,1)';
  function play(v) { if (!reduce.matches) { var r = v.play(); if (r && r.catch) r.catch(function () {}); } }
  /* videos play only while their slideshow is on screen */
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) {
    es.forEach(function (en) {
      var s = en.target, v = imgs(s)[idx(s)];
      if (v && v.tagName === 'VIDEO') { if (en.isIntersecting) play(v); else v.pause(); }
    });
  }) : null;
  if (io) document.querySelectorAll('.slides').forEach(function (s) { if (s.querySelector('video')) io.observe(s); });
  function idx(s) { return +(s.dataset.i || 0); }
  /* slide the current image out and the new one in from the side it comes from */
  function show(s, i, dir) {
    var l = imgs(s), n = l.length, cur = idx(s);
    i = (i + n) % n;
    if (i === cur) return i;
    var a = l[cur], b = l[i];
    for (var k = 0; k < n; k++) if (k !== cur && k !== i) { l[k].hidden = true; l[k].style.transition = ''; l[k].style.transform = ''; }
    s.dataset.i = i;
    if (reduce.matches) { a.hidden = true; b.hidden = false; }
    else {
      b.style.transition = 'none';
      b.style.transform = 'translateX(' + (dir * 100) + '%)';
      b.hidden = false;
      void b.offsetWidth; // start position applied before animating
      a.style.transition = b.style.transition = EASE;
      a.style.transform = 'translateX(' + (-dir * 100) + '%)';
      b.style.transform = 'translateX(0)';
      setTimeout(function () {
        if (l[idx(s)] !== a) a.hidden = true;
        a.style.transition = ''; a.style.transform = '';
      }, 600);
    }
    if (a.tagName === 'VIDEO') a.pause();
    if (b.tagName === 'VIDEO') play(b);
    l[(i + 1) % n].loading = 'eager'; // warm the next one
    return i;
  }
  document.querySelectorAll('.slides').forEach(function (s) {
    var title = s.closest('.project').querySelector('h2').textContent;
    s.querySelector('.prev').addEventListener('click', function () { show(s, idx(s) - 1, -1); });
    s.querySelector('.next').addEventListener('click', function () { show(s, idx(s) + 1, 1); });
    s.querySelector('.frame').addEventListener('click', function () { open(s, title); });
    s.querySelector('.enlarge').addEventListener('click', function (e) { e.stopPropagation(); open(s, title); });
    swipe(s, function (d) { show(s, idx(s) + d, d); });
  });

  /* lightbox */
  function paint(d) {
    var l = imgs(current.slides), img = l[current.i];
    var isVid = img.tagName === 'VIDEO', el = isVid ? lbVid : lbImg;
    lbImg.hidden = isVid; lbVid.hidden = !isVid;
    if (isVid) { if (lbVid.getAttribute('src') !== img.getAttribute('src')) lbVid.src = img.getAttribute('src'); play(lbVid); }
    else { lbVid.pause(); lbImg.src = img.currentSrc || img.src; }
    if (d && el.animate && !reduce.matches)
      el.animate([{ transform: 'translateX(' + (d * 6) + '%)', opacity: 0 }, { transform: 'none', opacity: 1 }],
                    { duration: 450, easing: 'cubic-bezier(.25,.8,.25,1)' });
    lbImg.alt = img.alt || '';
    lbCap.innerHTML = '';
    var b = document.createElement('b'); b.textContent = current.title;
    lbCap.append(b, '  ' + (current.i + 1) + ' / ' + l.length);
  }
  function step(d) {
    current.i = show(current.slides, current.i + d, d); // keeps the page slideshow in step
    paint(d);
  }
  function open(s, title) {
    current = { slides: s, title: title, i: idx(s) };
    paint();
    lb.hidden = false;
    document.body.classList.add('locked');
    lb.querySelector('.lb-close').focus();
  }
  function close() {
    lbVid.pause();
    lb.hidden = true;
    document.body.classList.remove('locked');
    if (current) current.slides.querySelector('.frame').focus();
    current = null;
  }
  lb.querySelector('.prev').addEventListener('click', function () { step(-1); });
  lb.querySelector('.next').addEventListener('click', function () { step(1); });
  lb.querySelector('.lb-close').addEventListener('click', close);
  lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
  swipe(lb, function (d) { step(d); });
  document.addEventListener('keydown', function (e) {
    if (!current) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });

  /* desktop rows: both projects in a row get the text height of the taller one when closed,
     so images line up; each column still stacks on its own */
  var mobile = window.matchMedia('(max-width:760px)');
  function alignRows() {
    var ps = Array.prototype.slice.call(document.querySelectorAll('.project'));
    ps.forEach(function (p) { p.style.removeProperty('--row-h'); });
    if (mobile.matches) return;
    function closedH(p) {
      function hgt(el) { return el.getBoundingClientRect().height; }
      return Math.ceil(Math.max(hgt(p.querySelector('.head')),
                                hgt(p.querySelector('.body'))));
    }
    var L = document.querySelectorAll('.col-left .project'), R = document.querySelectorAll('.col-right .project');
    for (var i = 0; i < L.length; i++) {
      var pair = R[i] ? [L[i], R[i]] : [L[i]];
      var h = Math.max.apply(null, pair.map(closedH));
      pair.forEach(function (p) { p.style.setProperty('--row-h', h + 'px'); });
    }
  }
  alignRows();
  window.addEventListener('resize', alignRows);
  window.addEventListener('hashchange', alignRows); // the work view measures 0 while hidden
  if (document.fonts) document.fonts.ready.then(alignRows);

  /* horizontal swipe on touch screens */
  function swipe(el, fn) {
    var x0 = null, y0 = null;
    el.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; y0 = e.touches[0].clientY; }, { passive: true });
    el.addEventListener('touchend', function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) {
        fn(dx < 0 ? 1 : -1);
        el.dataset.swiped = '1'; setTimeout(function () { delete el.dataset.swiped; }, 400);
      }
      x0 = null;
    }, { passive: true });
    el.addEventListener('click', function (e) { if (el.dataset.swiped) { e.stopPropagation(); e.preventDefault(); } }, true);
  }
})();
