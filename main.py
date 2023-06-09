import speech_recognition as sr # sr is a shortcut for speech recognition
from ttsvoice import tts # tts is a shortcut for text to speech
import requests
from bs4 import BeautifulSoup
import datetime
import wikipedia
r = sr.Recognizer() # initiaze the speech recognizer

def Greetings():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        tts("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        tts("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        tts("Hello,Good Evening")
        print("Hello,Good Evening")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5) 
        print("Listening...")

        try:
            statement = r.recognize_google(audio_data)
            print(f'You said {statement}')
            return statement
        
        except Exception:
            tts("I'm sorry, can you repeat ?")
            return ""
        
tts("Loading your personal AI")

Greetings()


if __name__ == '__main__':
    while True:
        tts("Hello, how can I help ?")
        command = listen().lower()
        if command == 0:
            continue
        if "good bye" in command or "bye" in command or "stop" in command:
            tts("Personal AI shutting down")
            break
        if 'wikipedia' in command:
            tts('Searching Wikipedia...')
            command =command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            tts("According to Wikipedia")
            print(results)
            tts(results)