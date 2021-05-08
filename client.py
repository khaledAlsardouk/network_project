import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
while True:
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
    if Response.decode('utf-8') != 'you are the attacker':
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    else:
        Input = input('Say Something: ')
        ClientSocket.send(str.encode(Input))

ClientSocket.close()
