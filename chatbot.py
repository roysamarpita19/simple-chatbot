# chatbot.py

import random

# Define some basic responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi, how can I help you?"],
    "how are you": ["I'm doing great, thank you!", "I'm just a program, but I'm doing fine!", "I'm doing well, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm sorry, I don't understand that.", "Can you please rephrase that?", "I didn't get that."]
}

# Function to get a random response from the list of responses
def get_response(user_input):
    # Convert user input to lowercase to handle case-insensitivity
    user_input = user_input.lower()
    
    # Check if the input matches one of the predefined responses
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        # If the user types "bye", exit the loop and end the conversation
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get the chatbot's response
        response = get_response(user_input)
        
        # Print the chatbot's response
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
