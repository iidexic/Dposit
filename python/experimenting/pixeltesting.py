
import pygame as pg
from pygame import gfxdraw as gfx
import sys
import random as rng
# Making a clean pygame setup to experiment from

# THIS SHIT FUCKING WORKS OH MY GOD
# TODO: Figure out how to make random coloring 



# IDEA: Instead of making random colors for specific pixels and modulating 
# based on that, make a random color once (or at specific points) and modulate.

RES = WIDTH, HEIGHT = 500, 500
WIN = pg.display.set_mode((RES))
BLACK = 0, 0, 0
FPS = 60
clock = pg.time.Clock()


def draw_window(surface):
    WIN.fill(BLACK)
    # Drawing images: 0,0 = top left, +X = further right, +Y = further down
    # pg.draw.rect(WIN,colorval,rectangle,((width)),((radius)))
    
    # This will blit the surface in the center of the screen at standard scale:
    # WIN.blit(surface,(round(WIDTH/4),round(HEIGHT/4)))

    #Blow up the surface before drawing hopefully?
    WIN.blit(pg.transform.scale2x(surface),(0,0))

    pg.display.update()



def randcolor( x, y): # Function gives random color

    nowcolor = (rng.randint(0,255),rng.randint(0,255),rng.randint(0,255))
    return nowcolor

def decidecolor(surface, color, x, y):

    #Start defautly off of previous color
    newcolor = color 

    # For clarity sake we are going to start by grabbing a random color
    # If X val even
    if (x % 2) == 0:
        newcolor = randcolor(x,y)

    return newcolor


def pixelcolor(surface):
    color = (150,150,150)
    # Loop through each pixel, column by column
    for x in range (1,WIDTH):
        for y in range(1,HEIGHT):
            # Separate Function does color modifications based off whatever
            color = decidecolor(surface, color, x, y)
            # Draw color onto pixel at position x, y
            gfx.pixel(surface, x, y, color)
        next



def main():  # clock, width, height, speed, black, WIN, ball
    # decides if required update
    requp = True

    # Literally all of this shit is arbitrary because I set this up dumb and am lazy
    mainsurf = pg.Surface((round(WIDTH/2),round(HEIGHT/2)))

    # [MAIN GAME LOOP]
    while 1:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        pressedKeys = pg.key.get_pressed()
        # What the fuck is this stupid shit

        #Check if we need to update the screen
        if requp is True:
            pixelcolor(mainsurf)
            requp = False
            print(mainsurf.get_at((2,2)))
        
        # Any Objects that need to be drawn this frame can be appended to objlist in the format:
        # objlist.append([rectname,[x,y]])

        draw_window(mainsurf)


if __name__ == "__main__":
    main()
