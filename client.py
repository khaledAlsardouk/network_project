import socket
import time
# import BitArray
# import encryption
import NRZ
import HammingCode
from attackerShift import *
global threshold
from random import randrange

def attackPath(text):
    choice = randrange(0,1)
    print(choice)
    if choice == 0:
        # 0 means NRZ
        text_binary = NRZ.ByteToBinary(text)
        return NRZ.NRZ(text_binary)
    else:
        # 1 means Shift
        return shift(text)
def defenderPath(text):
    choice = randrange(0,1)
    print(choice)
    if choice == 1:
        # 1 means NRZ
        #text_binary = NRZ.ByteToBinary(text)
        return NRZ.NRZ(text)
    else:
        # 0 means Shift
        return shift(text)

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
        defenderPath(Response)
        # response = encryption.decrypt(Response)  # defender behavior
        # print(Response.decode('ascii'))  # print the response
        print(Response.decode('ascii'))
        response = NRZ.ByteToBinary(Response)
        Response = NRZ.NRZ(response)
        Response = NRZ.BinaryToWord(Response)
        print('NRZ result: ' + Response)
        if Response == '1':
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
        intialy=time.time()
        word = 'ATTACK'
        word_encrypted = attackPath(word)
        ClientSocket.send(str.encode(word_encrypted, encoding='ascii'))  # send attack in ascii
        message = ClientSocket.recv(1024)  # receive if the attack failed or not
        finaly=time.time()
        rtt=finaly-intialy
        threshold=0.1
        print(rtt)
        if rtt>threshold:
            attk_score-=20
            def_score+=20
            print(attk_score)
        elif message.decode('ascii') == 'defence failed':
            attk_score += 10
            print(attk_score)
        else:
            attk_score -= 10
            print(attk_score)
    else:
        score = attk_score + def_score
        print(score)
        ClientSocket.send(str.encode(str(score), encoding='ascii'))
        result = ClientSocket.recv(1024)
        result.decode('ascii')
        print(result)




