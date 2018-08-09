from core.glob import entity_registry
from core.graphics.entities.animation import Animation
from fm.graphics.placeholder import Placeholder


class ExplosionPlaceholder(Animation):
    def __init__(self, explosion_size, position, color, **kwargs):
        super(ExplosionPlaceholder, self).__init__(60, 1, **kwargs)
        self.explosion_size = explosion_size
        self.position = position
        self._explosion_climax_frame = 10.0
        self._last_frame = float(self._frames_count - 1)
        self._placeholder = Placeholder(color=color)
        entity_registry.add(self._placeholder)

    def render_frame(self, frame_number):
        if frame_number < self._explosion_climax_frame:
            current_size = self.explosion_size * (float(frame_number) / self._explosion_climax_frame)
        else:
            current_size = self.explosion_size * (self._last_frame - float(frame_number)) / (self._last_frame - self._explosion_climax_frame)

        offset = (float(self.explosion_size) - current_size) / 2
        self._placeholder.placeholder_size.x = self._placeholder.placeholder_size.y = current_size
        self._placeholder.position.x = self.position.x + offset
        self._placeholder.position.y = self.position.y + offset

    def on_destroy(self):
        entity_registry.remove(self._placeholder)
