import math


class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        scalar = float(scalar)
        return Vector(self.x * scalar, self.y * scalar)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __nonzero__(self):
        return self.x != 0 or self.y != 0

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)

    def len(self):
        return math.sqrt(self.x**2 + self.y**2)

    def zero(self):
        self.x = 0
        self.y = 0

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def multiply(self, scalar):
        scalar = float(scalar)
        self.x *= scalar
        self.y *= scalar

    def multiply_v(self, vector):
        self.x *= vector.x
        self.y *= vector.y

    def normalize(self, norm=1.0):
        norm = float(norm)
        mul = norm / self.len()
        self.x *= mul
        self.y *= mul
