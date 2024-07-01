def chatbot_response(user_input):
    user_input = user_input.lower()
    
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! How can I assist you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created in Python.",
        "bye": "Goodbye! Have a nice day!",
        "thank you": "You're welcome!",
        "help": "I'm here to assist you with basic responses. How can I help you?"
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
