from cryptography.fernet import Fernet
import HammingCode
import defender

key = Fernet.generate_key()
Response = defender.WordToBinary('ATTACK')
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
    BinWord = defender.WordToBinary(message)
    correction = HammingCode.detectError(BinWord, r)
    correct = HammingCode.correction(BinWord, correction)
    return correct

def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    #print(num % 2, end='')

def shift():
    text="ATTACK"
    birep = ''.join(format(ord(char), 'b')for char in text)
    #print(birep)
    decimal = 0
    for digit in birep:
        decimal = decimal * 2 + int(digit)

    #print(decimal)

    shiftedDecimal=decimal>>2
    #print(shiftedDecimal)

    return decimalToBinary(shiftedDecimal)

