/* Mesin build Pinus Packindo — ubah _artikel/_berita (.md) menjadi halaman web 2 bahasa.
   Zero-dependency (Node murni). Halaman lama (legacy: true) dilewati. */
const fs = require('fs');
const path = require('path');

// ---------- util ----------
function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
function attrEsc(t) { return String(t).replace(/&/g, '&amp;').replace(/"/g, '&quot;'); }

// Parser frontmatter sederhana: key: value, "quoted", dan block scalar `key: |`
function parseMd(raw) {
  raw = raw.replace(/\r\n/g, '\n');
  const m = raw.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  const fm = {}; let body = '';
  if (!m) return { fm, body: raw };
  body = m[2] || '';
  const lines = m[1].split('\n');
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const km = line.match(/^([A-Za-z0-9_]+):\s*(.*)$/);
    if (!km) continue;
    const key = km[1]; let val = km[2];
    if (val === '|' || val === '|-' || val === '>') {
      // block scalar: kumpulkan baris terindentasi berikutnya
      const buf = [];
      let j = i + 1;
      while (j < lines.length && (lines[j].startsWith('  ') || lines[j].trim() === '')) {
        buf.push(lines[j].replace(/^ {2}/, ''));
        j++;
      }
      fm[key] = buf.join('\n').replace(/\n+$/, '');
      i = j - 1;
    } else {
      val = val.replace(/^["']|["']$/g, '');
      fm[key] = val;
    }
  }
  return { fm, body };
}

// Inline markdown → HTML
function inline(t) {
  t = esc(t);
  t = t.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (m, a, src) => `<img src="${attrEsc(src)}" alt="${attrEsc(a)}" style="width:100%;height:auto;border-radius:10px;margin:16px 0;">`);
  t = t.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, txt, url) => `<a href="${attrEsc(url)}" target="_blank">${txt}</a>`);
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  t = t.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  return t;
}

