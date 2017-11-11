from core.entity import Entity


class Player(Entity):
    def __init__(self, player_input=None, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.player_input = player_input
