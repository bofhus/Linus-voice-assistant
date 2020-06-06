#!/usr/bin/env python3

import os
import time
import playsound
import pyttsx3
import pyaudio
import webbrowser
import random
import json
#import pyautogui

from selenium import webdriver
from vosk import Model, KaldiRecognizer

# Random greetings
greetList = ["yes","how may i be of service","speak to me","i'm listening"]

# Engine settings
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('rate', 135)
engine.setProperty('voice', 'english')

# Recognizer settings
model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Capture the mic
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def getAudio():
        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                return(rec.Result())

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

# Greet us randomly
def greetVoice():
    speak(random.choice(greetList))
    getAudio()    
    text = json.loads(getAudio())
    wake = text["text"]
    print(wake)

def query():
    getAudio()    
    text = json.loads(getAudio())
    wake = text["text"]
    print(wake)


