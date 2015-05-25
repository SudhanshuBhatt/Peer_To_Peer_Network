from Server import MainServer
from Client import Client
__author__ = 'Sudhanshu'

print("Trying to instantiate Clients")
port = int(raw_input("Enter the server port number for the client: "))
client = Client.Client(port)
client.createClient()
