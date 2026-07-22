import os
import shutil

def update_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"Warning: Could not find '{old[:50]}...' in {path}")
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. PT: Chatbot -> Agentes de Conversação
shutil.move('pt/chatbot.html', 'pt/agentes-conversacao.html')
update_file('pt/agentes-conversacao.html', [
    ('<title>Chatbots com IA', '<title>Agentes de Conversação com IA'),
    ('Chatbots com IA que <span class="text-accent">Realmente Funcionam</span>', 'Agentes de Conversação com IA que <span class="text-accent">Realmente Funcionam</span>'),
    ('href="chatbot.html" class="text-accent">PT</a>', 'href="agentes-conversacao.html" class="text-accent">PT</a>'),
    ('href="../en/chatbot.html" class="text-slate-400', 'href="../en/conversational-agents.html" class="text-slate-400')
])
if os.path.exists('pt/agentes-de-texto.html'):
    os.remove('pt/agentes-de-texto.html')

# 2. PT: Ferramentas Personalizadas (duplicate from voice agents)
shutil.copy('pt/agentes-de-voz.html', 'pt/ferramentas-personalizadas.html')
update_file('pt/ferramentas-personalizadas.html', [
    ('<title>Agentes de Voz', '<title>Ferramentas Personalizadas'),
    ('Agentes de Voz com IA', 'Ferramentas Personalizadas com IA'),
    ('href="agentes-de-voz.html" class="text-accent">PT</a>', 'href="ferramentas-personalizadas.html" class="text-accent">PT</a>'),
    ('href="../en/voice-agents.html" class="text-slate-400', 'href="../en/custom-tools.html" class="text-slate-400')
])

# 3. EN: Chatbot -> Conversational Agents
shutil.move('en/chatbot.html', 'en/conversational-agents.html')
update_file('en/conversational-agents.html', [
    ('<title>AI Chatbots', '<title>AI Conversational Agents'),
    ('AI Chatbots that <span class="text-accent">Actually Work</span>', 'AI Conversational Agents that <span class="text-accent">Actually Work</span>'),
    ('href="chatbot.html" class="text-accent">EN</a>', 'href="conversational-agents.html" class="text-accent">EN</a>'),
    ('href="../pt/chatbot.html" class="text-slate-400', 'href="../pt/agentes-conversacao.html" class="text-slate-400')
])
if os.path.exists('en/text-agents.html'):
    os.remove('en/text-agents.html')

# 4. EN: Custom Tools (duplicate from voice agents)
shutil.copy('en/voice-agents.html', 'en/custom-tools.html')
update_file('en/custom-tools.html', [
    ('<title>AI Voice Agents', '<title>Custom AI Tools'),
    ('AI Voice Agents', 'Custom AI Tools'),
    ('href="voice-agents.html" class="text-accent">EN</a>', 'href="custom-tools.html" class="text-accent">EN</a>'),
    ('href="../pt/agentes-de-voz.html" class="text-slate-400', 'href="../pt/ferramentas-personalizadas.html" class="text-slate-400')
])

print("Reorganization complete.")
