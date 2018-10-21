from core.input.devices.mouse import Mouse


class PlayerInput(object):
    def __init__(self, input_devices, key_mapping):
        self._input_devices = input_devices
        self._key_mapping = key_mapping

    def is_pressed(self, action):
        if action not in self._key_mapping:
            return False

        for device in self._input_devices:
            for device_class, key in self._key_mapping[action]:
                if isinstance(device, device_class) and device.is_pressed(key):
                    return True

        return False

    def get_mouse_world_pos(self):
        mice = filter(lambda device: isinstance(device, Mouse), self._input_devices)
        if len(mice) == 0:
            return 0, 0

        return mice[0].get_world_pos()
