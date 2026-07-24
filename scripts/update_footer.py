import os
import re
import glob

PT_FOOTER_TEMPLATE = """    <!-- Footer -->
    <footer class="relative border-t border-slate-200 bg-white overflow-hidden">
        <div class="relative max-w-6xl mx-auto px-6 pt-16 pb-8">
            <div class="grid grid-cols-2 md:grid-cols-12 gap-10 md:gap-8 mb-12">
                <!-- Branding -->
                <div class="col-span-2 md:col-span-4">
                    <div class="font-display font-bold text-xl tracking-tight text-dark mb-4">
                        Mobizze
                    </div>
                    <p class="text-sm text-slate-500 leading-relaxed mb-6 max-w-xs font-medium">
                        Sistemas de IA personalizados para empresas. Operamos em Portugal e no Mundo, criando automações que reduzem custos e aceleram o crescimento.
                    </p>
                </div>

                <!-- Links -->
                <div class="col-span-1 md:col-span-2 md:col-start-7">
                    <h3 class="text-xs font-mono tracking-[0.1em] uppercase mb-4 text-slate-900 font-bold">Navegação</h3>
                    <ul class="space-y-3">
                        <li><a href="sobre.html" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors">Sobre Nós</a></li>
                        <li><a href="planos-implementacao.html" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors">Planos Flexíveis</a></li>
                        <li><a href="index.html#faq" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors">FAQ</a></li>
                    </ul>
                </div>

                <div class="col-span-2 md:col-span-3 md:col-start-10">
                    <h3 class="text-xs font-mono tracking-[0.1em] uppercase mb-4 text-slate-900 font-bold">Contacto</h3>
                    <ul class="space-y-3">
                        <li>
                            <span class="text-sm text-slate-500 font-medium flex items-start gap-2">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-accent mt-0.5"><path d="M20 10c0 7-8 13-8 13s-8-6-8-13a8 8 0 0 1 16 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                Portugal · Mundo
                            </span>
                        </li>
                        <li>
                            <a href="mailto:info@mobizze.com" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors flex items-center gap-2">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-accent"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                                info@mobizze.com
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="pt-8 border-t border-slate-200 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <p class="text-xs text-slate-400 font-medium">&copy; 2026 <span class="font-display font-bold text-slate-600">Mobizze</span>. Todos os direitos reservados.</p>
                <div class="flex gap-6">
                    <a href="privacidade.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Privacidade</a>
                    <a href="termos.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Termos</a>
                    <a href="seguranca.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Segurança</a>
                    <div class="h-4 w-px bg-slate-200"></div>
                    <div class="flex items-center gap-2 text-xs font-bold">
                        <a href="{pt_link}" class="text-accent">PT</a>
                        <span class="text-slate-300">|</span>
                        <a href="{en_link}" class="text-slate-400 hover:text-accent transition-colors">EN</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>"""

EN_FOOTER_TEMPLATE = """    <!-- Footer -->
    <footer class="relative border-t border-slate-200 bg-white overflow-hidden">
        <div class="relative max-w-6xl mx-auto px-6 pt-16 pb-8">
            <div class="grid grid-cols-2 md:grid-cols-12 gap-10 md:gap-8 mb-12">
                <!-- Branding -->
                <div class="col-span-2 md:col-span-4">
                    <div class="font-display font-bold text-xl tracking-tight text-dark mb-4">
                        Mobizze
                    </div>
                    <p class="text-sm text-slate-500 leading-relaxed mb-6 max-w-xs font-medium">
                        Custom AI systems for businesses. We operate in Portugal and worldwide, creating automations that reduce costs and accelerate growth.
                    </p>
                </div>

                <!-- Links -->
                <div class="col-span-1 md:col-span-2 md:col-start-7">
                    <h3 class="text-xs font-mono tracking-[0.1em] uppercase mb-4 text-slate-900 font-bold">Navigation</h3>
                    <ul class="space-y-3">
                        <li><a href="about.html" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors">About Us</a></li>
                        <li><a href="flexible-implementation-plans.html" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors">Flexible Plans</a></li>
                        <li><a href="index.html#faq" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors">FAQ</a></li>
                    </ul>
                </div>

                <div class="col-span-2 md:col-span-3 md:col-start-10">
                    <h3 class="text-xs font-mono tracking-[0.1em] uppercase mb-4 text-slate-900 font-bold">Contact</h3>
                    <ul class="space-y-3">
                        <li>
                            <span class="text-sm text-slate-500 font-medium flex items-start gap-2">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-accent mt-0.5"><path d="M20 10c0 7-8 13-8 13s-8-6-8-13a8 8 0 0 1 16 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                Portugal · World
                            </span>
                        </li>
                        <li>
                            <a href="mailto:info@mobizze.com" class="text-sm text-slate-500 hover:text-accent font-medium transition-colors flex items-center gap-2">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-accent"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
                                info@mobizze.com
                            </a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="pt-8 border-t border-slate-200 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
                <p class="text-xs text-slate-400 font-medium">&copy; 2026 <span class="font-display font-bold text-slate-600">Mobizze</span>. All rights reserved.</p>
                <div class="flex gap-6">
                    <a href="privacy.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Privacy</a>
                    <a href="terms.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Terms</a>
                    <a href="security.html" class="text-xs text-slate-400 hover:text-slate-600 font-medium transition-colors">Security</a>
                    <div class="h-4 w-px bg-slate-200"></div>
                    <div class="flex items-center gap-2 text-xs font-bold">
                        <a href="{pt_link}" class="text-slate-400 hover:text-accent transition-colors">PT</a>
                        <span class="text-slate-300">|</span>
                        <a href="{en_link}" class="text-accent">EN</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>"""

