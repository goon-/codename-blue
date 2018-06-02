from core.glob import get_vec_fact
from core.physics.entities.physic_entity import PhysicEntity


class DynamicPhysicEntity(PhysicEntity):
    def __init__(self, velocity=None, force=None, mass=0.0, **kwargs):
        super(DynamicPhysicEntity, self).__init__(**kwargs)
        self.velocity = velocity or get_vec_fact().vector2()
        self.force = force or get_vec_fact().vector2()
        self.mass = mass
        # TODO: introduce the notion of actually infinite mass. 99999 is not infinite enough
        self.rev_mass = 1 / float(mass) if mass else 99999
