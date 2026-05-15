import abc

from pyowl2.abstracts.property_range import OWLPropertyRange


class OWLClassExpression(OWLPropertyRange, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class represents a class expression within the Web Ontology Language (OWL), serving as a fundamental construct for defining classes based on their relationships to other entities and properties. It acts as a common interface for various types of class descriptions, ranging from simple named classes to complex logical restrictions, and can be utilized as a range for property definitions. As an abstract class, it is intended to be subclassed rather than instantiated directly. Implementations of this class determine equality and ordering by comparing their string representations, implying that logical equivalence is evaluated based on the specific serialization format used.
    """

    __slots__ = ()