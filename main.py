from core.drivers.fps_counter import FpsCounter
from core.glob import entity_registry
from core.input.devices.keyboard import KEYS
from core.input.key_mapping import KeyMapping
from core.input.player_input import PlayerInput
from core.physics.platformer import PlatformerPhysics
from core.vector import Vector
from core.world import World
from fm.game_rules import FmGameRules
from fm.player import FmPlayer
from fm.wall import Wall
from pygame_impl.event_pumper import PygameEventPumper
from pygame_impl.graphics.entites.renderer import PygameRenderer
from pygame_impl.graphics.entites.viewport import PygameViewport
from pygame_impl.init import init_pygame

import logging.config

from pygame_impl.input.devices.keyboard import PygameKeyboard

logger = logging.getLogger(__name__)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] [%(name)s] %(message)s'
        },
    },
    'handlers': {
        'stdout': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': ['stdout'],
            'level': 'DEBUG',
        },
    }
})


if __name__ == '__main__':
    init_pygame()
    keyboard = entity_registry.get_by_class(PygameKeyboard)[0]
    entity_registry.add(FpsCounter())
    entity_registry.add(PygameViewport((0, 0, 400, 400), (0, 0, 400, 400)))
    entity_registry.add(PygameRenderer())
    entity_registry.add(PygameEventPumper())

    entity_registry.add(FmPlayer(PlayerInput(keyboard, KeyMapping({1: KEYS.a})), Vector(100, 20)))
    entity_registry.add(Wall(Vector(-1000, 0), Vector(2000, 10), (200, 200, 200)))

    entity_registry.add(FmGameRules())
    world = World(60)
    entity_registry.add(PlatformerPhysics())
    world.run()
