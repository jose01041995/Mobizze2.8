const fs = require('fs');

function processSecurity(file, isPt) {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');

    if (file.includes('index.html')) {
        if (isPt) {
            content = content.replace(
                'Os seus dados da empresa e dos seus clientes nunca são partilhados com terceiros nem usados para treinar modelos públicos de IA.',
                'Os dados não são utilizados para treinar modelos públicos de IA nem vendidos a terceiros. O processamento ocorre através de fornecedores tecnológicos certificados, sujeitos a Acordos de Tratamento de Dados (DPA) rigorosos.'
            );
        } else {
            content = content.replace(
                'Your company and customer data are never shared with third parties or used to train public AI models.',
                'Data is not used to train public AI models nor sold to third parties. Processing is handled through certified tech providers under strict Data Processing Agreements (DPA).'
            );
        }
    } else if (file.includes('privacidade.html') || file.includes('privacy.html')) {
        if (isPt) {
            content = content.replace(
                'Podemos partilhar informações com fornecedores de serviços que nos auxiliam na operação do nosso negócio (ex: alojamento de site, análise de dados), que são obrigados a manter a confidencialidade das suas informações.',
                'Partilhamos informações apenas com subprocessadores estritamente necessários para a operação do serviço (ex: infraestrutura cloud, fornecedores de modelos LLM). Estes parceiros atuam sob Acordos de Tratamento de Dados (DPA) formais e são proibidos de utilizar os dados para os seus próprios fins.'
            );
        } else {
            content = content.replace(
                'We may share information with service providers who assist us in operating our business (e.g., website hosting, data analysis), who are obligated to keep your information confidential.',
                'We only share information with sub-processors strictly necessary to operate the service (e.g., cloud infrastructure, LLM providers). These partners operate under formal Data Processing Agreements (DPA) and are prohibited from using the data for their own purposes.'
            );
        }
    } else if (file.includes('seguranca.html') || file.includes('security.html')) {
        if (isPt) {
            content = content.replace(
                'assegurando que os dados não são partilhados publicamente.',
                'assegurando que os dados não são utilizados para treinar modelos públicos e que a soberania e retenção de dados são controladas.'
            );
        } else {
            content = content.replace(
                'ensuring data is not shared publicly.',
                'ensuring data is not used to train public models and that data sovereignty and retention are strictly controlled.'
            );
        }
    }

    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated Security in', file);
}

const files = [
    { name: 'pt/index.html', pt: true },
    { name: 'en/index.html', pt: false },
    { name: 'pt/privacidade.html', pt: true },
    { name: 'en/privacy.html', pt: false },
    { name: 'pt/seguranca.html', pt: true },
    { name: 'en/security.html', pt: false }
];

files.forEach(f => {
    processSecurity('/Users/pinto/Downloads/Mobizze2.0/' + f.name, f.pt);
});
