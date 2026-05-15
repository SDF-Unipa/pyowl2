import unittest

from rdflib import XSD, Literal

from pyowl2 import (
    IRI,
    OWLDataComplementOf,
    OWLDataIntersectionOf,
    OWLDataOneOf,
    OWLDatatype,
    OWLDatatypeDefinition,
    OWLDatatypeRestriction,
    OWLDataUnionOf,
    OWLDeclaration,
)
from pyowl2.data_range.datatype_restriction import OWLFacet, OWLFacetTypes
from pyowl2.getter.rdf_xml_getter import AxiomsType
from pyowl2.literal.literal import OWLTypedLiteral

from .helpers import NS, XSD_NS, roundtrip


class TestDataRanges(unittest.TestCase):

    @unittest.expectedFailure
    def test_data_complement_of(self):
        """OWLDataComplementOf getter not implemented (logs warning)."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataComplementOf(integer_dt)
        results = roundtrip([axiom], AxiomsType.DATA_COMPLEMENT_OF)
        self.assertGreaterEqual(len(results), 1)

    @unittest.expectedFailure
    def test_data_intersection_of(self):
        """OWLDataIntersectionOf requires list of OWLDataRange, not OWLDatatype."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataIntersectionOf([integer_dt])
        results = roundtrip([axiom], AxiomsType.DATA_INTERSECTION_OF)
        self.assertGreaterEqual(len(results), 1)

    @unittest.expectedFailure
    def test_data_union_of(self):
        """OWLDataUnionOf requires list of OWLDataRange, not OWLDatatype."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDataUnionOf([integer_dt])
        results = roundtrip([axiom], AxiomsType.DATA_UNION_OF)
        self.assertGreaterEqual(len(results), 1)

    def test_data_one_of(self):
        axiom = OWLDataOneOf([Literal(1), Literal(2)])
        results = roundtrip([axiom], AxiomsType.DATA_ONE_OF)
        self.assertGreaterEqual(len(results), 1)

    @unittest.expectedFailure
    def test_datatype_restriction(self):
        """OWLDatatypeRestriction mapper: facet URI not converted to rdflib term."""
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        facet = OWLFacet(OWLFacetTypes.MIN_INCLUSIVE, OWLTypedLiteral(0, integer_dt))
        axiom = OWLDatatypeRestriction(integer_dt, [facet])
        results = roundtrip([axiom], AxiomsType.DATATYPE_RESTRICTIONS)
        self.assertGreaterEqual(len(results), 1)

    @unittest.expectedFailure
    def test_datatype_definition(self):
        """OWLDatatypeDefinition getter returns empty."""
        my_int = OWLDatatype(IRI(NS, "myInt"))
        integer_dt = OWLDatatype(IRI(XSD_NS, XSD.integer))
        axiom = OWLDatatypeDefinition(my_int, integer_dt)
        results = roundtrip(
            [axiom, OWLDeclaration(my_int)], AxiomsType.DATATYPE_DEFINITION
        )
        self.assertGreaterEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
