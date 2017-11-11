import logging

from core.drivers.driver import Driver
from entity import Entity
from gametime import GameTime
from glob import entity_registry

logger = logging.getLogger(__name__)


class World(Entity):
    # TODO: move target_fps to run()
    def __init__(self, target_fps):
        super(World, self).__init__()
        self._game_time = GameTime(1.0 / float(target_fps))
        entity_registry.add(self)
        entity_registry.add(self._game_time)

    def run(self):
        drivers = entity_registry.get_by_class(Driver)
        self._game_time.start()
        for driver in drivers:
            driver.last_run = self._game_time.now

        while True:
            skip_frame = self._game_time.tick()
            for driver in drivers:
                if driver.run(skip_frame):
                    driver.last_run = self._game_time.now

            if skip_frame:
                logger.warning('Skipped a frame')
