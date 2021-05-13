from builtins import str
from ckanext.dcat.profiles import RDFProfile

from rdflib import URIRef, BNode, Literal
from rdflib.namespace import Namespace, RDF, RDFS

DCT = Namespace("http://purl.org/dc/terms/")


class DICEDCATProfile(RDFProfile):
    '''
    An RDF profile for the Swedish DCAT-AP recommendation for data portals

    It requires the European DCAT-AP profile (`euro_dcat_ap`)
    '''

    def parse_dataset(self, dataset_dict, dataset_ref):

        # Spatial label
        spatial = self._object(dataset_ref, DCT.spatial)
        if spatial:
            spatial_label = self.g.label(spatial)
            if spatial_label:
                dataset_dict['extras'].append({'key': 'spatial_text',
                                               'value': str(spatial_label)})

        return dataset_dict

    def graph_from_dataset(self, dataset_dict, dataset_ref):
        g = self.g
        print "-------------------------- main dataset_dict"
        print dataset_dict

        # g = self.g
        #
        # spatial_uri = self._get_dataset_value(dataset_dict, 'spatial_uri')
        # spatial_text = self._get_dataset_value(dataset_dict, 'spatial_text')
        #
        # if spatial_uri:
        #     spatial_ref = URIRef(spatial_uri)
        # else:
        #     spatial_ref = BNode()
        #
        # if spatial_text:
        #     g.add((dataset_ref, DCT.spatial, spatial_ref))
        #     g.add((spatial_ref, RDF.type, DCT.Location))
        #     g.add((spatial_ref, RDFS.label, Literal(spatial_text)))


o = DICEDCATProfile()
o.graph_from_dataset({'a': 1, 'b': 6}, None)