# Day: 36(Exception Handling using try and except)

n= input("Enter a number: ")
print(f"This is the mutiplication table of {n}:")

try:
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n)*i}")

except:
    print("Hello")

#try and except are used to prevent the program from stopping at a specific point in case any error is encountered
# by using these keywords if an error occurs the program skips that section and executes the lines further present in the program 

# We can put the section of code where there is a possibility of an error and we can use the except keyword to 
# perform something else in case that error occured like in this case printing hello

# except Exception as e:           #this prints the error encountered in the terminal
    # print(e)
try:    
    x= int(input("Enter a number: "))
    list=[1,7,8]
    print(list[x])
except ValueError:
    print("The value entered is invalid") #you can also use multiple excepts to handle specific errors
except IndexError:
    print("The index is out of range")
    