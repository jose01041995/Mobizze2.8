import os
import re

def replace_in_files(directory, old_str, new_str):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content.replace(old_str, new_str)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

if __name__ == '__main__':
    replace_in_files('pt', 'contato@mobizze.com', 'contact@mobizze.com')
    replace_in_files('en', 'contato@mobizze.com', 'contact@mobizze.com')
    replace_in_files('.', 'contato@mobizze.com', 'contact@mobizze.com')
    print("Email updated successfully!")
