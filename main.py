import speech_recognition as sr # sr is a shortcut for speech recognition
from ttsvoice import tts # tts is a shortcut for text to speech
import requests
from bs4 import BeautifulSoup
import datetime
import wikipedia
import time
import os , json
from dotenv import load_dotenv
from serpapi import GoogleSearch
r = sr.Recognizer() # initiaze the speech recognizer
from Greetings import Greetings
from Listen import listen



if __name__ == '__main__':
    Greetings()
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
            command =command.replace("wikipedia", "") # replacing word wikipedia with nothing (it is vital to do that because we don't want to search for example: Robert Lewandowski wikipedia. We want to delete that word)
            results = wikipedia.summary(command, sentences=3) # using pip install to install wikipedia and using it function/modules to summary the whole wikipedia page 
            tts("According to Wikipedia")
            print(results)
            tts(results) # saying the results 
        elif 'time' in command:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            tts(f"It is {Time}")

        elif "weather" in command:
            load_dotenv() # loading .env file
            API_KEY = os.getenv("WEATHER_API_KEY") # passing my API key
            tts("Say you city name")
            city_name = listen().lower() # listening for the name of the city
            while True:
                if city_name == 0:
                    continue
                else:
                    break

            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}") # this the request for the data
            data = response.json() # pass it to json
            temperature = data['main']['temp'] # getting temperature 
            weather = data['weather'][0]['description'] # getting weather
            tts(f"It's {temperature} Celsius, and it's a {weather}") # saying all the data
        
        elif "calculate" in command:
            load_dotenv() # loading .env file
            params = {
              "api_key": os.getenv("SEARCH_API_KEY"),
              "engine": "google",
              "q": command.replace('calculate', ''),
              "google_domain": "google.com",
              "gl": "us",
              "hl": "en"
            }
            try:
                search = GoogleSearch(params)
                results = search.get_dict()
                answer_box = results["answer_box"]
                tts(answer_box['result'])
            except Exception as e:
                print(e)
                tts("Try something else or say that again")
        
        elif "definition" in command:
            load_dotenv()
            params = {
              "api_key": os.getenv("SEARCH_API_KEY"),
              "engine": "google",
              "q":  command,
              "google_domain": "google.com",
              "gl": "us",
              "hl": "en"
            }
            try:
                search = GoogleSearch(params)
                results = search.get_dict()
                answer_box = results["answer_box"]
                tts(answer_box['definitions'])
            except Exception as e:
                print(e)
                tts("Try something else or say that again")