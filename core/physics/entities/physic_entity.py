import logging

from enum import Enum

from core.vector import Vector
from core.world_entity import WorldEntity

logger = logging.getLogger(__name__)


class Vertex(Enum):
    RIGHT_BOTTOM = 0
    RIGHT_TOP = 1
    LEFT_TOP = 2
    LEFT_BOTTOM = 3


class Edge(Enum):
    RIGHT = 0
    TOP = 1
    LEFT = 2
    BOTTOM = 3


class PhysicEntity(WorldEntity):
    def __init__(self, size=None, **kwargs):
        super(PhysicEntity, self).__init__(**kwargs)
        self.size = size or Vector()
        self.collision = None

    def vertices(self):
        return (
            self.position + Vector(self.size.x, 0),
            self.position + self.size,
            self.position + Vector(0, self.size.y),
            self.position,
        )

    def edges(self):
        vertices = self.vertices()
        return (
            (vertices[0], vertices[1]),
            (vertices[1], vertices[2]),
            (vertices[2], vertices[3]),
            (vertices[3], vertices[0]),
        )

    def collides(self, other):
        return \
            self._projections_collide(
                self.position.x, self.position.x + self.size.x, other.position.x, other.position.x + other.size.x
            ) and \
            self._projections_collide(
                self.position.y, self.position.y + self.size.y, other.position.y, other.position.y + other.size.y
            )

    def _projections_collide(self, c11, c12, c21, c22):
        return not (c12 <= c21 or c11 >= c22)

    def _is_inside(self, point):
        return self.position.x <= point.x <= self.position.x + self.size.x and \
               self.position.y <= point.y <= self.position.y + self.size.y
