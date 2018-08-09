import logging

from core.actors.actor_driver import ActorDriver
from core.drivers.driver import Driver
from core.gametime import GameTime
from core.glob import entity_registry, get_vec_fact
from core.input.devices.keyboard import KEYS, Keyboard
from core.input.key_mapping import KeyMapping
from core.input.player_input import PlayerInput
from fm.fm_player import FmPlayer
from fm.npc.dummy_enemy import DummyEnemy
from fm.physics.spacecraft import SpacecraftPhysics
from fm.wall import Wall

logger = logging.getLogger(__name__)


class FmGameRules(Driver):
    COLLSION_CAT_BACKGROUND = 0
    COLLSION_CAT_PLAYER = 1
    COLLSION_CAT_WALL = 2
    COLLSION_CAT_PLAYER_PROJECTILE = 3
    COLLSION_CAT_ENEMY = 4

    def __init__(self):
        super(FmGameRules, self).__init__()
        key_mapping = KeyMapping({
            FmPlayer.ACT_MOVE_RIGHT: KEYS.d,
            FmPlayer.ACT_MOVE_LEFT: KEYS.a,
            FmPlayer.ACT_MOVE_UP: KEYS.w,
            FmPlayer.ACT_MOVE_DOWN: KEYS.s,
            FmPlayer.ACT_EXIT: KEYS.esc,
            FmPlayer.ACT_FIRE: KEYS.space,
        })
        keyboard = entity_registry.get_by_class(Keyboard)[0]
        self._player = FmPlayer(
            PlayerInput(keyboard, key_mapping), get_vec_fact().vector2(1, 200), z=1,
            collision_category=self.COLLSION_CAT_PLAYER,
            projectile_collision_category=self.COLLSION_CAT_PLAYER_PROJECTILE
        )
        entity_registry.add(self._player)
        entity_registry.add(Wall(
            get_vec_fact().vector2(-1, -1), get_vec_fact().vector2(1000, 1000), (200, 200, 255), z=2,
            collision_category=self.COLLSION_CAT_BACKGROUND
        ))
        entity_registry.add(DummyEnemy(
            get_vec_fact().vector2(300, 300), 1000, 2, z=1, collision_category=self.COLLSION_CAT_ENEMY,
            color=(255, 0, 0)
        ))
        physics = SpacecraftPhysics()
        physics.set_collidable_categories(self.COLLSION_CAT_BACKGROUND, [])
        physics.set_collidable_categories(self.COLLSION_CAT_PLAYER, [])
        physics.set_collidable_categories(self.COLLSION_CAT_PLAYER_PROJECTILE, [self.COLLSION_CAT_ENEMY])
        entity_registry.add(physics)
        entity_registry.add(ActorDriver(20))
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def run(self, skip_frame):
        return True
