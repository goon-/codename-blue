import pygame

from core.glob import entity_registry
from core.graphics.entities.renderer2d import Renderer2d
from core.graphics.entities.viewport import Viewport
from pygame_impl.graphics.entites.screen import Screen


class PygameRenderer2d(Renderer2d):
    def __init__(self):
        super(PygameRenderer2d, self).__init__(20)
        self._screen = entity_registry.get_by_class(Screen)[0].screen
        self.surface = entity_registry.get_by_class(Viewport)[0].surface

    def clear_screen(self):
        self._screen.fill((0, 0, 0, 0))

    def render(self):
        super(PygameRenderer2d, self).render()
        # pygame.draw.line(self.surface, (255, 255, 255), (0, 0), (385, 385), 3)
        # pygame.draw.rect(self.surface, [255, 255, 255], [0, 300, 10, 10], 2)
        pygame.display.flip()
