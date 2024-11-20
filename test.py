from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to generate chatbot responses based on user input
def chatbot_response(user_input):
    # Converting the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! My name is Mr. Solver... How can I help you today?"
    
    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Responding to name queries
    elif "your name" in user_input:
        return "I'm Mr. Solver, here to assist you!"
    
    # Responding to general questions
    elif "how are you" in user_input:
        return "I'm here to help you with any questions you have!"
    
    # Specific questions about the weather
    elif "weather" in user_input:
        return "I'm not connected to the internet, so I can't fetch real-time weather. But I hope it's a nice day!"
    
    # Help/Support queries
    elif "help" in user_input or "support" in user_input:
        return "I'm here to assist you with any basic questions. Ask me anything!"
    
    # Default response for unknown queries
    else:
        return "I'm not sure I understand. Can you rephrase your question?"

# Route for the home page (rendering the HTML template)
@app.route('/')
def home():
    return render_template('chatbot.html')

# Route for handling chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # Get the user's message from the request
    response = chatbot_response(user_message)  # Call the function to get the response
    return jsonify({'response': response})  # Return the response as JSON

if __name__ == '__main__':
    app.run(debug=True)
