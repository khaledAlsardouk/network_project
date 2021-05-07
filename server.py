import socket
import os

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def welcome(connection):
    connection.send(str.encode('Welcome to the Servern \n waiting fo the other player'))


def clients_connection(socket1, socket2):
    socket1.send(str.encode('you are the attacker'))
    socket2.send(str.encode('you are the def'))
    while True:
        data = socket1.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        print(reply)
        if not data:
            break
        socket2.sendall(str.encode(reply))
    socket1.close()
    socket2.close()


arr = []
while True:

    if ThreadCount < 2:
        Client, address = ServerSocket.accept()
        print(Client)
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        welcome(Client)
        arr.append(Client)
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))

    else:
        clients_connection(arr[0], arr[1])

ServerSocket.close()
