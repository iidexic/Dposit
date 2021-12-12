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
            
class events_dynamic:
    def __init__(self,event):
        self.event = event
        self.userevent = {}
    def check_events(self):
        for e in self.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and 
                                        e.key == pg.K_ESCAPE):
                pg.quit()
                running = False
            elif e.type == pg.KEYDOWN:
                pass
            elif e.type in self.userevent:
                for u in self.userevent.keys:
                    if e.type == u:
                        print('checked')
    def new_event(self,name):
        self.userevent[name] = pg.USEREVENT
        