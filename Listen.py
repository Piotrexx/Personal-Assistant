import speech_recognition as sr # sr is a shortcut for speech recognition
from ttsvoice import tts # tts is a shortcut for text to speech

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