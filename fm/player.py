from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from core.player import Player
from core.vector import Vector
from pygame_impl.graphics.entites.placeholder import Placeholder


class FmPlayer(Player, Placeholder, DynamicPhysicEntity):
    def __init__(self, player_input, position):
        size = Vector(10, 15)
        super(FmPlayer, self).__init__(
            player_input=player_input,
            placeholder_size=size,
            position=position,
            mass=10.0,
            size=size,
        )
        # Player.__init__(self, player_input=player_input)
        # Placeholder.__init__(self, position, size)
        # DynamicPhysicEntity.__init__(self, position, size, mass=10.0)
