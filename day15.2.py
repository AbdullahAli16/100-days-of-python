import time #Using time module 
stdtime= time.strftime('%H:%M:%S')

print("Welcome to the greeting program :)")
name= str(input("Enter your name: "))

# print("The time right now is: ",stdtime)
# hours= time.strftime('%H')
# minutes= time.strftime('%M')
# seconds= time.strftime('%S')
# print(hours,"Hours",minutes,"Minutes and",seconds, "Seconds")

if(stdtime>="00:00:00" and stdtime<="11:59:59"):
    print("Good Morning", name, ". I hope you have a great day :)")
elif(stdtime>="12:00:00" and stdtime<="15:59:59"):
    print("Good Afternoon", name, ". I hope you are having a great day :3")
elif(stdtime>="16:00:00" and stdtime<"19:59:59"):
    print("Good Evening", name, ". I hope you had a great day :-)")
elif(stdtime>="20:00:00" and stdtime<="23:59:59"):
    print("Good Night", name, ". I know that you are tired but be proud of youself because I'm proud of you ", name,  "<3")
else:
    print("Invalid time entered. Please run the program again.")
