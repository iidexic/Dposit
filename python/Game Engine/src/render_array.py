import pygame as pg

import numpy as np

class output_array:
    def __init__(self,size):
        self.screensize = size
        self.output = np.empty(size)
    def bg_color(self,color):
        self.output[:] = color



class gameobj:
    def __init__(self,tex,size,loc=(0,0),rot=0, pos=5):
        if type(tex) == str:
            self.pix = pg.PixelArray(pg.image.load(tex))
