import pygame as pg

spritelib = {
    
}

def getsprite(name):
    return spritelib[name]

class physobject:
    def __init__(self,spritename):
        self.sprite = pg.image.load(spritename)
        self.surf = pg.Surface()