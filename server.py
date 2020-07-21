import socket

file = open("server.txt", "r+")

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind and listen to client
s.bind((socket.gethostname(), 9039))
s.listen(5)

#All varaibles are defined here
names = []
html_content = []
name = ""
address = ""
index = 0
i = 0
copy_i = 0
OK = 0

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

    #Open file all the times a client exits and another one joins
    file = open("server.txt", "r+")

    socket_client,address = s.accept()
    print(str(address) + " joined")

    socket_client.sendall("What is your name?".encode())

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
        copy_i = i
        #Check with the client
        socket_client.sendall("Welcome to the server ".encode() + name.encode())

    else:
        #If I find it then the address would take the value of the stored address and the index would take the value of the stored index
        address = Name[name]

        i = Index[address] + 1
        #Check with the client
        socket_client.sendall("Welcome back ".encode() + name.encode())

    #I want to print this information in the file (the name of the speaker, the address, and its index)
    print(address)
    print(name, i)

    html_content.append("<p>" + name + " " + str(address) + "(" + str(i) + "):" + "</p>" + "\n")

    I = i
    i = copy_i


    while True:

        #Receive any message from client
        data = socket_client.recv(1024)

        #Exit command
        if data.decode() == "Exit":
            break


        #End server command
        if data.decode() == "EXIT":
            OK=1
            break
        #Send data back to client
        socket_client.sendall(data)

        #Print data
        data = data.decode()

        #Create HTML Elements in a list
        text = "<p>" + data + "<\p>" +"\n"
        html_content.append(text)
        print(data)


    #Print text in a file(HTML Format)
    for text in html_content:
        print(text)
        file.write(text)
    file.close()

    #Close client socket
    socket_client.close()

    if OK == 1:
        s.close()

