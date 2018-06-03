from core.entity import Entity


class Actor(Entity):
    def think(self):
        raise NotImplementedError()
