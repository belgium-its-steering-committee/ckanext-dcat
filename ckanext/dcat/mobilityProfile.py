import rdflib
from rdflib.namespace import Namespace, RDF, SKOS
from rdflib import URIRef, BNode, Literal
from ckanext.dcat.profiles import EuropeanDCATAP2Profile, URIRefOrLiteral
from pprint import pprint

MOBILITYDCATAP = Namespace("https://w3id.org/mobilitydcat-ap")

namespaces = {
    'mobilitydcatap': MOBILITYDCATAP,
       'skos': SKOS,
}


class MobilityDCATAPProfile(EuropeanDCATAP2Profile):
    '''
    A RDF mobility extension for the DCAT application profile for data portals in Europe
    It requires the European DCAP-AP Profile V2.0.1 ('euro_dcat_ap_v2.0.1')
    '''

    def parse_dataset(self, dataset_dict, dataset_ref):
        print("PARSE self:: ", self.g)
        print("PARSE dataset_dict:: ")
        pprint(dataset_dict)
        print("PARSE dataset_ref:: ")
        pprint(dataset_ref)
        return super(MobilityDCATAPProfile, self).parse_dataset(dataset_dict, dataset_ref)
    
    def graph_from_dataset(self, dataset_dict, dataset_ref):
        print("GRAPH self:: ", self.g)
        print("GRAPH dataset_dict:: ")
        pprint(dataset_dict)
        print("GRAPH dataset_ref:: ")
        pprint(dataset_ref)
        
        g = self.g

        for preflix, namespace in namespaces.items():
            g.bind(preflix, namespace)
        
        #creeert hoofdclass
        #g.add((dataset_ref, RDF.type,MOBILITYDCATAP.location))
        
        #hoofdclass fields for mobilityDCATAT

        items =[
            ('network_coverage', MOBILITYDCATAP.networkCoverage, None, SKOS.Concept)
        ]

        self._add_triples_from_dict(dataset_dict, dataset_ref, items)

        
        super(MobilityDCATAPProfile, self).graph_from_dataset(dataset_dict, dataset_ref)
        return
