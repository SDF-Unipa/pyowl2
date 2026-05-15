import unittest

from rdflib import XSD, Literal

from pyowl2 import (
    IRI,
    OWLAnnotation,
    OWLAnnotationAssertion,
    OWLAnnotationProperty,
    OWLAnnotationPropertyDomain,
    OWLAnnotationPropertyRange,
    OWLClass,
    OWLDatatype,
    OWLDeclaration,
    OWLOntology,
    OWLSubAnnotationPropertyOf,
)
from pyowl2.getter.rdf_xml_getter import AxiomsType

from .helpers import NS, REF, XSD_NS, roundtrip


class TestAnnotations(unittest.TestCase):

    def test_annotation_assertion(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLAnnotationAssertion(person.iri, label, Literal("A person"))
        results = roundtrip(
            [axiom, OWLDeclaration(person), OWLDeclaration(label)],
            AxiomsType.ANNOTATIONS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_annotation_property_domain(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        person = OWLClass(IRI(NS, "Person"))
        axiom = OWLAnnotationPropertyDomain(label, person)
        results = roundtrip(
            [axiom, OWLDeclaration(label), OWLDeclaration(person)],
            AxiomsType.ANNOTATION_PROPERTY_DOMAINS,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_annotation_property_range(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        axiom = OWLAnnotationPropertyRange(label, OWLDatatype(IRI(XSD_NS, XSD.string)))
        results = roundtrip(
            [axiom, OWLDeclaration(label)],
            AxiomsType.ANNOTATION_PROPERTY_RANGES,
        )
        self.assertGreaterEqual(len(results), 1)

    def test_sub_annotation_property(self):
        label = OWLAnnotationProperty(IRI(NS, "label"))
        display_name = OWLAnnotationProperty(IRI(NS, "displayName"))
        axiom = OWLSubAnnotationPropertyOf(display_name, label)
        results = roundtrip(
            [axiom, OWLDeclaration(label), OWLDeclaration(display_name)],
            AxiomsType.SUB_ANNOTATION_PROPERTIES,
        )
        self.assertGreaterEqual(len(results), 1)

    @unittest.expectedFailure
    def test_ontology_annotations(self):
        """OWLOntology annotations getter returns empty."""
        import os
        import tempfile

        label = OWLAnnotationProperty(IRI(NS, "label"))
        annotation = OWLAnnotation(label, Literal("Test Ontology"))
        onto = OWLOntology(REF)
        onto.add_annotation(annotation)
        tmp_dir = tempfile.mkdtemp()
        filepath = os.path.join(tmp_dir, "test.owl")
        onto.save(filepath)

        onto2 = OWLOntology(REF, filepath)
        annotations = onto2.get_axioms(AxiomsType.ANNOTATIONS)
        os.unlink(filepath)
        os.rmdir(tmp_dir)

        self.assertGreaterEqual(len(annotations), 1)


if __name__ == "__main__":
    unittest.main()
