import speech_recognition as sr # sr is a shortcut for speech recognition
from ttsvoice import tts # tts is a shortcut for text to speech
import requests
from bs4 import BeautifulSoup
import datetime
import wikipedia
import time
import os 
from dotenv import load_dotenv
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
        print("Listening...")
        audio_data = r.record(source, duration=5)  # record will have duration of 5 seconds 
        print("Done !")


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
        elif 'time' in command:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            tts(f"It is {Time}")
        elif 'search' in command:
            URL = "https://www.google.co.in/search?q=" + command.replace(" ", "+")
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            print(soup)
            print(page)
            results = soup.find('div', {'role': 'heading', 'aria-level':3})
            tts(results)
        elif "weather" in command:
            load_dotenv()
            API_KEY = os.getenv("API_KEY")
            tts("Say you city name")
            city_name = listen().lower()
            while True:
                if city_name == 0:
                    continue
                else:
                    break

            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}")
            data = response.json()
            temperature = data['main']['temp']
            weather = data['weather'][0]['description']
            tts(f"It's {temperature} Celsius, and it's a {weather}")
            print(temperature)