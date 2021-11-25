import pygame as pg
import os
import pgphys as phys

RES = W,H = 640, 480



def main():
    pg.init()
    screen = pg.display.set_mode((RES))
    running = True
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and 
                                     e.key == pg.K_ESCAPE):
                pg.quit()
                running = False
            elif e.type == pg.KEYDOWN:
                pass


if __name__ == '__main__':
    main()