from core.drivers.driver import Driver
from core.gametime import GameTime
from core.glob import entity_registry
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from core.physics.entities.static_physic_entity import StaticPhysicEntity


class PlatformerPhysics(Driver):
    SPEED_CAP = 10.0
    GRAVITY = 0.5

    def __init__(self):
        super(PlatformerPhysics, self).__init__()
        self._game_time = entity_registry.get_by_class(GameTime)[0]

    def run(self, skip_frame):
        time_delta = self._game_time.now - self.last_run
        dynamic_physic_entities = entity_registry.get_by_class(DynamicPhysicEntity)
        static_physic_entities = entity_registry.get_by_class(StaticPhysicEntity)
        for entity in dynamic_physic_entities:
            entity.force.y -= self.GRAVITY
            if not entity.velocity and not entity.force:
                continue

            entity.velocity.add(entity.force * time_delta * entity.rev_mass)
            if len(entity.velocity) > self.SPEED_CAP:
                entity.velocity.normalize(self.SPEED_CAP)

            old_position = entity.position
            entity.position = old_position + entity.velocity * time_delta
            if self._collides_with_one_of(entity, static_physic_entities):
                entity.position = old_position
                entity.velocity.zero()

            entity.force.zero()

    def _collides_with_one_of(self, entity, entities):
        for ent in entities:
            if entity.collides(ent):
                return True

        return False
