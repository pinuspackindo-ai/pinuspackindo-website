import re, json

# ── 1. UPDATE NAV on all existing pages ──────────────────────────────────────
pages = ['index.html','about.html','products.html','contact.html']

old_nav = '    <a href="products.html" data-i18n="nav.products">Produk</a>\n    <a href="contact.html" data-i18n="nav.contact">Kontak</a>'
new_nav = '    <a href="products.html" data-i18n="nav.products">Produk</a>\n    <a href="artikel.html" data-i18n="nav.artikel">Artikel</a>\n    <a href="berita.html" data-i18n="nav.berita">Berita &amp; Acara</a>\n    <a href="contact.html" data-i18n="nav.contact">Kontak</a>'

old_foot = '        <li><a href="contact.html" data-i18n="nav.contact">Kontak</a></li>'
new_foot = '        <li><a href="artikel.html" data-i18n="nav.artikel">Artikel</a></li>\n        <li><a href="berita.html" data-i18n="nav.berita">Berita &amp; Acara</a></li>\n        <li><a href="contact.html" data-i18n="nav.contact">Kontak</a></li>'

for fname in pages:
    with open(fname,'r',encoding='utf-8') as f: h=f.read()
    h=h.replace(old_nav, new_nav)
    h=h.replace(old_foot, new_foot)
    with open(fname,'w',encoding='utf-8') as f: f.write(h)
    print(f'{fname} nav updated')

# ── 2. ADD i18n KEYS ─────────────────────────────────────────────────────────
for fname, vals in [
    ('lang/id.json', {'artikel':'Artikel','berita':'Berita & Acara'}),
    ('lang/en.json', {'artikel':'Articles','berita':'News & Events'}),
]:
    with open(fname,'r',encoding='utf-8') as f: d=json.load(f)
    d['nav']['artikel'] = vals['artikel']
    d['nav']['berita']  = vals['berita']
    with open(fname,'w',encoding='utf-8') as f: json.dump(d,f,ensure_ascii=False,indent=2)
    print(f'{fname} updated')

# ── 3. SHARED PARTS ───────────────────────────────────────────────────────────
nav_partial = lambda active: f'''<!-- NAV -->
<nav>
  <a class="logo" href="index.html">
    <div class="logo-icon"><img src="images/logo.jpg" alt="Pinus Packindo Logo"></div>
    <div>
      <div class="logo-name">Pinus Packindo</div>
      <div class="logo-sub">Packaging &amp; Baking Supply</div>
    </div>
  </a>
  <div class="nav-links">
    <a href="index.html" data-i18n="nav.home">Beranda</a>
    <a href="about.html" data-i18n="nav.about">Tentang Kami</a>
    <a href="products.html" data-i18n="nav.products">Produk</a>
    <a href="artikel.html" {'class="active"' if active=='artikel' else ''} data-i18n="nav.artikel">Artikel</a>
    <a href="berita.html" {'class="active"' if active=='berita' else ''} data-i18n="nav.berita">Berita &amp; Acara</a>
    <a href="contact.html" data-i18n="nav.contact">Kontak</a>
  </div>
  <div class="nav-right">
    <div class="lang-switcher">
      <button class="lang-btn active" onclick="switchLang('id')">ID</button>
      <button class="lang-btn" onclick="switchLang('en')">EN</button>
    </div>
    <button class="btn-quote" onclick="location.href=\'contact.html\'" data-i18n="nav.cta">Hubungi Kami</button>
  </div>
</nav>'''

breadcrumb = lambda label, label_en, href, page_name, page_name_en: f'''<!-- BREADCRUMB -->
<div class="breadcrumb">
  <a href="index.html" data-i18n="nav.home">Beranda</a>
  <span>›</span>
  <strong data-i18n="{href}">{label}</strong>
</div>'''

