#THIS FILE HAS 3 SELF DESCRIPTIVE FUNCTIONS:
# NRZ(BINARY) FUNCTION changes flips 1s and 0s
# WordToBinary(WORD) converts a word to binary
# BinaryToWord(BINARY) converts binary to char
def NRZ(BinWord):
    print("Got this:",BinWord)
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
    print ("Converted it to this:",y)
    return y

"""def BinaryToWord(BinWord):
    a_binary_string = BinWord
    binary_values = a_binary_string.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(ascii_string)
    return ascii_string"""

def WordToBinary(word):
    binary_word = ' '.join(format(ord(x), 'b') for x in word)  # converts the word to binary
    Binary_word2 = [""]
    for i in binary_word:
        if i == ' ':
            flip_the_bit = i.replace(" ", "")
        else:
            flip_the_bit = i
        Binary_word2.append(flip_the_bit)
    y = ''.join(str(j) for j in Binary_word2)
    print(y)
    return binary_word


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
    str_data = ' '
    for i in range(0, len(BinWord), 7):
        temp_data = int(BinWord[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    print("The Binary value after string conversion is:",str_data)
