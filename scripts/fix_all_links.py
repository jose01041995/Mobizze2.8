import os
import glob
import re

def process_file(filepath, is_pt):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    if is_pt:
        content = content.replace('href="chatbot.html"', 'href="agentes-conversacao.html"')
        content = content.replace('href="../en/chatbot.html"', 'href="../en/conversational-agents.html"')
        content = content.replace('href="agentes-de-texto.html"', 'href="ferramentas-personalizadas.html"')
        content = content.replace('href="../en/text-agents.html"', 'href="../en/custom-tools.html"')
        content = content.replace('Agentes de Texto', 'Ferramentas Personalizadas')
        content = content.replace('Chatbot', 'Agentes de Conversação')
    else:
        content = content.replace('href="chatbot.html"', 'href="conversational-agents.html"')
        content = content.replace('href="../pt/chatbot.html"', 'href="../pt/agentes-conversacao.html"')
        content = content.replace('href="text-agents.html"', 'href="custom-tools.html"')
        content = content.replace('href="../pt/agentes-de-texto.html"', 'href="../pt/ferramentas-personalizadas.html"')
        content = content.replace('Text Agents', 'Custom Tools')
        # Chatbot is tricky because it could be capitalized
        # Be careful not to replace it if it's already Conversational Agents
        content = re.sub(r'>\s*Chatbot\s*<', '> Conversational Agents <', content)
        content = re.sub(r'"Chatbot"', '"Conversational Agents"', content)

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
            if process_file(f, is_pt=(folder=='pt')):
                changed += 1
                print(f"Updated links in: {f}")
    print(f"Total files updated: {changed}")

if __name__ == "__main__":
    main()
