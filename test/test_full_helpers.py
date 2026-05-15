import os
import tempfile
import unittest

from rdflib import XSD

from pyowl2 import (
    IRI,
    OWLClass,
    OWLDatatype,
    OWLDeclaration,
    OWLFullClass,
    OWLFullDataProperty,
    OWLFullIndividual,
    OWLFullObjectProperty,
    OWLOntology,
)
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, REF, XSD_NS


class TestFullHelpers(unittest.TestCase):

    def test_full_class(self):
        person = OWLFullClass(IRI(NS, "Person"))
        animal = OWLFullClass(IRI(NS, "Animal"))
        person.is_subclass_of(animal.class_)

        onto = OWLOntology(REF)
        onto.add_axioms([person, animal])
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        classes = onto2.get_axioms(AxiomsType.CLASSES)
        subclasses = onto2.get_axioms(AxiomsType.SUBCLASSES)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(classes), 2)
        self.assertGreaterEqual(len(subclasses), 1)

    def test_full_object_property(self):
        person = OWLClass(IRI(NS, "Person"))
        has_pet = OWLFullObjectProperty(IRI(NS, "hasPet"), range=person, domain=person)

        onto = OWLOntology(REF)
        onto.add_axioms([OWLDeclaration(person), has_pet])
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        obj_props = onto2.get_axioms(AxiomsType.OBJECT_PROPERTIES)
        domains = onto2.get_axioms(AxiomsType.OBJECT_PROPERTY_DOMAIN)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(obj_props), 1)
        self.assertGreaterEqual(len(domains), 1)

    def test_full_data_property(self):
        person = OWLClass(IRI(NS, "Person"))
        has_name = OWLFullDataProperty(
            IRI(NS, "hasName"),
            domain=person,
            range=OWLDatatype(IRI(XSD_NS, XSD.string)),
        )

        onto = OWLOntology(REF)
        onto.add_axioms([OWLDeclaration(person), has_name])
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        data_props = onto2.get_axioms(AxiomsType.DATA_PROPERTIES)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(data_props), 1)

    def test_full_individual(self):
        person = OWLClass(IRI(NS, "Person"))
        john = OWLFullIndividual(IRI(NS, "John"))
        john.add_assertion(person)

        onto = OWLOntology(REF)
        onto.add_axioms([OWLDeclaration(person), john])
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        individuals = onto2.get_axioms(AxiomsType.INDIVIDUALS)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(individuals), 1)


if __name__ == "__main__":
    unittest.main()
