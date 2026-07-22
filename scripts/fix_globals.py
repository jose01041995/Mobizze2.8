import os
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Email fix
    content = content.replace('contato@mobizze.com', 'contact@mobizze.com')
    
    # 2. Footer worldwide text fix
    content = content.replace('Portugal · Worldwide', 'Portugal · World')
    
    # 3. Missing copyright fix (specifically in pt/agendar-reuniao.html and potentially others)
    # The document says: "Na página portuguesa de agendamento, o copyright aparece como: © Mobizze sem o ano 2026."
    content = content.replace('© Mobizze\n', '© 2026 Mobizze\n')
    content = content.replace('© Mobizze<', '© 2026 Mobizze<')
    
    # 4. AbsolutAI domain fix
    content = content.replace('absolutai.com', 'mobizze.com')
    content = content.replace('AbsolutAI', 'Mobizze')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    changed = 0
    for folder in ['en', 'pt']:
        files = glob.glob(f"{folder}/*.html")
        for f in files:
            if process_file(f):
                changed += 1
                print(f"Updated: {f}")
    print(f"Total files updated: {changed}")

if __name__ == "__main__":
    main()
