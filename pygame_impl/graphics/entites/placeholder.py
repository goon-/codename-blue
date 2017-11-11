import logging

import pygame

from core.graphics.entities.drawable_entity import DrawableEntity
from core.vector import Vector

logger = logging.getLogger(__name__)


class Placeholder(DrawableEntity):
    def __init__(self, placeholder_size=None, color=(255, 255, 255), **kwargs):
        super(Placeholder, self).__init__(**kwargs)
        self._placeholder_size = placeholder_size or Vector()
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
            1,
        )
        # logger.debug('Placeholder.draw(): %s, %s, %s, %s' % (
        #     rect[0],
        #     viewport.surface.get_height() - rect[1],
        #     rect[2] - rect[0],
        #     -(rect[3] - rect[1]),
        # ))
