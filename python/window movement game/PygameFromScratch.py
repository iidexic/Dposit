import pygame as pg
import os
from game_time import game_time as gt

#--------------
#* code to get screen resolution. Put in own file?
from screeninfo import get_monitors
MONITORS = get_monitors()
SCREENW = MONITORS[0].width
SCREENH = MONITORS[0].height
#--------------


# for later:
from pygame._sdl2.video import Window

# General Details:
W,H = 600,400
MDISP = 1
FPS = 120
FLAGS = 0

def centerwindow():
    center = ((SCREENW - (W*MDISP))/2, (SCREENH - (H*MDISP))/2)
    return center

def main():
    # Base setup for launch
    global MDISP
    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pg.display.set_mode((W*MDISP,H*MDISP))#,pg.NOFRAME)
    running = True
    igt = gt(pg.time)
    
    #mainloop
    while running:
        igt.frame() # record in-game time
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                running = False
            elif e.type == pg.KEYDOWN: 
                if e.key == pg.K_r:
                    print("Resetting.")
        
if __name__ == "__main__":
    main()