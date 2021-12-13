import pygame as pg
# TODO: Class where can add new userevent names in a dict
# this really is probably not the most importan tthing to be doing right now
#! shit just isn't working, back burner
"""
def check_events(events):
    actions = []
    for e in events:
        if e.type == pg.QUIT or (e.type == pg.KEYDOWN and 
                                    e.key == pg.K_ESCAPE):
            pg.quit()
            running = False
        elif e.type == pg.KEYDOWN:
            pass
        elif e.type == CAPTION:
            pass
            print(e)
            #write_text(igt)
"""          
            
class loop:
    def __init__(self,igt, event_handler = None):
        self.igt = igt
    def set_screen(self,screen):
        self.screen = screen
    def enter_loop(self, running = False):
        while running:
            #* ===[ game loop ]===
            self.igt.frame() # start
            
            
            self.igt.endframe() # end
            #* =================

            
class event_handler:
    def __init__(self,igt):
        pass