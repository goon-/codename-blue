from core.entity import Entity


class Screen(Entity):
    def __init__(self):
        super(Screen, self).__init__()
        self.res_x = None
        self.res_y = None

    def set_resolution(self, res_x, res_y):
        raise NotImplementedError()