// Markdown body → array blok {tag, html} (html = inner sudah jadi)
function blocks(md) {
  if (!md) return [];
  const out = [];
  const paras = md.replace(/\r\n/g, '\n').split(/\n{2,}/);
  for (let p of paras) {
    p = p.trim();
    if (!p) continue;
    let mm;
    if ((mm = p.match(/^#{1,2}\s+(.*)$/m)) && /^#/.test(p)) {
      // heading (gabungan baris pertama)
      const h = p.match(/^(#{1,3})\s+(.*)$/);
      if (h) { out.push({ tag: h[1].length >= 2 ? 'h2' : 'h2', inner: inline(h[2]) }); continue; }
    }
    if (/^([-*])\s+/.test(p)) {
      const items = p.split('\n').filter(x => /^[-*]\s+/.test(x)).map(x => '<li>' + inline(x.replace(/^[-*]\s+/, '')) + '</li>').join('');
      out.push({ tag: 'ul', inner: items, raw: true });
      continue;
    }
    if (/^!\[/.test(p)) { out.push({ tag: 'figure', inner: inline(p), raw: true }); continue; }
    // paragraf (baris dlm 1 blok digabung dgn <br>)
    out.push({ tag: 'p', inner: p.split('\n').map(inline).join('<br>') });
  }
  return out;
}

// Pasangkan ID + EN block-by-block → HTML dgn data-en
function bilingualBody(idMd, enMd) {
  const id = blocks(idMd);
  const en = blocks(enMd);
  return id.map((b, i) => {
    const e = en[i];
    if (b.tag === 'ul') {
      const da = e ? ' data-en="' + attrEsc('<ULRAW>') + '"' : '';
      // utk list, bungkus tiap li tidak praktis; render ul ID, EN via data-en di ul (innerHTML swap)
      const enInner = e ? attrEsc(e.inner) : '';
      return `<ul${e ? ' data-en="' + enInner + '"' : ''}>${b.inner}</ul>`;
    }
    if (b.tag === 'figure') return `<p>${b.inner}</p>`;
    const enAttr = e ? ' data-en="' + attrEsc(e.inner) + '"' : '';
    return `<${b.tag}${enAttr}>${b.inner}</${b.tag}>`;
  }).join('\n');
}

function fmtDate(d) {
  if (!d) return '';
  const dt = new Date(d);
  const idMon = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'];
  const enMon = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  return { id: `${dt.getDate()} ${idMon[dt.getMonth()]} ${dt.getFullYear()}`, en: `${enMon[dt.getMonth()]} ${dt.getDate()}, ${dt.getFullYear()}` };
}

// ---------- template ----------
function loadTemplate(baseFile) {
  const tpl = fs.readFileSync(baseFile, 'utf8').replace(/\r\n/g, '\n');
  const head = tpl.slice(0, tpl.indexOf('<div class="breadcrumb">'));
  const socialIdx = tpl.indexOf('<div style="display:flex;gap:12px;justify-content:center;align-items:center;padding:40px 0 48px');
  const tail = tpl.slice(socialIdx);
  return { head, tail };
}

function buildPage(kind, data) {
  const base = kind === 'artikel' ? 'artikel-1.html' : 'berita-1.html';
  const { head, tail } = loadTemplate(base);
  const listPage = kind === 'artikel' ? 'artikel.html' : 'berita.html';
  const listLabelId = kind === 'artikel' ? 'Artikel' : 'Berita';
  const listLabelEn = kind === 'artikel' ? 'Articles' : 'News';
  const backId = kind === 'artikel' ? '← Kembali ke Artikel' : '← Kembali ke Berita';
  const backEn = kind === 'artikel' ? '← Back to Articles' : '← Back to News';
  const d = fmtDate(data.date);

  // ganti <title>
  let h = head.replace(/<title>[\s\S]*?<\/title>/, `<title>${esc(data.title)} - Pinus Packindo</title>`);

  const titleEn = data.title_en || data.title;
  const catEn = data.category_en || data.category;

  const body = `<div class="breadcrumb">
  <a href="index.html" data-en="Home">Beranda</a><span>›</span>
  <a href="${listPage}" data-en="${listLabelEn}">${listLabelId}</a><span>›</span>
  <strong data-en="${attrEsc(titleEn)}">${esc(data.title)}</strong>
</div>

<div class="article-hero">
  <div class="article-hero-tag" data-en="${attrEsc(catEn)}">${esc(data.category)}</div>
  <h1 data-en="${attrEsc(titleEn)}">${esc(data.title)}</h1>
  <div class="article-hero-meta">
    <span class="meta-badge" data-en="${attrEsc(catEn)}">${esc(data.category)}</span>
    <span class="meta-text" data-en="📅 ${attrEsc(d.en)}">📅 ${esc(d.id)}</span>
    <span class="meta-text" data-en="✍️ Pinus Packindo Team">✍️ Tim Pinus Packindo</span>
    <span class="meta-text">🔗 pinuspackindo.com</span>
  </div>
</div>

<div class="article-main">
    <a class="article-back" href="${listPage}" data-en="${backEn}">${backId}</a>
  ${data.cover ? `<div style="width:100%;border-radius:16px;overflow:hidden;margin-bottom:36px;box-shadow:0 4px 24px rgba(0,0,0,0.1);">
    <img src="${attrEsc(data.cover)}" alt="${attrEsc(data.title)}" style="width:100%;display:block;max-height:480px;object-fit:cover;">
  </div>` : ''}
  <div class="article-content">
${bilingualBody(data.body, data.body_en)}
  </div>
  <hr class="article-divider">
  <div class="author-box">
    <div class="author-avatar-lg">PP</div>
    <div class="author-info">
      <h4 data-en="Pinus Packindo Team">Tim Pinus Packindo</h4>
      <p data-en="Published on ${attrEsc(d.en)} · Source: pinuspackindo.com">Diterbitkan pada ${esc(d.id)} · Sumber: pinuspackindo.com</p>
    </div>
  </div>
</div>

`;
  return h + body + tail;
}

// ---------- scan & generate ----------
function scan(dir, kind) {
  const items = [];
  if (!fs.existsSync(dir)) return items;
  for (const f of fs.readdirSync(dir)) {
    if (!f.endsWith('.md')) continue;
    const { fm, body } = parseMd(fs.readFileSync(path.join(dir, f), 'utf8'));
    const slug = f.replace(/\.md$/, '');
    items.push({ slug, kind, fm, body });
  }
  return items;
}

function cardHtml(kind, data, page) {
  const d = fmtDate(data.date);
  const titleEn = data.title_en || data.title;
  const catEn = data.category_en || data.category;
  const sumEn = data.summary_en || data.summary;
  return `<div class="article-card">
      <div class="article-img"><img src="${attrEsc(data.cover)}" alt="${attrEsc(data.title)}" loading="lazy" style="width:100%;height:100%;object-fit:cover;"></div>
      <div class="article-body">
        <div class="article-meta">
          <span class="article-cat" data-en="${attrEsc(catEn)}">${esc(data.category)}</span>
          <span class="article-date" data-en="${attrEsc(d.en)}">${esc(d.id)}</span>
        </div>
        <h3 data-en="${attrEsc(titleEn)}">${esc(data.title)}</h3>
        <p data-en="${attrEsc(sumEn)}">${esc(data.summary || '')}</p>
        <div class="article-footer">
          <div class="article-author"><div class="author-avatar">PP</div><div><div class="author-name">Tim Pinus</div><div style="font-size:10px;color:#aaa;">Pinus Packindo</div></div></div>
          <button class="btn-read" onclick="location.href='${page}'" data-en="Read More">Baca Selengkapnya</button>
        </div>
      </div>
    </div>`;
}

// Registry artikel/berita LAMA (hand-coded) untuk slider homepage "5 terbaru"
const LEGACY_A = [
  { page:'artikel-1.html', img:'images/ma-0001.png', cat:'Tips Kemasan', catEn:'Packaging Tips', date:'2026-06-12', title:'5 Tips Memilih Kemasan yang Tepat untuk Produk Makanan Anda', titleEn:'5 Tips for Choosing the Right Packaging for Your Food Products', sum:'Kemasan yang tepat bukan hanya melindungi produk, tapi juga media promosi bisnis Anda.', sumEn:'The right packaging not only protects your product but also markets your business.' },
  { page:'artikel-2.html', img:'images/ma-0002.png', cat:'Edukasi', catEn:'Education', date:'2026-06-05', title:'Perbedaan Kemasan Plastik Food Grade dan Non-Food Grade yang Wajib Diketahui', titleEn:'The Difference Between Food-Grade and Non-Food-Grade Plastic Packaging You Must Know', sum:'Tidak semua plastik aman untuk makanan. Kenali perbedaannya sebelum memilih.', sumEn:'Not all plastic is food-safe. Know the difference before choosing.' },
  { page:'artikel-3.html', img:'images/ma-0003.png', cat:'Tren', catEn:'Trends', date:'2026-05-28', title:'Tren Kemasan Ramah Lingkungan 2026 yang Wajib Diikuti Pelaku UMKM', titleEn:'2026 Eco-Friendly Packaging Trends Every SME Should Follow', sum:'Tren kemasan ramah lingkungan yang mendominasi pasar 2026.', sumEn:'Eco-friendly packaging trends dominating the 2026 market.' },
  { page:'artikel-4.html', img:'images/ma-0004.png', cat:'Panduan', catEn:'Guide', date:'2026-05-15', title:'Panduan Lengkap Memilih Box Kue untuk Usaha Bakery Rumahan', titleEn:'Complete Guide to Choosing Cake Boxes for Your Home Bakery Business', sum:'Panduan memilih box kue yang tepat untuk usaha bakery Anda.', sumEn:'A guide to choosing the right cake box for your bakery.' },
  { page:'artikel-5.html', img:'images/ma-0005.png', cat:'Tips Kemasan', catEn:'Packaging Tips', date:'2026-05-02', title:'Cara Menghitung Kebutuhan Kemasan untuk Bisnis F&B Anda', titleEn:'How to Calculate Packaging Needs for Your F&B Business', sum:'Hitung kebutuhan kemasan agar tidak kekurangan atau kelebihan stok.', sumEn:'Calculate packaging needs to avoid shortage or excess stock.' },
  { page:'artikel-6.html', img:'images/ma-0006.png', cat:'Edukasi', catEn:'Education', date:'2026-04-20', title:'Mengenal Jenis-jenis Kertas Roti dan Fungsinya dalam Dunia Baking', titleEn:'Getting to Know the Types of Baking Paper and Their Functions in Baking', sum:'Kenali jenis-jenis kertas roti dan fungsinya di dapur bakery.', sumEn:'Know the types of baking paper and their kitchen functions.' },
];
const LEGACY_B = [
  { page:'berita-5.html', img:'images/mb-0005.svg', cat:'🕗 Info Operasional', catEn:'🕗 Operational Info', date:'2026-06-12T12:00', title:'Pinus Packindo Buka Setiap Hari 08.00–21.00, Termasuk Libur Nasional!', titleEn:'Pinus Packindo Open Every Day 08.00–21.00, Including National Holidays!', sum:'Toko dan layanan buka setiap hari, termasuk hari libur nasional.', sumEn:'The store and services are open every day, including national holidays.' },
  { page:'berita-4.html', img:'images/mb-0004.svg', cat:'📉 Update Harga', catEn:'📉 Price Update', date:'2026-06-12T11:00', title:'Kabar Baik! Harga Bahan Baku Plastik Mulai Berangsur Turun', titleEn:'Good News! Plastic Raw Material Prices Begin to Gradually Fall', sum:'Harga bahan baku plastik mulai turun dari puncaknya.', sumEn:'Plastic raw material prices begin falling from their peak.' },
  { page:'berita-3.html', img:'images/mb-0003.svg', cat:'📢 Pernyataan Resmi', catEn:'📢 Official Statement', date:'2026-06-12T10:00', title:'Jangan Panik! Pinus Packindo Pastikan Stok Aman & Krisis Bersifat Sementara', titleEn:'Don\'t Panic! Pinus Packindo Ensures Stock Is Safe & the Crisis Is Temporary', sum:'Stok kemasan aman, krisis bersifat sementara.', sumEn:'Packaging stock is safe; the crisis is temporary.' },
  { page:'berita-2.html', img:'images/mb-0002.svg', cat:'Analisis Pasar', catEn:'Market Analysis', date:'2026-06-12T09:00', title:'Harga Kemasan Plastik Melonjak Hingga 78% Akibat Kelangkaan Bahan Baku', titleEn:'Plastic Packaging Prices Surge Up to 78% Due to Raw Material Shortage', sum:'Harga kemasan plastik melonjak hingga 78% akibat krisis bahan baku.', sumEn:'Plastic packaging prices surge up to 78% amid the raw material crisis.' },
  { page:'berita-1.html', img:'images/mb-0001.svg', cat:'Berita', catEn:'News', date:'2026-06-12T08:00', title:'Kelangkaan Bahan Baku Plastik Imbas Konflik Iran–Amerika Serikat', titleEn:'Plastic Resin Shortage Amid the Iran–United States Conflict', sum:'Pasokan petrokimia global terganggu akibat konflik Iran–AS.', sumEn:'Global petrochemical supply disrupted by the Iran–US conflict.' },
];

function sliderCard(it) {
  const d = fmtDate(it.date);
  return `<div class="aslide-card" onclick="location.href='${it.page}'">
          <div class="aslide-img"><img src="${attrEsc(it.img)}" alt="${attrEsc(it.title)}" loading="lazy" onerror="this.parentElement.classList.add('aslide-img-empty')"></div>
          <div class="aslide-body">
            <div class="aslide-meta"><span class="aslide-cat" data-en="${attrEsc(it.catEn)}">${esc(it.cat)}</span><span class="aslide-date" data-en="${attrEsc(d.en)}">${esc(d.id)}</span></div>
            <h3 data-en="${attrEsc(it.titleEn)}">${esc(it.title)}</h3>
            <p data-en="${attrEsc(it.sumEn)}">${esc(it.sum)}</p>
            <span class="aslide-read" data-en="Read More →">Baca Selengkapnya →</span>
          </div>
        </div>`;
}

function injectSlider(mark, items) {
  let s = fs.readFileSync('index.html', 'utf8');
  const re = new RegExp('<!--AUTO-' + mark + '-START-->[\\s\\S]*?<!--AUTO-' + mark + '-END-->');
  const html = items.map(sliderCard).join('\n        ');
  const block = '<!--AUTO-' + mark + '-START-->\n        ' + html + '\n        <!--AUTO-' + mark + '-END-->';
  if (re.test(s)) { s = s.replace(re, block); fs.writeFileSync('index.html', s); }
}

function injectCards(listFile, cardsHtml) {
  if (!fs.existsSync(listFile)) return;
  let s = fs.readFileSync(listFile, 'utf8');
  const re = /<!--AUTO-CARDS-START-->[\s\S]*?<!--AUTO-CARDS-END-->/;
  const block = '<!--AUTO-CARDS-START-->\n    ' + cardsHtml + '\n    <!--AUTO-CARDS-END-->';
  if (re.test(s)) { s = s.replace(re, block); fs.writeFileSync(listFile, s); }
}

function run() {
  const arts = scan('_artikel', 'artikel');
  const news = scan('_berita', 'berita');
  const cards = { artikel: [], berita: [] };
  const pool = { artikel: [], berita: [] };
  let gen = 0;
  // urutkan terbaru dulu
  const all = [...arts, ...news].sort((a, b) => new Date(b.fm.date || 0) - new Date(a.fm.date || 0));
  for (const it of all) {
    if (String(it.fm.legacy) === 'true') continue; // halaman lama, dilewati
    const kind = it.kind;
    const prefix = kind === 'artikel' ? 'ma' : 'mb';
    const ext = kind === 'artikel' ? 'png' : 'svg';
    const cover = it.fm.cover || (it.fm.kode ? `images/${prefix}-${it.fm.kode}.${ext}` : '');
    const data = {
      title: it.fm.title || 'Tanpa Judul',
      title_en: it.fm.title_en || '',
      category: it.fm.category || (kind === 'artikel' ? 'Artikel' : 'Berita'),
      category_en: it.fm.category_en || '',
      date: it.fm.date || '',
      summary: it.fm.summary || '',
      summary_en: it.fm.summary_en || '',
      cover,
      body: it.body || '',
      body_en: it.fm.body_en || '',
    };
    const out = `${kind}-${it.slug}.html`;
    fs.writeFileSync(out, buildPage(kind, data));
    cards[kind].push(cardHtml(kind, data, out));
    // entri utk slider homepage
    pool[kind].push({
      page: out, img: cover, cat: data.category, catEn: data.category_en || data.category,
      date: data.date, title: data.title, titleEn: data.title_en || data.title,
      sum: data.summary || '', sumEn: data.summary_en || data.summary || '',
    });
    gen++;
    console.log('  generated: ' + out);
  }
  injectCards('artikel.html', cards.artikel.join('\n    '));
  injectCards('berita.html', cards.berita.join('\n    '));

  // Slider homepage: gabung baru + lama, urut terbaru, ambil 5
  const byDateDesc = (a, b) => new Date(b.date) - new Date(a.date);
  const topA = [...pool.artikel, ...LEGACY_A].sort(byDateDesc).slice(0, 5);
  const topB = [...pool.berita, ...LEGACY_B].sort(byDateDesc).slice(0, 5);
  injectSlider('A', topA);
  injectSlider('B', topB);

  console.log(`build selesai: ${gen} halaman dibuat, listing & slider homepage diperbarui.`);
}
run();
