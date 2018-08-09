import pygame

from core.graphics.entities.screen import Screen as CoreScreen


class Screen(CoreScreen):
    def __init__(self):
        super(Screen, self).__init__()
        self.screen = None
        self.res_x = 0
        self.res_y = 0

    def set_resolution(self, res_x, res_y):
        self.res_x = res_x
        self.res_y = res_y
        self.screen = pygame.display.set_mode((res_x, res_y))
