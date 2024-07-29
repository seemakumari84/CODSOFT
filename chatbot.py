responses = {
    "hello": "Hi there! How can I help you today? If want to exit Type 'bye'",
    "hi": "Hello! What can I do for you? If want to exit Type 'bye'",
    "I'm fine and you?": "I'm just a chatbot, but I'm here to help you!",
    "how are you?": "I'm just a chatbot, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "help": "Sure, I can help you. What do you need assistance with?",
    "what's your name?": "I'm a chatbot created to assist you.",
    "who are you?": "I'm a friendly chatbot here to help you with your questions.",
    "what can you do?": "I can respond to your questions and provide information.",
    "what's the weather like?": "I'm unable to check the weather at the moment, but you can try looking it up online.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "good morning": "Good morning! How can I assist you today?",
    "good afternoon": "Good afternoon! How can I help you today?",
    "good evening": "Good evening! What can I do for you today?",
    "good night": "Good night! Sleep well!",
    "how can I contact support?": "You can contact support via email or phone. Please check our website for more details.",
    "where are you from?": "I'm a virtual assistant, so I exist in the digital world!",
    "how old are you?": "Age doesn't apply to me, but I'm always here to assist you.",
    "what's your favorite color?": "I don't have preferences, but I think all colors are great!",
    "how do I reset my password?": "You can reset your password by following the 'Forgot Password' link on the login page.",
    "where is the nearest coffee shop?": "I can't provide real-time locations, but you can use a map application to find nearby coffee shops.",
    "do you like music?": "I don't have preferences, but I can suggest some popular genres like pop, rock, or classical.",
    "can you help me with my homework?": "I'll do my best to help! What subject are you working on?",
    "what's the time?": "I'm unable to check the time, but you can look at the clock on your device.",
    "do you have any hobbies?": "I enjoy helping people with their questions!",
    "can you tell me a story?": "Once upon a time, in a land far, far away... there was a curious mind seeking knowledge, just like you!",
    "what's your favorite food?": "I don't eat, but I've heard that pizza is quite popular!",
    "what languages do you speak?": "I can understand and respond in English. What language do you speak?",
    "how do I make a reservation?": "To make a reservation, please visit our website or contact our customer service.",
    "can you recommend a book?": "Sure! 'To Kill a Mockingbird' by Harper Lee is a great read.",
    "what is your purpose?": "My purpose is to assist you with your questions and provide helpful information."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    response = responses.get(user_input, "I'm sorry, I don't understand that.")
    return response

def chat():
    print("Welcome to the chatbot! ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "hello":
            print("Chatbot: Hi there! How can I help you today? If want to exit Type 'bye'")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chat()
