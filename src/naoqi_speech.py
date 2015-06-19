import naoqi
import sys

from naoqi import ALProxy
IP   = "10.0.1.3"
PORT = 9559
loggerProxy = ALProxy("ALTextToSpeech", IP, PORT)
loggerProxy.setParameter("speed", 20)
loggerProxy.setParameter("pitchShift", 1.0)
print loggerProxy.getAvailableVoices()
#loggerProxy.setVoice("Kenny22Enhanced")
def say(speech):
    loggerProxy.say(speech)
