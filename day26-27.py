<<<<<<< HEAD
# Day 26 Ex: 2 shoutouts etc
# Day 27 Ex:3 (Kaun baega Crorepati)
import random
name= input("Enter your name: ")
questions=["Name the tallest mountain peak in the world ","When was French revolution approved ?",
           "Name the year in which World War 2 ended? "]

questions_ans=["mount everest","1789","1945"]

prize_amount=[100,1000,10000] 

j=0
total=0

print(f"\nWelcome to Kaun Bnega Crorepati {name} !!!\nHere, you will play a quiz\
 consisting of {len(questions)} questions. The reward will start from {prize_amount[0]}$ all the way to\
 {prize_amount[len(prize_amount)-1]}$. I'am ready ,when you are :D ") 

condition= str(input("Type 'yes' to begin: "))
condition.lower()
if condition == "yes":
    
    for i in questions:
    
            
        print("\nQuestion No",(questions.index(i)+1),"for the amount of :",prize_amount[j],"$")
        
        rand_question =random.randint(0,len(questions)-1)
        print("\n",questions[rand_question])
        
        answer= str(input("Answer: "))
        Answer=answer.lower()
        
        current_amount= prize_amount[j]
        
        total= current_amount + total
        j= j+1
        
        print("\nThe amount that you have currently won is: ",total,"$")
        
        if (i == len(questions)-1):
            print(f"Congratulations,  you have won {total}$. Have fun Millionare :)")
            break
        
        elif questions[rand_question]==questions_ans[rand_question] and Answer in questions_ans:
            print(f'The answer is "Correct", before moving onto the next question,do you want to continue playing or do you want to quit with your {total} $ ?\n')
            answer_2=str(input("Type 'yes' if you wish to play further: "))
            answer_2=answer_2.lower()
            if answer_2=="yes":
                continue
            else:
                break
            
        elif questions[rand_question]!=questions_ans[rand_question] and Answer not in questions_ans:
            print(f'Oops, looks like the answer is "Incorrect", but congratulations on winning {total}. Goodbye :)\n')
            break

else:
=======
# Day 26 Ex: 2 shoutouts etc
# Day 27 Ex:3 (Kaun baega Crorepati)
import random
name= input("Enter your name: ")
questions=["Name the tallest mountain peak in the world ","When was French revolution approved ?",
           "Name the year in which World War 2 ended? "]

questions_ans=["mount everest","1789","1945"]

prize_amount=[100,1000,10000] 

j=0
total=0

print(f"\nWelcome to Kaun Bnega Crorepati {name} !!!\nHere, you will play a quiz\
 consisting of {len(questions)} questions. The reward will start from {prize_amount[0]}$ all the way to\
 {prize_amount[len(prize_amount)-1]}$. I'am ready ,when you are :D ") 

condition= str(input("Type 'yes' to begin: "))
condition.lower()
if condition == "yes":
    
    for i in questions:
    
            
        print("\nQuestion No",(questions.index(i)+1),"for the amount of :",prize_amount[j],"$")
        
        rand_question =random.randint(0,len(questions)-1)
        print("\n",questions[rand_question])
        
        answer= str(input("Answer: "))
        Answer=answer.lower()
        
        current_amount= prize_amount[j]
        
        total= current_amount + total
        j= j+1
        
        print("\nThe amount that you have currently won is: ",total,"$")
        
        if (i == len(questions)-1):
            print(f"Congratulations,  you have won {total}$. Have fun Millionare :)")
            break
        
        elif questions[rand_question]==questions_ans[rand_question] and Answer in questions_ans:
            print(f'The answer is "Correct", before moving onto the next question,do you want to continue playing or do you want to quit with your {total} $ ?\n')
            answer_2=str(input("Type 'yes' if you wish to play further: "))
            answer_2=answer_2.lower()
            if answer_2=="yes":
                continue
            else:
                break
            
        elif questions[rand_question]!=questions_ans[rand_question] and Answer not in questions_ans:
            print(f'Oops, looks like the answer is "Incorrect", but congratulations on winning {total}. Goodbye :)\n')
            break

else:
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a
    print("Oh, I Guess you are busy right now, no worries. Just run the program again when you are ready :)")