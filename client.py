import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conect to server
s.connect((socket.gethostname(), 9039))

#Type Name

#Initial Data
data = s.recv(1024)
data = data.decode()
print(data)

#Send data to response
s.sendall(input().encode())

#Receive intial data
data = s.recv(1024)
data = data.decode()
print(data)

#Send and receive data
while True:

    #Send data
    msj = input()
    s.sendall(msj.encode())

    #Exit client command
    if msj == "Exit":
        print("Type any message to confirm...")

    #Exit server command
    if msj == "EXIT":
        print("Are you sure about this?")

    #Receive writen message
    data = s.recv(1024)
    print(data.decode())