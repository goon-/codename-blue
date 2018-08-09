import logging

import pygame

from core.glob import entity_registry
from core.subsystem import Subsystem
from pygame_impl.graphics.entites.renderer2d import PygameRenderer2d
from pygame_impl.graphics.entites.screen import Screen

logger = logging.getLogger(__name__)


class PygameGraphicsSubsystem(Subsystem):
    def initialize(self):
        logger.debug('Initializing pygame graphics')
        pygame.display.init()
        pygame.font.init()
        screen = Screen()
        entity_registry.add(screen)
        entity_registry.add(PygameRenderer2d())
