import logging

import pygame

from core.glob import get_vec_fact
from core.graphics.entities.drawable_entity import DrawableEntity

logger = logging.getLogger(__name__)


class Placeholder(DrawableEntity):
    def __init__(self, placeholder_size=None, color=(255, 255, 255), **kwargs):
        super(Placeholder, self).__init__(**kwargs)
        self._placeholder_size = placeholder_size or get_vec_fact().vector2()
        self._color = color

    def draw(self, viewport):
        rect = viewport.transform_r((
            self.position.x,
            self.position.y,
            self.position.x + self._placeholder_size.x,
            self.position.y + self._placeholder_size.y,
        ))
        pygame.draw.rect(
            viewport.surface,
            self._color,
            (
                rect[0],
                viewport.surface.get_height() - rect[1],
                rect[2] - rect[0],
                -(rect[3] - rect[1]),
            ),
            0,
        )
        # logger.debug('Placeholder.draw(): %s, %s, %s, %s' % (
        #     rect[0],
        #     viewport.surface.get_height() - rect[1],
        #     rect[2] - rect[0],
        #     -(rect[3] - rect[1]),
        # ))
