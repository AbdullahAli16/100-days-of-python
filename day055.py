# Day: 55(Ex: 05 "Snake, Water, Gun game")

import random

# Game Outcome graph:
'''game=[             Snake  Water  Gun
            Snake    [Draw,  Snake, Gun]
            Water    [Snake, Draw,  Water]
            Gun      [Gun,   Water, Draw]
    ]'''

def check_outcome(cpu_answer,user_answer):
    # If CPU chooses "Snake":
    if  cpu_answer=="snake" and user_answer=="snake":
        print ("It's a DRAW. No one wins.")
    elif cpu_answer=="snake" and user_answer=="water":
        print ("Snake DRINKS the water. CPU wins !")
    elif cpu_answer=="snake" and user_answer=="gun":
        print ("Gun KILLS the Snake. Player wins !")

    # If CPU chooses "Water":
    elif cpu_answer=="water" and user_answer=="snake":
        print ("Snake DRINKS the water. Player wins !")
    elif cpu_answer=="water" and user_answer=="water":
        print ("It's a DRAW. No one wins.")
    elif cpu_answer=="water" and user_answer=="gun":
        print ("Water SABOTAGES the gun. CPU wins !")
    
    # If CPU chooses "Gun":
    elif cpu_answer=="gun" and user_answer=="snake":
        print ("Gun KILLS the Snake. CPU wins !")
    elif cpu_answer=="gun" and user_answer=="water":
        print ("Water SABOTAGES the gun. Player wins !")
    elif cpu_answer=="gun" and user_answer=="gun":
        print ("It's a DRAW. No one wins.")
        

options= ["Snake","Water","Gun"]
cpu_answer=random.choice(options)
cpu_answer=cpu_answer.strip().lower()
print(cpu_answer)

print("Welcome to the Snake, Water and Gun game. The rules are basic, the Snake drinks the water, water \
sabotages the gun and the gun kills the snake. Shall we begin ?")

play_cond=input("Type 'yes' to play: ")
play_cond=play_cond.strip().lower()

if play_cond=="yes":
    user_answer=str(input("Snake,water or gun ? (Before the time runs out, type ONE): "))
    user_answer=user_answer.strip().lower()
    check_outcome(cpu_answer,user_answer)
else:
    print("It seems like you don't want to play right now, let's play sometime else soon")