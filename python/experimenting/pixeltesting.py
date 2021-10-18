
import pygame as pg
from pygame import gfxdraw as gfx
import sys
from colortools import *

# IDEA: Instead of making random colors for specific pixels and modulating 
# based on that, make a random color once (or at specific points) and modulate.

RES = WIDTH, HEIGHT = 800, 400
WIN = pg.display.set_mode((RES))
BLACK = 0, 0, 0
FPS = 60
clock = pg.time.Clock()
requp = True

def draw_window(surface):
    WIN.fill(BLACK)
    # Drawing images: 0,0 = top left, +X = further right, +Y = further down
    #Blow up the surface before drawing hopefully?
    WIN.blit(pg.transform.scale(surface,(WIDTH,HEIGHT)),(0,0))

    pg.display.update()


#def randcolor( x, y): # Function gives random color

#    nowcolor = (rng.randint(0,255),rng.randint(0,255),rng.randint(0,255))
#    return nowcolor

def decidecolor(surface, color, x, y):

    # Start defautly off of previous color 
    # (is this neccessary? can getcolor of prev pixel)
    newcolor = color 
    newcolor = randcolor()
    # if (x % 2) == 0:  # (if X val is even)
    """if x <= 50:
        newcolor = randcolor()
    
    if x > 30:
        oldcolor = surface.get_at(((x-1),y))
        newcolor = (round((newcolor[0] + oldcolor[0])/2,0),
                    round((newcolor[1] + oldcolor[1])/2,0), 
                    round((newcolor[2] + oldcolor[2])/2,0))"""

    return newcolor


def pixelcolor(surface):
    color = (150,150,150)
    # Loop through each pixel, column by column
    for x in range (0,int(WIDTH/4)):
        for y in range(0,int(HEIGHT/4)):
            # Separate Function does color modifications based off whatever
            color = decidecolor(surface, color, x, y)
            # Draw color onto pixel at position x, y
            gfx.pixel(surface, x, y, color)
        next

def shufflepixel(surface):
    for x in range (1,int(WIDTH/4)-1):
        for y in range(1,int(HEIGHT/4)-1):
            # try:
            newpixel = [a + b for a, b in zip((x,y), randdirection())]
            color = surface.get_at(newpixel)
            # except:
            #   color = surface.get_at((x,y))

            gfx.pixel(surface, x, y, color)

def userinput(inputs, surface):
    # all inputs can go here
    if inputs[pg.K_r]:
        global requp
        requp = True
    if inputs[pg.K_s]:
        shufflepixel(surface)

def main():  # clock, width, height, speed, black, WIN, ball
    # decides if required update
    elapsed = 0
    # Literally all of this shit is arbitrary because I set this up dumb and am lazy
    mainsurf = pg.Surface((round(WIDTH/4),round(HEIGHT/4)))

    # [MAIN GAME LOOP]
    while 1:
        elapsed += 1
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        userinput(pg.key.get_pressed(), mainsurf)
        
        # Get Global update boolr
        global requp
        # Check if we need to update the screen
        if requp is True:
            pixelcolor(mainsurf)
            requp = False
        
        if (elapsed % 60) == 0:
            print(str(elapsed/60))
        shufflepixel(mainsurf)
        draw_window(mainsurf)


if __name__ == "__main__":
    main()
