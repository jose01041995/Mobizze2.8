(function() {
    // Bot Configuration
    const API_KEY = "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";
    let userMessageCount = 0;
    let isOpen = false;
    let isWaitingForResponse = false;

    // Conversation history for API (OpenAI)
    let apiHistory = [
        { 
            role: "system", 
            content: "You are an intelligent virtual assistant for Mobizze, an AI agency. You are friendly, direct, and professional. Always reply in English. Your goal is to help the user understand the power of automation, but responses must be concise (max 2-3 short sentences)." 
        }
    ];

    // History to keep in the UI
    let uiMessages = [];

    // Function to save data and keep chat active after page refresh
    function saveState() {
        // We use a different key (_en) so it doesn't conflict with the PT version
        localStorage.setItem('mbz_chat_state_en', JSON.stringify({
            apiHistory,
            uiMessages,
            userMessageCount
        }));
    }

    const styles = `
        #mbz-widget { position: fixed; bottom: 24px; right: 24px; z-index: 999999; font-family: 'Inter', system-ui, sans-serif; }
        
        #mbz-toggle { background: #2563eb; color: white; border: none; border-radius: 9999px; padding: 14px 28px; font-weight: 600; font-size: 14px; cursor: pointer; box-shadow: 0 10px 25px -5px rgba(37,99,235,0.4); display: flex; align-items: center; gap: 8px; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
        #mbz-toggle:hover { transform: translateY(-3px); box-shadow: 0 20px 25px -5px rgba(37,99,235,0.3); background: #1d4ed8; }
        #mbz-toggle svg { width: 20px; height: 20px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
        
        #mbz-chat { display: none; width: min(360px, calc(100vw - 48px)); height: 550px; max-height: calc(100vh - 100px); background: #ffffff; border-radius: 20px; box-shadow: 0 20px 60px -15px rgba(0,0,0,0.15); flex-direction: column; overflow: hidden; border: 1px solid #e2e8f0; margin-bottom: 20px; transform-origin: bottom right; }
        #mbz-chat.mbz-open { display: flex; animation: mbz-pop-in 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        
        @keyframes mbz-pop-in { 0% { opacity: 0; transform: scale(0.8) translateY(20px); } 100% { opacity: 1; transform: scale(1) translateY(0); } }
        
        #mbz-header { background: #2563eb; color: white; padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; }
        #mbz-header-title { font-weight: 600; font-size: 15px; display: flex; align-items: center; gap: 8px; }
        #mbz-header-title span.status { display: block; width: 8px; height: 8px; background: #4ade80; border-radius: 50%; box-shadow: 0 0 0 2px rgba(74,222,128,0.3); }
        
        #mbz-header-actions { display: flex; gap: 4px; align-items: center; }
        #mbz-restart, #mbz-close { background: none; border: none; color: white; cursor: pointer; opacity: 0.8; transition: all 0.2s; padding: 6px; display: flex; align-items: center; justify-content: center; border-radius: 50%; }
        #mbz-restart:hover, #mbz-close:hover { opacity: 1; background: rgba(255,255,255,0.15); }
        
        #mbz-messages { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 12px; background: #f8fafc; scroll-behavior: smooth; }
        
        .mbz-msg { max-width: 85%; padding: 10px 14px; border-radius: 16px; font-size: 14px; line-height: 1.5; word-wrap: break-word; }
        .mbz-msg.user { background: #2563eb; color: white; border-bottom-right-radius: 4px; align-self: flex-end; }
        .mbz-msg.bot { background: #ffffff; color: #334155; border-bottom-left-radius: 4px; border: 1px solid #e2e8f0; box-shadow: 0 2px 4px rgba(0,0,0,0.02); align-self: flex-start; }
        .mbz-msg.system { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; text-align: center; max-width: 100%; margin: 10px 0; border-radius: 12px; font-weight: 500; align-self: center; }
        
        #mbz-input-area { padding: 16px; background: white; border-top: 1px solid #e2e8f0; display: flex; gap: 10px; align-items: center; }
        #mbz-input { flex: 1; border: 1px solid #e2e8f0; background: #f8fafc; padding: 12px 16px; border-radius: 999px; font-size: 14px; outline: none; transition: all 0.2s; color: #0f172a; }
        #mbz-input:focus { border-color: #93c5fd; background: white; box-shadow: 0 0 0 3px rgba(37,99,235,0.1); }
        #mbz-input:disabled { background: #f1f5f9; cursor: not-allowed; opacity: 0.7; }
        
        #mbz-send { background: #2563eb; color: white; border: none; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s; flex-shrink: 0; }
        #mbz-send:hover:not(:disabled) { background: #1d4ed8; transform: scale(1.05); }
        #mbz-send:disabled { background: #94a3b8; cursor: not-allowed; }
        #mbz-send svg { width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; margin-left: -2px; }

        .mbz-typing { display: flex; gap: 4px; padding: 4px 2px; }
        .mbz-dot { width: 6px; height: 6px; background: #cbd5e1; border-radius: 50%; animation: mbz-bounce 1.4s infinite ease-in-out both; }
        .mbz-dot:nth-child(1) { animation-delay: -0.32s; }
        .mbz-dot:nth-child(2) { animation-delay: -0.16s; }
        @keyframes mbz-bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }
    `;

    const styleEl = document.createElement('style');
    styleEl.innerHTML = styles;
    document.head.appendChild(styleEl);

    const widgetHTML = `
        <div id="mbz-chat">
            <div id="mbz-header">
                <div id="mbz-header-title">
                    <span class="status"></span> Mobizze AI
                </div>
                <div id="mbz-header-actions">
                    <button id="mbz-restart" aria-label="Restart" title="Clear and restart conversation">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
                    </button>
                    <button id="mbz-close" aria-label="Close" title="Close chat">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                    </button>
                </div>
            </div>
            <div id="mbz-messages">
                <!-- Messages generated via JS -->
            </div>
            <div id="mbz-input-area">
                <input type="text" id="mbz-input" placeholder="Type your message..." autocomplete="off">
                <button id="mbz-send" aria-label="Send">
                    <svg viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                </button>
            </div>
        </div>
        <button id="mbz-toggle">
            <svg viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
            Try it now
        </button>
    `;

    const widgetContainer = document.createElement('div');
    widgetContainer.id = 'mbz-widget';
    widgetContainer.innerHTML = widgetHTML;
    document.body.appendChild(widgetContainer);

    const toggleBtn = document.getElementById('mbz-toggle');
    const closeBtn = document.getElementById('mbz-close');
    const restartBtn = document.getElementById('mbz-restart');
    const chatWindow = document.getElementById('mbz-chat');
    const messagesContainer = document.getElementById('mbz-messages');
    const inputField = document.getElementById('mbz-input');
    const sendBtn = document.getElementById('mbz-send');

    // Open/Close events
    toggleBtn.addEventListener('click', () => {
        isOpen = !isOpen;
        chatWindow.classList.toggle('mbz-open', isOpen);
        if (isOpen) {
            toggleBtn.style.display = 'none';
            inputField.focus();
        }
    });

    closeBtn.addEventListener('click', () => {
        isOpen = false;
        chatWindow.classList.remove('mbz-open');
        setTimeout(() => { toggleBtn.style.display = 'flex'; }, 200);
    });

    // Restart conversation event
    restartBtn.addEventListener('click', () => {
        localStorage.removeItem('mbz_chat_state_en');
        
        userMessageCount = 0;
        uiMessages = [];
        apiHistory = [
            { 
                role: "system", 
                content: "You are an intelligent virtual assistant for Mobizze, an AI agency. You are friendly, direct, and professional. Always reply in English. Your goal is to help the user understand the power of automation, but responses must be concise (max 2-3 short sentences)." 
            }
        ];

        messagesContainer.innerHTML = '';
        appendMessage('bot', 'Hello! 👋 I am Mobizze\'s AI assistant. You can test my capabilities right now. How can I help you?');
    });

    function appendMessage(role, text, save = true) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `mbz-msg ${role}`;
        
        if (role === 'system') {
            msgDiv.innerHTML = text;
        } else {
            msgDiv.textContent = text;
        }
        
        messagesContainer.appendChild(msgDiv);
        scrollToBottom();

        if (save) {
            uiMessages.push({ type: role, content: text });
            saveState();
        }
    }

    function initChat() {
        const saved = localStorage.getItem('mbz_chat_state_en');
        if (saved) {
            const state = JSON.parse(saved);
            apiHistory = state.apiHistory;
            uiMessages = state.uiMessages || [];
            userMessageCount = state.userMessageCount || 0;
            
            uiMessages.forEach(msg => {
                appendMessage(msg.type, msg.content, false);
            });
        } else {
            appendMessage('bot', 'Hello! 👋 I am Mobizze\'s AI assistant. You can test my capabilities right now. How can I help you?');
        }
    }
    
    initChat();

    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'mbz-msg bot mbz-typing-container';
        typingDiv.id = 'mbz-typing-indicator';
        typingDiv.innerHTML = `
            <div class="mbz-typing">
                <div class="mbz-dot"></div>
                <div class="mbz-dot"></div>
                <div class="mbz-dot"></div>
            </div>
        `;
        messagesContainer.appendChild(typingDiv);
        scrollToBottom();
    }

    function removeTyping() {
        const typingIndicator = document.getElementById('mbz-typing-indicator');
        if (typingIndicator) typingIndicator.remove();
    }

    function scrollToBottom() {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    async function handleSend() {
        const text = inputField.value.trim();
        if (!text || isWaitingForResponse) return;

        appendMessage('user', text);
        inputField.value = '';
        userMessageCount++;
        
        apiHistory.push({ role: "user", content: text });
        saveState();

        isWaitingForResponse = true;
        inputField.disabled = true;
        sendBtn.disabled = true;
        showTyping();

        try {
            const response = await fetch('https://api.openai.com/v1/chat/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${API_KEY}`
                },
                body: JSON.stringify({
                    model: 'gpt-4o-mini',
                    messages: apiHistory,
                    temperature: 0.7,
                    max_tokens: 150
                })
            });

            if (!response.ok) throw new Error('API Error');

            const data = await response.json();
            const botReply = data.choices[0].message.content;

            removeTyping();
            appendMessage('bot', botReply);
            
            apiHistory.push({ role: "assistant", content: botReply });
            saveState();

            // Promotional message every 3 interactions
            if (userMessageCount > 0 && userMessageCount % 3 === 0) {
                setTimeout(() => {
                    appendMessage('system', 'Want to implement an assistant like this in your company?<br><br>Talk to us at <a href="../en/contact.html" style="color: #991b1b; text-decoration: underline; font-weight: bold;">www.mobizze.com/contact</a>');
                }, 800);
            }

        } catch (error) {
            console.error("Mobizze Bot Error:", error);
            removeTyping();
            appendMessage('bot', 'Sorry, a connection error occurred. Please try again later.');
            
            // Revert failed count
            userMessageCount--; 
            apiHistory.pop();
            saveState();
        } finally {
            isWaitingForResponse = false;
            inputField.disabled = false;
            sendBtn.disabled = false;
            inputField.focus();
        }
    }

    // Send events
    sendBtn.addEventListener('click', handleSend);
    inputField.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

})();