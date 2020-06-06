#!/usr/bin/env python3

import os
import time
import playsound
import pyttsx3
import pyaudio
import webbrowser
import random
import json
import pyautogui

from wake import wakeListening
from selenium import webdriver
from vosk import Model, KaldiRecognizer

# Random greetings
greetList = ["yes","how may i be of service","speak to me","i'm listening"]
webSearch =["search","search for","look up","google"]

# Engine settings
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('rate', 135)
engine.setProperty('voice', 'english')

# Recognizer settings
model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Capture the mic
def getAudio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    while True:
        data = stream.read(400)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            return(rec.Result())

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

def query():
    getAudio()    
    text = json.loads(getAudio())
    wake = text["text"]
    print(wake)

# Start listening
wakeListening()

# If wake word detected, greet us randomly
speak(random.choice(greetList))

# Take commands
getAudio()
text = json.loads(getAudio())
query = text["text"]

# Let's search the web
for phrase in webSearch:
    if phrase in query:
        voiceI = query.replace(phrase, "")
        browser = webdriver.Firefox()
        browser.get("http://www.google.com")
        element = browser.find_element_by_name("q")
        element.send_keys(voiceI)
        element.submit()
        speak("searching for" + voiceI)

        time.sleep(5)
        speak("found these result on google for" + voiceI)
        for element in browser.find_elements_by_class_name("LC20lb"):
            speak(element.text)
            
        browser.quit()

    else:
        continue

