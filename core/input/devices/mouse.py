from enum import Enum

from core.input.devices.input_device import InputDevice


class MBUTTONS(Enum):
    lmb = 'lmb'
    mmb = 'mmb'
    rmb = 'rmb'


class Mouse(InputDevice):
    def __init__(self):
        super(Mouse, self).__init__()
        self.viewport = None

    def get_screen_pos(self):
        raise NotImplementedError()

    def get_world_pos(self):
        if self.viewport is None:
            raise Exception('Cannot translate mouse position to world coordinates: viewport not set')

        return self.viewport.screen_to_world_p(self.get_screen_pos())

    def set_viewport(self, viewport):
        self.viewport = viewport
