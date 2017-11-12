from core.entity import Entity


class Driver(Entity):
    def __init__(self, order):
        super(Driver, self).__init__()
        self.last_run = 0
        self.order = order

    def run(self, skip_frame):
        raise NotImplementedError()
