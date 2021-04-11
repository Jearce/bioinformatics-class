import pygame
from pygame.math import Vector2


class Molecule:
    def __init__(
        self,
        *,
        center: Vector2,
        speed: Vector2,
        radius: int,
        mass: float,
    ):
        self.center = center
        self.color = "white"
        self.radius = radius
        self.mass = mass
        self.speed = speed

    def draw(self, screen: pygame.Surface):
        return pygame.draw.circle(
            screen, color=self.color, center=self.center, radius=self.radius
        )

    def update(self, screen: pygame.Surface):
        self.center += self.speed

        if not (
            self.radius < self.center.x < (screen.get_width() - self.radius)
        ):
            self.speed.x = -self.speed.x

        if not (
            self.radius < self.center.y < (screen.get_height() - self.radius)
        ):
            self.speed.y = -self.speed.y

        molecule = self.draw(screen)
