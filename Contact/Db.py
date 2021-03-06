import sqlite3


class Db():
    def __init__(self):
        self.conn = sqlite3.connect('./data/address-book.db')
        self.conn.row_factory = sqlite3.Row
        self.create_entry_table()

    def create_entry_table(self):
        query = """CREATE TABLE IF NOT EXISTS entry (
            id INTEGER PRIMARY KEY,
            name TEXT,
            telephone TEXT
            )
        """
        self.conn.execute(query)

    def save(self, entry):
        if(entry.get_id()):
            result = self.update(entry)
        else:
            result = self.insert(entry)
        return result;

    def insert(self, entry):
        query = """INSERT INTO entry (id, name, telephone) VALUES(null, ?,?)
                """
        result = self.conn.execute(query, [entry.get_name(), entry.get_telephone()])
        self.conn.commit()
        entry.set_id(result.lastrowid)
        return result

    def update(self, entry):
        query = """UPDATE entry set
                    name = ?,
                    telephone = ?
                    WHERE ID = ?
                """
        result = self.conn.execute(query, [entry.get_name(), entry.get_telephone(), entry.get_id()])
        self.conn.commit()
        return result

    def load(self, entry, id):
        query = """select * from entry where id = ?
        """
        result = self.conn.execute(query, (id,))
        data = result.fetchone()
        if (data is not None):
            data = dict(zip(data.keys(), data))
            entry.set_data(**data)

        return entry;

    def get_all(self):
        query = "select * from entry"
        return self.conn.execute(query).fetchall()
