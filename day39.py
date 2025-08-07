# Day: 39(Instructor's solution to Ex: 03 "Kaun Banega Crorepati")

import random

# ✅ User input
name = input("Enter your name: ")

# ✅ Question and answers list
questions = [
    "Name the tallest mountain peak in the world",
    "When was French revolution approved?",
    "Name the year in which World War 2 ended?"
]

# ✅ Answer list - should match each question by index
questions_ans = ["mount everest", "1789", "1945"]

# ✅ Prize amounts for each question
prize_amount = [100, 1000, 10000]

j = 0  # Prize level index
total = 0  # Total amount won

# ✅ Welcome message
print(f"\nWelcome to Kaun Banega Crorepati, {name}!!!\nHere, you will play a quiz consisting of {len(questions)} questions.")
print(f"The reward will start from {prize_amount[0]}$ all the way to {prize_amount[-1]}$. I'm ready when you are :D") 

# ⚠️ MISTAKE: You wrote `condition.lower()` but didn’t assign it — this does nothing.
condition = input("Type 'yes' to begin: ").strip().lower()

if condition == "yes":

    for i in range(len(questions)):  # ⚠️ MISTAKE: Earlier you used `for i in questions`, then did `questions.index(i)` — inefficient.
        
        print("\nQuestion No", (i + 1), "for the amount of:", prize_amount[j], "$")
        
        # ⚠️ MISTAKE: You used random selection inside a loop — this caused repeated or mismatched questions and answers.
        # FIX: Use questions in order instead.
        print(questions[i])
        
        # ⚠️ MISTAKE: You used answer.lower(), but didn’t assign it.
        answer = input("Answer: ").strip().lower()

        # ✅ Check if answer is correct for this specific question
        if answer == questions_ans[i]:
            current_amount = prize_amount[j]
            total += current_amount
            print("\nCorrect answer!")
            print("The amount that you have currently won is:", total, "$")

            # ✅ Ask to continue
            if i == len(questions) - 1:
                print(f"\nCongratulations! You have answered all questions correctly and won {total}$. Have fun, Millionaire :)")
                break
            else:
                answer_2 = input("\nDo you want to continue playing or quit? Type 'yes' to play further: ").strip().lower()
                if answer_2 == "yes":
                    j += 1  # Move to next prize level
                    continue
                else:
                    print(f"\nYou chose to quit. Congratulations on winning {total}$! Goodbye :)")
                    break
        else:
            # ⚠️ MISTAKE: Previously you still gave prize money even on wrong answers
            print(f"\nOops, the answer is Incorrect. The correct answer was '{questions_ans[i]}'.")
            print(f"But congratulations on winning {total}$. Goodbye :)")
            break

else:
    print("Oh, I guess you are busy right now. No worries! Just run the program again when you're ready :)")
