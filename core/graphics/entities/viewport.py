from core.entity import Entity
from core.glob import get_vec_fact


class Viewport(Entity):
    def __init__(self, rect, screen_rect):
        super(Viewport, self).__init__()
        self._rect = rect
        self._screen_rect = screen_rect
        self._transform = get_vec_fact().vector2(
            float(screen_rect[2]) / float(rect[2]),
            float(screen_rect[3]) / float(rect[3]),
        )
        self._world_translate = get_vec_fact().vector2(-rect[0], -rect[1])
        self._screen_translate = get_vec_fact().vector2(screen_rect[0], screen_rect[1])
        self._tmp = get_vec_fact().vector2()

    def transform_v(self, vector):
        vector.add(self._world_translate)
        vector.multiply_v(self._transform)
        # vector.add(self._screen_translate)

    def transform_p(self, point):
        self._tmp.x = point[0]
        self._tmp.y = point[1]
        self.transform_v(self._tmp)
        return self._tmp.x, self._tmp.y

    def transform_r(self, rect):
        self._tmp.x = rect[0]
        self._tmp.y = rect[1]
        self.transform_v(self._tmp)
        x1 = self._tmp.x
        y1 = self._tmp.y
        self._tmp.x = rect[2]
        self._tmp.y = rect[3]
        self.transform_v(self._tmp)
        return x1, y1, self._tmp.x, self._tmp.y
