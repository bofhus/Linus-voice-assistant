#!/usr/bin/env python3

import os
import time
import playsound
import pyttsx3
import pyaudio
import webbrowser
import random
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

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

# Greet us randomly
def greetVoice():
    speak(random.choice(greetList))

