import unittest

from rdflib import XSD, Literal

from pyowl2 import (
    IRI,
    OWLClass,
    OWLDataAllValuesFrom,
    OWLDataExactCardinality,
    OWLDataHasValue,
    OWLDataMaxCardinality,
    OWLDataMinCardinality,
    OWLDataSomeValuesFrom,
    OWLDatatype,
    OWLDeclaration,
    OWLNamedIndividual,
    OWLObjectAllValuesFrom,
    OWLObjectComplementOf,
    OWLObjectExactCardinality,
    OWLObjectHasSelf,
    OWLObjectHasValue,
    OWLObjectIntersectionOf,
    OWLObjectMaxCardinality,
    OWLObjectMinCardinality,
    OWLObjectOneOf,
    OWLObjectSomeValuesFrom,
    OWLObjectUnionOf,
)
from pyowl2.expressions.data_property import OWLDataProperty as DataPropertyExpr
from pyowl2.expressions.object_property import OWLObjectProperty as ObjectPropertyExpr
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, XSD_NS, roundtrip


class TestObjectClassExpressions(unittest.TestCase):

    def test_object_intersection_of(self):
        person = OWLClass(IRI(NS, "Person"))
        employee = OWLClass(IRI(NS, "Employee"))
        axiom = OWLObjectIntersectionOf([person, employee])
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(employee)],
            AxiomsType.OBJECT_INTERSECTION_OF,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_union_of(self):
        cat = OWLClass(IRI(NS, "Cat"))
        dog = OWLClass(IRI(NS, "Dog"))
        axiom = OWLObjectUnionOf([cat, dog])
        results = roundtrip(
            [axiom, OWLDeclaration(cat), OWLDeclaration(dog)],
            AxiomsType.OBJECT_UNION_OF,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_complement_of(self):
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLObjectComplementOf(person)
        results = roundtrip(
            [axiom, OWLDeclaration(person)],
            AxiomsType.OBJECT_COMPLEMENT_OF,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_one_of(self):
        john = OWLNamedIndividual(IRI(NS, "John"))
        mary = OWLNamedIndividual(IRI(NS, "Mary"))
        axiom = OWLObjectOneOf([john, mary])
        results = roundtrip(
            [axiom, OWLDeclaration(john), OWLDeclaration(mary)],
            AxiomsType.OBJECTS_ONE_OF,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_some_values_from(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        animal = OWLClass(IRI(NS, "Animal"))
        axiom = OWLObjectSomeValuesFrom(has_pet, animal)
        results = roundtrip(
            [axiom, OWLDeclaration(has_pet), OWLDeclaration(animal)],
            AxiomsType.OBJECTS_SOME_VALUES_FROM,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_all_values_from(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        animal = OWLClass(IRI(NS, "Animal"))
        axiom = OWLObjectAllValuesFrom(has_pet, animal)
        results = roundtrip(
            [axiom, OWLDeclaration(has_pet), OWLDeclaration(animal)],
            AxiomsType.OBJECTS_ALL_VALUES_FROM,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_has_value(self):
        has_pet = ObjectPropertyExpr(IRI(NS, "hasPet"))
        fido = OWLNamedIndividual(IRI(NS, "Fido"))
        axiom = OWLObjectHasValue(has_pet, fido)
        results = roundtrip(
            [axiom, OWLDeclaration(has_pet), OWLDeclaration(fido)],
            AxiomsType.OBJECTS_HAS_VALUE,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_has_self(self):
        loves = ObjectPropertyExpr(IRI(NS, "loves"))
        axiom = OWLObjectHasSelf(loves)
        results = roundtrip(
            [axiom, OWLDeclaration(loves)],
            AxiomsType.OBJECTS_HAS_SELF,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_min_cardinality(self):
        has_child = ObjectPropertyExpr(IRI(NS, "hasChild"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLObjectMinCardinality(2, has_child, person)
        results = roundtrip(
            [axiom, OWLDeclaration(has_child), OWLDeclaration(person)],
            AxiomsType.OBJECTS_MIN_CARDINALITY,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_max_cardinality(self):
        has_child = ObjectPropertyExpr(IRI(NS, "hasChild"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLObjectMaxCardinality(3, has_child, person)
        results = roundtrip(
            [axiom, OWLDeclaration(has_child), OWLDeclaration(person)],
            AxiomsType.OBJECTS_MAX_CARDINALITY,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_object_exact_cardinality(self):
        has_child = ObjectPropertyExpr(IRI(NS, "hasChild"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLObjectExactCardinality(2, has_child, person)
        results = roundtrip(
            [axiom, OWLDeclaration(has_child), OWLDeclaration(person)],
            AxiomsType.OBJECTS_EXACT_CARDINALITY,
        )
        self.assertGreaterEqual(len(results), 1)


class TestDataClassExpressions(unittest.TestCase):

    def test_data_some_values_from(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataSomeValuesFrom([has_age], integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATA_SOME_VALUES_FROM,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_all_values_from(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataAllValuesFrom([has_age], integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATA_ALL_VALUES_FROM,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_has_value(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        axiom = OWLDataHasValue([has_age], Literal(25))
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATAS_HAS_VALUE,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_min_cardinality(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataMinCardinality(0, [has_age], integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATA_MIN_CARDINALITY,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_max_cardinality(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataMaxCardinality(1, [has_age], integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATA_MAX_CARDINALITY,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_data_exact_cardinality(self):
        has_age = DataPropertyExpr(IRI(NS, "hasAge"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataExactCardinality(1, [has_age], integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(has_age)],
            AxiomsType.DATA_EXACT_CARDINALITY,
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
