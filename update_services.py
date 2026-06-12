with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Replace CSS: services-grid → services-viewport/track ──
old_css = """.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; align-items: stretch; }
.service-card {
  background: transparent;
  transition: transform 0.2s;
  display: flex; flex-direction: column;
}
.service-card:hover { transform: translateY(-4px); }
.service-card-img {
  width: 100%; height: 240px; overflow: hidden;
  border-radius: 16px;
}
.service-card-img img {
  width: 100%; height: 100%;
  object-fit: cover;
}
.service-card-body { padding: 16px 4px; display: flex; flex-direction: column; flex: 1; }
.service-card-body h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
.service-card-body p { font-size: 13px; color: #666; line-height: 1.6; margin-bottom: 16px; flex: 1; }
.btn-book {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600;
  cursor: pointer; border: none; width: fit-content; align-self: flex-start;
}
/* Selang-seling: card ganjil = putih, card genap = hijau */
.service-card:nth-child(odd)  .btn-book { background: #fff;     color: #27ae60; box-shadow: 0 1px 6px rgba(0,0,0,0.08); }
.service-card:nth-child(odd)  .btn-book:hover { background: #f0f0f0; }
.service-card:nth-child(even) .btn-book { background: #27ae60; color: #fff; }
.service-card:nth-child(even) .btn-book:hover { background: #1e8449; }"""

new_css = """.services-viewport { overflow: hidden; }
.services-track {
  display: flex; gap: 24px;
  transition: transform 0.5s ease-in-out;
}
.service-card {
  flex-shrink: 0;
  width: calc((100% - 48px) / 3);
  background: #fff; border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.07);
  display: flex; flex-direction: column;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}
.service-card:hover { transform: translateY(-4px); box-shadow: 0 8px 28px rgba(0,0,0,0.12); }
.service-card-icon {
  height: 160px; display: flex; align-items: center; justify-content: center;
  position: relative; overflow: hidden;
}
.service-card-icon svg { width: 64px; height: 64px; stroke: rgba(255,255,255,0.95); fill: none; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.service-card-body { padding: 20px; display: flex; flex-direction: column; flex: 1; }
.service-card-body h3 { font-size: 16px; font-weight: 800; margin-bottom: 12px; color: #111; }
.prod-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; flex: 1; }
.prod-tag {
  font-size: 11px; color: #444; background: #f4f4f4;
  padding: 3px 9px; border-radius: 20px; font-weight: 500;
}
.btn-book {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600;
  cursor: pointer; border: none; width: fit-content; align-self: flex-start;
  transition: transform 0.18s, box-shadow 0.18s;
}
.btn-book:hover { transform: translateY(-2px); }
.service-card:nth-child(odd)  .btn-book { background: #fff; color: #27ae60; box-shadow: 0 1px 6px rgba(0,0,0,0.1); }
.service-card:nth-child(odd)  .btn-book:hover { background: #f0f0f0; }
.service-card:nth-child(even) .btn-book { background: #27ae60; color: #fff; }
.service-card:nth-child(even) .btn-book:hover { background: #1e8449; }
/* Slider nav */
.services-nav { display: flex; align-items: center; gap: 12px; margin-top: 24px; justify-content: flex-end; }
.svc-btn {
  width: 38px; height: 38px; border-radius: 50%; border: 1.5px solid #ddd;
  background: #fff; cursor: pointer; display: flex; align-items: center; justify-content: center;
  font-size: 16px; color: #27ae60; transition: all 0.2s; flex-shrink: 0;
}
.svc-btn:hover { background: #27ae60; color: #fff; border-color: #27ae60; }
.svc-btn:disabled { opacity: 0.3; cursor: default; }
.svc-counter { font-size: 13px; color: #888; font-weight: 600; }"""

html = html.replace(old_css, new_css)

