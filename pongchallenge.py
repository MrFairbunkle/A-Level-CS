# imports
import pygame, random, sys

# general code
pygame.display.set_caption("BadPong")
clock=pygame.time.Clock()
screen_width=1000
screen_height=500

pygame.init()

# variables
screen=pygame.display.set_mode((screen_width,screen_height))
timepassed=0
redsize=15
bluesize=15
ballwidth=7
ballradius=7
redsquare=pygame.Rect(920,200,redsize,redsize*6)
bluesquare=pygame.Rect(80,200,bluesize,bluesize*6)
ball=pygame.Rect(screen_height//2,screen_width//2,ballwidth,ballradius)
redsquare.y
bluesquare.y
ball.y
ball.x
pygame.display.flip()
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)

# main loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    key = pygame.key.get_pressed()
    if key[pygame.K_w]: 
        if bluesquare.y - 5 >= 0:
            bluesquare.y-=5
    if key[pygame.K_s]:
        if bluesquare.y + 5 <= screen_height - 80:
            bluesquare.y+=5
    if key[pygame.K_UP]:
        if redsquare.y - 5 >= 0:
            redsquare.y-=5
    if key[pygame.K_DOWN]:
        if redsquare.y + 5 <= screen_height - 80:
            redsquare.y+=5

    while ball.x<=0:
        ball.x+=5

    screen.fill("#ffffff")
    pygame.draw.rect(screen,RED,redsquare)
    pygame.draw.rect(screen,BLUE,bluesquare)
    pygame.draw.circle(screen,(BLACK),(screen_width//2,screen_height//2),ballwidth,ballradius)

    pygame.display.update()
    clock.tick(60)