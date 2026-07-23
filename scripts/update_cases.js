const fs = require('fs');
const path = require('path');

function replaceCases(filePath, isPt) {
    let content = fs.readFileSync(filePath, 'utf8');

    const casesPt = `
                <!-- Case Study 1 -->
                <div class="bg-white p-8 md:p-12 rounded-3xl border border-slate-200 shadow-sm reveal flex flex-col md:flex-row gap-8 items-center">
                    <div class="flex-1">
                        <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-xs font-bold uppercase tracking-wider mb-4">Portugal Textile</div>
                        <h3 class="text-2xl md:text-3xl font-display font-bold text-dark mb-4">Automação Comercial e de Encomendas</h3>
                        <p class="text-slate-600 leading-relaxed mb-6"><strong>O Problema:</strong> Receção de um elevado volume de pedidos complexos por email, com informação técnica dispersa, criando a necessidade constante de validação manual e atrasando respostas ao cliente.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">-80%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Trabalho Administrativo</div>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">5x</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Resposta Mais Rápida</div>
                            </div>
                        </div>
                        
                        <h4 class="font-bold text-dark mb-2 text-sm">A Solução & Resultado:</h4>
                        <p class="text-sm text-slate-600 leading-relaxed">Implementámos um sistema de IA que analisa automaticamente todos os pedidos, extrai especificações técnicas, qualifica as oportunidades e prepara esboços de respostas. Os dados são organizados diretamente no CRM, garantindo um acompanhamento comercial imediato e permitindo à equipa focar-se em vendas em vez de triagem.</p>
                    </div>
                </div>

                <!-- Case Study 2 -->
                <div class="bg-white p-8 md:p-12 rounded-3xl border border-slate-200 shadow-sm reveal flex flex-col md:flex-row gap-8 items-center">
                    <div class="flex-1">
                        <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-xs font-bold uppercase tracking-wider mb-4">Portugal Shoes</div>
                        <h3 class="text-2xl md:text-3xl font-display font-bold text-dark mb-4">Sincronização Logística e Gestão de Fornecedores</h3>
                        <p class="text-slate-600 leading-relaxed mb-6"><strong>O Problema:</strong> Acompanhar falhas em matérias-primas e comunicar alterações de planeamento à fábrica envolvia dezenas de telefonemas e atualizações manuais no ERP, gerando atrasos na produção.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">100%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Rastreio Automático</div>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">-40%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Atrasos de Produção</div>
                            </div>
                        </div>
                        
                        <h4 class="font-bold text-dark mb-2 text-sm">A Solução & Resultado:</h4>
                        <p class="text-sm text-slate-600 leading-relaxed">Criámos um assistente logístico que cruza dados de fornecedores com o planeamento interno. A IA alerta automaticamente a equipa fabril sobre atrasos de material, sugere ajustes de planeamento e atualiza o estado da encomenda no ERP. A fábrica opera com muito menos interrupções.</p>
                    </div>
                </div>

                <!-- Case Study 3 -->
                <div class="bg-white p-8 md:p-12 rounded-3xl border border-slate-200 shadow-sm reveal flex flex-col md:flex-row gap-8 items-center">
                    <div class="flex-1">
                        <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-xs font-bold uppercase tracking-wider mb-4">Grupo Absolutarget</div>
                        <h3 class="text-2xl md:text-3xl font-display font-bold text-dark mb-4">Análise Documental e Reporting Financeiro</h3>
                        <p class="text-slate-600 leading-relaxed mb-6"><strong>O Problema:</strong> Conciliar faturas, recibos e relatórios de despesas de várias empresas do grupo requeria semanas de trabalho manual no fecho do mês, com elevado risco de erro humano.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">Dias &rarr; Horas</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Tempo de Fecho</div>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">99.9%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Precisão na Extração</div>
                            </div>
                        </div>
                        
                        <h4 class="font-bold text-dark mb-2 text-sm">A Solução & Resultado:</h4>
                        <p class="text-sm text-slate-600 leading-relaxed">Desenvolvemos um sistema que lê centenas de documentos financeiros num formato desestruturado. A IA extrai valores, categoriza despesas e exporta dashboards centralizados para a gestão do grupo. O processo que demorava dias é agora fechado em horas com precisão total.</p>
                    </div>
                </div>`;

    const casesEn = `
                <!-- Case Study 1 -->
                <div class="bg-white p-8 md:p-12 rounded-3xl border border-slate-200 shadow-sm reveal flex flex-col md:flex-row gap-8 items-center">
                    <div class="flex-1">
                        <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-xs font-bold uppercase tracking-wider mb-4">Portugal Textile</div>
                        <h3 class="text-2xl md:text-3xl font-display font-bold text-dark mb-4">Commercial & Order Automation</h3>
                        <p class="text-slate-600 leading-relaxed mb-6"><strong>The Problem:</strong> Receiving a high volume of complex email orders with scattered technical information created a constant need for manual validation, delaying customer responses.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">-80%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Admin Work</div>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">5x</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Faster Response</div>
                            </div>
                        </div>
                        
                        <h4 class="font-bold text-dark mb-2 text-sm">Solution & Result:</h4>
                        <p class="text-sm text-slate-600 leading-relaxed">We implemented an AI system that automatically analyzes all incoming orders, extracts technical specs, qualifies opportunities, and prepares draft replies. Data is organized directly into the CRM, ensuring immediate commercial follow-up and allowing the team to focus on selling rather than triaging.</p>
                    </div>
                </div>

                <!-- Case Study 2 -->
                <div class="bg-white p-8 md:p-12 rounded-3xl border border-slate-200 shadow-sm reveal flex flex-col md:flex-row gap-8 items-center">
                    <div class="flex-1">
                        <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-xs font-bold uppercase tracking-wider mb-4">Portugal Shoes</div>
                        <h3 class="text-2xl md:text-3xl font-display font-bold text-dark mb-4">Logistics Sync & Supplier Management</h3>
                        <p class="text-slate-600 leading-relaxed mb-6"><strong>The Problem:</strong> Tracking raw material shortages and communicating schedule changes to the factory involved dozens of phone calls and manual ERP updates, causing production delays.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">100%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Automated Tracking</div>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">-40%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Production Delays</div>
                            </div>
                        </div>
                        
                        <h4 class="font-bold text-dark mb-2 text-sm">Solution & Result:</h4>
                        <p class="text-sm text-slate-600 leading-relaxed">We built a logistics assistant that cross-references supplier data with internal planning. The AI automatically alerts the factory team about material delays, suggests schedule adjustments, and updates the order status in the ERP. The factory now operates with far fewer interruptions.</p>
                    </div>
                </div>

                <!-- Case Study 3 -->
                <div class="bg-white p-8 md:p-12 rounded-3xl border border-slate-200 shadow-sm reveal flex flex-col md:flex-row gap-8 items-center">
                    <div class="flex-1">
                        <div class="inline-block px-3 py-1 rounded-full bg-blue-50 text-accent text-xs font-bold uppercase tracking-wider mb-4">Absolutarget Group</div>
                        <h3 class="text-2xl md:text-3xl font-display font-bold text-dark mb-4">Document Analysis & Financial Reporting</h3>
                        <p class="text-slate-600 leading-relaxed mb-6"><strong>The Problem:</strong> Reconciling invoices, receipts, and expense reports across multiple group companies required weeks of manual work at month-end, with a high risk of human error.</p>
                        
                        <div class="grid grid-cols-2 gap-4 mb-6">
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">Days &rarr; Hrs</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Closing Time</div>
                            </div>
                            <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                                <div class="text-3xl font-display font-bold text-accent mb-1">99.9%</div>
                                <div class="text-xs font-medium text-slate-500 uppercase">Extraction Accuracy</div>
                            </div>
                        </div>
                        
                        <h4 class="font-bold text-dark mb-2 text-sm">Solution & Result:</h4>
                        <p class="text-sm text-slate-600 leading-relaxed">We developed a system that reads hundreds of unstructured financial documents. The AI extracts values, categorizes expenses, and exports centralized dashboards for group management. A process that used to take days is now closed in hours with total accuracy.</p>
                    </div>
                </div>`;

    const startMarker = '<div class="max-w-5xl mx-auto flex flex-col gap-16">';
    const startIdx = content.indexOf(startMarker);
    const endMarker = '            </div>\n        </section>';
    const endIdx = content.indexOf(endMarker, startIdx);

    if (startIdx !== -1 && endIdx !== -1) {
        const newCases = isPt ? casesPt : casesEn;
        const newContent = content.substring(0, startIdx + startMarker.length) + '\n' + newCases + '\n' + content.substring(endIdx);
        fs.writeFileSync(filePath, newContent, 'utf8');
        console.log('Updated', filePath);
    } else {
        console.log('Could not find markers in', filePath);
    }
}

replaceCases('/Users/pinto/Downloads/Mobizze2.0/pt/casos-estudo.html', true);
replaceCases('/Users/pinto/Downloads/Mobizze2.0/en/case-studies.html', false);
