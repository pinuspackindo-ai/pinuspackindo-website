files = ['index.html', 'about.html', 'products.html', 'contact.html']

linkedin = '''  <a href="https://www.linkedin.com/company/cv-pinus-packindo/" target="_blank" aria-label="LinkedIn"
     style="width:36px;height:36px;border-radius:8px;background:#f0f0f0;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;flex-shrink:0;overflow:hidden;transition:background 0.2s;"
     onmouseover="this.style.background='#27ae60';this.querySelector('svg').style.fill='#fff'"
     onmouseout="this.style.background='#f0f0f0';this.querySelector('svg').style.fill='#555'">
    <svg width="18" height="18" viewBox="0 0 24 24" style="fill:#555;flex-shrink:0;" xmlns="http://www.w3.org/2000/svg"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
  </a>
</div>'''

# Insert before closing </div> of the social strip
old = '''  </a>
</div>

<!-- FOOTER -->'''

new = linkedin + '\n\n<!-- FOOTER -->'

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f: html = f.read()
        if 'linkedin' in html:
            print(f'{fname} already has LinkedIn'); continue
        # Find the Facebook closing </a> followed by </div> before FOOTER
        if old in html:
            html = html.replace(old, new)
            with open(fname, 'w', encoding='utf-8') as f: f.write(html)
            print(f'{fname} updated')
        else:
            print(f'{fname} pattern not found')
    except Exception as e:
        print(f'{fname} ERROR: {e}')
