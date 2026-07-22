import os
import re

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

# Update pt/index.html
pt_index_replacements = [
    (
        '<h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">\n                    Recupere Até 70% do Tempo da Sua Equipa <span class="text-accent">Com IA e Automação</span>\n                </h2>',
        '<h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">\n                    Sistemas de IA Personalizados para Empresas\n                </h2>'
    ),
    (
        '<p class="max-w-xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">\n                    Criamos agentes de IA, automatizamos processos e devolvemos horas à sua equipa — para decisões que fazem a diferença.\n                </p>',
        '<p class="max-w-xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">\n                    Analisamos os seus processos, desenvolvemos agentes, automações e ferramentas personalizadas para reduzir custos, recuperar tempo e acelerar o crescimento.\n                </p>'
    ),
    (
        '<span class="hidden sm:inline">Diagnóstico gratuito — Ver quanto posso poupar</span>',
        '<span class="hidden sm:inline">Descobrir oportunidades no meu negócio</span>'
    ),
    (
        '<a href="#problema" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full text-sm font-medium transition-all duration-300 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 shadow-sm">\n                            Descobrir mais\n                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 3L8 13M8 13L4 9M8 13L12 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>\n                        </a>',
        '<a href="casos-estudo.html" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full text-sm font-medium transition-all duration-300 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 shadow-sm">\n                            Ver casos reais\n                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 3L8 13M8 13L4 9M8 13L12 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>\n                        </a>'
    ),
    (
        '<a href="chatbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Chatbot</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualificar-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualificar Leads CRM</a>\n                            <a href="agendar-reunioes.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agendar Reuniões</a>\n                            <a href="agentes-de-voz.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Voz</a>\n                            <a href="agentes-de-texto.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Texto</a>\n                            <a href="redes-sociais.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Redes Sociais</a>',
        '<a href="agentes-conversacao.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Conversação</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualificar-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualificar Leads CRM</a>\n                            <a href="agendar-reunioes.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agendar Reuniões</a>\n                            <a href="agentes-de-voz.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Voz</a>\n                            <a href="ferramentas-personalizadas.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Ferramentas Personalizadas</a>\n                            <a href="redes-sociais.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Redes Sociais</a>'
    ),
    (
        '<a href="chatbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Chatbot</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualificar-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualificar CRM</a>\n                    <a href="agendar-reunioes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agendar Reuniões</a>\n                    <a href="agentes-de-voz.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Voz</a>\n                    <a href="agentes-de-texto.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Texto</a>\n                    <a href="redes-sociais.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Redes Sociais</a>',
        '<a href="agentes-conversacao.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Conversação</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualificar-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualificar CRM</a>\n                    <a href="agendar-reunioes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agendar Reuniões</a>\n                    <a href="agentes-de-voz.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Voz</a>\n                    <a href="ferramentas-personalizadas.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Ferramentas Personalizadas</a>\n                    <a href="redes-sociais.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Redes Sociais</a>'
    )
]

update_file('/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0/pt/index.html', pt_index_replacements)

# Add disclaimer after stats bar in pt/index.html
with open('/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0/pt/index.html', 'r', encoding='utf-8') as f:
    pt_content = f.read()

disclaimer_pt = '            </div>\n            <div class="max-w-5xl mx-auto mt-6 text-center">\n                <p class="text-xs text-slate-400">Dados agregados de projetos implementados entre 2024 e 2026. Resultados variam consoante os processos, volume e sistemas de cada empresa.</p>\n            </div>'
if 'Dados agregados de projetos' not in pt_content:
    pt_content = pt_content.replace('            </div>\n        </div>\n\n        <!-- Clientes e Parceiros -->', disclaimer_pt + '\n        </div>\n\n        <!-- Clientes e Parceiros -->')
    with open('/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0/pt/index.html', 'w', encoding='utf-8') as f:
        f.write(pt_content)
        
print("Updated pt/index.html")
