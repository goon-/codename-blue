from core.world_entity import WorldEntity


class DrawableEntity(WorldEntity):
    def __init__(self, z=0, rendering_group=None, **kwargs):
        super(DrawableEntity, self).__init__(**kwargs)
        self.z = z
        self.rendering_group = rendering_group

    def draw(self, viewport):
        raise NotImplementedError()
