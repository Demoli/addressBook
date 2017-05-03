from Contact.Entry import Entry
from Contact.Index import Index
from Contact.Db import Db
import uuid
import os
import glob

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

    def search(self, term):
        term = term.lower()
        results = self.index.search(term)

        entries = []
        if len(results):
            for index in results:
                entries.append(self.__load_entry(index['_id']))
        return entries

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

    def get_entries(self):
        entries = [];
        for id in self.index.get_entries():
            entry = self.__load_entry(id)
            if(entry.get_id()):
                entries.append(entry)

        return entries

    def __load_entry(self, id):
        entry = Entry()
        self.db.load(entry, id)
        return entry
