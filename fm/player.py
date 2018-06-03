from core.glob import get_vec_fact
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from core.player import Player
from pygame_impl.graphics.entites.placeholder import Placeholder


class FmPlayer(Player, Placeholder, DynamicPhysicEntity):
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
