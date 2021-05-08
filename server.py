import socket
import os
from dotenv import load_dotenv

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


def clients_connection(socket1, socket2):
    socket1.send(str.encode('you are the attacker'))
    socket2.send(str.encode('you are the def'))
    while True:
        data = socket1.recv(2048)
        reply = address[0] + ':' + str(address[1]) + ' says ' + data.decode('utf-8')
        print(reply)
        if not data:
            break
        socket2.sendall(str.encode(reply))
    socket1.close()
    socket2.close()


clients = []
while True:

    if len(clients) < 2:
        Client, address = ServerSocket.accept()
        print(Client)
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        Client.send(str.encode('Welcome to the Server \nwaiting fo the other player'))
        clients.append(Client)

    else:
        clients_connection(clients[0], clients[1])

ServerSocket.close()
