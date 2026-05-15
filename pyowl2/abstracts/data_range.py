import abc

from pyowl2.abstracts.object import OWLObject


class OWLDataRange(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class represents a set of literal values within an ontology, typically corresponding to specific datatypes or logical combinations of datatypes. It serves as the foundational type for defining the value space of data properties, specifying what kinds of literal inputs—such as integers, strings, or restricted value sets—are permissible. Equality, ordering, and hashing for instances are determined exclusively by their string representations, meaning two objects are considered equal if their string forms match. Because this is an abstract class, it is intended to be subclassed by concrete implementations that define specific data ranges rather than instantiated directly.
    """

    __slots__ = ()