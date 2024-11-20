// Toggle chat box visibility
function toggleChatBox() {
    const chatBox = document.getElementById('chatBox');
    chatBox.style.display = chatBox.style.display === 'none' ? 'block' : 'none';
}

// Start chat function
function startChat() {
    document.getElementById('chatInputArea').style.display = 'block';
    document.getElementById('startButton').style.display = 'none';  // Hide the Start button
    document.getElementById('closeButton').style.display = 'inline'; // Show the Close button

    const chatContent = document.getElementById('chatContent');
    chatContent.innerHTML += "<p>Mr. Solver: Hello! How can I help you today?</p>";
}

// Send message function
function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatContent = document.getElementById('chatContent');
    const userMessage = userInput.value;

    if (userMessage.trim() !== "") {
        // Display user message
        chatContent.innerHTML += `<p>You: ${userMessage}</p>`;
        
        // Clear input field
        userInput.value = "";

        // Send message to server
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            chatContent.innerHTML += `<p>Mr. Solver: ${data.response}</p>`;
        })
        .catch(error => {
            console.error('Error:', error);
            chatContent.innerHTML += "<p>Mr. Solver: There was an error processing your request. Please try again.</p>";
        });
    }
}

// Close chat function
function closeChat() {
    const chatBox = document.getElementById('chatBox');
    chatBox.style.display = 'none';
    document.getElementById('chatInputArea').style.display = 'none';
    document.getElementById('startButton').style.display = 'inline'; // Show the Start button again
    document.getElementById('closeButton').style.display = 'none';    // Hide the Close button
}