social_strip = '''<!-- SOCIAL MEDIA STRIP -->
<div style="display:flex;gap:12px;justify-content:center;align-items:center;padding:40px 0 48px;background:#fff;">
  <a href="https://www.instagram.com/pinuspackindo?igsh=MXQ1OWNoMzlkaTg5aw==" target="_blank" aria-label="Instagram"
     style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;"
     onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'"
     onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'">
    <svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
  </a>
  <a href="https://www.tiktok.com/@pinus.packindo?_r=1&amp;_t=ZS-978Su6GNPwT" target="_blank" aria-label="TikTok"
     style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;"
     onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'"
     onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'">
    <svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.17 8.17 0 004.78 1.52V6.75a4.85 4.85 0 01-1.01-.06z"/></svg>
  </a>
  <a href="https://www.facebook.com/pinuspackindo?mibextid=rS40aB7S9Ucbxw6v" target="_blank" aria-label="Facebook"
     style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;"
     onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'"
     onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'">
    <svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
  </a>
  <a href="https://www.linkedin.com/company/cv-pinus-packindo/" target="_blank" aria-label="LinkedIn"
     style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;"
     onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'"
     onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'">
    <svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
  </a>
</div>'''

footer_html = '''<!-- FOOTER -->
<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="footer-logo">
        <div class="logo-icon"><img src="images/logo.jpg" alt="Pinus Packindo Logo"></div>
        <div>
          <div style="font-weight:800;font-size:16px;color:#fff;">Pinus Packindo</div>
          <div style="font-size:10px;color:#666;letter-spacing:0.5px;">Packaging &amp; Baking Supply</div>
        </div>
      </div>
      <p data-i18n="footer.desc">Solusi kemasan dan baking supply berkualitas tinggi untuk bisnis Anda di seluruh Indonesia.</p>
    </div>
    <div class="footer-col">
      <h4 data-i18n="footer.menu">Menu</h4>
      <ul>
        <li><a href="index.html" data-i18n="nav.home">Beranda</a></li>
        <li><a href="about.html" data-i18n="nav.about">Tentang Kami</a></li>
        <li><a href="products.html" data-i18n="nav.products">Produk</a></li>
        <li><a href="artikel.html" data-i18n="nav.artikel">Artikel</a></li>
        <li><a href="berita.html" data-i18n="nav.berita">Berita &amp; Acara</a></li>
        <li><a href="contact.html" data-i18n="nav.contact">Kontak</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4 data-i18n="footer.products_col">Produk</h4>
      <ul>
        <li><a href="products.html#kemasan-plastik" data-i18n="services.c1_title">Kemasan Plastik</a></li>
        <li><a href="products.html#kemasan-kertas" data-i18n="services.c2_title">Kemasan Kertas</a></li>
        <li><a href="products.html#kemasan-styrofoam" data-i18n="services.c3_title">Kemasan Styrofoam</a></li>
        <li><a href="products.html#peralatan-baking" data-i18n="services.c4_title">Peralatan Baking</a></li>
        <li><a href="products.html#bahan-baking" data-i18n="services.c5_title">Bahan Baking</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4 data-i18n="footer.newsletter">Newsletter</h4>
      <p style="font-size:13px;color:#777;margin-bottom:8px;" data-i18n="footer.newsletter_desc">Dapatkan info produk terbaru dan penawaran spesial.</p>
      <div class="newsletter-input-wrap">
        <input class="newsletter-input" type="email" placeholder="Email Anda" data-i18n-placeholder="footer.newsletter_ph">
        <button class="btn-send-sm" data-i18n="footer.newsletter_btn">Daftar</button>
      </div>
    </div>
  </div>
  <div class="footer-bottom">&copy; <span id="year"></span> Pinus Packindo. Hak Cipta Dilindungi.</div>
</footer>'''

