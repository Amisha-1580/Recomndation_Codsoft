# Rule-based Chatbot

def chatbot_response(user_input):
    # Converting the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello!,my name is MR.solver... How can I help you today?"
    
    # Farewell responses
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Responding to name queries
    elif "your name" in user_input:
        return "I'm a Mr.solver, here to assist you!"
    
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
        return "I'm not sure I understand. please Can you rephrase your question?"

# Testing the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Ending chat.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)