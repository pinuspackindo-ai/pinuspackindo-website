import json

# ── DATA ─────────────────────────────────────────────────────────────────────
artikels = [
    {'slug':'artikel-1','cat':'Tips Kemasan','date':'12 Juni 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'5 Tips Memilih Kemasan yang Tepat untuk Produk Makanan Anda',
     'desc':'Kemasan yang tepat bukan hanya melindungi produk, tapi juga menjadi media promosi bisnis Anda.',
     'body':'''<p>Kemasan adalah wajah pertama produk Anda yang dilihat konsumen. Pemilihan kemasan yang tepat tidak hanya melindungi produk dari kerusakan, tetapi juga bisa menjadi alat pemasaran yang powerful untuk bisnis Anda.</p>
<h2>1. Sesuaikan dengan Jenis Produk</h2>
<p>Langkah pertama adalah memahami karakteristik produk Anda. Produk basah seperti minuman membutuhkan kemasan yang kedap air, sementara makanan kering bisa menggunakan kemasan kertas atau plastik biasa. Pastikan bahan kemasan tidak bereaksi dengan produk di dalamnya.</p>
<h2>2. Pilih Bahan yang Food Grade</h2>
<p>Untuk produk makanan, selalu gunakan kemasan berlabel food grade. Kemasan food grade telah memenuhi standar keamanan pangan dan aman bersentuhan langsung dengan makanan tanpa risiko kontaminasi bahan kimia berbahaya.</p>
<h2>3. Pertimbangkan Ukuran dan Bentuk</h2>
<p>Kemasan yang terlalu besar akan memboroskan biaya dan terlihat tidak profesional, sementara yang terlalu kecil bisa merusak produk. Pilih ukuran yang pas dengan sedikit ruang untuk padding jika diperlukan. Bentuk kemasan juga memengaruhi efisiensi penyimpanan dan pengiriman.</p>
<h2>4. Perhatikan Desain dan Branding</h2>
<p>Kemasan adalah media branding yang efektif. Pastikan kemasan Anda mencerminkan identitas brand — mulai dari warna, logo, hingga tipografi. Konsumen cenderung lebih mempercayai produk dengan kemasan yang rapi dan profesional.</p>
<h2>5. Hitung Biaya per Unit</h2>
<p>Kemasan yang mahal tidak selalu yang terbaik. Hitung biaya kemasan per unit produk dan pastikan tidak melebihi 10-15% dari harga jual. Untuk pembelian dalam jumlah besar (grosir), biasanya tersedia harga yang jauh lebih terjangkau.</p>
<p>Pinus Packindo menyediakan ribuan pilihan kemasan food grade berkualitas — mulai dari mika, box kraft, paper bag, hingga standing pouch. Konsultasikan kebutuhan kemasan Anda dengan tim kami secara gratis.</p>'''},
    {'slug':'artikel-2','cat':'Edukasi','date':'5 Juni 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Perbedaan Kemasan Plastik Food Grade dan Non-Food Grade yang Wajib Diketahui',
     'desc':'Tidak semua plastik aman untuk makanan. Ketahui perbedaannya sebelum memilih kemasan.',
     'body':'''<p>Memilih kemasan plastik untuk produk makanan bukan hal yang bisa dilakukan sembarangan. Ada perbedaan mendasar antara plastik food grade dan non-food grade yang wajib Anda pahami demi keamanan konsumen dan legalitas bisnis.</p>
<h2>Apa itu Plastik Food Grade?</h2>
<p>Plastik food grade adalah plastik yang telah memenuhi standar keamanan pangan internasional (FDA, BPOM, atau standar setara). Plastik ini bebas dari zat kimia berbahaya seperti BPA (Bisphenol A), phthalate, dan zat pewarna yang dapat larut ke dalam makanan.</p>
<h2>Cara Mengenali Kemasan Food Grade</h2>
<p>Perhatikan kode segitiga daur ulang di bagian bawah kemasan. Kode 1 (PET), 2 (HDPE), 4 (LDPE), dan 5 (PP) umumnya aman untuk makanan. Kode 3 (PVC), 6 (PS), dan 7 (Other) sebaiknya dihindari untuk kontak langsung dengan makanan.</p>
<h2>Bahaya Plastik Non-Food Grade</h2>
<p>Plastik non-food grade berpotensi melepaskan zat kimia berbahaya ke dalam makanan, terutama saat terkena panas atau asam. Penggunaan jangka panjang bisa berdampak pada kesehatan konsumen dan berisiko menimbulkan masalah hukum bagi pelaku usaha.</p>
<h2>Rekomendasi untuk UMKM Makanan</h2>
<p>Selalu beli kemasan dari supplier terpercaya yang bisa memberikan sertifikasi food grade. Simpan faktur pembelian sebagai bukti bahwa kemasan yang Anda gunakan aman dan legal. Pinus Packindo hanya menjual kemasan plastik food grade yang telah tersertifikasi.</p>'''},
    {'slug':'artikel-3','cat':'Tren','date':'28 Mei 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Tren Kemasan Ramah Lingkungan 2026 yang Wajib Diikuti Pelaku UMKM',
     'desc':'Konsumen semakin peduli lingkungan. Simak tren kemasan eco-friendly yang sedang naik daun.',
     'body':'''<p>Di era kesadaran lingkungan yang semakin tinggi, pilihan kemasan bisnis Anda berdampak langsung pada citra brand di mata konsumen. Berikut tren kemasan ramah lingkungan yang mendominasi pasar 2026.</p>
<h2>1. Kemasan Kraft Biodegradable</h2>
<p>Kemasan berbahan kraft (kertas coklat) yang dapat terurai secara alami semakin digemari. Box makan, paper bag, dan mangkok kertas berbahan kraft kini tersedia dalam berbagai ukuran dan ketebalan sesuai kebutuhan.</p>
<h2>2. Plastik Daur Ulang (Recycled Plastic)</h2>
<p>Kemasan plastik yang dibuat dari bahan daur ulang (rPET, rHDPE) mulai banyak dipilih oleh brand-brand besar. Selain lebih ramah lingkungan, penggunaan kemasan ini juga bisa menjadi poin keunggulan di mata konsumen yang eco-conscious.</p>
<h2>3. Kemasan Minimal & Lightweight</h2>
<p>Tren "less is more" — kemasan yang lebih tipis namun tetap kuat. Ini mengurangi penggunaan bahan baku sekaligus menekan biaya logistik karena bobot lebih ringan.</p>
<h2>4. Desain Kemasan Transparan</h2>
<p>Kemasan mika atau bening yang memperlihatkan produk langsung semakin populer, terutama untuk produk bakery dan snack premium. Konsumen bisa melihat langsung kualitas produk tanpa membuka kemasan.</p>
<p>Pinus Packindo menyediakan berbagai pilihan kemasan eco-friendly mulai dari paper bag kraft, box makanan biodegradable, hingga kemasan mika food grade. Hubungi tim kami untuk konsultasi gratis.</p>'''},
    {'slug':'artikel-4','cat':'Panduan','date':'15 Mei 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Panduan Lengkap Memilih Box Kue untuk Usaha Bakery Rumahan',
     'desc':'Panduan ini membantu Anda memilih box kue yang sesuai budget dan kebutuhan usaha bakery.',
     'body':'''<p>Bagi pelaku usaha bakery rumahan, kemasan kue bukan sekadar wadah — ini adalah representasi kualitas produk Anda. Panduan ini akan membantu Anda memilih box kue yang tepat.</p>
<h2>Jenis-jenis Box Kue</h2>
<p><strong>Box Mika (Transparan):</strong> Ideal untuk kue yang ingin ditampilkan langsung. Cocok untuk cupcake, kue kering, dan snack. Tersedia dalam berbagai ukuran dari kotak kecil hingga box besar untuk tart.</p>
<p><strong>Box Kraft:</strong> Berkesan premium dan natural. Cocok untuk brownies, roti artisan, dan kue ulang tahun. Bisa dicustom dengan stiker label brand Anda.</p>
<p><strong>Box Karton Putih:</strong> Pilihan ekonomis namun tetap rapi. Cocok untuk pesanan dalam jumlah besar seperti katering atau hampers.</p>
<h2>Cara Memilih Ukuran yang Tepat</h2>
<p>Ukur produk Anda dan tambahkan minimal 1-2 cm di setiap sisi untuk kenyamanan packaging. Untuk kue bulat, gunakan box persegi dengan sisi sedikit lebih besar dari diameter kue.</p>
<h2>Tips Hemat Biaya Kemasan</h2>
<p>Beli dalam jumlah banyak (minimal 50-100 pcs) untuk mendapatkan harga satuan yang lebih murah. Pilih box yang serbaguna — satu ukuran bisa digunakan untuk berbagai produk. Pinus Packindo menyediakan box kue mulai dari pembelian satuan hingga grosir.</p>'''},
    {'slug':'artikel-5','cat':'Tips Kemasan','date':'2 Mei 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Cara Menghitung Kebutuhan Kemasan untuk Bisnis F&B Anda',
     'desc':'Pelajari cara menghitung kebutuhan kemasan yang tepat agar tidak kekurangan atau kelebihan stok.',
     'body':'''<p>Manajemen stok kemasan yang buruk bisa menghambat operasional bisnis. Kekurangan kemasan saat pesanan membludak, atau kelebihan stok yang mengikat modal — keduanya sama-sama merugikan.</p>
<h2>Rumus Dasar Perhitungan Kebutuhan Kemasan</h2>
<p>Kebutuhan Kemasan Bulanan = (Rata-rata produk terjual/hari) × 30 hari × Buffer stok (1.2–1.5×)</p>
<p>Contoh: Jika Anda menjual rata-rata 50 box kue per hari, kebutuhan bulanan = 50 × 30 × 1.3 = 1.950 box per bulan.</p>
<h2>Faktor yang Perlu Dipertimbangkan</h2>
<p><strong>Seasonality:</strong> Tambahkan 20-30% stok ekstra untuk periode ramai seperti Lebaran, Natal, atau musim wisuda.</p>
<p><strong>Lead time supplier:</strong> Hitung waktu yang dibutuhkan dari pemesanan hingga kemasan sampai di tangan Anda. Pesan kemasan 1-2 minggu sebelum stok habis.</p>
<p><strong>Minimum order:</strong> Perhatikan minimum order supplier. Sesuaikan jumlah pembelian agar tidak terlalu jauh dari kebutuhan aktual.</p>
<h2>Tips Manajemen Stok Kemasan</h2>
<p>Gunakan metode FIFO (First In First Out) — kemasan yang pertama masuk, pertama digunakan. Catat keluar-masuk stok kemasan setiap hari. Buat reorder point: ketika stok tersisa X buah, segera order ulang.</p>'''},
    {'slug':'artikel-6','cat':'Edukasi','date':'20 April 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Mengenal Jenis-jenis Kertas Roti dan Fungsinya dalam Dunia Baking',
     'desc':'Kenali berbagai jenis kertas roti dan kapan menggunakannya untuk hasil baking terbaik.',
     'body':'''<p>Kertas roti adalah salah satu perlengkapan wajib di dapur bakery. Namun tahukah Anda bahwa ada beberapa jenis kertas roti dengan fungsi yang berbeda-beda?</p>
<h2>1. Parchment Paper (Kertas Roti Silikon)</h2>
<p>Parchment paper dilapisi silikon di kedua sisinya sehingga anti lengket sempurna dan tahan panas hingga 220°C. Ideal untuk memanggang kue kering, melapisi loyang brownies, dan membungkus makanan untuk dipanggang. Bisa digunakan ulang beberapa kali.</p>
<h2>2. Greaseproof Paper</h2>
<p>Kertas ini tahan terhadap lemak dan minyak, namun tidak anti lengket seperti parchment. Lebih cocok untuk membungkus makanan berminyak (burger, fried chicken), alas kemasan, atau pembungkus roti. Tidak disarankan untuk langsung melapisi loyang tanpa olesan mentega.</p>
<h2>3. Wax Paper</h2>
<p>Dilapisi lilin di kedua sisinya. Cocok untuk membungkus makanan dingin atau suhu ruang, namun TIDAK tahan panas — tidak boleh masuk oven. Biasa digunakan untuk alas display kue atau pembungkus permen.</p>
<h2>4. Kertas Roti Kraft (Unbleached)</h2>
<p>Kertas coklat alami tanpa pemutih kimia. Berkesan artisan dan eco-friendly. Banyak digunakan untuk membungkus roti artisan, packaging sourdough, atau alas tatakan makanan.</p>
<p>Pinus Packindo menyediakan semua jenis kertas roti di atas dalam berbagai ukuran dan kuantitas — mulai dari pack kecil untuk kebutuhan rumahan hingga rol besar untuk bisnis bakery skala besar.</p>'''},
]

