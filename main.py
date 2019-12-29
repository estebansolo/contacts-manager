import os
import sys
import csv
import click
from clients import commands as clients_commands

CLIENTS_TABLE = "clients.csv"

@click.group()
@click.pass_context
def cli(ctx):
  ctx.obj = {
    "clients_table": CLIENTS_TABLE
  }

cli.add_command(clients_commands.all)

"""
clients = []

CLIENT_SCHEMA = ["name", "company", "email", "position"]

def _initialize_clients_from_storage():
  global clients

  with open(CLIENTS_TABLE) as f:
    reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
    clients = [dict(row) for row in reader]

def _save_clients_to_storage():
  with open(CLIENTS_TABLE, "w") as f:
    writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
    writer.writerows(clients)

def create_client(client):
  global clients
  if client not in clients:
    clients.append(client)
  else:
    print("Client already is in the client's list")

def update_client(client_name, updated_client):
  global clients
  for key, client in enumerate(clients):
    if client["name"] == client_name:
      clients[key] = updated_client
      break
  else:
    print("Client is not in the client's list")

def delete_client(client_name):
  global clients
  for key, client in enumerate(clients):
    if client["name"] == client_name:
      del clients[key]
      break
  else:
    print("Client is not in the client's list")

def search_client(client_name):
  for client in clients:
    if client['name'] == client_name:
      return True
  return False

def list_clients():
  for uid, client in enumerate(clients):
    print("{uid} | {name} | {company} | {email} | {position}".format(uid=uid, **client))

def _print_welcome():
  print("WELCOME TO CLI-SALES")
  print("*" * 50)
  print("What would you like to do?")
  print("[C]reate client")
  print("[R]ead clients")
  print("[U]pdate client")
  print("[D]elete client")
  print("[S]earch client")

def _get_client_field(field_name, is_new=False):
  field = None
  while not field:
    new_value = "new " if is_new else ""
    field = input(f"What is the {new_value}client {field_name}? ").strip()
    if field.lower() == "exit":
      field = None
      break
  
  if not field:
    sys.exit()
  
  return field
"""

if __name__ == '__main__':
  """
  _initialize_clients_from_storage()
  _print_welcome()

  command = input().upper()
  if command == "C":
    client = {
      "name": _get_client_field("name"),
      "company": _get_client_field("company"),
      "email": _get_client_field("email"),
      "position": _get_client_field("position")
    }

    create_client(client)
  elif command == "D":
    client_name = _get_client_field("name")
    delete_client(client_name)
  elif command == "R":
    list_clients()
  elif command == "U":
    client_name = _get_client_field("name")
    
    client = {
      "name": _get_client_field("name", is_new=True),
      "company": _get_client_field("company", is_new=True),
      "email": _get_client_field("email", is_new=True),
      "position": _get_client_field("position", is_new=True)
    }

    update_client(client_name, client)
  elif command == "S":
    client_name = _get_client_field("name")
    found = search_client(client_name)
    if found:
      print("Client is in the client's list")
    else:
      print("The client {} is not in the client's list".format(client_name))
  else:
    print("Invalid Command")

  _save_clients_to_storage()
  """
  cli()