from core.entity import Entity

PHYSICS_DEFAULT_ORDER = 1000
GRAPHICS_DEFAULT_ORDER = 2000
GAME_RULES_DEFAULT_ORDER = 3000


class Driver(Entity):
    def __init__(self, order):
        super(Driver, self).__init__()
        self.last_run = 0
        self.order = order

    def run(self, skip_frame):
        raise NotImplementedError()
