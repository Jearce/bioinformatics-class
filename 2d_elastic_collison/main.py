import pygame
import sys

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)

center = pygame.math.Vector2((50, 50))
radius = 5

speed = pygame.math.Vector2((0.10, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    center += speed

    if not (radius < center.x < (width - radius)):
        speed.x = -speed.x

    if not (radius < center.y < (height - radius)):
        speed.y = -speed.y

    molecule = pygame.draw.circle(
        screen, color="white", center=center, radius=5
    )
    pygame.display.flip()
