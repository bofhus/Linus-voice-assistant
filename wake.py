#!/usr/bin/env python3

import os
import pyaudio
import commands
import json

from vosk import Model, KaldiRecognizer


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

# Testing
while True:
    getAudio()
    text = json.loads(getAudio())
    wake = text["text"]
    
    if "hello" in wake:
        commands.greetVoice()
              
    

