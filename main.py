import speech_recognition as sr # sr is a shortcut for speech recognition
from ttsvoice import tts # tts is a shortcut for text to speech
import requests
from bs4 import BeautifulSoup
import datetime
import wikipedia
r = sr.Recognizer() # initiaze the speech recognizer

def Greetings(): # function that's greet the user depending on the day time
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        tts("Hello,Good Morning")
    elif hour>=12 and hour<18:
        tts("Hello,Good Afternoon")
    else:
        tts("Hello,Good Evening")

def listen(): # simple function to record commands
    r = sr.Recognizer() # initiaze the speech recognizer
    with sr.Microphone() as source: # using microphone 
        audio_data = r.record(source, duration=5)  # record will have duration of 5 seconds 
        print("Listening...")

        try:
            statement = r.recognize_google(audio_data) # trying to convert speech to text
            print(f'You said {statement}')
            return statement
        
        except Exception:
            tts("I'm sorry, can you repeat ?")
            return ""
        
tts("Loading your personal AI")

Greetings()


if __name__ == '__main__':
    while True: # infinite loop that wait for command 
        tts("Hello, how can I help ?")
        command = listen().lower()
        if command == 0:
            continue
        if "good bye" in command or "bye" in command or "stop" in command: # if command (your sentence) contains good bye, bye or stop, program will turn off
            tts("Personal AI shutting down")
            break
        if 'wikipedia' in command: # search for wikipedia
            tts('Searching Wikipedia...')
            command =command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            tts("According to Wikipedia")
            print(results)
            tts(results)