import logging

from core.gametime import GameTime
from core.glob import get_vec_fact, entity_registry
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from core.player import Player
from core.world import World
from fm.entities.projectile import Projectile
from fm.graphics.placeholder import Placeholder

logger = logging.getLogger(__name__)


class FmPlayer(Player, Placeholder, DynamicPhysicEntity):
    SPEED_CAP = 100.0
    ACT_MOVE_RIGHT = 0
    ACT_MOVE_LEFT = 1
    ACT_MOVE_UP = 2
    ACT_MOVE_DOWN = 3
    ACT_EXIT = 4
    ACT_FIRE = 5

    def __init__(self, player_input, position, z=0, collision_category=None, projectile_collision_category=None):
        size = get_vec_fact().vector2(20, 10)
        super(FmPlayer, self).__init__(
            player_input=player_input,
            placeholder_size=size,
            position=position,
            mass=10.0,
            size=size,
            z=z,
            collision_category=collision_category
        )
        self.projectile_collision_category = projectile_collision_category
        self.fire_cooldown = 0.2
        self._last_shot_time = 0
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def think(self):
        if self.player_input.is_pressed(self.ACT_MOVE_RIGHT) and self.velocity.len() <= self.SPEED_CAP:
            self.force.x += 6000

        if self.player_input.is_pressed(self.ACT_MOVE_LEFT) and self.velocity.len() <= self.SPEED_CAP:
            self.force.x -= 6000

        if self.player_input.is_pressed(self.ACT_MOVE_UP) and self.velocity.len() <= self.SPEED_CAP:
            self.force.y += 6000

        if self.player_input.is_pressed(self.ACT_MOVE_DOWN) and self.velocity.len() <= self.SPEED_CAP:
            self.force.y -= 6000

        if self.player_input.is_pressed(self.ACT_EXIT):
            logger.info('Exiting')
            entity_registry.get_by_class(World)[0].stop()

        if self.player_input.is_pressed(self.ACT_FIRE):
            self.shoot()

    def shoot(self):
        if self._game_time.now - self._last_shot_time < self.fire_cooldown:
            return

        projectile_spawn_position = self.position + get_vec_fact().vector2(21, 0)
        projectile_direction = self._calc_normalized_projectile_direction(projectile_spawn_position)
        entity_registry.add(Projectile(
            projectile_spawn_position, projectile_direction * 1000, (0, 0, 255),
            velocity=projectile_direction * 300, mass=1, z=self.z,
            collision_category=self.projectile_collision_category
        ))
        self._last_shot_time = self._game_time.now

    def _calc_normalized_projectile_direction(self, spawn_position):
        mouse_position = self.player_input.get_mouse_world_pos()
        direction = get_vec_fact().vector2(*mouse_position) - spawn_position
        direction.normalize()
        return direction

    @property
    def time_until_next_shot(self):
        time = self.fire_cooldown - (self._game_time.now - self._last_shot_time)
        return time if time > 0 else 0
