import logging.config

from core.drivers.fps_counter import FpsCounter
from core.gametime import GameTime
from core.glob import entity_registry
from core.physics.platformer import PlatformerPhysics
from core.world import World
from fm.game_rules import FmGameRules
from pygame_impl.event_pumper import PygameEventPumper
from pygame_impl.graphics.entites.renderer import PygameRenderer
from pygame_impl.graphics.entites.viewport import PygameViewport
from pygame_impl.init import init_pygame

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
    entity_registry.add(FpsCounter())
    entity_registry.add(PygameViewport((0, 0, 400, 400), (0, 0, 400, 400)))
    entity_registry.add(PygameRenderer())
    entity_registry.add(PygameEventPumper())

    entity_registry.add(GameTime(1.0 / 60.0))
    entity_registry.add(FmGameRules())
    world = World()
    world.run()
