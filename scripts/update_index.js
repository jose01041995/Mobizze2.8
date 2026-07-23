const fs = require('fs');

const ptNewSection = `
        <!-- Sistemas Personalizados -->
        <section class="relative px-6 py-24 bg-white border-t border-slate-100">
            <div class="max-w-5xl mx-auto">
                <div class="text-center mb-16 reveal">
                    <h2 class="font-display font-bold text-dark text-3xl md:text-4xl tracking-tight mb-4">Ferramentas de IA construídas para o seu negócio</h2>
                    <p class="text-lg text-slate-600 max-w-2xl mx-auto">A Mobizze não é apenas uma agência de chatbots. Construímos sistemas personalizados integrados nos seus processos para resolver problemas específicos da sua operação.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 reveal delay-100">
                        <div class="w-12 h-12 bg-blue-100 text-accent rounded-xl flex items-center justify-center mb-6">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        </div>
                        <h3 class="text-xl font-display font-bold text-dark mb-3">Análise Documental</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Sistemas automáticos para extrair dados de faturas, contratos e processos, eliminando o fecho de mês manual.</p>
                    </div>
                    
                    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 reveal delay-200">
                        <div class="w-12 h-12 bg-blue-100 text-accent rounded-xl flex items-center justify-center mb-6">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
                        </div>
                        <h3 class="text-xl font-display font-bold text-dark mb-3">Dashboards Inteligentes</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Plataformas internas que centralizam KPIs e usam IA preditiva para gerar relatórios de gestão em tempo real.</p>
                    </div>
                    
                    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 reveal delay-300">
                        <div class="w-12 h-12 bg-blue-100 text-accent rounded-xl flex items-center justify-center mb-6">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        </div>
                        <h3 class="text-xl font-display font-bold text-dark mb-3">Assistentes Internos</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Copilotos alimentados pelo conhecimento técnico da sua empresa para apoiar equipas comerciais e de recursos humanos.</p>
                    </div>
                </div>
            </div>
        </section>
`;

const enNewSection = `
        <!-- Custom Systems -->
        <section class="relative px-6 py-24 bg-white border-t border-slate-100">
            <div class="max-w-5xl mx-auto">
                <div class="text-center mb-16 reveal">
                    <h2 class="font-display font-bold text-dark text-3xl md:text-4xl tracking-tight mb-4">AI Tools Built For Your Business</h2>
                    <p class="text-lg text-slate-600 max-w-2xl mx-auto">Mobizze isn't just a chatbot agency. We build custom systems integrated into your processes to solve specific operational problems.</p>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 reveal delay-100">
                        <div class="w-12 h-12 bg-blue-100 text-accent rounded-xl flex items-center justify-center mb-6">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                        </div>
                        <h3 class="text-xl font-display font-bold text-dark mb-3">Document Analysis</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Automated systems to extract data from invoices, contracts, and processes, eliminating manual month-end closing.</p>
                    </div>
                    
                    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 reveal delay-200">
                        <div class="w-12 h-12 bg-blue-100 text-accent rounded-xl flex items-center justify-center mb-6">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
                        </div>
                        <h3 class="text-xl font-display font-bold text-dark mb-3">Smart Dashboards</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Internal platforms that centralize KPIs and use predictive AI to generate management reports in real-time.</p>
                    </div>
                    
                    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-100 reveal delay-300">
                        <div class="w-12 h-12 bg-blue-100 text-accent rounded-xl flex items-center justify-center mb-6">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        </div>
                        <h3 class="text-xl font-display font-bold text-dark mb-3">Internal Assistants</h3>
                        <p class="text-slate-600 text-sm leading-relaxed">Copilots powered by your company's technical knowledge to support commercial and human resources teams.</p>
                    </div>
                </div>
            </div>
        </section>
`;

function processIndex(file, isPt) {
    let content = fs.readFileSync(file, 'utf8');

    // 1. Insert new section before tools ticker
    const hook = '<section class="relative bg-dark py-16 overflow-hidden">';
    if (content.indexOf(hook) !== -1 && !content.includes('Dashboards Inteligentes') && !content.includes('Smart Dashboards')) {
        content = content.replace(hook, (isPt ? ptNewSection : enNewSection) + '\n' + hook);
    }

    // 2. Fix Meta Description
    if (isPt) {
        content = content.replace('e devolvemos até 70% do tempo à sua equipa.', 'e ajudamos a automatizar os seus processos repetitivos.');
    } else {
        content = content.replace("and give back up to 70% of your team's time.", 'and help automate your repetitive processes.');
    }

    // 3. Fix main problem header
    if (isPt) {
        content = content.replace(
            'A Sua Equipa Perde <span class="text-accent">Até 70% do Tempo</span> em Tarefas Que a IA Resolve em Minutos',
            'A Sua Equipa Perde <span class="text-accent">Centenas de Horas</span> em Tarefas Que Podem Ser Automatizadas'
        );
    } else {
        content = content.replace(
            'Your Team Wastes <span class="text-accent">Up to 70% of Its Time</span> on Tasks That AI Solves in Minutes',
            'Your Team Wastes <span class="text-accent">Hundreds of Hours</span> on Tasks That Can Be Automated'
        );
    }

    // 4. Fix response text
    if (isPt) {
        content = content.replace('redige e envia a prepara respostas consistentes com as regras definidas', 'redige e envia respostas consistentes de acordo com as regras da sua empresa');
    }

    // 5. Fix 98% description
    if (isPt) {
        content = content.replace('<div class="text-3xl md:text-4xl font-bold font-display text-accent">98%*</div>\n                        <div class="text-[11px] uppercase tracking-wider font-bold text-slate-500 mt-2">Clientes<br>Satisfeitos</div>', '<div class="text-3xl md:text-4xl font-bold font-display text-accent">98%*</div>\n                        <div class="text-[11px] uppercase tracking-wider font-bold text-slate-500 mt-2">Satisfação<br>Projetos Realizados</div>');
    } else {
        content = content.replace('<div class="text-3xl md:text-4xl font-bold font-display text-accent">98%*</div>\n                        <div class="text-[11px] uppercase tracking-wider font-bold text-slate-500 mt-2">Satisfied<br>Clients</div>', '<div class="text-3xl md:text-4xl font-bold font-display text-accent">98%*</div>\n                        <div class="text-[11px] uppercase tracking-wider font-bold text-slate-500 mt-2">Satisfaction<br>Completed Projects</div>');
    }

    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated', file);
}

processIndex('/Users/pinto/Downloads/Mobizze2.0/pt/index.html', true);
processIndex('/Users/pinto/Downloads/Mobizze2.0/en/index.html', false);
