const fs = require('fs');
const path = require('path');

const PT_DIR = "/Users/pinto/Downloads/Mobizze2.0/pt";
const EN_DIR = "/Users/pinto/Downloads/Mobizze2.0/en";

const PT_MOBILE_LINK = '<a href="setores.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Setores</a>\n                ';
const EN_MOBILE_LINK = '<a href="sectors.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Sectors</a>\n                ';

function processFile(filepath, isPt) {
    let content = fs.readFileSync(filepath, 'utf8');
    
    if (isPt) {
        if (!content.includes('href="setores.html" class="mobile-link text-xl')) {
            content = content.replace(
                '<a href="sobre.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Sobre Nós</a>',
                PT_MOBILE_LINK + '<a href="sobre.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">Sobre Nós</a>'
            );
        }
    } else {
        if (!content.includes('href="sectors.html" class="mobile-link text-xl')) {
            content = content.replace(
                '<a href="about.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">About Us</a>',
                EN_MOBILE_LINK + '<a href="about.html" class="mobile-link text-xl font-display font-bold text-slate-800 hover:text-accent">About Us</a>'
            );
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

console.log("Done adding mobile links");
