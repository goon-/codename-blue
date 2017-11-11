from core.vector import Vector
from core.world_entity import WorldEntity


class PhysicEntity(WorldEntity):
    def __init__(self, size=None, **kwargs):
        super(PhysicEntity, self).__init__(**kwargs)
        self.size = size or Vector()

    def collides(self, other):
        return self._is_inside(other.position) or \
               self._is_inside(Vector(other.position.x + other.size.x, other.position.y)) or \
               self._is_inside(Vector(other.position.x, other.position.y + other.size.y)) or \
               self._is_inside(other.position + other.size)

    def _is_inside(self, point):
        return self.position.x <= point.x <= self.position.x + self.size.x and \
               self.position.y <= point.y <= self.position.y + self.size.y
