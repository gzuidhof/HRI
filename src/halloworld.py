
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.0.1.3", 9559)
tts.say("It is alive!")