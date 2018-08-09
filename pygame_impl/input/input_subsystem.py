import logging

import pygame

from core.glob import entity_registry
from core.subsystem import Subsystem
from pygame_impl.input.devices.keyboard import PygameKeyboard

logger = logging.getLogger(__name__)


class PygameInputSubsystem(Subsystem):
    def initialize(self):
        logger.debug('Initializing pygame user input')
        pygame.joystick.init()
        already_registered = len(entity_registry.get_by_class(PygameKeyboard)) > 0
        if not already_registered:
            entity_registry.add(PygameKeyboard())
