#!/usr/bin/env python3

import os
import pyaudio
import commands
import json

from vosk import Model, KaldiRecognizer


# Recognizer settings
model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Wake the bot up
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    def getAudio():
        while True:
            data = stream.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                return(rec.Result())


    text = json.loads(getAudio())
    wake = text["text"]
# Testing
    if "linus" in wake:
        commands.greetVoice()
        
    

