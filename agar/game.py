import pygame
import random

from agar.square import Square

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
size = (1000, 600)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("Agar")

squares = []

player = Square(1, 50, 50, 50)
squares.append(player)

for i in range(50):
    square = Square(i + 2, 10, random.randint(0, 1000), random.randint(0, 600))
    squares.append(square)

running = True

clock = pygame.time.Clock()

while running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player.set_sx(player.get_sx() - 5)
        if event.key == pygame.K_RIGHT:
            player.set_sx(player.get_sx() + 5)
        if event.key == pygame.K_UP:
            player.set_sy(player.get_sy() - 5)
        if event.key == pygame.K_DOWN:
            player.set_sy(player.get_sy() + 5)

    surface.fill(WHITE)

    for square in squares:
        pygame.draw.rect(surface,
                         BLACK,
                         pygame.Rect(square.get_sx(),
                                     square.get_sy(),
                                     square.get_radius(),
                                     square.get_radius()
                                     )
                         )

        pygame.display.flip()

        clock.tick(60)


pygame.quit()