# ── 2. Replace HTML: old 3 cards → new 7-card slider ──
old_html = """  <hr style="border:none;border-top:2.5px solid #d0d0d0;margin-bottom:32px;">
  <div class="services-grid">
    <div class="service-card">
      <div class="service-card-img">
        <img src="images/prod-kotak.jpg" alt="Kotak & Box Kemasan">
      </div>
      <div class="service-card-body">
        <h3 data-i18n="services.card1_title">Kotak &amp; Box Kemasan</h3>
        <p data-i18n="services.card1_desc">Berbagai pilihan kotak kemasan kraft, mika, dan karton untuk produk makanan, kue, dan souvenir Anda.</p>
        <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
      </div>
    </div>
    <div class="service-card">
      <div class="service-card-img">
        <img src="images/prod-paperbag.jpg" alt="Paper Bag & Kantong">
      </div>
      <div class="service-card-body">
        <h3 data-i18n="services.card2_title">Paper Bag &amp; Kantong</h3>
        <p data-i18n="services.card2_desc">Kantong kertas berkualitas dalam berbagai ukuran dan warna untuk mendukung branding bisnis Anda.</p>
        <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
      </div>
    </div>
    <div class="service-card">
      <div class="service-card-img">
        <img src="images/prod-baking.jpg" alt="Peralatan Baking">
      </div>
      <div class="service-card-body">
        <h3 data-i18n="services.card3_title">Peralatan Baking</h3>
        <p data-i18n="services.card3_desc">Loyang, cetakan, dan peralatan baking profesional untuk usaha kue dan bakeri Anda.</p>
        <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
      </div>
    </div>
  </div>
</section>"""

