import pygame
import sys

from molecule import Molecule

pygame.init()

vector = pygame.math.Vector2

size = width, height = 320, 240
black = 0, 0, 0

molecule1 = Molecule(
    center=vector(50, 50), velocity=vector(0.05, 0), radius=5, mass=0.2
)

molecule2 = Molecule(
    center=vector(300, 50), velocity=vector(-0.05, 0), radius=5, mass=0.2
)

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    molecule1.draw(screen)
    molecule1.update(screen)

    molecule2.draw(screen)
    molecule2.update(screen)

    pygame.display.flip()
