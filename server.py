import socket
#from dotenv import load_dotenv

ServerSocket = socket.socket()  # create socket
host = '127.0.0.1'
port = 1234
  def connect():
    try:
        ServerSocket.bind((host, port))  # create tcp socket
    except socket.error as e:  # return errors related to socket or address semantics
        print(str(e))
    print('Waiting for a Connection..')
    ServerSocket.listen(5)  # wait for a connection

clients = []

def clients_connection(socket1, socket2):
    socket1.send(str.encode('you are the attacker', encoding='ascii'))  # assign roles
    socket2.send(str.encode('you are the defender', encoding='ascii'))
    hostname = socket1.getpeername()  # get the attacker address
    data = socket1.recv(1024)  # wait and receive data from the attack max 2048 bytes
    if data.decode() == "no":
        socket1.close()
        socket2.close()
        clients[0].pop()
    else:
     reply_origin = hostname[0] + ':' + str(hostname[1]) + ' says ' + data.decode('ascii')  # create a reply
     reply = data
     print(reply_origin)
     socket2.sendall(data)  # send the reply to the defender



while True:
    if len(clients) < 2:  # we want only 2 players so 2 connections and 2 clients in the array
        Client, address = ServerSocket.accept()  # accept connection and assign variables
        print('Connected to: ' + address[0] + ':' + str(address[1]))  # tells us which socket is connected now
        Client.send(str.encode('Welcome to the Server \nwaiting for the other player'))  # send welcome message
        clients.append(Client)  # add the connection to the array to access it later

    else:
        clients_connection(clients[0], clients[1])  # go to  game
        clients_connection(clients[1], clients[0])  # simple method to switch turns for now
