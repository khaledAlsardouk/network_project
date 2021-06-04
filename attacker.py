from cryptography.fernet import Fernet
import HammingCode
import NRZ

key = Fernet.generate_key()
Response = NRZ.WordToBinary('ATTACK')
m = len(Response)
r = HammingCode.calcRedundantBits(m)
arr = HammingCode.posRedundantBits(Response, r)
arr = HammingCode.calcParityBits(arr, r)


def encryption():
    crypter = Fernet(key)
    attack = crypter.encrypt(b'ATTACK')
    return attack


def decrypt(encrypted_text):
    crypter = Fernet(key)
    attack = crypter.decrypt(encrypted_text)
    attack = detect_errors(attack)
    return attack


def detect_errors(message):
    BinWord = NRZ.WordToBinary(message)
    correction = HammingCode.detectError(BinWord, r)
    correct = HammingCode.correction(BinWord, correction)
    return correct

def shift(text):
    output = ""
    shift= -10
    for char in text:
        output += chr(ord(char) + shift)
    return output