from ttsvoice import tts # tts is a shortcut for text to speech
import datetime

def Greetings(): # function that's greet the user depending on the day time
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        tts("Hello,Good Morning")
    elif hour>=12 and hour<18:
        tts("Hello,Good Afternoon")
    else:
        tts("Hello,Good Evening")