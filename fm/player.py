import logging

from core.glob import get_vec_fact, entity_registry
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from core.player import Player
from core.world import World
from pygame_impl.graphics.entites.placeholder import Placeholder

logger = logging.getLogger(__name__)


class FmPlayer(Player, Placeholder, DynamicPhysicEntity):
    SPEED_CAP = 100.0

    def __init__(self, player_input, position, z=0, collision_category=None):
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

    def think(self):
        if self.player_input.is_pressed(0) and self.velocity.len() <= self.SPEED_CAP:
            self.force.x += 6000

        if self.player_input.is_pressed(1) and self.velocity.len() <= self.SPEED_CAP:
            self.force.x -= 6000

        if self.player_input.is_pressed(2) and self.velocity.len() <= self.SPEED_CAP:
            self.force.y += 6000

        if self.player_input.is_pressed(3) and self.velocity.len() <= self.SPEED_CAP:
            self.force.y -= 6000

        if self.player_input.is_pressed(4):
            logger.info('Exiting')
            entity_registry.get_by_class(World)[0].stop()
