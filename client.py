import socket
import time
import encryption
import NRZ
import HammingCode
ClientSocket = socket.socket()  # create socket
host = '127.0.0.1'  # local host ip for now
port = 1234
score = 0

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))  # connect socket to host on  a specific port
except socket.error as e:  # return errors related to socket or address semantics
    print(str(e))


def play1(message):
     ClientSocket.send(message)
     Input = input("do you want to continue attacking:yes or no")
     if Input == str("no"):
        print("the connection is closed")
        ClientSocket.close()
        return False
     else:
        ClientSocket.send(message)
        return True

Response = ClientSocket.recv(1024)  # wait and receive data from server with max size 1024 bytes
print(Response.decode('ascii'))  # decode and print message
connection = True
while connection:
    Response = ClientSocket.recv(1024)
    print(Response.decode('ascii'))
    if Response.decode('ascii') != 'you are the attacker':
        m = len(Response)
        r = HammingCode.calcRedundantBits(m)
        arr = HammingCode.posRedundantBits(Response, r)
        arr = HammingCode.calcParityBits(arr, r)
        Response = ClientSocket.recv(1024)
        response = Response.decode('ascii')  # defender behavior
        correction = HammingCode.detectError(Response, r)
        BinWord = NRZ.WordToBinary(response)
        RNZBinWord = NRZ.NRZ(BinWord)
        WordBin = NRZ.BinaryToWord(RNZBinWord)
        print("the encoded message:", WordBin)
        print("decoding message...")
        DecodedWordBin = NRZ.NRZ(RNZBinWord)
        DecodedWord = NRZ.BinaryToWord(DecodedWordBin)
        print("the decoded message:", DecodedWord)


    #     if response.__eq__('attack'):
    #         print('defence failed')
    #     else:
    #         score = score + 1
    #         print('defence successful')
    #          print(f'score: {score}')

    else:
        time.sleep(5)
        message = encryption.encryption()
        sent = encryption.decrypt(message)
        connection = play1(sent)



