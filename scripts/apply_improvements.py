import os
import glob
import re

directories = ['pt', 'en']

replacements = [
    # Emails
    (r'contato@mobizze\.com', 'contact@mobizze.com'),
    
    # Copyright
    (r'©\s*(?:2024|2025)?\s*Mobizze', '© 2026 Mobizze'),
    
    # Footer Locations
    (r'Portugal\s*(?:·|&middot;)\s*World\b', 'Portugal &middot; Worldwide'),
    (r'Portugal\s*(?:·|&middot;)\s*Worldwide\b', 'Portugal &middot; Worldwide'),
    
    # Absolute claims
    (r'resposta perfeita autonomamente', 'prepara respostas consistentes com as regras definidas'),
    (r'funcionam desde o primeiro dia', 'integra-se progressivamente nos processos existentes'),
    (r'sem latência', 'baixa latência'),
    (r'voz indistinguível da humana', 'voz natural'),
    (r'a concorrência já automatizou', 'cada vez mais empresas estão a automatizar estes processos'),
    (r'o ROI cresce mês após mês', 'acompanhamos os resultados e identificamos novas oportunidades de melhoria'),
    
    # specific copy
    (r'Porteiro Inteligente', 'motor inteligente de qualificação comercial'),
    (r'Voz indistinguível da humana e sem latência', 'Voz natural e de baixa latência, com identificação clara de que o utilizador está a interagir com um assistente virtual'),
    
    # English versions of absolute claims (guessing based on translation, let's do a quick manual check later if needed, but I'll add some obvious ones)
    (r'perfect response autonomously', 'prepares consistent responses based on defined rules'),
    (r'work from day one', 'integrates progressively into existing processes'),
    (r'zero latency', 'low latency'),
    (r'indistinguishable from human voice', 'natural voice'),
    (r'the competition has already automated', 'more and more companies are automating these processes'),
    (r'ROI grows month after month', 'we track results and identify new improvement opportunities'),
    (r'Intelligent Bouncer', 'intelligent commercial qualification engine'),
]

for d in directories:
    for filepath in glob.glob(f'{d}/**/*.html', recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        for old, new in replacements:
            content = re.sub(old, new, content, flags=re.IGNORECASE)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {filepath}')

print("Global text replacements applied.")
