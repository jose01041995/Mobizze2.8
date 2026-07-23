const fs = require('fs');

const ptSection = `
        <!-- Hero Section -->
        <section class="relative w-full overflow-hidden bg-white pt-32 pb-20 md:pt-40 md:pb-28">
            <div class="absolute top-0 left-0 w-full h-full pointer-events-none" style="background: radial-gradient(ellipse 80% 100% at 50% -20%, rgba(239, 246, 255, 0.8) 0%, rgba(255,255,255,0) 100%);"></div>
            
            <div class="max-w-4xl mx-auto px-6 w-full relative z-10 text-center">
                <h1 class="text-xs font-mono tracking-[0.2em] uppercase mb-4 text-accent animate-fade-in-up">A Nossa História</h1>
                <h2 class="font-display font-bold text-dark leading-[1.1] tracking-tight mb-6 animate-fade-in-up delay-100" style="font-size: clamp(2.5rem, 5vw, 4rem);">
                    Nascida de <span class="text-accent">Empresas Reais</span>
                </h2>
                <p class="text-lg text-slate-600 leading-relaxed max-w-3xl mx-auto animate-fade-in-up delay-200 font-medium">
                    A Mobizze nasceu da necessidade de resolver problemas reais dentro das nossas próprias empresas. Hoje aplicamos essa experiência para ajudar outras organizações.
                </p>
                
                <!-- Team Photo Placeholder -->
                <div class="mt-12 animate-fade-in-up delay-300">
                    <div class="w-full max-w-3xl mx-auto h-[400px] md:h-[500px] bg-slate-100 rounded-3xl border border-slate-200 flex flex-col items-center justify-center text-slate-400 overflow-hidden relative shadow-lg shadow-blue-900/5">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="mb-4 opacity-50"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                        <span class="font-mono text-sm tracking-widest uppercase opacity-70">[FOTO-EQUIPA.jpg]</span>
                        <div class="absolute inset-0 bg-gradient-to-t from-slate-900/10 to-transparent"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Mission & Values Section -->
        <section class="relative px-6 py-24 bg-slate-50 border-y border-slate-200">
            <div class="max-w-5xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 md:gap-16 items-center">
                <div class="reveal">
                    <h3 class="text-3xl font-display font-bold text-dark tracking-tight mb-6">A Nossa <span class="text-accent">Origem</span></h3>
                    <div class="space-y-4 text-slate-600 leading-relaxed">
                        <p>A Mobizze não nasceu de um grupo de programadores à procura de um problema para resolver com Inteligência Artificial. Nasceu de líderes empresariais e fundadores do <strong class="text-dark">Grupo Absolutarget</strong>, a procurar soluções para problemas reais nas suas operações industriais e logísticas.</p>
                        <p>Após automatizarmos com sucesso processos complexos na <strong class="text-dark">Portugal Textile</strong> e na <strong class="text-dark">Portugal Shoes</strong> — desde o processamento comercial à logística — percebemos o impacto brutal que estas ferramentas personalizadas têm na rentabilidade. Agora, construímos esses mesmos sistemas robustos para o seu negócio.</p>
                    </div>
                </div>
`;

const enSection = `
        <!-- Hero Section -->
        <section class="relative w-full overflow-hidden bg-white pt-32 pb-20 md:pt-40 md:pb-28">
            <div class="absolute top-0 left-0 w-full h-full pointer-events-none" style="background: radial-gradient(ellipse 80% 100% at 50% -20%, rgba(239, 246, 255, 0.8) 0%, rgba(255,255,255,0) 100%);"></div>
            
            <div class="max-w-4xl mx-auto px-6 w-full relative z-10 text-center">
                <h1 class="text-xs font-mono tracking-[0.2em] uppercase mb-4 text-accent animate-fade-in-up">Our Story</h1>
                <h2 class="font-display font-bold text-dark leading-[1.1] tracking-tight mb-6 animate-fade-in-up delay-100" style="font-size: clamp(2.5rem, 5vw, 4rem);">
                    Born from <span class="text-accent">Real Companies</span>
                </h2>
                <p class="text-lg text-slate-600 leading-relaxed max-w-3xl mx-auto animate-fade-in-up delay-200 font-medium">
                    Mobizze was born out of the necessity to solve real problems within our own companies. Today we apply that experience to help other organizations.
                </p>
                
                <!-- Team Photo Placeholder -->
                <div class="mt-12 animate-fade-in-up delay-300">
                    <div class="w-full max-w-3xl mx-auto h-[400px] md:h-[500px] bg-slate-100 rounded-3xl border border-slate-200 flex flex-col items-center justify-center text-slate-400 overflow-hidden relative shadow-lg shadow-blue-900/5">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="mb-4 opacity-50"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                        <span class="font-mono text-sm tracking-widest uppercase opacity-70">[TEAM-PHOTO.jpg]</span>
                        <div class="absolute inset-0 bg-gradient-to-t from-slate-900/10 to-transparent"></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Mission & Values Section -->
        <section class="relative px-6 py-24 bg-slate-50 border-y border-slate-200">
            <div class="max-w-5xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 md:gap-16 items-center">
                <div class="reveal">
                    <h3 class="text-3xl font-display font-bold text-dark tracking-tight mb-6">Our <span class="text-accent">Origin</span></h3>
                    <div class="space-y-4 text-slate-600 leading-relaxed">
                        <p>Mobizze wasn't started by a group of developers looking for a problem to solve with Artificial Intelligence. It was founded by business leaders from the <strong class="text-dark">Absolutarget Group</strong>, looking for solutions to real problems in their industrial and logistics operations.</p>
                        <p>After successfully automating complex processes at <strong class="text-dark">Portugal Textile</strong> and <strong class="text-dark">Portugal Shoes</strong> — from commercial processing to logistics — we realized the massive impact these custom tools have on profitability. Now, we build these same robust systems for your business.</p>
                    </div>
                </div>
`;

function processAbout(file, isPt) {
    let content = fs.readFileSync(file, 'utf8');

    const startMarker = '<!-- Hero Section -->';
    const startIdx = content.indexOf(startMarker);
    const endMarker = '<div class="grid grid-cols-1 sm:grid-cols-2 gap-6 reveal delay-100">';
    const endIdx = content.indexOf(endMarker);

    if (startIdx !== -1 && endIdx !== -1) {
        const newSection = isPt ? ptSection : enSection;
        content = content.substring(0, startIdx) + newSection + '                ' + content.substring(endIdx);
        fs.writeFileSync(file, content, 'utf8');
        console.log('Updated About Us in', file);
    } else {
        console.log('Markers not found in', file);
    }
}

processAbout('/Users/pinto/Downloads/Mobizze2.0/pt/sobre.html', true);
processAbout('/Users/pinto/Downloads/Mobizze2.0/en/about.html', false);
