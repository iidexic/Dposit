import pygame

pygame.init()
running = True
screen = pygame.display.set_mode((400,400))
controller = pygame.joystick.Joystick(0).init()
clock = pygame.time.Clock()
while running:
    for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                running = False
            elif e.type == pygame.KEYDOWN: 
                if e.key == pygame.K_r:
                    print(clock.get_fps())
            elif e.type == pygame.JOYAXISMOTION:
                print('?')
                pass

    clock.tick(120)