def update_footers():
    # We will map english equivalents based on file names for translation.
    # We need a dictionary if the names are translated. 
    # Let's read en and pt folders to find pairs.
    # Since I don't have a perfect mapping for all files, I'll default to index.html if the exact file doesn't exist in the other language.
    
    pt_files = set([os.path.basename(f) for f in glob.glob('pt/*.html')])
    en_files = set([os.path.basename(f) for f in glob.glob('en/*.html')])
    
    # PT -> EN mapping heuristics
    mapping_pt_to_en = {
        'index.html': 'index.html',
        'sobre.html': 'about.html',
        'contacto.html': 'contact.html',
        'emailbot.html': 'emailbot.html',
        'privacidade.html': 'privacy.html',
        'termos.html': 'terms.html',
        'seguranca.html': 'security.html',
        'ferramentas-personalizadas.html': 'custom-tools.html',
        'planos-implementacao.html': 'flexible-implementation-plans.html',
        'casos-estudo.html': 'case-studies.html',
        'caso-estudo-portugal-textile.html': 'case-study-portugal-textile.html',
        'integracoes.html': 'integrations.html',
        'agendar-reunioes.html': 'schedule-meetings.html',
        'agentes-conversacao.html': 'conversational-agents.html',
        'agentes-de-voz.html': 'voice-agents.html',
        'qualificar-leads-crm.html': 'qualify-leads-crm.html',
        'redes-sociais.html': 'social-media.html',
        'setores.html': 'sectors.html',
        'setor-advogados.html': 'sector-lawyers.html',
        'setor-agricultura.html': 'sector-agriculture.html',
        'setor-clinicas-saude.html': 'sector-clinics-health.html',
        'setor-construcao.html': 'sector-construction.html',
        'setor-contabilidade.html': 'sector-accounting.html',
        'setor-ecommerce.html': 'sector-ecommerce.html',
        'setor-educacao.html': 'sector-education.html',
        'setor-ginasios.html': 'sector-gyms.html',
        'setor-imobiliarias.html': 'sector-real-estate.html',
        'setor-industria.html': 'sector-industry.html',
        'setor-oficinas.html': 'sector-workshops.html',
        'setor-restaurantes.html': 'sector-restaurants.html',
        'setor-retalho.html': 'sector-retail.html',
        'setor-saloes-estetica.html': 'sector-salons-aesthetics.html',
        'setor-suporte-b2b.html': 'sector-b2b-support.html',
        'setor-turismo.html': 'sector-tourism.html',
    }
    
    # Reverse mapping
    mapping_en_to_pt = {v: k for k, v in mapping_pt_to_en.items()}
    
    def process_dir(directory, template, is_pt):
        count = 0
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.html'):
                    filepath = os.path.join(root, file)
                    
                    # Determine links
                    if is_pt:
                        pt_link = file
                        en_link = f"../en/{mapping_pt_to_en.get(file, 'index.html')}"
                    else:
                        pt_link = f"../pt/{mapping_en_to_pt.get(file, 'index.html')}"
                        en_link = file
                        
                    footer_content = template.format(pt_link=pt_link, en_link=en_link)
                    
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    new_content = re.sub(
                        r'<!-- Footer -->\s*<footer.*?</footer\s*>', 
                        footer_content, 
                        content, 
                        flags=re.DOTALL
                    )
                    
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        count += 1
        return count

    pt_count = process_dir('pt', PT_FOOTER_TEMPLATE, True)
    en_count = process_dir('en', EN_FOOTER_TEMPLATE, False)
    
    print(f"Updated {pt_count} PT footers and {en_count} EN footers.")

if __name__ == '__main__':
    update_footers()
