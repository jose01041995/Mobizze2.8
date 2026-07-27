(function() {
    const messagesContainer = document.getElementById('ai-chat-messages');
    const inputField = document.getElementById('ai-chat-input');
    const sendBtn = document.getElementById('ai-chat-send');
    
    let isWaitingForResponse = false;
    let apiHistory = [
        { 
            role: "system", 
            content: "\u00c9s um assistente virtual da Mobizze especializado em receber novos contactos. O teu objetivo \u00e9 recolher os seguintes dados do utilizador de forma amig\u00e1vel e conversacional: Nome, Empresa, Email (OBRIGAT\u00d3RIO E V\u00c1LIDO), Telefone (opcional), e qual \u00e9 o seu maior Desafio atual. REGRA DE OURO CR\u00cdTICA: O EMAIL \u00c9 100% OBRIGAT\u00d3RIO! NUNCA, SOB NENHUMA CIRCUNST\u00c2NCIA, avances para a pr\u00f3xima pergunta ou chames a fun\u00e7\u00e3o 'enviar_formulario' sem antes o utilizador ter fornecido um endere\u00e7o de e-mail perfeitamente v\u00e1lido (que contenha '@' e um dom\u00ednio como '.com', '.pt', etc.). Se o utilizador recusar dar o email, ou der um email inv\u00e1lido, explica educadamente que o e-mail \u00e9 indispens\u00e1vel para que a equipa da Mobizze possa entrar em contacto e insiste at\u00e9 receber um e-mail v\u00e1lido. S\u00f3 podes chamar 'enviar_formulario' quando tiveres recolhido Nome, Empresa, um E-mail V\u00c1LIDO e o Desafio. Responde sempre em Portugu\u00eas de Portugal e s\u00ea sucinto." 
        }
    ];

    function appendMessage(role, text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'mbz-msg-page ' + role;
        if (role === 'system') { msgDiv.innerHTML = text; } else { msgDiv.textContent = text; }
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    appendMessage('bot', "Ol\u00e1! \ud83d\udc4b Bem-vindo \u00e0 Mobizze. Estou aqui para ajudar com o seu contacto. Para podermos dar o melhor seguimento, com quem estou a falar?");

    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'mbz-msg-page bot mbz-typing-container';
        typingDiv.id = 'ai-typing-indicator';
        typingDiv.innerHTML = '<div class="flex gap-1 py-1"><div class="mbz-dot-page"></div><div class="mbz-dot-page"></div><div class="mbz-dot-page"></div></div>';
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function removeTyping() {
        const indicator = document.getElementById('ai-typing-indicator');
        if (indicator) indicator.remove();
    }

    function triggerMailtoFallback(data) {
        const subject = encodeURIComponent('Novo Pedido via Chatbot - ' + data.empresa);
        const body = encodeURIComponent('Nome: ' + data.nome + '\nEmpresa: ' + data.empresa + '\nEmail: ' + data.email + '\nTelefone: ' + (data.telefone || 'N/A') + '\nDesafio: ' + data.desafio + '\nDetalhes: ' + (data.detalhes || 'N/A'));
        window.location.href = 'mailto:info@mobizze.com?subject=' + subject + '&body=' + body;
    }

    async function handleSend() {
        const text = inputField.value.trim();
        if (!text || isWaitingForResponse) return;
        let formSubmitted = false;

        appendMessage('user', text);
        inputField.value = '';
        apiHistory.push({ role: "user", content: text });

        isWaitingForResponse = true;
        inputField.disabled = true;
        sendBtn.disabled = true;
        showTyping();

        try {
            const response = await fetch('../chat_api.php', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    model: 'gpt-4o-mini',
                    messages: apiHistory,
                    temperature: 0.7,
                    tools: [{
                        type: "function",
                        function: {
                            name: "enviar_formulario",
                            description: "Aciona o envio do formulário de contacto após recolheres todos os dados obrigatórios do utilizador, INCLUINDO EMAIL VÁLIDO.",
                            parameters: {
                                type: "object",
                                properties: {
                                    nome: { type: "string" },
                                    empresa: { type: "string" },
                                    email: { type: "string", description: "Endereço de e-mail absolutamente OBRIGATÓRIO e válido (com @ e domínio)" },
                                    telefone: { type: "string" },
                                    desafio: { type: "string" },
                                    detalhes: { type: "string", description: "Qualquer informação ou detalhe adicional fornecido pelo utilizador" }
                                },
                                required: ["nome", "empresa", "email", "desafio"]
                            }
                        }
                    }],
                    tool_choice: "auto"
                })
            });

            if (!response.ok) throw new Error('API Error');

            const data = await response.json();
            const messageObj = data.choices[0].message;

            removeTyping();

            if (messageObj.tool_calls && messageObj.tool_calls.length > 0) {
                const toolCall = messageObj.tool_calls[0];
                const args = JSON.parse(toolCall.function.arguments);
                
                // CLIENT-SIDE GUARDRAIL: Verify if email is actually present and valid!
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!args.email || !emailRegex.test(args.email)) {
                    appendMessage('bot', "Para podermos dar seguimento ao seu pedido e entrar em contacto, necessitamos de um endere\u00e7o de e-mail v\u00e1lido com '@' e dom\u00ednio. Poderia indicar o seu e-mail corporativo ou pessoal, por favor?");
                    apiHistory.push({ role: "assistant", content: "Para podermos dar seguimento ao seu pedido e entrar em contacto, necessitamos de um endere\u00e7o de e-mail v\u00e1lido com '@' e dom\u00ednio. Poderia indicar o seu e-mail corporativo ou pessoal, por favor?" });
                    return;
                }
                
                appendMessage('bot', "Obrigado " + args.nome + "! Vou preparar o envio do seu pedido. Um elemento da nossa equipa entrar\u00e1 em contacto muito brevemente.");
                
                try {
                    fetch('../contact.php', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(args)
                    }).then(async res => {
                        const resData = await res.json().catch(() => ({}));
                        if (!res.ok || !resData.success) {
                            console.error('PHP mail failed on server:', resData.message);
                            triggerMailtoFallback(args);
                        }
                    }).catch(e => triggerMailtoFallback(args));
                } catch(e) {
                    triggerMailtoFallback(args);
                }

                formSubmitted = true;
                inputField.disabled = true;
                inputField.placeholder = "Pedido enviado com sucesso!";
                sendBtn.disabled = true;
                return;
            }

            const botReply = messageObj.content;
            if (botReply) {
                appendMessage('bot', botReply);
                apiHistory.push({ role: "assistant", content: botReply });
            }

        } catch (error) {
            removeTyping();
            appendMessage('bot', "Desculpe, ocorreu um erro de liga\u00e7\u00e3o. Tente novamente.");
            apiHistory.pop();
        } finally {
            isWaitingForResponse = false;
            if(!formSubmitted) {
                inputField.disabled = false;
                sendBtn.disabled = false;
                inputField.focus();
            }
        }
    }

    sendBtn.addEventListener('click', handleSend);
    inputField.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });
})();
