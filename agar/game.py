import pygame
import random

from square import Square


def draw_sqr(square):
    pygame.draw.rect(surface,
                     BLACK,
                     pygame.Rect(square.get_sx(),
                                 square.get_sy(),
                                 square.get_radius(),
                                 square.get_radius()
                                 )
                     )


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
size = (1000, 600)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("Agar")

squares = []

player = Square(1, 50, 50, 50)

for i in range(100):
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
        if event.key == pygame.K_SPACE:
            print(3)

    surface.fill(WHITE)

    for square in squares:
        if (player.get_sx() <= square.get_sx() <= player.get_sx() + player.get_radius() - square.get_radius()
                and player.get_sy() <= square.get_sy() <= player.get_sy() + player.get_radius() - square.get_radius()):
            player.set_radius(player.get_radius() + square.get_radius())
            squares.remove(square)

    draw_sqr(player)

    for square in squares:
        draw_sqr(square)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
