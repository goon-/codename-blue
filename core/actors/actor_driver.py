from core.actors.actor import Actor
from core.drivers.driver import Driver
from core.glob import entity_registry


class ActorDriver(Driver):
    def run(self, skip_frame):
        actors = entity_registry.get_by_class(Actor)
        for actor in actors:
            actor.think()
