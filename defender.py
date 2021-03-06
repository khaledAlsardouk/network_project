# THIS FILE HAS 3 SELF DESCRIPTIVE FUNCTIONS:
# NRZ(BINARY) FUNCTION changes flips 1s and 0s
# ByteToBinary(WORD) converts ASCII to binary
# BinaryToWord(BINARY) converts binary to char
# WordToBinary(WORD) converts char to binary
import binascii


def NRZ(BinWord):
    # print("Got this:",BinWord) #for testing purposes
    word_in_list = list(BinWord)
    # print(word_in_list)
    NRZ_of_word = [""]
    for i in word_in_list:
        if i == '0':
            flip_the_bit = i.replace("0", "1")
        elif i == '1':
            flip_the_bit = i.replace("1", "0")
        elif i == ' ':
            flip_the_bit = i.replace(" ", "")
        NRZ_of_word.append(flip_the_bit)
    y = ''.join(str(j) for j in NRZ_of_word)
    # print ("Converted it to this:",y) #for testing purposes
    return BinaryToWord(y)


def ByteToBinary(word):
    binary_word = ' '.join(format(ord(x), 'b') for x in word)  # converts the word to binary
    Binary_word2 = [""]
    for i in binary_word:
        if i == ' ':
            flip_the_bit = i.replace(" ", "")
        else:
            flip_the_bit = i
        Binary_word2.append(flip_the_bit)
    y = ''.join(str(j) for j in Binary_word2)
    # print(y) #for testing purposes
    return y


def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def BinaryToWord(s):
    result = ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))
    result = result.replace("=", "")
    return result


def WordToBinary(word):
    res = ''.join(format(i, '08b') for i in bytearray(word, encoding='utf-8'))
    return res


# def WordToBinNew(word):
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    # print(num % 2, end='')
