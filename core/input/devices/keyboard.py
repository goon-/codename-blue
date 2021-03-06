from enum import Enum

from core.input.devices.input_device import InputDevice


class KEYS(Enum):
    w = 'w'
    a = 'a'
    s = 's'
    d = 'd'
    space = 'space'
    esc = 'esc'


class Keyboard(InputDevice):
    pass
