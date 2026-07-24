const fs = require('fs');

function processContact(file) {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');

    const fetchBlock = `
                    const formData = {
                        nome: document.getElementById('nome').value,
                        empresa: document.getElementById('empresa').value,
                        email: document.getElementById('email').value,
                        telefone: document.getElementById('telefone').value,
                        desafio: document.getElementById('desafio').value,
                        detalhes: document.getElementById('detalhes').value
                    };

                    fetch('../contact.php', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log('Success:', data);
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
`;

    if (file.includes('pt/contacto.html')) {
        content = content.replace(
            `                    e.preventDefault(); // Impede o recarregamento da página`,
            `                    e.preventDefault(); // Impede o recarregamento da página\n${fetchBlock}`
        );
    } else {
        content = content.replace(
            `                    e.preventDefault();`,
            `                    e.preventDefault();\n${fetchBlock}`
        );
    }

    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated Form in', file);
}

processContact('/Users/pinto/Downloads/Mobizze2.0/pt/contacto.html');
processContact('/Users/pinto/Downloads/Mobizze2.0/en/contact.html');
