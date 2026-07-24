const fs = require('fs');
const path = require('path');

const rootDir = '/Users/pinto/Downloads/Mobizze2.0';
const ptDir = path.join(rootDir, 'pt');
const enDir = path.join(rootDir, 'en');

function injectSeoTags(dir, lang) {
    if (!fs.existsSync(dir)) return;
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

    for (const file of files) {
        const filePath = path.join(dir, file);
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Remove old tags if they exist to prevent duplication
        content = content.replace(/<!-- SEO Architecture -->[\s\S]*?x-default[\s\S]*?\/>\s*/g, '');

        const canonical = `https://mobizze.com/${lang}/${file === 'index.html' ? '' : file}`;
        const alternatePt = `https://mobizze.com/pt/${file === 'index.html' ? '' : file}`;
        const alternateEn = `https://mobizze.com/en/${file === 'index.html' ? '' : file}`;
        const alternateDefault = `https://mobizze.com/${file === 'index.html' ? '' : file}`;

        const seoBlock = `
    <!-- SEO Architecture -->
    <link rel="canonical" href="${canonical}" />
    <link rel="alternate" hreflang="pt" href="${alternatePt}" />
    <link rel="alternate" hreflang="en" href="${alternateEn}" />
    <link rel="alternate" hreflang="x-default" href="${alternateDefault}" />`;

        // Inject right before </head>
        content = content.replace('</head>', `${seoBlock}\n</head>`);
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Injected SEO into ${lang}/${file}`);
    }
}

injectSeoTags(ptDir, 'pt');
injectSeoTags(enDir, 'en');
