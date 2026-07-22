import os
import glob
import re

directories = ['pt', 'en']

replacements = [
    # PT
    (r'(<a href="termos\.html".*?>Termos</a>)', r'\1\n                    <a href="seguranca.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Segurança</a>'),
    # EN
    (r'(<a href="terms\.html".*?>Terms</a>)', r'\1\n                    <a href="security.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Security</a>')
]

for d in directories:
    for filepath in glob.glob(f'{d}/**/*.html', recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        for old, new in replacements:
            content = re.sub(old, new, content)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filepath}')

print("Added security links.")
