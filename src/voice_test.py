import speech_recognition as sr
def callback(recognizer, audio):
    try:
        print("You said " + recognizer.recognize(audio))  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! wtf?")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

import time
while True: time.sleep(0.1)
