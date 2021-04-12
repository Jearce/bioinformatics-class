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
    center=vector(300, 50), velocity=vector(-0.05, 0), radius=5, mass=0.5
)

screen = pygame.display.set_mode(size)


def collide(molecule1, molecule2):
    diff = molecule1.center - molecule2.center
    distance = (diff.x ** 2 + diff.y ** 2) ** 0.5
    return distance < (molecule1.radius + molecule1.radius)


def calculate_v1(*, m1, m2, v1, v2):
    if m1 == m2:
        return v2

    left = ((m1 - m2) / (m1 + m2)) * v1
    right = ((2 * m2) / (m1 + m2)) * v2
    return left + right


def calculate_v2(*, m1, m2, v1, v2):
    if m1 == m2:
        return v1

    left = ((2 * m1) / (m1 + m2)) * v1
    right = ((m2 - m1) / (m1 + m2)) * v2
    return left + right


def calculate_velocities(molecule1, molecule2):
    v1 = calculate_v1(
        m1=molecule1.mass,
        m2=molecule2.mass,
        v1=molecule1.velocity,
        v2=molecule2.velocity,
    )
    v2 = calculate_v2(
        m1=molecule1.mass,
        m2=molecule2.mass,
        v1=molecule1.velocity,
        v2=molecule2.velocity,
    )
    return v1, v2


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if collide(molecule1, molecule2):
        v1, v2 = calculate_velocities(molecule1, molecule2)
        molecule1.velocity = vector(v1, molecule1.velocity.y)
        molecule2.velocity = vector(v2, molecule2.velocity.y)

    molecule1.draw(screen)
    molecule1.update(screen)

    molecule2.draw(screen)
    molecule2.update(screen)

    pygame.display.flip()
