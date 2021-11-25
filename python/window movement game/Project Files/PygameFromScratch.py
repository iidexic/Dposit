import pygame as pg
import os

from pygame.event import get
from game_time import game_time as gt
from gameobjects import get_obj
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


def centerwindow():
    center = ((SCREENW - (W*MDISP))/2, (SCREENH - (H*MDISP))/2)
    return center

def drawto(screen,surf):
    pass

def main():
    # Base setup for launch
    global MDISP
    pg.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pg.display.set_mode((W*MDISP,H*MDISP))#,pg.NOFRAME)
    running = True
    redraw = True
    igt = gt(pg.time)
    test_object = get_obj('ball16')
    test_rect = test_object.get_rect()
    x,y = 10,10
    test_rect = test_rect.move(100,100)
    screen.fill((0,0,0))
    blorb = pg.Surface((100,60))
    glarg = pg.draw.line(blorb,0xFFFFFF,(20,20),(40,40),4)
    glorg = pg.draw.rect()
    screen.blit(blorb, glarg)
    screen.blit(blorb,glorg)
    screen.blit(test_object,test_rect)
    #screen.ref
    #mainloop
    while running:
        igt.frame() # record in-game time\
        
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                running = False
            elif e.type == pg.KEYDOWN: 
                if e.key == pg.K_r:
                    print("Resetting.")
                if e.key == pg.K_w:
                   screen.blit(blorb, glarg)
                if e.key == pg.K_s:
                    screen.blit(blorb, glorg)
                if e.key == pg.K_a:
                    pass
                if e.key == pg.K_d: 
                    pass
        if redraw:
            
            pg.display.flip()
           # drawto(screen,test_object)
            redraw = False


if __name__ == "__main__":
    main()