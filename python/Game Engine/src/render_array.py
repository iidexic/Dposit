import pygame as pg

import numpy as np

class output_array:
    def __init__(self,size,bg_color = 0x000000):
        self.screensize = size
        self.background = np.full(size,bg_color)
        self.output = np.full(size,bg_color)
        
    def write_at(self,array, loc = (0,0)):
        (x,y) = loc
        #trim to size. this covers all 4 directions
        if x < 0 or y < 0: 
            pass
        if (array.shape[0]+x < self.output.shape[0]) or (
            array.shape[1]+y < self.output.shape[1]):
            pass #can write full array
        # write over:
        self.output[x:x+array.size[0],y:y+array.size[0]] = array
        
    def wipe(self):
        self.output = np.
        
            
            


