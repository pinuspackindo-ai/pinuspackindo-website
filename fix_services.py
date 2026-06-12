import re, json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Fix CSS: remove white card background/shadow, restore transparent card ──
old_css = """.service-card {
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
}"""

new_css = """.service-card {
  flex-shrink: 0;
  width: calc((100% - 48px) / 3);
  background: transparent;
  display: flex; flex-direction: column;
  transition: transform 0.2s;
}
.service-card:hover { transform: translateY(-4px); }
.service-card-icon {
  height: 200px; display: flex; align-items: center; justify-content: center;
  border-radius: 16px; overflow: hidden;
  transition: transform 0.3s ease;
}
.service-card:hover .service-card-icon { transform: scale(1.03); }
.service-card-icon svg { width: 72px; height: 72px; stroke: rgba(255,255,255,0.95); fill: none; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.service-card-body { padding: 16px 4px; display: flex; flex-direction: column; flex: 1; }
.service-card-body h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; color: #111; }
.service-card-body p { font-size: 13px; color: #666; line-height: 1.6; margin-bottom: 16px; flex: 1; }"""

html = html.replace(old_css, new_css)

# ── 2. Replace each card's prod-tags section with a plain <p> description ──
card_descs = {
    'c1': ('c1_desc', 'Berbagai kemasan plastik untuk kebutuhan makanan & minuman: gelas, piring, mika, botol, kantong, standing pouch, thinwall, vacuum bag, toples, sedotan, dan shopping bag.'),
    'c2': ('c2_desc', 'Kemasan berbahan kertas ramah lingkungan: gelas kertas, box makanan, mangkok, paper bag, kemasan nasi, snack, kue, dan kertas roti.'),
    'c3': ('c3_desc', 'Aneka kemasan styrofoam untuk makanan: box, piring, mangkok, ice box, tray buah, hingga kemasan daging dan sayuran segar.'),
    'c4': ('c4_desc', 'Peralatan lengkap untuk membuat kue & roti: pengocok telur, timbangan, cetakan, spuit, alas adonan, botol saus, loyang, dan mixer.'),
    'c5': ('c5_desc', 'Bahan-bahan berkualitas untuk membuat kue: tepung, gula, susu, obat kue, coklat, topping, pewarna makanan, dan berbagai essens.'),
    'c6': ('c6_desc', 'Berbagai pilihan makanan siap saji dan minuman kemasan: snack, makanan ringan, kue & roti, serta minuman dalam berbagai varian.'),
    'c7': ('c7_desc', 'Perlengkapan pendukung lainnya: isolasi, staples, spunbond, alat kayu, tusuk sate & cilok, tissue, dan bubble wrap.'),
}

for key, (i18n_key, desc_text) in card_descs.items():
    # Find and replace prod-tags block in each card
    # Each card has data-i18n="services.cX_title" followed by prod-tags
    old_tags_pattern = f'data-i18n="services.{key}_title">[^<]*</h3>\n          <div class="prod-tags">'

    # Replace the entire prod-tags div (find by surrounding context)
    title_key = f'{key}_title'
    # Build the replacement: find prod-tags div and replace with <p>
    pass

