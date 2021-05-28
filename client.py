import socket
import time
import encryption
import NRZ
import HammingCode

ClientSocket = socket.socket()  # create socket
host = '127.0.0.1'  # local host ip for now
port = 1234
score = 0
connection = True

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))  # connect socket to host on  a specific port
except socket.error as e:  # return errors related to socket or address semantics
    print(str(e))

Response = ClientSocket.recv(1024)  # wait and receive data from server with max size 1024 bytes
print(Response.decode('ascii'))  # decode and print message

while connection:
    Response = ClientSocket.recv(1024)
    print(Response.decode('ascii'))
    if Response.decode('ascii') != 'you are the attacker':
        Response = ClientSocket.recv(1024)  # receive attack
        # response = encryption.decrypt(Response)  # defender behavior
        print(Response.decode('ascii'))  # print the response
        # BinWord = NRZ.WordToBinary(response)
        # RNZBinWord = NRZ.NRZ(BinWord)
        # DecodedWord = NRZ.BinaryToWord(RNZBinWord)
        if Response.decode('ascii') == 'ATTACK':
            score -= 1
            print('defence failed')
            ClientSocket.send(str.encode('defence failed', encoding='ascii'))
        else:  # send if the attack failed or not
            score += 1
            print('defence successful')
            ClientSocket.send(str.encode('defence successful', encoding='ascii'))


    else:
        time.sleep(2)  # sleep for testing
        # message = encryption.encryption()
        ClientSocket.send(str.encode('ATTACK', encoding='ascii'))  # send attack in ascii
        message = ClientSocket.recv(1024)  # receive if the attack failed or not
        if message == 'defence failed':
            score += 1
        else:
            score -= 1
