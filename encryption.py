import random
def encrypt():
    text="ATTACK"
    birep = ''.join(format(ord(char), '08b')for char in text)
    output=""
    for char in text:
        shift=random.randrange(1,50)
        output+=chr(ord(char)+shift)
    birep=''.join(format(ord(char),'08b')for char in output)
    return bytes(output,'ascii')