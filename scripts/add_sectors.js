const fs = require('fs');
const path = require('path');

const PT_DIR = "/Users/pinto/Downloads/Mobizze2.0/pt";
const EN_DIR = "/Users/pinto/Downloads/Mobizze2.0/en";

const PT_SECTORS = `
                <!-- Dropdown Setores -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Setores <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Hitbox Invisível e Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-[400px] z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-4 grid grid-cols-2 gap-2">
                            <a href="setor-advogados.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Advogados</a>
                            <a href="setor-agricultura.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agricultura</a>
                            <a href="setor-clinicas-saude.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Clínicas & Saúde</a>
                            <a href="setor-construcao.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Construção</a>
                            <a href="setor-contabilidade.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Contabilidade</a>
                            <a href="setor-ecommerce.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">E-commerce</a>
                            <a href="setor-educacao.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Educação</a>
                            <a href="setor-ginasios.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Ginásios</a>
                            <a href="setor-imobiliarias.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Imobiliárias</a>
                            <a href="setor-industria.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Indústria</a>
                            <a href="setor-oficinas.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Oficinas</a>
                            <a href="setor-restaurantes.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Restaurantes</a>
                            <a href="setor-retalho.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Retalho</a>
                            <a href="setor-saloes-estetica.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Salões & Estética</a>
                            <a href="setor-suporte-b2b.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Suporte B2B</a>
                            <a href="setor-turismo.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Turismo</a>
                            <div class="col-span-2 h-px bg-slate-100 my-1 mx-2"></div>
                            <a href="setores.html" class="col-span-2 px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-semibold transition-colors text-center">Ver todos os setores &rarr;</a>
                        </div>
                    </div>
                </div>
                <a href="sobre.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Sobre Nós</a>`;

const EN_SECTORS = `
                <!-- Dropdown Sectors -->
                <div class="relative group flex items-center h-full">
                    <button class="text-xs font-medium text-slate-600 group-hover:text-accent transition-colors duration-300 tracking-wide flex items-center gap-1 cursor-pointer">Sectors <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform duration-300 group-hover:-rotate-180"><path d="m6 9 6 6 6-6"></path></svg></button>
                    <!-- Invisible Hitbox and Menu -->
                    <div class="absolute top-full left-1/2 -translate-x-1/2 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 w-[400px] z-50">
                        <div class="bg-white rounded-2xl shadow-[0_10px_40px_-10px_rgba(0,0,0,0.1)] border border-slate-100 p-4 grid grid-cols-2 gap-2">
                            <a href="sector-accounting.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Accounting</a>
                            <a href="sector-agriculture.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Agriculture</a>
                            <a href="sector-b2b-support.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">B2B Support</a>
                            <a href="sector-clinics-health.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Clinics & Health</a>
                            <a href="sector-construction.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Construction</a>
                            <a href="sector-ecommerce.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">E-commerce</a>
                            <a href="sector-education.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Education</a>
                            <a href="sector-gyms.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Gyms</a>
                            <a href="sector-industry.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Industry</a>
                            <a href="sector-lawyers.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Lawyers</a>
                            <a href="sector-real-estate.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Real Estate</a>
                            <a href="sector-restaurants.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Restaurants</a>
                            <a href="sector-retail.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Retail</a>
                            <a href="sector-salons-aesthetics.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Salons & Aesthetics</a>
                            <a href="sector-tourism.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Tourism</a>
                            <a href="sector-workshops.html" class="px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Workshops</a>
                            <div class="col-span-2 h-px bg-slate-100 my-1 mx-2"></div>
                            <a href="sectors.html" class="col-span-2 px-3 py-2 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-semibold transition-colors text-center">View all sectors &rarr;</a>
                        </div>
                    </div>
                </div>
                <a href="about.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">About Us</a>`;

function processFile(filepath, isPt) {
    let content = fs.readFileSync(filepath, 'utf8');
    
    if (isPt) {
        if (!content.includes('<!-- Dropdown Setores -->')) {
            content = content.replace('<a href="sobre.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">Sobre Nós</a>', PT_SECTORS);
        }
    } else {
        if (!content.includes('<!-- Dropdown Sectors -->')) {
            content = content.replace('<a href="about.html" class="text-xs font-medium text-slate-600 hover:text-accent transition-colors duration-300 tracking-wide">About Us</a>', EN_SECTORS);
        }
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