beritas = [
    {'slug':'berita-1','cat':'Acara','date':'12 Juni 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Pinus Packindo Hadir di Pameran UMKM Pati 2026',
     'desc':'Pinus Packindo turut berpartisipasi dalam Pameran UMKM Kabupaten Pati 2026.',
     'body':'''<p>Pinus Packindo dengan bangga mengumumkan partisipasi kami dalam Pameran UMKM Kabupaten Pati 2026 yang diselenggarakan di Alun-alun Kabupaten Pati.</p>
<h2>Detail Acara</h2>
<p><strong>Tanggal:</strong> 15–20 Juni 2026<br><strong>Lokasi:</strong> Alun-alun Kabupaten Pati, Jawa Tengah<br><strong>Jam:</strong> 09.00 – 21.00 WIB<br><strong>Stand:</strong> Area Produk Kemasan & Baking Supply</p>
<h2>Apa yang Bisa Anda Temukan di Stand Kami?</h2>
<p>Kunjungi stand Pinus Packindo dan temukan ratusan produk kemasan langsung — mulai dari kemasan plastik food grade, box kertas, paper bag, styrofoam, peralatan baking, hingga bahan-bahan membuat kue. Dapatkan penawaran spesial pameran yang tidak tersedia di toko reguler.</p>
<h2>Penawaran Spesial Pameran</h2>
<p>Selama pameran berlangsung, kami memberikan diskon khusus untuk pembelian pertama, free konsultasi kemasan untuk UMKM, dan hadiah menarik untuk setiap pembelian di atas nilai tertentu. Jangan lewatkan kesempatan ini!</p>
<p>Untuk informasi lebih lanjut, hubungi kami melalui WhatsApp di (0852) 8333 8989 atau kunjungi toko kami di Jalan Penjawi No. 11, Pati.</p>'''},
    {'slug':'berita-2','cat':'Berita','date':'1 Juni 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Pinus Packindo Resmi Buka Toko di Jalan Penjawi No. 11 Pati',
     'desc':'Pembukaan resmi toko Pinus Packindo di lokasi baru yang lebih strategis di Pati.',
     'body':'''<p>Dengan penuh rasa syukur, kami mengumumkan pembukaan resmi toko Pinus Packindo di alamat baru yang lebih strategis: Jalan Penjawi No. 11, Pati, Jawa Tengah, 59111.</p>
<h2>Lokasi yang Lebih Strategis</h2>
<p>Toko baru kami berlokasi di pusat kota Pati, mudah dijangkau dari berbagai arah. Tersedia parkir yang luas untuk kendaraan roda dua maupun roda empat. Anda bisa menemukan titik lokasi kami di Google Maps dengan mencari "Pinus Packindo Pati".</p>
<h2>Fasilitas Toko Baru</h2>
<p>Toko baru kami hadir dengan tampilan yang lebih modern dan nyaman. Area display yang lebih luas memungkinkan Anda untuk melihat langsung ribuan produk kemasan dan baking supply yang kami sediakan. Tim CS kami siap membantu konsultasi kebutuhan kemasan Anda secara langsung.</p>
<h2>Jam Operasional</h2>
<p><strong>Senin – Sabtu:</strong> 08.00 – 17.00 WIB<br><strong>Minggu & Hari Libur:</strong> Tutup (order online tetap bisa melalui WhatsApp)</p>
<p>Kami mengundang seluruh pelanggan setia dan calon pelanggan untuk mengunjungi toko baru kami. Dapatkan promo grand opening spesial yang menanti Anda!</p>'''},
    {'slug':'berita-3','cat':'Promo','date':'20 Mei 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Promo Kemasan Spesial Lebaran: Diskon hingga 20% untuk Semua Kemasan Kue',
     'desc':'Dapatkan diskon spesial untuk kemasan kue, mika, dan paper bag selama periode promo.',
     'body':'''<p>Sambut momen Lebaran dengan kemasan berkualitas dari Pinus Packindo! Kami menghadirkan promo spesial diskon hingga 20% untuk semua produk kemasan kue selama periode promo berlangsung.</p>
<h2>Produk yang Mendapat Diskon</h2>
<p>✓ Box Mika / Transparan semua ukuran — diskon 15%<br>✓ Box Kraft Kue semua ukuran — diskon 20%<br>✓ Paper Bag semua ukuran dan warna — diskon 15%<br>✓ Gelas Kertas & Tutup — diskon 10%<br>✓ Standing Pouch Kue Kering — diskon 15%</p>
<h2>Syarat & Ketentuan</h2>
<p>Promo berlaku untuk pembelian minimal 100 pcs per item. Tidak berlaku bersamaan dengan promo lainnya. Stok terbatas — dapatkan sebelum kehabisan! Berlaku untuk pembelian langsung di toko maupun via WhatsApp CS.</p>
<h2>Cara Memesan</h2>
<p>Datang langsung ke toko kami di Jalan Penjawi No. 11, Pati, atau hubungi CS kami via WhatsApp di (0852) 8333 8989 untuk pemesanan online. Kami melayani pengiriman ke seluruh wilayah Pati dan sekitarnya.</p>'''},
    {'slug':'berita-4','cat':'Acara','date':'10 Mei 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Workshop Kemasan untuk UMKM F&B: Bersama Pinus Packindo',
     'desc':'Pinus Packindo menyelenggarakan workshop gratis tentang strategi pemilihan kemasan untuk UMKM.',
     'body':'''<p>Pinus Packindo menyelenggarakan Workshop Kemasan UMKM F&B secara GRATIS untuk para pelaku usaha food & beverage di wilayah Pati dan sekitarnya. Daftarkan diri Anda sekarang!</p>
<h2>Detail Workshop</h2>
<p><strong>Tema:</strong> Strategi Kemasan untuk Meningkatkan Penjualan UMKM<br><strong>Tanggal:</strong> Sabtu, 24 Mei 2026<br><strong>Waktu:</strong> 09.00 – 12.00 WIB<br><strong>Tempat:</strong> Toko Pinus Packindo, Jl. Penjawi No. 11, Pati<br><strong>Biaya:</strong> GRATIS (terbatas 30 peserta)</p>
<h2>Materi Workshop</h2>
<p>✓ Cara memilih kemasan yang tepat untuk produk F&B<br>✓ Tips branding melalui kemasan dengan budget minimal<br>✓ Menghitung biaya kemasan yang efisien<br>✓ Tren kemasan 2026 untuk UMKM<br>✓ Sesi konsultasi langsung dengan tim Pinus Packindo</p>
<h2>Cara Daftar</h2>
<p>Hubungi kami melalui WhatsApp di (0852) 8333 8989 dengan format: WORKSHOP_NAMA_USAHA_JUMLAH PESERTA. Pendaftaran ditutup saat kuota penuh. Peserta akan mendapatkan goodie bag dan voucher belanja eksklusif!</p>'''},
    {'slug':'berita-5','cat':'Berita','date':'1 April 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Pinus Packindo Kini Hadir di Shopee dan TikTok Shop',
     'desc':'Kini Anda bisa berbelanja produk Pinus Packindo secara online melalui Shopee dan TikTok Shop.',
     'body':'''<p>Kabar gembira bagi pelanggan Pinus Packindo di seluruh Indonesia! Mulai hari ini, Anda bisa berbelanja produk kemasan dan baking supply dari Pinus Packindo secara online melalui dua platform e-commerce terpercaya.</p>
<h2>Toko Online Pinus Packindo</h2>
<p><strong>Shopee:</strong> Cari "Pinus Packindo" di aplikasi Shopee atau kunjungi toko kami langsung.<br><strong>TikTok Shop:</strong> Temukan produk kami di TikTok Shop Pinus Packindo dengan ribuan pilihan kemasan.</p>
<h2>Keunggulan Belanja Online</h2>
<p>✓ Pengiriman ke seluruh Indonesia<br>✓ Tersedia berbagai pilihan jasa kirim<br>✓ Pembayaran mudah (transfer, COD, e-wallet)<br>✓ Foto produk detail dan deskripsi lengkap<br>✓ Rating & ulasan dari pembeli sebelumnya</p>
<h2>Promo Pembukaan Toko Online</h2>
<p>Untuk merayakan pembukaan toko online kami, dapatkan diskon spesial untuk pembelian pertama di Shopee dan TikTok Shop. Gratis ongkir untuk pembelian pertama (syarat & ketentuan berlaku).</p>
<p>Untuk pembelian grosir dalam jumlah besar, tetap hubungi CS kami langsung via WhatsApp untuk harga terbaik.</p>'''},
    {'slug':'berita-6','cat':'Promo','date':'15 Maret 2026','author':'Tim Pinus Packindo','src':'pinuspackindo.com',
     'title':'Peluncuran Produk Baru: Kemasan Kraft Ramah Lingkungan',
     'desc':'Pinus Packindo meluncurkan lini terbaru kemasan kraft biodegradable untuk bisnis F&B.',
     'body':'''<p>Pinus Packindo dengan bangga memperkenalkan lini produk terbaru kami: Kemasan Kraft Ramah Lingkungan — solusi packaging eco-friendly untuk bisnis food & beverage modern.</p>
<h2>Produk Baru yang Diluncurkan</h2>
<p><strong>1. Box Makan Kraft Biodegradable</strong><br>Tersedia dalam ukuran small, medium, dan large. Tahan minyak dan panas, cocok untuk nasi, ayam, dan berbagai menu siap saji. Material 100% dapat terurai secara biologis.</p>
<p><strong>2. Paper Bag Kraft Handles</strong><br>Paper bag dengan handle twisted kraft yang kuat. Tersedia dalam 5 ukuran dan 3 pilihan warna natural. Cocok untuk bakery, oleh-oleh, dan fashion.</p>
<p><strong>3. Mangkok Kertas Kraft</strong><br>Mangkok kertas kraft untuk bakso, mie, bubur, dan makanan berkuah. Tahan bocor dengan lapisan food-safe coating biodegradable.</p>
<h2>Harga & Pemesanan</h2>
<p>Produk baru ini tersedia mulai dari pembelian eceran di toko hingga pembelian grosir minimum 500 pcs dengan harga spesial. Untuk info harga dan katalog lengkap, hubungi CS kami via WhatsApp (0852) 8333 8989 atau kunjungi toko di Jl. Penjawi No. 11, Pati.</p>'''},
]

