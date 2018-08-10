from core.drivers.driver import Driver, GRAPHICS_DEFAULT_ORDER


class Renderer(Driver):
    def __init__(self):
        super(Renderer, self).__init__(GRAPHICS_DEFAULT_ORDER)

    def run(self, skip_frame):
        if not skip_frame:
            self.render()

        return not skip_frame

    def render(self):
        raise NotImplementedError()
