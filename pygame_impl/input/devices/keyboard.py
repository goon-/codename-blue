import pygame
from pygame import constants

from core.input.devices.input_device import InputDevice
from core.input.devices.keyboard import KEYS


class PygameKeyboard(InputDevice):
    KEYMAP = {
        KEYS.w: constants.K_w,
        KEYS.a: constants.K_a,
        KEYS.s: constants.K_s,
        KEYS.d: constants.K_d,
    }

    def is_pressed(self, key):
        if key not in self.KEYMAP:
            return False

        return pygame.key.get_pressed()[self.KEYMAP[key]]
