#Create a code generator. This can that take text as input, replaces
# each letter with another letter, and outputs the “encoded” message

#function to get plain text and key input
def get_text_input():   
        text = input("Please enter your text to encode here: ")
        key =  int(input("Enter Key for encoding: "))

        if (text and key):             
              return encode_text(text, key) 
        else:
              print('your input cannot be blank and the Key must be a numerical value ')
              get_text_input()

#function to encode plain text using caesar cipher
def encode_text(plain_text, cipherKey):
       cipher_text= ""
       small_starting_point = 97
       small_ending_point = 122
       cap_starting_point = 65
       cap_ending_point = 90

#loop through text check if character is lower or upper case, find value of character and add shift value
# convert value back to alphabet
# cater for if value is more than value of Z for lower or uppercase      

       for index in range(0,len(plain_text), 1):
            if(plain_text[index] == " "):
                cipher_text += chr(ord(plain_text[index]) + cipherKey)
            else:
                cipher_value = ord(plain_text[index]) + cipherKey
                if( plain_text[index].islower() and cipher_value > small_ending_point):
                    diff = cipher_value - small_ending_point
                    next_value = diff + (small_starting_point - 1)
                    cipher_text += chr(next_value)
                elif( plain_text[index].isupper() and cipher_value > cap_ending_point):
                    diff = cipher_value - cap_ending_point
                    next_value = diff + (cap_starting_point - 1)
                    cipher_text += chr(next_value)
                else:
                    cipher_text += chr(ord(plain_text[index]) + cipherKey)

       print(cipher_text)

#function to get cipher text and key input to decode
def get_decode_input():   
        text = input("Please enter your text to decode here: ")
        key =  int(input("Enter Key for encoding: "))

        if (text and key):             
              return decode(text, key) 
        else:
              print('your input cannot be blank and the Key must be a numerical value ')
              get_text_input()


#function to decode the cipher text back to the original message
def decode(cipher , key):
    decode_value =""
    print(cipher)
    for ind in range (0 , len(cipher) , 1):
        if(cipher[ind].isupper()):            
            if(ord(cipher[ind]) - key < 65 ):
                diffs = 64 - (ord(cipher[ind]) - key)
                dif_value = 90 - diffs
                decode_value += (chr(dif_value))
            else:
                decode_value += (chr(ord(cipher[ind]) - key))
        elif(cipher[ind].islower()):
            if(ord(cipher[ind]) - key < 97 ):
                print(cipher[ind])
                diffs = 96 - (ord(cipher[ind]) - key)
                dif_value = 122 - diffs
                decode_value+=(chr(dif_value))
            else:
                decode_value += (chr(ord(cipher[ind]) - key))
        else:
            decode_value += chr(ord(cipher[ind]) - key)
    return (decode_value)


get_text_input()
print (get_decode_input())