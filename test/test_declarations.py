import unittest


from pyowl2 import (
    IRI,
    OWLAnnotationProperty,
    OWLClass,
    OWLDatatype,
    OWLDeclaration,
    OWLNamedIndividual,
)
from pyowl2.expressions.data_property import OWLDataProperty as DataPropertyExpr
from pyowl2.expressions.object_property import OWLObjectProperty as ObjectPropertyExpr
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, roundtrip


class TestDeclarations(unittest.TestCase):

    def test_entity_declarations(self):
        person = OWLClass(IRI(NS, "Person"))
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        name = DataPropertyExpr(IRI(NS, "name"))
        age = OWLDatatype(IRI(NS, "age"))
        label = OWLAnnotationProperty(IRI(NS, "label"))
        john = OWLNamedIndividual(IRI(NS, "John"))

        axioms = [
            OWLDeclaration(person),
            OWLDeclaration(has_pet),
            OWLDeclaration(name),
            OWLDeclaration(age),
            OWLDeclaration(label),
            OWLDeclaration(john),
        ]

        results = roundtrip(axioms, AxiomsType.DECLARATIONS)
        self.assertGreaterEqual(len(results), len(axioms))
        result_strs = {str(r) for r in results}
        for a in axioms:
            self.assertIn(str(a), result_strs, f"Missing declaration: {a}")

    def test_declaration_class_entities(self):
        person = OWLClass(IRI(NS, "Person"))
        axioms = [OWLDeclaration(person)]
        results = roundtrip(axioms, AxiomsType.CLASSES)
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any("Person" in str(c) for c in results))

    def test_declaration_object_property_entities(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        axioms = [OWLDeclaration(has_pet)]
        results = roundtrip(axioms, AxiomsType.OBJECT_PROPERTIES)
        self.assertGreaterEqual(len(results), 1)
        self.assertTrue(any("hasPet" in str(p) for p in results))


if __name__ == "__main__":
    unittest.main()
