import sqlite3
from abc import ABCMeta, abstractmethod


class SqliteDriver(metaclass=ABCMeta):
    def __init__(self, table):
        self.table = table
        self.conn = sqlite3.connect("database.db")
        self.create_table()

    @abstractmethod
    def get_schema(self):
        pass

    def create_table(self):
        schema = self.get_schema()
        schema_values = ",".join(schema)

        cursor = self.conn.cursor()
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table} (id INTEGER PRIMARY KEY AUTOINCREMENT, {schema_values})"
        )
        self.conn.commit()

    def insert_row(self, keys, values):
        cursor = self.conn.cursor()
        query = cursor.execute(f"INSERT INTO {self.table}({keys}) VALUES({values})")

        self.conn.commit()
        return query.lastrowid

    def get_all_records(self):
        schema = self.get_schema()
        schema.insert(0, "id")

        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        rows = cursor.fetchall()
        return [dict(zip(schema, row)) for row in rows]

    def get_record_by_id(self, cid):
        schema = self.get_schema()
        schema.insert(0, "id")

        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE id = {cid}")
        row = cursor.fetchone()
        if row:
            return dict(zip(schema, row))

        return {}

    def update_record(self, cid, data_update):
        sets = SqliteDriver.get_update_values(data_update)
        cursor = self.conn.cursor()
        query = cursor.execute(f"UPDATE {self.table} SET {sets} WHERE id = {cid}")

        self.conn.commit()
        return query.rowcount

    @staticmethod
    def get_insert_values(row):
        values = "', '".join(row.values())
        return "'{}'".format(values)

    @staticmethod
    def get_insert_keys(row):
        return ",".join(row.keys())

    @staticmethod
    def get_update_values(data):
        sets = []
        for key, value in data.items():
            sets.append(f"{key} = '{value}'")

        return ",".join(sets)
