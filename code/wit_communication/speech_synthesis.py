__author__ = 'stefjanssen'

import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 130)

voices = engine.getProperty('voices')

def say_something(s):
    print "Using voice:", repr(voices[3])
    engine.setProperty('voice', voices[3].id)
    engine.say(s)
    engine.runAndWait()