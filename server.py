import socket
from dotenv import load_dotenv

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def clients_connection(socket1, socket2):
    socket1.send(str.encode('you are the attacker', encoding='ascii'))
    socket2.send(str.encode('you are the defender', encoding='ascii'))
    hostname = socket1.getpeername()
    data = socket1.recv(2048)
    reply = hostname[0] + ':' + str(hostname[1]) + ' says ' + data.decode('ascii')
    print(reply)
    socket2.sendall(str.encode(reply))


clients = []
while True:

    if len(clients) < 2:
        Client, address = ServerSocket.accept()
        print(Client)
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        Client.send(str.encode('Welcome to the Server \nwaiting for the other player'))
        clients.append(Client)

    else:
        clients_connection(clients[0], clients[1])
        clients_connection(clients[1], clients[0])
clients[0].close()
clients[1].close()
ServerSocket.close()
