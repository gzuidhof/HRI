# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:45:01 2015

@author: Luc
"""
from __future__ import division
from naoqi import ALProxy
import time

import numpy as np

class FaceTracker():
    
    def __init__(self, ip = "10.0.1.3", port = 9559):
        self.faceProxy = ALProxy("ALFaceTracker", ip, port)
        self.motion = ALProxy("ALMotion", ip, port)
        
    def start_tracking(self):
        print "StartTracking"
        self.motion.setStiffnesses("Head", 1.0)
        self.faceProxy.startTracker()
        self.faceProxy.setWholeBodyOn(True)
    
    def stop_tracking(self):
        self.faceProxy.stopTracker()
        self.motion.setStiffnesses("Head", 0.0)
        print "Tracking stopped"
    
    def shake_no(self):
        names = "HeadYaw"
        currentAngle = self.motion.getAngles("Head", False)[0]

        angles = [0.5, 0, -0.5, 0, 0.5, currentAngle]
        times = [(i/len(angles))+0.2 for i in np.arange(1, len(angles)+1)]
                
        self.faceProxy.stopTracker()
        print "no"
        self.motion.setStiffnesses("Head", 1.0)
        self.motion.angleInterpolation(names, angles, times, True)
        self.motion.setStiffnesses("Head", 0.0)
        self.start_tracking()
    
    def shake_yes(self):
        names = "HeadPitch"        
        currentAngle = self.motion.getAngles("Head", False)[1]
        angles = [0, 0.3, 0, currentAngle]
        times = [i/len(angles) for i in np.arange(1, len(angles)+1)]
        
        self.faceProxy.stopTracker()
        self.motion.setStiffnesses("Head", 1.0)
        self.motion.angleInterpolation(names, angles, times, True)
        self.motion.setStiffnesses("Head", 0.0)
        self.start_tracking()
    
if __name__ == '__main__':
    tracker = FaceTracker()
    tracker.start_tracking()
    time.sleep(5)
    tracker.shake_yes()
    tracker.shake_no()
    
    
        