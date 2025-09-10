# Jarvis - A simple voice assistant in Python 

from pydoc import text
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

def speak(text):
    engine.say(text)
    engine.runAndWait()
    



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
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    elif "exit" in c.lower() or "quit" in c.lower():
        speak("Exiting. Goodbye!")
         
        engine.runAndWait()
        os._exit(0)





if __name__ == "__main__":
    speak("Initializing Jarvis....")
     
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            try:    
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                       speak("Yes, how can I help you?")
                        
                       engine.runAndWait()
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            except sr.UnknownValueError:
                print("Could not understand audio")        


        except Exception as e:
            print("Error; {0}".format(e))


