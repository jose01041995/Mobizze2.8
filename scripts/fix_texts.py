import os
import glob
import re

for filepath in glob.glob('en/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Worldwidewide
    content = re.sub(r'Worldwidewide', 'Worldwide', content)
    # Fix Copyright
    content = re.sub(r'&copy;.*?<\/p>', r'&copy; 2026 <span class="font-display font-bold text-slate-600">Mobizze</span>. All rights reserved.</p>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob('pt/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Worldwidewide
    content = re.sub(r'Worldwidewide', 'Mundo', content)
    # Fix Copyright
    content = re.sub(r'&copy;.*?<\/p>', r'&copy; 2026 <span class="font-display font-bold text-slate-600">Mobizze</span>. Todos os direitos reservados.</p>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Texts fixed.")
