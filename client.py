import socket
#hello world
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode('ascii'))
while True:
    Response = ClientSocket.recv(1024)
    print(Response.decode('ascii'))
    if Response.decode('ascii') != 'you are the attacker':
        Response = ClientSocket.recv(1024)
        print(Response)
        print(Response.decode('ascii'))
    else:
        Input = input('Say Something: ')
        ClientSocket.send(Input.encode(encoding='ascii'))

ClientSocket.close()
