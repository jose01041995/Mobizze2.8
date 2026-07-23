const fs = require('fs');

function fixFooter(indexFile, targetFile) {
    const indexHtml = fs.readFileSync(indexFile, 'utf8');
    
    // Extract footer block
    const footerStart = indexHtml.indexOf('<footer class="relative border-t border-slate-200 bg-white overflow-hidden">');
    const footerEnd = indexHtml.indexOf('</footer>') + 9;
    const footerHtml = indexHtml.substring(footerStart, footerEnd);
    
    // Now process target file
    let targetHtml = fs.readFileSync(targetFile, 'utf8');
    
    // Replace footer
    const tFooterStart = targetHtml.indexOf('<footer');
    const tFooterEnd = targetHtml.indexOf('</footer>') + 9;
    if (tFooterStart !== -1 && tFooterEnd !== -1) {
        targetHtml = targetHtml.substring(0, tFooterStart) + footerHtml + targetHtml.substring(tFooterEnd);
        fs.writeFileSync(targetFile, targetHtml, 'utf8');
        console.log("Fixed footer in", targetFile);
    } else {
        console.log("Could not find footer in", targetFile);
    }
}

fixFooter(
    '/Users/pinto/Downloads/Mobizze2.0/pt/index.html',
    '/Users/pinto/Downloads/Mobizze2.0/pt/casos-estudo.html'
);

fixFooter(
    '/Users/pinto/Downloads/Mobizze2.0/en/index.html',
    '/Users/pinto/Downloads/Mobizze2.0/en/case-studies.html'
);
