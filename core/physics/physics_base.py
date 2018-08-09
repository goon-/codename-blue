from core.drivers.driver import Driver, PHYSICS_DEFAULT_ORDER


class PhysicsBase(Driver):
    def __init__(self):
        super(PhysicsBase, self).__init__(PHYSICS_DEFAULT_ORDER)
        self.collision_rules = {}

    def set_collidable_categories(self, category, collidable_categories):
        cc_set = set(collidable_categories + [category])
        for collision_category in cc_set:
            if collision_category not in self.collision_rules:
                self._add_collision_category(self.collision_rules, collision_category)

        for collidable_category in collidable_categories:
            self._set_collision_category_rule(self.collision_rules, category, collidable_category, True)

    @staticmethod
    def _add_collision_category(collision_rules, collision_category):
        collision_rules[collision_category] = {k: False for k in collision_rules.keys()}
        for collision_category_rules in collision_rules.values():
            collision_category_rules[collision_category] = False

    @staticmethod
    def _set_collision_category_rule(collision_rules, category1, category2, collidable):
        collision_rules[category1][category2] = collidable
        collision_rules[category2][category1] = collidable

    def are_entities_collidable(self, entity1, entity2):
        return entity1.collision_category is not None and \
               entity2.collision_category is not None and \
               self._are_categories_collidable(
                   self.collision_rules, entity1.collision_category, entity2.collision_category
               )

    @staticmethod
    def _are_categories_collidable(collision_rules, category1, category2):
        if category1 not in collision_rules:
            raise Exception('Collision category {category} is not registered'.format(category=category1))

        return collision_rules[category1][category2]
