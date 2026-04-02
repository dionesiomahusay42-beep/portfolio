/* ── Dark Mode ─────────────────────────────────────────────── */
(function () {
  const html   = document.documentElement;
  const KEY    = 'portfolio-theme';
  const saved  = localStorage.getItem(KEY) || 'dark';

  // Apply theme immediately (before paint)
  html.setAttribute('data-theme', saved);

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem(KEY, theme);

    // Update ALL toggle icons
    document.querySelectorAll('.theme-icon').forEach(el => {
      el.className = 'bi theme-icon ' + (theme === 'dark' ? 'bi-moon-fill' : 'bi-sun-fill');
    });
  }

  // Attach click handlers after DOM is ready
  document.addEventListener('DOMContentLoaded', function () {
    // Set correct icon on load
    setTheme(saved);

    // Attach to all toggle buttons
    document.querySelectorAll('.theme-toggle').forEach(btn => {
      btn.addEventListener('click', function () {
        const current = html.getAttribute('data-theme');
        setTheme(current === 'dark' ? 'light' : 'dark');
      });
    });
  });
})();

/* ── Navbar scroll effect ──────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function () {
  const nav = document.getElementById('mainNav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
  }

  /* ── Fade-in on scroll ───────────────────────────────────── */
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
    fadeEls.forEach(el => { el.classList.add('aos-init'); fadeObserver.observe(el); });
  }

  /* ── Skill bar animation (home page) ────────────────────── */
  const homeBars = document.querySelectorAll('.skill-pill .skill-bar-fill');
  if (homeBars.length) {
    const stored = {};
    homeBars.forEach(b => { stored[b] = b.style.width; b.style.width = '0'; });
    const barObs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.style.width = stored[e.target] || '75%';
          barObs.unobserve(e.target);
        }
      });
    }, { threshold: 0.2 });
    homeBars.forEach(b => barObs.observe(b));
  }

  /* ── Close mobile menu on link click ────────────────────── */
  document.querySelectorAll('#navbarNav .nav-link, #navbarNav .nav-cta').forEach(link => {
    link.addEventListener('click', () => {
      const collapse = document.getElementById('navbarNav');
      if (collapse && collapse.classList.contains('show')) {
        const bsCollapse = bootstrap.Collapse.getInstance(collapse);
        if (bsCollapse) bsCollapse.hide();
      }
    });
  });
});