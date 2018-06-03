from core.physics.platformer import PlatformerPhysics


class SpacecraftPhysics(PlatformerPhysics):
    GRAVITY = 0
    DEFAULT_FRICTION = 0
    SLOWDOWN_RATE = 3

    def _update_forces(self, entity):
        super(SpacecraftPhysics, self)._update_forces(entity)
        entity.force.y -= self.SLOWDOWN_RATE * entity.mass * entity.velocity.y
        entity.force.x -= self.SLOWDOWN_RATE * entity.mass * entity.velocity.x
