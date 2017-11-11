from core.entity import Entity


class Driver(Entity):
    def __init__(self):
        super(Driver, self).__init__()
        self.last_run = 0

    def run(self, skip_frame):
        raise NotImplementedError()
