import socket
import time
# import BitArray
# import encryption
import NRZ
import HammingCode

ClientSocket = socket.socket()  # create socket
host = '127.0.0.1'  # local host ip for now
port = 1234
def_score = 0
attk_score = 0
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
    Response = Response.decode('ascii')
    print(Response)
    if Response == 'you are the defender':
        Response = ClientSocket.recv(1024)  # receive attack
        # response = encryption.decrypt(Response)  # defender behavior
        # print(Response.decode('ascii'))  # print the response
        response = NRZ.ByteToBinary(Response)
        NRZ_bin = NRZ.NRZ(response)
        print(NRZ.BinaryToWord(NRZ_bin))
        print("the message was:", NRZ.BinaryToWord(NRZ.NRZ(NRZ_bin)))
        # BinWord = NRZ.WordToBinary(response)
        # RNZBinWord = NRZ.NRZ(BinWord)
        # DecodedWord = NRZ.BinaryToWord(RNZBinWord)
        print(Response.decode("ascii"))
        if Response.decode('ascii') == 'ATTACK':
            def_score -= 10
            print(def_score)
            print('defence failed')
            ClientSocket.send(str.encode('defence failed', encoding='ascii'))

        else:  # send if the attack failed or not
            def_score += 10
            print(def_score)
            print('defence successful')
            ClientSocket.send(str.encode('defence successful', encoding='ascii'))
    elif Response == 'you are the attacker':
        time.sleep(2)  # sleep for testing
        # message = encryption.encryption()
        ClientSocket.send(str.encode('ATTACK', encoding='ascii'))  # send attack in ascii
        message = ClientSocket.recv(1024)  # receive if the attack failed or not
        if message.decode('ascii') == 'defence failed':
            attk_score += 10
            print(attk_score)
        else:
            attk_score -= 10
            print(attk_score)

    else:
        score = attk_score + def_score
        print(score)
        ClientSocket.send(str.encode(str(score), encoding='ascii'))
        print('worked')
        result = ClientSocket.recv(1024)
        result.decode('ascii')
        print(result)