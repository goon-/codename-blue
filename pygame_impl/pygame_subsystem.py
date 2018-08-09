import logging

import pygame

from core.glob import entity_registry
from core.subsystem import Subsystem
from pygame_impl.event_pumper import PygameEventPumper

logger = logging.getLogger(__name__)


class PygameSubsystem(Subsystem):
    def initialize(self):
        logger.debug('Initializing pygame')
        # pygame.init()
        entity_registry.add(PygameEventPumper())
