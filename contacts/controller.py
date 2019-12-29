import click
from contacts.models import ContactsModel


class ContactsController:
    def __init__(self):
        self.table_name = ""
        self.model = ContactsModel()

    def list_contacts(self):
        return self.model.list_contacts()

    def create_contact(self, name, lastname, email, phone):
        contact = {"name": name, "lastname": lastname, "email": email, "phone": phone}
        return self.model.insert_contact(contact)

    def get_contact(self, cid):
        return self.model.get_contact(cid)

    def update_contact(self, cid, data_contact):
        return self.model.update_contact(cid, data_contact)

    def ask_for_values(self, contact):
        return {
            "name": click.prompt("What is the new name?", default=contact["name"]),
            "lastname": click.prompt(
                "What is the new lastname?", default=contact["lastname"]
            ),
            "email": click.prompt("What is the new email?", default=contact["email"]),
            "phone": click.prompt("What is the new phone?", default=contact["phone"]),
        }
