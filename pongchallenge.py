# Imports
import pygame
import sys

pygame.init()

# General code
pygame.display.set_caption("BadPong")
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 500
font = pygame.font.SysFont('Bauhaus 93', 20)

# Variables
screen = pygame.display.set_mode((screen_width, screen_height))
redscore = 0
bluescore = 0
gametime = 0
redsize = 15
bluesize = 15
ballwidth = 7
ballradius = 7
redsquare = pygame.Rect(920, 200, redsize, redsize * 6)
bluesquare = pygame.Rect(80, 200, bluesize, bluesize * 6)
ball = pygame.Rect(screen_width // 2, screen_height // 2, ballwidth, ballradius)
ball_speed_x = 0 
ball_speed_y = 0 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if score = 11
    if redscore == 11 or bluescore == 11:
        running = False
        pygame.quit()

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        ball_speed_x = 5
        ball_speed_y = 5

    if key[pygame.K_w]:
        if bluesquare.y - 5 >= 0:
            bluesquare.y -= 5
    if key[pygame.K_s]:
        if bluesquare.y + 5 <= screen_height - 80:
            bluesquare.y += 5
    if key[pygame.K_UP]:
        if redsquare.y - 5 >= 0:
            redsquare.y -= 5
    if key[pygame.K_DOWN]:
        if redsquare.y + 5 <= screen_height - 80:
            redsquare.y += 5

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions with walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball.left <= 0:
        redscore += 1
        print(f"redscore={redscore}")
        ball.left = screen_width // 2
        ball.top = screen_height // 2
        ball_speed_x = 0
        ball_speed_y = 0
    if ball.right >= screen_width:
        bluescore += 1
        print(f"bluescore={bluescore}")
        ball.left = screen_width // 2
        ball.top = screen_height // 2
        ball_speed_x = 0
        ball_speed_y = 0

    # Check for collisions with paddles
    if ball.colliderect(bluesquare) or ball.colliderect(redsquare):
        ball_speed_x = -ball_speed_x
        ball_speed_x *= 1.1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw objects
    pygame.draw.rect(screen, RED, redsquare)
    pygame.draw.rect(screen, BLUE, bluesquare)
    pygame.draw.circle(screen, BLACK, (ball.x, ball.y), ballwidth, ballradius)

    # Render text surfaces for red and blue scores
    red_score_text = font.render("Red Score: " + str(redscore), True, BLACK)
    blue_score_text = font.render("Blue Score: " + str(bluescore), True, BLACK)

    # Blit the text surfaces onto the screen
    screen.blit(red_score_text, (10, 10))
    screen.blit(blue_score_text, (screen_width - blue_score_text.get_width() - 10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
