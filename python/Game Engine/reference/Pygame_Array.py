import pygame as pg
import os
import numpy as np

from pygame.event import get
from src.game_time import game_time as gt
from src.windowhandler import centerwindow as center # prob don't need for now
#--------------
#* code to get screen resolution. Put in own file?
from screeninfo import get_monitors
MONITORS = get_monitors()
SCREENW = MONITORS[0].width
SCREENH = MONITORS[0].height
#--------------
# TODO: CLEAN THIS FUCKING SHIT UP

# for later:
from pygame._sdl2.video import Window

# General Details:
W,H = 600,400
MDISP = 1
FPS = 120
FLAGS = 0



def drawto(screen,surf):
    pass

def initialize():
    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    return pg.display.set_mode((W*MDISP,H*MDISP)) #,pg.NOFRAME)

def main():
    # Base setup for launch
    global MDISP
    screen = initialize()
    running = True
    redraw = True
    igt = gt(pg.time)

    
    arr_color = np.random.randint(0,0xFFFFFF,(600,400))
    test_object = pg.Surface((600,400))
    test_rect = test_object.get_rect()
    #test_object = get_obj('ball16')
    #test_rect = test_object.get_rect()
    #test_rect = test_rect.move(100,100)
    screen.fill((0,0,0))
    #mainloop
    while running:
        igt.frame() # record in-game time
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                running = False
            elif e.type == pg.KEYDOWN: 
                if e.key == pg.K_r:
                    print("Resetting.")
                if e.key == pg.K_w:
                   pass
                if e.key == pg.K_s:
                    pass
                if e.key == pg.K_a:
                    pass
                if e.key == pg.K_d: 
                    pass
        if redraw:
            pg.surfarray.blit_array(screen,arr_color)
            #screen.blit(test_object,test_rect)
            pg.display.flip()
           # drawto(screen,test_object)
            redraw = False


if __name__ == "__main__":
    main()