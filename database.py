import os
import sqlite3

class SimpleDataBase:

    def __init__(self, db_name, schema_path):
        self._db_name = db_name
        self._schema_path = schema_path

    def connect_db(self):
        if self.db_is_new():
            with sqlite3.connect(self._db_name) as conn:
                schema = self.create_schema()
                print(schema)
                conn.executescript(schema)
        else:
            conn = sqlite3.connect(self._db_name)
        return conn

    def create_schema(self):
        with open(self._schema_path) as f:
            schema = f.read()
        return schema

    def db_is_new(self):
        return not os.path.exists(self._db_name)


