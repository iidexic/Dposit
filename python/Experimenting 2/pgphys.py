import pygame as pg

spritelib = {
    
}

def getsprite(name):
    return spritelib[name]
    
class phys_system:
    def __init__(self,objects):
        self.objects = objects
        

class physobject:
    def __init__(self, weight = 1, size = (16,16), shape = 'square', origin = 'center'):
        self.size = size
        self.weight = weight
        self.shape = shape
        self.origin = origin
    def setlocation(self,x,y):
        self.position = (self.x,self.y) = (x,y)
