import abc
import typing

from pyowl2.abstracts.object import OWLObject
from pyowl2.base.annotation import OWLAnnotation


class OWLAxiom(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    This abstract base class represents a fundamental assertion or statement within an ontology, serving as the foundational component for defining the logical structure of the knowledge base. It supports the attachment of optional metadata through a list of annotations, which are automatically sorted upon assignment to maintain a consistent state. Instances of this class utilize their string representation to determine equality, hash values, and ordering, meaning that comparisons are based on the textual form of the axiom rather than object identity.

    :param axiom_annotations: Sorted list of annotations providing metadata about the axiom, or None if no annotations are present.
    :type axiom_annotations: typing.Optional[list[OWLAnnotation]]
    """

    # __slots__ = ()
    def __init__(self, annotations: typing.Optional[list[OWLAnnotation]] = None):
        """
        Initializes the instance with an optional list of annotations, storing them in a normalized, sorted state to ensure consistent structural representation. If annotations are provided, they are sorted lexicographically before assignment to the internal attribute; otherwise, the annotation collection remains unset. This behavior facilitates reliable comparison and hashing of axioms by decoupling the internal state from the arbitrary order of input annotations.

        :param annotations: Optional list of annotations to be associated with the axiom. If provided, the list is sorted before storage.
        :type annotations: typing.Optional[list[OWLAnnotation]]
        """

        self._axiom_annotations: typing.Optional[list[OWLAnnotation]] = (
            sorted(annotations) if annotations else annotations
        )

    @property
    def axiom_annotations(self) -> typing.Optional[list[OWLAnnotation]]:
        """
        Sets the annotations associated with the OWL axiom, overwriting any previously stored annotations. The method accepts a list of OWLAnnotation objects or None; if a non-empty list is provided, it is sorted before being assigned to the internal state to maintain a consistent order. If the input is None or an empty list, it is stored as is without sorting.

        :param value: A list of OWL annotations to assign to the axiom.
        :type value: typing.Optional[list[OWLAnnotation]]
        """

        return self._axiom_annotations

    @axiom_annotations.setter
    def axiom_annotations(self, value: typing.Optional[list[OWLAnnotation]]) -> None:
        """Setter for axiom_annotations."""
        self._axiom_annotations = sorted(value) if value else value