/* ===========================
   PINUS PACK INDO — Main JS
   =========================== */

let currentLang = localStorage.getItem('lang') || 'id';
let translations = {};

// ── Load language data ───────────────────
async function loadLang(lang) {
  const base = location.pathname.endsWith('/') || location.pathname.includes('index') ? '' : '../';
  const res = await fetch(`${base}lang/${lang}.json`);
  return res.json();
}

async function initLang() {
  translations = await loadLang(currentLang);
  applyTranslations();
  updateLangButtons();
}

function applyTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const val = getNestedVal(translations, key);
    if (val !== undefined) el.textContent = val;
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    const val = getNestedVal(translations, key);
    if (val !== undefined) el.placeholder = val;
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    const key = el.getAttribute('data-i18n-html');
    const val = getNestedVal(translations, key);
    if (Array.isArray(val)) {
      el.innerHTML = val.map(item => `<li>${item}</li>`).join('');
    }
  });
}

function getNestedVal(obj, path) {
  return path.split('.').reduce((acc, k) => (acc && acc[k] !== undefined ? acc[k] : undefined), obj);
}

function updateLangButtons() {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === currentLang);
  });
}

async function switchLang(lang) {
  if (lang === currentLang) return;
  currentLang = lang;
  localStorage.setItem('lang', lang);
  translations = await loadLang(lang);
  applyTranslations();
  updateLangButtons();
}

// ── Navbar ───────────────────────────────
function initNavbar() {
  const navEl      = document.querySelector('nav');
  const hamburger  = document.querySelector('.hamburger');
  const mobileNav  = document.getElementById('mobileNav');
  const mobileClose = document.getElementById('mobileClose');

  window.addEventListener('scroll', () => {
    navEl?.classList.toggle('scrolled', window.scrollY > 20);
    document.getElementById('scrollTop')?.classList.toggle('visible', window.scrollY > 300);
  });

  hamburger?.addEventListener('click', () => {
    mobileNav?.classList.toggle('open');
  });

  mobileClose?.addEventListener('click', () => {
    mobileNav?.classList.remove('open');
  });

  document.addEventListener('click', e => {
    if (!navEl?.contains(e.target) && !mobileNav?.contains(e.target)) {
      mobileNav?.classList.remove('open');
    }
  });

  // Active link
  const currentPage = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-nav a').forEach(a => {
    const href = a.getAttribute('href');
    a.classList.remove('active');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });
}

// ── Language buttons ─────────────────────
function initLangButtons() {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => switchLang(btn.dataset.lang));
  });
}

// ── Product filter (products page) ───────
function initFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.product-card');
  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const cat = btn.dataset.filter;
      cards.forEach(card => {
        const show = cat === 'all' || card.dataset.category === cat;
        card.style.display = show ? '' : 'none';
      });
    });
  });
}

// ── Contact form ──────────────────────────
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', e => {
    e.preventDefault();
    const name    = form.querySelector('[name="name"]').value.trim();
    const phone   = form.querySelector('[name="phone"]').value.trim();
    const message = form.querySelector('[name="message"]').value.trim();

    // Redirect to WhatsApp with pre-filled message
    const WA_NUMBER = '6285283338989'; // TODO: ganti dengan nomor WA bisnis
    const text = encodeURIComponent(`Halo Pinus Pack Indo,\n\nNama: ${name}\nPesan: ${message}`);
    window.open(`https://wa.me/${WA_NUMBER}?text=${text}`, '_blank');

    showToast(currentLang === 'id' ? 'Pesan dikirim via WhatsApp!' : 'Message sent via WhatsApp!');
    form.reset();
  });
}

// ── Send button di homepage (bukan form) ──
function initSendBtn() {
  const btn = document.getElementById('sendBtn');
  if (!btn) return;
  btn.addEventListener('click', () => {
    const inputs = btn.closest('section').querySelectorAll('input, textarea');
    const name    = inputs[0]?.value.trim() || '';
    const phone   = inputs[1]?.value.trim() || '';
    const message = inputs[3]?.value.trim() || '';
    if (!name) { inputs[0]?.focus(); return; }
    const WA_NUMBER = '6285283338989'; // TODO: ganti nomor WA bisnis
    const text = encodeURIComponent(`Halo Pinus Pack Indo,\n\nNama: ${name}\nHP: ${phone}\nPesan: ${message}`);
    window.open(`https://wa.me/${WA_NUMBER}?text=${text}`, '_blank');
  });
}

// ── Scroll to top ─────────────────────────
function initScrollTop() {
  const btn = document.getElementById('scrollTop');
  btn?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// ── Toast notification ────────────────────
function showToast(msg) {
  let toast = document.querySelector('.toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3000);
}

// ── Init ──────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initLangButtons();
  initFilter();
  initContactForm();
  initSendBtn();
  initScrollTop();
  initLang();
});
