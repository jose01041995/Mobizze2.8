const fs = require('fs');
const path = require('path');

function replaceEmailInFiles(dir) {
    const files = fs.readdirSync(dir);
    
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        
        if (stat.isDirectory()) {
            if (file !== 'node_modules' && file !== '.git') {
                replaceEmailInFiles(fullPath);
            }
        } else if (fullPath.endsWith('.html') || fullPath.endsWith('.php')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            if (content.includes('contact@mobizze.com')) {
                content = content.replace(/contact@mobizze\.com/g, 'info@mobizze.com');
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log(`Updated: ${fullPath}`);
            }
        }
    }
}

replaceEmailInFiles('/Users/pinto/Downloads/Mobizze2.0');
console.log('Done!');
