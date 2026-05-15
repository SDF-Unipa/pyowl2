import unittest

from pyowl2 import (
    IRI,
    OWLClass,
    OWLDeclaration,
    OWLDisjointClasses,
    OWLDisjointUnion,
    OWLEquivalentClasses,
    OWLSubClassOf,
)
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, roundtrip


class TestClassAxioms(unittest.TestCase):

    def test_subclass_of(self):
        person = OWLClass(IRI(NS, "Person"))
        animal = OWLClass(IRI(NS, "Animal"))
        axiom = OWLSubClassOf(person, animal)
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(animal)],
            AxiomsType.SUBCLASSES,
        )
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any(isinstance(r, OWLSubClassOf) for r in results))

    def test_equivalent_classes(self):
        human = OWLClass(IRI(NS, "Human"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLEquivalentClasses([human, person])
        results = roundtrip(
            [axiom, OWLDeclaration(human), OWLDeclaration(person)],
            AxiomsType.EQUIVALENT_CLASSES,
        )
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any(isinstance(r, OWLEquivalentClasses) for r in results))

    def test_disjoint_classes(self):
        cat = OWLClass(IRI(NS, "Cat"))
        dog = OWLClass(IRI(NS, "Dog"))
        axiom = OWLDisjointClasses([cat, dog])
        results = roundtrip(
            [axiom, OWLDeclaration(cat), OWLDeclaration(dog)],
            AxiomsType.DISJOINT_CLASSES,
        )
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any(isinstance(r, OWLDisjointClasses) for r in results))

    @unittest.expectedFailure
    def test_disjoint_union(self):
        """OWLDisjointUnion getter returns empty."""
        animal = OWLClass(IRI(NS, "Animal"))
        cat = OWLClass(IRI(NS, "Cat"))
        dog = OWLClass(IRI(NS, "Dog"))
        axiom = OWLDisjointUnion(animal, [cat, dog])
        results = roundtrip(
            [axiom, OWLDeclaration(animal), OWLDeclaration(cat), OWLDeclaration(dog)],
            AxiomsType.DISJOINT_UNIONS,
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