new_html = """  <hr style="border:none;border-top:2.5px solid #d0d0d0;margin-bottom:32px;">
  <div class="services-viewport">
    <div class="services-track" id="servicesTrack">

      <!-- 1. Kemasan Plastik -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#2980b9,#3498db);">
          <svg viewBox="0 0 24 24"><path d="M6 2l1.5 4h9L18 2"/><rect x="3" y="6" width="18" height="14" rx="2"/><path d="M3 10h18"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c1_title">Kemasan Plastik</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c1_t1">Gelas & Tutup</span>
            <span class="prod-tag" data-i18n="services.c1_t2">Piring Plastik</span>
            <span class="prod-tag" data-i18n="services.c1_t3">Mika</span>
            <span class="prod-tag" data-i18n="services.c1_t4">Botol</span>
            <span class="prod-tag" data-i18n="services.c1_t5">Kantong Plastik</span>
            <span class="prod-tag" data-i18n="services.c1_t6">Trashbag</span>
            <span class="prod-tag" data-i18n="services.c1_t7">Standing Pouch</span>
            <span class="prod-tag" data-i18n="services.c1_t8">Thinwall</span>
            <span class="prod-tag" data-i18n="services.c1_t9">Vacuum Bag</span>
            <span class="prod-tag" data-i18n="services.c1_t10">Toples</span>
            <span class="prod-tag" data-i18n="services.c1_t11">Sedotan</span>
            <span class="prod-tag" data-i18n="services.c1_t12">Shopping Bag</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

      <!-- 2. Kemasan Kertas -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#c0392b,#e74c3c);">
          <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c2_title">Kemasan Kertas</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c2_t1">Gelas Kertas</span>
            <span class="prod-tag" data-i18n="services.c2_t2">Box Makanan</span>
            <span class="prod-tag" data-i18n="services.c2_t3">Mangkok Kertas</span>
            <span class="prod-tag" data-i18n="services.c2_t4">Paper Bag</span>
            <span class="prod-tag" data-i18n="services.c2_t5">Kemasan Nasi</span>
            <span class="prod-tag" data-i18n="services.c2_t6">Kemasan Snack</span>
            <span class="prod-tag" data-i18n="services.c2_t7">Kemasan Kue</span>
            <span class="prod-tag" data-i18n="services.c2_t8">Kertas Roti</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

      <!-- 3. Kemasan Styrofoam -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#7f8c8d,#95a5a6);">
          <svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/><line x1="12" y1="12" x2="12" y2="16"/><line x1="10" y1="14" x2="14" y2="14"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c3_title">Kemasan Styrofoam</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c3_t1">Box Styrofoam</span>
            <span class="prod-tag" data-i18n="services.c3_t2">Piring Foam</span>
            <span class="prod-tag" data-i18n="services.c3_t3">Mangkok Foam</span>
            <span class="prod-tag" data-i18n="services.c3_t4">Ice Box</span>
            <span class="prod-tag" data-i18n="services.c3_t5">Tray Buah</span>
            <span class="prod-tag" data-i18n="services.c3_t6">Kemasan Daging</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

      <!-- 4. Peralatan Baking -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#d35400,#e67e22);">
          <svg viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 010 8h-1"/><path d="M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c4_title">Peralatan Baking</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c4_t1">Pengocok Telur</span>
            <span class="prod-tag" data-i18n="services.c4_t2">Timbangan</span>
            <span class="prod-tag" data-i18n="services.c4_t3">Cetakan Kue</span>
            <span class="prod-tag" data-i18n="services.c4_t4">Spuit</span>
            <span class="prod-tag" data-i18n="services.c4_t5">Alas Adonan</span>
            <span class="prod-tag" data-i18n="services.c4_t6">Botol Saus</span>
            <span class="prod-tag" data-i18n="services.c4_t7">Loyang</span>
            <span class="prod-tag" data-i18n="services.c4_t8">Mixer</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

      <!-- 5. Bahan Baking -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#b7950b,#f1c40f);">
          <svg viewBox="0 0 24 24"><path d="M3 11l19-9-9 19-2-8-8-2z"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c5_title">Bahan Baking</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c5_t1">Tepung</span>
            <span class="prod-tag" data-i18n="services.c5_t2">Gula</span>
            <span class="prod-tag" data-i18n="services.c5_t3">Susu</span>
            <span class="prod-tag" data-i18n="services.c5_t4">Obat Kue</span>
            <span class="prod-tag" data-i18n="services.c5_t5">Coklat</span>
            <span class="prod-tag" data-i18n="services.c5_t6">Topping</span>
            <span class="prod-tag" data-i18n="services.c5_t7">Pewarna</span>
            <span class="prod-tag" data-i18n="services.c5_t8">Essens</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

      <!-- 6. Makanan & Minuman -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#8e44ad,#9b59b6);">
          <svg viewBox="0 0 24 24"><path d="M18 8h1a4 4 0 010 8h-1"/><path d="M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c6_title">Makanan &amp; Minuman</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c6_t1">Snack</span>
            <span class="prod-tag" data-i18n="services.c6_t2">Minuman Kemasan</span>
            <span class="prod-tag" data-i18n="services.c6_t3">Makanan Ringan</span>
            <span class="prod-tag" data-i18n="services.c6_t4">Kue & Roti</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

      <!-- 7. Lain-Lain -->
      <div class="service-card">
        <div class="service-card-icon" style="background:linear-gradient(135deg,#1e8449,#27ae60);">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
        </div>
        <div class="service-card-body">
          <h3 data-i18n="services.c7_title">Lain-Lain</h3>
          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c7_t1">Isolasi</span>
            <span class="prod-tag" data-i18n="services.c7_t2">Staples</span>
            <span class="prod-tag" data-i18n="services.c7_t3">Spunbond</span>
            <span class="prod-tag" data-i18n="services.c7_t4">Alat Kayu</span>
            <span class="prod-tag" data-i18n="services.c7_t5">Tusuk Sate</span>
            <span class="prod-tag" data-i18n="services.c7_t6">Tissue</span>
            <span class="prod-tag" data-i18n="services.c7_t7">Bubble Wrap</span>
          </div>
          <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>
        </div>
      </div>

    </div>
  </div>
  <!-- Slider Navigation -->
  <div class="services-nav">
    <span class="svc-counter"><span id="svcCurrent">1</span> / 5</span>
    <button class="svc-btn" id="svcPrev" onclick="slideServices(-1)" disabled>←</button>
    <button class="svc-btn" id="svcNext" onclick="slideServices(1)">→</button>
  </div>
</section>"""

html = html.replace(old_html, new_html)

# ── 3. Add slideServices JS ──
old_js = "  document.getElementById('year').textContent = new Date().getFullYear();"
new_js = """  document.getElementById('year').textContent = new Date().getFullYear();

  // Services slider (show 3, total 7, max shift = 4)
  let svcIndex = 0;
  const svcMax = 4;
  function slideServices(dir) {
    svcIndex = Math.max(0, Math.min(svcMax, svcIndex + dir));
    const card = document.querySelector('.service-card');
    const gap = 24;
    const cardW = card.offsetWidth + gap;
    document.getElementById('servicesTrack').style.transform = 'translateX(-' + (svcIndex * cardW) + 'px)';
    document.getElementById('svcCurrent').textContent = svcIndex + 1;
    document.getElementById('svcPrev').disabled = svcIndex === 0;
    document.getElementById('svcNext').disabled = svcIndex === svcMax;
  }"""

html = html.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated")
print("services-viewport found:", 'services-viewport' in html)
print("7 service cards:", html.count('service-card-icon'))
print("slideServices JS:", 'slideServices' in html)
