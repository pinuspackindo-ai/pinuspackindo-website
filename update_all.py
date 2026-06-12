import re, json

# ─────────────────────────────────────────────
# 1. UPDATE BOTH JSON FILES
# ─────────────────────────────────────────────

# ── id.json ──
with open('lang/id.json', 'r', encoding='utf-8') as f:
    id_data = json.load(f)

id_data['pricing'].update({
    "p1_f1": "Kotak kemasan kraft & mika",
    "p1_f2": "Paper bag berbagai ukuran",
    "p1_f3": "Baking cup & kertas roti",
    "p1_f4": "Harga satuan standar",
    "p1_f5": "Pengiriman via ekspedisi",
    "p1_f6": "Konsultasi produk gratis",
    "p2_f1": "Semua produk di Paket Starter",
    "p2_f2": "Diskon harga grosir",
    "p2_f3": "Prioritas proses pesanan",
    "p2_f4": "Pilihan cetak logo/branding",
    "p2_f5": "Account manager khusus",
    "p2_f6": "Free ongkir area tertentu",
    "p3_f1": "Semua produk di Paket Bisnis",
    "p3_f2": "Harga spesial industri",
    "p3_f3": "Custom desain & ukuran",
    "p3_f4": "Cetak logo full color",
    "p3_f5": "Dedicated account manager",
    "p3_f6": "Kontrak jangka panjang"
})

id_data['footer'].update({
    "prod1": "Kotak Kemasan",
    "prod2": "Paper Bag",
    "prod3": "Peralatan Baking",
    "prod4": "Kertas Baking",
    "prod5": "Baking Cup"
})

id_data['testi'].update({
    "q1": "Produk kemasan dari Pinus Packindo sangat memuaskan! Kualitas kotak dan paper bag jauh melebihi ekspektasi saya. Pengiriman cepat dan packaging aman sampai tujuan. Sangat direkomendasikan untuk semua pelaku usaha!",
    "n1": "Joya Pratama",
    "r1": "Pemilik Coffee Shop, Rembang",
    "q2": "Saya sudah langganan Pinus Packindo untuk kemasan toko roti saya. Kotak kemasan dan kertas rotinya selalu bersih, rapi, dan membuat produk saya makin menarik. Harga juga sangat bersahabat untuk usaha kecil seperti saya!",
    "n2": "Tasya Amelia",
    "r2": "Pemilik Toko Roti, Kudus",
    "q3": "Sebagai pemilik toko bahan kue, saya sangat puas dengan kelengkapan produk di Pinus Packindo. Stok selalu tersedia, pelayanannya ramah dan cepat tanggap, serta harga grosirnya sangat menguntungkan untuk bisnis saya.",
    "n3": "Sukardi",
    "r3": "Pemilik Toko Bahan Kue, Pati"
})
# remove old 'quote' key if present
id_data['testi'].pop('quote', None)

with open('lang/id.json', 'w', encoding='utf-8') as f:
    json.dump(id_data, f, ensure_ascii=False, indent=2)
print("id.json updated")

