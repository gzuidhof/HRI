# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 11:45:35 2015

@author: Luc
"""

from naoqi import ALModule
from naoqi import ALProxy
from naoqi import ALBroker
from optparse import OptionParser
import time
import sys


class SpeechDetectorModule(ALModule):
    """Detects speech (hopefully)
    """

    def __init__(self, name):
        ALModule.__init__(self, name)
        
        self.tts  = ALProxy("ALTextToSpeech")
        self.tts.say("Starting speech detection")
        
        
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized", "SpeechDetector", "onSpeechDetected")
        
    def onSpeechDetected(self, *args):
        """
        blabal
        """
        print "start hallo"
#        memory.unsubcribeToEvent("WordRecognized", "SpeechDetector")
#        self.tts.say("Speech detected")
        print "hallo?"
#        memory.subcribeToEvent("WordRecognized", "SpeechDetector", "onSpeechDetected")
    
        


def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip="10.0.1.3",
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port


    asr = ALProxy("ALSpeechRecognition", "10.0.1.3", 9559)

    asr.setLanguage("English")
    
    # Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
    vocabulary = ["yes", "no", "please"]
    asr.setVocabulary(vocabulary, False)
    
    # Start the speech recognition engine with user Test_ASR
    asr.subscribe("Test_ASR")

    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global SpeechDetector
    SpeechDetector = SpeechDetectorModule("SpeechDetector")

    

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        asr.unsubscribe("Test_ASR")
        myBroker.shutdown()
        sys.exit(0)



if __name__ == "__main__":
    main()