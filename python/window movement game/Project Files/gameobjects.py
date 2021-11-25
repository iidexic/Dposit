from numpy import lib
import pygame as pg
import numpy as np
import os

# going to handle game object deets and physics.
# on hold for nowsies

#why do I have to be so inconsistent
# CURRENTLY INCLUDES:

# Testball: RETURNS pygame surface with shitty ball 32x32
# arrayball: MAKES self.ball_array, a numpy array with pixel colors for dumb_ball

# Put it into a fucking dict who cares
# all separate Surfaces + dict for return in different formats
ball16 = pg.image.load(os.path.join('Assets', 'lightdark-ball_light.png'))
ball32 = pg.transform.scale(
            pg.image.load(os.path.join('Assets', 'shittyball.png')), [32, 32])

OBJECT_LIBRARY = {
    "ball16": ball16,
    "ball32": ball32,
    "ball16_np":np.array(pg.PixelArray(ball16)),
    "ball32_np":np.array(pg.PixelArray(ball32)),
}
def get_obj(name):
    return OBJECT_LIBRARY[name]

class gameobject:
    def __init__(self, func):
        self.func()

    
    def testball(self):
        return pg.transform.scale(
            pg.image.load(os.path.join('Assets', 'shittyball.png')), [32, 32])

    def arrayball(self):
        b = pg.image.load(os.path.join('Assets', 'dumb_ball.png'))
        self.ball_array = np.array(pg.PixelArray(b))