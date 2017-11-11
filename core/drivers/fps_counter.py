import logging
from time import time

from core.drivers.driver import Driver

logger = logging.getLogger(__name__)


class FpsCounter(Driver):
    def __init__(self):
        super(FpsCounter, self).__init__()
        self._runs = []
        self._count_period = 1.0
        self._output_period = 1.0
        self._last_output = 0

    def run(self, skip_frame):
        now = time()
        if not skip_frame:
            self._runs.append(now)

        while len(self._runs) > 0 and now - self._runs[0] > self._count_period:
            self._runs.pop(0)

        if now - self._last_output >= self._output_period:
            logger.debug('{} fps'.format(float(len(self._runs)) / float(self._count_period)))
            self._last_output = now
