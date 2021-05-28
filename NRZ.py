
#THIS FILE HAS 3 SELF DESCRIPTIVE FUNCTIONS:
# NRZ(BINARY) FUNCTION changes flips 1s and 0s
# ByteToBinary(WORD) converts ASCII to binary
# BinaryToWord(BINARY) converts binary to char

import binascii

def NRZ(BinWord):
    #print("Got this:",BinWord) #for testing purposes
    word_in_list = list(BinWord)
    #print(word_in_list)
    NRZ_of_word=[""]
    for i in word_in_list:
        if i == '0':
            flip_the_bit= i.replace("0","1")
        elif i == '1':
            flip_the_bit = i.replace("1","0")
        elif i == ' ':
            flip_the_bit=i.replace(" ", "")
        NRZ_of_word.append(flip_the_bit)
    y = ''.join(str(j) for j in NRZ_of_word)
    #print ("Converted it to this:",y) #for testing purposes
    return y

def BinaryToWord(BinWord):
    a_binary_string = BinWord
    binary_values = a_binary_string.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(ascii_string)
    return ascii_string

def ByteToBinary(word):
    x= word.decode("utf-8")
    binary_word = ' '.join(format(ord(x), 'b') for x in x)  # converts the word to binary
    Binary_word2 = [""]
    for i in binary_word:
        if i == ' ':
            flip_the_bit = i.replace(" ", "")
        else:
            flip_the_bit = i
        Binary_word2.append(flip_the_bit)
    y = ''.join(str(j) for j in Binary_word2)
    #print(y) #for testing purposes
    return y


def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)


def BinaryToWord(BinWord):
    str_data = ''
    for i in range(0, len(BinWord), 7):
        temp_data = int(BinWord[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    #print("The Binary value after string conversion is:",str_data) #for testing purposes
    return str_data
#def WordToBinNew(word):
"""
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
"""