# Catatan Perubahan Tampilan HP — Pinus Packindo Website

Tanggal kerja: **14 Juni 2026**

## Ringkasan
Sebelum 14 Juni, tampilan HP = **clone desktop yang diperkecil** (3 kolom, teks kecil, harus zoom).
Sejak 14 Juni, dibuat **tampilan HP khusus** (1–2 kolom, teks pas, tidak perlu zoom).

---

## TITIK BALIK (untuk revert)
| Penanda (git tag) | Commit | Arti |
|---|---|---|
| `tampilan-awal-clone-desktop` | `356bdda` | Tampilan HP AWAL = clone desktop (sebelum redesign) |
| `tampilan-hp-baru-14juni` | `95ea591` | Tampilan HP BARU (hasil hari ini) |

Kedua penanda sudah di-backup di GitHub.

### Kalau bos minta kembali ke tampilan awal (3 kolom clone desktop):
Cukup beri tahu saya "kembalikan tampilan HP ke awal". Caranya (teknis):
- Kecilkan blok `@media (max-width: 768px)` di tiap halaman kembali ke versi asli (hanya logo), atau
- Restore file dari tag `tampilan-awal-clone-desktop`.
- **Konten tetap dipertahankan** (teks, foto sampul, jam buka, dll) — yang dikembalikan hanya LAYOUT.

---

## DAFTAR PERUBAHAN (urut waktu)

### Layout dasar
1. `741f999` Tambah CSS mobile semua halaman (padding 80→20px, hero kecil, grid 1–2 kolom)
2. `0130a92` Cegah zoom-out: `overflow-x` + `img max-width` + `max-width:100vw`
3. `63fce67` Redesign penuh teks lebih besar, layout 1 kolom (ala Indomaret/Alfamart)
4. `ca10659` Carousel JS responsif: 1 kartu di HP, 3 di desktop
5. `997146f` Layout **2 kolom** semua section (services, keunggulan, cara beli, footer)

### Penyempurnaan
6. `9c48522` Perbaikan menyeluruh: about/contact/products dapat CSS mobile (sebelumnya melebar)
   - Produk **3 kolom**, artikel/berita listing **2 kolom**, footer 2 kolom
7. `dea35be` Hero foto penuh + teks lebih kecil + CSS mobile halaman detail artikel
8. `8e7171b` Hero kembali overlay, foto sampul artikel diperbaiki, font contact/footer dikecilkan
9. `f39b16e` Collage foto digeser, konten berita terbaca (grid 1 kolom, tabel scroll), tombol "Baca Selengkapnya" di bawah penulis, hero slide geser
10. `00937c3` **Bugfix**: berita-3 komentar CSS rusak (footer error), jam pengiriman H+1, jam CS 08–16, panah hero jadi segitiga
11. `b80b4e6` **Header sticky/freeze** saat scroll (fix `overflow-x: clip`), panah mobile, badge/tanggal, konten berita detail
12. `794615f` Hero slide s1-4 digeser (bukan s1-5), semua panah slideshow disembunyikan di HP (pakai swipe)
13. `95ea591` Indikator **titik (dots)** untuk slider services & testimoni di HP, tanggal di bawah badge

### Perubahan KONTEN (bukan layout — sebaiknya tetap dipertahankan walau revert)
- Foto sampul artikel/berita → `ma-000N.png` / `mb-000N.svg`
- Berita-5: pengiriman **H+1** (bukan hari sama), jam CS **08.00–16.00**
- Berita-3: perbaikan bug komentar CSS yang merusak footer
- Favicon logo Pinus

---

## YANG BELUM DIKERJAKAN
- Isi artikel/berita **belum 2 bahasa (ID/EN)** — `switchLang` di halaman detail masih stub, konten hardcoded Indonesia. Pekerjaan besar, menunggu persetujuan untuk dimulai.
