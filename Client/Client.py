import socket
from Server import MainServer
__author__ = 'Sudhanshu'

class Client:
    clientPortNumber = None

    def __init__(self,portnumber):
        print("Creating a Client")
        Client.clientPortNumber = portnumber
        print("The port number given to Client is: "+str(Client.clientPortNumber))

    def createClient(self):
        socketObj = socket.socket()
        hostname = "localhost"
        print("The server port number connecting to is: "+str(7734))
        socketObj.connect((hostname, 7734))
        print socketObj.recv(1024)

