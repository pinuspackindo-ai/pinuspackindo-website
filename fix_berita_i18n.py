import json, re

# ─── 1. Update lang/id.json ───────────────────────────────────────────────────
with open('lang/id.json', 'r', encoding='utf-8') as f:
    id_data = json.load(f)

id_data['news'] = {
    "label": "Update Terbaru dari Pinus Packindo!",
    "title": "Berita & Acara",
    "sub": "Ikuti perkembangan terbaru, info harga, dan pengumuman penting dari Pinus Packindo.",
    "all": "Lihat Semua Berita & Acara →",
    "read_more": "Baca Selengkapnya →",
    "n1_cat": "Berita",
    "n1_title": "Kelangkaan Bahan Baku Plastik Imbas Konflik Iran–Amerika Serikat",
    "n1_desc": "Pasokan petrokimia global terganggu akibat memanasnya konflik Iran–AS. Harga kemasan plastik berpotensi naik 15–25% dalam waktu dekat...",
    "n2_cat": "Analisis Pasar",
    "n2_title": "Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku",
    "n2_desc": "Kenaikan harga PE, PP, dan PVC memukul industri kemasan. Tabel lengkap dampak per jenis kemasan dan strategi bertahan untuk UMKM...",
    "n3_cat": "Pernyataan Resmi",
    "n3_title": "Jangan Panik! Pinus Packindo Pastikan Stok Aman & Krisis Bersifat Sementara",
    "n3_desc": "Pernyataan resmi manajemen Pinus Packindo: stok kemasan aman, harga terjangkau, dan situasi diproyeksikan pulih dalam 3–6 bulan...",
    "n4_cat": "Update Harga",
    "n4_title": "Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun",
    "n4_desc": "PE dan PP sudah turun −11% dari puncaknya. Tren pemulihan terkonfirmasi, target kembali normal akhir 2026...",
    "n5_cat": "Info Operasional",
    "n5_title": "Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!",
    "n5_desc": "Kami hadir setiap hari tanpa libur, dari pagi hingga malam. Kebutuhan kemasan Anda selalu terpenuhi kapanpun dibutuhkan..."
}

id_data['berita'] = {
    "tag": "Update & Kegiatan",
    "h1": "Berita & Acara",
    "desc": "Ikuti perkembangan terbaru Pinus Packindo — mulai dari info harga, stok, hingga pengumuman penting kami.",
    "section_label": "Terbaru",
    "section_title": "Semua Berita & Acara",
    "btn_read": "Baca Selengkapnya",
    "n1_cat": "Berita",
    "n1_title": "Kelangkaan Bahan Baku Plastik Imbas Konflik Iran–Amerika Serikat",
    "n1_desc": "Pasokan petrokimia global terganggu akibat memanasnya konflik Iran–AS. Harga kemasan plastik berpotensi naik 15–25% dalam waktu dekat...",
    "n2_cat": "Analisis Pasar",
    "n2_title": "Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku",
    "n2_desc": "Kenaikan harga PE, PP, dan PVC memukul industri kemasan. Tabel lengkap dampak per jenis kemasan dan strategi bertahan untuk UMKM...",
    "n3_cat": "Pernyataan Resmi",
    "n3_title": "Jangan Panik! Pinus Packindo Pastikan Stok Aman & Krisis Bersifat Sementara",
    "n3_desc": "Pernyataan resmi manajemen Pinus Packindo: stok kemasan aman, harga terjangkau, dan situasi diproyeksikan pulih dalam 3–6 bulan...",
    "n4_cat": "Update Harga",
    "n4_title": "Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun",
    "n4_desc": "PE dan PP sudah turun −11% dari puncaknya. Tren pemulihan terkonfirmasi, target kembali normal akhir 2026...",
    "n5_cat": "Info Operasional",
    "n5_title": "Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!",
    "n5_desc": "Kami hadir setiap hari tanpa libur, dari pagi hingga malam. Kebutuhan kemasan Anda selalu terpenuhi kapanpun dibutuhkan..."
}

with open('lang/id.json', 'w', encoding='utf-8') as f:
    json.dump(id_data, f, ensure_ascii=False, indent=2)
print('id.json updated')

