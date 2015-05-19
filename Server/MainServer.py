__author__ = 'Sudhanshu'
import thread
import socket
import os
from Database import Peers_List
from Database import Peer_Node
from Database import RFC_List
from Database import RFC_Node


def handlenewclient(clientSocket, clientAddress):
    print("Received connection from{0} with port number  {1} and adding this peer to Active Peers".format(
        str(clientAddress[0]), str(clientAddress[1])))
    # This method call is to add the peer to the list of active peers
    MainServer.addActivePeer(clientAddress[0], clientAddress[1])

    ## Opening and reading a file
    with open("C:\Users\Sudhanshu\PycharmProjects\PeerToPeerNetwork\FilesArchive\RFC_1.txt", "r+") as fileObj:
        clientSocket.send(fileObj.read())
        clientSocket.close()


class MainServer:
    serverPortNumber = 0
    peersList = Peers_List.Peers_List()
    rfcList = RFC_List.RFC_List()

    def __init__(self, socketport):
        MainServer.serverPortNumber = socketport
        print("Creating object and assigning socketport: ")
        print(self.serverPortNumber)


    def createServerSocket(self):
        socketOBj = socket.socket()
        hostName = 'localhost'
        socketOBj.bind((hostName, int(MainServer.serverPortNumber)))
        socketOBj.listen(1)

        while True:
            clientSocket, clientAddress = socketOBj.accept()
            if (clientSocket and clientAddress):
                print("Connection made")
            else:
                print("Connection not made")
            thread.start_new_thread(handlenewclient, (clientSocket, clientAddress))

    def getActivePeers(self):
        return self.peersList.listOfActivePeers

    def addActivePeer(self, hostname, serverport):
        newObject = Peer_Node.Peer_Node(hostname, serverport)
        self.peersList.listOfActivePeers.append(newObject)

    def addRFCForPeer(self, rfcnumber, rfctitle, rfchostname):
        newObject = RFC_Node.RFC_Node(rfcnumber, rfctitle, rfchostname)
        self.rfcList.listOfAvailableRfc.append(newObject)

    def getPeerForAnRFC(self, rfcnumber):
        for rfc in self.rfcList.listOfAvailableRfc:
            if rfc.rfcNumber == rfcnumber:
                return rfc.peerHostName
            else:
                return "Not Found"




