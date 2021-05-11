import socket
ClientSocket = socket.socket() #create socket
host = '127.0.0.1'  #local host ip for now
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port)) #connect socket to host on  a specific port
except socket.error as e: # return errors related to socket or address semantics
    print(str(e))

Response = ClientSocket.recv(1024) # wait and recieve data from server with max size 1024 bytes
print(Response.decode('ascii')) #decode and print message
while True:
    Response = ClientSocket.recv(1024)
    print(Response.decode('ascii'))
    if Response.decode('ascii') != 'you are the attacker': 
        Response = ClientSocket.recv(1024)
        print(Response)                                 #defender behavior
        print(Response.decode('ascii'))
    else:
        Input = input('Say Something: ')                        #attack behavior
        ClientSocket.send(Input.encode(encoding='ascii'))

ClientSocket.close()   #close connection
