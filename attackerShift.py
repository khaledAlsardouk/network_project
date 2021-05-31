

def shift():
    text="ATTACK"
    print(text)
    #represent ATTACK in binary
    birep = ''.join(format(ord(char), '08b')for char in text)
    print("the original word in its binary representation before shifting was",str(birep))
    output = ""
    shift=-10 # used to shift ATTACK by -10, defender shifts by 10
    for char in text:
        #birep = ''.join(format(ord(char), '08b'))
        #print("the original binary representation of the letter was", str(birep))

        #print(char,ord(char),ord(char)+shift,chr(ord(char)+shift))
        #birep=''.join(format(ord(char), '08b')for char in chr(ord(char)+shift) )
        #print("the binary representation of the letter becomes\n",str(birep))
        output+=chr(ord(char)+shift)


    print(output)
    # represent ATTACK after shifting
    birep=''.join(format(ord(char),'08b')for char in output)
    print("the binary representation of the word after shifting  becomes ",str(birep))
    return(output)