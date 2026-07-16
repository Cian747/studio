'use strict';

// ── Nav scroll state ──────────────────────────────────────
const header = document.getElementById('siteHeader');
if (header) {
  const onScroll = () =>
    header.classList.toggle('is-scrolled', window.scrollY > 24);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

// ── Mobile burger ─────────────────────────────────────────
const burger  = document.getElementById('burger');
const mainNav = document.getElementById('mainNav');
if (burger && mainNav) {
  burger.addEventListener('click', () => {
    const open = mainNav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', open);
  });
  // Close on nav link click
  mainNav.querySelectorAll('a').forEach(a =>
    a.addEventListener('click', () => {
      mainNav.classList.remove('is-open');
      burger.setAttribute('aria-expanded', false);
    })
  );
}

// ── Auto-dismiss toasts ───────────────────────────────────
document.querySelectorAll('.toast').forEach(el => {
  setTimeout(() => {
    el.style.transition = 'opacity 0.4s';
    el.style.opacity    = '0';
    setTimeout(() => el.remove(), 420);
  }, 4500);
});

// ── Scroll-reveal (lightweight, no library) ───────────────
const revealEls = document.querySelectorAll(
  '.disc-card, .work-item, .pkg-card, .pillar, .gallery-cell, .pricing-note-card'
);
if ('IntersectionObserver' in window && revealEls.length) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity    = '1';
        e.target.style.transform  = 'translateY(0)';
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(el => {
    el.style.opacity    = '0';
    el.style.transform  = 'translateY(16px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    io.observe(el);
  });
}
