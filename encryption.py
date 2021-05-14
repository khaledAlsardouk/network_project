import random
text="ATTACK"
print(text)
birep = ''.join(format(ord(char), '08b')for char in text)
print("the original word in its binary representation before encryption was",str(birep))
output=""
for char in text:
    birep = ''.join(format(ord(char), '08b'))
    print("the original binary representation of the letter was", str(birep))
    shift=random.randrange(1,50)
    print(char,ord(char),ord(char)+shift,chr(ord(char)+shift))
    birep=''.join(format(ord(char), '08b')for char in chr(ord(char)+shift) )
    print("the binary representation of the letter becomes\n",str(birep))
    output+=chr(ord(char)+shift)


print(output)
birep=''.join(format(ord(char),'08b')for char in output)
print("the binary representation of the word after encryption becomes ",str(birep))