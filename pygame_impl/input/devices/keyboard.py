import pygame
from pygame import constants

from core.input.devices.keyboard import KEYS, Keyboard


class PygameKeyboard(Keyboard):
    KEYMAP = {
        KEYS.w: constants.K_w,
        KEYS.a: constants.K_a,
        KEYS.s: constants.K_s,
        KEYS.d: constants.K_d,
        KEYS.space: constants.K_SPACE,
    }

    def is_pressed(self, key):
        if key not in self.KEYMAP:
            return False

        return pygame.key.get_pressed()[self.KEYMAP[key]]
