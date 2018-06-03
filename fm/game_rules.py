import logging

from core.actors.actor_driver import ActorDriver
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
    COLLSION_CAT_BACKGROUND = 0
    COLLSION_CAT_PLAYER = 1
    COLLSION_CAT_WALL = 2

    def __init__(self):
        super(FmGameRules, self).__init__(0)
        key_mapping = KeyMapping({
            0: KEYS.d,
            1: KEYS.a,
            2: KEYS.w,
            3: KEYS.s,
            4: KEYS.esc,
        })
        keyboard = entity_registry.get_by_class(Keyboard)[0]
        self._player = FmPlayer(
            PlayerInput(keyboard, key_mapping), get_vec_fact().vector2(1, 200), z=1,
            collision_category=self.COLLSION_CAT_PLAYER
        )
        entity_registry.add(self._player)
        entity_registry.add(Wall(
            get_vec_fact().vector2(-1, -1), get_vec_fact().vector2(1000, 1000), (200, 200, 255), z=2,
            collision_category=self.COLLSION_CAT_BACKGROUND
        ))
        physics = SpacecraftPhysics()
        physics.set_collidable_categories(self.COLLSION_CAT_BACKGROUND, [])
        physics.set_collidable_categories(self.COLLSION_CAT_PLAYER, [])
        entity_registry.add(physics)
        entity_registry.add(ActorDriver(20))
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def run(self, skip_frame):

        return True
