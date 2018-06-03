from core.actors.actor import Actor


class Player(Actor):
    def __init__(self, player_input=None, **kwargs):
        super(Player, self).__init__(**kwargs)
        self.player_input = player_input
