import logging

from core.drivers.driver import Driver
from core.gametime import GameTime
from core.glob import entity_registry
from core.input.devices.keyboard import KEYS, Keyboard
from core.input.key_mapping import KeyMapping
from core.input.player_input import PlayerInput
from core.physics.entities.physic_entity import Edge
from core.physics.platformer import PlatformerPhysics
from core.vector import Vector
from fm.player import FmPlayer
from fm.wall import Wall

logger = logging.getLogger(__name__)


class FmGameRules(Driver):
    SPEED_CAP = 100.0

    def __init__(self):
        super(FmGameRules, self).__init__(0)
        key_mapping = KeyMapping({
            0: KEYS.d,
            1: KEYS.a,
            2: KEYS.space,
        })
        keyboard = entity_registry.get_by_class(Keyboard)[0]
        self._player = FmPlayer(PlayerInput(keyboard, key_mapping), Vector(100, 200))
        entity_registry.add(self._player)
        entity_registry.add(Wall(Vector(-1000, 0), Vector(2000, 10), (200, 200, 200)))
        entity_registry.add(PlatformerPhysics())
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def run(self, skip_frame):
        if self._player.player_input.is_pressed(0) and self._player.velocity.x <= self.SPEED_CAP:
            self._player.force.x += 6000

        if self._player.player_input.is_pressed(1) and self._player.velocity.x >= -self.SPEED_CAP:
            self._player.force.x -= 6000

        if self._player.player_input.is_pressed(2) and self._player.collision is not None and \
                        self._player.collision.side == Edge.TOP:
            self._player.velocity.y += 150

        return True
