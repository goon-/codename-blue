from core.actors.actor import Actor
from core.glob import get_vec_fact, entity_registry
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from fm.graphics.placeholder import Placeholder


class Projectile(DynamicPhysicEntity, Placeholder, Actor):
    def __init__(self, position=None, projectile_force=None, color=(255, 255, 255), **kwargs):
        size = get_vec_fact().vector2(2, 2)
        super(Projectile, self).__init__(position=position, size=size, placeholder_size=size, color=color, **kwargs)
        self.projectile_force = projectile_force or get_vec_fact().vector2()

    def think(self):
        # TODO: fix physics to not modify vectors, but overwrite them with new ones
        self.force = self.projectile_force.copy()
        if self.collision:
            entity_registry.remove(self)
