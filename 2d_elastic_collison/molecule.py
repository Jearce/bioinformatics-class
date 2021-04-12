import pygame
from pygame.math import Vector2


def postion_time(s_o: Vector2, v_o: Vector2, a: Vector2):
    return s_o + v_o + (0.5 * Vector2(a.x ** 2, a.y ** 2))


class Molecule:
    def __init__(
        self,
        *,
        center: Vector2,
        velocity: Vector2,
        mass: float,
    ):
        self.center = center
        self.color = "white"
        self.mass = mass
        self.velocity = velocity

        self.acceleration = Vector2((0.01, 0.01))
        self.radius = self.mass * 1.25

    def draw(self, screen: pygame.Surface):
        return pygame.draw.circle(
            screen, color=self.color, center=self.center, radius=self.radius
        )

    def update(self, screen: pygame.Surface):
        self.center = postion_time(
            self.center, self.velocity, self.acceleration
        )

        if not (
            self.radius < self.center.x < (screen.get_width() - self.radius)
        ):
            self.velocity.x = -self.velocity.x

        if not (
            self.radius < self.center.y < (screen.get_height() - self.radius)
        ):
            self.velocity.y = -self.velocity.y

        molecule = self.draw(screen)
