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


entity_registry = EntityRegistry()
