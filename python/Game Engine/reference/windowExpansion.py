import sys
import os
sys.path.insert(1, os.path.join(os.getcwd(),'Project Files'))

import pygame
import numpy
import src.assethandler as gobj
# TODO: Decide if NOFRAME IS GOING TO STAY OR NOT

from pygame._sdl2.video import Window
# Grabbing monitor info. TODO: may have to get all screens later if want compatibility with multi-monitor
from screeninfo import get_monitors
MONITORS = get_monitors()
SCREENW = MONITORS[0].width
SCREENH = MONITORS[0].height
TIMER = 0

XV = 0
YV = 0
WV = 0
HV = 0
# REPLACE WITH:
W,H = 200,100
MDISP = 2
FPS = 60

BLACK = 0x000000

FLAGS = 0 #  | pygame.SCALED
SHIFTS = [(0, 1), (-1, 0), (1, 0), (0, -1),(0,0)]

class State: # a relic that I've yet to remove or redo.
    def __init__(self): # on init: create grid of random colors with size WxH
        self.reset()

    def step(self):
        pass

    def draw(self, screen):
        if MDISP == 1:
            drawgrid = self.grid
        else:
            drawgrid = numpy.repeat(numpy.repeat(self.grid,MDISP,axis=1),MDISP,axis=0)

        pygame.surfarray.blit_array(screen, drawgrid)

    def reset(self):
        self.grid = numpy.full((W,H),BLACK)

def centerwindow():
    center = ((SCREENW - (W*MDISP))/2, (SCREENH - (H*MDISP))/2)
    return center

def movewindow(window,screen):
    
    global W, H
    x,y = window.position
    x += XV
    y += YV
    W += WV
    H += HV
    if (XV,YV,WV,HV) != (0,0,0,0) or pygame.display.get_window_size() != (W*MDISP,H*MDISP):
         screen = setdisplay(window)
    window.position = (x,y)
    

def setdisplay(window):
    # os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (centerwindow())
    #print(window.position)
    return pygame.display.set_mode((W*MDISP,H*MDISP))#,pygame.NOFRAME)

def resetvelocity():
    global HV,WV,XV,YV
    HV = 0
    WV = 0
    YV = 0
    XV = 0


def DVDLogo(window):
    global XV
    global YV
    x = -(XV)
    y = -(YV)
    wMax = W*MDISP + window.position[0]
    hMax = H*MDISP + window.position[1]
    wMin = window.position[0]
    hMin = window.position[1]
    if wMax >= (SCREENW-1) or wMin <= 1:
        XV = x
    if hMax >= (SCREENH-1) or hMin <= 1:
        YV = y


def expandwindow(dir):
    global XV,YV,W,H,HV,WV
    if dir == 'u':
        HV += 1
        YV += -MDISP
    elif dir == 'd':
        HV += 1 
    elif dir == 'l':
        WV += 1
        XV += -MDISP
    elif dir == 'r':
        WV += 1

if __name__ == "__main__":
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((W*MDISP,H*MDISP))#,pygame.NOFRAME)
    window = Window.from_display_module()
    window.position = centerwindow()
    screen = setdisplay(window)
    state = State()
    clock = pygame.time.Clock()
    running = True
    last_update_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()
        dt = (current_time - last_update_time) / 1000
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                running = False
            elif e.type == pygame.KEYDOWN: 
                if e.key == pygame.K_r:
                    print("Resetting.")
                    state = State()
                elif e.key == pygame.K_RIGHT:
                    FPS += 10
                    print("Increased target FPS to: {}".format(FPS))
                elif e.key == pygame.K_LEFT:
                    FPS = max(10, FPS - 10)
                    print("Decreased target FPS to: {}".format(FPS))
                elif e.key == pygame.K_UP:
                    MDISP += 1
                    print("MDISP now {}".format(MDISP))
                    screen = setdisplay(window)
                elif e.key == pygame.K_DOWN and MDISP > 2:
                    MDISP -= 1
                    print("MDISP now {}".format(MDISP))
                    screen = setdisplay(window)
                elif e.key == pygame.K_w:
                    expandwindow('u')
                    state.reset()
                    screen = setdisplay(window)
                elif e.key == pygame.K_s:
                    expandwindow('d')
                    state.reset()
                    screen = setdisplay(window)
                elif e.key == pygame.K_a:
                    expandwindow('l')
                    state.reset()
                    screen = setdisplay(window)
                elif e.key == pygame.K_d:
                    expandwindow('r')
                    state.reset()
                    screen = setdisplay(window)
            elif e.type == pygame.KEYUP:
                pass
            
        #DVDLogo(window)
        #print(TIMER)
        movewindow(window,screen)
        if (XV,YV,WV,HV) != (0,0,0,0) and TIMER == 0:
            TIMER = 60
        if TIMER > 0:
            TIMER -= 1
            if TIMER <= 0:
                resetvelocity()

        pygame.display.flip()
        
        if current_time // 1000 > last_update_time // 1000:
            pass
            #[LINE]
            pygame.display.set_caption("FPS:{:.1f}|TICK:{}|RES:{}"
            .format(clock.get_fps(), dt, pygame.display.get_window_size()[0]))
            #[ENDL]

        last_update_time = current_time
        clock.tick(FPS)
