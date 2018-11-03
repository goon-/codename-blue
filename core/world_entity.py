from core.entity import Entity
from core.glob import get_vec_fact


class WorldEntity(Entity):
    def __init__(self, position=None):
        super(WorldEntity, self).__init__()
        self.position = position or get_vec_fact().vector2()
        self.rotation = 0
