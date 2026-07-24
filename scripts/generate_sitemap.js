const fs = require('fs');
const path = require('path');

const rootDir = '/Users/pinto/Downloads/Mobizze2.0';
const ptDir = path.join(rootDir, 'pt');
const enDir = path.join(rootDir, 'en');
const baseUrl = 'https://mobizze.com';

function getUrls(dir, prefix) {
    if (!fs.existsSync(dir)) return [];
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
    return files.map(file => {
        const route = file === 'index.html' ? '' : file;
        return `${baseUrl}/${prefix}/${route}`;
    });
}

const ptUrls = getUrls(ptDir, 'pt');
const enUrls = getUrls(enDir, 'en');

const sitemapContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
${ptUrls.map(url => `  <url>\n    <loc>${url}</loc>\n  </url>`).join('\n')}
${enUrls.map(url => `  <url>\n    <loc>${url}</loc>\n  </url>`).join('\n')}
</urlset>`;

fs.writeFileSync(path.join(rootDir, 'sitemap.xml'), sitemapContent, 'utf8');
console.log('Generated sitemap.xml with', ptUrls.length + enUrls.length, 'URLs.');

const robotsTxt = `User-agent: *
Allow: /
Sitemap: ${baseUrl}/sitemap.xml`;

fs.writeFileSync(path.join(rootDir, 'robots.txt'), robotsTxt, 'utf8');
console.log('Generated robots.txt');

// Update package.json to include sitemap.xml and robots.txt in build
const pkgPath = path.join(rootDir, 'package.json');
let pkg = fs.readFileSync(pkgPath, 'utf8');
pkg = pkg.replace('contact.php api dist/', 'contact.php api sitemap.xml robots.txt dist/');
fs.writeFileSync(pkgPath, pkg, 'utf8');
console.log('Updated package.json to include sitemap and robots');
