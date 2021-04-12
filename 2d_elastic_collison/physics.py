def collide(molecule1, molecule2):
    diff = molecule1.center - molecule2.center
    distance = (diff.x ** 2 + diff.y ** 2) ** 0.5
    return distance < (molecule1.radius + molecule2.radius)


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
