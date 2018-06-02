from core.entity import Entity
from core.math.vector import Vector2
from core.math.vector_factory import VectorFactory


class DefaultVectorFactory(VectorFactory, Entity):
    def vector2(self, x=0.0, y=0.0):
        return Vector2(x, y)