common_css = '''* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; color: #222; }
a { text-decoration: none; color: inherit; }
nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 16px 80px; background: #fff;
  position: sticky; top: 0; z-index: 100;
  box-shadow: 0 1px 8px rgba(0,0,0,0.07);
}
.logo { display: flex; align-items: center; gap: 10px; cursor: pointer; }
.logo-icon { width: 64px; height: 64px; border-radius: 10px; overflow: hidden; flex-shrink: 0; }
.logo-icon img { width: 100%; height: 100%; object-fit: cover; }
.logo-name { font-weight: 800; font-size: 22px; color: #27ae60; line-height: 1.15; }
.logo-sub  { font-size: 11px; color: #999; letter-spacing: 0.5px; }
.nav-links { display: flex; gap: 24px; font-size: 14px; font-weight: 500; color: #444; }
.nav-links a { transition: color 0.18s, transform 0.18s; display: inline-block; }
.nav-links a:hover { color: #27ae60; transform: translateY(-2px); }
.nav-links a.active { color: #27ae60; font-weight: 700; }
.nav-right { display: flex; align-items: center; gap: 12px; }
.lang-switcher { display: flex; gap: 4px; }
.lang-btn { padding: 5px 10px; border-radius: 5px; border: 1.5px solid #ddd; background: #fff; font-size: 12px; font-weight: 600; cursor: pointer; color: #666; transition: all 0.2s; }
.lang-btn.active, .lang-btn:hover { background: #27ae60; color: #fff; border-color: #27ae60; }
.btn-quote { background: #27ae60; color: #fff; padding: 10px 22px; border-radius: 6px; font-size: 14px; font-weight: 600; border: none; cursor: pointer; transition: transform 0.18s, box-shadow 0.18s, background 0.18s; }
.btn-quote:hover { background: #1e8449; transform: translateY(-3px) scale(1.04); box-shadow: 0 6px 20px rgba(39,174,96,0.35); }
.breadcrumb { background: #f8f8f8; padding: 12px 80px; border-bottom: 1px solid #eee; }
.breadcrumb a { font-size: 13px; color: #27ae60; }
.breadcrumb span { font-size: 13px; color: #999; margin: 0 6px; }
.breadcrumb strong { font-size: 13px; color: #444; }
.page-hero { padding: 72px 80px; position: relative; overflow: hidden; background-size: cover; background-position: center; }
.page-hero-inner { position: relative; z-index: 1; max-width: 640px; }
.page-hero-tag { font-size: 12px; color: rgba(255,255,255,0.6); text-transform: uppercase; letter-spacing: 2px; margin-bottom: 14px; }
.page-hero h1 { font-size: 44px; font-weight: 800; color: #fff; line-height: 1.15; margin-bottom: 16px; }
.page-hero p { font-size: 15px; color: rgba(255,255,255,0.75); line-height: 1.7; max-width: 500px; }
/* Article grid */
.articles-section { padding: 72px 80px; background: #fff; }
.articles-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; margin-top: 40px; }
.article-card {
  background: #fff; border-radius: 16px; overflow: hidden;
  box-shadow: 0 2px 16px rgba(0,0,0,0.07);
  transition: transform 0.22s, box-shadow 0.22s;
  display: flex; flex-direction: column;
  border: 1px solid #f0f0f0;
}
.article-card:hover { transform: translateY(-6px); box-shadow: 0 12px 32px rgba(0,0,0,0.13); }
.article-img { width: 100%; height: 200px; overflow: hidden; background: linear-gradient(135deg,#e8f5e9,#c8e6c9); position: relative; }
.article-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s; }
.article-card:hover .article-img img { transform: scale(1.06); }
.article-img-placeholder { width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; }
.article-img-placeholder svg { width: 48px; height: 48px; fill: #27ae60; opacity: 0.4; }
.article-meta { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; flex-wrap: wrap; }
.article-cat { font-size: 10px; font-weight: 700; color: #27ae60; background: #e8f5e9; border-radius: 20px; padding: 3px 10px; text-transform: uppercase; letter-spacing: 0.5px; }
.article-date { font-size: 11px; color: #aaa; }
.article-body { padding: 20px 22px 24px; flex: 1; display: flex; flex-direction: column; }
.article-body h3 { font-size: 16px; font-weight: 800; color: #111; line-height: 1.45; margin-bottom: 10px; }
.article-body p { font-size: 13px; color: #666; line-height: 1.7; flex: 1; margin-bottom: 18px; }
.article-footer { display: flex; align-items: center; justify-content: space-between; padding-top: 14px; border-top: 1px solid #f0f0f0; margin-top: auto; }
.article-author { display: flex; align-items: center; gap: 8px; }
.author-avatar { width: 28px; height: 28px; border-radius: 50%; background: #27ae60; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: #fff; flex-shrink: 0; }
.author-name { font-size: 12px; font-weight: 600; color: #444; }
.btn-read { font-size: 12px; font-weight: 700; color: #27ae60; background: none; border: 1.5px solid #27ae60; border-radius: 20px; padding: 5px 14px; cursor: pointer; transition: all 0.2s; }
.btn-read:hover { background: #27ae60; color: #fff; }
/* Footer */
footer { background: #111; color: #aaa; padding: 56px 80px 24px; }
.footer-grid { display: grid; grid-template-columns: 2fr 1fr 1fr 1.5fr; gap: 48px; margin-bottom: 40px; }
.footer-brand p { font-size: 13px; color: #666; line-height: 1.7; margin-top: 14px; max-width: 260px; }
.footer-logo { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.footer-col h4 { font-size: 13px; font-weight: 700; color: #fff; margin-bottom: 14px; }
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 8px; }
.footer-col ul li a { font-size: 13px; color: #666; transition: color 0.2s; }
.footer-col ul li a:hover { color: #27ae60; }
.newsletter-input-wrap { display: flex; gap: 8px; margin-top: 8px; }
.newsletter-input { flex: 1; padding: 9px 12px; border-radius: 6px; border: 1px solid #333; background: #1a1a1a; color: #ccc; font-size: 13px; outline: none; }
.btn-send-sm { background: #27ae60; color: #fff; border: none; padding: 9px 14px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer; }
.footer-bottom { border-top: 1px solid #222; padding-top: 20px; font-size: 12px; color: #555; text-align: center; }'''

