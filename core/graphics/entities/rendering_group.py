from core.entity import Entity


class RenderingGroup(Entity):
    def __init__(self, visible=True):
        super(RenderingGroup, self).__init__()
        self.visible = visible