# ── SHARED PARTS ──────────────────────────────────────────────────────────────
social_strip = '''<div style="display:flex;gap:12px;justify-content:center;align-items:center;padding:40px 0 48px;background:#fff;">
  <a href="https://www.instagram.com/pinuspackindo?igsh=MXQ1OWNoMzlkaTg5aw==" target="_blank" aria-label="Instagram" style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;" onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'" onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'"><svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></a>
  <a href="https://www.tiktok.com/@pinus.packindo?_r=1&amp;_t=ZS-978Su6GNPwT" target="_blank" aria-label="TikTok" style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;" onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'" onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'"><svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.17 8.17 0 004.78 1.52V6.75a4.85 4.85 0 01-1.01-.06z"/></svg></a>
  <a href="https://www.facebook.com/pinuspackindo?mibextid=rS40aB7S9Ucbxw6v" target="_blank" aria-label="Facebook" style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;" onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'" onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'"><svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
  <a href="https://www.linkedin.com/company/cv-pinus-packindo/" target="_blank" aria-label="LinkedIn" style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;" onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'" onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'"><svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
</div>'''

footer_html = '''<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="footer-logo">
        <div class="logo-icon"><img src="images/logo.jpg" alt="Pinus Packindo Logo"></div>
        <div><div style="font-weight:800;font-size:16px;color:#fff;">Pinus Packindo</div><div style="font-size:10px;color:#666;">Packaging &amp; Baking Supply</div></div>
      </div>
      <p>Solusi kemasan dan baking supply berkualitas tinggi untuk bisnis Anda di seluruh Indonesia.</p>
    </div>
    <div class="footer-col">
      <h4>Menu</h4>
      <ul>
        <li><a href="index.html">Beranda</a></li>
        <li><a href="about.html">Tentang Kami</a></li>
        <li><a href="products.html">Produk</a></li>
        <li><a href="artikel.html">Artikel</a></li>
        <li><a href="berita.html">Berita &amp; Acara</a></li>
        <li><a href="contact.html">Kontak</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Produk</h4>
      <ul>
        <li><a href="products.html#kemasan-plastik">Kemasan Plastik</a></li>
        <li><a href="products.html#kemasan-kertas">Kemasan Kertas</a></li>
        <li><a href="products.html#kemasan-styrofoam">Kemasan Styrofoam</a></li>
        <li><a href="products.html#peralatan-baking">Peralatan Baking</a></li>
        <li><a href="products.html#bahan-baking">Bahan Baking</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Kontak</h4>
      <ul>
        <li><a href="tel:02954107604">(0295) 410 7604</a></li>
        <li><a href="https://wa.me/6285283338989" target="_blank">(0852) 8333 8989</a></li>
        <li><a href="mailto:cspinuspackindo@gmail.com">cspinuspackindo@gmail.com</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">&copy; <span id="year"></span> Pinus Packindo. Hak Cipta Dilindungi.</div>
</footer>'''

