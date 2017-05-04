from elasticsearch import Elasticsearch


class Index():
    es_index_name = 'address-book'
    es_doc_type = 'contact'

    def __init__(self):
        self.index = [];
        self.es = Elasticsearch()

    def add_entry(self, entry):
        try:
            result = self.es.index(self.es_index_name, self.es_doc_type, entry.get_data(), str(entry.get_id()))
        except Exception as err:
            pass

    def reindex(self, data):
        for id in self.get_entries():
            self.es.delete(self.es_index_name, self.es_doc_type, id)

        try:
            for doc in data:
                self.es.index(self.es_index_name, self.es_doc_type, doc, str(doc['id']))
        except Exception as err:
            pass

    def search(self, term):
        body = {
            "query": {
                "query_string": {
                    "query": "*{}*".format(term),
                    "fields": ["name", "telephone"]
                }
            }
        }

        try:
            result = self.es.search(self.es_index_name, self.es_doc_type, body)
            hits = result['hits']['hits']
            return hits
        except Exception as err:
            pass

    def get_entries(self):
        ids = []
        result = self.es.search(self.es_index_name, self.es_doc_type, {'size': 100, "query": {"match_all": {}}})
        for result in result['hits']['hits']:
            ids.append(result['_id'])

        return ids
