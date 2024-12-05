// Function to send user input and display bot response
function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== "") {
        addMessage(userInput, "user");
        document.getElementById('user-input').value = ""; // Clear the input field

        // Send user input to the Flask backend via a POST request
        fetch('/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userInput }),
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response || "I am sorry, I can only provide information about the hotel.";
            addMessage(botResponse, "bot");
        })
        .catch(error => {
            addMessage("Sorry, there was an error. Please try again later.", "bot");
        });
    }
}

// Function to add messages to the chat
function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(sender + '-message');
    messageDiv.innerHTML = message;
    
    const chatBox = document.getElementById('chat-box');
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
}

// Automatically focus on the input field when the page loads
document.getElementById('user-input').focus();
