const fs = require('fs');
const path = require('path');

const PT_DIR = "/Users/pinto/Downloads/Mobizze2.0/pt";
const EN_DIR = "/Users/pinto/Downloads/Mobizze2.0/en";

// Rename files
const ptOldFile = path.join(PT_DIR, "planos-implementacao.html");
const ptNewFile = path.join(PT_DIR, "financiamento.html");
if (fs.existsSync(ptOldFile)) {
    fs.renameSync(ptOldFile, ptNewFile);
}

const enOldFile = path.join(EN_DIR, "flexible-implementation-plans.html");
const enNewFile = path.join(EN_DIR, "financing.html");
if (fs.existsSync(enOldFile)) {
    fs.renameSync(enOldFile, enNewFile);
}

const PT_NAV = `            <div class="hidden md:flex items-center gap-6 h-full">
                <!-- Dropdown Serviços -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Serviços <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Hitbox Invisível e Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-64 z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-2 flex flex-col gap-1">
                            <a href="chatbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Chatbot</a>
                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>
                            <a href="qualificar-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualificar Leads CRM</a>
                            <a href="agendar-reunioes.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agendar Reuniões</a>
                            <a href="agentes-de-voz.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Voz</a>
                            <a href="agentes-de-texto.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agentes de Texto</a>
                            <a href="redes-sociais.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Redes Sociais</a>
                        </div>
                    </div>
                </div>
                <a href="sobre.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Sobre Nós</a>
                <a href="financiamento.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Financiamento</a>
                <a href="index.html#faq" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">FAQ</a>
            </div>`;

const PT_MOBILE_NAV = `            <div>
                <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Serviços</div>
                <div class="flex flex-col gap-4">
                    <a href="chatbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Chatbot</a>
                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>
                    <a href="qualificar-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualificar CRM</a>
                    <a href="agendar-reunioes.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agendar Reuniões</a>
                    <a href="agentes-de-voz.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Voz</a>
                    <a href="agentes-de-texto.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Agentes de Texto</a>
                    <a href="redes-sociais.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Redes Sociais</a>
                </div>
            </div>
            
            <div class="h-px w-full bg-slate-100"></div>
            
            <div class="flex flex-col gap-5">
                <a href="sobre.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Sobre Nós</a>
                <a href="financiamento.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Financiamento</a>
                <a href="index.html#faq" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">FAQ</a>
            </div>`;

const EN_NAV = `            <div class="hidden md:flex items-center gap-6 h-full">
                <!-- Dropdown Services -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Services <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Invisible Hitbox and Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-64 z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-2 flex flex-col gap-1">
                            <a href="chatbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Chatbot</a>
                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>
                            <a href="qualify-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualify Leads CRM</a>
                            <a href="schedule-meetings.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Schedule Meetings</a>
                            <a href="voice-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Voice Agents</a>
                            <a href="conversational-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Text Agents</a>
                            <a href="social-media.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Social Media</a>
                        </div>
                    </div>
                </div>
                <a href="about.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">About Us</a>
                <a href="financing.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Financing</a>
                <a href="index.html#faq" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">FAQ</a>
            </div>`;

const EN_MOBILE_NAV = `            <div>
                <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Services</div>
                <div class="flex flex-col gap-4">
                    <a href="chatbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Chatbot</a>
                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>
                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>
                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>
                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>
                    <a href="conversational-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Text Agents</a>
                    <a href="social-media.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Social Media</a>
                </div>
            </div>
            
            <div class="h-px w-full bg-slate-100"></div>
            
            <div class="flex flex-col gap-5">
                <a href="about.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">About Us</a>
                <a href="financing.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Financing</a>
                <a href="index.html#faq" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">FAQ</a>
            </div>`;

function processFile(filepath, isPt) {
    let content = fs.readFileSync(filepath, 'utf8');
    
    if (isPt) {
        // Desktop nav replace
        content = content.replace(/<div class="hidden md:flex items-center gap-6 h-full">.*?<a href="contacto\.html"/s, PT_NAV + '\n            <a href="contacto.html"');
        // Mobile nav replace
        content = content.replace(/<div>\s*<div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Serviços<\/div>.*?<a href="contacto\.html"/s, PT_MOBILE_NAV + '\n            </div>\n            \n            <!-- Link para a página de contacto -->\n            <div class="mt-auto pt-6">\n                <a href="contacto.html"');
        
        // Link replacement
        content = content.replace(/planos-implementacao\.html/g, 'financiamento.html');
        content = content.replace(/Planos Flexíveis/g, 'Financiamento');
        content = content.replace(/\.\.\/en\/flexible-implementation-plans\.html/g, '../en/financing.html');
    } else {
        // Desktop nav replace
        content = content.replace(/<div class="hidden md:flex items-center gap-6 h-full">.*?<a href="contact\.html"/s, EN_NAV + '\n            <a href="contact.html"');
        // Mobile nav replace
        content = content.replace(/<div>\s*<div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-4">Services<\/div>.*?<a href="contact\.html"/s, EN_MOBILE_NAV + '\n            </div>\n            \n            <!-- Contact page link -->\n            <div class="mt-auto pt-6">\n                <a href="contact.html"');
        
        // Link replacement
        content = content.replace(/flexible-implementation-plans\.html/g, 'financing.html');
        content = content.replace(/Flexible Implementation Plans/g, 'Financing');
        content = content.replace(/Flexible Plans/g, 'Financing');
        content = content.replace(/\.\.\/pt\/planos-implementacao\.html/g, '../pt/financiamento.html');
    }
    
    fs.writeFileSync(filepath, content, 'utf8');
}

fs.readdirSync(PT_DIR).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(PT_DIR, file), true);
    }
});

fs.readdirSync(EN_DIR).forEach(file => {
    if (file.endsWith('.html')) {
        processFile(path.join(EN_DIR, file), false);
    }
});

console.log("Done");
