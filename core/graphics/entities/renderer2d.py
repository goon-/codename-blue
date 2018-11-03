from core.drivers.driver import Driver, GRAPHICS_DEFAULT_ORDER
from core.glob import entity_registry
from core.graphics.entities.drawable_entity import DrawableEntity
from core.graphics.entities.renderer import Renderer
from core.graphics.entities.viewport import Viewport


def is_in_visible_rendering_group(entity):
    return not entity.rendering_group or entity.rendering_group.visible


class Renderer2d(Renderer):
    def __init__(self):
        super(Renderer2d, self).__init__()

    def render(self):
        viewports = entity_registry.get_by_class(Viewport)
        entities = entity_registry.get_by_class(DrawableEntity)
        self.clear_screen()
        for entity in sorted(filter(is_in_visible_rendering_group, entities), key=lambda x: -x.z):
            for viewport in viewports:
                entity.draw(viewport)

    def create_viewport(self, world_rect, screen_rect):
        raise NotImplementedError()

    def clear_screen(self):
        raise NotImplementedError()

    def fill_rect(self, viewport, rect, color):
        raise NotImplementedError()

    def text(self, viewport, position, text, color, font=None):
        raise NotImplementedError()

    def fill_polygon(self, viewport, pointlist, color):
        raise NotImplementedError()

    def line(self, viewport, start, end, color):
        raise NotImplementedError()
