import logging

from core.glob import get_vec_fact, entity_registry
from core.graphics.entities.drawable_entity import DrawableEntity
from core.graphics.entities.renderer2d import Renderer2d

logger = logging.getLogger(__name__)


class Placeholder(DrawableEntity):
    def __init__(self, placeholder_size=None, color=(255, 255, 255), **kwargs):
        super(Placeholder, self).__init__(**kwargs)
        self.placeholder_size = placeholder_size or get_vec_fact().vector2()
        self.color = color

    def draw(self, viewport):
        self._get_renderer().fill_rect(
            viewport=viewport,
            rect=(
                self.position.x,
                self.position.y,
                self.position.x + self.placeholder_size.x,
                self.position.y + self.placeholder_size.y,
            ),
            color=self.color
        )

    @staticmethod
    def _get_renderer():
        return entity_registry.get_by_class(Renderer2d)[0]
