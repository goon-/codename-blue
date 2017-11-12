import pygame

from core.drivers.driver import Driver


class PygameEventPumper(Driver):
    def run(self, skip_frame):
        pygame.event.pump()
        return True
