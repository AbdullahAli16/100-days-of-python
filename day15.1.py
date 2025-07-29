#Day 14(Greeting program using (if else and user input))

print("Welcome to the greeting program :)")
name= str(input("Enter your name: "))
time= int(input(("Enter time (24-hour format): ")))


if(time>0 and time<=12):
    print("Good Morning", name, ". I hope you have a great day :)")
elif(time>12 and time<=16):
    print("Good Afternoon", name, ". I hope you are having a great day :3")
elif(time>16 and time<=20):
    print("Good Evening", name, ". I hope you had a great day :-)")
elif(time>20 and time<=24):
    print("Good Night", name, ". I know that you are tired but be proud of youself because I'm proud of you ", name,  "<3")
else:
    print("Invalid time entered. Please run the program again.")
    