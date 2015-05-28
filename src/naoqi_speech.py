import naoqi
import sys

print "naoqi speech available"
ip ="10.0.1.2"
port="9559"

from naoqi import ALProxy
IP   = "10.0.1.2"
PORT = 9559
loggerProxy = ALProxy("ALTextToSpeech", IP, PORT)

def say(speech):
    loggerProxy.say(speech)

