import pygame, random, sys
pygame.display.set_caption("BadPong")
clock=pygame.time.Clock()
screen_width=1000
screen_height=500

pygame.init()

screen=pygame.display.set_mode((screen_width,screen_height))
redsize=15
bluesize=15
redy=200
bluey=200
redsquare=pygame.Rect(920,redy,redsize,redsize*6)
bluesquare=pygame.Rect(80,bluey,bluesize,bluesize*6)
pygame.display.flip()
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    key = pygame.key.get_pressed()
    if key[pygame.K_w] == False: 
        bluey-=5
    if key[pygame.K_s]:
        bluey+=5
    if key[pygame.K_UP]:
        redy-=5
    if key[pygame.K_DOWN]:
        redy+=5

    screen.fill("#ffffff")
    pygame.draw.rect(screen,RED,redsquare)
    pygame.draw.rect(screen,BLUE,bluesquare)
    pygame.draw.circle(screen,(BLACK),(screen_width//2,screen_height//2),7,7)

    pygame.display.update()
    clock.tick(60)