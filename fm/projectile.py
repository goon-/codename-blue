from core.actors.actor import Actor
from core.glob import get_vec_fact
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from pygame_impl.graphics.entites.placeholder import Placeholder


class Projectile(DynamicPhysicEntity, Placeholder, Actor):
    def __init__(self, position=None, projectile_force=None, color=(255, 255, 255), **kwargs):
        size = get_vec_fact().vector2(2, 2)
        super(Projectile, self).__init__(position=position, size=size, placeholder_size=size, color=color, **kwargs)
        self.projectile_force = projectile_force or get_vec_fact().vector2()

    def think(self):
        self.force = self.projectile_force