common_js = '''<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  const translations = {};
  async function loadLang(lang) {
    if (!translations[lang]) {
      const r = await fetch('lang/' + lang + '.json');
      translations[lang] = await r.json();
    }
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const keys = el.getAttribute('data-i18n').split('.');
      let val = translations[lang];
      for (const k of keys) val = val?.[k];
      if (val) el.textContent = val;
    });
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const keys = el.getAttribute('data-i18n-placeholder').split('.');
      let val = translations[lang];
      for (const k of keys) val = val?.[k];
      if (val) el.placeholder = val;
    });
    localStorage.setItem('lang', lang);
    document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
    const btn = document.querySelector(`.lang-btn[onclick*="'${lang}'"]`);
    if (btn) btn.classList.add('active');
  }
  function switchLang(lang) { loadLang(lang); }
  loadLang(localStorage.getItem('lang') || 'id');
</script>'''

# ── 4. ARTIKEL.HTML ───────────────────────────────────────────────────────────
artikel_articles = [
    {'date':'12 Juni 2026','cat':'Tips Kemasan','catkey':'artikel.cat1','author':'Tim Pinus','title':'5 Tips Memilih Kemasan yang Tepat untuk Produk Makanan Anda','titlekey':'artikel.a1_title','desc':'Kemasan yang tepat bukan hanya melindungi produk, tapi juga menjadi media promosi bisnis Anda. Berikut 5 tips memilih kemasan makanan yang efektif...','desckey':'artikel.a1_desc','src':'Pinus Packindo','slug':'artikel-1.html'},
    {'date':'5 Juni 2026','cat':'Edukasi','catkey':'artikel.cat2','author':'Tim Pinus','title':'Perbedaan Kemasan Plastik Food Grade dan Non-Food Grade yang Wajib Diketahui','titlekey':'artikel.a2_title','desc':'Tidak semua plastik aman untuk makanan. Ketahui perbedaan antara kemasan food grade dan non-food grade sebelum memilih kemasan untuk produk Anda...','desckey':'artikel.a2_desc','src':'Pinus Packindo','slug':'artikel-2.html'},
    {'date':'28 Mei 2026','cat':'Tren','catkey':'artikel.cat3','author':'Tim Pinus','title':'Tren Kemasan Ramah Lingkungan 2026 yang Wajib Diikuti Pelaku UMKM','titlekey':'artikel.a3_title','desc':'Konsumen semakin peduli lingkungan. Simak tren kemasan eco-friendly yang sedang naik daun dan bagaimana UMKM bisa beradaptasi...','desckey':'artikel.a3_desc','src':'Pinus Packindo','slug':'artikel-3.html'},
    {'date':'15 Mei 2026','cat':'Panduan','catkey':'artikel.cat4','author':'Tim Pinus','title':'Panduan Lengkap Memilih Box Kue untuk Usaha Bakery Rumahan','titlekey':'artikel.a4_title','desc':'Bagi pelaku usaha bakery, kemasan kue adalah investasi penting. Panduan ini membantu Anda memilih box kue yang sesuai budget dan kebutuhan...','desckey':'artikel.a4_desc','src':'Pinus Packindo','slug':'artikel-4.html'},
    {'date':'2 Mei 2026','cat':'Tips Kemasan','catkey':'artikel.cat1','author':'Tim Pinus','title':'Cara Menghitung Kebutuhan Kemasan untuk Bisnis F&B Anda','titlekey':'artikel.a5_title','desc':'Salah menghitung stok kemasan bisa merugikan bisnis. Pelajari cara menghitung kebutuhan kemasan yang tepat agar tidak kekurangan atau kelebihan stok...','desckey':'artikel.a5_desc','src':'Pinus Packindo','slug':'artikel-5.html'},
    {'date':'20 April 2026','cat':'Edukasi','catkey':'artikel.cat2','author':'Tim Pinus','title':'Mengenal Jenis-jenis Kertas Roti dan Fungsinya dalam Dunia Baking','titlekey':'artikel.a6_title','desc':'Kertas roti bukan sekadar alas loyang. Kenali berbagai jenis kertas roti — parchment, greaseproof, silicone — dan kapan menggunakannya...','desckey':'artikel.a6_desc','src':'Pinus Packindo','slug':'artikel-6.html'},
]

