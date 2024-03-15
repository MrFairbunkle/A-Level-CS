import pygame, random, time, sys

pygame.init()
pygame.display.set_caption("FlappyBird")
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500
font = pygame.font.SysFont('Bauhaus 93', 20)

screen = pygame.display.set_mode((screen_width, screen_height))
score = 0
gametime = 0
birdwidth = 7
birdradius = 7
pillargap = 200
pillarwidth = 35
pillar_speed_x = -5
bird_speed_y = 0
gravity = 0.5
last_score_update = time.time()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (53, 129, 34)
BLACK = (0, 0, 0)
WHITE = (230, 230, 230)

def generate_pillars():
    pillarheight = random.randint(50, screen_height - pillargap - 50)
    bottompillar = pygame.Rect(screen_width, 0, pillarwidth, pillarheight)
    toppillar = pygame.Rect(screen_width, pillarheight + pillargap, pillarwidth, screen_height - pillarheight - pillargap)
    return bottompillar, toppillar

bottompillar, toppillar = generate_pillars()

birdy = pygame.image.load("bird.jfif")
bird = pygame.transform.scale(birdy, (50, 50))
bird_rect = bird.get_rect(topleft=(100, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        bird_speed_y = -7

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

    current_time = time.time()
    if current_time - last_score_update >= 1:
        score += 1
        last_score_update = current_time

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, toppillar)
    pygame.draw.rect(screen, GREEN, bottompillar)
    screen.blit(bird, bird_rect.topleft)

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()
