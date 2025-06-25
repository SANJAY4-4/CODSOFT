def simple_chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello there! How can I help you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple chatbot created by a human like you.")
        elif 'help' in user_input:
            print("Chatbot: Sure! You can ask me about basic topics like greetings, my name, or how I'm doing.")
        elif 'bye' in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else.")

# Run the chatbot
simple_chatbot()