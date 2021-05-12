from ckan.logic import get_action
from ckanext.dcat.processors import RDFSerializer

# Serializing a single dataset

dataset = get_action('package_show')({}, {'id': 'sample-ds'})

serializer = RDFserializer()

dataset_ttl = serializer.serialize_dataset(dataset, _format='turtle')

print("---------------------dataset_ttl")
print(dataset_ttl)

# Serializing the whole catalog (or rather part of it)
#
# datasets = get_action('package_search')({}, {'q': '*:*', 'rows': 50})
#
# serializer = RDFserializer()
#
# catalog_xml = serializer.serialize_catalog({'title': 'My catalog'},
#                                            dataset_dicts=datasets,
#                                            _format='xml')

# Creating and RDFLib graph from a single dataset

dataset = get_action('package_show')({}, {'id': 'sample-ds'})

serializer = RDFserializer()

dataset_reference = serializer.graph_from_dataset(dataset)

print("---------------------dataset_reference")
print(dataset_reference)

# serializer.g now contains the full dataset graph, an RDFLib Graph class

