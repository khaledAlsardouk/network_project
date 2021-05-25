from cryptography.fernet import Fernet


def encryption():
    key=Fernet.generate_key()
    crypter=Fernet(key)
    text="ATTACK"
    attack= crypter.encrypt(b'ATTACK')
    return(attack)
print(encryption())

def decrypt(encryption1):
     key=Fernet.generate_key()
     crypter=Fernet(key)
     attack= crypter.decrypt(encryption1)
     return attack

