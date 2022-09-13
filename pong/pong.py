# Import the pygame library and initialise the game engine
import pygame, sys
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)



# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

bx = 350
by = 250
br = 5
dx = 0
dy = 0
mx = 2.5

p1y = 225
pm = 5
p2y = 225

score1 = 0
score2 = 0

pause = True

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and pause:
                pause = False
                dx += 1
                dy += 1

    # --- Game logic should go here
    bx += mx * dx
    by += mx * dy

    if bx == 5 and p1y - br <= by <= p1y + 50:
        dx *= -1
        bx = 7.5

    if bx == 695 and p2y - br <= by <= p2y + 50:
        dx *= -1
        bx = 692.5

    if bx <= 0 or bx >= 700 - br:
        if bx <= 0:
            score2 += 1
        else:
            score1 += 1
        bx = 350
        by = 250
        dx = 0
        dy = 0
        pause = True
        print("score: " + str(score1) + "  ||  " + str(score2) + "\n Press "
                                                                 "space bar "
                                                                 "to "
                                                                 "continue.")

    if by <= 0 or by >= 500 - br:c
        dy *= -1

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN and p1y < 450:
            p1y += pm
        if event.key == pygame.K_UP and p1y > 0:
            p1y -= pm

    if dx == 1:
        if by > p2y + 25 and p2y < 450:
            p2y += pm/2
        if by < p2y + 25 and p2y > 0:
            p2y -= pm/2

    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.circle(screen, WHITE, [bx, by], br)
    pygame.draw.line(screen, WHITE, [2.5, p1y], [2.5, p1y + 50], 5)
    pygame.draw.line(screen, WHITE, [697.5, p2y], [697.5, p2y + 50], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
