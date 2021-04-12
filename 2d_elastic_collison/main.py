import pygame
import sys

import physics

from molecule import Molecule

pygame.init()

vector = pygame.math.Vector2

size = width, height = 320, 240
black = 0, 0, 0

molecules = [
    Molecule(center=vector(10, 10), velocity=vector(0.05, 0.05), mass=5),
    Molecule(center=vector(300, 20), velocity=vector(-0.05, 0.05), mass=7),
    Molecule(center=vector(51, 220), velocity=vector(0.05, -0.05), mass=12),
    Molecule(center=vector(300, 220), velocity=vector(-0.05, -0.05), mass=8),
]

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    for molecule1 in molecules:
        for molecule2 in molecules:
            if molecule1 is not molecule2 and physics.collide(
                molecule1, molecule2
            ):
                v1, v2 = physics.calculate_velocities(molecule1, molecule2)
                molecule1.velocity = v1
                molecule2.velocity = v2

        molecule1.draw(screen)
        molecule1.update(screen)

    pygame.display.flip()
