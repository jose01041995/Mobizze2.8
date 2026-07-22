import os
import glob
import re

PT_NAV = """    <!-- Navigation -->
    <nav id="navbar" class="fixed top-4 left-1/2 z-50 transition-all duration-700 -translate-x-1/2 w-[min(800px,94vw)] rounded-full px-5 glass-nav">
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

EN_NAV = """    <!-- Navigation -->
    <nav id="navbar" class="fixed top-4 left-1/2 z-50 transition-all duration-700 -translate-x-1/2 w-[min(800px,94vw)] rounded-full px-5 glass-nav">
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
                                    <a href="integrations.html" class="block px-2 py-1.5 rounded-lg hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Data & Integrations</a>
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
                            <a href="sectors.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-semibold transition-colors">See all sectors &rarr;</a>
                        </div>
                    </div>
                </div>
                <a href="about.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">About Us</a>
                <a href="flexible-implementation-plans.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Flexible Plans</a>
                <a href="index.html#faq" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">FAQ</a>
            </div>
            
            <a href="contact.html" class="hidden md:inline-flex items-center px-4 py-1.5 rounded-full text-xs font-semibold transition-all duration-300 bg-accent text-white hover:bg-blue-700 shadow-sm hover:shadow-md">Talk to us</a>
            
            <button id="mobile-menu-btn" class="md:hidden text-slate-600 focus:outline-none" aria-label="Menu">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16"></path><path d="M4 12h16"></path><path d="M4 19h16"></path></svg>
            </button>
        </div>
    </nav>"""


def replace_in_files(directory, pattern, replacement):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Using regex to replace the whole nav block
                new_content = re.sub(
                    r'<!-- Navigation -->\s*<nav id="navbar".*?</nav>', 
                    replacement, 
                    content, 
                    flags=re.DOTALL
                )
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated nav in {filepath}")

if __name__ == '__main__':
    replace_in_files('pt', r'<!-- Navigation -->.*?<nav id="navbar".*?</nav>', PT_NAV)
    replace_in_files('en', r'<!-- Navigation -->.*?<nav id="navbar".*?</nav>', EN_NAV)
    print("Navigation updated successfully!")
