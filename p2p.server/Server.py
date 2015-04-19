import thread

__author__ = 'Sudhanshu'

import socket


def handleNewClient(clientSocket, clientAddress):
    print("Received connection from client address "+clientAddress)
    clientSocket.send("Thank you for connecting")


class MainServer:
    serverPortNumber = None
    print("Creating main server")
    def __init__(self, socketport):
        self.serverPortNumber = socketport

    socketOBj = socket.socket()
    hostName = "localhost"
    socketOBj.bind(hostName, serverPortNumber)
    socketOBj.listen(1)

    while True:
        clientSocket, clientAddress = socketOBj.accept()
        thread.start_new_thread(handleNewClient(clientSocket, clientAddress))