def build_detail(item, back_href, back_label, hero_img):
    return f'''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{item['title']} - Pinus Packindo</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter',sans-serif;color:#222;}}
a{{text-decoration:none;color:inherit;}}
nav{{display:flex;align-items:center;justify-content:space-between;padding:16px 80px;background:#fff;position:sticky;top:0;z-index:100;box-shadow:0 1px 8px rgba(0,0,0,0.07);}}
.logo{{display:flex;align-items:center;gap:10px;cursor:pointer;}}
.logo-icon{{width:64px;height:64px;border-radius:10px;overflow:hidden;flex-shrink:0;}}
.logo-icon img{{width:100%;height:100%;object-fit:cover;}}
.logo-name{{font-weight:800;font-size:22px;color:#27ae60;line-height:1.15;}}
.logo-sub{{font-size:11px;color:#999;letter-spacing:0.5px;}}
.nav-links{{display:flex;gap:24px;font-size:14px;font-weight:500;color:#444;}}
.nav-links a{{transition:color 0.18s,transform 0.18s;display:inline-block;}}
.nav-links a:hover{{color:#27ae60;transform:translateY(-2px);}}
.nav-links a.active{{color:#27ae60;font-weight:700;}}
.nav-right{{display:flex;align-items:center;gap:12px;}}
.lang-switcher{{display:flex;gap:4px;}}
.lang-btn{{padding:5px 10px;border-radius:5px;border:1.5px solid #ddd;background:#fff;font-size:12px;font-weight:600;cursor:pointer;color:#666;transition:all 0.2s;}}
.lang-btn.active,.lang-btn:hover{{background:#27ae60;color:#fff;border-color:#27ae60;}}
.btn-quote{{background:#27ae60;color:#fff;padding:10px 22px;border-radius:6px;font-size:14px;font-weight:600;border:none;cursor:pointer;transition:transform 0.18s,box-shadow 0.18s,background 0.18s;}}
.btn-quote:hover{{background:#1e8449;transform:translateY(-3px) scale(1.04);box-shadow:0 6px 20px rgba(39,174,96,0.35);}}
.breadcrumb{{background:#f8f8f8;padding:12px 80px;border-bottom:1px solid #eee;}}
.breadcrumb a{{font-size:13px;color:#27ae60;}}
.breadcrumb span{{font-size:13px;color:#999;margin:0 6px;}}
.breadcrumb strong{{font-size:13px;color:#444;}}
.article-hero{{
  background:linear-gradient(135deg,rgba(13,34,24,0.85) 0%,rgba(26,74,46,0.78) 55%,rgba(39,174,96,0.65) 100%),
  url('images/{hero_img}') center center/cover no-repeat;
  padding:72px 80px;
}}
.article-hero-tag{{font-size:11px;font-weight:700;color:rgba(255,255,255,0.6);text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;}}
.article-hero h1{{font-size:40px;font-weight:800;color:#fff;line-height:1.2;margin-bottom:20px;max-width:760px;}}
.article-hero-meta{{display:flex;align-items:center;gap:20px;flex-wrap:wrap;}}
.meta-badge{{font-size:11px;font-weight:700;background:rgba(255,255,255,0.15);color:#fff;border-radius:20px;padding:4px 12px;border:1px solid rgba(255,255,255,0.3);}}
.meta-text{{font-size:13px;color:rgba(255,255,255,0.7);}}
.article-main{{max-width:800px;margin:0 auto;padding:64px 80px;}}
.article-content h2{{font-size:22px;font-weight:800;color:#111;margin:32px 0 14px;}}
.article-content p{{font-size:15px;color:#444;line-height:1.85;margin-bottom:18px;}}
.article-content strong{{color:#111;}}
.article-divider{{border:none;border-top:2px solid #f0f0f0;margin:40px 0;}}
.article-back{{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:#27ae60;margin-bottom:40px;transition:gap 0.2s;cursor:pointer;}}
.article-back:hover{{gap:12px;}}
.author-box{{background:#f7fdf9;border-radius:14px;padding:24px 28px;display:flex;align-items:center;gap:20px;margin-top:48px;border:1px solid #e0f0e8;}}
.author-avatar-lg{{width:52px;height:52px;border-radius:50%;background:#27ae60;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:800;color:#fff;flex-shrink:0;}}
.author-info h4{{font-size:15px;font-weight:700;color:#111;margin-bottom:3px;}}
.author-info p{{font-size:13px;color:#666;}}
footer{{background:#111;color:#aaa;padding:56px 80px 24px;}}
.footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1.5fr;gap:48px;margin-bottom:40px;}}
.footer-brand p{{font-size:13px;color:#666;line-height:1.7;margin-top:14px;max-width:260px;}}
.footer-logo{{display:flex;align-items:center;gap:10px;margin-bottom:10px;}}
.footer-col h4{{font-size:13px;font-weight:700;color:#fff;margin-bottom:14px;}}
.footer-col ul{{list-style:none;display:flex;flex-direction:column;gap:8px;}}
.footer-col ul li a{{font-size:13px;color:#666;transition:color 0.2s;}}
.footer-col ul li a:hover{{color:#27ae60;}}
.footer-bottom{{border-top:1px solid #222;padding-top:20px;font-size:12px;color:#555;text-align:center;}}
</style>
</head>
<body>

<nav>
  <a class="logo" href="index.html">
    <div class="logo-icon"><img src="images/logo.jpg" alt="Pinus Packindo Logo"></div>
    <div><div class="logo-name">Pinus Packindo</div><div class="logo-sub">Packaging &amp; Baking Supply</div></div>
  </a>
  <div class="nav-links">
    <a href="index.html">Beranda</a>
    <a href="about.html">Tentang Kami</a>
    <a href="products.html">Produk</a>
    <a href="artikel.html" {"class='active'" if back_href=='artikel.html' else ""}>Artikel</a>
    <a href="berita.html" {"class='active'" if back_href=='berita.html' else ""}>Berita &amp; Acara</a>
    <a href="contact.html">Kontak</a>
  </div>
  <div class="nav-right">
    <div class="lang-switcher">
      <button class="lang-btn active" onclick="switchLang('id')">ID</button>
      <button class="lang-btn" onclick="switchLang('en')">EN</button>
    </div>
    <button class="btn-quote" onclick="location.href='contact.html'">Hubungi Kami</button>
  </div>
</nav>

<div class="breadcrumb">
  <a href="index.html">Beranda</a><span>›</span>
  <a href="{back_href}">{back_label}</a><span>›</span>
  <strong>{item['title'][:60]}{'...' if len(item['title'])>60 else ''}</strong>
</div>

<div class="article-hero">
  <div class="article-hero-tag">{item['cat']}</div>
  <h1>{item['title']}</h1>
  <div class="article-hero-meta">
    <span class="meta-badge">{item['cat']}</span>
    <span class="meta-text">📅 {item['date']}</span>
    <span class="meta-text">✍️ {item['author']}</span>
    <span class="meta-text">🔗 {item['src']}</span>
  </div>
</div>

<div class="article-main">
  <a class="article-back" href="{back_href}" onclick="history.back();return false;">← Kembali ke {back_label}</a>
  <div class="article-content">
    {item['body']}
  </div>
  <hr class="article-divider">
  <div class="author-box">
    <div class="author-avatar-lg">PP</div>
    <div class="author-info">
      <h4>{item['author']}</h4>
      <p>Diterbitkan pada {item['date']} · Sumber: {item['src']}</p>
    </div>
  </div>
</div>

{social_strip}

{footer_html}

<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  function switchLang(lang) {{ localStorage.setItem('lang',lang); }}
</script>
</body>
</html>'''

# Build all detail pages
for item in artikels:
    html = build_detail(item, 'artikel.html', 'Artikel', 'artikel-hero.png')
    with open(f"{item['slug']}.html",'w',encoding='utf-8') as f: f.write(html)
    print(f"{item['slug']}.html created")

for item in beritas:
    html = build_detail(item, 'berita.html', 'Berita & Acara', 'berita-hero.png')
    with open(f"{item['slug']}.html",'w',encoding='utf-8') as f: f.write(html)
    print(f"{item['slug']}.html created")

print('All detail pages done!')
