import os
import re
import glob

PT_NAV_TEMPLATE = """    <nav id="navbar" class="fixed top-4 left-1/2 z-50 transition-all duration-700 -translate-x-1/2 w-[min(800px,94vw)] rounded-full px-5 glass-nav">
        <div class="flex items-center justify-between h-12">
            <a href="index.html" aria-label="Mobizze — Home" class="font-display font-bold text-lg tracking-tight text-dark">
                Mobizze
            </a>
            <div class="hidden md:flex items-center gap-6 h-full">
                <!-- Dropdown Serviços -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Serviços <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Hitbox Invisível e Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-[400px] z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-4 grid grid-cols-2 gap-4">
                            <div>
                                <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Agentes de IA</h4>
                                <a href="agentes-conversacao.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Conversação</a>
                                <a href="agentes-de-voz.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Voz</a>
                                <a href="emailbot.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbots</a>
                            </div>
                            <div>
                                <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Automação de Processos</h4>
                                <a href="qualificar-leads-crm.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Vendas e CRM</a>
                                <a href="agendar-reunioes.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agendar Reuniões</a>
                                <a href="redes-sociais.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Redes Sociais</a>
                            </div>
                            <div class="col-span-2 border-t border-slate-100 pt-3 mt-1 grid grid-cols-2 gap-4">
                                <div>
                                    <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Desenvolvimento</h4>
                                    <a href="ferramentas-personalizadas.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Ferramentas Personalizadas</a>
                                </div>
                                <div>
                                    <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Sistemas</h4>
                                    <a href="integracoes.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Integrações e Dados</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Dropdown Setores -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Setores <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Hitbox Invisível e Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-48 z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-2 flex flex-col gap-1">
                            <a href="setor-clinicas-saude.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Clínicas & Saúde</a>
                            <a href="setor-imobiliarias.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Imobiliárias</a>
                            <a href="setor-ecommerce.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">E-commerce</a>
                            <div class="h-px bg-slate-100 my-1 mx-2"></div>
                            <a href="setores.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-semibold transition-colors">Ver todos os setores &rarr;</a>
                        </div>
                    </div>
                </div>
                <a href="sobre.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Sobre Nós</a>
                <a href="planos-implementacao.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Planos Flexíveis</a>
                <a href="index.html#faq" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">FAQ</a>
            </div>
            
            <!-- Link para a página de contacto -->
            <a href="contacto.html" class="hidden md:inline-flex items-center px-4 py-1.5 rounded-full text-xs font-semibold transition-all duration-300 bg-accent text-white hover:bg-blue-700 shadow-sm hover:shadow-md">Falar connosco</a>
            
            <button id="mobile-menu-btn" class="md:hidden text-slate-600 focus:outline-none" aria-label="Menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16"></path><path d="M4 12h16"></path><path d="M4 19h16"></path></svg>
            </button>
        </div>
    </nav>"""

EN_NAV_TEMPLATE = """    <nav id="navbar" class="fixed top-4 left-1/2 z-50 transition-all duration-700 -translate-x-1/2 w-[min(800px,94vw)] rounded-full px-5 glass-nav">
        <div class="flex items-center justify-between h-12">
            <a href="index.html" aria-label="Mobizze — Home" class="font-display font-bold text-lg tracking-tight text-dark">
                Mobizze
            </a>
            <div class="hidden md:flex items-center gap-6 h-full">
                <!-- Dropdown Services -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Services <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Hitbox Invisível e Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-[400px] z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-4 grid grid-cols-2 gap-4">
                            <div>
                                <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">AI Agents</h4>
                                <a href="conversational-agents.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Conversational Agents</a>
                                <a href="voice-agents.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Voice Agents</a>
                                <a href="emailbot.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbots</a>
                            </div>
                            <div>
                                <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Process Automation</h4>
                                <a href="qualify-leads-crm.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Sales & CRM</a>
                                <a href="schedule-meetings.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Schedule Meetings</a>
                                <a href="social-media.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Social Media</a>
                            </div>
                            <div class="col-span-2 border-t border-slate-100 pt-3 mt-1 grid grid-cols-2 gap-4">
                                <div>
                                    <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Development</h4>
                                    <a href="custom-tools.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Custom Tools</a>
                                </div>
                                <div>
                                    <h4 class="text-[10px] font-bold tracking-wider text-slate-400 uppercase mb-2 px-2">Systems</h4>
                                    <a href="integrations.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Integrations & Data</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Dropdown Sectors -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Sectors <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Hitbox Invisível e Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-48 z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-2 flex flex-col gap-1">
                            <a href="sector-clinics-health.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Clinics & Health</a>
                            <a href="sector-real-estate.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Real Estate</a>
                            <a href="sector-ecommerce.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">E-commerce</a>
                            <div class="h-px bg-slate-100 my-1 mx-2"></div>
                            <a href="sectors.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-semibold transition-colors">View all sectors &rarr;</a>
                        </div>
                    </div>
                </div>
                <a href="about.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">About Us</a>
                <a href="flexible-implementation-plans.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Flexible Plans</a>
                <a href="index.html#faq" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">FAQ</a>
            </div>
            
            <!-- Link para a página de contacto -->
            <a href="contact.html" class="hidden md:inline-flex items-center px-4 py-1.5 rounded-full text-xs font-semibold transition-all duration-300 bg-accent text-white hover:bg-blue-700 shadow-sm hover:shadow-md">Talk to us</a>
            
            <button id="mobile-menu-btn" class="md:hidden text-slate-600 focus:outline-none" aria-label="Menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16"></path><path d="M4 12h16"></path><path d="M4 19h16"></path></svg>
            </button>
        </div>
    </nav>"""

PT_MOBILE_MENU_TEMPLATE = """    <div id="mobile-menu" class="hidden md:hidden fixed inset-0 w-full h-[100dvh] bg-white z-[100] flex flex-col">
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

EN_MOBILE_MENU_TEMPLATE = """    <div id="mobile-menu" class="hidden md:hidden fixed inset-0 w-full h-[100dvh] bg-white z-[100] flex flex-col">
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
                <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Services</div>
                <div class="flex flex-col gap-4">
                    <a href="conversational-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Conversational Agents</a>
                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>
                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>
                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>
                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>
                    <a href="custom-tools.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Custom Tools</a>
                    <a href="integrations.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Integrations & Data</a>
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
            
            <!-- Link para a página de contacto -->
            <div class="mt-auto pt-6">
                <a href="contact.html" class="mobile-link w-full block py-4 rounded-full text-base font-semibold bg-accent text-white hover:bg-blue-700 text-center shadow-md">Talk to us</a>
            </div>
        </div>
    </div>"""

def update_headers():
    def process_dir(directory, nav_template, mobile_template):
        count = 0
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Replace navbar
                    new_content = re.sub(
                        r'<nav id="navbar".*?</nav>', 
                        nav_template, 
                        content, 
                        flags=re.DOTALL
                    )
                    
                    # Replace mobile menu
                    new_content = re.sub(
                        r'<div id="mobile-menu".*?(?=<main>)', 
                        mobile_template + "\n\n    ", 
                        new_content, 
                        flags=re.DOTALL
                    )

                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
        return count

    pt_count = process_dir('pt', PT_NAV_TEMPLATE, PT_MOBILE_MENU_TEMPLATE)
    en_count = process_dir('en', EN_NAV_TEMPLATE, EN_MOBILE_MENU_TEMPLATE)
    
    print(f"Updated {pt_count} PT headers/mobile menus and {en_count} EN headers/mobile menus.")

if __name__ == '__main__':
    update_headers()
