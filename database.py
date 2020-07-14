import os
import sqlite3
from object_handler import ObjectHandler


class DataBase:

    def __init__(self, db_name, schema_path):
        self._db_name = db_name
        self._schema_path = schema_path

    def connect_db(self):
        with sqlite3.connect(self._db_name) as conn:
            if not self.schema_exists():
                schema = self.create_schema()
                conn.execute(schema)
        return conn

    def create_schema(self):
        with open(self._schema_path) as f:
            schema = f.read()
        return schema

    def schema_exists(self):
        return os.path.exists(self._schema_path)

    def get_table_col(self, conn, table_name):
        if DataBase.validate_table_name(conn, table_name):
            cur = conn.cursor()
            cur.execute('select * from {}'.format(table_name))
            table_cols = tuple(col[0] for col in cur.description)
            return table_cols
        raise Exception(sqlite3.OperationalError,
                        f"{table_name} is not a table name of current data base")

    @classmethod
    def validate_table_name(cls, conn, table_name):
        if isinstance(table_name, str):
            table_names = conn.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
            for name in table_names:
                if table_name == name[0]:
                    return True
        return False



    def get_matched_pair(self, table_cols, *stringed_attrs ):
        sorted_attrs = sorted(stringed_attrs, key=lambda col: table_cols.index(col))
        table_cols, attrs = tuple(pair[0], pair[1] for pair in zip(table_cols, sorted_attrs))

    def insert_data(self, obj, *stringed_attrs):
        validated = ObjectHandler.validate_attrs(obj, stringed_attrs)
        if validated:
            with self.connect_db() as conn:
                table_name = ObjectHandler.get_cls_name(obj)
                table_cols = self.get_table_col(conn, table_name)
                sorted_attrs = ObjectHandler.get_sorted_attrs(obj, stringed_attrs)
                cur = conn.cursor()
                cur.execute("""
                INSERT INTO 
                """)








"""def get_schema_attrs(self, schema, obj):
        schema_list = [word.strip() for word in schema]
        filtered_list = []
        obj_data = self.get_obj_data(obj)
        for string in schema_list:
            for word in string.split(' '):
                if word in obj_data.values():
                    filtered_list.append(word)
        return filtered_list"""

"""def get_obj_data(self, obj):
    table_name = type(obj).__name__.lower()
    table_attrs = tuple(k.lower() for k in vars(obj))
    table_data = {'table_name': table_name, 'table_attrs': table_attrs}
    return table_data"""