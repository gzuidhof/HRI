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
    
    def __init__(self, use_nao, ip = "10.0.1.3", port = 9559):
        self.use_nao = use_nao
        if use_nao:
            self.faceProxy = ALProxy("ALFaceTracker", ip, port)
            self.motion = ALProxy("ALMotion", ip, port)
        
    def start_tracking(self):
        if self.use_nao:
            print "StartTracking"
            self.motion.setStiffnesses("Head", 1.0)
            self.faceProxy.startTracker()
            self.faceProxy.setWholeBodyOn(True)
    
    def stop_tracking(self):
        if self.use_nao:
            self.faceProxy.stopTracker()
            self.motion.setStiffnesses("Head", 0.0)
            print "Tracking stopped"
    
    def to_default(self):
        if self.use_nao:
            self.motion.setStiffnesses("Head", 1.0)
            self.motion.setAngles("HeadYaw", 0.0, 0.6)
            self.motion.setAngles("HeadPitch", 0.0, 0.6)
#        self.motion.setStiffnesses("Head", 0)
    
    def shake_no(self):
        if self.use_nao:
            names = "HeadYaw"
            currentAngle = self.motion.getAngles("Head", True)[0]
    
            angles = [0.25, 0, -0.25, 0, 0.25, currentAngle]
            times = [(i/len(angles))+0.2 for i in np.arange(1, len(angles)+1)]
                    
            self.faceProxy.stopTracker()
            print "no"
            self.motion.setStiffnesses("Head", 1.0)
            self.motion.angleInterpolation(names, angles, times, True)
            self.motion.setStiffnesses("Head", 0.0)
            self.start_tracking()
    
    def shake_yes(self):
        if self.use_nao:
            names = "HeadPitch"        
            currentAngle = self.motion.getAngles("Head", False)[1]
            angles = [0, 0.15, 0, currentAngle]
            times = [i/len(angles) for i in np.arange(1, len(angles)+1)]
            
            self.faceProxy.stopTracker()
            self.motion.setStiffnesses("Head", 1.0)
            self.motion.angleInterpolation(names, angles, times, True)
            self.motion.setStiffnesses("Head", 0.0)
            self.start_tracking()
    
if __name__ == '__main__':
    tracker = FaceTracker()
#    tracker.start_tracking()
#    time.sleep(5)
#    tracker.shake_yes()
    tracker.to_default()
