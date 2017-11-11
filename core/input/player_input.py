class PlayerInput(object):
    def __init__(self, input_device, key_mapping):
        self._input_device = input_device
        self._key_mapping = key_mapping

    def is_pressed(self, action):
        if action not in self._key_mapping:
            return False

        return self._input_device.is_pressed(self._key_mapping[action])
