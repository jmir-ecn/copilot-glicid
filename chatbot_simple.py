import random

# Define a dictionary with some predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm doing well, thank you!", "I'm good, thanks for asking!", "I'm fine, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["Sorry, I didn't understand that.", "Can you please repeat that?", "I'm not sure what you mean."]
}

def get_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined responses
    for key in responses:
        if user_input in key:
            return random.choice(responses[key])
    
    # If no match is found, return a default response
    return random.choice(responses["default"])

print("ChatGPT: Hello! I'm ChatGPT. How can I help you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatGPT: Goodbye! Have a great day.")
        break
    response = get_response(user_input)
    print("ChatGPT:", response)

