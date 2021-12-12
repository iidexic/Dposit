import pygame as pg
import os
import src.asset_handler as assets
from src.game_time import game_time
#from src.event_handler import events_dynamic #failure

RES = W,H = 640, 480
FPS = 30



def write_text(igt):
    pg.display.set_caption('FPS:{:.1f}'.format(igt.clock.get_fps()))
    
#what the fuck do we do about this
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

def show_all_sprites(sprites,screen):
    x = 10
    y = 100
    for s in sprites:
        screen.blit(pg.transform.scale(s,(48,48)),(x,y))
        x += 60
        if x > 600:
            x = 10
            y += 60

def main():
    
    pg.init()
    igt = game_time(pg.time,pg.time.Clock(),FPS = FPS)
    screen = pg.display.set_mode((RES))
    running = True
    spritesheet = assets.spritelib('SPRITESHEET.png','SPRITESHEET.json',mode = 'slices')
    sprites = list(spritesheet.sprites.values())
    
    #======== Placeholder just to show all sprites:============
    show_all_sprites(sprites,screen)
    #==========================================================
    #-Timer Figure out:-
    user_events = []
    CAPTION = pg.USEREVENT
    user_events.append(CAPTION)
    timer = igt.time.set_timer(CAPTION,1000)
    #-------------------
    
    while running:
        igt.frame()  
        event_checker(user_events,igt)    
        pg.display.flip()
        if igt.last % 50 == 0:
            print(igt.past)
        igt.endframe()
if __name__ == '__main__':
    main()