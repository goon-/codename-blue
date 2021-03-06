import logging

from core.actors.actor_driver import ActorDriver
from core.drivers.fps_counter import FpsCounter
from core.game_rules import GameRules
from core.gametime import GameTime
from core.glob import entity_registry, get_vec_fact
from core.graphics.entities.renderer2d import Renderer2d
from core.graphics.entities.screen import Screen
from core.input.devices.keyboard import KEYS, Keyboard
from core.input.devices.mouse import Mouse, MBUTTONS
from core.input.key_mapping import KeyMapping
from core.input.player_input import PlayerInput
from fm.fm_player import FmPlayer
from fm.hud import Hud
from fm.npc.dummy_enemy import DummyEnemy
from fm.physics.spacecraft import SpacecraftPhysics
from fm.wall import Wall

logger = logging.getLogger(__name__)


class FmGameRules(GameRules):
    COLLSION_CAT_BACKGROUND = 0
    COLLSION_CAT_PLAYER = 1
    COLLSION_CAT_WALL = 2
    COLLSION_CAT_PLAYER_PROJECTILE = 3
    COLLSION_CAT_ENEMY = 4

    def __init__(self):
        super(FmGameRules, self).__init__()
        self._player = None
        self._game_time = None

    def initialize(self):
        key_mapping = KeyMapping({
            FmPlayer.ACT_MOVE_RIGHT: [(Keyboard, KEYS.d)],
            FmPlayer.ACT_MOVE_LEFT: [(Keyboard, KEYS.a)],
            FmPlayer.ACT_MOVE_UP: [(Keyboard, KEYS.w)],
            FmPlayer.ACT_MOVE_DOWN: [(Keyboard, KEYS.s)],
            FmPlayer.ACT_EXIT: [(Keyboard, KEYS.esc)],
            FmPlayer.ACT_FIRE: [(Keyboard, KEYS.space), (Mouse, MBUTTONS.lmb)],
        })
        keyboard = entity_registry.get_by_class(Keyboard)[0]
        mouse = entity_registry.get_by_class(Mouse)[0]
        self._player = FmPlayer(
            PlayerInput([keyboard, mouse], key_mapping), get_vec_fact().vector2(1, 200), z=1,
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
        entity_registry.add(FpsCounter())
        screen = entity_registry.get_by_class(Screen)[0]
        screen.set_resolution(400, 500)
        renderer = entity_registry.get_by_class(Renderer2d)[0]
        viewport = renderer.create_viewport((0, 0, 400, 500), (0, 0, 400, 500))
        entity_registry.add(viewport)
        mouse.set_viewport(viewport)
        entity_registry.add(Hud(get_vec_fact().vector2(0, 0), get_vec_fact().vector2(400, 100), self._player))
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def run(self, skip_frame):
        return True
