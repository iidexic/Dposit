import pygame as pg
import numpy as np
import os
#* no nerd shit like sprites here
from src.game_time import game_time

RES = W,H = 1280, 720
FPS = 120



def write_text(igt):
    pg.display.set_caption('FPS:{:.1f}'.format(igt.clock.get_fps()))
    
    
def event_checker(user_events,igt):
    for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and 
                                        e.key == pg.K_ESCAPE):
                pg.quit()
                running = False
            elif e.type == pg.KEYDOWN:
                pass
            elif e.type in user_events:
                if e.type == user_events[0]:
                    write_text(igt)
                    
def draw_array(surf,array):
    pg.surfarray.blit_array(surf,array)
    
def overwrite(dest,source,loc):
    (x,y) = loc
    if (x < 0):
        source = source[abs(x):]
        x = 0
    if (y < 0):
        source = source[:,abs(y):]
        y = 0
    if (source.shape[0]+x > dest.shape[0]):
        source = source[:dest.shape[0]-x,:]
    if (source.shape[1]+y > dest.shape[1]):
        source = source[:,:(dest.shape[1]-y)]
    dest[x:x+source.shape[0],y:y+source.shape[1]] = source
    
def sizearray(size):
    arr = np.full(size,0x0A0A0A)
    arr[:,:5] = 0xEE0101
    arr[:5,:] = 0x01EE01
    return arr
    
    
def main():
    pg.init()
    igt = game_time(pg.time,pg.time.Clock())
    screen = pg.display.set_mode((RES))
    running = True
    
    #---Array Fun-------
    screenarray = np.full((RES),0x666666)
    white_square = np.full((250,250),0xEEEEFF)
    mystery1 = np.linspace(0x111111, 0xFFFFFF, 10000).reshape(100,100)
    mystery2 = np.linspace(0x444444, 0xFFFFFF, 10000).reshape(100,100)
    mystery3 = np.linspace(0x888888, 0xFFFFFF, 10000).reshape(100,100)
    mystery4 = np.linspace(0xBBBBBB, 0xFFFFFF, 10000).reshape(100,100)
    
    overwrite(screenarray,mystery1,(100,100))
    overwrite(screenarray,mystery2,(200,100))
    overwrite(screenarray,mystery3,(300,100))
    overwrite(screenarray,mystery4,(400,100))
    #-------------------
    
    #-Timer Figure out:-
    user_events = []
    CAPTION = pg.USEREVENT
    user_events.append(CAPTION)
    timer = igt.time.set_timer(CAPTION,1000)
    #-------------------
    
    draw_array(screen,screenarray)
    while running:
        igt.frame()
            
        event_checker(user_events,igt)    
        
        
        pg.display.flip()
        igt.endframe()
if __name__ == '__main__':
    main()