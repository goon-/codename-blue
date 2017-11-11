from time import time, sleep

from entity import Entity


class GameTime(Entity):
    def __init__(self, frame_time):
        super(GameTime, self).__init__()
        self.now = 0
        self._frame_time = frame_time

    def start(self):
        self.now = time()

    def tick(self):
        self.now += self._frame_time
        time_gap = self.now - time()
        if time_gap > 0:
            sleep(time_gap)

        return time_gap < 0
