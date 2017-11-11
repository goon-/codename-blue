import logging

import pygame

from core.glob import entity_registry
from pygame_impl.graphics.entites.screen import Screen

logger = logging.getLogger(__name__)


def init_graphics():
    logger.debug('Initializing pygame graphics...')
    screen = pygame.display.set_mode((400, 400))
    entity_registry.add(Screen(screen))
    logger.debug('Initializing pygame graphics... done')
