# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:45:01 2015

@author: Luc
"""

from naoqi import ALProxy

class FaceTracker():
    
    def __init__(self, ip = "10.0.1.3", port = 9559):
        self.faceProxy = ALProxy("ALFaceTracker", ip, port)
        self.motion = ALProxy("ALMotion", ip, port)
        
    def startTracking(self):
        print "StartTracking"
        self.motion.setStiffnesses("Head", 1.0)
        self.faceProxy.startTracker()
        self.faceProxy.setWholeBodyOn(True)
    
    def stopTracking(self):
        self.faceProxy.stopTracker()
        self.motion.setStiffnesses("Head", 0.0)
        print "Tracking stopped"
    
if __name__ == '__main__':
    tracker = FaceTracker()
    tracker.startTracking()
    
    
        