# Do targeted string replacements for each card's prod-tags
replacements = [
    # Card 1
    (
        '''          <div class="prod-tags">
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
          </div>''',
        '          <p data-i18n="services.c1_desc">Berbagai kemasan plastik untuk kebutuhan makanan & minuman: gelas, piring, mika, botol, kantong, standing pouch, thinwall, vacuum bag, toples, sedotan, dan shopping bag.</p>'
    ),
    # Card 2
    (
        '''          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c2_t1">Gelas Kertas</span>
            <span class="prod-tag" data-i18n="services.c2_t2">Box Makanan</span>
            <span class="prod-tag" data-i18n="services.c2_t3">Mangkok Kertas</span>
            <span class="prod-tag" data-i18n="services.c2_t4">Paper Bag</span>
            <span class="prod-tag" data-i18n="services.c2_t5">Kemasan Nasi</span>
            <span class="prod-tag" data-i18n="services.c2_t6">Kemasan Snack</span>
            <span class="prod-tag" data-i18n="services.c2_t7">Kemasan Kue</span>
            <span class="prod-tag" data-i18n="services.c2_t8">Kertas Roti</span>
          </div>''',
        '          <p data-i18n="services.c2_desc">Kemasan berbahan kertas ramah lingkungan: gelas kertas, box makanan, mangkok, paper bag, kemasan nasi, snack, kue, dan kertas roti.</p>'
    ),
    # Card 3
    (
        '''          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c3_t1">Box Styrofoam</span>
            <span class="prod-tag" data-i18n="services.c3_t2">Piring Foam</span>
            <span class="prod-tag" data-i18n="services.c3_t3">Mangkok Foam</span>
            <span class="prod-tag" data-i18n="services.c3_t4">Ice Box</span>
            <span class="prod-tag" data-i18n="services.c3_t5">Tray Buah</span>
            <span class="prod-tag" data-i18n="services.c3_t6">Kemasan Daging</span>
          </div>''',
        '          <p data-i18n="services.c3_desc">Aneka kemasan styrofoam untuk makanan: box, piring, mangkok, ice box, tray buah, hingga kemasan daging dan sayuran segar.</p>'
    ),
    # Card 4
    (
        '''          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c4_t1">Pengocok Telur</span>
            <span class="prod-tag" data-i18n="services.c4_t2">Timbangan</span>
            <span class="prod-tag" data-i18n="services.c4_t3">Cetakan Kue</span>
            <span class="prod-tag" data-i18n="services.c4_t4">Spuit</span>
            <span class="prod-tag" data-i18n="services.c4_t5">Alas Adonan</span>
            <span class="prod-tag" data-i18n="services.c4_t6">Botol Saus</span>
            <span class="prod-tag" data-i18n="services.c4_t7">Loyang</span>
            <span class="prod-tag" data-i18n="services.c4_t8">Mixer</span>
          </div>''',
        '          <p data-i18n="services.c4_desc">Peralatan lengkap untuk membuat kue & roti: pengocok telur, timbangan, cetakan, spuit, alas adonan, botol saus, loyang, dan mixer.</p>'
    ),
    # Card 5
    (
        '''          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c5_t1">Tepung</span>
            <span class="prod-tag" data-i18n="services.c5_t2">Gula</span>
            <span class="prod-tag" data-i18n="services.c5_t3">Susu</span>
            <span class="prod-tag" data-i18n="services.c5_t4">Obat Kue</span>
            <span class="prod-tag" data-i18n="services.c5_t5">Coklat</span>
            <span class="prod-tag" data-i18n="services.c5_t6">Topping</span>
            <span class="prod-tag" data-i18n="services.c5_t7">Pewarna</span>
            <span class="prod-tag" data-i18n="services.c5_t8">Essens</span>
          </div>''',
        '          <p data-i18n="services.c5_desc">Bahan-bahan berkualitas untuk membuat kue: tepung, gula, susu, obat kue, coklat, topping, pewarna makanan, dan berbagai essens.</p>'
    ),
    # Card 6
    (
        '''          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c6_t1">Snack</span>
            <span class="prod-tag" data-i18n="services.c6_t2">Minuman Kemasan</span>
            <span class="prod-tag" data-i18n="services.c6_t3">Makanan Ringan</span>
            <span class="prod-tag" data-i18n="services.c6_t4">Kue & Roti</span>
          </div>''',
        '          <p data-i18n="services.c6_desc">Berbagai pilihan makanan siap saji dan minuman kemasan: snack, makanan ringan, kue & roti, serta minuman dalam berbagai varian.</p>'
    ),
    # Card 7
    (
        '''          <div class="prod-tags">
            <span class="prod-tag" data-i18n="services.c7_t1">Isolasi</span>
            <span class="prod-tag" data-i18n="services.c7_t2">Staples</span>
            <span class="prod-tag" data-i18n="services.c7_t3">Spunbond</span>
            <span class="prod-tag" data-i18n="services.c7_t4">Alat Kayu</span>
            <span class="prod-tag" data-i18n="services.c7_t5">Tusuk Sate</span>
            <span class="prod-tag" data-i18n="services.c7_t6">Tissue</span>
            <span class="prod-tag" data-i18n="services.c7_t7">Bubble Wrap</span>
          </div>''',
        '          <p data-i18n="services.c7_desc">Perlengkapan pendukung lainnya: isolasi, staples, spunbond, alat kayu, tusuk sate & cilok, tissue, dan bubble wrap.</p>'
    ),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"  Replaced tags → desc")
    else:
        print(f"  NOT FOUND: {old[:60]}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html saved")

