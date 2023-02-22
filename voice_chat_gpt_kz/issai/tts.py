#!/usr/bin/env python3
import pyttsx3
import gtts
import time

class TTS:
    def __init__(self, model='google', gender=0):
        self.model = model
        self.gender = gender
        if self.model == 'google':
            self.tts = gtts.gTTS
        else:
            self.tts = pyttsx3.init()

            # getting details of current speaking rate
            self.rate = self.tts.getProperty('rate')
            # setting up new voice rate
            # self.tts.setProperty('rate', 125)

            # getting to know current volume level (min=0 and max=1)
            self.volume = self.tts.getProperty('volume')
            # setting up volume level  between 0 and 1
            self.tts.setProperty('volume', 1.0)

            # getting details of current voice
            self.voices = self.tts.getProperty('voices')

            # changing index, changes voices. 0: male, 1: female
            self.tts.setProperty('voice', self.voices[self.gender].id)

    def convert(self, text_input, save_path):
        if self.model == 'google':
            tts = self.tts(text_input, lang='en', tld='us')
            tts.save(save_path)
        else:
            self.tts.save_to_file(text_input, save_path)
            self.tts.runAndWait()


