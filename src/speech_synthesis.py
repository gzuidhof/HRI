__author__ = 'stefjanssen'

import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 130)

ROBOTIC_VOICE = 3
AWESOME_VOICE = 9
SEXY_VOICE = 20
voices = engine.getProperty('voices')

def say_something(s):
    engine.setProperty('voice', voices[9].id)
    engine.say(s)
    engine.runAndWait()
