from core.physics.entities.static_physic_entity import StaticPhysicEntity
from pygame_impl.graphics.entites.placeholder import Placeholder


class Wall(StaticPhysicEntity, Placeholder):
    def __init__(self, position=None, size=None, color=(255, 255, 255), **kwargs):
        super(Wall, self).__init__(position=position, size=size, placeholder_size=size, color=color, **kwargs)
