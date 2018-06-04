import math

from core.actors.actor import Actor
from core.gametime import GameTime
from core.glob import entity_registry


class Animation(Actor):
    def __init__(
            self, frames_count, animation_time, speed=1.0, playing=True, cycle=False, destroy_on_completion=False,
            **kwargs
    ):
        super(Animation, self).__init__(**kwargs)
        if frames_count <= 0:
            raise Exception('Invalid number of animation frames: %s' % self._frames_count)

        self._speed = None
        self._frame_time = None
        self._previous_frame_time = 0
        self._current_frame = 0
        self._game_time = entity_registry.get_by_class(GameTime)[0]
        self._playing = None
        self._frames_count = frames_count
        self._animation_time = animation_time

        self.cycle = cycle
        self.destroy_on_completion = destroy_on_completion
        self.speed = speed
        self.playing = playing

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, val):
        self._speed = val
        self._frame_time = float(self._animation_time) / float(self._frames_count) / float(self._speed)

    @property
    def playing(self):
        return self._playing

    @playing.setter
    def playing(self, val):
        resumed = (not self._playing) and val
        if resumed:
            self._previous_frame_time = self._game_time.now

        self._playing = val

    def _update_animation(self):
        if not self.playing:
            return

        # calculate by how many frames to advance the animation
        now = self._game_time.now
        time_diff = now - self._previous_frame_time
        frames_diff = int(math.ceil(time_diff / self._frame_time))
        if frames_diff <= 0:
            return

        # render current animation frame
        self.render_frame(self._current_frame)

        # update frame number and previous frame time
        self._current_frame = (self._current_frame + frames_diff) % self._frames_count
        self._previous_frame_time = now

        # pause or destroy animation if it shouldn't be cycled and we've played all the frames
        animation_has_cycled = self._current_frame < frames_diff or frames_diff > self._frames_count
        if animation_has_cycled and not self.cycle:
            if self.destroy_on_completion:
                entity_registry.remove(self)
            else:
                self.playing = False

    def think(self):
        self._update_animation()

    def render_frame(self, frame_number):
        raise NotImplementedError()
