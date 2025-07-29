#Day 40 (Ex:4 Secret Code Langauge Program):
import random
alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"
            ,"O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n"
            ,"o","p","q","r","s","t","u","v","w","x","y","z"]

random_alph1=random.choice(alphabets)
print(random_alph1)

random_alph2=random.choice(alphabets)
print(random_alph2)

random_alph3=random.choice(alphabets)
print(random_alph3)

message=str(input("Enter your secret messege:"))
sentence= list(message)
print("All the letters are: ",sentence) #Distributes the whole messege into letters

words_as_letters=[] #Final output and will contain the words as sublists
current_word=[]     #Current output
encoded_list=[]
decoded_list=[]    
word_lengths=[]

for letter in sentence:
    if letter==" ":
        if len(current_word)>0:
            words_as_letters.append(current_word)
            current_word=[]
    else:
        current_word.append(letter)

if len(current_word)>0: #For the last word because there is no space to trigger the case we defined earlier
    words_as_letters.append(current_word)
        

print("Broken words are: ",words_as_letters,"\n")

i=0 

# ENCODING

for word in words_as_letters:
    print(f"word no {i+1}: {word}")
    # print(f"No of characters in this word is: {len(word)}")
    
    if(len(word)>3):
        letter=word.pop(0)                  #remove first letter
        print("The char removed is:",letter)
        print("The word now is:",word)
        word.append(letter)                 #append first letter in the end
        print("The word now after appending is:",word)
        word.insert(0,random_alph1)
        word.insert(1,random_alph2)          #adding 3 random characters in the beginning
        word.insert(2,random_alph3)
        word.append(random_alph1)
        word.append(random_alph2)             #adding 3 random characters in the end
        word.append(random_alph3)
        print("The word after appending 3 random chars is: ",word,"\n")
        word_lengths.append(len(word))
        encoded_list.extend(word)
        
    else:
        word.reverse()
        print("The word length doesnt excede 5 so:",word,"\n")
        word_lengths.append(len(word))
        encoded_list.extend(word)
    i+=1

print("The encoded list is: ",encoded_list)

# DECODING
start =0    
word_number = 1
for length in word_lengths:
    chunk = encoded_list[start:start + length]
    print("Encoded word", word_number, ":", chunk)

    if length > 6:  # It has 3 + original word + 3 random chars
        # Remove first 3 and last 3 characters (random letters)
        core = chunk[3:-3]

        # Move last letter back to front (reverse the encoding logic)
        original = [core[-1]] + core[:-1]
        print("Decoded:", original)
        decoded_list.extend(original)
    else:
        # Reverse short words again
        chunk.reverse()
        print("Decoded:", chunk)
        decoded_list.extend(chunk)

    # Add a space after each word
    decoded_list.append(" ")
    start += length
    word_number += 1

# Final decoded message
final_message = ''.join(decoded_list).strip()
print("\nFinal Decoded Message:", final_message)



