import socket

ServerSocket = socket.socket()  # create socket
host = '127.0.0.1'
port = 1234


def connect(host, port):
    try:
        ServerSocket.bind((host, port))  # create tcp socket
    except socket.error as e:  # return errors related to socket or address semantics
        print(str(e))

    print('Waiting for a Connection..')
    ServerSocket.listen(5)  # wait for a connection


clients = []


def clients_connection(socket1, socket2):
    #insert initial time
    socket1.send(str.encode('you are the attacker', encoding='ascii'))  # assign roles
    socket2.send(str.encode('you are the defender', encoding='ascii'))
    hostname = socket1.getpeername()  # get the attacker address
    data = socket1.recv(1024)  # wait and receive data from the attack max 1024 bytes
    #time when attack is received
    hostname2 = socket1.getpeername()  # get the defender address
    reply_origin = hostname[0] + ':' + str(hostname[1]) + ' says ' + data.decode('ascii')  # create a reply
    print(reply_origin)
    socket2.sendall(data)  # send the reply to the defender
    data2 = socket2.recv(1024)  # see if the defence failed or not
    #time when defence failed or or successful is received
    reply_origin = hostname2[0] + ':' + str(hostname2[1]) + ' says ' + data2.decode('ascii')  # create a reply
    print(reply_origin)
    socket1.sendall(data2)  # send the response to the attacker


def game():
    while True:
        if len(clients) < 2:  # we want only 2 players so 2 connections and 2 clients in the array
            Client, address = ServerSocket.accept()  # accept connection and assign variables
            print('Connected to: ' + address[0] + ':' + str(address[1]))  # tells us which socket is connected now
            Client.send(str.encode('Welcome to the Server \nwaiting for the other player'))  # send welcome message
            clients.append(Client)  # add the connection to the array to access it later

        else:
            clients_connection(clients[0], clients[1])  # go to  game
            clients_connection(clients[1], clients[0])  # simple method to switch turns for now
            clients_connection(clients[0], clients[1])
            break


def check_score(socket1, socket2):
    socket1.send(str.encode('calculate score', encoding='ascii'))
    score_1 = socket1.recv(1024)
    socket2.send(str.encode('calculate score', encoding='ascii'))
    score_2 = socket2.recv(1024)
    score1 = int(score_1.decode('ascii'))
    score2 = int(score_2.decode('ascii'))
    if score1 < score2:
        socket1.send(str.encode('you win', encoding='ascii'))
        socket2.send(str.encode('you lose', encoding='ascii'))
    else:
        socket2.send(str.encode('you win', encoding='ascii'))
        socket1.send(str.encode('you lose', encoding='ascii'))
    socket1.close()
    socket2.close()


choice = 'yes'
while choice != 'no':
    connect(host, port)
    game()
    check_score(clients[0], clients[1])
    choice = input('do you want to restart type no if you want to stop')
