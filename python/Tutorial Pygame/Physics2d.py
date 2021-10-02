# import sys
import os
import pygame as pg
# import numpy as np
"""
TODO:[NEXT STEPS]
    ********IMPLEMENT ACTUAL EXIT FUNCTIONALITY JUST IN CASE
    * MOVE TO VECTOR2 also just actually learn pygame
    * Figure out how Pygame Layering works (Is it just order of )
    * Implementation of Collisions
    * Implementation of Friction/Air Drag
    * Implementation of Angular Velocity
    [LATER]
    * Figure out how to make actual physics independent of screen size/FPS
    * Get a good color system going
    * Learn how to use pg.display.update to selectively update
        using method of blitting created in the cleanloop

"""
pg.init()
# Check the original at: https://www.pygame.org/docs/tut/PygameIntro.html

# Added clock to keep framerate in check. Also game's internal clock
clock = pg.time.Clock()
FPS = 120
size = width, height = 640, 480  # Size of screen
speed = [0, 0]  # Initialized ball velocity in [x,y] (I think)

# TODO IN FUTURE: MAKE A BETTER SETUP TO HANDLE COLORS

black = 0, 0, 0  # Color black
white = 255, 255, 255  # Color white
GRAVITY = 120  # Set grav for physics calculations
WIN = pg.display.set_mode(
    size)  # initializing screen, ie window everything is drawn to\

# Toggle for debug display


ball = pg.transform.scale(pg.image.load(
    os.path.join('Assets', 'shittyball.png')), [32, 32])
# ===[VELOCITY CALCULATIONS]==============


def calculateVelocity(gameobj, vel, accel):
    applygrav = True  # eliminates gravity decay

    # We check whether an object is "Out of Bounds", as well as whether its
    # velocity would place it more out of bounds on the axis it's going
    if gameobj.left < 0 and vel[0] < 0 \
            or gameobj.right > width and vel[0] > 0:
        vel[0] = -vel[0]
    if gameobj.top < 0 and vel[1] < 0 \
            or gameobj.bottom > height and vel[1] > 0:
        vel[1] = -vel[1]
        applygrav = False
    # Gravity Addition:
    if applygrav:
        vel[1] += GRAVITY/(FPS)
        # New Test: Replacing FPS variable with clock.get_fps() to deal
        # with framerate variance
    # gameobj = calculateAngular(vel, ball)

# this shit aint working fam


def calculateAngular(vel, img):
    return pg.transform.rotate(img, 30).get_rect()


# Collisions: Only way I can think of right now is to loop through everything
# and make sure they aren't hitting each other. Better way?
# if want to define my own objects I will have to make lists that contain both
# the pygame rect and whatever transformations I will use to calculate the
# def debugDisplay()

# LEARNING TEXT:


def main():  # clock, width, height, speed, black, WIN, ball
    ballrect = ball.get_rect()

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        ballrect = ballrect.move(speed)
        # =[BOUNCING FUNCTION:]
        # earlier, speed was initialized as [x,y] velocities
        calculateVelocity(ballrect, speed, [0, 0])

        WIN.fill(black)
        WIN.blit(ball, ballrect)
        pg.display.update()
    pg.quit()


if __name__ == "__main__":
    main()
