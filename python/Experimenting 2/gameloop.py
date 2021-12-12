import pygame as pg
import os
import pgphys as phys
import asset_handler 
RES = W,H = 640, 480



def main():
    pg.init()
    screen = pg.display.set_mode((RES))
    running = True
    spritesheet = asset_handler.spritelib('SPRITESHEET.png','SPRITESHEET.json',mode = 'slices')
    sprites = list(spritesheet.sprites.values())
    x = 10
    y = 100
    for s in sprites:
        
        screen.blit(pg.transform.scale(s,(48,48)),(x,y))
        x += 60
        if x > 600:
            x = 10
            y += 60
    print(spritesheet.sprites)
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and 
                                     e.key == pg.K_ESCAPE):
                pg.quit()
                running = False
            elif e.type == pg.KEYDOWN:
                pass
        pg.display.flip()           

if __name__ == '__main__':
    main()