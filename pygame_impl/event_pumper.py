import pygame

from core.drivers.driver import Driver


class PygameEventPumper(Driver):
    def __init__(self):
        super(PygameEventPumper, self).__init__(0)

    def run(self, skip_frame):
        pygame.event.pump()
        return True
