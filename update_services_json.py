import json

cats = {
  "c1_title": "Kemasan Plastik",
  "c1_t1":"Gelas & Tutup","c1_t2":"Piring Plastik","c1_t3":"Mika","c1_t4":"Botol",
  "c1_t5":"Kantong Plastik","c1_t6":"Trashbag","c1_t7":"Standing Pouch","c1_t8":"Thinwall",
  "c1_t9":"Vacuum Bag","c1_t10":"Toples","c1_t11":"Sedotan","c1_t12":"Shopping Bag",

  "c2_title": "Kemasan Kertas",
  "c2_t1":"Gelas Kertas","c2_t2":"Box Makanan","c2_t3":"Mangkok Kertas","c2_t4":"Paper Bag",
  "c2_t5":"Kemasan Nasi","c2_t6":"Kemasan Snack","c2_t7":"Kemasan Kue","c2_t8":"Kertas Roti",

  "c3_title": "Kemasan Styrofoam",
  "c3_t1":"Box Styrofoam","c3_t2":"Piring Foam","c3_t3":"Mangkok Foam",
  "c3_t4":"Ice Box","c3_t5":"Tray Buah","c3_t6":"Kemasan Daging",

  "c4_title": "Peralatan Baking",
  "c4_t1":"Pengocok Telur","c4_t2":"Timbangan","c4_t3":"Cetakan Kue","c4_t4":"Spuit",
  "c4_t5":"Alas Adonan","c4_t6":"Botol Saus","c4_t7":"Loyang","c4_t8":"Mixer",

  "c5_title": "Bahan Baking",
  "c5_t1":"Tepung","c5_t2":"Gula","c5_t3":"Susu","c5_t4":"Obat Kue",
  "c5_t5":"Coklat","c5_t6":"Topping","c5_t7":"Pewarna","c5_t8":"Essens",

  "c6_title": "Makanan & Minuman",
  "c6_t1":"Snack","c6_t2":"Minuman Kemasan","c6_t3":"Makanan Ringan","c6_t4":"Kue & Roti",

  "c7_title": "Lain-Lain",
  "c7_t1":"Isolasi","c7_t2":"Staples","c7_t3":"Spunbond",
  "c7_t4":"Alat Kayu","c7_t5":"Tusuk Sate","c7_t6":"Tissue","c7_t7":"Bubble Wrap",
}

cats_en = {
  "c1_title": "Plastic Packaging",
  "c1_t1":"Cups & Lids","c1_t2":"Plastic Plates","c1_t3":"Acrylic Boxes","c1_t4":"Bottles",
  "c1_t5":"Plastic Bags","c1_t6":"Trash Bags","c1_t7":"Standing Pouches","c1_t8":"Thinwall",
  "c1_t9":"Vacuum Bags","c1_t10":"Jars","c1_t11":"Straws","c1_t12":"Shopping Bags",

  "c2_title": "Paper Packaging",
  "c2_t1":"Paper Cups","c2_t2":"Food Boxes","c2_t3":"Paper Bowls","c2_t4":"Paper Bags",
  "c2_t5":"Rice Packaging","c2_t6":"Snack Packaging","c2_t7":"Cake Boxes","c2_t8":"Bread Paper",

  "c3_title": "Styrofoam Packaging",
  "c3_t1":"Styrofoam Boxes","c3_t2":"Foam Plates","c3_t3":"Foam Bowls",
  "c3_t4":"Ice Boxes","c3_t5":"Fruit Trays","c3_t6":"Meat Packaging",

  "c4_title": "Baking Equipment",
  "c4_t1":"Egg Beater","c4_t2":"Scale","c4_t3":"Cake Molds","c4_t4":"Piping Tips",
  "c4_t5":"Dough Mat","c4_t6":"Sauce Bottle","c4_t7":"Baking Pan","c4_t8":"Mixer",

  "c5_title": "Baking Ingredients",
  "c5_t1":"Flour","c5_t2":"Sugar","c5_t3":"Milk","c5_t4":"Baking Agents",
  "c5_t5":"Chocolate","c5_t6":"Toppings","c5_t7":"Food Coloring","c5_t8":"Essence",

  "c6_title": "Food & Beverages",
  "c6_t1":"Snacks","c6_t2":"Packaged Drinks","c6_t3":"Light Snacks","c6_t4":"Cakes & Bread",

  "c7_title": "Others",
  "c7_t1":"Tape","c7_t2":"Staples","c7_t3":"Spunbond",
  "c7_t4":"Wooden Utensils","c7_t5":"Skewers","c7_t6":"Tissue","c7_t7":"Bubble Wrap",
}

# Update id.json
with open('lang/id.json','r',encoding='utf-8') as f: id_data = json.load(f)
id_data['services'].update(cats)
with open('lang/id.json','w',encoding='utf-8') as f: json.dump(id_data,f,ensure_ascii=False,indent=2)
print("id.json updated")

# Update en.json
with open('lang/en.json','r',encoding='utf-8') as f: en_data = json.load(f)
en_data['services'].update(cats_en)
with open('lang/en.json','w',encoding='utf-8') as f: json.dump(en_data,f,ensure_ascii=False,indent=2)
print("en.json updated")
