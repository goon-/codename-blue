import pygame

from core.graphics.entities.drawable_entity import DrawableEntity


class Text(DrawableEntity):
    def __init__(self, x, y, **kwargs):
        super(Text, self).__init__(**kwargs)
        self._x = x
        self._y = y
        self._font = pygame.font.SysFont("monospace", 10)
        self._text = ''

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def draw(self, viewport):
        label = self._font.render(self._text, 1, (255, 255, 255))
        viewport.surface.blit(label, (self._x, self._y))
