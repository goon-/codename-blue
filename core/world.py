import logging

from core.drivers.driver import Driver
from entity import Entity
from gametime import GameTime
from glob import entity_registry

logger = logging.getLogger(__name__)


class World(Entity):
    def __init__(self, ):
        super(World, self).__init__()
        entity_registry.add(self)
        self._stop = False

    def run(self):
        drivers = sorted(entity_registry.get_by_class(Driver), key=lambda x: x.order)
        game_time = entity_registry.get_by_class(GameTime)[0]
        game_time.start()
        for driver in drivers:
            driver.last_run = game_time.now

        skipped_frames = 0
        while not self._stop:
            skip_frame = game_time.tick()
            for driver in drivers:
                if driver.run(skip_frame):
                    driver.last_run = game_time.now

            if skip_frame:
                skipped_frames += 1
            elif skipped_frames > 0:
                logger.warning('Skipped %s frames' % skipped_frames)
                skipped_frames = 0

        logger.info('The world has stopped')

    def stop(self):
        self._stop = True