def article_card(a):
    return f'''    <div class="article-card">
      <div class="article-img">
        <div class="article-img-placeholder">
          <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
        </div>
      </div>
      <div class="article-body">
        <div class="article-meta">
          <span class="article-cat" data-i18n="{a['catkey']}">{a['cat']}</span>
          <span class="article-date">{a['date']}</span>
        </div>
        <h3 data-i18n="{a['titlekey']}">{a['title']}</h3>
        <p data-i18n="{a['desckey']}">{a['desc']}</p>
        <div class="article-footer">
          <div class="article-author">
            <div class="author-avatar">PP</div>
            <div>
              <div class="author-name">{a['author']}</div>
              <div style="font-size:10px;color:#aaa;">{a['src']}</div>
            </div>
          </div>
          <button class="btn-read" onclick="location.href='{a['slug']}'" data-i18n="artikel.btn_read">Baca Selengkapnya</button>
        </div>
      </div>
    </div>'''

artikel_cards = '\n'.join(article_card(a) for a in artikel_articles)

artikel_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Artikel - Pinus Packindo</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{common_css}
.page-hero {{
  background: linear-gradient(135deg, rgba(13,34,24,0.85) 0%, rgba(26,74,46,0.78) 55%, rgba(39,174,96,0.65) 100%),
              url('images/about-hero.png') center center / cover no-repeat;
}}
</style>
</head>
<body>

{nav_partial('artikel')}

<!-- BREADCRUMB -->
<div class="breadcrumb">
  <a href="index.html" data-i18n="nav.home">Beranda</a>
  <span>›</span>
  <strong data-i18n="nav.artikel">Artikel</strong>
</div>

<!-- HERO -->
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-tag" data-i18n="artikel.tag">Konten &amp; Edukasi</div>
    <h1 data-i18n="artikel.h1">Artikel</h1>
    <p data-i18n="artikel.desc">Temukan artikel informatif seputar kemasan, baking supply, dan tips bisnis dari tim Pinus Packindo.</p>
  </div>
</div>

<!-- ARTICLES -->
<section class="articles-section">
  <div class="section-label" data-i18n="artikel.section_label">Artikel Terbaru</div>
  <div class="section-title" style="font-size:28px;font-weight:800;" data-i18n="artikel.section_title">Semua Artikel</div>
  <div class="articles-grid">
{artikel_cards}
  </div>
</section>

{social_strip}

{footer_html}

