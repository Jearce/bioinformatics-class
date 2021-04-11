import pygame
import sys

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)

center = pygame.math.Vector2((50, 50))

speed = pygame.math.Vector2((0.10, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    center += speed
    molecule = pygame.draw.circle(
        screen, color="white", center=center, radius=5
    )
    pygame.display.flip()
