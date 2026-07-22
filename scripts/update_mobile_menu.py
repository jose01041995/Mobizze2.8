import os
import glob
import re

PT_MOBILE_MENU = """    <div id="mobile-menu" class="hidden md:hidden fixed inset-0 w-full h-[100dvh] bg-white z-[100] flex flex-col">
        <!-- Cabeçalho Menu Mobile -->
        <div class="flex items-center justify-between p-6 pb-4 border-b border-slate-100">
            <a href="index.html" aria-label="Mobizze — Home" class="font-display font-bold text-xl tracking-tight text-dark">
                Mobizze
            </a>
            <button id="close-mobile-menu" class="text-slate-600 focus:outline-none p-2 -mr-2 hover:bg-slate-50 rounded-full transition-colors" aria-label="Fechar Menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
        </div>

        <!-- Links e Opções -->
        <div class="flex-1 overflow-y-auto px-6 py-8 flex flex-col gap-8">
            <div>
                <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Serviços</div>
                <div class="flex flex-col gap-4">
                    <a href="agentes-conversacao.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Conversação</a>
                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>
                    <a href="qualificar-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualificar CRM</a>
                    <a href="agendar-reunioes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agendar Reuniões</a>
                    <a href="agentes-de-voz.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Voz</a>
                    <a href="ferramentas-personalizadas.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Ferramentas Personalizadas</a>
                    <a href="integracoes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Integrações e Dados</a>
                    <a href="redes-sociais.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Redes Sociais</a>
                </div>
            </div>
            
            <div class="h-px w-full bg-slate-100"></div>
            
            <div class="flex flex-col gap-5">
                <a href="setores.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Setores</a>
                <a href="sobre.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Sobre Nós</a>
                <a href="planos-implementacao.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Planos Flexíveis</a>
                <a href="index.html#faq" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">FAQ</a>
            </div>
            
            <!-- Link para a página de contacto -->
            <div class="mt-auto pt-6">
                <a href="contacto.html" class="mobile-link w-full block py-4 rounded-full text-base font-semibold bg-accent text-white hover:bg-blue-700 text-center shadow-md">Falar connosco</a>
            </div>
        </div>
    </div>"""

EN_MOBILE_MENU = """    <div id="mobile-menu" class="hidden md:hidden fixed inset-0 w-full h-[100dvh] bg-white z-[100] flex flex-col">
        <div class="flex items-center justify-between p-6 pb-4 border-b border-slate-100">
            <a href="index.html" aria-label="Mobizze — Home" class="font-display font-bold text-xl tracking-tight text-dark">
                Mobizze
            </a>
            <button id="close-mobile-menu" class="text-slate-600 focus:outline-none p-2 -mr-2 hover:bg-slate-50 rounded-full transition-colors" aria-label="Close Menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
        </div>

        <div class="flex-1 overflow-y-auto px-6 py-8 flex flex-col gap-8">
            <div>
                <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Services</div>
                <div class="flex flex-col gap-4">
                    <a href="conversational-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Conversational Agents</a>
                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>
                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>
                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>
                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>
                    <a href="custom-tools.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Custom Tools</a>
                    <a href="integrations.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Data & Integrations</a>
                    <a href="social-media.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Social Media</a>
                </div>
            </div>
            
            <div class="h-px w-full bg-slate-100"></div>
            
            <div class="flex flex-col gap-5">
                <a href="sectors.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Sectors</a>
                <a href="about.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">About Us</a>
                <a href="flexible-implementation-plans.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Flexible Plans</a>
                <a href="index.html#faq" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">FAQ</a>
            </div>
            
            <div class="mt-auto pt-6">
                <a href="contact.html" class="mobile-link w-full block py-4 rounded-full text-base font-semibold bg-accent text-white hover:bg-blue-700 text-center shadow-md">Contact Us</a>
            </div>
        </div>
    </div>"""

def replace_in_files(directory, replacement):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Using regex to replace the whole mobile menu block
                new_content = re.sub(
                    r'<div id="mobile-menu".*?</div>\s*</div>\s*</div>', 
                    replacement, 
                    content, 
                    flags=re.DOTALL
                )
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated mobile menu in {filepath}")

if __name__ == '__main__':
    replace_in_files('pt', PT_MOBILE_MENU)
    replace_in_files('en', EN_MOBILE_MENU)
    print("Mobile menu updated successfully!")
