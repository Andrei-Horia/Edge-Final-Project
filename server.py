import socket
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

file = open("server.txt", "r+")

#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Bind and listen to client
s.bind((socket.gethostname(), 9039))
s.listen(5)

#All varaibles are defined here
#List of names
names = []

#The list that will store each html element
html_content = []

#Name of the client
name = ""

#Address of the client
address = ""

#Index
index = 0

#Index of the client
i = 0

#Copy the i
copy_i = 0

#Verify EXIT command
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


    #Create HTML Content
    text = "<html>" + "\n" + "<title>Server-Client Connection</title>" + "\n" + "<body style='background-color:#ffd9b3; margin-left:40px; margin-top:30px'>" + "\n"
    file.write(text)

    #Create top HTML Content
    #First three things that will be print out the name, the index, and the address of the client who joined in

    text =  "<h1>Welcome to the Chat<h1>"
    file.write(text)

    html_content.append("<h2 style='color:black'>" + name + "</h2>" + "\n")
    html_content.append("<font size='0.5' style='color:grey'>" + str(address) + "(" + str(i) + "):" + "</font>")

    #Reassign the value of i(index) to the one where it was supposted to be
    #Basically, when somebody types an already existing name, the index will reset. We are not supposted to lose the counting
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
        text = "<h3 style='margin-left:20px; color:gray'>" + data + "</h3>" +"\n"
        html_content.append(text)
        print(data)


    #Print text in a file(HTML Format)
    for text in html_content:
        file.write(text)

    #Create HTML Content
    text = "</body>" + "\n" + "</html>"
    file.write(text)

    file.close()

    #Close client socket
    socket_client.close()

    if OK == 1:
        break

s.close()

