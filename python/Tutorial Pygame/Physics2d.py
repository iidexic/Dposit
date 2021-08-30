import sys, os, pygame as pg
import numpy
"""
TODO:[NEXT STEPS]
    * Implementation of Collisions
    * Implementation of Friction/Air Drag
    * Implementation of Angular Velocity
    [LATER]
    * Figure out how to make actual physics independent of screen size/FPS (should not be that hard if I'm not an idiot)
    * Get a good color system going
    
    
"""
pg.init()
#Check the original at: https://www.pygame.org/docs/tut/PygameIntro.html

#Added clock to keep framerate in check. This is also basically the game's internal clock
clock = pg.time.Clock() 
FPS = 120
size = width, height = 640, 480 #Size of screen, also used for spatial calculations
speed = [0, 0] #Initialized ball velocity in [x,y] (I think)

#TODO IN FUTURE: MAKE A BETTER SETUP TO HANDLE COLORS

black = 0, 0, 0 #Color black
white = 255,255,255 #Color white
GRAVITY = 400 #Set grav for physics calculations
WIN = pg.display.set_mode(size) #initializing screen, ie window everything is drawn to

# random initializations. I don't like this and it's bad (also didn't work anyway so it's gone)
ball = pg.transform.scale(pg.image.load(os.path.join('Assets','shittyball.png')), [32,32])
#===[VELOCITY CALCULATIONS]==============
def calculateVelocity(object,vel,accel):
    #Bouncing Script. It's Shit really.
    #TODO NOW: FIX THIS DUMB THING
    #ISSUE: The velocity can be high enough (with gravity) that the object is 
    #         past 0 on 2 consecutve frames.This just fucks up this whole idea. 
    if object.left < 0 and vel[0] < 0 or object.right > width and vel[0] > 0:
        vel[0] = -vel[0]
    if object.top < 0 and vel[1] < 0 or object.bottom > height and vel[1] > 0:
        vel[1] = -vel[1]



    

    #Gravity Addition:
    vel[1] += GRAVITY/(FPS)

def main(): #clock, width, height, speed, black, WIN, ball
    ballrect = ball.get_rect()
    while 1:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        #=[BOUNCING FUNCTION:]
        #earlier, speed was initialized as [x,y] velocities
        calculateVelocity(ballrect,speed,[0,0])


        WIN.fill(black)
        WIN.blit(ball, ballrect)
        pg.display.flip()

if __name__ == "__main__":
    main()
