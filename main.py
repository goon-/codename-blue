import logging.config

from core.gametime import GameTime
from core.glob import entity_registry
from core.math.default_vector_factory import DefaultVectorFactory
from core.subsystem import Subsystem
from core.world import World
from fm.game_rules import FmGameRules
from pygame_impl.graphics.graphics_subsystem import PygameGraphicsSubsystem
from pygame_impl.input.input_subsystem import PygameInputSubsystem
from pygame_impl.pygame_subsystem import PygameSubsystem

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


def initialize_subsystems():
    subsystems = entity_registry.get_by_class(Subsystem)
    for subsystem in subsystems:
        subsystem.initialize()


if __name__ == '__main__':
    # TODO: move core stuff initialization somewhere
    entity_registry.add(DefaultVectorFactory())
    entity_registry.add(GameTime(1.0 / 60.0))

    entity_registry.add(PygameSubsystem())
    entity_registry.add(PygameGraphicsSubsystem())
    entity_registry.add(PygameInputSubsystem())
    initialize_subsystems()

    game_rules = FmGameRules()
    entity_registry.add(game_rules)
    game_rules.initialize()

    world = World()
    world.run()
