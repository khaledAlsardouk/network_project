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


res = ''


def shift(res):
    text = "ATTACK"
    birep = ''.join(format(ord(char), 'b') for char in text)
    res = (birep * 3)[len(birep) + 7 - 3:
                      2 * len(birep) + 7 - 3]
    return res


def defenderShift(defres):
    defres = (res * 3)[len(res) + 3 - 7:
                       2 * len(res) + 3 - 7]

    return defres
