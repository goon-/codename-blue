from core.math.vector_factory import VectorFactory
from entity import entity_registry as e
entity_registry = e

_vector_factory = None


def get_vec_fact():
    global _vector_factory
    if _vector_factory:
        return _vector_factory

    impls = e.get_by_class(VectorFactory)
    _vector_factory = impls[0] if len(impls) > 0 else None
    return _vector_factory
