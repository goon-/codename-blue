from core.graphics.entities.drawable_entity import DrawableEntity


class Hud(DrawableEntity):
    def __init__(self, position, size, player, **kwargs):
        super(Hud, self).__init__(z=-1, **kwargs)
        self.position = position
        self.player = player
        self.size = size

    def draw(self, viewport):
        self.renderer.fill_rect(
            viewport=viewport,
            rect=(
                self.position.x,
                self.position.y,
                self.position.x + self.size.x,
                self.position.y + self.size.y,
            ),
            color=(0, 0, 0)
        )
        self.renderer.fill_rect(
            viewport=viewport,
            rect=(
                self.position.x,
                self.position.y,
                self.position.x + (1 - self.player.time_until_next_shot / self.player.fire_cooldown) * 100,
                self.position.y + 20,
            ),
            color=(0, 0, 255)
        )