# ── 3. Update JSON: add desc keys ──
id_descs = {
    "c1_desc": "Berbagai kemasan plastik untuk kebutuhan makanan & minuman: gelas, piring, mika, botol, kantong, standing pouch, thinwall, vacuum bag, toples, sedotan, dan shopping bag.",
    "c2_desc": "Kemasan berbahan kertas ramah lingkungan: gelas kertas, box makanan, mangkok, paper bag, kemasan nasi, snack, kue, dan kertas roti.",
    "c3_desc": "Aneka kemasan styrofoam untuk makanan: box, piring, mangkok, ice box, tray buah, hingga kemasan daging dan sayuran segar.",
    "c4_desc": "Peralatan lengkap untuk membuat kue & roti: pengocok telur, timbangan, cetakan, spuit, alas adonan, botol saus, loyang, dan mixer.",
    "c5_desc": "Bahan-bahan berkualitas untuk membuat kue: tepung, gula, susu, obat kue, coklat, topping, pewarna makanan, dan berbagai essens.",
    "c6_desc": "Berbagai pilihan makanan siap saji dan minuman kemasan: snack, makanan ringan, kue & roti, serta minuman dalam berbagai varian.",
    "c7_desc": "Perlengkapan pendukung lainnya: isolasi, staples, spunbond, alat kayu, tusuk sate & cilok, tissue, dan bubble wrap.",
}
en_descs = {
    "c1_desc": "Various plastic packaging for food & beverage needs: cups, plates, acrylic boxes, bottles, plastic bags, standing pouches, thinwall, vacuum bags, jars, straws, and shopping bags.",
    "c2_desc": "Eco-friendly paper packaging: paper cups, food boxes, bowls, paper bags, rice packaging, snack packaging, cake boxes, and bread paper.",
    "c3_desc": "Various styrofoam packaging for food: boxes, plates, bowls, ice boxes, fruit trays, and meat & vegetable packaging.",
    "c4_desc": "Complete equipment for baking: egg beater, scale, cake molds, piping tips, dough mat, sauce bottles, baking pans, and mixer.",
    "c5_desc": "Quality baking ingredients: flour, sugar, milk, baking agents, chocolate, toppings, food coloring, and various essences.",
    "c6_desc": "Various ready-to-eat food and packaged beverages: snacks, light food, cakes & bread, and beverages in various variants.",
    "c7_desc": "Other supporting supplies: tape, staples, spunbond, wooden utensils, skewers, tissue, and bubble wrap.",
}

with open('lang/id.json','r',encoding='utf-8') as f: id_data = json.load(f)
id_data['services'].update(id_descs)
with open('lang/id.json','w',encoding='utf-8') as f: json.dump(id_data,f,ensure_ascii=False,indent=2)

with open('lang/en.json','r',encoding='utf-8') as f: en_data = json.load(f)
en_data['services'].update(en_descs)
with open('lang/en.json','w',encoding='utf-8') as f: json.dump(en_data,f,ensure_ascii=False,indent=2)

print("JSON updated with descriptions")
