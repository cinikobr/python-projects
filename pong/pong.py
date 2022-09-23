import pygame

# Initialise the game engine
pygame.init()

# Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball parameters
ball_x = 350
ball_y = 250
ball_radius = 5
direction_x = 0
direction_y = 0
mx = 2.5

# Paddle parameters
paddle_1_y = 225
paddle_2_y = 225
paddle_speed = 5

# Scores
score_1 = 0
score_2 = 0

pause = True

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

running = True

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 32)

# Main loop
while running:
    # Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pause:
                pause = False
                direction_x += 1
                direction_y += 1

    # Game logic
    ball_x += mx * direction_x
    ball_y += mx * direction_y

    if ball_x == 5 and paddle_1_y - ball_radius <= ball_y <= paddle_1_y + 50:
        direction_x *= -1
        ball_x = 7.5

    if ball_x == 695 and paddle_2_y - ball_radius <= ball_y <= paddle_2_y + 50:
        direction_x *= -1
        ball_x = 692.5

    if ball_x <= 0 or ball_x >= 700 - ball_radius:
        if ball_x <= 0:
            score_2 += 1
        else:
            score_1 += 1
        ball_x = 350
        ball_y = 250
        direction_x = 0
        direction_y = 0
        pause = True

    if ball_y <= 0 or ball_y >= 500 - ball_radius:
        direction_y *= -1

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and paddle_1_y < 450:
            paddle_1_y += paddle_speed
        if event.key == pygame.K_UP and paddle_1_y > 0:
            paddle_1_y -= paddle_speed

    if direction_x == 1:
        if ball_y > paddle_2_y + 25 and paddle_2_y < 450:
            paddle_2_y += paddle_speed / 2.2
        elif ball_y < paddle_2_y + 25 and paddle_2_y > 0:
            paddle_2_y -= paddle_speed / 2
    else:
        if paddle_2_y < 225:
            paddle_2_y += paddle_speed / 2.5
        if paddle_2_y > 225:
            paddle_2_y -= paddle_speed / 2.5

    # Drawing to window
    screen.fill(BLACK)

    if pause:
        text = font.render('Press space to continue', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (350, 250)

        screen.blit(text, textRect)

    # Draw scores
    text = font.render(str(score_1) + '   |   ' + str(score_2), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (350, 50)

    screen.blit(text, textRect)

    # Draw objects
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.circle(screen, WHITE, [ball_x, ball_y], ball_radius)
    pygame.draw.line(screen, WHITE, [2.5, paddle_1_y], [2.5, paddle_1_y + 50], 5)
    pygame.draw.line(screen, WHITE, [697.5, paddle_2_y], [697.5, paddle_2_y + 50], 5)

    # Update screen
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

pygame.quit()
