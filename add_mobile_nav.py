import os, re

# ── CSS to inject (mobile hamburger) ─────────────────────────────────────────
MOBILE_CSS = """
/* ── HAMBURGER MOBILE NAV ── */
.hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 40px;
  height: 40px;
  cursor: pointer;
  background: none;
  border: 1.5px solid #e5e5e5;
  border-radius: 8px;
  padding: 8px;
  transition: border-color 0.2s;
  flex-shrink: 0;
}
.hamburger:hover { border-color: #27ae60; }
.hamburger span {
  display: block;
  width: 100%;
  height: 2px;
  background: #333;
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s, background 0.2s;
  transform-origin: center;
}
.hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); background: #27ae60; }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); background: #27ae60; }

/* Mobile dropdown menu */
.mobile-menu {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  z-index: 99;
  pointer-events: none;
}
.mobile-menu.open {
  display: block;
  pointer-events: auto;
}
.mobile-menu-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.35);
  backdrop-filter: blur(2px);
}
.mobile-menu-panel {
  position: absolute;
  top: 0; right: 0;
  width: 280px;
  height: 100%;
  background: #fff;
  box-shadow: -4px 0 24px rgba(0,0,0,0.12);
  display: flex;
  flex-direction: column;
  padding: 0;
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.4,0,0.2,1);
}
.mobile-menu.open .mobile-menu-panel {
  transform: translateX(0);
}
.mobile-menu-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 18px 20px;
  border-bottom: 1px solid #f0f0f0;
}
.mobile-menu-brand {
  font-weight: 800;
  font-size: 16px;
  color: #27ae60;
}
.mobile-menu-close {
  width: 32px; height: 32px;
  display: flex; align-items: center; justify-content: center;
  border: none; background: #f5f5f5;
  border-radius: 8px;
  cursor: pointer;
  font-size: 18px;
  color: #555;
  transition: background 0.2s, color 0.2s;
}
.mobile-menu-close:hover { background: #27ae60; color: #fff; }
.mobile-menu-links {
  display: flex;
  flex-direction: column;
  padding: 12px 0;
  flex: 1;
  overflow-y: auto;
}
.mobile-menu-links a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 20px;
  font-size: 15px;
  font-weight: 600;
  color: #333;
  text-decoration: none;
  border-bottom: 1px solid #f8f8f8;
  transition: background 0.15s, color 0.15s;
}
.mobile-menu-links a:hover,
.mobile-menu-links a.active { background: #f0fdf4; color: #27ae60; }
.mobile-menu-links a .nav-icon { font-size: 18px; width: 24px; text-align: center; }
.mobile-menu-footer {
  padding: 16px 20px;
  border-top: 1px solid #f0f0f0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.mobile-lang-row {
  display: flex;
  gap: 8px;
}
.mobile-lang-btn {
  flex: 1;
  padding: 8px;
  border-radius: 8px;
  border: 1.5px solid #ddd;
  background: #fff;
  font-size: 13px;
  font-weight: 700;
  color: #666;
  cursor: pointer;
  transition: all 0.2s;
  text-align: center;
}
.mobile-lang-btn.active,
.mobile-lang-btn:hover { background: #27ae60; color: #fff; border-color: #27ae60; }
.mobile-cta-btn {
  display: block;
  background: #27ae60;
  color: #fff;
  text-align: center;
  padding: 12px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  transition: background 0.2s;
}
.mobile-cta-btn:hover { background: #1e8449; }

@media (max-width: 900px) {
  nav { padding: 12px 20px; }
  .nav-links { display: none !important; }
  .nav-right .btn-quote { display: none; }
  .nav-right .lang-switcher { display: none; }
  .hamburger { display: flex; }
}
@media (max-width: 600px) {
  .logo-name { font-size: 17px; }
  .logo-icon { width: 44px; height: 44px; }
}
"""

# ── Mobile menu HTML to inject just before </nav> ─────────────────────────────
HAMBURGER_BTN = '  <button class="hamburger" id="hamburgerBtn" onclick="toggleMobileMenu()" aria-label="Menu">\n    <span></span><span></span><span></span>\n  </button>'

