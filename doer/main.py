#!/usr/bin/env python3

from threading import Thread
import speech_recognition as sr
import doer
# Record Audio
r = sr.Recognizer()


with sr.Microphone() as source:

    while True:
        r.energy_threshold = 4000
        print("Say something!")
        audio = r.listen(source)
        try:
            seq = r.recognize_google(audio)
            print("You said: " + seq)
            Thread(target = doer.analyze, args = (seq,)).start()
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
