# THIS IS NOT MY CODE I'M JUST TOO LAZY TO FORK OR DL FROM GITHUB CORRECTLY
# From: https://github.com/davidpendergast/pygame-utils/

import pygame
import numpy
import os

# so this is a mess
#RW, RH = 400,400
#W, H = 200, 200
#MW, MH = (RW/W, RH/H) # mults for repeat

# REPLACE WITH:
W,H = 75,75
MDISP = 2
FPS = 60

BLACK = 0x000000

FLAGS = 0 #  | pygame.SCALED
SHIFTS = [(0, 1), (-1, 0), (1, 0), (0, -1),(0,0)]

class State:
    def __init__(self): # on init: create grid of random colors with size WxH
        self.reset()

    def step(self):
        pass

    def draw(self, screen):
        if MDISP == 1:
            drawgrid = self.grid
        else:
            drawgrid = numpy.repeat(numpy.repeat(self.grid,MDISP,axis=1),MDISP,axis=0)

        pygame.surfarray.blit_array(screen, drawgrid)

    def reset(self):
        self.grid = numpy.full((W,H),BLACK)

def setdisplay():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (W,H)
    return pygame.display.set_mode((W*MDISP,H*MDISP),flags = FLAGS)
    
    
if __name__ == "__main__":
    pygame.init()
    screen = setdisplay()
    state = State()
    clock = pygame.time.Clock()
    
    running = True
    last_update_time = pygame.time.get_ticks()

    while running:
        current_time = pygame.time.get_ticks()
        dt = (current_time - last_update_time) / 1000
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                running = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    print("Resetting.")
                    state = State()
                elif e.key == pygame.K_RIGHT:
                    FPS += 10
                    print("Increased target FPS to: {}".format(FPS))
                elif e.key == pygame.K_LEFT:
                    FPS = max(10, FPS - 10)
                    print("Decreased target FPS to: {}".format(FPS))
                elif e.key == pygame.K_UP:
                    MDISP += 1
                    print("MDISP now {}".format(MDISP))
                    screen = setdisplay()
                elif e.key == pygame.K_DOWN and MDISP > 2:
                    MDISP -= 1
                    print("MDISP now {}".format(MDISP))
                    screen = setdisplay()
        state.step()
        state.draw(screen)

        pygame.display.flip()

        if current_time // 1000 > last_update_time // 1000:
            
            #[LINE]
            pygame.display.set_caption("FPS:{:.1f}|TARGET:{}|RES:{}"
            .format(clock.get_fps(), FPS, (W * MDISP, H * MDISP)))
            #[ENDL]

        last_update_time = current_time
        clock.tick(FPS)
