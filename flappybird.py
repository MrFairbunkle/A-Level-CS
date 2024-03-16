# Imports
import pygame, random, time, sys


# General Code
pygame.init()
pygame.display.set_caption("FlappyRyall")
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500
font = pygame.font.SysFont('Bauhaus 93', 20)
font2 = pygame.font.SysFont('Bauhaus 93', 64)


# Variables
screen = pygame.display.set_mode((screen_width, screen_height))
score = 0
gametime = 0
birdwidth = 7
birdradius = 7
pillargap = 150
pillarwidth = 35
pillar_speed_x = 0
bird_speed_y = 0
gravity = 0
last_score_update = time.time()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (159,191,87)
BLACK = (0, 0, 0)
WHITE = (230, 230, 230)
BACKGROUND = (74, 195, 206)

def generate_pillars():
    pillarheight = random.randint(50, screen_height - pillargap - 50)
    bottompillar = pygame.Rect(screen_width, 0, pillarwidth, pillarheight)
    toppillar = pygame.Rect(screen_width, pillarheight + pillargap, pillarwidth, screen_height - pillarheight - pillargap)
    return bottompillar, toppillar

bottompillar, toppillar = generate_pillars()

birdy = pygame.image.load("bird.jfif")
bird = pygame.transform.scale(birdy, (50, 50))
bird_rect = bird.get_rect(topleft=(100, screen_height // 2))


# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Code to start the game
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        bird_speed_y = -5
        gravity = 0.5
        pillar_speed_x = -5
        current_time = time.time()
        if current_time - last_score_update >= 1:
            score += 1
            last_score_update = current_time

    bird_speed_y += gravity
    bird_rect.y += bird_speed_y

    bottompillar.x += pillar_speed_x
    toppillar.x += pillar_speed_x

    if bottompillar.right < 0:
        bottompillar, toppillar = generate_pillars()

    if bird_rect.top <= 0 or bird_rect.bottom >= screen_height:
        running = False

    if bird_rect.colliderect(bottompillar) or bird_rect.colliderect(toppillar):
        running = False

    screen.fill(BACKGROUND)

    pygame.draw.rect(screen, GREEN, toppillar)
    pygame.draw.rect(screen, GREEN, bottompillar)
    screen.blit(bird, bird_rect.topleft)

    score_text = font.render("Score: " + str(score), True, BLACK)
    start_text = font2.render("Press Space to Start", True, BLACK)
    screen.blit(score_text, (10, 10))
    if gravity == 0:
        screen.blit(start_text, (screen_width // 2 - 220, screen_height // 2 - 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
