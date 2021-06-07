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





def shift(res):
    text = "ATTACK"
    temp = (7- 3) % len(text)
    res = text[temp:] + text[: temp]
    return res


def defenderShift(defres):
    temp = (3 - 7) % len(defres)
    res = defres[temp:] + defres[: temp]

    return res
