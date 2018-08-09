from core.entity import Entity


class Subsystem(Entity):
    def initialize(self):
        raise NotImplementedError()
