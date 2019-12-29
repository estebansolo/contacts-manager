import click
from utilities import decorators
from contacts.controller import ContactsController


@click.group()
def cli():
    """ Manage my directory """
    pass


@cli.command(name="list")
@decorators.title
def list_contacts():
    """ Show my contact list """
    contact_list = ContactsController().list_contacts()

    click.echo("ID | FULL NAME | EMAIL | PHONE")
    for contact in contact_list:
        contact["id"] = "{:02d}".format(contact["id"])
        click.echo("{id} | {name} {lastname} | {email} | {phone}".format(**contact))


@cli.command(name="create", help="Create a new contact into my directory")
@click.option("-n", "--name", type=str, prompt=True, help="The contact name")
@click.option("-l", "--lastname", type=str, prompt=True, help="The contact lastname")
@click.option("-e", "--email", type=str, prompt=True, help="The contact email")
@click.option("-p", "--phone", type=str, prompt=True, help="The contact phone")
@decorators.title
def create_contact(name, lastname, email, phone):
    contacts_ctrl = ContactsController()
    insertion_id = contacts_ctrl.create_contact(name, lastname, email, phone)
    if isinstance(insertion_id, int):
        click.echo(f"Contact was inserted with id: {insertion_id}")
    else:
        click.secho("There was a problem trying to insert the contact", fg="red")


@cli.command(name="delete")
@click.argument("cid", required=True, type=int)
@decorators.title
def delete_contact(cid):
    """ Update a contact by id """
    contacts_ctrl = ContactsController()
    contact = contacts_ctrl.get_contact(cid)
    if not contact:
        click.echo("Contact was not found".center(50))
    else:
        click.confirm(
            f"Are you sure you want to delete: {contact['name']} {contact['lastname']}?",
            abort=True,
        )

        print("Yes")


@cli.command(name="update")
@click.argument("cid", required=True, type=int)
@decorators.title
def update_contact(cid):
    """ Update a contact by id """

    contacts_ctrl = ContactsController()
    contact = contacts_ctrl.get_contact(cid)
    if not contact:
        click.echo("Contact was not found".center(50))
    else:
        click.confirm(
            f"Would you like to update contact: {contact['name']}?", abort=True
        )

        data_contact = contacts_ctrl.ask_for_values(contact)
        updated = contacts_ctrl.update_contact(cid, data_contact)
        if updated:
            click.echo(f"Contact with id {cid} was updated successfully")
        else:
            click.secho("There was a problem trying to update the contact", fg="red")


if __name__ == "__main__":
    cli()

