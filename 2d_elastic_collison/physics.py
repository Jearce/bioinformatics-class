from pygame.math import Vector2

from molecule import Molecule


def collide(molecule1, molecule2) -> bool:
    diff = molecule1.center - molecule2.center
    distance = (diff.x ** 2 + diff.y ** 2) ** 0.5
    return distance < (molecule1.radius + molecule2.radius)


def compute_collision_velocity(*, molecule1, molecule2) -> Vector2:
    masses = (2 * molecule2.mass) / (molecule1.mass + molecule2.mass)
    velocity_diff: Vector2 = molecule1.velocity - molecule2.velocity
    position_diff: Vector2 = molecule1.center - molecule2.center
    dot_product: Vector2 = velocity_diff * position_diff
    magnitude_squared: Vector2 = position_diff.magnitude_squared()
    return (
        molecule1.velocity
        - masses * (dot_product / magnitude_squared) * position_diff
    )


def calculate_v(*, molecule1: Molecule, molecule2: Molecule) -> Vector2:
    if molecule1.mass == molecule2.mass:
        return molecule2.velocity

    return compute_collision_velocity(molecule1=molecule1, molecule2=molecule2)


def calculate_velocities(molecule1, molecule2):
    v1 = calculate_v(molecule1=molecule1, molecule2=molecule2)
    v2 = calculate_v(molecule1=molecule2, molecule2=molecule1)
    return v1, v2
