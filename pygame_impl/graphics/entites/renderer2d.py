import pygame

from core.glob import entity_registry
from core.graphics.entities.renderer2d import Renderer2d
from pygame_impl.graphics.entites.screen import Screen
from pygame_impl.graphics.entites.viewport import PygameViewport


class PygameRenderer2d(Renderer2d):
    def __init__(self):
        super(PygameRenderer2d, self).__init__()
        self._default_font = pygame.font.SysFont("monospace", 10)

    def clear_screen(self):
        screen = entity_registry.get_by_class(Screen)[0].screen
        screen.fill((0, 0, 0, 0))

    def render(self):
        super(PygameRenderer2d, self).render()
        pygame.display.flip()

    def create_viewport(self, world_rect, screen_rect):
        return PygameViewport(world_rect, screen_rect)

    def fill_rect(self, viewport, rect, color):
        rect = viewport.transform_r(rect)
        pygame.draw.rect(
            viewport.surface,
            color,
            (
                rect[0],
                viewport.surface.get_height() - rect[1],
                rect[2] - rect[0],
                -(rect[3] - rect[1]),
            ),
            0,
        )

    def text(self, viewport, position, text, color, font=None):
        font = font or self._default_font
        label = font.render(text, 1, color)
        viewport.surface.blit(label, (position.x, position.y))
