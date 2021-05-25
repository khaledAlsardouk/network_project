word='attack'
word1=word.encode('ascii')
def NRZ(word):
    #word = "0111000110011"
    word_in_list= list(word)
    print(word_in_list)
    NRZ_of_word=[]
    for i in word_in_list:
        if i == '0':
            flip_the_bit= i.replace("0","1")
        elif i == '1':
            flip_the_bit = i.replace("1","0")
        NRZ_of_word.append(flip_the_bit)
    y = ''.join(str(j) for j in NRZ_of_word)
    print (y)

#x = input("please enter a binary number to perform NRZ on it:")
NRZ(word1)

