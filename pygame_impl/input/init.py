import logging

from core.glob import entity_registry
from pygame_impl.input.devices.keyboard import PygameKeyboard

logger = logging.getLogger(__name__)


def init_input_devices():
    logger.debug('Initializing pygame user input...')
    already_registered = len(entity_registry.get_by_class(PygameKeyboard)) > 0
    if not already_registered:
        entity_registry.add(PygameKeyboard())

    logger.debug('Initializing pygame user input... done')
