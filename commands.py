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
engine.setProperty('rate', 100)
engine.setProperty('voice', 'mb-us3')

# Recognizer and voice stream
model = Model("model")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

# Start listening
wakeListening()

# Capture the mic
def getAudio():
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()
    while True:
        data = stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            return(rec.Result())
                  
def speak(voice):
    engine.say(voice)
    engine.runAndWait()

# If wake word detected, greet us randomly
speak(random.choice(greetList))

# Take commands
text = json.loads(getAudio())
query = text["text"]

# Let's search the web
for phrase in webSearch:
    if phrase in query:
        voiceI = query.replace(phrase, "")
        while True:
            if voiceI == "":
                speak("i did not understand, please repeat")
                text = json.loads(getAudio())
                query = text["text"]
                voiceI = query.replace(phrase, "")

            else:
                browser = webdriver.Firefox()
                browser.get("https://duckduckgo.com/")
                element = browser.find_element_by_name("q")
                element.send_keys(voiceI)
                element.submit()
                speak("searching for" + voiceI)

                time.sleep(5)
                speak("found these result on duckduckgo for" + voiceI)
                for element in browser.find_elements_by_class_name("result__a"):
                    speak(element.text)
            
                browser.quit()
                break

    else:
        continue

