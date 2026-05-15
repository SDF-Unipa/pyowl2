from __future__ import annotations

import typing

from rdflib import OWL, Namespace, URIRef

from pyowl2.abstracts.annotation_subject import OWLAnnotationSubject
from pyowl2.abstracts.annotation_value import OWLAnnotationValue


class IRI(OWLAnnotationSubject, OWLAnnotationValue):
    """
    This class models an Internationalized Resource Identifier (IRI), acting as a global identifier for entities within an ontology by combining a namespace prefix with a specific local value. It is primarily used to reference classes, individuals, or properties in OWL structures and can be instantiated by providing a `Namespace` object and an optional string identifier. The class facilitates interaction with RDF data by offering a method to convert the IRI into a `URIRef`, while also providing utility methods to identify standard OWL entities such as `owl:Thing` and `owl:Nothing`. Comparisons and string representations are handled based on the full resolved identifier.

    :param namespace: The base prefix or context for the identifier, representing a collection of related entities and combining with the specific value to construct the full Internationalized Resource Identifier.
    :type namespace: Namespace
    :param value: The specific identifier for an entity, which can be a local string fragment combined with the namespace or a complete URI reference.
    :type value: typing.Union[str, URIRef]
    """

    def __init__(
        self,
        namespace: Namespace,
        value: typing.Union[str, URIRef] = "",
    ) -> None:
        """
        Initializes a new Internationalized Resource Identifier (IRI) instance by associating a specific local value with a given namespace. The constructor requires a `Namespace` object to define the base context and accepts an optional `value` argument—either a string or a `URIRef`—which defaults to an empty string if not provided. This method stores the namespace and value as internal attributes without performing immediate validation or concatenation, allowing the object to represent either the namespace itself (if the value is empty) or a specific resource within it.

        :param namespace: The namespace instance to associate with this object.
        :type namespace: Namespace
        :param value: The specific value or URI reference for the term, accepted as a string or a URIRef object.
        :type value: typing.Union[str, URIRef]
        """

        self._namespace: Namespace = namespace
        self._value: typing.Union[str, URIRef] = value

    @staticmethod
    def thing_iri() -> typing.Self:
        """
        Returns an instance of the IRI class representing the `owl:Thing` concept, which serves as the root class of the class hierarchy in the OWL ontology. This static method generates the IRI by combining the standard OWL namespace with the specific identifier for 'Thing'. The function requires no arguments and has no side effects, simply providing a convenient way to access the IRI for the universal class.

        :return: Returns the IRI for `owl:Thing`.

        :rtype: typing.Self
        """

        return IRI(Namespace(OWL._NS), OWL.Thing)

    @staticmethod
    def nothing_iri() -> typing.Self:
        """
        Returns an IRI instance representing the OWL concept of "Nothing," which denotes the empty class containing no instances. This static method constructs the IRI by combining the standard OWL namespace with the specific identifier for "Nothing," providing a convenient accessor for this fundamental ontology term. The method creates a new IRI object upon each invocation.

        :return: Returns the IRI for `owl:Nothing`.

        :rtype: typing.Self
        """

        return IRI(Namespace(OWL._NS), OWL.Nothing)

    @property
    def value(self) -> typing.Union[str, URIRef]:
        """
        Updates the internal representation of the IRI by assigning the provided value to the private `_value` attribute. This setter accepts either a string or a URIRef object as input, performing no validation or type conversion before assignment. As a result, the internal state is modified directly to reflect the provided argument, regardless of whether it constitutes a valid IRI or matches the expected type strictly.

        :param value: The full IRI to set, provided as either a string or a URIRef.
        :type value: typing.Union[str, URIRef]
        """

        return self._value

    @value.setter
    def value(self, value: typing.Union[str, URIRef]) -> None:
        """Setter for full_iri."""
        self._value = value

    @property
    def namespace(self) -> Namespace:
        """
        Updates the namespace associated with the IRI instance by assigning the provided Namespace object to the internal state. This setter replaces any previously defined namespace, effectively altering the IRI's context or prefix mapping. The operation mutates the object in place and does not return a value.

        :param value: The Namespace object to assign to the instance.
        :type value: Namespace
        """

        return self._namespace

    @namespace.setter
    def namespace(self, value: Namespace) -> None:
        self._namespace = value

    def to_uriref(self) -> URIRef:
        """
        Converts the IRI instance into a concrete URIRef object by resolving it against the associated namespace. If the internal value is already a URIRef, it is returned directly; otherwise, the value is treated as a local identifier and used to construct a URIRef via the namespace. This method requires the `namespace` attribute to be a valid `Namespace` instance, raising an `AssertionError` if this condition is not met, and may propagate errors if the value cannot be resolved within the namespace context.

        :return: A `URIRef` representing the fully qualified URI. Returns the value directly if it is already a URIRef, otherwise resolves it against the associated namespace.

        :rtype: URIRef
        """

        # assert isinstance(self.namespace, Namespace)
        return (
            self.value if isinstance(self.value, URIRef) else self.namespace[self.value]
        )

    def is_owl_thing(self) -> bool:
        """
        Determines whether the current IRI corresponds to the universal class 'owl:Thing' within the Web Ontology Language (OWL). The method performs a strict equality check by converting the IRI instance to a URI reference and comparing it against the standard OWL.Thing constant. It returns True if the identifiers match exactly, and False otherwise. This operation is read-only and does not modify the state of the IRI object.

        :return: True if the object is the OWL Thing class, otherwise False.

        :rtype: bool
        """

        return self.to_uriref() == OWL.Thing

    def is_owl_nothing(self) -> bool:
        """
        Checks if the current IRI corresponds to the OWL Nothing entity, which represents the empty class in Web Ontology Language (OWL) semantics. The method performs this check by converting the object to a URI reference and comparing it against the standard `owl:Nothing` constant. It returns `True` if the identifiers match exactly, and `False` otherwise, without modifying the state of the object.

        :return: True if the entity represents the OWL Nothing concept, False otherwise.

        :rtype: bool
        """

        return self.to_uriref() == OWL.Nothing

    def __str__(self) -> str:
        """
        Returns the string representation of the IRI in its URI-encoded form. By delegating to the `to_uriref` method, this ensures that the returned string is a valid URI reference, typically involving the percent-encoding of any non-ASCII characters present in the IRI. This behavior makes the object compatible with contexts requiring standard ASCII URIs, such as HTTP headers or legacy systems, while the internal representation may retain the original Unicode characters.

        :return: The string representation of the URI reference.

        :rtype: str
        """

        return str(self.to_uriref())