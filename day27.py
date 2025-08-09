# Day: 27(Ex: 03 "Kaun baega Crorepati")

import random
questions=[
            ["Name the tallest mountain peak in the world",
            "Mount Everest","K2","Mauna Kea","Kangchenjunga",1],
           ["When was French revolution approved ?",
            1971,1642,1789,1519,3],
           ["Name the year in which World War 2 ended?",
            1940,1945,1946,1939,2]
           ]
prize_amount=[100,1000,10000] 

i=0 # Variable for iterating
random.shuffle(questions)
name= input("Hello, user. Please enter your name: ")
print(f"Welcome to Kaun Banega Crorepati: {name}. You will be asked several questions and after each question \
you can take the money prize that you have won and leave, or you can compete for a bigger prize. So are \
you ready ?")

play_cond=input(" Type 'yes' to begin: ")
play_cond=play_cond.strip().lower()


if play_cond=="yes":
    for index , question in enumerate(questions):
            print(f"\n{question[0]}")
            print(f"1- {question[1]:<15} 2- {question[2]:<15}")
            print(f"3- {question[3]:<15} 4- {question[4]:<15}\n")
            answer=int(input("Enter your answer (1-4): "))
            
            
            if answer == question[-1]:
                if len(questions)-1==index:
                    print(f"Congratulations, You have won the highest prize of '{prize_amount[i]}' Rs.\n Have a Great Day :)")
                    break
                else:
                    pass
                print(f"Your answer is Correct. You have won {prize_amount[i]} Rs.\n")
                print(f"Do you want to go continue or leave now with your {prize_amount[i]} Rs ?")
                cont_cond= str(input("What's your answer ? (Yes/No): "))
                cont_cond=cont_cond.strip().lower()
                if (cont_cond == "no"):
                    print(f"Well, congrats on winning your {prize_amount[i]} Rs. Goodbye.")
                    break
                elif(cont_cond == "yes"):
                    pass 
                else:
                    print("Wrong input, so quiting anyways ...")
                    break
                i=i+1
            else:
                print("Oops, your answer is Incorrect.")    

else:
    print("You answered something else than 'yes' so, it seems like you are busy at the moment. No worries \
let's play again soon :)")
    
    