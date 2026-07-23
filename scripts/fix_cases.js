const fs = require('fs');

function fixFile(indexFile, targetFile, oldFinancingLink, newFinancingLink, oldFinancingText, newFinancingText) {
    const indexHtml = fs.readFileSync(indexFile, 'utf8');
    
    // Extract nav block
    const navStart = indexHtml.indexOf('<nav id="navbar"');
    const navEnd = indexHtml.indexOf('</nav>') + 6;
    const navHtml = indexHtml.substring(navStart, navEnd);
    
    // Extract mobile menu block
    const mobileStart = indexHtml.indexOf('<div id="mobile-menu"');
    const mobileEnd = indexHtml.indexOf('<main>');
    const mobileHtml = indexHtml.substring(mobileStart, mobileEnd);

    // Now process target file
    let targetHtml = fs.readFileSync(targetFile, 'utf8');
    
    // Replace nav
    const tNavStart = targetHtml.indexOf('<nav id="navbar"');
    const tNavEnd = targetHtml.indexOf('</nav>') + 6;
    if (tNavStart !== -1 && tNavEnd !== -1) {
        targetHtml = targetHtml.substring(0, tNavStart) + navHtml + targetHtml.substring(tNavEnd);
    }
    
    // Check if mobile menu exists in target
    const tMobileStart = targetHtml.indexOf('<div id="mobile-menu"');
    if (tMobileStart !== -1) {
        // Replace existing
        const tMobileEnd = targetHtml.indexOf('<main>');
        targetHtml = targetHtml.substring(0, tMobileStart) + mobileHtml + targetHtml.substring(tMobileEnd);
    } else {
        // Insert before <main>
        const mainIdx = targetHtml.indexOf('<main>');
        if (mainIdx !== -1) {
            targetHtml = targetHtml.substring(0, mainIdx) + mobileHtml + targetHtml.substring(mainIdx);
        }
    }

    // Fix other links inside the content/footer
    targetHtml = targetHtml.replaceAll(oldFinancingLink, newFinancingLink);
    targetHtml = targetHtml.replaceAll(oldFinancingText, newFinancingText);
    
    if (targetFile.includes('pt/')) {
        targetHtml = targetHtml.replaceAll('../en/flexible-implementation-plans.html', '../en/financing.html');
    } else {
        targetHtml = targetHtml.replaceAll('Flexible Plans', 'Financing');
        targetHtml = targetHtml.replaceAll('../pt/planos-implementacao.html', '../pt/financiamento.html');
    }

    fs.writeFileSync(targetFile, targetHtml, 'utf8');
    console.log("Fixed", targetFile);
}

fixFile(
    '/Users/pinto/Downloads/Mobizze2.0/pt/index.html',
    '/Users/pinto/Downloads/Mobizze2.0/pt/casos-estudo.html',
    'planos-implementacao.html', 'financiamento.html',
    'Planos Flexíveis', 'Financiamento'
);

fixFile(
    '/Users/pinto/Downloads/Mobizze2.0/en/index.html',
    '/Users/pinto/Downloads/Mobizze2.0/en/case-studies.html',
    'flexible-implementation-plans.html', 'financing.html',
    'Flexible Implementation Plans', 'Financing'
);
