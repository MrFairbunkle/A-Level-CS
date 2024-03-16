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
highscore = 0
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

# Function to generate pillars
def generate_pillars():
    pillarheight = random.randint(50, screen_height - pillargap - 50)
    bottompillar = pygame.Rect(screen_width, 0, pillarwidth, pillarheight)
    toppillar = pygame.Rect(screen_width, pillarheight + pillargap, pillarwidth, screen_height - pillarheight - pillargap)
    return bottompillar, toppillar

# Initial pillars
active_pillars = [generate_pillars()]

birdy = pygame.image.load("bird.jfif")
bird = pygame.transform.scale(birdy, (50, 50))
bird_rect = bird.get_rect(topleft=(100, screen_height // 2))

# Reset function
def reset_game():
    global bird_rect, active_pillars, score, bird_speed_y, gravity, pillar_speed_x
    bird_rect = bird.get_rect(topleft=(100, screen_height // 2))
    active_pillars = [generate_pillars()]
    score = 0
    bird_speed_y = 0
    gravity = 0
    pillar_speed_x = 0

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)  # Fill the screen with the background color

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

    # Move and draw pillars
    for i, (bottompillar, toppillar) in enumerate(active_pillars):
        bottompillar.x += pillar_speed_x
        toppillar.x += pillar_speed_x
        pygame.draw.rect(screen, GREEN, toppillar)
        pygame.draw.rect(screen, GREEN, bottompillar)

        # Remove pillars that have moved off-screen
        if bottompillar.right < 0:
            active_pillars.pop(i)
            active_pillars.append(generate_pillars())

        # Collision detection
        if bird_rect.colliderect(bottompillar) or bird_rect.colliderect(toppillar):
            bird_speed_y = 0
            gravity = 0
            pillar_speed_x = 0
            highscore = max(highscore, score)
            time.sleep(3)
            reset_game()

    # Check for bird collision with screen boundaries
    if bird_rect.top <= 0 or bird_rect.bottom >= screen_height:
        bird_speed_y = 0
        gravity = 0
        pillar_speed_x = 0
        highscore = max(highscore, score)
        time.sleep(3)
        reset_game()

    screen.blit(bird, bird_rect.topleft)

    score_text = font.render("Score: " + str(score), True, BLACK)
    start_text = font2.render("Press Space to Start", True, BLACK)
    highscore_text = font.render("Highscore: " + str(highscore), True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(highscore_text, (80, 10))
    if gravity == 0:
        screen.blit(start_text, (screen_width // 2 - 220, screen_height // 2 - 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()