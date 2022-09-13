# Import the pygame library and initialise the game engine
import pygame
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
bx = 100
by = 100
br = 5
dx = 1
dy = 1
mx = 2

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

    # --- Game logic should go here
    bx += mx * dx
    by += mx * dx

    if bx <= 0 or bx >= 700 - br:
        dx *= -1

    if by <= 0 or by >= 200 - br:
        dy *= -1


    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.circle(screen, WHITE, [bx, by], br)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
