// Audio Custom · shared behaviour for every page

// Copy email (works where mail apps don't open, e.g. webmail users)
document.querySelectorAll('.copy-email').forEach((btn) => {
  const label = btn.textContent;
  btn.addEventListener('click', async () => {
    const email = btn.dataset.email;
    try {
      await navigator.clipboard.writeText(email);
    } catch (e) {
      const target = document.querySelector('.contact-email');
      if (target) {
        const r = document.createRange();
        r.selectNodeContents(target);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(r);
        try { document.execCommand('copy'); } catch (_) {}
      }
    }
    btn.textContent = 'Copied: ' + email;
    setTimeout(() => { btn.textContent = label; }, 2500);
  });
});

// Nav border on scroll
const nav = document.getElementById('nav');
if (nav) {
  const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 20);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// Routes map: draw the lines when the map scrolls into view
const map = document.querySelector('.routes-map');
if (map) {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) {
    map.classList.add('is-drawn');
  } else {
    map.classList.add('is-ready');
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          map.classList.add('is-drawn');
          io.disconnect();
        }
      });
    }, { threshold: 0.35 });
    io.observe(map);
  }
}

// Product gallery: thumbnails swap the main image
document.querySelectorAll('.product-gallery').forEach((g) => {
  const main = g.querySelector('.pg-main img');
  g.querySelectorAll('.pg-thumbs button').forEach((b) => {
    b.addEventListener('click', () => {
      main.src = b.dataset.src;
      main.alt = b.dataset.alt || main.alt;
      g.querySelectorAll('.pg-thumbs button').forEach((x) => x.setAttribute('aria-pressed', 'false'));
      b.setAttribute('aria-pressed', 'true');
    });
  });
});

// Mobile menu
const toggle = document.querySelector('.menu-toggle');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.textContent = open ? 'Close' : 'Menu';
  });
  nav.querySelectorAll('.nav-links a').forEach((a) => a.addEventListener('click', () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.textContent = 'Menu';
  }));
}
