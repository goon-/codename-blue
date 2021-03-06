import logging

from enum import Enum

from core.glob import get_vec_fact
from core.world_entity import WorldEntity

logger = logging.getLogger(__name__)


class Vertex(Enum):
    RIGHT_BOTTOM = 0
    RIGHT_TOP = 1
    LEFT_TOP = 2
    LEFT_BOTTOM = 3


class Edge(Enum):
    RIGHT = 1
    TOP = 2
    LEFT = -1
    BOTTOM = -2


class PhysicEntity(WorldEntity):
    def __init__(self, size=None, collision_category=None, **kwargs):
        super(PhysicEntity, self).__init__(**kwargs)
        self.size = size or get_vec_fact().vector2()
        self.collision_category = collision_category
        self.collision = None

    def vertices(self):
        return (
            self.position + get_vec_fact().vector2(self.size.x, 0),
            self.position + self.size,
            self.position + get_vec_fact().vector2(0, self.size.y),
            self.position,
        )

    def edges(self):
        vertices = self.vertices()
        return {
            Edge.RIGHT: (vertices[0], vertices[1]),
            Edge.TOP: (vertices[1], vertices[2]),
            Edge.LEFT: (vertices[2], vertices[3]),
            Edge.BOTTOM: (vertices[3], vertices[0]),
        }

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
