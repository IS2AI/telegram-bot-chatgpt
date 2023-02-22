#!/usr/bin/env python3
import speech_recognition as sr
import time

class ASR:
    def __init__(self, lang='en', model='google'):
        self.recognizer = sr.Recognizer()
        self.model = model
        self.message = ""
        self.lang = lang

    def convert(self, audio_input):
        with sr.AudioFile(audio_input) as source:
            audio = self.recognizer.record(source)

        if self.model is 'google':
            # recognize speech using Google Speech Recognition
            try:
                self.message = self.recognizer.recognize_google(audio, language=self.lang)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            # recognize speech using Vosk Speech Recognition
            try:
                self.message = self.recognizer.recognize_vosk(audio)
            except sr.UnknownValueError:
                print("Vosk Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Vosk")


