class Entity(object):
    def __init__(self):
        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        try:
            me = entity_registry[val]
        except:
            me = None

        if self is not me:
            raise Exception("Can't touch this")

        self._id = val

    def on_destroy(self):
        pass


class EntityRegistry(object):
    def __init__(self):
        super(EntityRegistry, self).__init__()
        self._next_id = 1
        self._entities = {}

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Entity id must be int')

        return self._entities[item]

    def add(self, entity):
        if not isinstance(entity, Entity):
            raise TypeError('Entity registry is for entities')

        # TODO: check for duplicates
        self._entities[self._next_id] = entity
        entity.id = self._next_id
        self._next_id += 1

    def get_by_class(self, clazz):
        ret = []
        for entity in self._entities.values():
            if isinstance(entity, clazz):
                ret.append(entity)

        return ret

    def remove(self, entity):
        if not isinstance(entity, Entity):
            raise TypeError('Cannot remove a non-entity from the registry')

        if entity.id not in self._entities:
            raise TypeError('Entity with id %s is not registered' % entity.id)

        entity_from_registry = self._entities[entity.id]
        if entity_from_registry is not entity:
            raise TypeError('Tried to remove an invalid entity (did you manually assign the entity id?)')

        self._entities[entity.id].on_destroy()
        del self._entities[entity.id]


entity_registry = EntityRegistry()
