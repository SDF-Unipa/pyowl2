import abc

from pyowl2.abstracts.object import OWLObject


class OWLAnnotationValue(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    Represents the specific value assigned to an annotation property for a given subject in the Web Ontology Language (OWL). As an abstract base class, it defines a common interface for different types of values, which may include anonymous individuals, IRIs, or Literals. The implementation enforces that equality, ordering, and hashing are determined solely by the string representation of the object, ensuring that comparisons are based on lexical form rather than object identity.
    """

    __slots__ = ()