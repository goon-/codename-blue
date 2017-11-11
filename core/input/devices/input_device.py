from core.entity import Entity


class InputDevice(Entity):
    def is_pressed(self, key):
        raise NotImplementedError()
