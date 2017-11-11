from core.world_entity import WorldEntity


class DrawableEntity(WorldEntity):
    def __init__(self, z=0, **kwargs):
        super(DrawableEntity, self).__init__(**kwargs)
        self.z = z

    def draw(self, viewport):
        raise NotImplementedError()
