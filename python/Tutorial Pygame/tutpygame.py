import pygame as pg
import os

#Defining Constants:
#WIDTH/HEIGHT will be used as game window size along with any calculations requiring locational information
WIDTH,HEIGHT = 900,500
#WIN = Window of game
WIN = pg.display.set_mode((WIDTH,HEIGHT))
#Colors for easier use
WHITE = (255,255,255)
BLACK = (0,0,0)

#==[JUST TO HAVE ON HAND: RANDOM SHIT FOR LEARNING]==
#For Making Pygame Fullscreen:
#DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#Making a border for player movement:
BORDER = pg.Rect(WIDTH/2-5,0,10,HEIGHT)

FPS = 60
pg.display.set_caption("Game that game fart")

#Loading Images for use in game:
#Using OS to find path to images. os.path.join(folder,filename) - path.join(path1,path2,path3) etc
#When looking for path to anything, begins looking from folder being executed from. In this case is Pyle, and not the tutorial pygame folder directly
PLAYERSHIP_IMAGE = pg.image.load(os.path.join('Assets','ship_0000.png'))
ENEMYSHIP1_IMAGE = pg.image.load(os.path.join('Assets','ship_0005.png'))

SHIPWIDTH, SHIPHEIGHT = 50,50
#Resizing: pg.transform.scale
PLAYERSHIP = pg.transform.scale(PLAYERSHIP_IMAGE,(SHIPWIDTH, SHIPHEIGHT))
#Rotation: pg.transform.rotate
PLAYERSHIP = pg.transform.rotate(PLAYERSHIP,270)
ENEMYSHIP1 = pg.transform.rotate(pg.transform.scale(ENEMYSHIP1_IMAGE,(SHIPWIDTH,SHIPHEIGHT)),90)


#Gameplay Variables
VEL = 2
BULLET_VEL = 7

def draw_window(player, enemy):
        WIN.fill(WHITE)
        #Drawing images: 0,0 = top left, +X = further right, +Y = further down
        pg.draw.rect(WIN,BLACK,BORDER)
        WIN.blit(PLAYERSHIP,(player.x,player.y))
        WIN.blit(ENEMYSHIP1,(enemy.x,enemy.y))
        pg.display.update()

def player_movement(player, keys_pressed):
    if keys_pressed[pg.K_a] and player.x - VEL +(player.width*0.2) > 0: #Left
       player.x -= VEL
    if keys_pressed[pg.K_d] and player.x + VEL + (0.8*player.width) < BORDER.x : #Right
        player.x += VEL
    if keys_pressed[pg.K_s] and player.y + VEL + (0.9*player.height) < HEIGHT: #Down
        player.y += VEL
    if keys_pressed[pg.K_w] and player.y - VEL > 0: #Up
        player.y -= VEL


def main():
    #defining sprite/character sizes
    player = pg.Rect(200,300,SHIPWIDTH,SHIPHEIGHT)
    enemy = pg.Rect(700,300,SHIPWIDTH,SHIPHEIGHT)

    bullets = []

    #Defining FPS
    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        #Movement of player:
        #player.x += 1

        keys_pressed = pg.key.get_pressed()
#------------------STARTING FROM HERE NEXT TIME-------------------------------
        player_movement(player,keys_pressed)

        draw_window(player,enemy)
    pg.quit()




if __name__ == "__main__":
    main()
