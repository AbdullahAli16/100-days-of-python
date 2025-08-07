# Day: 40(Ex: 04 "Secret Code Langauge Program")

import random
alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
            ,"O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n"
            ,"o","p","q","r","s","t","u","v","w","x","y","z"]

# Getting random variables from the list of alphabets
random_alphabet_1=random.choice(alphabets)
random_alphabet_2=random.choice(alphabets)
random_alphabet_3=random.choice(alphabets)

print("The 3 random chars are:",random_alphabet_1,random_alphabet_2,random_alphabet_3)

print("Welcome to the Encoding messege program :) \n")
user_input= str(input("Please enter the sentence you wish to encode: "))

letters=list(user_input)


words_length=[]          # The list for storing lengths of each word for decoding purpose
current_word=[]           # The list for storing a word 
all_words=[]                # The list for storing all the words in the input

encoded_words=[]
decoded_words=[]
list_of_encoded_words=[]                

# Breaking the entire string into words

for index, letter in enumerate(letters):       
    current_word.append(letter)
    if letter==' ':
        current_word.pop()
        words_length.append(len(current_word))
        all_words.append(current_word)
        current_word=[]
    elif index==len(letters)-1:
        all_words.append(current_word)
        words_length.append(len(current_word))
        current_word=[]

# Encoding

for index ,word in enumerate(all_words):
    if len(word)>=3:
        first_char= word.pop(0)      # Removing the first character
        word.append(first_char)         # and Appending it in the end
        word.insert(0,random_alphabet_1)
        word.insert(0,random_alphabet_2)       #Appending 3 random characters in the start
        word.insert(0,random_alphabet_3)
        word.append(random_alphabet_1)
        word.append(random_alphabet_2)         #Appending 3 random characters in the end 
        word.append(random_alphabet_3)
        encoded_words.append(word)
        
    else:
        word.reverse()
        encoded_words.append(word)
        
for encoded_letter in encoded_words:         #Converting the nested list into a single flar list
    list_of_encoded_words.extend(encoded_letter)
    
string_of_encoded_words="".join(list_of_encoded_words)    #Converting into a string

print(f"The encoded words are: {string_of_encoded_words}")

# Decoding

for index, encoded_word in enumerate(encoded_words):
    if len(encoded_word) <3:
        encoded_word.reverse()           #If word has less than 4 characters
        encoded_word.append(' ')
        decoded_words.extend(encoded_word)
    else:
        encoded_word.pop(0)                #Removing 3 random characters from start
        encoded_word.pop(0)            
        encoded_word.pop(0)  

        encoded_word.pop(-1)                #Removing 3 random characters from end
        encoded_word.pop(-1)
        encoded_word.pop(-1)
        
        first_char= encoded_word.pop(-1)            #Removing the last letter and adding it in the start
        encoded_word.insert(0,first_char)
        encoded_word.append(' ')
        
        decoded_words.extend(encoded_word)

print(decoded_words)        
string_of_decoded_words="".join(decoded_words)

print(f"The decoded words are: {string_of_decoded_words}")

    
    




