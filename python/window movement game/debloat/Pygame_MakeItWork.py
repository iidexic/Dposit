import pygame as pg
import os

#from pygame.event import get
#from game_time import game_time as gt
#from gameobjects import get_obj
#--------------


# for later:
from pygame._sdl2.video import Window

# General Details:
W,H = 600,400
MDISP = 1
FPS = 120
FLAGS = 0



def main():
    pg.init()
    screen = pg.display.set_mode((500,500))#,pg.NOFRAME)
    gray = pg.Surface((500,500))
    gray.fill((200,200,200))
    running = True
    screen.fill(0xFFFFFF)
    screen.blit(gray,(0,0))
    #mainloop
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                running = False
            
            screen.blit(gray,(0,0))
            pg.display.flip()
        


if __name__ == "__main__":
    main()