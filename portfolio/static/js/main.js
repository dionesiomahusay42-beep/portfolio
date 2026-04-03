/* ── Dark Mode ─────────────────────────────────────────────── */
(function () {
  var html = document.documentElement;
  var saved = localStorage.getItem('portfolio-theme') || 'dark';
  html.setAttribute('data-theme', saved);
  updateIcons(saved);

  function updateIcons(theme) {
    document.querySelectorAll('.theme-icon').forEach(function(el) {
      el.className = theme === 'dark' ? 'bi bi-moon-fill theme-icon' : 'bi bi-sun-fill theme-icon';
    });
  }

  function toggleTheme() {
    var current = document.documentElement.getAttribute('data-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('portfolio-theme', next);
    updateIcons(next);
  }

  document.addEventListener('DOMContentLoaded', function () {
    updateIcons(saved);
    document.querySelectorAll('.theme-toggle').forEach(function(btn) {
      btn.addEventListener('click', toggleTheme);
    });

    /* Navbar scroll */
    var nav = document.getElementById('mainNav');
    if (nav) {
      window.addEventListener('scroll', function() {
        nav.classList.toggle('scrolled', window.scrollY > 40);
      }, { passive: true });
    }

    /* Close mobile menu on link click */
    document.querySelectorAll('#navbarNav .nav-link, #navbarNav .nav-cta').forEach(function(link) {
      link.addEventListener('click', function() {
        var collapse = document.getElementById('navbarNav');
        if (collapse && collapse.classList.contains('show')) {
          var bsCollapse = bootstrap.Collapse.getInstance(collapse);
          if (bsCollapse) bsCollapse.hide();
        }
      });
    });

    /* Skill bars */
    var homeBars = document.querySelectorAll('.skill-pill .skill-bar-fill');
    if (homeBars.length) {
      var stored = {};
      homeBars.forEach(function(b) { stored[b] = b.style.width; b.style.width = '0'; });
      var barObs = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (e.isIntersecting) { e.target.style.width = stored[e.target] || '75%'; barObs.unobserve(e.target); }
        });
      }, { threshold: 0.2 });
      homeBars.forEach(function(b) { barObs.observe(b); });
    }

    /* AOS */
    var fadeEls = document.querySelectorAll('[data-aos]');
    if (fadeEls.length) {
      var fadeObs = new IntersectionObserver(function(entries) {
        entries.forEach(function(e) {
          if (e.isIntersecting) { e.target.classList.add('aos-visible'); fadeObs.unobserve(e.target); }
        });
      }, { threshold: 0.1 });
      fadeEls.forEach(function(el) { el.classList.add('aos-init'); fadeObs.observe(el); });
    }
  });
})();