import socket
from Server import MainServer
__author__ = 'Sudhanshu'

class Client:
    clientPortNumber = None

    def __init__(self,portnumber):
        print("Creating a Client")
        Client.clientPortNumber = portnumber
        print("The port number given to Client is: "+str(Client.clientPortNumber))

    def createClient(self, portnumber):
        socketObj = socket.socket()
        hostname = "localhost"
        print("The server port number connecting to is: "+str(MainServer.serverPortNumber))
        socketObj.connect((hostname,MainServer.serverPortNumber))


obj = Client(4444)