from cryptography.fernet import Fernet
key=Fernet.generate_key()
def encryption():
    crypter=Fernet(key)
    attack= crypter.encrypt(b'ATTACK')
    return(attack)
def decrypt(encrypted_text):
     crypter = Fernet(key)
     attack = crypter.decrypt(encrypted_text)
     return attack

