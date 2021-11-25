import pygame as pg
import os

#! TODO: STOP CODING SHIT THAT LITERALLY DOES NOT MATTER RIGHT NOW
# ====[Pygame Window handler]====
# used to handle all window movement (and the window itself?)
def setup(something):
    os.environ['SDL_VIDEO_CENTERED'] = '1'

#* Will need to build class to use this:    
def centerwindow(w,h,sw,sh):
    pass
    center = ((sw - (w))/2, (sh - (h))/2)
    return center


class windowhandler:
    def __init__(self,startres,m = 1): #m = pixel mult, is this necessary?
        pg.init()
        self.width = startres[0]
        self.height = startres[0]
        self.res = (self.width, self.height)
        

    def setvelocity(self, vel):
        self.vel = vel
    
    def addvel(self, vel):
        self.vel += vel
    
    def setposition(self,pos):
        self.position = pos
    
    def monitor_info(self, monitor = 0):
        from screeninfo import get_monitors
        MONITORS = get_monitors()
        self.screen_w = MONITORS[monitor].width
        self.screen_h = MONITORS[monitor].height

    def centerwindow(self, m = 1):
        center = ((self.screen_w - (self.width*m))/2, 
                (self.screen_h - (self.height*m))/2)
        return center
    
    def start(self):
        self.window = pg.display.set_mode(self.res)
        
    def update(self,function_list):
        """
        Takes list of all functions required for a screen refresh.
        Does not require pg.flip(),
        """
        
        #--------Applying Velocities-----------
        
        #--------------------------------------
        for i in function_list:
            pass