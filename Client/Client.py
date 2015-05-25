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
        socketObj.bind(('', Client.clientPortNumber))
        hostname = "localhost"
        print("Hostname for client is: "+str(hostname))
        print("Portnumber for client is: "+str(Client.clientPortNumber))
        print("The server port number connecting to is: "+str(7734))
        socketObj.connect((hostname, 7734))
        if socketObj.recv(1024) == 'Connected':
            print("Options for host "+str(hostname)+" :")
            print("1. ADD")
            print("2. LOOK UP")
            print("3. LIST ALL")

            choice = int(raw_input())
            if choice == 1:
                numberOFRFC = int(raw_input("How many RFC's do you want to enter: "))
                for item in range(numberOFRFC):
                    rfcNumber = int(raw_input("Enter RFC number: "))
                    rfcTitle = raw_input("Enter RFC Title: ")
                    print("Added RFC Number: "+str(rfcNumber)+" with Title: "+str(rfcTitle))
            elif choice == 2:
                pass
            elif choice == 3:
                pass


