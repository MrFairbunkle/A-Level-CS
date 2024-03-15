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
pillarsize = 25
bottompillar = pygame.Rect(600, 0, pillarsize, pillarsize * 6)
toppillar = pygame.Rect(800, 350, pillarsize, pillarsize * 6)
bird = pygame.Rect(screen_width // 2, screen_height // 2, birdwidth, birdradius)
bird_speed_x = 0 
bird_speed_y = 0 
gravity = 0.5 
last_score_update = time.time()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (230, 230, 230)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        bird_speed_x = 5
        bird_speed_y = -10

    # Apply gravity
    bird_speed_y += gravity

    # Update bird position
    bird.x += bird_speed_x
    bird.y += bird_speed_y

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
    pygame.draw.rect(screen, RED, toppillar)
    pygame.draw.rect(screen, BLUE, bottompillar)
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
