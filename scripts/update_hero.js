const fs = require('fs');

const ptHeroReplace = `                <h1 class="text-xs font-mono tracking-[0.2em] uppercase mb-6 text-accent animate-fade-in-up">Contrate o seu próximo melhor funcionário</h1>
                
                <h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">
                    Aumente as vendas sem <span class="text-accent">contratar mais pessoas</span>.
                </h2>
                
                <p class="max-w-2xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">
                    Implementamos colaboradores virtuais que trabalham 24 horas por dia, libertando a sua equipa humana para as tarefas de alto valor.
                </p>

                <!-- Metrics block -->
                <div class="mt-8 mb-4 grid grid-cols-2 md:flex md:flex-wrap justify-center gap-x-6 gap-y-3 text-sm font-medium text-slate-700 animate-fade-in-up delay-300">
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">⚡</span> Responde em &lt; 5 segundos</div>
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">🕒</span> Disponível 24/7, sem pausas</div>
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">📉</span> Até 70% menos trabalho administrativo</div>
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">🔗</span> Integra: WhatsApp, Email, CRM...</div>
                </div>
                
                <div class="mt-8 animate-fade-in-up delay-300">`;

const ptHeroSearch = `                <h1 class="text-xs font-mono tracking-[0.2em] uppercase mb-6 text-accent animate-fade-in-up">Acelere o seu negócio com IA</h1>
                
                <h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">
                    Transformamos problemas empresariais em <span class="text-accent">sistemas de IA personalizados</span>.
                </h2>
                
                <p class="max-w-xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">
                    Criamos agentes, automações e ferramentas que se integram nos seus processos para reduzir custos, recuperar tempo e acelerar o crescimento.
                </p>
                
                <div class="mt-10 animate-fade-in-up delay-300">`;

const enHeroReplace = `                <h1 class="text-xs font-mono tracking-[0.2em] uppercase mb-6 text-accent animate-fade-in-up">Hire your next best employee</h1>
                
                <h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">
                    Increase sales without <span class="text-accent">hiring more people</span>.
                </h2>
                
                <p class="max-w-2xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">
                    We deploy virtual employees that work 24/7, freeing your human team to focus on high-value tasks.
                </p>

                <!-- Metrics block -->
                <div class="mt-8 mb-4 grid grid-cols-2 md:flex md:flex-wrap justify-center gap-x-6 gap-y-3 text-sm font-medium text-slate-700 animate-fade-in-up delay-300">
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">⚡</span> Responds in &lt; 5 seconds</div>
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">🕒</span> Available 24/7, no breaks</div>
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">📉</span> Up to 70% less admin work</div>
                    <div class="flex items-center gap-2"><span class="text-accent text-lg">🔗</span> Integrates: WhatsApp, Email, CRM...</div>
                </div>
                
                <div class="mt-8 animate-fade-in-up delay-300">`;

const enHeroSearch = `                <h1 class="text-xs font-mono tracking-[0.2em] uppercase mb-6 text-accent animate-fade-in-up">AI Built for Your Business</h1>
                
                <h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">
                    We Transform Business Problems <span class="text-accent">Into Custom AI Systems</span>
                </h2>
                
                <p class="max-w-xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">
                    We build agents, automations, and tools that integrate into your processes to reduce costs, recover time, and accelerate growth.
                </p>
                
                <div class="mt-10 animate-fade-in-up delay-300">`;

function processHero(file, isPt) {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');

    if (isPt) {
        if (content.includes(ptHeroSearch)) {
            content = content.replace(ptHeroSearch, ptHeroReplace);
            fs.writeFileSync(file, content, 'utf8');
            console.log('Updated Hero in', file);
        } else {
            console.log('Could not find search string in', file);
        }
    } else {
        if (content.includes(enHeroSearch)) {
            content = content.replace(enHeroSearch, enHeroReplace);
            fs.writeFileSync(file, content, 'utf8');
            console.log('Updated Hero in', file);
        } else {
            console.log('Could not find search string in', file);
        }
    }
}

processHero('/Users/pinto/Downloads/Mobizze2.0/pt/index.html', true);
processHero('/Users/pinto/Downloads/Mobizze2.0/en/index.html', false);
