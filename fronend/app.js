
class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            messageInput: document.querySelector('.chatbox__footer input'),
            optionsContainer: document.querySelector('.chatbox__options')
        };
        
        this.state = false;
        this.messages = [];
        this.sessionId = Math.random().toString(36).substring(2, 9);
        this.setupSocket();
        this.handleButtonClick = this.handleButtonClick.bind(this);
    }

    setupSocket() {
        this.socket = io.connect('http://0.0.0.0:5005', { path: '/socket.io/' });

        this.socket.on('connect', () => {
            console.log('Connected to the chat server!');
            this.socket.emit('session_request', { session_id: this.sessionId });
        });

        this.socket.on('bot_uttered', (message) => {
            if (message.text === '/show_buttons') {
                this.showButton();
            } else if (message.text === '/show_hour_available') {
                this.showButtonHourAvailable();
            } else {
                this.addMessage("Bot", message.text);
            }
        });

        this.socket.on('connect_error', (error) => {
            console.error('Error connecting to the chat server:', error);
        });
    }

    display() {
        const { openButton, chatBox, sendButton, messageInput } = this.args;
        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.sendMessage(messageInput.value));
        messageInput.addEventListener('keyup', ({ key }) => {
            if (key === 'Enter') {
                this.sendMessage(messageInput.value);
            }
        });
    }

    toggleState(chatbox) {
        this.state = !this.state;
        if (this.state) {
            chatbox.classList.add('chatbox--active');
        } else {
            chatbox.classList.remove('chatbox--active');
        }
    }


    sendMessageToRasa(intent) {
        this.socket.emit('user_uttered', { message: intent, session_id: this.sessionId });
    }

  
    sendMessage(text) {
        if (text.trim() === '') return;

        this.addMessage('User', text);
        this.sendMessageToRasa(text);
        this.args.messageInput.value = '';
    }

    addMessage(sender, message, type = 'text') {
        let msg = { name: sender, message, type };
        this.messages.push(msg);
        this.updateChatText();
    }

    showButton() {
        const buttons = [
            { text: "Dúvida sobre algo", intent: "/duvida_sobre_algo" },
            { text: "Marcar Consulta", intent: "/marcar_consulta" },
            { text: "Cancelar Consulta", intent: "/cancelar_consulta" },
            { text: "Remarcar Consulta", intent: "/remarcar_consulta" }
        ];

        this.addMessage("Bot", buttons, 'buttons');
    }
/* 
    showButtonHourAvailable() {
        // Recuperar os slots livres do estado do chatbot
        const freeSlots = this.getSlot('free_slots');  // Supondo que getSlot seja uma função que retorna o valor de um slot
    
        // Verificar se existem slots livres
        if (!freeSlots || freeSlots.length === 0) {
            this.addMessage("Bot", "Não há horários disponíveis.");
            return;
        }
    
        // Criar um botão para cada slot livre
        const buttons = freeSlots.map(slot => ({
            text: slot,  // O texto do botão será o horário livre
            intent: "/escolher_horario",  // Defina o intent para quando o botão for pressionado
            payload: slot  // Você pode querer enviar o horário como payload para facilitar o processamento do intent
        }));
    
        // Adicionar uma mensagem com os botões ao chat
        this.addMessage("Bot", buttons, 'buttons');
    }
*/
    handleButtonClick(intent, buttonElement) {
        console.log("Clicou no botão, estado disabled:", buttonElement.disabled);
    
        if (buttonElement.disabled) {
            console.log("Botão já está desabilitado.");
            return; // Sai da função se o botão já está desabilitado
        }
    
        console.log("Enviando intenção e desabilitando o botão:", intent);
        this.sendMessageToRasa(intent);
        buttonElement.disabled = true; // Corretamente desabilita o botão após o clique
    
        // Verificação adicional para confirmar se o botão foi desabilitado
        if (buttonElement.disabled) {
            console.log("Botão agora está desabilitado.");
            console.log("Clicou no botão, estado disabled:", buttonElement.disabled);
        }

    }
    updateChatText() {
        const chatbox = this.args.chatBox;
        const chatMessage = chatbox.querySelector('.chatbox__messages');
        chatMessage.innerHTML = ''; // Limpa as mensagens existentes para a nova renderização

        this.messages.slice().reverse().forEach((item, index) => {
            if (item.type === 'text') {
                const messageDiv = document.createElement('div');
                messageDiv.className = `messages__item messages__item--${item.name === "Bot" ? "visitor" : "operator"}`;
                messageDiv.innerText = item.message;
                chatMessage.appendChild(messageDiv);
            } else if (item.type === 'buttons') {
                item.message.forEach((button) => {
                    const buttonElement = document.createElement('button');
                    buttonElement.className = "chat-button";
                    buttonElement.innerText = button.text;
                    buttonElement.addEventListener('click', () => {
                        this.handleButtonClick(button.intent, buttonElement);
                    });
                    chatMessage.appendChild(buttonElement);
                });
            }
        });
    }
    }


const chatbox = new Chatbox();
chatbox.display();