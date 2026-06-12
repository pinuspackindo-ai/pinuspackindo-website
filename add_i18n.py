import re

with open('index.html','r',encoding='utf-8') as f:
    h = f.read()

# ── ARTIKEL cards ──
artikel_map = [
    ('5 Tips Memilih Kemasan yang Tepat untuk Produk Makanan Anda', 'blog.a1_title'),
    ('Kemasan yang tepat bukan hanya melindungi produk, tapi juga menjadi media promosi bisnis Anda...', 'blog.a1_desc'),
    ('Perbedaan Kemasan Plastik Food Grade dan Non-Food Grade yang Wajib Diketahui', 'blog.a2_title'),
    ('Tidak semua plastik aman untuk makanan. Ketahui perbedaannya sebelum memilih kemasan untuk produk Anda...', 'blog.a2_desc'),
    ('Tren Kemasan Ramah Lingkungan 2026 yang Wajib Diikuti Pelaku UMKM', 'blog.a3_title'),
    ('Konsumen semakin peduli lingkungan. Simak tren kemasan eco-friendly yang sedang naik daun...', 'blog.a3_desc'),
    ('Panduan Lengkap Memilih Box Kue untuk Usaha Bakery Rumahan', 'blog.a4_title'),
    ('Panduan ini membantu Anda memilih box kue yang sesuai budget dan kebutuhan usaha bakery...', 'blog.a4_desc'),
    ('Cara Menghitung Kebutuhan Kemasan untuk Bisnis F&amp;B Anda', 'blog.a5_title'),
    ('Pelajari cara menghitung kebutuhan kemasan yang tepat agar tidak kekurangan atau kelebihan stok...', 'blog.a5_desc'),
]

for text, key in artikel_map:
    h = h.replace(
        f'>{text}<',
        f' data-i18n="{key}">{text}<',
        1
    )

# Fix aslide-read in artikel section (first 5 occurrences = artikel)
count = [0]
def fix_artikel_read(m):
    count[0] += 1
    if count[0] <= 5:
        return f'<span class="aslide-read" data-i18n="blog.read_more">{m.group(1)}</span>'
    return m.group(0)

h = re.sub(r'<span class="aslide-read">(Baca Selengkapnya →)</span>', fix_artikel_read, h)

# ── BERITA section header ──
h = h.replace(
    '<p class="section-label">Update Terbaru dari Pinus Packindo!</p>',
    '<p class="section-label" data-i18n="news.label">Update Terbaru dari Pinus Packindo!</p>'
)
h = h.replace(
    '<h2 class="section-title">Berita &amp; Acara</h2>',
    '<h2 class="section-title" data-i18n="news.title">Berita &amp; Acara</h2>'
)
h = h.replace(
    '<p class="section-sub">Ikuti perkembangan terbaru, promo spesial, dan acara-acara menarik dari Pinus Packindo.</p>',
    '<p class="section-sub" data-i18n="news.sub">Ikuti perkembangan terbaru, promo spesial, dan acara-acara menarik dari Pinus Packindo.</p>'
)
h = h.replace(
    '<a href="berita.html" class="btn-all-artikel">Lihat Semua Berita &amp; Acara →</a>',
    '<a href="berita.html" class="btn-all-artikel" data-i18n="news.all">Lihat Semua Berita &amp; Acara →</a>'
)

# ── BERITA cards ──
berita_map = [
    ('Pinus Packindo Hadir di Pameran UMKM Pati 2026', 'news.n1_title'),
    ('Pinus Packindo turut berpartisipasi dalam Pameran UMKM Kabupaten Pati 2026 dengan penawaran spesial...', 'news.n1_desc'),
    ('Pinus Packindo Resmi Buka Toko di Jalan Penjawi No. 11 Pati', 'news.n2_title'),
    ('Pembukaan resmi toko Pinus Packindo di lokasi baru yang lebih strategis di pusat kota Pati...', 'news.n2_desc'),
    ('Promo Kemasan Spesial Lebaran: Diskon hingga 20% untuk Semua Kemasan Kue', 'news.n3_title'),
    ('Dapatkan diskon spesial untuk kemasan kue, mika, dan paper bag selama periode promo berlangsung...', 'news.n3_desc'),
    ('Workshop Kemasan untuk UMKM F&amp;B: Bersama Pinus Packindo', 'news.n4_title'),
    ('Pinus Packindo menyelenggarakan workshop gratis tentang strategi pemilihan kemasan untuk UMKM...', 'news.n4_desc'),
    ('Pinus Packindo Kini Hadir di Shopee dan TikTok Shop', 'news.n5_title'),
    ('Kini Anda bisa berbelanja produk Pinus Packindo secara online melalui Shopee dan TikTok Shop...', 'news.n5_desc'),
]

for text, key in berita_map:
    h = h.replace(f'>{text}<', f' data-i18n="{key}">{text}<', 1)

# Category badges in berita section
cat_map = [
    ('style="background:#e8f0fd;color:#2563eb;">Acara</span>\n          </div>\n          <div class="aslide-body">\n            <div class="aslide-meta"><span class="aslide-cat" style="background:#e8f5e9',
     'style="background:#e8f0fd;color:#2563eb;" data-i18n="news.n1_cat">Acara</span>\n          </div>\n          <div class="aslide-body">\n            <div class="aslide-meta"><span class="aslide-cat" style="background:#e8f5e9'),
]
for old, new in cat_map:
    h = h.replace(old, new, 1)

# All remaining aslide-read spans (berita section = the remaining ones)
h = re.sub(
    r'<span class="aslide-read">(Baca Selengkapnya →)</span>',
    r'<span class="aslide-read" data-i18n="news.read_more">Baca Selengkapnya →</span>',
    h
)

with open('index.html','w',encoding='utf-8') as f:
    f.write(h)
print('Done! Verifying...')

# Quick check
checks = ['data-i18n="blog.a1_title"', 'data-i18n="blog.a5_desc"',
          'data-i18n="news.title"', 'data-i18n="news.n5_title"',
          'data-i18n="news.sub"', 'data-i18n="blog.read_more"']
for c in checks:
    found = c in open('index.html',encoding='utf-8').read()
    print(f'  {"OK" if found else "MISSING"}: {c}')
