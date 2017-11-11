from core.drivers.driver import Driver
from core.glob import entity_registry
from core.graphics.entities.drawable_entity import DrawableEntity
from core.graphics.entities.viewport import Viewport


class Renderer(Driver):
    def run(self, skip_frame):
        if not skip_frame:
            self.render()

    def render(self):
        viewports = entity_registry.get_by_class(Viewport)
        entities = entity_registry.get_by_class(DrawableEntity)
        self.clear_screen()
        for entity in sorted(entities, key=lambda x: x.z):
            for viewport in viewports:
                entity.draw(viewport)

    def clear_screen(self):
        raise NotImplementedError()
