import logging

from core.actors.actor import Actor
from core.glob import entity_registry, get_vec_fact
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from fm.entities.projectile import Projectile
from fm.fm_player import FmPlayer
from fm.graphics.explosion_placeholder import ExplosionPlaceholder
from fm.graphics.placeholder import Placeholder

logger = logging.getLogger(__name__)


class DummyEnemy(DynamicPhysicEntity, Placeholder, Actor):
    def __init__(self, position, movement_force=1, hp=2, z=0, **kwargs):
        size = get_vec_fact().vector2(20, 10)
        super(DummyEnemy, self).__init__(position=position, z=z, size=size, placeholder_size=size, mass=10, **kwargs)
        self.movement_force = movement_force
        self.hp = hp
        self._player = entity_registry.get_by_class(FmPlayer)[0]

    def think(self):
        if self.collision and isinstance(self.collision.entity, Projectile):
            logger.debug("DummyEnemy #%s: I'm hit!" % self.id)
            self.hp -= 1

        if self.hp > 0:
            self._do_enemy_stuff()
        else:
            self._handle_death()

    def _do_enemy_stuff(self):
        # move towards the player
        self.force = (self.position - self._player.position).normalized(-self.movement_force)

    def _handle_death(self):
        entity_registry.add(ExplosionPlaceholder(
            20, color=self.color, position=self.position.copy(), playing=True, cycle=False, destroy_on_completion=True,
            speed=2.0
        ))
        entity_registry.remove(self)
