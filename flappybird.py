# Imports 
import pygame, random, time, sys


# General code
pygame.init()
pygame.display.set_caption("FlappyBird")
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500
font = pygame.font.SysFont('Bauhaus 93', 20)


# Variables
screen = pygame.display.set_mode((screen_width, screen_height))
score = 0
gametime = 0
birdwidth = 7
birdradius = 7
pillargap = 200
pillarwidth = 35
pillarheight = random.randint(50, screen_height - pillargap - 50)

bottompillar = pygame.Rect(700, 0, pillarwidth, pillarheight)
toppillar = pygame.Rect(pillarheight, pillarheight + pillargap, pillarwidth, screen_height - pillarheight - pillargap)

bird = pygame.Rect(300, screen_height // 2, birdwidth, birdradius)
pillar_speed_x = 0
pillar_speed_y = 0
bird_speed_x = 0
bird_speed_y = 0 
gravity = 0.5 
last_score_update = time.time()
bottompillar_speed_x = -5
bottompillar_speed_y = 0 
toppillar_speed_x = -5 
toppillar_speed_y = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (53, 129, 34)
BLACK = (0, 0, 0)
WHITE = (230, 230, 230)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()

    bottompillar.x += bottompillar_speed_x
    bottompillar.y += bottompillar_speed_y
    toppillar.x += toppillar_speed_x
    toppillar.y += toppillar_speed_y

    if key[pygame.K_SPACE]:
        bird_speed_y = -7

    # Apply gravity
    bird_speed_y += gravity

    # Update bird position
    bird.x += bird_speed_x
    bird.y += bird_speed_y

    # Update pillar position
    bottompillar.x += pillar_speed_y
    bottompillar.y += pillar_speed_x
    toppillar.x += pillar_speed_y
    toppillar.y += pillar_speed_x

    if toppillar.right < 0:
        pillarheight = random.randint(50, screen_height - pillargap - 50)
        toppillar.height = pillarheight
        bottompillar.y = pillarheight + pillargap
        toppillar.x = screen_width
        bottompillar.x = screen_width

    # Ensure bird stays within the screen bounds
    if bird.top <= 0:
        bird.top = 0
        bird_speed_y = 0
    if bird.bottom >= screen_height:
        bird.bottom = screen_height
        bird_speed_y = 0

    # Check for collisions with pillars
    if bird.colliderect(bottompillar) or bird.colliderect(toppillar):
        sys.exit()

    # Check if it's time to update the score (every second)
    current_time = time.time()
    if current_time - last_score_update >= 1:
        score += 1
        last_score_update = current_time

    # Colour the screen
    screen.fill(WHITE)

    # Draw objects
    pygame.draw.rect(screen, GREEN, toppillar)
    pygame.draw.rect(screen, GREEN, bottompillar)
    pygame.draw.circle(screen, BLACK, (bird.x, bird.y), birdwidth, birdradius)

    # Render text surfaces for red and blue scores
    score_text = font.render("Score: " + str(score), True, BLACK)

    # Blit the text surfaces onto the screen
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
