import pygame as pg
import sys
import os
# Making a clean pygame setup to experiment from

FLAGS = 0 #|pygame.SCALED
FPS = 60
# res used for actual image size, MDISP for sizing to window
RES = W,H = 250, 250
MDISP = 2

BLACK = 0, 0, 0



def draw_window(blitlist, screen):
    screen.fill(BLACK)
    # Drawing images: 0,0 = top left, +X = further right, +Y = further down
    # pg.draw.rect(WIN,colorval,rectangle,((width)),((radius)))
    for item in blitlist:
        doblit(item, screen)
    next

    pg.display.update()

def setdisplay():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (W,H)
    return pg.display.set_mode((W*MDISP,H*MDISP),flags = FLAGS)

# Does this need to be a function?
def doblit(drawobj,screen):
    screen.blit(drawobj[0], drawobj[1])
    

def main():  # clock, width, height, speed, black, WIN, ball
    # init rect if neccessary
    pg.init()
    screen = setdisplay()
    clock = pg.time.Clock()
    running = True
    objlist = []
    
    while running:

        clock.tick(FPS)
        elapsed = pg.time.get_ticks()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_RIGHT:
                    FPS += 10
                    print("Increased target FPS to: {}".format(FPS))
                elif e.key == pg.K_LEFT:
                    FPS = max(10, FPS - 10)
                    print("Decreased target FPS to: {}".format(FPS))
        # Any Objects that need to be drawn this frame can be appended to objlist in the format:
        # objlist.append([rectname,[x,y]])

        draw_window(objlist, screen)


if __name__ == "__main__":
    main()
