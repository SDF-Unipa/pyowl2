import abc

from pyowl2.abstracts.object import OWLObject


class OWLEntity(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class serves as the foundational representation for named elements within an OWL ontology, such as classes, object properties, and individuals. It is designed to be subclassed rather than instantiated directly, providing a common structural ancestor for all distinct ontology components. The class implements comparison and hashing logic that relies entirely on the string representation of the entity; therefore, equality, ordering, and hash values are determined by comparing the string forms of the objects. This behavior ensures that entities with identical string identifiers are treated as indistinguishable for the purposes of sorting and storage in collections like sets and dictionaries.
    """

    __slots__ = ()