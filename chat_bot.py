# This is a simple chatbot that responds to user input with pre-defined responses.
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a chatbot created by a human. What's your name?",
        "who created you": "I was created by a human. What's your name?",
        "what can you do": "I can respond to your messages with pre-defined responses.",
        "what is your purpose": "I'm here to help you with any questions you have.",
        "thank you": "You're welcome!",
        "thanks": "You're welcome!",
        "default": "I'm not sure how to respond to that."
        
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    print(f"Bot: {chatbot_response(user_input)}")
