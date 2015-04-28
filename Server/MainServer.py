import thread

__author__ = 'Sudhanshu'

import socket

def handlenewclient(clientSocket, clientAddress):
        print("Received connection from Client address "+clientAddress)
        clientSocket.send("Thank you for connecting")


class MainServer:
    serverPortNumber = 0

    def __init__(self, socketport):
        MainServer.serverPortNumber = socketport
        print("Creating object and assigning socketport: ")
        print(self.serverPortNumber)


    def createServerSocket(self):
        socketOBj = socket.socket()
        hostName = "localhost"
        socketOBj.bind((hostName, int(MainServer.serverPortNumber)))
        socketOBj.listen(1)

        while True:
            clientSocket, clientAddress = socketOBj.accept()
            if (clientSocket and clientAddress):
                print("Connection made")
            else:
                print("Connection not made")
            thread.start_new_thread(handlenewclient, clientSocket, clientAddress)


print("Trying to instantiate server")
obj = MainServer(12345)
obj.createServerSocket()