{common_js}
</body>
</html>'''

with open('artikel.html','w',encoding='utf-8') as f: f.write(artikel_html)
print('artikel.html created')

# ── 5. BERITA.HTML ────────────────────────────────────────────────────────────
berita_items = [
    {'date':'12 Juni 2026','cat':'Acara','catkey':'berita.cat1','author':'Tim Pinus','title':'Pinus Packindo Hadir di Pameran UMKM Pati 2026','titlekey':'berita.b1_title','desc':'Pinus Packindo turut berpartisipasi dalam Pameran UMKM Kabupaten Pati 2026 yang diselenggarakan di Alun-alun Pati. Kunjungi stand kami dan dapatkan penawaran spesial...','desckey':'berita.b1_desc','src':'Pinus Packindo','slug':'berita-1.html'},
    {'date':'1 Juni 2026','cat':'Berita','catkey':'berita.cat2','author':'Tim Pinus','title':'Pinus Packindo Resmi Buka Toko di Jalan Penjawi No. 11 Pati','titlekey':'berita.b2_title','desc':'Dengan bangga kami umumkan pembukaan resmi toko Pinus Packindo di lokasi baru yang lebih strategis. Nikmati pengalaman belanja kemasan yang lebih nyaman...','desckey':'berita.b2_desc','src':'Pinus Packindo','slug':'berita-2.html'},
    {'date':'20 Mei 2026','cat':'Promo','catkey':'berita.cat3','author':'Tim Pinus','title':'Promo Kemasan Spesial Lebaran: Diskon hingga 20% untuk Semua Kemasan Kue','titlekey':'berita.b3_title','desc':'Sambut momen spesial dengan kemasan berkualitas. Dapatkan diskon spesial untuk kemasan kue, mika, dan paper bag selama periode promo Lebaran...','desckey':'berita.b3_desc','src':'Pinus Packindo','slug':'berita-3.html'},
    {'date':'10 Mei 2026','cat':'Acara','catkey':'berita.cat1','author':'Tim Pinus','title':'Workshop Kemasan untuk UMKM F&B: Bersama Pinus Packindo','titlekey':'berita.b4_title','desc':'Pinus Packindo menyelenggarakan workshop gratis tentang strategi pemilihan kemasan untuk pelaku UMKM food & beverage di Pati dan sekitarnya...','desckey':'berita.b4_desc','src':'Pinus Packindo','slug':'berita-4.html'},
    {'date':'1 April 2026','cat':'Berita','catkey':'berita.cat2','author':'Tim Pinus','title':'Pinus Packindo Kini Hadir di Shopee dan TikTok Shop','titlekey':'berita.b5_title','desc':'Kabar baik! Kini Anda bisa berbelanja produk Pinus Packindo secara online melalui Shopee dan TikTok Shop. Belanja lebih mudah, pengiriman ke seluruh Indonesia...','desckey':'berita.b5_desc','src':'Pinus Packindo','slug':'berita-5.html'},
    {'date':'15 Maret 2026','cat':'Promo','catkey':'berita.cat3','author':'Tim Pinus','title':'Peluncuran Produk Baru: Kemasan Kraft Ramah Lingkungan','titlekey':'berita.b6_title','desc':'Pinus Packindo meluncurkan lini terbaru kemasan kraft biodegradable. Produk ramah lingkungan ini tersedia untuk box makanan, paper bag, dan mangkok kertas...','desckey':'berita.b6_desc','src':'Pinus Packindo','slug':'berita-6.html'},
]

berita_cards = '\n'.join(article_card(a) for a in berita_items)

berita_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Berita & Acara - Pinus Packindo</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{common_css}
.page-hero {{
  background: linear-gradient(135deg, rgba(13,34,24,0.85) 0%, rgba(26,74,46,0.78) 55%, rgba(39,174,96,0.65) 100%),
              url('images/products-hero.png') center center / cover no-repeat;
}}
</style>
</head>
<body>

{nav_partial('berita')}

<!-- BREADCRUMB -->
<div class="breadcrumb">
  <a href="index.html" data-i18n="nav.home">Beranda</a>
  <span>›</span>
  <strong data-i18n="nav.berita">Berita &amp; Acara</strong>
</div>

<!-- HERO -->
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-tag" data-i18n="berita.tag">Update &amp; Kegiatan</div>
    <h1 data-i18n="berita.h1">Berita &amp; Acara</h1>
    <p data-i18n="berita.desc">Ikuti perkembangan terbaru Pinus Packindo — mulai dari promo, peluncuran produk, hingga kegiatan dan event kami.</p>
  </div>
</div>

<!-- BERITA -->
<section class="articles-section">
  <div class="section-label" data-i18n="berita.section_label">Terbaru</div>
  <div class="section-title" style="font-size:28px;font-weight:800;" data-i18n="berita.section_title">Semua Berita &amp; Acara</div>
  <div class="articles-grid">
{berita_cards}
  </div>
</section>

{social_strip}

{footer_html}

{common_js}
</body>
</html>'''

