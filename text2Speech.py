from dataclasses import dataclass
import pyttsx3

engine = pyttsx3.init() # initializing 

def textSpeech():
    data = input("Enter your text to convert into a speech: \n")
    engine.say(data)
    engine.runAndWait()
textSpeech()
