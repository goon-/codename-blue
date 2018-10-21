import pygame

from core.glob import get_vec_fact, entity_registry
from core.graphics.entities.screen import Screen
from core.input.devices.mouse import Mouse, MBUTTONS


class PygameMouse(Mouse):
    def __init__(self):
        super(PygameMouse, self).__init__()
        self._button_indexes = {
            MBUTTONS.lmb: 0,
            MBUTTONS.mmb: 1,
            MBUTTONS.rmb: 2
        }
        self._screen = None

    def is_pressed(self, key):
        if key not in self._button_indexes:
            return False

        button_index = self._button_indexes[key]
        return pygame.mouse.get_pressed()[button_index]

    def get_screen_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        screen = self._get_screen()
        return mouse_pos[0], screen.res_y - mouse_pos[1]

    def _get_screen(self):
        if not self._screen:
            self._screen = entity_registry.get_by_class(Screen)[0]

        return self._screen
