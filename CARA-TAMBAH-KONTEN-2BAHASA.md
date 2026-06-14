# Cara Tambah Artikel / Berita 2 Bahasa (Otomatis)

Sejak sistem otomatis aktif, Anda **cukup isi form di admin** → terbit → halaman 2 bahasa muncul sendiri di website. Tidak perlu lewat developer.

## Langkah
1. Buka **pinuspackindo.com/admin**
2. Pilih **📝 Artikel** atau **📰 Berita & Acara** → **New**
3. Isi kolomnya:
   | Kolom | Isi |
   |-------|-----|
   | 🇮🇩 Judul (Indonesia) | Judul bahasa Indonesia |
   | 🇬🇧 Judul (English) | Terjemahan judul ke Inggris |
   | Kategori | mis. Tips, Edukasi, Berita |
   | Tanggal | tanggal terbit |
   | Kode Foto | mis. `0007` → foto `ma-0007.png` (artikel) / `mb-0007.svg` (berita) di folder images |
   | 🇮🇩 Ringkasan / 🇬🇧 Ringkasan (English) | ringkasan singkat 2 bahasa |
   | 🇮🇩 Konten (Indonesia) | isi lengkap |
   | 🇬🇧 Konten (English) | terjemahan isi — **susun paragraf/judul dengan URUTAN SAMA** seperti versi ID |
4. Klik **Publish/Save**
5. Tunggu ~1–2 menit → halaman otomatis muncul di menu Artikel/Berita, lengkap dengan tombol ID/EN.

## PENTING — agar terjemahan pas
- Versi Inggris harus punya **jumlah & urutan blok yang sama** (paragraf, judul `##`, list) dengan versi Indonesia. Sistem memasangkan blok ke-1 ID ↔ blok ke-1 EN, dst.
- Kalau kolom English **dikosongkan**, halaman tetap terbit tapi tombol EN menampilkan teks Indonesia (tidak error).

## Format konten (markdown sederhana)
- Judul bagian: `## Judul Bagian`
- Tebal: `**teks tebal**`
- List: baris diawali `- `
- Gambar: `![keterangan](images/namafile.png)`
- Tautan: `[teks](https://...)`

## Catatan teknis (untuk developer)
- Mesin build: `build.js` (zero-dependency, jalan otomatis saat Vercel build via `vercel.json` → `buildCommand`).
- Halaman lama (artikel-1..6, berita-1..5) ditandai `legacy: true` di file `.md`-nya → **dilewati** build (tetap pakai versi hand-coded yang sudah kaya konten/tabel).
- Halaman hasil generate: `artikel-<slug>.html` / `berita-<slug>.html` (di-gitignore, dibuat ulang tiap build).
- Kartu di listing disisipkan otomatis di antara penanda `<!--AUTO-CARDS-START-->...<!--AUTO-CARDS-END-->`.
- Untuk konten kaya (kartu data, tabel, timeline) seperti berita lama: itu hand-coded, tidak dari CMS. Konten CMS = teks/heading/list/gambar standar.
