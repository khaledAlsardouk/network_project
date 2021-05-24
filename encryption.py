from cryptography.fernet import Fernet


def encryption():
    key=Fernet.generate_key()
    crypter=Fernet(key)
    text="ATTACK"
    birep = ''.join(format(ord(char), '08b')for char in text)
    #print("the binary form is ",birep)

    attack= crypter.encrypt(b'ATTACK')

    return(birep,attack)
print(encryption())
