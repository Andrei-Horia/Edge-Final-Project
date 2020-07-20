import socket

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind and listen to client
s.bind((socket.gethostname(), 9039))
s.listen(5)

names = []
name = ""
address = ""
index = 0
i = 0
I = 0

#Each name will have an unique address
Name = {
    name : address
}

#Each address will have an unique index so that I can correlate a name with an index
Index = {
    address : index
}

#Send and Receive messaje from a client
while True:
    socket_client,address = s.accept()
    print(str(address) + " joined")

    socket_client.sendall("What is your name".encode())

    #Receive a name
    name = socket_client.recv(1024)
    name = name.decode()

    #Search for the name in a list
    if not name in names:
    #If I don't find it then I will assigne to that specific name a unique address and then to that address a new index

        Name[name] = address
        name_address = Name[name]

        #Add the name to the list
        names.append(name)
        Index[name_address] = i

        #I save the index in a new variable I to never lose the counting since it will reset in case the name is found
        i += 1
        I = i

    else:
        #If I find it then the address would take the value of the stored address and the index would take the value of the stored index
        address = Name[name]

        i = Index[address] + 1

    #I want to print this information in the file (the name of the speaker, the address, and its index)
    print(address)
    print(name, i)
    i = I

    #Check with the client
    socket_client.sendall("Welcome to the server ".encode() + name.encode())

    while True:

        #Receive any message from client
        data = socket_client.recv(1024)

        #Exit command
        if data.decode() == "Exit":
            break

        #Send data back to client
        socket_client.sendall(data)

        #Print data
        data = data.decode()
        print(data)

    #Close client socket
    socket_client.close()

