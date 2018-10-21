import logging

import pygame

from core.glob import entity_registry
from core.subsystem import Subsystem
from pygame_impl.input.devices.keyboard import PygameKeyboard
from pygame_impl.input.devices.mouse import PygameMouse

logger = logging.getLogger(__name__)


class PygameInputSubsystem(Subsystem):
    def initialize(self):
        logger.debug('Initializing pygame user input')
        pygame.joystick.init()
        self.register_keyboard()
        self.register_mouse()

    def register_keyboard(self):
        already_registered = len(entity_registry.get_by_class(PygameKeyboard)) > 0
        if not already_registered:
            entity_registry.add(PygameKeyboard())

    def register_mouse(self):
        already_registered = len(entity_registry.get_by_class(PygameMouse)) > 0
        if not already_registered:
            entity_registry.add(PygameMouse())
