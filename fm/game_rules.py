import logging

from core.drivers.driver import Driver
from core.gametime import GameTime
from core.glob import entity_registry, get_vec_fact
from core.input.devices.keyboard import KEYS, Keyboard
from core.input.key_mapping import KeyMapping
from core.input.player_input import PlayerInput
from fm.physics.spacecraft import SpacecraftPhysics
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
            2: KEYS.w,
            3: KEYS.s,
        })
        keyboard = entity_registry.get_by_class(Keyboard)[0]
        self._player = FmPlayer(PlayerInput(keyboard, key_mapping), get_vec_fact().vector2(100, 200))
        entity_registry.add(self._player)
        entity_registry.add(Wall(get_vec_fact().vector2(-1000, 0), get_vec_fact().vector2(2000, 10), (200, 200, 200)))
        physics = SpacecraftPhysics()
        entity_registry.add(physics)
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def run(self, skip_frame):
        if self._player.player_input.is_pressed(0) and self._player.velocity.len() <= self.SPEED_CAP:
            self._player.force.x += 6000

        if self._player.player_input.is_pressed(1) and self._player.velocity.len() <= self.SPEED_CAP:
            self._player.force.x -= 6000

        if self._player.player_input.is_pressed(2) and self._player.velocity.len() <= self.SPEED_CAP:
            self._player.force.y += 6000

        if self._player.player_input.is_pressed(3) and self._player.velocity.len() <= self.SPEED_CAP:
            self._player.force.y -= 6000

        return True
