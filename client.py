import socket
import time
import attacker
import defender
import HammingCode
import random

global threshold

ClientSocket = socket.socket()  # create socket
host = '127.0.0.1'    # local host ip for now
#host = '25.75.141.183'   #hamachi

port = 1234
def_score = 0
atk_score = 0
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

        print(Response.decode('utf-8'))
        Response = Response.decode('utf-8')
        # Response = attacker.detect_errors(Response)
        print(Response)
        choice = random.randint(0, 1)
        if choice == 0:
            Response = defender.WordToBinary(Response)
            Response = defender.NRZ(Response)
        elif choice == 1:
            Response = attacker.defenderShift(Response)

        if Response == 'ATTACK':
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
        time.sleep(1)  # sleep for testing
        # message = encryption.encryption()
        initial = time.time()
        word = 'ATTACK'
        choice = random.randint(0, 1)
        if choice == 0:
            word = defender.WordToBinary(word)
            word = defender.NRZ(word)

        else:
            word = attacker.shift(word)
            print(Response)

        ClientSocket.send(str(word).encode('utf-8'))  # send attack in utf-8
        message = ClientSocket.recv(1024)  # receive if the attack failed or not
        final = time.time()
        rtt = final - initial
        threshold = 0.1
        print(f'rtt={rtt}')
        if rtt > threshold:
            atk_score -= 20
            def_score += 20
            print(atk_score)
        elif message.decode('ascii') == 'defence failed':
            atk_score += 10
            print(f'atk score={atk_score}')
        else:
            atk_score -= 10
            print(f'atk score={atk_score}')
    else:
        score = atk_score + def_score
        print(score)
        ClientSocket.send(str.encode(str(score), encoding='ascii'))
        result = ClientSocket.recv(1024)
        print(result.decode('ascii'))
