import os
import glob

def process_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

pt_replacements = [
    (
        '<a href="chatbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Chatbot</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualificar-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualificar Leads CRM</a>\n                            <a href="agendar-reunioes.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agendar Reuniões</a>\n                            <a href="agentes-de-voz.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Voz</a>\n                            <a href="agentes-de-texto.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Texto</a>\n                            <a href="redes-sociais.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Redes Sociais</a>',
        '<a href="agentes-conversacao.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Conversação</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualificar-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualificar Leads CRM</a>\n                            <a href="agendar-reunioes.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agendar Reuniões</a>\n                            <a href="agentes-de-voz.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Voz</a>\n                            <a href="ferramentas-personalizadas.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Ferramentas Personalizadas</a>\n                            <a href="redes-sociais.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Redes Sociais</a>'
    ),
    (
        '<a href="chatbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Chatbot</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualificar-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualificar CRM</a>\n                    <a href="agendar-reunioes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agendar Reuniões</a>\n                    <a href="agentes-de-voz.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Voz</a>\n                    <a href="agentes-de-texto.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Texto</a>\n                    <a href="redes-sociais.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Redes Sociais</a>',
        '<a href="agentes-conversacao.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Conversação</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualificar-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualificar CRM</a>\n                    <a href="agendar-reunioes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agendar Reuniões</a>\n                    <a href="agentes-de-voz.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Voz</a>\n                    <a href="ferramentas-personalizadas.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Ferramentas Personalizadas</a>\n                    <a href="redes-sociais.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Redes Sociais</a>'
    )
]

en_replacements = [
    (
        '<a href="chatbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Chatbot</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualify-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualify Leads CRM</a>\n                            <a href="schedule-meetings.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Schedule Meetings</a>\n                            <a href="voice-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Voice Agents</a>\n                            <a href="text-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Text Agents</a>\n                            <a href="social-media.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Social Media</a>',
        '<a href="conversational-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Conversational Agents</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualify-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualify Leads CRM</a>\n                            <a href="schedule-meetings.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Schedule Meetings</a>\n                            <a href="voice-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Voice Agents</a>\n                            <a href="custom-tools.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Custom Tools</a>\n                            <a href="social-media.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Social Media</a>'
    ),
    (
        '<a href="chatbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Chatbot</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>\n                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>\n                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>\n                    <a href="text-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Text Agents</a>\n                    <a href="social-media.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Social Media</a>',
        '<a href="conversational-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Conversational Agents</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>\n                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>\n                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>\n                    <a href="custom-tools.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Custom Tools</a>\n                    <a href="social-media.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Social Media</a>'
    )
]

def main():
    changed_pt = 0
    for f in glob.glob("pt/*.html"):
        if process_file(f, pt_replacements):
            changed_pt += 1
            print(f"Updated PT: {f}")
            
    changed_en = 0
    for f in glob.glob("en/*.html"):
        if process_file(f, en_replacements):
            changed_en += 1
            print(f"Updated EN: {f}")

    print(f"Total files updated: PT={changed_pt}, EN={changed_en}")

if __name__ == "__main__":
    main()