with open('berita.html','w',encoding='utf-8') as f: f.write(berita_html)
print('berita.html created')

# ── 6. ADD i18n for article/berita content ────────────────────────────────────
for fname, vals in [('lang/id.json',{
    'artikel':{
      'tag':'Konten & Edukasi','h1':'Artikel','desc':'Temukan artikel informatif seputar kemasan, baking supply, dan tips bisnis dari tim Pinus Packindo.',
      'section_label':'Artikel Terbaru','section_title':'Semua Artikel','btn_read':'Baca Selengkapnya',
      'cat1':'Tips Kemasan','cat2':'Edukasi','cat3':'Tren','cat4':'Panduan',
      'a1_title':'5 Tips Memilih Kemasan yang Tepat untuk Produk Makanan Anda','a1_desc':'Kemasan yang tepat bukan hanya melindungi produk, tapi juga menjadi media promosi bisnis Anda. Berikut 5 tips memilih kemasan makanan yang efektif...',
      'a2_title':'Perbedaan Kemasan Plastik Food Grade dan Non-Food Grade yang Wajib Diketahui','a2_desc':'Tidak semua plastik aman untuk makanan. Ketahui perbedaan antara kemasan food grade dan non-food grade sebelum memilih kemasan untuk produk Anda...',
      'a3_title':'Tren Kemasan Ramah Lingkungan 2026 yang Wajib Diikuti Pelaku UMKM','a3_desc':'Konsumen semakin peduli lingkungan. Simak tren kemasan eco-friendly yang sedang naik daun dan bagaimana UMKM bisa beradaptasi...',
      'a4_title':'Panduan Lengkap Memilih Box Kue untuk Usaha Bakery Rumahan','a4_desc':'Bagi pelaku usaha bakery, kemasan kue adalah investasi penting. Panduan ini membantu Anda memilih box kue yang sesuai budget dan kebutuhan...',
      'a5_title':'Cara Menghitung Kebutuhan Kemasan untuk Bisnis F&B Anda','a5_desc':'Salah menghitung stok kemasan bisa merugikan bisnis. Pelajari cara menghitung kebutuhan kemasan yang tepat...',
      'a6_title':'Mengenal Jenis-jenis Kertas Roti dan Fungsinya dalam Dunia Baking','a6_desc':'Kertas roti bukan sekadar alas loyang. Kenali berbagai jenis kertas roti dan kapan menggunakannya...',
    },
    'berita':{
      'tag':'Update & Kegiatan','h1':'Berita & Acara','desc':'Ikuti perkembangan terbaru Pinus Packindo — mulai dari promo, peluncuran produk, hingga kegiatan dan event kami.',
      'section_label':'Terbaru','section_title':'Semua Berita & Acara',
      'cat1':'Acara','cat2':'Berita','cat3':'Promo',
      'b1_title':'Pinus Packindo Hadir di Pameran UMKM Pati 2026','b1_desc':'Pinus Packindo turut berpartisipasi dalam Pameran UMKM Kabupaten Pati 2026. Kunjungi stand kami dan dapatkan penawaran spesial...',
      'b2_title':'Pinus Packindo Resmi Buka Toko di Jalan Penjawi No. 11 Pati','b2_desc':'Dengan bangga kami umumkan pembukaan resmi toko Pinus Packindo di lokasi baru yang lebih strategis...',
      'b3_title':'Promo Kemasan Spesial Lebaran: Diskon hingga 20%','b3_desc':'Sambut momen spesial dengan kemasan berkualitas. Dapatkan diskon spesial untuk kemasan kue, mika, dan paper bag...',
      'b4_title':'Workshop Kemasan untuk UMKM F&B: Bersama Pinus Packindo','b4_desc':'Pinus Packindo menyelenggarakan workshop gratis tentang strategi pemilihan kemasan untuk pelaku UMKM...',
      'b5_title':'Pinus Packindo Kini Hadir di Shopee dan TikTok Shop','b5_desc':'Kini Anda bisa berbelanja produk Pinus Packindo secara online melalui Shopee dan TikTok Shop...',
      'b6_title':'Peluncuran Produk Baru: Kemasan Kraft Ramah Lingkungan','b6_desc':'Pinus Packindo meluncurkan lini terbaru kemasan kraft biodegradable. Tersedia untuk box makanan, paper bag, dan mangkok kertas...',
    }
  }),('lang/en.json',{
    'artikel':{
      'tag':'Content & Education','h1':'Articles','desc':'Find informative articles about packaging, baking supplies, and business tips from the Pinus Packindo team.',
      'section_label':'Latest Articles','section_title':'All Articles','btn_read':'Read More',
      'cat1':'Packaging Tips','cat2':'Education','cat3':'Trends','cat4':'Guide',
      'a1_title':'5 Tips for Choosing the Right Packaging for Your Food Products','a1_desc':'The right packaging not only protects your product but also serves as a marketing medium for your business. Here are 5 tips for choosing effective food packaging...',
      'a2_title':'Food Grade vs Non-Food Grade Plastic Packaging: What You Need to Know','a2_desc':'Not all plastics are safe for food. Learn the differences between food grade and non-food grade packaging before choosing for your products...',
      'a3_title':'Eco-Friendly Packaging Trends 2026 That SMEs Should Follow','a3_desc':'Consumers are increasingly eco-conscious. Explore the rising eco-friendly packaging trends and how SMEs can adapt...',
      'a4_title':'Complete Guide to Choosing Cake Boxes for Home Bakery Businesses','a4_desc':'For bakery businesses, cake packaging is an important investment. This guide helps you choose the right cake box for your budget and needs...',
      'a5_title':'How to Calculate Packaging Needs for Your F&B Business','a5_desc':'Miscalculating packaging stock can hurt your business. Learn how to accurately calculate your packaging needs...',
      'a6_title':'Understanding Different Types of Baking Paper and Their Uses','a6_desc':'Baking paper is more than just a pan liner. Learn about parchment, greaseproof, silicone paper and when to use each...',
    },
    'berita':{
      'tag':'Updates & Activities','h1':'News & Events','desc':'Stay up to date with the latest from Pinus Packindo — promos, product launches, events, and more.',
      'section_label':'Latest','section_title':'All News & Events',
      'cat1':'Event','cat2':'News','cat3':'Promo',
      'b1_title':'Pinus Packindo at the Pati SME Exhibition 2026','b1_desc':'Pinus Packindo participates in the Pati Regency SME Exhibition 2026. Visit our booth and get special offers...',
      'b2_title':'Pinus Packindo Officially Opens Store at Jalan Penjawi No. 11 Pati','b2_desc':'We are proud to announce the grand opening of our new Pinus Packindo store at a more strategic location...',
      'b3_title':'Special Eid Packaging Promo: Discounts up to 20%','b3_desc':'Welcome the special moment with quality packaging. Get special discounts on cake boxes, acrylic, and paper bags...',
      'b4_title':'Free Packaging Workshop for F&B SMEs with Pinus Packindo','b4_desc':'Pinus Packindo hosts a free workshop on packaging strategy for food & beverage SMEs in Pati and surrounding areas...',
      'b5_title':'Pinus Packindo Now Available on Shopee and TikTok Shop','b5_desc':'Great news! You can now shop Pinus Packindo products online via Shopee and TikTok Shop. Delivery nationwide...',
      'b6_title':'New Product Launch: Eco-Friendly Kraft Packaging','b6_desc':'Pinus Packindo launches a new line of biodegradable kraft packaging. Available for food boxes, paper bags, and bowls...',
    }
  })]:
    with open(fname,'r',encoding='utf-8') as f: d=json.load(f)
    for k,v in vals.items(): d[k]=v
    with open(fname,'w',encoding='utf-8') as f: json.dump(d,f,ensure_ascii=False,indent=2)
    print(f'{fname} content updated')

print('Done!')
