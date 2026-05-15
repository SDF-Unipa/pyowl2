import os
import tempfile

from rdflib import XSD, Namespace, URIRef

from pyowl2 import OWLOntology

REF = URIRef("http://example.org/test#")
NS = Namespace(REF)
XSD_NS = Namespace(XSD._NS)


def roundtrip(axioms, axiom_type, tmp_dir=None):
    """Write axioms, save, reload, read back via AxiomsType. Return results."""
    cleanup = False
    if tmp_dir is None:
        tmp_dir = tempfile.mkdtemp()
        cleanup = True
    onto = OWLOntology(REF)
    onto.add_axioms(axioms)
    filepath = os.path.join(tmp_dir, "test.owl")
    assert onto.save(filepath) is True
    onto2 = OWLOntology(REF, filepath)
    results = onto2.get_axioms(axiom_type)
    os.unlink(filepath)
    if cleanup:
        os.rmdir(tmp_dir)
    return results
