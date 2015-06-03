import socket
from Server import MainServer
from Database import Peer_RFC_Dictionary
from Database import RFC_Node
from Database import Peer_Node

__author__ = 'Sudhanshu'

class Client:
    clientPortNumber = None
    peerRfcDictObj = Peer_RFC_Dictionary.Peer_RFC_Dictionary()

    def __init__(self,portnumber):
        print("Creating a Client")
        Client.clientPortNumber = portnumber
        print("The port number given to Client is: "+str(Client.clientPortNumber))

    def createClient(self):
        socketObj = socket.socket()
        socketObj.bind(('', Client.clientPortNumber))
        hostname = "localhost"
        print("Hostname for client is: "+str(hostname))
        print("Portnumber for client is: "+str(Client.clientPortNumber))
        print("The server port number connecting to is: "+str(7734))
        socketObj.connect((hostname, 7734))
        if socketObj.recv(1024) == 'Connected':
            while True:
                print("Options for host "+str(hostname)+" :")
                print("1. ADD")
                print("2. LOOK UP")
                print("3. LIST ALL")
                print("4. EXIT")

                choice = int(raw_input())
                if choice == 1:
                    numberOFRFC = int(raw_input("How many RFC's do you want to enter: "))
                    for item in range(numberOFRFC):
                        rfcNumber = int(raw_input("Enter RFC number: "))
                        rfcTitle = raw_input("Enter RFC Title: ")
                        self.addRFCForPeer(rfcNumber, rfcTitle, hostname)
                        print("Added RFC Number: "+str(rfcNumber)+" with Title: "+str(rfcTitle))
                    break
                elif choice == 2:
                    toFindRfc = raw_input("Which RFC Number do you need to search: ")
                    self.getPeerForAnRFC(toFindRfc)
                elif choice == 3:
                    pass
                elif choice == 4:
                    break

    def addRFCForPeer(self, rfcnumber, rfctitle, rfchostname):
        newObject = RFC_Node.RFC_Node(rfcnumber, rfctitle)
        self.peerRfcDictObj.rfc_dict[rfchostname] = newObject

    def getPeerForAnRFC(self, rfcNumber):
        count = 1
        for rfcHost in self.peerRfcDictObj.rfc_dict.keys():
            if self.peerRfcDictObj.rfc_dict[rfcHost].rfcNumber == rfcNumber:
                print(count + ") " + self.peerRfcDictObj.rfc_dict[rfcHost].peerHostName)
            else:
                print("Not Found")
