import pygame as pg
# Making a clean pygame setup to experiment from


RES = WIDTH, HEIGHT = 900, 500
WIN = pg.display.set_mode((RES))
BLACK = 0, 0, 0
FPS = 60


def draw_window(blitlist):
    WIN.fill(BLACK)
    # Drawing images: 0,0 = top left, +X = further right, +Y = further down
    # pg.draw.rect(WIN,colorval,rectangle,((width)),((radius)))
    for item in blitlist:
        doblit(item)
    next

    pg.display.update()


# Does this need to be a function?
def doblit(drawobj):
    WIN.blit(drawobj[0], drawobj[1])


def main():  # clock, width, height, speed, black, WIN, ball
    # init rect if neccessary

    while 1:
        objlist = []
        pg.clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        # Any Objects that need to be drawn this frame can be appended to objlist in the format:
        # objlist.append([rectname,[x,y]])

        draw_window(objlist)


if __name__ == "__main__":
    main()
