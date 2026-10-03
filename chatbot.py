# Basic Rule-Based Chatbot

def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    elif text in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif text in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"
    elif text in ["what is your name", "what's your name"]:
        return "I'm a simple chatbot built in Python."
    elif text in ["thanks", "thank you"]:
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def main():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    main()
