from core.entity import Entity


class Screen(Entity):
    def __init__(self, screen):
        super(Screen, self).__init__()
        self.screen = screen
