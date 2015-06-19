use_nao = True

if use_nao:
    import naoqi_speech as speech
else:
    import speech_synthesis as speech

def say(what):
    print "Saying", what
    speech.say(what)


say("hallo?")
