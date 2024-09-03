import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm good, thanks for asking!"],
    "what is your name?": ["You can call me ChatBot.", "I'm ChatBot."],
    "help": ["Sure, I can help you. What do you need help with?"],
    "weather": ["Sorry, I cannot provide weather information at the moment."],
    "bye": ["Goodbye!", "Bye! Take care."]
}

def respond(user_input):
    # Convert user input to lowercase for easier comparison
    user_input = user_input.lower()
    
    if user_input in responses:
        # If there's a match, randomly select a response from the corresponding list
        return random.choice(responses[user_input])
    else:
        # If no match is found, respond with a default message
        return "I'm sorry, I don't understand that."
def chat_with_user():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = respond(user_input)
        print("ChatBot:", response)

# Start the conversation
chat_with_user()
