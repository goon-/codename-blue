from core.glob import entity_registry
from core.graphics.entities.renderer import Renderer
from core.world_entity import WorldEntity


class DrawableEntity(WorldEntity):
    RENDERER_CLASS = Renderer

    def __init__(self, z=0, rendering_group=None, **kwargs):
        super(DrawableEntity, self).__init__(**kwargs)
        self.z = z
        self.rendering_group = rendering_group

    def draw(self, viewport):
        raise NotImplementedError()

    @property
    def renderer(self):
        return entity_registry.get_by_class(self.RENDERER_CLASS)[0]
