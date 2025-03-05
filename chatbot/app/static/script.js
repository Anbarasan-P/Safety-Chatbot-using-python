// DOM Elements
const messagesDiv = document.getElementById('messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Function to add a message to the chatbox
function addMessage(text, isUser) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(isUser ? 'user' : 'bot');
    messageDiv.textContent = text;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to the latest message
}

// Function to send user input to the backend
async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    // Add user message to the chatbox
    addMessage(userMessage, true);
    userInput.value = ''; // Clear the input field

    try {
        // Send the message to the backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        });

        const data = await response.json();
        // Add bot's response to the chatbox
        addMessage(data.response, false);
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, something went wrong. Please try again.', false);
    }
}

// Event Listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});