#!/usr/bin/env python3

import os
import time
import playsound
import speech_recognition as sr
import pyttsx3
import pyaudio
import webbrowser
import random
#import pyautogui

from selenium import webdriver
from vosk import Model, KaldiRecognizer

# Random greetings
greetList = ["yes","how may i be of service","speak to me","i'm listening"]

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('rate', 135)
engine.setProperty('voice', 'english+f4')

def speak(voice):
    engine.say(voice)
    engine.runAndWait()

def greetVoice():
    speak(random.choice(greetList))

#def google(text):
#    voiceI = text

#    browser = webdriver.Firefox()
#    browser.get("http://www.google.com")
#    input_element = browser.find_element_by_name("q")
#    input_element.send_keys(voiceI)
#    input_element.submit()

#def close_browser():
#    pyautogui.hotkey('alt', 'f4')

