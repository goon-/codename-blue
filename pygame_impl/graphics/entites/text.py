from core.glob import entity_registry
from core.graphics.entities.drawable_entity import DrawableEntity
from core.graphics.entities.renderer2d import Renderer2d


class Text(DrawableEntity):
    def __init__(self, position, text='', color=(255, 255, 255), **kwargs):
        super(Text, self).__init__(**kwargs)
        self.position = position
        self.text = text
        self.color = color

    def draw(self, viewport):
        self._get_renderer().text(viewport, self.position, self.text, self.color)

    @staticmethod
    def _get_renderer():
        return entity_registry.get_by_class(Renderer2d)[0]
