import pygame
import sys

import physics

from molecule import Molecule

pygame.init()

vector = pygame.math.Vector2

size = width, height = 320, 240
black = 0, 0, 0

molecule1 = Molecule(
    center=vector(50, 50), velocity=vector(0.05, 0), radius=20, mass=0.2
)

molecule2 = Molecule(
    center=vector(300, 50), velocity=vector(-0.05, 0), radius=5, mass=0.5
)

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if physics.collide(molecule1, molecule2):
        v1, v2 = physics.calculate_velocities(molecule1, molecule2)
        molecule1.velocity = vector(v1, molecule1.velocity.y)
        molecule2.velocity = vector(v2, molecule2.velocity.y)

    molecule1.draw(screen)
    molecule1.update(screen)

    molecule2.draw(screen)
    molecule2.update(screen)

    pygame.display.flip()
