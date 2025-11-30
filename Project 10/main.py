#Personal Chatbot Assistant
#Rules-Based Chatbot Assistant in Python
import datetime
import time

name=input("Hello! What's your name? ")
presentHr=datetime.datetime.now().hour
if presentHr<12:
    print(f"Good Morning, {name}!")
elif 12 <= presentHr < 18:
    print(f"Good Afternoon, {name}!")
else:
    print(f"Good Evening, {name}!")
    time.sleep(1)


print("Welcome to Personal Chatbot Assistant")
print("You can ask me basic questions about such as weather, time, or just have a chat!")
print("Type 'bye' to end the chat.")

responses = {
    "how are you": "I'm just a program, but thanks for asking!",
    "what's your name": "I'm your Personal Chatbot Assistant.",
    "what time is it": f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}.",
    "what's the date today": f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}.",
    "tell me a joke": "Why did the computer show up at work late? It had a hard drive!",
    "what's the weather like": "I don't have access to real-time weather data, but I hope it's nice where you are!",
    "motivate me": "Believe in yourself! You can achieve anything you set your mind to.",
    "happy": "That's great to hear! Keep smiling!",
    "sad": "I'm sorry to hear that. Remember, after every storm comes a rainbow.",
    "bye": "Goodbye! Have a great day!"
    }

while True:
    user_input = input("You: ").lower()
    
    if user_input in responses:
        print(f"Bot: {responses[user_input]}")
        if user_input == "bye":
            break
    else:
        print("Bot: I'm sorry, I don't understand that. Can you ask something else?")