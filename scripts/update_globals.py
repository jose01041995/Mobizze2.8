import os
import re

def main():
    pt_content = open('pt/index.html', 'r', encoding='utf-8').read()
    en_content = open('en/index.html', 'r', encoding='utf-8').read()
    
    pt_nav = re.search(r'(<nav id="navbar".*?</nav>)', pt_content, re.DOTALL | re.IGNORECASE).group(1)
    pt_mobile = re.search(r'(<div id="mobile-menu".*?)\s*<main>', pt_content, re.DOTALL | re.IGNORECASE).group(1)
    pt_footer = re.search(r'(<footer.*?</footer>)', pt_content, re.DOTALL | re.IGNORECASE).group(1)
    
    en_nav = re.search(r'(<nav id="navbar".*?</nav>)', en_content, re.DOTALL | re.IGNORECASE).group(1)
    en_mobile = re.search(r'(<div id="mobile-menu".*?)\s*<main>', en_content, re.DOTALL | re.IGNORECASE).group(1)
    en_footer = re.search(r'(<footer.*?</footer>)', en_content, re.DOTALL | re.IGNORECASE).group(1)
    
    en_footer = en_footer.replace('Portugal · World\n', 'Portugal · Worldwide\n')
    en_footer = en_footer.replace('Portugal · World<', 'Portugal · Worldwide<')
    
    for root, dirs, files in os.walk('.'):
        if 'dist' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if filepath == './pt/index.html' or filepath == './en/index.html':
                    continue
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '/pt/' in filepath or filepath.startswith('./pt/') or filepath == './index.html':
                    content = re.sub(r'<nav id="navbar".*?</nav>', pt_nav.replace('\\', '\\\\'), content, flags=re.DOTALL | re.IGNORECASE)
                    content = re.sub(r'<div id="mobile-menu".*?\s*<main>', pt_mobile.replace('\\', '\\\\') + '\n\n    <main>', content, flags=re.DOTALL | re.IGNORECASE)
                    content = re.sub(r'<footer.*?</footer>', pt_footer.replace('\\', '\\\\'), content, flags=re.DOTALL | re.IGNORECASE)
                elif '/en/' in filepath or filepath.startswith('./en/'):
                    content = re.sub(r'<nav id="navbar".*?</nav>', en_nav.replace('\\', '\\\\'), content, flags=re.DOTALL | re.IGNORECASE)
                    content = re.sub(r'<div id="mobile-menu".*?\s*<main>', en_mobile.replace('\\', '\\\\') + '\n\n    <main>', content, flags=re.DOTALL | re.IGNORECASE)
                    content = re.sub(r'<footer.*?</footer>', en_footer.replace('\\', '\\\\'), content, flags=re.DOTALL | re.IGNORECASE)
                    
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
    with open('en/index.html', 'w', encoding='utf-8') as f:
        content = en_content
        content = re.sub(r'<footer.*?</footer>', en_footer.replace('\\', '\\\\'), content, flags=re.DOTALL | re.IGNORECASE)
        f.write(content)
        
    print("Globals updated successfully!")

if __name__ == "__main__":
    main()
