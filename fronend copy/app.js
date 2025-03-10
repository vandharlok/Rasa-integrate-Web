class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            messageInput: document.querySelector('.chatbox__footer input'),
            chatMessages: document.querySelector('.chatbox__messages')
        };

        this.state = false;
        this.messages = [
            { name: "Bot", message: "Oi, bem vindo ao Fidelity Marketing", type: "text", buttons: [] } // Mensagem inicial
        ];
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
            const processedMessage = this.processBotMessage(message);
            if (processedMessage) {
                this.addMessage("Bot", processedMessage.text, processedMessage.type, processedMessage.buttons);
                if (processedMessage.type === 'buttons') {
                    this.toggleInput(false);
                }
            }
        });

        this.socket.on('connect_error', (error) => {
            console.error('Error connecting to the chat server:', error);
        });
    }

    display() {
        const { openButton, chatBox, sendButton, messageInput } = this.args;
        if (openButton) {
            openButton.addEventListener('click', () => this.toggleState(chatBox));
        }
        sendButton.addEventListener('click', () => this.sendMessage(messageInput.value));
        messageInput.addEventListener('keyup', ({ key }) => {
            if (key === 'Enter') {
                this.sendMessage(messageInput.value);
            }
        });
        this.updateChatText(); // Atualiza o chat com a mensagem inicial
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

    addMessage(sender, message, type = 'text', buttons = []) {
        let msg = { name: sender, message, type, buttons };
        this.messages.push(msg);
        this.updateChatText();
    }

    handleButtonClick(intent, buttonElement) {
        if (buttonElement.disabled) {
            return;
        }

        this.sendMessage(intent);
        buttonElement.disabled = true;
    }

    updateChatText() {
        const chatMessage = this.args.chatMessages;
        chatMessage.innerHTML = ''; // Clear existing messages for new rendering

        this.messages.forEach((item) => {
            if (item.type === 'text') {
                const messageContainer = document.createElement('div');
                messageContainer.className = `messages__container messages__container--${item.name === "Bot" ? "operator" : "visitor"}`;
                
                if (item.name === "Bot") {
                    const image = document.createElement('img');
                    image.src = './images/logo_chatbox.png';
                    image.className = 'logo_image';
                    messageContainer.appendChild(image);
                }
                
                const messageDiv = document.createElement('div');
                messageDiv.className = `messages__item messages__item--${item.name === "Bot" ? "operator" : "visitor"}`;
                messageDiv.innerText = item.message;
                messageContainer.appendChild(messageDiv);
                
                chatMessage.appendChild(messageContainer);
            } else if (item.type === 'buttons') {
                // Add the title text first
                const messageContainer = document.createElement('div');
                messageContainer.className = 'messages__container messages__container--operator';

                const image = document.createElement('img');
                image.src = './images/logo_chatbox.png';
                image.className = 'logo_image';
                messageContainer.appendChild(image);

                const titleDiv = document.createElement('div');
                titleDiv.className = 'messages__item messages__item--operator';
                titleDiv.innerText = item.message;
                messageContainer.appendChild(titleDiv);

                chatMessage.appendChild(messageContainer);

                // Add the buttons container
                const buttonsContainer = document.createElement('div');
                buttonsContainer.className = 'chat-buttons';
                item.buttons.forEach((button) => {
                    const buttonElement = document.createElement('button');
                    buttonElement.className = "chat-button";
                    buttonElement.innerText = button.title;
                    buttonElement.addEventListener('click', (e) => {
                        this.handleButtonClick(button.payload, e.target);
                    });
                    buttonsContainer.appendChild(buttonElement);
                });
                chatMessage.appendChild(buttonsContainer);
            }
        });

        // Scroll to the bottom of the chat
        chatMessage.scrollTop = chatMessage.scrollHeight;
    }

    toggleInput(enable) {
        this.args.messageInput.disabled = !enable;
        this.args.sendButton.disabled = !enable;
    }

    processBotMessage(message) {
        const processedMessage = {
            text: message.text || '',
            type: message.quick_replies ? 'buttons' : 'text',
            buttons: message.quick_replies ? message.quick_replies.map(reply => ({
                title: reply.title,
                payload: reply.payload
            })) : []
        };
        return processedMessage;
    }
}

const chatbox = new Chatbox();
chatbox.display();