# ─── 2. Update lang/en.json ───────────────────────────────────────────────────
with open('lang/en.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

en_data['news'] = {
    "label": "Latest Updates from Pinus Packindo!",
    "title": "News & Events",
    "sub": "Stay up to date with the latest news, price updates, and important announcements from Pinus Packindo.",
    "all": "View All News & Events →",
    "read_more": "Read More →",
    "n1_cat": "News",
    "n1_title": "Plastic Raw Material Shortage Due to Iran–US Conflict",
    "n1_desc": "Global petrochemical supply disrupted by the escalating Iran–US conflict. Plastic packaging prices may rise 15–25% in the near term...",
    "n2_cat": "Market Analysis",
    "n2_title": "Plastic Packaging Prices Surge Up to 78% Due to Raw Material Shortage",
    "n2_desc": "Rising PE, PP, and PVC prices are hitting the packaging industry hard. Full price table by packaging type and survival strategies for SMEs...",
    "n3_cat": "Official Statement",
    "n3_title": "Don’t Panic! Pinus Packindo Ensures Stable Stock & Crisis is Temporary",
    "n3_desc": "Official statement from Pinus Packindo management: packaging stock is secure, prices remain competitive, situation projected to recover in 3–6 months...",
    "n4_cat": "Price Update",
    "n4_title": "Good News! Plastic Raw Material Prices Are Gradually Falling",
    "n4_desc": "PE and PP have already dropped −11% from their peak. Recovery trend confirmed, target back to normal by end of 2026...",
    "n5_cat": "Operational Info",
    "n5_title": "Pinus Packindo Open Every Day 08:00–21:00, Including Public Holidays!",
    "n5_desc": "We’re open every single day, morning to night. Your packaging needs are always fulfilled whenever you need us..."
}

en_data['berita'] = {
    "tag": "Updates & Activities",
    "h1": "News & Events",
    "desc": "Stay updated with the latest from Pinus Packindo — price info, stock updates, and important announcements.",
    "section_label": "Latest",
    "section_title": "All News & Events",
    "btn_read": "Read More",
    "n1_cat": "News",
    "n1_title": "Plastic Raw Material Shortage Due to Iran–US Conflict",
    "n1_desc": "Global petrochemical supply disrupted by the escalating Iran–US conflict. Plastic packaging prices may rise 15–25% in the near term...",
    "n2_cat": "Market Analysis",
    "n2_title": "Plastic Packaging Prices Surge Up to 78% Due to Raw Material Shortage",
    "n2_desc": "Rising PE, PP, and PVC prices are hitting the packaging industry hard. Full price table by packaging type and survival strategies for SMEs...",
    "n3_cat": "Official Statement",
    "n3_title": "Don’t Panic! Pinus Packindo Ensures Stable Stock & Crisis is Temporary",
    "n3_desc": "Official statement from Pinus Packindo management: packaging stock is secure, prices remain competitive, situation projected to recover in 3–6 months...",
    "n4_cat": "Price Update",
    "n4_title": "Good News! Plastic Raw Material Prices Are Gradually Falling",
    "n4_desc": "PE and PP have already dropped −11% from their peak. Recovery trend confirmed, target back to normal by end of 2026...",
    "n5_cat": "Operational Info",
    "n5_title": "Pinus Packindo Open Every Day 08:00–21:00, Including Public Holidays!",
    "n5_desc": "We’re open every single day, morning to night. Your packaging needs are always fulfilled whenever you need us..."
}

with open('lang/en.json', 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)
print('en.json updated')

# ─── 3. Patch index.html — add data-i18n to berita slide cards ────────────────
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Berita 1 card patches
html = html.replace(
    '<span class="aslide-cat" style="background:#fde8e8;color:#e74c3c;">Berita</span>',
    '<span class="aslide-cat" style="background:#fde8e8;color:#e74c3c;" data-i18n="news.n1_cat">Berita</span>'
)
html = html.replace(
    '<h3>Kelangkaan Bijah Plastik Imbas Konflik Iran–Amerika Serikat</h3>',
    '<h3 data-i18n="news.n1_title">Kelangkaan Bahan Baku Plastik Imbas Konflik Iran–Amerika Serikat</h3>'
)
html = html.replace(
    '<p>Pasokan petrokimia global terganggu, harga kemasan plastik berpotensi naik 15–25% dalam waktu dekat...</p>',
    '<p data-i18n="news.n1_desc">Pasokan petrokimia global terganggu, harga kemasan plastik berpotensi naik 15–25% dalam waktu dekat...</p>'
)

# Berita 2 card patches
html = html.replace(
    '<span class="aslide-cat" style="background:#fff3e0;color:#e67e22;">Analisis Pasar</span>',
    '<span class="aslide-cat" style="background:#fff3e0;color:#e67e22;" data-i18n="news.n2_cat">Analisis Pasar</span>'
)
html = html.replace(
    '<h3>Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku</h3>',
    '<h3 data-i18n="news.n2_title">Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku</h3>'
)
html = html.replace(
    '<p>PE naik 78%, PP naik 65% — tabel lengkap dampak per jenis kemasan dan strategi bertahan UMKM...</p>',
    '<p data-i18n="news.n2_desc">PE naik 78%, PP naik 65% — tabel lengkap dampak per jenis kemasan dan strategi bertahan UMKM...</p>'
)

# Berita 3 card patches
html = html.replace(
    '<span class="aslide-cat" style="background:#e8f5e9;color:#27ae60;">\U0001f4e2 Pernyataan Resmi</span>',
    '<span class="aslide-cat" style="background:#e8f5e9;color:#27ae60;" data-i18n="news.n3_cat">\U0001f4e2 Pernyataan Resmi</span>'
)
html = html.replace(
    '<h3>Jangan Panik! Pinus Packindo Pastikan Stok Aman &amp; Krisis Bersifat Sementara</h3>',
    '<h3 data-i18n="news.n3_title">Jangan Panik! Pinus Packindo Pastikan Stok Aman &amp; Krisis Bersifat Sementara</h3>'
)
html = html.replace(
    '<p>Pernyataan resmi: stok terjaga, harga kompetitif, dan situasi diproyeksikan pulih dalam 3–6 bulan...</p>',
    '<p data-i18n="news.n3_desc">Pernyataan resmi: stok terjaga, harga kompetitif, dan situasi diproyeksikan pulih dalam 3–6 bulan...</p>'
)

# Berita 4 card patches
html = html.replace(
    '<span class="aslide-cat" style="background:#dbeafe;color:#1d4ed8;">\U0001f4c9 Update Harga</span>',
    '<span class="aslide-cat" style="background:#dbeafe;color:#1d4ed8;" data-i18n="news.n4_cat">\U0001f4c9 Update Harga</span>'
)
html = html.replace(
    '<h3>Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun</h3>',
    '<h3 data-i18n="news.n4_title">Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun</h3>'
)
html = html.replace(
    '<p>PE dan PP sudah turun −11% dari puncaknya. Tren pemulihan terkonfirmasi, target normal akhir 2026...</p>',
    '<p data-i18n="news.n4_desc">PE dan PP sudah turun −11% dari puncaknya. Tren pemulihan terkonfirmasi, target normal akhir 2026...</p>'
)

# Berita 5 card patches
html = html.replace(
    '<span class="aslide-cat" style="background:#e8f5e9;color:#27ae60;">\U0001f557 Info Operasional</span>',
    '<span class="aslide-cat" style="background:#e8f5e9;color:#27ae60;" data-i18n="news.n5_cat">\U0001f557 Info Operasional</span>'
)
html = html.replace(
    '<h3>Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!</h3>',
    '<h3 data-i18n="news.n5_title">Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!</h3>'
)
html = html.replace(
    '<p>Hadir 7 hari seminggu dari pagi hingga malam. Kebutuhan kemasan Anda selalu terpenuhi kapanpun...</p>',
    '<p data-i18n="news.n5_desc">Hadir 7 hari seminggu dari pagi hingga malam. Kebutuhan kemasan Anda selalu terpenuhi kapanpun...</p>'
)

# Patch read_more spans that have no data-i18n inside bslide section
# Only the ones inside bslideTrack that don't already have data-i18n
html = html.replace(
    '            <span class="aslide-read">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 2 -->',
    '            <span class="aslide-read" data-i18n="news.read_more">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 2 -->'
)
html = html.replace(
    '            <span class="aslide-read">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 3 -->',
    '            <span class="aslide-read" data-i18n="news.read_more">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 3 -->'
)
html = html.replace(
    '            <span class="aslide-read">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 4 -->',
    '            <span class="aslide-read" data-i18n="news.read_more">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 4 -->'
)
html = html.replace(
    '            <span class="aslide-read">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 5 -->',
    '            <span class="aslide-read" data-i18n="news.read_more">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n        <!-- Berita 5 -->'
)
# Last berita (5) read_more before closing
html = html.replace(
    '            <span class="aslide-read">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n      </div>\n    </div>\n  </div>',
    '            <span class="aslide-read" data-i18n="news.read_more">Baca Selengkapnya →</span>\n          </div>\n        </div>\n\n      </div>\n    </div>\n  </div>'
)

# Section title/label/sub for berita section
html = html.replace(
    'data-i18n="news.label">Update Terbaru dari Pinus Packindo!',
    'data-i18n="news.label">Update Terbaru dari Pinus Packindo!'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html patched')

# ─── 4. Patch berita.html — add data-i18n to all berita cards ────────────────
with open('berita.html', 'r', encoding='utf-8') as f:
    bhtml = f.read()

# Section labels
bhtml = bhtml.replace(
    '<div class="section-label" data-i18n="berita.section_label">Terbaru</div>',
    '<div class="section-label" data-i18n="berita.section_label">Terbaru</div>'
)
bhtml = bhtml.replace(
    '<div class="section-title" style="font-size:28px;font-weight:800;" data-i18n="berita.section_title">Semua Berita &amp; Acara</div>',
    '<div class="section-title" style="font-size:28px;font-weight:800;" data-i18n="berita.section_title">Semua Berita &amp; Acara</div>'
)

# Berita 1
bhtml = bhtml.replace(
    '<span class="article-cat" style="background:#fde8e8;color:#e74c3c;">Berita</span>',
    '<span class="article-cat" style="background:#fde8e8;color:#e74c3c;" data-i18n="berita.n1_cat">Berita</span>'
)
bhtml = bhtml.replace(
    '<h3>Kelangkaan Bijih Plastik Imbas Konflik Iran–Amerika Serikat</h3>',
    '<h3 data-i18n="berita.n1_title">Kelangkaan Bahan Baku Plastik Imbas Konflik Iran–Amerika Serikat</h3>'
)
bhtml = bhtml.replace(
    '<p>Pasokan petrokimia global terganggu akibat memanasnya konflik Iran–AS. Harga kemasan plastik berpotensi naik 15–25% dalam waktu dekat...</p>',
    '<p data-i18n="berita.n1_desc">Pasokan petrokimia global terganggu akibat memanasnya konflik Iran–AS. Harga kemasan plastik berpotensi naik 15–25% dalam waktu dekat...</p>'
)
bhtml = bhtml.replace(
    '<button class="btn-read" onclick="location.href=\'berita-1.html\'">Baca Selengkapnya</button>',
    '<button class="btn-read" onclick="location.href=\'berita-1.html\'" data-i18n="berita.btn_read">Baca Selengkapnya</button>'
)

# Berita 2
bhtml = bhtml.replace(
    '<span class="article-cat" style="background:#fff3e0;color:#e67e22;">Analisis Pasar</span>',
    '<span class="article-cat" style="background:#fff3e0;color:#e67e22;" data-i18n="berita.n2_cat">Analisis Pasar</span>'
)
bhtml = bhtml.replace(
    '<h3>Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku</h3>',
    '<h3 data-i18n="berita.n2_title">Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku</h3>'
)
bhtml = bhtml.replace(
    '<p>Kenaikan harga PE, PP, dan PVC memukul industri kemasan. Tabel lengkap dampak per jenis kemasan dan strategi bertahan untuk UMKM...</p>',
    '<p data-i18n="berita.n2_desc">Kenaikan harga PE, PP, dan PVC memukul industri kemasan. Tabel lengkap dampak per jenis kemasan dan strategi bertahan untuk UMKM...</p>'
)
bhtml = bhtml.replace(
    '<button class="btn-read" onclick="location.href=\'berita-2.html\'">Baca Selengkapnya</button>',
    '<button class="btn-read" onclick="location.href=\'berita-2.html\'" data-i18n="berita.btn_read">Baca Selengkapnya</button>'
)

# Berita 3
bhtml = bhtml.replace(
    '<span class="article-cat" style="background:#e8f5e9;color:#27ae60;">\U0001f4e2 Pernyataan Resmi</span>',
    '<span class="article-cat" style="background:#e8f5e9;color:#27ae60;" data-i18n="berita.n3_cat">\U0001f4e2 Pernyataan Resmi</span>'
)
bhtml = bhtml.replace(
    '<h3>Jangan Panik! Pinus Packindo Pastikan Stok Aman &amp; Krisis Bersifat Sementara</h3>',
    '<h3 data-i18n="berita.n3_title">Jangan Panik! Pinus Packindo Pastikan Stok Aman &amp; Krisis Bersifat Sementara</h3>'
)
bhtml = bhtml.replace(
    '<p>Pernyataan resmi manajemen Pinus Packindo: stok kemasan aman, harga terjangkau, dan situasi kelangkaan diproyeksikan pulih dalam 3–6 bulan...</p>',
    '<p data-i18n="berita.n3_desc">Pernyataan resmi manajemen Pinus Packindo: stok kemasan aman, harga terjangkau, dan situasi kelangkaan diproyeksikan pulih dalam 3–6 bulan...</p>'
)
bhtml = bhtml.replace(
    '<button class="btn-read" onclick="location.href=\'berita-3.html\'">Baca Selengkapnya</button>',
    '<button class="btn-read" onclick="location.href=\'berita-3.html\'" data-i18n="berita.btn_read">Baca Selengkapnya</button>'
)

# Berita 4
bhtml = bhtml.replace(
    '<span class="article-cat" style="background:#dbeafe;color:#1d4ed8;">\U0001f4c9 Update Harga</span>',
    '<span class="article-cat" style="background:#dbeafe;color:#1d4ed8;" data-i18n="berita.n4_cat">\U0001f4c9 Update Harga</span>'
)
bhtml = bhtml.replace(
    '<h3>Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun</h3>',
    '<h3 data-i18n="berita.n4_title">Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun</h3>'
)
bhtml = bhtml.replace(
    '<p>Setelah puncak di Mei 2026, indeks harga PE dan PP sudah turun −11% lebih. Tren pemulihan terkonfirmasi — target kembali normal akhir 2026...</p>',
    '<p data-i18n="berita.n4_desc">Setelah puncak di Mei 2026, indeks harga PE dan PP sudah turun −11% lebih. Tren pemulihan terkonfirmasi — target kembali normal akhir 2026...</p>'
)
bhtml = bhtml.replace(
    '<button class="btn-read" onclick="location.href=\'berita-4.html\'">Baca Selengkapnya</button>',
    '<button class="btn-read" onclick="location.href=\'berita-4.html\'" data-i18n="berita.btn_read">Baca Selengkapnya</button>'
)

# Berita 5
bhtml = bhtml.replace(
    '<span class="article-cat" style="background:#e8f5e9;color:#27ae60;">\U0001f557 Info Operasional</span>',
    '<span class="article-cat" style="background:#e8f5e9;color:#27ae60;" data-i18n="berita.n5_cat">\U0001f557 Info Operasional</span>'
)
bhtml = bhtml.replace(
    '<h3>Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!</h3>',
    '<h3 data-i18n="berita.n5_title">Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!</h3>'
)
bhtml = bhtml.replace(
    '<p>Kami hadir setiap hari tanpa libur, dari pagi hingga malam. Kebutuhan kemasan Anda selalu terpenuhi kapanpun dibutuhkan...</p>',
    '<p data-i18n="berita.n5_desc">Kami hadir setiap hari tanpa libur, dari pagi hingga malam. Kebutuhan kemasan Anda selalu terpenuhi kapanpun dibutuhkan...</p>'
)
bhtml = bhtml.replace(
    '<button class="btn-read" onclick="location.href=\'berita-5.html\'">Baca Selengkapnya</button>',
    '<button class="btn-read" onclick="location.href=\'berita-5.html\'" data-i18n="berita.btn_read">Baca Selengkapnya</button>'
)

# Hero section
bhtml = bhtml.replace(
    '<div class="page-hero-tag" data-i18n="berita.tag">Update &amp; Kegiatan</div>',
    '<div class="page-hero-tag" data-i18n="berita.tag">Update &amp; Kegiatan</div>'
)

with open('berita.html', 'w', encoding='utf-8') as f:
    f.write(bhtml)
print('berita.html patched')
print('All done!')
