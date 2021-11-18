import pygame as pg
import numpy




class windowhandler:
    def __init__(self,startres,vel):
        self.width = startres[0]
        self.height = startres[0]
        self.velocity = vel

    def setvelocity(self, vel):
        self.vel = vel
    
    def addvel(self, vel):
        self.vel += vel
    
    def setposition(self,pos):
        self.position = pos
