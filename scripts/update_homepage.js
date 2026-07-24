const fs = require('fs');
const path = require('path');

const ptPath = path.join(__dirname, '../pt/index.html');
const enPath = path.join(__dirname, '../en/index.html');

const ptContent = fs.readFileSync(ptPath, 'utf8');
const enContent = fs.readFileSync(enPath, 'utf8');

const ptNewSection = `
<section class="relative bg-slate-50 py-24 overflow-hidden border-t border-slate-100">
    <div class="max-w-5xl mx-auto px-6">
        <div class="flex flex-col md:flex-row justify-between items-end gap-6 mb-12 reveal">
            <div>
                <p class="text-[10px] md:text-xs font-mono tracking-[0.25em] uppercase mb-3 text-accent">Impacto Comprovado</p>
                <h3 class="text-2xl md:text-3xl font-display font-bold text-dark tracking-tight">Casos de Sucesso B2B</h3>
            </div>
            <a href="casos-estudo.html" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full text-xs font-medium bg-white border border-slate-200 text-slate-700 hover:bg-blue-50 hover:text-accent hover:border-blue-200 transition-all shadow-sm">
                Ver todos os casos
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm reveal delay-100">
                <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-[10px] font-bold uppercase tracking-wider mb-4">Portugal Textile</div>
                <h4 class="text-xl font-display font-bold text-dark mb-3">Automação Comercial</h4>
                <p class="text-slate-600 text-sm mb-6 leading-relaxed">Implementámos IA para triar centenas de emails técnicos de encomendas, reduzindo em 80% o trabalho administrativo e aumentando a velocidade de resposta em 5x.</p>
                <div class="pt-4 border-t border-slate-100">
                    <p class="text-sm italic text-slate-700 mb-2">"O impacto foi imediato. A equipa comercial deixou de perder horas a ler emails técnicos e passou a focar-se apenas em fechar negócio."</p>
                    <p class="text-[10px] font-bold text-dark uppercase tracking-wide">— Diretor Comercial</p>
                </div>
            </div>
            
            <div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm reveal delay-200">
                <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-[10px] font-bold uppercase tracking-wider mb-4">Portugal Shoes</div>
                <h4 class="text-xl font-display font-bold text-dark mb-3">Sincronização Logística</h4>
                <p class="text-slate-600 text-sm mb-6 leading-relaxed">Assistente IA que cruza dados de fornecedores com planeamento interno, reduzindo os atrasos de produção em 40% com rastreio automático a 100%.</p>
                <div class="pt-4 border-t border-slate-100">
                    <p class="text-sm italic text-slate-700 mb-2">"O melhor investimento tecnológico que fizemos. Agora, a IA prevê as falhas de matéria-prima antes mesmo delas acontecerem."</p>
                    <p class="text-[10px] font-bold text-dark uppercase tracking-wide">— Gestor de Operações</p>
                </div>
            </div>
        </div>
    </div>
</section>
`;

const enNewSection = `
<section class="relative bg-slate-50 py-24 overflow-hidden border-t border-slate-100">
    <div class="max-w-5xl mx-auto px-6">
        <div class="flex flex-col md:flex-row justify-between items-end gap-6 mb-12 reveal">
            <div>
                <p class="text-[10px] md:text-xs font-mono tracking-[0.25em] uppercase mb-3 text-accent">Proven Impact</p>
                <h3 class="text-2xl md:text-3xl font-display font-bold text-dark tracking-tight">B2B Success Stories</h3>
            </div>
            <a href="case-studies.html" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full text-xs font-medium bg-white border border-slate-200 text-slate-700 hover:bg-blue-50 hover:text-accent hover:border-blue-200 transition-all shadow-sm">
                View all cases
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </a>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm reveal delay-100">
                <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-[10px] font-bold uppercase tracking-wider mb-4">Portugal Textile</div>
                <h4 class="text-xl font-display font-bold text-dark mb-3">Commercial Automation</h4>
                <p class="text-slate-600 text-sm mb-6 leading-relaxed">We implemented AI to sort hundreds of technical order emails, reducing admin work by 80% and increasing response speed by 5x.</p>
                <div class="pt-4 border-t border-slate-100">
                    <p class="text-sm italic text-slate-700 mb-2">"The impact was immediate. The team stopped wasting hours reading technical emails and focused solely on closing deals."</p>
                    <p class="text-[10px] font-bold text-dark uppercase tracking-wide">— Commercial Director</p>
                </div>
            </div>
            
            <div class="bg-white p-8 rounded-3xl border border-slate-200 shadow-sm reveal delay-200">
                <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-[10px] font-bold uppercase tracking-wider mb-4">Portugal Shoes</div>
                <h4 class="text-xl font-display font-bold text-dark mb-3">Logistics Sync</h4>
                <p class="text-slate-600 text-sm mb-6 leading-relaxed">AI assistant that cross-references supplier data with internal planning, reducing production delays by 40% with 100% automated tracking.</p>
                <div class="pt-4 border-t border-slate-100">
                    <p class="text-sm italic text-slate-700 mb-2">"The best technological investment we've made. Now, the AI predicts raw material shortages before they even happen."</p>
                    <p class="text-[10px] font-bold text-dark uppercase tracking-wide">— Operations Manager</p>
                </div>
            </div>
        </div>
    </div>
</section>
`;

function replaceSection(content, newSection) {
    const startIndex = content.indexOf('<section class="relative bg-dark py-16 overflow-hidden">');
    if (startIndex === -1) return content;
    
    // Find the closing tag of this section
    let depth = 0;
    let i = startIndex;
    let endIndex = -1;
    
    while (i < content.length) {
        if (content.substr(i, 8) === '<section') depth++;
        if (content.substr(i, 9) === '</section>') {
            depth--;
            if (depth === 0) {
                endIndex = i + 10;
                break;
            }
        }
        i++;
    }
    
    if (endIndex === -1) return content;
    
    return content.substring(0, startIndex) + newSection + content.substring(endIndex);
}

fs.writeFileSync(ptPath, replaceSection(ptContent, ptNewSection), 'utf8');
fs.writeFileSync(enPath, replaceSection(enContent, enNewSection), 'utf8');

console.log('Homepage layout updated for PT and EN');
