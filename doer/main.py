#!/usr/bin/env python2

import speech_recognition as sr
import doer
import time

def callback(recognizer, audio): # this is called from the background thread
    try:
        sequence = recognizer.recognize_google(audio)
        print("You said: " + sequence )  # received audio data, now need to recognize it
        doer.analyze(sequence)
        #print "next"
    except LookupError:
        print("Oops! Didn't catch that")
    except:
        pass

r = sr.Recognizer()
r.energy_threshold = 4000
r.listen_in_background(sr.Microphone(), callback)


while True: time.sleep(0.5)