def mobile_menu_html(active_page):
    pages = [
        ("index.html", "🏠", "Beranda", "nav.home"),
        ("about.html", "ℹ️", "Tentang Kami", "nav.about"),
        ("products.html", "📦", "Produk", "nav.products"),
        ("artikel.html", "📝", "Artikel", "nav.artikel"),
        ("berita.html", "📰", "Berita & Acara", "nav.berita"),
        ("contact.html", "📞", "Kontak", "nav.contact"),
    ]
    links = ""
    for href, icon, label, i18n in pages:
        active_class = ' class="active"' if href == active_page else ''
        links += f'    <a href="{href}"{active_class} data-i18n="{i18n}"><span class="nav-icon">{icon}</span>{label}</a>\n'

    return f"""
<!-- MOBILE MENU -->
<div class="mobile-menu" id="mobileMenu">
  <div class="mobile-menu-overlay" onclick="toggleMobileMenu()"></div>
  <div class="mobile-menu-panel">
    <div class="mobile-menu-header">
      <span class="mobile-menu-brand">Pinus Packindo</span>
      <button class="mobile-menu-close" onclick="toggleMobileMenu()">✕</button>
    </div>
    <div class="mobile-menu-links">
{links}    </div>
    <div class="mobile-menu-footer">
      <div class="mobile-lang-row">
        <button class="mobile-lang-btn active" id="mobileLangID" onclick="switchLang('id')">🇮🇩 ID</button>
        <button class="mobile-lang-btn" id="mobileLangEN" onclick="switchLang('en')">🇬🇧 EN</button>
      </div>
      <a href="contact.html" class="mobile-cta-btn" data-i18n="nav.cta">Hubungi Kami</a>
    </div>
  </div>
</div>"""

# ── JS to inject before </body> ───────────────────────────────────────────────
MOBILE_JS = """
/* Mobile menu toggle */
function toggleMobileMenu() {
  const menu = document.getElementById('mobileMenu');
  const btn  = document.getElementById('hamburgerBtn');
  if (!menu || !btn) return;
  const isOpen = menu.classList.toggle('open');
  btn.classList.toggle('open', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
}
/* Sync lang buttons in mobile menu */
(function syncMobileLang(){
  const lang = localStorage.getItem('lang') || 'id';
  const bid = document.getElementById('mobileLangID');
  const ben = document.getElementById('mobileLangEN');
  if (bid && ben) {
    bid.classList.toggle('active', lang === 'id');
    ben.classList.toggle('active', lang === 'en');
  }
})();
"""

# ── Detect which page each file represents ───────────────────────────────────
def active_for(filename):
    name = os.path.basename(filename)
    if name == 'index.html': return 'index.html'
    if name.startswith('about'): return 'about.html'
    if name.startswith('product'): return 'products.html'
    if name.startswith('artikel'): return 'artikel.html'
    if name.startswith('berita'): return 'berita.html'
    if name.startswith('contact'): return 'contact.html'
    return 'index.html'

# ── Process all HTML files ────────────────────────────────────────────────────
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
changed = 0

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already patched
    if 'hamburger' in html:
        print(f'  [skip] {fname} already has hamburger')
        continue

    # 1. Inject mobile CSS before </style>
    if '</style>' in html:
        html = html.replace('</style>', MOBILE_CSS + '\n</style>', 1)

    # 2. Add hamburger button inside <nav> before </nav>
    if '</nav>' in html:
        html = html.replace('</nav>', HAMBURGER_BTN + '\n</nav>', 1)

    # 3. Inject mobile menu HTML after </nav>
    if '</nav>' in html:
        active = active_for(fname)
        html = html.replace('</nav>', '</nav>' + mobile_menu_html(active), 1)

    # 4. Inject mobile JS before </body>
    # Find the last <script> block before </body> and append inside it,
    # or just inject a <script> tag before </body>
    if '</body>' in html:
        script_tag = f'\n<script>\n{MOBILE_JS}\n</script>\n'
        html = html.replace('</body>', script_tag + '</body>', 1)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  [ok] {fname}')
    changed += 1

print(f'\nDone. {changed} files updated.')
