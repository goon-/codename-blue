import math

from core.glob import get_vec_fact


class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return get_vec_fact().vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        scalar = float(scalar)
        return get_vec_fact().vector2(self.x * scalar, self.y * scalar)

    def __sub__(self, other):
        return get_vec_fact().vector2(self.x - other.x, self.y - other.y)

    def __div__(self, scalar):
        return get_vec_fact().vector2(self.x / scalar, self.y / scalar)

    def __nonzero__(self):
        return self.x != 0 or self.y != 0

    def __repr__(self):
        return 'Vector2(%s, %s)' % (self.x, self.y)

    def len(self):
        return math.sqrt(self.x**2 + self.y**2)

    def zero(self):
        self.x = 0
        self.y = 0

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y

    def multiply_v(self, other):
        self.x *= other.x
        self.y *= other.y

    def normalize(self, norm=1.0):
        norm = float(norm)
        mul = norm / self.len()
        self.x *= mul
        self.y *= mul

    def normalized(self, norm=1.0):
        normalized_vector = get_vec_fact().vector2(self.x, self.y)
        normalized_vector.normalize(norm)
        return normalized_vector

    def copy(self):
        return get_vec_fact().vector2(self.x, self.y)

    def rotated(self, angle):
        return get_vec_fact().vector2(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle),
        )

    def rotated_around(self, angle, center):
        centered = self - center
        return centered.rotated(angle) + center

    def point(self):
        return self.x, self.y
