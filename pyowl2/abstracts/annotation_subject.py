from __future__ import annotations

import abc

from pyowl2.abstracts.object import OWLObject


class OWLAnnotationSubject(OWLObject, abc.ABC, metaclass=abc.ABCMeta):
    """
    Represents the entity to which an annotation is applied within the Web Ontology Language (OWL) framework, acting as a polymorphic abstraction for Internationalized Resource Identifiers (IRIs), anonymous individuals, and literals. This abstract base class enforces a comparison strategy where equality and ordering are determined solely by the string representation of the subject's underlying value, rather than by object identity or type. It is designed to be subclassed by specific entity types that define the `value` attribute, ensuring consistent string conversion and hashing behavior across different annotation targets.
    """

    __slots__ = ()

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the annotation subject by delegating to the string conversion of the underlying `value` attribute. This method is invoked implicitly by the `str()` built-in function and during string formatting operations, providing a direct textual representation of the entity being annotated. The behavior depends entirely on the type of the wrapped value, and no side effects occur during the conversion process.

        :return: The string representation of the object's value.

        :rtype: str
        """

        return str(self.value)