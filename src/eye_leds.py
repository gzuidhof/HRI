# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:00:22 2015

@author: Tom
"""

from naoqi import ALProxy
class LedController:

    def __init__(self, use_nao):
        self.use_nao = use_nao

        if use_nao:
            leds = ALProxy("ALLeds","10.0.1.3",9559)
            red_names = [
                "Face/Led/Red/Left/0Deg/Actuator/Value",
                "Face/Led/Red/Left/90Deg/Actuator/Value",
                "Face/Led/Red/Left/180Deg/Actuator/Value",
                "Face/Led/Red/Left/270Deg/Actuator/Value",
                "Face/Led/Red/Left/45Deg/Actuator/Value",
                "Face/Led/Red/Left/135Deg/Actuator/Value",
                "Face/Led/Red/Left/225Deg/Actuator/Value",
                "Face/Led/Red/Left/315Deg/Actuator/Value",
                "Face/Led/Red/Right/0Deg/Actuator/Value",
                "Face/Led/Red/Right/90Deg/Actuator/Value",
                "Face/Led/Red/Right/180Deg/Actuator/Value",
                "Face/Led/Red/Right/270Deg/Actuator/Value",
                "Face/Led/Red/Right/45Deg/Actuator/Value",
                "Face/Led/Red/Right/135Deg/Actuator/Value",
                "Face/Led/Red/Right/225Deg/Actuator/Value",
                "Face/Led/Red/Right/315Deg/Actuator/Value"]
            leds.createGroup("RedGroup",red_names)

            blue_names = [
                "Face/Led/Blue/Left/0Deg/Actuator/Value",
                "Face/Led/Blue/Left/90Deg/Actuator/Value",
                "Face/Led/Blue/Left/180Deg/Actuator/Value",
                "Face/Led/Blue/Left/270Deg/Actuator/Value",
                "Face/Led/Blue/Left/45Deg/Actuator/Value",
                "Face/Led/Blue/Left/135Deg/Actuator/Value",
                "Face/Led/Blue/Left/225Deg/Actuator/Value",
                "Face/Led/Blue/Left/315Deg/Actuator/Value",
                "Face/Led/Blue/Right/0Deg/Actuator/Value",
                "Face/Led/Blue/Right/90Deg/Actuator/Value",
                "Face/Led/Blue/Right/180Deg/Actuator/Value",
                "Face/Led/Blue/Right/270Deg/Actuator/Value",
                "Face/Led/Blue/Right/45Deg/Actuator/Value",
                "Face/Led/Blue/Right/135Deg/Actuator/Value",
                "Face/Led/Blue/Right/225Deg/Actuator/Value",
                "Face/Led/Blue/Right/315Deg/Actuator/Value"]
            leds.createGroup("BlueGroup",blue_names)

            green_names = [
                "Face/Led/Green/Left/0Deg/Actuator/Value",
                "Face/Led/Green/Left/90Deg/Actuator/Value",
                "Face/Led/Green/Left/180Deg/Actuator/Value",
                "Face/Led/Green/Left/270Deg/Actuator/Value",
                "Face/Led/Green/Left/45Deg/Actuator/Value",
                "Face/Led/Green/Left/135Deg/Actuator/Value",
                "Face/Led/Green/Left/225Deg/Actuator/Value",
                "Face/Led/Green/Left/315Deg/Actuator/Value",
                "Face/Led/Green/Right/0Deg/Actuator/Value",
                "Face/Led/Green/Right/90Deg/Actuator/Value",
                "Face/Led/Green/Right/180Deg/Actuator/Value",
                "Face/Led/Green/Right/270Deg/Actuator/Value",
                "Face/Led/Green/Right/45Deg/Actuator/Value",
                "Face/Led/Green/Right/135Deg/Actuator/Value",
                "Face/Led/Green/Right/225Deg/Actuator/Value",
                "Face/Led/Green/Right/315Deg/Actuator/Value"]
            leds.createGroup("GreenGroup",green_names)


            # Switch the new groups on
            leds.on("RedGroup")
            leds.on("BlueGroup")
            leds.on("GreenGroup")
    
    def set_eyes_to_green(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 0)
            self.leds.setIntensity("BlueGroup", 0)
            self.leds.setIntensity("GreenGroup", 1)
        
    def set_eyes_to_blue(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 0)
            self.leds.setIntensity("BlueGroup", 1)
            self.leds.setIntensity("GreenGroup", 0)
        
    def set_eyes_to_red(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 1)
            self.leds.setIntensity("BlueGroup", 0)
            self.leds.setIntensity("GreenGroup", 0)
        
    def set_eyes_to_yellow(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 1)
            self.leds.setIntensity("BlueGroup", 0)
            self.leds.setIntensity("GreenGroup", 1)
        
    def set_eyes_to_white(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 1)
            self.leds.setIntensity("BlueGroup", 1)
            self.leds.setIntensity("GreenGroup", 1)
        
    def set_eyes_to_turquoise(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 0)
            self.leds.setIntensity("BlueGroup", 1)
            self.leds.setIntensity("GreenGroup", 1)
        
    def set_eyes_to_off(self, use_nao):
        if use_nao:
            self.leds.setIntensity("RedGroup", 0)
            self.leds.setIntensity("BlueGroup", 0)
            self.leds.setIntensity("GreenGroup", 0)
