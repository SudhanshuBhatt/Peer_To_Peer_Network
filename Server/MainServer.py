__author__ = 'Sudhanshu'
import thread
import socket
from Database import Peers_List
from Database import Peer_Node
from Database import RFC_List
from Database import RFC_Node
from Database import Peer_RFC_Dictionary


class MainServer:
    serverPortNumber = 0
    peersList = Peers_List.Peers_List()
    rfcList = RFC_List.RFC_List()
    peerRfcDictObj = Peer_RFC_Dictionary.Peer_RFC_Dictionary()

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
            thread.start_new_thread(self.handlenewclient, (clientSocket, clientAddress))

    def handlenewclient(self, clientSocket, clientAddress):
        print("Received connection from {0} with port number  {1} and adding this peer to Active Peers".format(
            str(clientAddress[0]), str(clientAddress[1])))
        clientSocket.send('Connected')
        # This method call is to add the peer to the list of active peers
        self.addActivePeer(clientAddress[0], clientAddress[1])
        print("Getting list of all active peers")
        self.getActivePeers()

         # Opening and reading a file
        '''
        with open("C:\Users\Sudhanshu\PycharmProjects\PeerToPeerNetwork\FilesArchive\RFC_1.txt", "r+") as fileObj:
            clientSocket.send(fileObj.read())
            clientSocket.close()
        '''

    def getActivePeers(self):
        count = 1
        for peer in self.peerRfcDictObj.peer_dict.keys():
            print(str(count) + ") " + "Hostname: " + str(peer) + " PortNumber: " + str(
                self.peerRfcDictObj.peer_dict.get(peer).peerServerPortNumber))

    def addActivePeer(self, hostname, serverport):
        newObject = Peer_Node.Peer_Node(serverport)
        self.peerRfcDictObj.peer_dict[hostname] = newObject
        '''
        newObject = Peer_Node.Peer_Node(hostname, serverport)
        self.peersList.listOfActivePeers.append(newObject)
        '''

    def addRFCForPeer(self, rfcnumber, rfctitle, rfchostname):
        newObject = RFC_Node.RFC_Node(rfcnumber, rfctitle)
        self.peerRfcDictObj.rfc_dict[rfchostname] = newObject
        '''
        newObject = RFC_Node.RFC_Node(rfcnumber, rfctitle, rfchostname)
        self.rfcList.listOfAvailableRfc.append(newObject)
        '''

    def getPeerForAnRFC(self, rfcNumber):
        count = 1
        for rfcHost in self.peerRfcDictObj.rfc_dict.keys():
            if self.peerRfcDictObj.rfc_dict[rfcHost].rfcNumber == rfcNumber:
                print(count + ") " + self.peerRfcDictObj.rfc_dict[rfcHost].peerHostName)
            else:
                print("Not Found")
