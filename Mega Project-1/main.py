# Jarvis - A simple voice assistant in Python 

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os 
 


# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()


newsapi = "f2f0dacb4394457baa887333cef79f71"

# Text-to-speech function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Process user commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak("Sorry, I could not find that song.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=f2f0dacb4394457baa887333cef79f71")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            if articles:
                speak("Here are the top headlines from India.")
                for i, article in enumerate(articles[:5], start=1):  # Top 5 headlines
                    headline = article['title']
                    print(f"{i}. {headline}")
                    speak(headline)
            else:
                print("Sorry, I couldn't find any news right now.")
        else:
            print("Sorry, I was not able to fetch the news.")

    elif "exit" in c.lower() or "quit" in c.lower():
        speak("Exiting. Goodbye!")
        os._exit(0)

# Main program
if __name__ == "__main__":
    speak("Initializing Jarvis....")
     
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            try:    
                word = recognizer.recognize_google(audio)
                if(word.lower() == "jarvis"):
                    speak("Yes, how can I help you?")

                    # Listen for actual command
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)

                        processCommand(command)

            except sr.UnknownValueError:
                print("Could not understand audio")        

        except Exception as e:
            print("Error; {0}".format(e))
