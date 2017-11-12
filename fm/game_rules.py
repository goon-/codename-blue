import logging

from core.drivers.driver import Driver
from core.glob import entity_registry
from core.player import Player

logger = logging.getLogger(__name__)


class FmGameRules(Driver):
    def run(self, skip_frame):
        player = entity_registry.get_by_class(Player)[0]
        if player.player_input.is_pressed(1):
            player.force.x = 0.1
        else:
            player.force.x = 0.0

        return True
