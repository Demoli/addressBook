class Entry():

    def __init__(self, **kwargs):
        self._id = None
        self._name = None
        self._telephone = None

        self.set_data(**kwargs)
        # if (len(data)):
        #     if 'id' in data:
        #         self._id = data['id']
        #
        #     self._name = data['name']
        #     self._telephone = data['telephone']

    def set_id(self, id):
        self._id = id
        return self

    def get_id(self):
        return self._id

    def set_name(self, name):
        self._name = name
        return self

    def get_name(self):
        return self._name

    def set_telephone(self, telephone):
        self._telephone = telephone
        return self

    def get_telephone(self):
        return self._telephone

    def get_data(self):
        return {
            "id": self.get_id(),
            'name': self.get_name(),
            'telephone': self.get_telephone()
        }

    def set_data(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self,'set_' + key)(value)
            except AttributeError as err:
                pass

