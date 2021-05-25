from cryptography.fernet import Fernet

key=Fernet.generate_key()

def encryption():

    crypter=Fernet(key)
    print(key)
    attack= crypter.encrypt(b'ATTACK')
    return(attack)

def decrypt(encrypted_text):

     crypter = Fernet(key)
     attack = crypter.decrypt(encrypted_text)
     return attack

encrypted_text = encryption()
print("Encrypted Text:")
print(encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Decrypted Text:")
print(decrypted_text)