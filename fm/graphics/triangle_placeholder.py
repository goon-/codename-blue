import logging

from core.glob import get_vec_fact
from core.graphics.entities.drawable_entity import DrawableEntity

logger = logging.getLogger(__name__)


class TrianglePlaceholder(DrawableEntity):
    def __init__(self, placeholder_size=None, color=(255, 255, 255), **kwargs):
        super(TrianglePlaceholder, self).__init__(**kwargs)
        self.placeholder_size = placeholder_size or get_vec_fact().vector2()
        self.color = color

    def draw(self, viewport):
        center = self.position + (self.placeholder_size / 2)
        self.renderer.fill_polygon(
            viewport=viewport,
            color=self.color,
            pointlist=(
                self.position.rotated_around(self.rotation, center).point(),
                # (self.position + get_vec_fact().vector2(self.placeholder_size.x, 0.0)).rotated_around(self.rotation, center).point(),
                (self.position + get_vec_fact().vector2(self.placeholder_size.x, self.placeholder_size.y / 2.0)).rotated_around(self.rotation, center).point(),
                (self.position + get_vec_fact().vector2(0.0, self.placeholder_size.y)).rotated_around(self.rotation, center).point(),
            ),
        )
