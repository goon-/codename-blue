import logging
from collections import namedtuple
from copy import copy

from core.drivers.driver import Driver
from core.gametime import GameTime
from core.glob import entity_registry
from core.physics.entities.dynamic_physic_entity import DynamicPhysicEntity
from core.physics.entities.physic_entity import Edge
from core.physics.entities.static_physic_entity import StaticPhysicEntity
from core.vector import Vector

logger = logging.getLogger(__name__)
CollisionParams = namedtuple('CollisionParams', ('side', 'time'))


class PlatformerPhysics(Driver):
    GRAVITY = 600
    DEFAULT_FRICTION = 0.5

    def __init__(self, tolerance=0.001):
        super(PlatformerPhysics, self).__init__(10)
        self._game_time = entity_registry.get_by_class(GameTime)[0]
        self._tolerance = tolerance

    def run(self, skip_frame):
        time_delta = self._game_time.now - self.last_run
        dynamic_physic_entities = entity_registry.get_by_class(DynamicPhysicEntity)
        for entity in dynamic_physic_entities:
            self._update_forces(entity)
            self._update_velocity(entity, time_delta)
            collision = self._get_collision(entity, time_delta)
            self._process_collision(entity, collision, time_delta)
            entity.force.zero()

        return True

    def _update_forces(self, entity):
        entity.force.y -= self.GRAVITY * entity.mass
        if entity.collision is not None and entity.collision.side == Edge.TOP and entity.velocity.x != 0:
            entity.force.x += entity.mass * self.GRAVITY * self.DEFAULT_FRICTION * (
                -1.0 if entity.velocity.x > 0 else 1.0
            )

    def _update_velocity(self, entity, time_delta):
        entity.velocity.add(entity.force * time_delta * entity.rev_mass)

    def _get_collision(self, entity, time_delta):
        velocity = entity.velocity.len()
        if not velocity:
            return

        entity_offset = Vector(entity.velocity.x * time_delta, entity.velocity.y * time_delta)
        collision_candidates = self._get_collision_candidates(entity, entity_offset)
        point_projections = [
            (point, Vector(point.x + entity_offset.x, point.y + entity_offset.y))
            for point in entity.vertices()
        ]
        rev_velocity = 1.0 / entity.velocity.len()
        collisions = []
        for candidate in collision_candidates:
            for point_proj in point_projections:
                for edge_num, edge in enumerate(candidate.edges()):
                    cross_point = self._get_cross_point(point_proj, edge)
                    if cross_point is not None:
                        collision_time = (cross_point - point_proj[0]).len() * rev_velocity
                        if self._eq(collision_time, 0):
                            collision_time = 0.0

                        collisions.append(CollisionParams(
                            Edge(edge_num),
                            collision_time
                        ))

        if collisions:
            return min(collisions, key=lambda x: x.time)

        return None

    def _process_collision(self, entity, collision, time_delta):
        entity.collision = collision
        if collision is not None:
            if collision.side in (Edge.LEFT, Edge.RIGHT):
                entity.position.x += entity.velocity.x * collision.time
                entity.position.y += entity.velocity.y * time_delta
                entity.velocity.x = 0.0
            else:
                entity.position.x += entity.velocity.x * time_delta
                entity.position.y += entity.velocity.y * collision.time
                entity.velocity.y = 0.0
        else:
            entity.position.add(entity.velocity * time_delta)

    def _get_collision_candidates(self, entity, entity_offset):
        entity_projection = copy(entity)
        entity_projection.position = entity.position + entity_offset
        static_entities = entity_registry.get_by_class(StaticPhysicEntity)
        return [ent for ent in static_entities if entity_projection.collides(ent)]

    def _get_cross_point(self, line1, line2):
        x1 = line1[0].x
        x2 = line1[1].x
        x3 = line2[0].x
        x4 = line2[1].x
        y1 = line1[0].y
        y2 = line1[1].y
        y3 = line2[0].y
        y4 = line2[1].y
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if self._eq(denominator, 0):
            return None

        cross_point = Vector(
            ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator,
            ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
        )
        if self._point_is_on_line(cross_point, line1) and self._point_is_on_line(cross_point, line2):
            return cross_point

        return None

    def _point_is_on_line(self, point, line):
        x = point.x
        y = point.y
        x1 = line[0].x
        x2 = line[1].x
        y1 = line[0].y
        y2 = line[1].y
        if self._eq(x1, x2) and self._eq(y1, y2) and self._eq(x1, x) and self._eq(y1, y):
            return True

        return self._eq((x - x1) * (y2 - y1) - (y - y1) * (x2 - x1), 0.0) and (
            self._ge(x, x1) and self._ge(x2, x) or self._ge(x, x2) and self._ge(x1, x)
        )

    def _eq(self, f1, f2):
        return abs(f1 - f2) < self._tolerance

    def _ge(self, f1, f2):
        return f1 - f2 >= -self._tolerance
