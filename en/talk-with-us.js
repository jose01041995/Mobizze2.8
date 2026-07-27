(function() {
    const messagesContainer = document.getElementById('ai-chat-messages');
    const inputField = document.getElementById('ai-chat-input');
    const sendBtn = document.getElementById('ai-chat-send');
    
    let isWaitingForResponse = false;
    let apiHistory = [
        { 
            role: "system", 
            content: "You are a virtual assistant for Mobizze specialized in receiving new contacts. Your goal is to collect the following user data in a friendly, conversational manner: Name, Company, Email (MANDATORY AND VALID), Phone (optional), and their biggest current Challenge. CRITICAL GOLDEN RULE: EMAIL IS 100% MANDATORY! NEVER, under any circumstance, proceed to the next question or call the 'enviar_formulario' function without the user providing a valid email address (containing '@' and a domain). If the user refuses or gives an invalid email, politely explain that the email is essential for our team to reach out and insist until a valid email is provided. Only call 'enviar_formulario' once you have collected Name, Company, a VALID Email, and Challenge. Always respond in English and keep your answers brief." 
        }
    ];

    function appendMessage(role, text) {
        const msgDiv = document.createElement('div');
        msgDiv.className = 'mbz-msg-page ' + role;
        if (role === 'system') { msgDiv.innerHTML = text; } else { msgDiv.textContent = text; }
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    appendMessage('bot', "Hello! \ud83d\udc4b Welcome to Mobizze. I am here to help you get in touch. To serve you best, whom am I speaking with?");

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
                    appendMessage('bot', "To proceed with your request and get in touch, we require a valid email address with an '@' symbol and domain. Could you please provide your email address?");
                    apiHistory.push({ role: "assistant", content: "To proceed with your request and get in touch, we require a valid email address with an '@' symbol and domain. Could you please provide your email address?" });
                    return;
                }
                
                appendMessage('bot', "Thank you " + args.nome + "! I will prepare your request for submission. A member of our team will be in touch shortly.");
                
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
                inputField.placeholder = "Request submitted successfully!";
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
            appendMessage('bot', "Sorry, a connection error occurred. Please try again.");
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