# ── en.json ──
with open('lang/en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

en_data['pricing'].update({
    "p1_f1": "Kraft & acrylic packaging boxes",
    "p1_f2": "Paper bags in various sizes",
    "p1_f3": "Baking cups & bread paper",
    "p1_f4": "Standard unit price",
    "p1_f5": "Delivery via courier",
    "p1_f6": "Free product consultation",
    "p2_f1": "All products in Starter Package",
    "p2_f2": "Wholesale discount prices",
    "p2_f3": "Priority order processing",
    "p2_f4": "Custom logo/branding printing",
    "p2_f5": "Dedicated account manager",
    "p2_f6": "Free shipping for certain areas",
    "p3_f1": "All products in Business Package",
    "p3_f2": "Special industry pricing",
    "p3_f3": "Custom design & sizes",
    "p3_f4": "Full color logo printing",
    "p3_f5": "Dedicated account manager",
    "p3_f6": "Long-term contract"
})

en_data['footer'].update({
    "prod1": "Packaging Boxes",
    "prod2": "Paper Bag",
    "prod3": "Baking Equipment",
    "prod4": "Baking Paper",
    "prod5": "Baking Cup"
})

en_data['testi'].update({
    "q1": "Packaging products from Pinus Packindo are very satisfying! The quality of the boxes and paper bags far exceeded my expectations. Fast delivery and packaging arrived safely. Highly recommended for all business owners!",
    "n1": "Joya Pratama",
    "r1": "Coffee Shop Owner, Rembang",
    "q2": "I have been a loyal customer of Pinus Packindo for my bakery packaging needs. The boxes and bread paper are always clean, neat, and make my products look more attractive. Prices are also very affordable for a small business like mine!",
    "n2": "Tasya Amelia",
    "r2": "Bakery Owner, Kudus",
    "q3": "As a baking supply store owner, I am very satisfied with the complete product range at Pinus Packindo. Stock is always available, service is friendly and responsive, and wholesale prices are very beneficial for my business.",
    "n3": "Sukardi",
    "r3": "Baking Supply Store Owner, Pati"
})
en_data['testi'].pop('quote', None)

with open('lang/en.json', 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)
print("en.json updated")

# ─────────────────────────────────────────────
# 2. UPDATE index.html
# ─────────────────────────────────────────────
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── Fix service card 2 btn-book (missing data-i18n) ──
html = html.replace(
    '<h3 data-i18n="services.card2_title">Paper Bag &amp; Kantong</h3>\n        <p data-i18n="services.card2_desc">Kantong kertas berkualitas dalam berbagai ukuran dan warna untuk mendukung branding bisnis Anda.</p>\n        <a href="products.html" class="btn-book">Lihat Produk ↗</a>',
    '<h3 data-i18n="services.card2_title">Paper Bag &amp; Kantong</h3>\n        <p data-i18n="services.card2_desc">Kantong kertas berkualitas dalam berbagai ukuran dan warna untuk mendukung branding bisnis Anda.</p>\n        <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>'
)

# ── Fix service card 3 btn-book (missing data-i18n) ──
html = html.replace(
    '<h3 data-i18n="services.card3_title">Peralatan Baking</h3>\n        <p data-i18n="services.card3_desc">Loyang, cetakan, dan peralatan baking profesional untuk usaha kue dan bakeri Anda.</p>\n        <a href="products.html" class="btn-book">Lihat Produk ↗</a>',
    '<h3 data-i18n="services.card3_title">Peralatan Baking</h3>\n        <p data-i18n="services.card3_desc">Loyang, cetakan, dan peralatan baking profesional untuk usaha kue dan bakeri Anda.</p>\n        <a href="products.html" class="btn-book" data-i18n="services.btn_view">Lihat Produk ↗</a>'
)

# ── Fix pricing feature lists ──
# Package 1
old_p1 = '''      <ul class="pricing-features">
        <li><span class="check-icon">✓</span> Kotak kemasan kraft &amp; mika</li>
        <li><span class="check-icon">✓</span> Paper bag berbagai ukuran</li>
        <li><span class="check-icon">✓</span> Baking cup &amp; kertas roti</li>
        <li><span class="check-icon">✓</span> Harga satuan standar</li>
        <li><span class="check-icon">✓</span> Pengiriman via ekspedisi</li>
        <li><span class="check-icon">✓</span> Konsultasi produk gratis</li>
      </ul>
      <button class="btn-pricing" onclick="location.href='contact.html'" data-i18n="pricing.btn">Pesan Sekarang</button>
    </div>
    <div class="pricing-card featured">'''
new_p1 = '''      <ul class="pricing-features">
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p1_f1">Kotak kemasan kraft &amp; mika</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p1_f2">Paper bag berbagai ukuran</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p1_f3">Baking cup &amp; kertas roti</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p1_f4">Harga satuan standar</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p1_f5">Pengiriman via ekspedisi</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p1_f6">Konsultasi produk gratis</span></li>
      </ul>
      <button class="btn-pricing" onclick="location.href='contact.html'" data-i18n="pricing.btn">Pesan Sekarang</button>
    </div>
    <div class="pricing-card featured">'''
html = html.replace(old_p1, new_p1)

# Package 2
old_p2 = '''      <ul class="pricing-features">
        <li><span class="check-icon">✓</span> Semua produk di Paket Starter</li>
        <li><span class="check-icon">✓</span> Diskon harga grosir</li>
        <li><span class="check-icon">✓</span> Prioritas proses pesanan</li>
        <li><span class="check-icon">✓</span> Pilihan cetak logo/branding</li>
        <li><span class="check-icon">✓</span> Account manager khusus</li>
        <li><span class="check-icon">✓</span> Free ongkir area tertentu</li>
      </ul>'''
new_p2 = '''      <ul class="pricing-features">
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p2_f1">Semua produk di Paket Starter</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p2_f2">Diskon harga grosir</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p2_f3">Prioritas proses pesanan</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p2_f4">Pilihan cetak logo/branding</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p2_f5">Account manager khusus</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p2_f6">Free ongkir area tertentu</span></li>
      </ul>'''
html = html.replace(old_p2, new_p2)

# Package 3
old_p3 = '''      <ul class="pricing-features">
        <li><span class="check-icon">✓</span> Semua produk di Paket Bisnis</li>
        <li><span class="check-icon">✓</span> Harga spesial industri</li>
        <li><span class="check-icon">✓</span> Custom desain &amp; ukuran</li>
        <li><span class="check-icon">✓</span> Cetak logo full color</li>
        <li><span class="check-icon">✓</span> Dedicated account manager</li>
        <li><span class="check-icon">✓</span> Kontrak jangka panjang</li>
      </ul>'''
new_p3 = '''      <ul class="pricing-features">
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p3_f1">Semua produk di Paket Bisnis</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p3_f2">Harga spesial industri</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p3_f3">Custom desain &amp; ukuran</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p3_f4">Cetak logo full color</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p3_f5">Dedicated account manager</span></li>
        <li><span class="check-icon">✓</span> <span data-i18n="pricing.p3_f6">Kontrak jangka panjang</span></li>
      </ul>'''
html = html.replace(old_p3, new_p3)

# ── Fix footer product links ──
old_footer_products = '''      <ul>
        <li><a href="products.html">Kotak Kemasan</a></li>
        <li><a href="products.html">Paper Bag</a></li>
        <li><a href="products.html">Peralatan Baking</a></li>
        <li><a href="products.html">Kertas Baking</a></li>
        <li><a href="products.html">Baking Cup</a></li>
      </ul>'''
new_footer_products = '''      <ul>
        <li><a href="products.html" data-i18n="footer.prod1">Kotak Kemasan</a></li>
        <li><a href="products.html" data-i18n="footer.prod2">Paper Bag</a></li>
        <li><a href="products.html" data-i18n="footer.prod3">Peralatan Baking</a></li>
        <li><a href="products.html" data-i18n="footer.prod4">Kertas Baking</a></li>
        <li><a href="products.html" data-i18n="footer.prod5">Baking Cup</a></li>
      </ul>'''
html = html.replace(old_footer_products, new_footer_products)

# ── Replace testimonial section (single card → 3-card slider) ──
# CSS: add testi-viewport / testi-track styles
old_testi_css = '''.testimonial-card {
  flex: 1; background: #fff; border-radius: 14px; padding: 28px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
}'''
new_testi_css = '''.testi-viewport { flex: 1; overflow: hidden; }
.testi-track { display: flex; transition: transform 0.5s ease-in-out; }
.testimonial-card {
  min-width: 100%; background: #fff; border-radius: 14px; padding: 28px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08);
}'''
html = html.replace(old_testi_css, new_testi_css)

# HTML: Replace the nav buttons and single card with 3-card slider
old_testi_html = '''      <div class="testimonial-nav">
        <button class="nav-btn">←</button>
        <button class="nav-btn">→</button>
      </div>
    </div>
    <div class="testimonial-card">
      <div class="quote-icon">"</div>
      <p class="testimonial-text" data-i18n="testi.quote">Produk kemasan dari Pinus Packindo sangat memuaskan! Kualitas kotak dan paper bag jauh melebihi ekspektasi saya. Pengiriman cepat dan packaging aman sampai tujuan. Sangat direkomendasikan untuk semua pelaku usaha!</p>
      <div class="testimonial-author">
        <div class="author-avatar"><img src="images/testi-joya.jpg" alt="Joya Pratama"></div>
        <div>
          <div class="stars" style="font-size:12px;">★★★★★</div>
          <p class="author-name">Joya Pratama</p>
          <p class="author-title">Pemilik Coffee Shop, Rembang</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

new_testi_html = '''      <div class="testimonial-nav">
        <button class="nav-btn" onclick="changeTesti(-1)">←</button>
        <button class="nav-btn" onclick="changeTesti(1)">→</button>
      </div>
    </div>
    <div class="testi-viewport">
      <div class="testi-track" id="testiTrack">
        <!-- Testimoni 1: Joya Pratama -->
        <div class="testimonial-card">
          <div class="quote-icon">"</div>
          <p class="testimonial-text" data-i18n="testi.q1">Produk kemasan dari Pinus Packindo sangat memuaskan! Kualitas kotak dan paper bag jauh melebihi ekspektasi saya. Pengiriman cepat dan packaging aman sampai tujuan. Sangat direkomendasikan untuk semua pelaku usaha!</p>
          <div class="testimonial-author">
            <div class="author-avatar"><img src="images/testi-joya.jpg" alt="Joya Pratama"></div>
            <div>
              <div class="stars" style="font-size:12px;">★★★★★</div>
              <p class="author-name" data-i18n="testi.n1">Joya Pratama</p>
              <p class="author-title" data-i18n="testi.r1">Pemilik Coffee Shop, Rembang</p>
            </div>
          </div>
        </div>
        <!-- Testimoni 2: Tasya Amelia -->
        <div class="testimonial-card">
          <div class="quote-icon">"</div>
          <p class="testimonial-text" data-i18n="testi.q2">Saya sudah langganan Pinus Packindo untuk kemasan toko roti saya. Kotak kemasan dan kertas rotinya selalu bersih, rapi, dan membuat produk saya makin menarik. Harga juga sangat bersahabat untuk usaha kecil seperti saya!</p>
          <div class="testimonial-author">
            <div class="author-avatar"><img src="images/testi-tasya.jpg" alt="Tasya Amelia"></div>
            <div>
              <div class="stars" style="font-size:12px;">★★★★★</div>
              <p class="author-name" data-i18n="testi.n2">Tasya Amelia</p>
              <p class="author-title" data-i18n="testi.r2">Pemilik Toko Roti, Kudus</p>
            </div>
          </div>
        </div>
        <!-- Testimoni 3: Sukardi (avatar laki-laki) -->
        <div class="testimonial-card">
          <div class="quote-icon">"</div>
          <p class="testimonial-text" data-i18n="testi.q3">Sebagai pemilik toko bahan kue, saya sangat puas dengan kelengkapan produk di Pinus Packindo. Stok selalu tersedia, pelayanannya ramah dan cepat tanggap, serta harga grosirnya sangat menguntungkan untuk bisnis saya.</p>
          <div class="testimonial-author">
            <div class="author-avatar" style="background:#e8f5e9;display:flex;align-items:center;justify-content:center;">
              <svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                <circle cx="20" cy="15" r="9" fill="#27ae60" opacity="0.85"/>
                <ellipse cx="20" cy="36" rx="14" ry="9" fill="#27ae60" opacity="0.65"/>
              </svg>
            </div>
            <div>
              <div class="stars" style="font-size:12px;">★★★★★</div>
              <p class="author-name" data-i18n="testi.n3">Sukardi</p>
              <p class="author-title" data-i18n="testi.r3">Pemilik Toko Bahan Kue, Pati</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

html = html.replace(old_testi_html, new_testi_html)

# ── Add changeTesti JS function ──
old_js_marker = "  document.getElementById('year').textContent = new Date().getFullYear();"
new_js_marker = """  document.getElementById('year').textContent = new Date().getFullYear();

  // Testimonial slider
  let testiCurrent = 0;
  const testiTotal = 3;
  function changeTesti(dir) {
    testiCurrent = (testiCurrent + dir + testiTotal) % testiTotal;
    document.getElementById('testiTrack').style.transform = 'translateX(-' + (testiCurrent * 100) + '%)';
  }"""
html = html.replace(old_js_marker, new_js_marker)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated successfully")

# Verify replacements worked
checks = [
    ('data-i18n="services.btn_view"', html.count('data-i18n="services.btn_view"')),
    ('data-i18n="pricing.p1_f1"', html.count('data-i18n="pricing.p1_f1"')),
    ('data-i18n="footer.prod1"', html.count('data-i18n="footer.prod1"')),
    ('testi-tasya.jpg', html.count('testi-tasya.jpg')),
    ('changeTesti', html.count('changeTesti')),
    ('testi-track', html.count('testi-track')),
]
for name, count in checks:
    status = "OK" if count > 0 else "MISSING"
    print(f"  {status}: {name} (found {count}x)")
