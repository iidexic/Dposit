# THIS IS NOT MY CODE I'M JUST TOO LAZY TO FORK OR DL FROM GITHUB CORRECTLY
# From: https://github.com/davidpendergast/pygame-utils/

import pygame
import numpy

RW, RH = 400,400
W, H = 200, 200
MW, MH = (RW/W, RH/H) # mults for repeat
FPS = 22

FLAGS = 0 #  | pygame.SCALED
SHIFTS = [(0, 1), (-1, 0), (1, 0), (0, -1),(0,0)]

class State:
    def __init__(self):
        self.grid = numpy.random.randint(0, 0xFFFFFF + 1, (W, H), numpy.int32)

    def step(self):
        shifted = [] 
        # STEP 1: Create a list of arrays for each direction (4 cardinal + 4 diagonal) can be shifted
        for dx, dy in SHIFTS:
            # Here we append a shifted (rolled) version of the grid array
            shifted.append(numpy.roll(self.grid, (dx, dy), (0, 1)))
        
        rand_vals = numpy.random.randint(0, len(shifted), (W, H), numpy.int16)

        masks = []
        for i in range(len(shifted)):
            masks.append(1 * (rand_vals == i))

        self.grid[:] = 0
        for i in range(len(shifted)):
            self.grid += masks[i] * shifted[i]

    def draw(self, screen):
        pygame.surfarray.blit_array(screen, numpy.repeat(numpy.repeat(self.grid,MH,axis=1),MW,axis=0))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((RW, RH), flags=FLAGS)
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
        state.step()
        state.draw(screen)

        pygame.display.flip()

        if current_time // 1000 > last_update_time // 1000:
            pygame.display.set_caption("Color Swirl (FPS={:.1f}, TARGET_FPS={}, SIZE={})".format(clock.get_fps(), FPS, (W, H)))

        last_update_time = current_time
        clock.tick(FPS)
