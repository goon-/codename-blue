from core.drivers.driver import Driver, GAME_RULES_DEFAULT_ORDER


class GameRules(Driver):
    def __init__(self):
        super(GameRules, self).__init__(GAME_RULES_DEFAULT_ORDER)

    def initialize(self):
        raise NotImplementedError()
