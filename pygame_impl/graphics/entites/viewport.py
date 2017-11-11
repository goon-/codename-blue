import logging

from core.glob import entity_registry
from core.graphics.entities.viewport import Viewport
from pygame_impl.graphics.entites.screen import Screen

logger = logging.getLogger(__name__)


class PygameViewport(Viewport):
    def __init__(self, rect, screen_rect):
        super(PygameViewport, self).__init__(rect, screen_rect)
        screen = entity_registry.get_by_class(Screen)[0].screen
        logger.debug('PygameViewport surface: %s, %s, %s, %s' % (
            screen_rect[0],
            screen.get_height() - screen_rect[1] - screen_rect[3],
            screen_rect[2],
            screen_rect[3],
        ))
        self.surface = screen.subsurface((
            screen_rect[0],
            screen.get_height() - screen_rect[1] - screen_rect[3],
            screen_rect[2],
            screen_rect[3],
        ))
