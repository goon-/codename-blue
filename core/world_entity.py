from core.entity import Entity
from core.vector import Vector


class WorldEntity(Entity):
    def __init__(self, position=None):
        super(WorldEntity, self).__init__()
        self.position = position or Vector()
