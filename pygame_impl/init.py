import logging

import pygame

from pygame_impl.graphics.init import init_graphics
from pygame_impl.input.init import init_input_devices

logger = logging.getLogger(__name__)


def init_pygame():
    logger.debug('Initializing pygame...')
    pygame.init()
    init_graphics()
    init_input_devices()
    logger.debug('Initializing pygame... done')
