def chatbot():
    print("Chatbot: Hello! I'm a simple rule-based bot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        # Exit condition
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        
        # Asking name
        elif "your name" in user_input:
            print("Chatbot: I'm just a rule-based chatbot.")
        
        # Asking about time
        elif "time" in user_input:
            print("Chatbot: I don't know the exact time, but it's always a good time to code!")
        
        # Asking about age
        elif "age" in user_input:
            print("Chatbot: I'm timeless!")
        
        # Weather-related
        elif "weather" in user_input:
            print("Chatbot: I can't feel the weather, but I hope it's good there.")
        
        # Default response
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
