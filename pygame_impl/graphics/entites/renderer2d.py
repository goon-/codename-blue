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
        screen_rect = self._world_to_screen_r(viewport, rect)
        pygame.draw.rect(
            viewport.surface,
            color,
            (
                screen_rect[0],
                screen_rect[1],
                screen_rect[2] - screen_rect[0],
                screen_rect[3] - screen_rect[1],
            ),
            0,
        )

    def text(self, viewport, position, text, color, font=None):
        font = font or self._default_font
        label = font.render(text, 1, color)
        viewport.surface.blit(label, self._world_to_screen_p(viewport, (position.x, position.y)))

    def fill_polygon(self, viewport, color, pointlist):
        pygame.draw.polygon(viewport.surface, color, map(lambda x: self._world_to_screen_p(viewport, x), pointlist))

    def line(self, viewport, start, end, color):
        pygame.draw.line(viewport.surface, color, self._world_to_screen_p(viewport, start), self._world_to_screen_p(viewport, end))

    def _invert_y_p(self, viewport, point):
        return point[0], viewport.surface.get_height() - point[1]

    def _world_to_screen_p(self, viewport, point):
        return self._invert_y_p(viewport, viewport.world_to_screen_p(point))

    def _world_to_screen_r(self, viewport, rect):
        point1 = self._world_to_screen_p(viewport, (rect[0], rect[1]))
        point2 = self._world_to_screen_p(viewport, (rect[2], rect[3]))
        return point1[0], point1[1], point2[0], point2[1]
