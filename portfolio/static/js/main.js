/* ── Navbar scroll effect ──────────────────────────────────── */
const nav = document.getElementById('mainNav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });
}

/* ── Fade-in on scroll ─────────────────────────────────────── */
const fadeEls = document.querySelectorAll('[data-aos]');
if (fadeEls.length) {
  const fadeObserver = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('aos-visible');
        fadeObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  fadeEls.forEach(el => {
    el.classList.add('aos-init');
    fadeObserver.observe(el);
  });
}

/* ── Skill bar animation trigger (home page) ───────────────── */
const homeBars = document.querySelectorAll('.skill-pill .skill-bar-fill');
if (homeBars.length) {
  const stored = {};
  homeBars.forEach(b => { stored[b] = b.style.width; b.style.width = '0'; });

  const barObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.width = stored[e.target] || e.target.dataset.width || '75%';
        barObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.2 });
  homeBars.forEach(b => barObs.observe(b));
}
