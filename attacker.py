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
    BinWord = defender.ByteToBinary(message)
    correction = HammingCode.detectError(BinWord, r)
    correct = HammingCode.correction(BinWord, correction)
    return correct


def shift(word):
    birep = ''.join(format(ord(char), 'b') for char in word)
    # print(birep)
    decimal = 0
    for digit in birep:
        decimal = decimal * 2 + int(digit)
    shiftedDecimal = decimal >> 2
    word = defender.decimalToBinary(shiftedDecimal)
    word = defender.BinaryToWord(word)
    return word
