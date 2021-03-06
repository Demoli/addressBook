from Contact.Entry import Entry
from Contact.Index import Index
from Contact.Db import Db
from operator import itemgetter

class AddressBook():
    data_path = './data/'

    def __init__(self):
        self.db = Db()
        self.index = Index()
        self.reindex()
        self.entries = []

    def add_entry(self, **kwargs):
        # properties = [
        #     'name', 'telephone'
        # ]
        # values = {}
        # for prop in properties:
        #     values[prop] = input(prop.title())

        contact = Entry(**kwargs)
        self.db.save(contact)
        self.entries.append(contact)
        self.index.add_entry(contact)
        pass

    def save_entry(self, entry):
        self.db.save(entry);
        self.reindex()

    def search(self, term):
        term = term.lower()
        results = self.index.search(term)

        entries = []
        if len(results):
            for index in results:
                entries.append(self.__load_entry(index['_id']))

        return self.__sort_entries(entries)

    def reindex(self):
        index_data = []
        rows = self.db.get_all()
        for row in rows:
            data = {}
            for key in row.keys():
                data[key] = row[key]
            index_data.append(data)

        if(len(index_data)):
            self.index.reindex(index_data)

    def get_entry(self, id):
        return self.__load_entry(id);

    def get_entries(self):
        entries = [];
        for id in self.index.get_entries():
            entry = self.__load_entry(id)
            if(entry.get_id()):
                entries.append(entry)

        return self.__sort_entries(entries)

    def __sort_entries(self, entries):
        entries.sort(key=lambda x: x.get_id())
        return entries

    def __load_entry(self, id):
        entry = Entry()
        self.db.load(entry, id)
        return entry
