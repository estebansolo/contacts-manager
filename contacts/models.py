import uuid
import sqlite3
from utilities.database import SqliteDriver


class ContactsModel(SqliteDriver):
    def __init__(self):
        self.table = "contacts"
        super().__init__(self.table)

    def list_contacts(self):
        return self.get_all_records()

    def insert_contact(self, contact):
        keys = SqliteDriver.get_insert_keys(contact)
        values = SqliteDriver.get_insert_values(contact)
        return self.insert_row(keys, values)

    def get_contact(self, cid):
        return self.get_record_by_id(cid)

    def update_contact(self, cid, contact):
        return self.update_record(cid, contact)

    def get_schema(self):
        return [
            "name",
            "lastname",
            "phone",
            "email",
        ]

